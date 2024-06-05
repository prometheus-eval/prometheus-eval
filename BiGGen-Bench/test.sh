#!/bin/bash

# python run_base_inference.py --model_name openai-community/gpt2 --output_file_path "dummy_responses.json"
python run_chat_inference.py --model_name openai-community/gpt2 --output_file_path "dummy_responses.json"
python run_response_eval.py --model_name prometheus-eval/prometheus-7b-v2.0 --input_file_path "dummy_responses.json" --output_file_path "dummy_evals.json"