import argparse
from pathlib import Path

from transformers import AutoTokenizer
import pandas as pd
import json

# Run `source init.sh` to correctly import prometheus_eval
from prometheus_eval.mock import MockLLM, AsyncMockLLM
from prometheus_eval.vllm import VLLM
from prometheus_eval.prompts import SCORE_RUBRIC_TEMPLATE, ABSOLUTE_PROMPT
from prometheus_eval import PrometheusEval


def read_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def main(args):
    input_file_path = args.input_file_path
    output_file_path = args.output_file_path
    eval_model_name = args.model_name
    eval_model_id = eval_model_name

    assert eval_model_name in [
        "prometheus-eval/prometheus-7b-v2.0",
        "prometheus-eval/prometheus-8x7b-v2.0",
        "prometheus-eval/prometheus-8x7b-v2.0-bgb",
    ], "Model not officially supported as an evaluation model"

    input_data = read_json(input_file_path)
    input_data_list = list(input_data.values())

    assert isinstance(input_data, dict), "Wrong input file data format"
    assert isinstance(input_data_list, list), "Wrong input file data format"
    assert isinstance(input_data_list[0], dict), "Wrong input file data format"
    assert len(input_data_list[0].keys()) == 10, "Wrong input file data format"

    # records: Full data that has all the information of BiGGen-Bench
    records = []
    # necessary for PrometheusEval
    instructions = []
    responses = []
    reference_answers = []
    rubric = []

    # TODO: Use different grading template for llm judge tasks
    for instance_id, instance in input_data.items():
        record = instance
        records.append(record)
        instructions.append(record["input"])
        responses.append(record["response"])
        reference_answers.append(record["reference_answer"])
        score_rubric = SCORE_RUBRIC_TEMPLATE.format(**record["score_rubric"])
        rubric.append(score_rubric)

    # model = MockLLM(mode="absolute")
    model = AsyncMockLLM(mode="absolute")
    # model = VLLM(eval_model_name)
    judge = PrometheusEval(model=model, absolute_grade_template=ABSOLUTE_PROMPT)

    feedbacks, scores = judge.absolute_grade(
        instructions=instructions,
        responses=responses,
        rubric=rubric,
        reference_answers=reference_answers,
    )

    result = {}

    for record, output in zip(records, zip(feedbacks, scores)):
        instance_id = record["id"]

        result[instance_id] = record.copy()
        result[instance_id]["feedback"] = output[0]
        result[instance_id]["score"] = output[1]
        result[instance_id]["eval_model_name"] = eval_model_name

    output_file_path = Path(output_file_path)
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    with output_file_path.open("w", encoding="utf-8") as file:
        file.write(json.dumps(result, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run model inference.")
    parser.add_argument(
        "--model_name",
        type=str,
        default="prometheus-eval/prometheus-7b-v2.0",
        help="Model name to use as evaluation model",
    )
    parser.add_argument(
        "--input_file_path",
        type=str,
        required=True,
        help="Path to the input response file",
    )
    parser.add_argument(
        "--output_file_path",
        type=str,
        required=True,
        help="Path to save the output feedback file",
    )

    args = parser.parse_args()

    main(args)
