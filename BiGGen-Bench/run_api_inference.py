import argparse
import json
import os
from pathlib import Path

import pandas as pd
from datasets import load_dataset
from dotenv import load_dotenv

# Run `source init.sh` to correctly import prometheus_eval
import litellm
from prometheus_eval.litellm import LiteLLM, AsyncLiteLLM


def dummy_completions(inputs, **kwargs):
    return ["dummy output"] * len(inputs)


def apply_template_openai(record):
    message = [
        {"role": "system", "content": record["system_prompt"]},
        {"role": "user", "content": record["input"]},
    ]
    return message


def main(args):
    load_dotenv()

    model_name: str = args.model_name
    save_file_path: str = args.save_file_path
    batch_size: int = args.batch_size
    requests_per_minute: int = args.requests_per_minute

    model = LiteLLM(
        model_name, batch_size=batch_size, requests_per_minute=requests_per_minute
    )
    dataset: pd.DataFrame = load_dataset(
        "prometheus-eval/BiGGen-Bench", split="test"
    ).to_pandas()

    # records: Full data that has all the information of BiGGen-Bench
    # inputs: Inputs that will be fed to the model
    records = []
    inputs = []

    for row in dataset.iterrows():
        record = row[1]
        records.append(record.to_dict())
        inputs.append(apply_template_openai(record))

    params = {
        "max_tokens": 2048,
        "repetition_penalty": 1.03,
        "best_of": 1,
        "temperature": 1.0,
        "top_p": 0.9,
    }

    outputs = model.completions(inputs, **params)

    result = {}

    for record, output in zip(records, outputs):
        uid = record["id"]

        result[uid] = record.copy()
        result[uid]["response"] = output.strip()
        result[uid]["response_model_name"] = model_name

    save_file_path = Path(save_file_path)
    save_file_path.parent.mkdir(parents=True, exist_ok=True)

    with save_file_path.open("w", encoding="utf-8") as file:
        file.write(json.dumps(result, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run model inference.")
    parser.add_argument(
        "--model_name",
        type=str,
        required=True,
        help="Name of the model to evaluate. Has to be a valid litellm model name.",
    )
    parser.add_argument(
        "--save_file_path", type=str, required=True, help="Path to save the output file"
    )
    parser.add_argument(
        "--batch_size", type=int, default=100, help="Batch size for model inference"
    )
    parser.add_argument(
        "--requests_per_minute",
        type=int,
        default=100,
        help="Number of requests per minute for model inference",
    )

    args = parser.parse_args()

    main(args)
