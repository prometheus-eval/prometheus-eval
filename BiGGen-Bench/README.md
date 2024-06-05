# BiGGen-Bench

Documentation TBA


```bash
#!/bin/bash

# python run_base_inference.py --model_name openai-community/gpt2 --output_file_path "dummy_responses.json"
python run_chat_inference.py --model_name openai-community/gpt2 --output_file_path "dummy_responses.json"
CUDA_VISIBLE_DEVICES=7 python run_response_eval.py --model_name prometheus-eval/prometheus-7b-v2.0 --input_file_path "sample_responses.json" --output_file_path "sample-prometheus-7b_evals.json"

# Test on all the scripts

# Response models: meta-llama/Meta-Llama-3-8B, meta-llama/Meta-Llama-3-8B-Instruct, gpt-3.5-turbo
# Evaluation models: prometheus-eval/prometheus-bgb-8x7b-v2.0, gpt-4-turbo-2024-04-09

CUDA_VISIBLE_DEVICES=4 python run_base_inference.py --model_name meta-llama/Meta-Llama-3-8B --output_file_path "Meta-Llama-3-8B_responses.json"
CUDA_VISIBLE_DEVICES=5 python run_chat_inference.py --model_name meta-llama/Meta-Llama-3-8B-Instruct --output_file_path "Meta-Llama-3-8B-Instruct_responses.json"
CUDA_VISIBLE_DEVICES=6 python run_api_inference.py --model_name gpt-3.5-turbo --output_file_path "gpt-3.5-turbo_responses.json"
CUDA_VISIBLE_DEVICES=7 python run_response_eval.py --model_name gpt-4-turbo --input_file_path "gpt-3.5-turbo_responses.json" --output_file_path "gpt-3.5-turbo-graded-by-gpt-4-turbo_evals.json"
```