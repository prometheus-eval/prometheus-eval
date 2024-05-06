
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

- For merging the two expert 7B models, we utilized [LazyMergekit.ipynb](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing), which allows easy merge between multiple models and also supports uploading to Huggingface Hub. Special thanks to Maxime Labonne for releasing such a useful notebook!
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
# TBA

# Step 5 - Merge the two expert models to get the final model
# TBA
```
