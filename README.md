<p align="center">
  <img src="assets/logo.png" alt="Prometheus-Logo" style="width: 15%; display: block; margin: auto;">
</p>

<h1 align="center">🔥 Prometheus-Eval 🔥</h1>

<p align="center">
  ⚡ A repository for evaluating LLMs in generation tasks 🚀 ⚡ <br>
</p>


**Latest News** 🔥

- [2024/05] We release Prometheus 2 (7B & 8x7B) models!

  - **Prometheus 2 (8x7B)** is an open-source state-of-the-art evaluator language model!
    - Compared to Prometheus 1 (13B), Prometheus 2 (8x7B) shows improved evaluation performances & supports assessing in pairwise ranking (relative grading) formats as well!
    - It achieves a Pearson correlation of 0.6 to 0.7 with GPT-4-1106 on a 5-point Likert scale across multiple direct assessment benchmarks, including [VicunaBench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge/data/vicuna_bench), [MT-Bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge/data/mt_bench), and [FLASK](https://github.com/kaistAI/FLASK). 
    - It also scores a 72% to 85% agreement with human judgments across multiple pairwise ranking benchmarks, including [HHH Alignment](https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/hhh_alignment), [MT Bench Human Judgment](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments), and [Auto-J Eval](https://github.com/GAIR-NLP/auto-j/blob/main/data/test/testdata_pairwise.jsonl). 

  - **Prometheus 2 (7B)** is a lighter version of Prometheus 2 (8x7B) model with reasonable performances (outperforming Llama-2-70B \& on par with Mixtral-8x7B). 
    - It achieves at least 80% of the evaluation statistics or performances of Prometheus 2 (8x7B) 
    - It requires only 16 GB of VRAM, making it suitable for running on consumer GPUs.


## ⏩ Quick Start

*Note*: `prometheus-eval` library is currently in the beta stage. If you encounter any issues, please let us know by creating an issue on the repository.

Installation with pip:
```shell
pip install prometheus-eval
```

> **With `prometheus-eval`, evaluating *any* instruction and response pair is as simple as:**

```python
from prometheus_eval import PrometheusEval

judge = PrometheusEval(model_id="prometheus-eval/prometheus-7b-v2.0")

instruction = "What are the key components of a neural network?"
response_A = "Neurons, weights, and activation functions are the key components."
response_B = "Layers, nodes, and input data are the main components."
rubric = "Are the components accurately identified?"
reference_answer = "Neurons, weights, and activation functions are fundamental to neural networks."

feedback, score = judge.single_relative_grade(
    instruction=instruction,
    response_A=response_A,
    response_B=response_B,
    rubric=rubric,
    reference_answer=reference_answer
)
```

## 🤔 What is Prometheus-Eval?

**Prometheus-Eval**🔥 is a repository that provides a collection of tools for training, evaluating, and using language models specialized in evaluating other language models. The repository includes the following components:

1. The `prometheus-eval` Python package, which provides a simple interface for evaluating instruction-response pairs using Prometheus.
2. Collection of evaluation datasets for training and evaluating Prometheus models.
3. Scripts for training Prometheus models or fine-tuning on custom datasets.

### Prometheus 

**Prometheus**🔥 is a family of open-source language models specialized in evaluating other language models. By effectively simulating human judgments and proprietary LM-based evaluations, we aim to resolve the following issues:

* *Fairness*: Not relying on closed-source models for evaluations!

* *Controllability*: You don’t have to worry about GPT version updates or sending your private data to OpenAI by constructing internal evaluation pipelines

* *Affordability*: If you already have GPUs, it is free to use!

<p align="center">
<img align="center" alt="finegrained-eval" src="assets/finegrained_eval.png" width="550"/>
</p>


## 🚀 What's special about Prometheus?

Compared to the Prometheus 1 models, the Prometheus 2 models support both **direct assessment** (absolute grading) and **pairwise ranking** (relative grading). 

You could switch modes by providing a different input prompt format and system prompt.

Within the prompt, you should fill in the instruction, response(s), and score rubrics with your own data. Optionally, you could also add a reference answer which leads to better performance! Click on the appropriate sections below to expand the templates and see detailed examples of how to correctly format your input data. This will help ensure that the evaluations are accurate and reflect the true capabilities of the models being tested.


<p align="center">
<img align="center" alt="formats" src="assets/formats.png" width="700"/>
</p>

 
## 🏃 Running Prometheus-Eval

### Using the package `prometheus-eval`

The `prometheus-eval` package provides a simple interface for evaluating instruction-response pairs using Prometheus. The package includes the following methods:

- `absolute_grade`: Evaluates a single response based on a given instruction, reference answer, and score rubric. Outputs a score between 1 and 5.
- `relative_grade`: Evaluates two responses based on a given instruction and score rubric. Outputs 'A' or 'B' based on the better response.


### Using the weights from Huggingface Hub 🤗

If you prefer directly working with the weights uploaded in Huggingface Hub, you can directly download the model weights! 

```python
# Example code for transformers
# TBA
```

## 📚 Learn more

| Section | Description |
|-|-|
| [Documentation](docs/library.md) | WIP |
| [Custom Benchmark Evaluation](docs/custom_eval.md) | WIP |
| [Evaluation for Evaluator LMs](docs/eval_for_eval_lm.md) | WIP |
| [Training Prometheus](docs/train_prometheus.md) | WIP |
| [Collection of Prompts](docs/prompts.md) | WIP |


## 👏 Acknowledgements

The underlying codebase for training originates from Huggingface's [Alignment Handbook](https://github.com/huggingface/alignment-handbook) and [Super Mario Merging](https://github.com/martyn/safetensors-merge-supermario) repository. Also, for inference, it heavily utilizes the [vllm](https://github.com/vllm-project/vllm) and the [transformer](https://github.com/huggingface/transformers) library. Lastly, we referred to the [AlpacaEval](https://github.com/tatsu-lab/alpaca_eval) repository to write this README file. Huge thanks to all the contributors for these awesome repositories!! 🙌


## Citation

If you find our work useful, please consider citing our paper!

```bibtex
@misc{kim2024prometheus,
      title={Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models}, 
      author={Seungone Kim and Juyoung Suk and Shayne Longpre and Bill Yuchen Lin and Jamin Shin and Sean Welleck and Graham Neubig and Moontae Lee and Kyungjae Lee and Minjoon Seo},
      year={2024},
      eprint={2405.01535},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```