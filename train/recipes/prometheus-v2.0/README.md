
# Instructions to Replicate Prometheus-v2.0

This document provides instructions to replicate the Prometheus-v2.0 models. The Prometheus-v2.0 models are made by training absolute and relative grading expert models, and then merging them. 

Running the following commands will train the Prometheus-v2.0 models. Make sure to execute these commands in `prometheus-eval/train/recipes/prometheus-v2.0` and to have required environment set up before running the commands. 

## Prometheus-7B-v2.0 training examples

```shell
# Step 1 - Prepare Dataset
python prepare_dataset.py

# Step 2 - Train absolute grading expert model
ACCELERATE_LOG_LEVEL=info accelerate launch --config_file recipes/accelerate_configs/deepspeed_zero3.yaml scripts/run_sft.py recipes/prometheus-v2.0/sft/config_full_1.yaml

# Step 3 - Train relative grading expert model
ACCELERATE_LOG_LEVEL=info accelerate launch --config_file recipes/accelerate_configs/deepspeed_zero3.yaml scripts/run_sft.py recipes/prometheus-v2.0/sft/config_full_2.yaml

# Step 4 - Merge the two expert models to get the final model
# Read the instruction below.
```

- For merging the two expert 7B models, we utilized [LazyMergekit.ipynb](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing), which facilitates easy merging between multiple models and also supports uploading to the Hugging Face Hub. Special thanks to Maxime Labonne for releasing such a useful notebook!
- We used the mergekit argument below.

```
models:
  - model: PATH_TO_YOUR_ABSOLUTE_GRADING_MODEL
    parameters:
      weight: 1.0
  - model: PATH_TO_YOUR_ABSOLUTE_GRADING_MODEL
    parameters:
      weight: 1.0
merge_method: linear
dtype: bfloat16
```

## Prometheus-8x7B-v2.0 training examples

```shell
# Step 1 - Prepare Dataset
python prepare_dataset.py

# Step 2 - Train absolute grading expert model with LoRA
ACCELERATE_LOG_LEVEL=info accelerate launch --config_file recipes/accelerate_configs/deepspeed_zero3.yaml scripts/run_sft.py recipes/prometheus-v2.0/sft/config_full_10.yaml

# Step 3 - Train relative grading expert model with LoRA
ACCELERATE_LOG_LEVEL=info accelerate launch --config_file recipes/accelerate_configs/deepspeed_zero3.yaml  scripts/run_sft.py recipes/prometheus-v2.0/sft/config_full_11.yaml

# Step 4 - Merge LoRA adapters
python -m merge_adapter --base_model_path "mistralai/Mixtral-8x7B-Instruct-v0.1" --target_model_path ABSOLUTE_OUTPUT_PATH --adapter_path YOUR_ABSOLUTE_MODEL_ADAPTER

python -m push_to_hub --target_model_path ABSOLUTE_OUTPUT_PATH --hf_token YOUR_HF_TOKEN --repo_id HF_REPO_ID

python -m merge_adapter --base_model_path "mistralai/Mixtral-8x7B-Instruct-v0.1" --target_model_path RELATIVE_OUTPUT_PATH --adapter_path YOUR_RELATIVE_MODEL_ADAPTER

python -m push_to_hub --target_model_path RELATIVE_OUTPUT_PATH --hf_token YOUR_HF_TOKEN --repo_id HF_REPO_ID


# Step 5 - Merge the two expert models to get the final model
# Read the instruction below.
```

- Due to the size of the models, we couln't use LazyMergekit in free Colab instance. We used [safetensor-merge-supermario](https://github.com/martyn/safetensors-merge-supermario) for merging two 8x7B models.

```shell
git clone https://github.com/martyn/safetensors-merge-supermario.git
cd safetensors-merge-supermario

# Create mergelist.txt and add the content
echo "mistralai/Mixtral-8x7B-Instruct-v0.1" > mergelist.txt
echo "ABSOLUTE_GRADING_MODEL" >> mergelist.txt
echo "RELATIVE_GRADING_MODEL" >> mergelist.txt

# Now run the Python script with the mergelist.txt
python hf_merge.py mergelist.txt OUTPUT_PATH -p 0.1 -lambda 1.95
```