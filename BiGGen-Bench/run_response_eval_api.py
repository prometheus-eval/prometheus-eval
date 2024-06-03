import argparse
import asyncio
import glob
import json
import os
import pickle
import warnings
from pathlib import Path

import tiktoken
from tqdm import tqdm

from src.data_loader import BiGGenBenchLoader
from src.llms.openai_utils import OpenAILLM
from src.llms.openrouter_utils import LiteLLM
from src.load_utils import (
    BASE_PATH,
    RESPONSE_BASE_PATH,
    get_response_data_dict,
    load_json,
)
from src.model_list import get_all_model_list, get_model_type, get_pretrained_models
from src.prompts import (
    ABS_REFINE_PROMPT_GPT4,
    ABS_SYSTEM_PROMPT,
    ABSOLUTE_PROMPT_GPT4,
    SCORE_RUBRIC_TEMPLATE,
    MT_BENCH_PROMPT,
    get_flask_rubric,
)

DEBUG = False
DUMMY = False


def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
    """Return the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
    }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = (
            4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        )
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model:
        # print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        # print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return num_tokens_from_messages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens


def save_checkpoint(state, path="temp_cache.pkl"):
    with open(path, "wb") as f:
        pickle.dump(state, f)


def load_checkpoint(path="temp_cache.pkl"):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    return None


async def dummy_async_completions(inputs, **kwargs):
    ["Hello. [RESULT] 5"] * len(inputs)
    await asyncio.sleep(1)
    return ["Hello. [RESULT] 5"] * len(inputs)


def parse_output(outputs):
    parts = outputs.split("[RESULT]")
    if len(parts) == 2:
        feedback, result = parts[0].strip(), parts[1].strip()
        if result.isdigit() and result in ["1", "2", "3", "4", "5"]:
            return feedback, int(result)
    return None, None


# Moddel inference (Use offline batching)
async def batch_completions_with_retries(
    model,
    inputs,
    params,
    batch_size,
    parse_output,
    max_retries=5,
):
    # DEBUG: Debugging purposes
    if DEBUG:
        inputs = inputs[:10]
    batched_outputs = []

    total_batches = len(inputs) // batch_size + (
        1 if len(inputs) % batch_size > 0 else 0
    )
    total_len = len(inputs)

    # Process initial batches with progress bar
    print("Processing initial batches...")
    for i in tqdm(
        range(0, len(inputs), batch_size), total=total_batches, desc="Initial Batches"
    ):
        batch_inputs = inputs[i : i + batch_size]
        if DUMMY:
            batch_outputs = await dummy_async_completions(batch_inputs, **params)
        else:
            batch_outputs = await model.completions(batch_inputs, **params)
        batched_outputs.extend(batch_outputs)

    # Identify failed instances and prepare for retries
    to_retry_inputs = []
    to_retry_indices = []
    for i, output in enumerate(batched_outputs):
        feedback, score = parse_output(output)
        if feedback is None:  # Parsing failed
            # DEBUG: Debugging purposes
            if DEBUG:
                print("Parsing failed: ", output)
                import pdb

                pdb.set_trace()
            to_retry_inputs.append(inputs[i])
            to_retry_indices.append(i)

    # Retry logic with progress bar
    retries = 0
    while to_retry_inputs and retries < max_retries:
        retries += 1
        print(f"Retrying failed batches: Attempt {retries}/{max_retries}")
        retry_outputs = []
        for i in tqdm(
            range(0, len(to_retry_inputs), batch_size), desc=f"Retry Attempt {retries}"
        ):
            batch_inputs = to_retry_inputs[i : i + batch_size]
            if DUMMY:
                batch_outputs = await dummy_async_completions(
                    batch_inputs, **params, use_tqdm=True
                )
            else:
                batch_outputs = await model.completions(batch_inputs, **params)

            assert len(batch_outputs) == len(batch_inputs)
            retry_outputs.extend(batch_outputs)

        new_to_retry_inputs = []
        new_to_retry_indices = []
        for idx, (retry_idx, output) in enumerate(zip(to_retry_indices, retry_outputs)):
            feedback, score = parse_output(output)
            if feedback is None:  # Still failing
                new_to_retry_inputs.append(to_retry_inputs[idx])
                new_to_retry_indices.append(to_retry_indices[idx])
            else:
                batched_outputs[retry_idx] = output  # Update with successful retry

        to_retry_inputs = new_to_retry_inputs
        to_retry_indices = new_to_retry_indices

    # Final aggregation and printing
    outputs_len = len(batched_outputs)
    print(f"Processed {outputs_len}/{total_len} instances.")

    if outputs_len < total_len:
        warnings.warn("Some instances failed to generate feedback.")
        warnings.warn("They will be written as None in the output file.")
        raise Exception(
            f"Failed to generate feedback for {total_len - outputs_len} instances."
        )

    feedbacks = []
    scores = []

    for output in tqdm(batched_outputs, desc="Finalizing"):
        feedback, score = parse_output(output)
        if feedback is not None:
            feedbacks.append(feedback)
            scores.append(score)
        else:
            # raise Exception(
            #     f"Parsing failed for output: {output}. Feedback: {feedback}, Score: {score}"
            # )
            feedbacks.append(None)
            scores.append(None)

    if DEBUG:
        print("Checking the results")
        print(*list(zip(feedbacks, scores))[:10])

    return feedbacks, scores


def prepare_inputs(
    tokenizer, records, model_name: str, is_refine=False, mode: str = "bgb"
):
    assert tokenizer is None

    inputs = []

    for record in records:
        orig_response = record["response"]
        orig_instruction = record["input"]
        score_rubric = SCORE_RUBRIC_TEMPLATE.format(**record["score_rubric"]).strip()
        system_message = ABS_SYSTEM_PROMPT

        if mode == "bgb":
            if is_refine:
                content = ABS_REFINE_PROMPT_GPT4.format(
                    orig_response=orig_response,
                    orig_instruction=orig_instruction,
                    score_rubric=score_rubric,
                    orig_reference_answer=record["reference_answer"],
                ).strip()
            else:
                content = ABSOLUTE_PROMPT_GPT4.format(
                    orig_response=orig_response,
                    orig_instruction=orig_instruction,
                    score_rubric=score_rubric,
                    orig_reference_answer=record["reference_answer"],
                ).strip()
        elif mode == "mt-bench":
            content = MT_BENCH_PROMPT.format(
                orig_response=orig_response,
                orig_instruction=orig_instruction,
                orig_reference_answer=record["reference_answer"],
            ).strip()
        elif mode == "flask":
            flask_score_rubric = get_flask_rubric(record["capability"], record["task"])
            flask_score_rubric_str = SCORE_RUBRIC_TEMPLATE.format(
                **flask_score_rubric
            ).strip()
            if is_refine:
                content = ABS_REFINE_PROMPT_GPT4.format(
                    orig_response=orig_response,
                    orig_instruction=orig_instruction,
                    score_rubric=flask_score_rubric_str,
                    orig_reference_answer=record["reference_answer"],
                ).strip()
            else:
                content = ABSOLUTE_PROMPT_GPT4.format(
                    orig_response=orig_response,
                    orig_instruction=orig_instruction,
                    score_rubric=flask_score_rubric_str,
                    orig_reference_answer=record["reference_answer"],
                ).strip()
        else:
            raise NotImplementedError(f"Mode {mode} not implemented")

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": content},
        ]
        inputs.append(messages)

    # random_inputs = random.sample(inputs, 3)
    # width = 20

    # for input_str in random_inputs:
    #     print("-" * width)
    #     print("Example inputs:")
    #     print(input_str)
    # print("-" * width)
    return inputs


async def main(model_name: str, rerun_invalid: bool = False, mode: str = "bgb"):
    if model_name == "gpt-4-1106-preview":
        folder_name = "responses_gpt4_eval"
        model = OpenAILLM(model_name)
    elif model_name == "gpt-4-turbo-2024-04-09":
        folder_name = "responses_gpt4_04_turbo_eval"
        # model = OpenAILLM(model_name)
        model = LiteLLM("openrouter/openai/gpt-4-turbo")
    elif model_name == "claude-3-opus-20240229":
        folder_name = "responses_claude_eval"
        model = LiteLLM("openrouter/anthropic/claude-3-opus:beta")

    assert mode in ["bgb", "mt-bench", "flask"]

    if mode != "bgb":
        folder_name = folder_name + "_" + mode

    all_models = get_all_model_list()

    for response_model_id in all_models:
        response_model_name = response_model_id.split("/")[-1]
        response_file_path = (
            Path(RESPONSE_BASE_PATH) / f"{response_model_name}_responses.json"
        )
        eval_file_path = (
            Path(BASE_PATH)
            / f"{folder_name}"
            / f"{response_model_name}_evaluation.json"
        )

        if mode != "bgb":
            if response_model_name not in [
                "Llama-2-13b-hf",
                "Mistral-7B-Instruct-v0.2",
                "Mixtral-8x7B-Instruct-v0.1",
                "gpt-3.5-turbo-0125",
            ]:
                continue

        print(f"Model: {response_model_name}")
        if os.path.exists(response_file_path):
            print("\tResponse file exists")
            response_data_dict = get_response_data_dict(response_model_name)
            data_cnt = len(response_data_dict.keys())
            print("\t\tData count: ", data_cnt)
        else:
            response_data_dict = {}
            print("\tResponse file does not exist")
            print("\tFirst generate response for this model and then run evaluate\n")
            continue

        if os.path.exists(eval_file_path):
            print("\tEvaluation file exists")
            eval_data_dict = load_json(eval_file_path)
            data_cnt = len(eval_data_dict.keys())
            print("\t\tData count: ", data_cnt)
        else:
            eval_data_dict = {}
            print("\tEvaluation file does not exist")

        to_run_uids = set(response_data_dict.keys()) - set(eval_data_dict.keys())

        # For invalid entries in eval_data_dict, add them to to_run_uids
        invalid_uids = []
        if rerun_invalid:
            for uid, record in eval_data_dict.items():
                if "feedback" not in record.keys() or record["feedback"] is None:
                    invalid_uids.append(uid)

                if (
                    "score" not in record.keys()
                    or not isinstance(record["score"], int)
                    or not 1 <= record["score"] <= 5
                ):
                    invalid_uids.append(uid)

        if len(invalid_uids) > 0:
            # import pdb; pdb.set_trace()
            pass

        to_run_uids.update(invalid_uids)

        filtered_uids = []
        for uid in to_run_uids:
            filtered_uids.append(uid)

        print("filtered_uids count: ", len(filtered_uids))
        print("\n")

        inputs = []
        for uid in filtered_uids:
            record = response_data_dict[uid]
            # import pdb; pdb.set_trace()
            if "llm_judge" in record["id"]:
                input_str = prepare_inputs(
                    None, [record], model_name, is_refine=True, mode=mode
                )[0]
            else:
                input_str = prepare_inputs(
                    None, [record], model_name, is_refine=False, mode=mode
                )[0]
            inputs.append(input_str)

        if len(inputs) > 0:
            # import pdb; pdb.set_trace()
            pass

        params = {
            "max_tokens": 2048,
            "n": 1,
            "temperature": 1.0,
            "top_p": 0.9,
        }

        batch_size = 100

        feedbacks, scores = await batch_completions_with_retries(
            model, inputs, params, batch_size, parse_output
        )

        for idx, uid in enumerate(filtered_uids):
            response_data_dict[uid].update(
                {"feedback": feedbacks[idx], "score": scores[idx]}
            )
            eval_data_dict[uid] = response_data_dict[uid]

        eval_file_path.parent.mkdir(parents=True, exist_ok=True)
        eval_data_dict = dict(sorted(eval_data_dict.items()))

        with eval_file_path.open("w", encoding="utf-8") as file:
            file.write(json.dumps(eval_data_dict, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run model inference.")
    parser.add_argument(
        "--model_name",
        type=str,
        default="gpt-4-turbo-2024-04-09",
        help="Name of the model to evaluate",
    )
    parser.add_argument(
        "--rerun_invalid",
        action="store_true",
        help="Rerun invalid entries in the evaluation file",
    )

    args = parser.parse_args()

    assert args.model_name in [
        "gpt-4-1106-preview",
        "gpt-4-turbo-2024-04-09",
        "claude-3-opus-20240229",
    ], "Model not supported"

    # asyncio.run(main(model_name, num_gpus, False))
    # asyncio.run(rerun_refinement(model_name, num_gpus))
    asyncio.run(main(args.model_name, args.rerun_invalid, mode="flask"))
