---
layout: default
title: API Reference
nav_order: 4
has_children: false
---

## 4. API Reference

This section provides detailed information about the classes, methods, and functions available in the PrometheusEval package.

### 4.1. PrometheusEval

The `PrometheusEval` class is the main entry point for using the package. It provides methods for absolute and relative grading of responses.

#### 4.1.1. Initialization

To initialize the `PrometheusEval` class, you need to provide the following parameters:

- `model_id` (str): The ID of the model to use for grading (default: "prometheus-eval/prometheus-7b-v2.0").
- `num_gpus` (int): The number of GPUs to use for inference (default: 1).
- `download_dir` (str): The directory to download the model files (default: None).
- `absolute_grade_template` (str): The template for absolute grading (default: ABSOLUTE_PROMPT_WO_REF).
- `relative_grade_template` (str): The template for relative grading (default: RELATIVE_PROMPT_WO_REF).
- `is_test` (bool): Whether to use a mock model for testing purposes (default: False).
- `dtype` (str): The data type to use for inference (default: "auto").
- `**kwargs`: Additional keyword arguments to pass to the underlying language model.

Example:
```python
from prometheus_eval import PrometheusEval

judge = PrometheusEval(model_id="prometheus-eval/prometheus-7b-v2.0", num_gpus=1)
```

#### 4.1.2. Methods

The `PrometheusEval` class provides the following methods:

- `single_absolute_grade(instruction, response, rubric, reference_answer=None, params={})`: Grades a single response absolutely based on the provided instruction, response, rubric, and optional reference answer.
  - Returns a tuple containing the feedback (str) and score (int).

- `single_relative_grade(instruction, response_A, response_B, rubric, reference_answer=None, params={})`: Grades two responses relatively based on a single instruction, rubric, and optional reference answer.
  - Returns a tuple containing the feedback (str) and score (int).

- `absolute_grade(instructions, responses, params, rubric, reference_answers=None)`: Grades a batch of responses absolutely based on the provided instructions, responses, parameters, rubric, and optional reference answers.
  - Returns a tuple containing lists of feedbacks (List[str]) and scores (List[int]).

- `relative_grade(instructions, responses_A, responses_B, params, rubric, reference_answers=None)`: Grades a batch of responses relatively based on the provided instructions, paired responses, parameters, rubric, and optional reference answers.
  - Returns a tuple containing lists of feedbacks (List[str]) and scores (List[int]).

### 4.2. Prompts

The `prompts` module contains templates for absolute and relative grading, as well as score rubric templates.

#### 4.2.1. Absolute Grading Templates

- `ABSOLUTE_PROMPT`: The template for absolute grading with a reference answer.
- `ABSOLUTE_PROMPT_WO_REF`: The template for absolute grading without a reference answer.

#### 4.2.2. Relative Grading Templates

- `RELATIVE_PROMPT`: The template for relative grading with a reference answer.
- `RELATIVE_PROMPT_WO_REF`: The template for relative grading without a reference answer.

#### 4.2.3. Score Rubric Templates

- `SCORE_RUBRIC_TEMPLATE`: The template for defining score rubrics.
- `HELPFULNESS_RUBRIC`: A predefined rubric for evaluating the helpfulness of responses.
- `HARMLESSNESS_RUBRIC`: A predefined rubric for evaluating the harmlessness of responses.
- `HONESTY_RUBRIC`: A predefined rubric for evaluating the honesty of responses.
- `FACTUAL_VALIDITY_RUBRIC`: A predefined rubric for evaluating the factual validity of responses.
- `REASONING_RUBRIC`: A predefined rubric for evaluating the reasoning in responses.


#### 4.2.4. Utility Functions

- `get_prompt_template(grading_format, include_reference)`: Get the prompt template based on grading format and whether to include a reference answer.
  - `grading_format` (str): The grading format, either 'absolute' or 'relative'.
  - `include_reference` (bool): Whether to include a reference answer.
  - Returns the appropriate prompt template (str).

- `load_rubric(criteria, grading_format)`: Load the score rubric based on the provided criteria and grading format.
  - `criteria` (str): The criteria for which the score rubric is being loaded. Supported values: 'helpfulness', 'harmlessness', 'honesty', 'factual_validity', 'reasoning'.
  - `grading_format` (str): The grading format, either 'absolute' or 'relative'.
  - Returns the appropriate score rubric (str).

Example usage of `get_prompt_template`:
```python
from prometheus_eval.prompts import get_prompt_template

absolute_prompt = get_prompt_template(grading_format='absolute', include_reference=True)
relative_prompt = get_prompt_template(grading_format='relative', include_reference=False)
```

Example usage of `load_rubric`:
```python
from prometheus_eval.prompts import load_rubric

helpfulness_rubric = load_rubric(criteria='helpfulness', grading_format='absolute')
harmlessness_rubric = load_rubric(criteria='harmlessness', grading_format='relative')
```

These utility functions in the `prompts` module provide convenient ways to load appropriate prompt templates and score rubrics based on the grading format and criteria.

The `get_prompt_template` function takes the `grading_format` ('absolute' or 'relative') and a boolean `include_reference` to determine which prompt template to return. It allows you to easily select the desired prompt template for absolute or relative grading, with or without a reference answer.

The `load_rubric` function takes the `criteria` (e.g., 'helpfulness', 'harmlessness', etc.) and the `grading_format` ('absolute' or 'relative') to load the corresponding score rubric. It provides a simple way to access predefined rubrics for common evaluation criteria.

These functions enhance the flexibility and usability of the PrometheusEval package by allowing users to easily retrieve the appropriate prompt templates and score rubrics based on their specific grading requirements.

### 4.3. Utils

The `utils` module contains utility functions for batch processing and output parsing. It is used inside the `PrometheusEval` class.

#### 4.3.1. Batch Processing Functions

- `batch_completions_with_retries(model, inputs, mode, max_retries=10, params=None)`: Performs batch completions with retries for failed instances.


These are the main components of the PrometheusEval package API. For more detailed information about each class, method, and function, please refer to the docstrings and type annotations in the source code.