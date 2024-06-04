import argparse
import json
import os
from pathlib import Path

from datasets import load_dataset
from dotenv import dotenv_values
from prometheus_eval.vllm import VLLM
from transformers import AutoTokenizer

# from ..libs.prometheus_eval.prometheus_eval.vllm import VLLM


def apply_template_hf(tokenizer, records: list, model_name: str):
    inputs = []

    for record in records:
        if tokenizer.chat_template is not None and "system" in tokenizer.chat_template:
            messages = [
                {"role": "system", "content": record["system_prompt"]},
                {"role": "user", "content": record["input"]},
            ]
        else:
            messages = [
                {
                    "role": "user",
                    "content": record["system_prompt"] + "\n\n" + record["input"],
                }
            ]

        input_str = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs.append(input_str)
    return inputs


def dummy_completions(inputs, **kwargs):
    return ["dummy output"] * len(inputs)


def prepare_inputs(tokenizer, records, model_name: str):
    inputs = apply_template_hf(tokenizer, records, model_name)
    return inputs


def main(args):
    model_name = args.model_name
    save_file_path = args.save_file_path

    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    dataset = load_dataset("prometheus-eval/BiGGen-Bench")

    import pdb

    pdb.set_trace()

    inputs = []
    inputs.append(
        prepare_inputs(tokenizer, [record], model_id, urial_prompts=urial_prompts)[0]
    )

    params = {
        "max_tokens": 2048,
        "repetition_penalty": 1.03,
        "best_of": 1,
        "temperature": 1.0,
        "top_p": 0.9,
    }

    if "awq" in model_id.lower():
        model = VLLM(
            model_id, num_gpus=num_gpus, cache_dir=CACHE_DIR, quantization="AWQ"
        )
    elif "gptq" in model_id.lower():
        model = VLLM(
            model_id, num_gpus=num_gpus, cache_dir=CACHE_DIR, quantization="GPTQ"
        )
    else:
        model = VLLM(model_id, num_gpus=num_gpus, cache_dir=CACHE_DIR)

    outputs = model.completions(inputs, **params, use_tqdm=True)
    for idx, output in enumerate(outputs):
        if output == "":
            outputs[idx] = "Too long input."

    # Parsing the output for base models (because of urial prompts)
    if response_model_type == "base":
        for idx, output in enumerate(outputs):
            outputs[idx] = outputs[idx].split("```\n\n# Query:")[0].strip()

    for idx, uid in enumerate(filtered_uids):
        response_data_dict[uid] = {
            "capability": full_data_dict[uid]["capability"],
            "task": full_data_dict[uid]["task"],
            "response": outputs[idx].strip(),
        }

    response_output_dict = {}
    for key, val in response_data_dict.items():
        response_output_dict[key] = {
            "capability": val["capability"],
            "task": val["task"],
            "response": val["response"].strip(),
        }

    response_file_path.parent.mkdir(parents=True, exist_ok=True)
    response_output_dict = dict(sorted(response_output_dict.items()))

    with response_file_path.open("w", encoding="utf-8") as file:
        file.write(json.dumps(response_output_dict, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run model inference.")
    parser.add_argument(
        "--model_name", type=str, required=True, help="Name of the model to evaluate"
    )
    parser.add_argument(
        "--save_file_path", type=str, required=True, help="Path to save the output file"
    )
    args = parser.parse_args()

    main(args)
