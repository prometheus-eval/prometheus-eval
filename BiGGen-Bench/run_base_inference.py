import argparse
import json
import os
import warnings
from pathlib import Path

import huggingface_hub
import pandas as pd
from datasets import load_dataset
from dotenv import dotenv_values, load_dotenv

# Run `source init.sh` to use local prometheus_eval
from prometheus_eval.mock import MockLLM
from prometheus_eval.vllm import VLLM
from transformers import AutoTokenizer
from urial_conversation import get_conv_template


def read_text(file_path):
    try:
        # Open the file in read mode
        with open(file_path, "r") as file:
            # Read the entire content of the file
            content = file.read()
        return content
    except FileNotFoundError:
        return "The file was not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


URIAL_PROMPTS = {
    "inst_1k_v4": read_text("urial_prompts/inst_1k_v4.txt"),
    "inst_1k_v4.help": read_text("urial_prompts/inst_1k_v4.help.txt"),
}


def apply_template_base(record):
    if record["capability"] == "safety":
        urial_version = "inst_1k_v4"
    else:
        urial_version = "inst_1k_v4.help"

    urial_prompt = URIAL_PROMPTS[urial_version]

    def map_to_conv(urial_version=None):
        if "inst_help_v5" in urial_version:
            conv = get_conv_template("urial_v5")
        elif "inst_help_v6" in urial_version:
            conv = get_conv_template("urial_v6")
        else:
            conv = get_conv_template("urial_backticks")
        conv.set_system_message(urial_prompt)
        return conv

    conv = map_to_conv(urial_version)
    conv.append_message(
        conv.roles[0], record["system_prompt"] + "\n\n" + record["input"]
    )
    conv.append_message(conv.roles[1], None)
    return conv.get_prompt()


def dummy_completions(inputs, **kwargs):
    return ["dummy output"] * len(inputs)


def main(args):
    model_name: str = args.model_name
    output_file_path: str = args.output_file_path

    dataset: pd.DataFrame = load_dataset(
        "prometheus-eval/BiGGen-Bench", split="test"
    ).to_pandas()

    # records: Full data that has all the information of BiGGen-Bench
    # inputs: Inputs that will be fed to the model
    records = []
    inputs = []

    for row in dataset.iterrows():
        record = row[1].to_dict()
        # Exclude multilingual tasks for base models
        if record["capability"] == "multilingual":
            continue
        records.append(record)
        inputs.append(apply_template_base(record))

    params = {
        "max_tokens": 2048,
        "repetition_penalty": 1.03,
        "best_of": 1,
        "temperature": 1.0,
        "top_p": 0.9,
        "use_tqdm": True,
    }

    if model_name.endswith("AWQ"):
        model = VLLM(model_name, tensor_parallel_size=1, quantization="AWQ")
    elif model_name.endswith("GPTQ"):
        model = VLLM(model_name, tensor_parallel_size=1, quantization="GPTQ")
    else:
        model = VLLM(model_name, tensor_parallel_size=1)

    outputs = model.completions(inputs, **params)

    if len(outputs) != 695:
        warnings.warn(f"Expected 765 outputs, got {len(outputs)}")

    result = {}

    for record, output in zip(records, outputs):
        uid = record["id"]

        result[uid] = record.copy()
        # Parsing the output for base models (because of urial prompts)
        result[uid]["response"] = output.split("```\n\n# Query:")[0].strip()
        result[uid]["response_model_name"] = model_name

    output_file_path = Path(output_file_path)
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    with output_file_path.open("w", encoding="utf-8") as file:
        file.write(json.dumps(result, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run model inference.")
    parser.add_argument(
        "--model_name",
        type=str,
        required=True,
        help="Name of the model to evaluate. Has to be a valid Hugging Face model name.",
    )
    parser.add_argument(
        "--output_file_path",
        type=str,
        required=True,
        help="Path to save the output response file",
    )

    hf_token = dotenv_values(".env").get("HF_TOKEN", None)
    if hf_token is not None:
        huggingface_hub.login(token=hf_token)

    args = parser.parse_args()

    main(args)
