import argparse
import json
import os
import random
from pathlib import Path

from transformers import AutoTokenizer

from src import CACHE_DIR
from src.llms.prometheus_utils import batch_completions_with_retries

# from eval.parser import parse_output
from src.llms.vllm_utils import VLLM
from src.load_utils import (
    BASE_PATH,
    RESPONSE_BASE_PATH,
    get_response_data_dict,
    load_json,
)
from src.model_list import get_all_model_list, get_model_type
from src.prompts import (
    ABS_REFINE_PROMPT,
    ABS_SYSTEM_PROMPT,
    ABSOLUTE_PROMPT,
    SCORE_RUBRIC_TEMPLATE,
    MT_BENCH_PROMPT,
    get_flask_rubric,
)


DEBUG = True

def prepare_inputs(tokenizer, records, model_name: str, is_refine=False, mode="bgb"):
    inputs = []

    for record in records:
        orig_response = record["response"]
        orig_instruction = record["input"]
        score_rubric = SCORE_RUBRIC_TEMPLATE.format(**record["score_rubric"]).strip()
        system_message = ABS_SYSTEM_PROMPT

        if mode == "bgb":
            if is_refine:
                content = ABS_REFINE_PROMPT.format(
                    orig_response=orig_response,
                    orig_instruction=orig_instruction,
                    score_rubric=score_rubric,
                    orig_reference_answer=record["reference_answer"],
                ).strip()
            else:
                    content = ABSOLUTE_PROMPT.format(
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
            flask_score_rubric = get_flask_rubric(record['capability'], record['task'])
            flask_score_rubric_str = SCORE_RUBRIC_TEMPLATE.format(**flask_score_rubric).strip()
            if is_refine:
                content = ABS_REFINE_PROMPT.format(
                    orig_response=orig_response,
                    orig_instruction=orig_instruction,
                    score_rubric=flask_score_rubric_str,
                    orig_reference_answer=record["reference_answer"],
                ).strip()
            else:
                content = ABSOLUTE_PROMPT.format(
                    orig_response=orig_response,
                    orig_instruction=orig_instruction,
                    score_rubric=flask_score_rubric_str,
                    orig_reference_answer=record["reference_answer"],
                ).strip()
        else:
            raise NotImplementedError(f"Mode {mode} not implemented")

        import pdb; pdb.set_trace()

        if "system" in tokenizer.chat_template:
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": content},
            ]
        else:
            messages = [
                {"role": "user", "content": system_message + "\n" + content},
            ]
        input_str = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs.append(input_str)

    return inputs


def main(eval_model_id: str, num_gpus: int, shuffle: bool, mode: str):
    assert eval_model_id in [
        "prometheus-eval/prometheus-7b-v2.0",
        "prometheus-eval/prometheus-8x7b-v2.0",
        "prometheus-eval/prometheus-8x7b-v2.0-bgb",
    ], "Model not supported as evaluation model"

    folder_name_dict = {
        "prometheus-eval/prometheus-7b-v2.0": "responses_prometheus_7b_eval",
        "prometheus-eval/prometheus-8x7b-v2.0": "responses_prometheus_8x7b_eval",
        "prometheus-eval/prometheus-8x7b-v2.0-bgb": "responses_prometheus_8x7b_bgb_eval",
    }
    folder_name = folder_name_dict[eval_model_id]
    
    assert mode in ["bgb", "mt-bench", "flask"]
    
    if mode != "bgb":
        folder_name = folder_name + "_" + mode

    debug = DEBUG

    all_models = get_all_model_list()

    tokenizer = AutoTokenizer.from_pretrained(eval_model_id, cache_dir=CACHE_DIR)
    
    if debug:
        model = None
    else:
        model = VLLM(eval_model_id, num_gpus=num_gpus, cache_dir=CACHE_DIR)
    

    if shuffle:
        random.shuffle(all_models)

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
        filtered_uids = []
        for uid in to_run_uids:
            if "llm_judge" not in uid:
                filtered_uids.append(uid)

        print("filtered_uids count: ", len(filtered_uids))
        print("\n")

        inputs = []
        for uid in filtered_uids:
            record = response_data_dict[uid]
            inputs.append(prepare_inputs(tokenizer, [record], eval_model_id, mode=mode)[0])

        feedbacks, scores = batch_completions_with_retries(
            model, inputs, mode="absolute", debug=debug
        )

        MULTI_RUN = True

        if MULTI_RUN:
            all_scores = [scores]
            for num_trial in range(1, 5):
                print(f"Trial {num_trial}")
                _, temp_scores = batch_completions_with_retries(
                    model, inputs, mode="absolute", debug=debug
                )
                all_scores.append(temp_scores)
            zipped_scores = list(zip(*all_scores))
            combined_scores = [list(score_group) for score_group in zipped_scores]
            assert len(combined_scores) == len(scores)
            scores = combined_scores

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
        "--reverse",
        action="store_true",
        help="Use system prompt during evaluation",
    )
    parser.add_argument(
        "--model_name",
        type=str,
        default="prometheus-eval/prometheus-8x7b-v2.0",
        help="Model name to use as evaluation model",
    )

    args = parser.parse_args()

    assert args.model_name in [
        "prometheus-eval/prometheus-7b-v2.0",
        "prometheus-eval/prometheus-8x7b-v2.0",
        "prometheus-eval/prometheus-8x7b-v2.0-bgb",
    ], "Model not supported as evaluation model"

    num_gpus = 2

    main(args.model_name, num_gpus, True, mode="flask")
