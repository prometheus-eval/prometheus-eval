import argparse
import json
import os
import random
from pathlib import Path

from transformers import AutoTokenizer

# Run `source init.sh` to correctly import prometheus_eval
from prometheus_eval.vllm import VLLM
from prometheus_eval import PrometheusEval


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

    tokenizer = AutoTokenizer.from_pretrained(eval_model_id)
    
    import pdb; pdb.set_trace()


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
