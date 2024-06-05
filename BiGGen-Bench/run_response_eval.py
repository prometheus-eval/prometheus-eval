import argparse
import json
from pathlib import Path

import pandas as pd
from prometheus_eval import PrometheusEval
from prometheus_eval.litellm import AsyncLiteLLM, LiteLLM

# Run `source init.sh` to correctly import prometheus_eval
from prometheus_eval.mock import AsyncMockLLM, MockLLM
from prometheus_eval.prompts import ABSOLUTE_PROMPT, SCORE_RUBRIC_TEMPLATE
from prometheus_eval.vllm import VLLM
from transformers import AutoTokenizer

ABSOLLUTE_REFINE_PROMPT = """###Task Description:
An instruction (might include an Input inside it), a response to evaluate, a reference answer that gets a score of 5, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.
3. The output format should look as follows: "(write a feedback for criteria) [RESULT] (an integer number between 1 and 5)"
4. Please do not generate any other opening, closing, and explanations.
5. Don't get confused. You are conducting an absolute grading of another model's grading! For convenience, I will seperate the input and output of the other model's relative grading with "@@@"s.

@@@
###The instruction to evaluate:
{orig_instruction}
@@@

###Response to evaluate:
{orig_response}

###Reference Answer (Score 5):
{orig_reference_answer}

###Score Rubrics:
{score_rubric}

###Feedback: """


def read_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def init_eval():
    # records: Full data that has all the information of BiGGen-Bench
    records = []
    # necessary for PrometheusEval
    instructions = []
    responses = []
    reference_answers = []
    rubric = []
    return records, instructions, responses, reference_answers, rubric


def main(args):
    input_file_path = args.input_file_path
    output_file_path = args.output_file_path
    eval_model_name = args.model_name

    is_prometheus = False

    if eval_model_name in [
        "prometheus-eval/prometheus-7b-v2.0",
        "prometheus-eval/prometheus-8x7b-v2.0",
        "prometheus-eval/prometheus-8x7b-v2.0-bgb",
    ]:
        is_prometheus = True

    input_data = read_json(input_file_path)
    input_data_list = list(input_data.values())

    assert isinstance(input_data, dict), "Wrong input file data format"
    assert isinstance(input_data_list, list), "Wrong input file data format"
    assert isinstance(input_data_list[0], dict), "Wrong input file data format"
    assert len(input_data_list[0].keys()) == 10, "Wrong input file data format"

    records, instructions, responses, reference_answers, rubric = init_eval()
    records_2, instructions_2, responses_2, reference_answers_2, rubric_2 = init_eval()

    for instance_id, instance in input_data.items():
        record = instance

        if "llm_judge" in record["id"]:
            records_2.append(record)
            instructions_2.append(record["input"])
            responses_2.append(record["response"])
            reference_answers_2.append(record["reference_answer"])
            score_rubric = SCORE_RUBRIC_TEMPLATE.format(**record["score_rubric"])
            rubric_2.append(score_rubric)
        else:
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

    judge.absolute_grade_prompt = ABSOLLUTE_REFINE_PROMPT
    feedbacks_2, scores_2 = judge.absolute_grade(
        instructions=instructions_2,
        responses=responses_2,
        rubric=rubric_2,
        reference_answers=reference_answers_2,
    )

    # Extend the feedbacks and scores
    feedbacks.extend(feedbacks_2)
    scores.extend(scores_2)

    import pdb

    pdb.set_trace()

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
