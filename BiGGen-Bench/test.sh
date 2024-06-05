#!/bin/bash

python run_base_inference.py --model_name openai-community/gpt2 --output_file_path "dummy.json"
python run_response_eval.py --model_name prometheus-eval/prometheus-7b-v2.0 --input_file_path "dummy.json" --output_file_path "dummy_output.json"