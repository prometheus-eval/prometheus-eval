---
layout: default
title: Advanced Usage
nav_order: 5
has_children: false
---

# 5. Advanced Usage

This section covers more advanced topics and customization options for using the PrometheusEval package.

## 5.1. Customizing Prompts

PrometheusEval allows you to customize the prompts used for absolute and relative grading. You can modify the existing prompt templates or create your own templates to suit your specific evaluation criteria and requirements.

To customize a prompt template, you can either:
1. Modify the existing prompt templates in the `prompts` module directly.
2. Create a new prompt template string and pass it to the `PrometheusEval` class during initialization using the `absolute_grade_template` or `relative_grade_template` parameters.

Example:
```python
custom_absolute_prompt = """
Your custom absolute grading prompt template here...
"""

judge = PrometheusEval(model_id="prometheus-eval/prometheus-7b-v2.0", absolute_grade_template=custom_absolute_prompt)
```

When customizing prompts, make sure to include the necessary placeholders for variables such as `{instruction}`, `{response}`, `{rubric}`, and `{reference_answer}` (if applicable) in your template.

## 5.2. Defining Custom Rubrics

In addition to using the predefined rubrics provided by the package, you can define your own custom rubrics for evaluation. Custom rubrics allow you to specify the criteria and scoring descriptions tailored to your specific use case.

PrometheusEval supports both global rubrics and instance-wise rubrics:

- Global rubrics: A single rubric string that is applied to all instances in a batch.
- Instance-wise rubrics: A list of rubric strings, where each rubric corresponds to a specific instance in a batch.


To define a custom rubric, you can create a rubric string using the `SCORE_RUBRIC_TEMPLATE` and provide the necessary criteria and score descriptions.

Example of a global rubric:
```python
from prometheus_eval.prompts import SCORE_RUBRIC_TEMPLATE

custom_rubric_data = {
    "criteria": "Your custom criteria description",
    "score1_description": "Description for score 1",
    "score2_description": "Description for score 2",
    "score3_description": "Description for score 3",
    "score4_description": "Description for score 4",
    "score5_description": "Description for score 5"
}

custom_rubric = SCORE_RUBRIC_TEMPLATE.format(**custom_rubric_data)
```

You can then use the custom rubric in the `single_absolute_grade`, `single_relative_grade`, `absolute_grade`, or `relative_grade` methods of the `PrometheusEval` class.


Example of instance-wise rubrics:
```python
custom_rubric_1 = "..."  # Rubric string for instance 1
custom_rubric_2 = "..."  # Rubric string for instance 2
custom_rubric_3 = "..."  # Rubric string for instance 3

instance_wise_rubrics = [custom_rubric_1, custom_rubric_2, custom_rubric_3]
```

When using instance-wise rubrics, ensure that the number of rubric strings in the list matches the number of instances being evaluated.

You can then use the custom rubric or instance-wise rubrics in the `single_absolute_grade`, `single_relative_grade`, `absolute_grade`, or `relative_grade` methods of the `PrometheusEval` class.

Example usage with instance-wise rubrics:
```python
instructions = [...]  # List of instructions
responses = [...]  # List of responses
reference_answers = [...]  # List of reference answers (optional)
instance_wise_rubrics = [...]  # List of rubric strings for each instance

feedbacks, scores = judge.absolute_grade(
    instructions=instructions,
    responses=responses,
    params={},
    rubric=instance_wise_rubrics,
    reference_answers=reference_answers
)
```

By supporting both global and instance-wise rubrics, PrometheusEval provides flexibility in defining evaluation criteria specific to each instance or applying a common rubric across all instances in a batch.

## 5.3. Handling Large Datasets

When working with large datasets, you can leverage the batch processing capabilities of PrometheusEval to efficiently evaluate multiple responses simultaneously.

The `absolute_grade` and `relative_grade` methods of the `PrometheusEval` class allow you to pass lists of instructions, responses, and reference answers to grade a batch of responses in a single call.

Example:
```python
instructions = [...]  # List of instructions
responses = [...]  # List of responses
reference_answers = [...]  # List of reference answers (optional)
rubric = "..."  # Rubric string

feedbacks, scores = judge.absolute_grade(
    instructions=instructions,
    responses=responses,
    params={},
    rubric=rubric,
    reference_answers=reference_answers
)
```

By grading responses in batches, you can significantly reduce the overall processing time compared to grading each response individually.