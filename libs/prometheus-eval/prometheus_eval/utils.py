import random
import warnings
from typing import List

from tqdm import tqdm

from .vllm import VLLM


def _get_logprob_of_token(data, target_token):
    for key, value in data.items():
        if value.decoded_token.strip() == target_token:
            return value.logprob
    return None


def batch_absolute_grade(model: VLLM, inputs: List[str], params):
    """
    Batch grades responses using a VLLM model based on a grading rubric, assigning a score from 1 to 5 for each.

    :param model: The VLLM model instance to use for grading.
    :param inputs: A list of pre-formatted strings, each including the necessary information for grading.
    :param params: Parameters for the model completion requests.
    """
    feedback_results = model.completions(inputs, use_tqdm=True, **params)

    score_prompts = []
    for idx, feedback in enumerate(feedback_results):
        feedback_text = feedback.split("[RESULT]")[0].strip()
        for score in [1, 2, 3, 4, 5]:
            score_prompts.append(
                inputs[idx] + feedback_text + " [RESULT] " + str(score)
            )

    scoring_params = params.copy()
    scoring_params["max_tokens"] = 1
    scoring_params["prompt_logprobs"] = 1

    scoring_results = model.generate(score_prompts, use_tqdm=True, **scoring_params)

    # Process scoring results to find the best score for each feedback
    final_output = []
    for i in range(0, len(scoring_results), 5):
        batch = scoring_results[i : i + 5]
        prompt_logprobs_list = [result.prompt_logprobs for result in batch]

        log_probs = []
        for j in range(1, 6):
            log_prob = _get_logprob_of_token(prompt_logprobs_list[j - 1][-1], str(j))
            log_probs.append(log_prob)

        best_score_idx = log_probs.index(max(log_probs))
        final_output.append(batch[best_score_idx].prompt.split("[/INST]")[-1].strip())

    # Parse the final output to get the scores
    feedbacks = []
    scores = []
    for output in final_output:
        feedback, score = output.split("[RESULT]")
        feedbacks.append(feedback.strip())
        scores.append(int(score.strip()))

    assert len(inputs) == len(
        feedbacks
    ), f"Length of inputs ({len(inputs)}) does not match length of feedbacks ({len(feedbacks)})"
    assert len(inputs) == len(
        scores
    ), f"Length of inputs ({len(inputs)}) does not match length of scores ({len(scores)})"

    return feedbacks, scores


def batch_relative_grade(model: VLLM, inputs: List[str], params):
    """
    Batch grades responses using a VLLM model based on a grading rubric, assigning an alphabet A or B.

    :param model: The VLLM model instance to use for grading.
    :param inputs: A list of pre-formatted strings, each including the necessary information for grading.
    :param params: Parameters for the model completion requests.
    """

    feedback_results = model.completions(inputs, use_tqdm=True, **params)

    score_prompts = []
    for idx, feedback in enumerate(feedback_results):
        feedback_text = feedback.split("[RESULT]")[0].strip()
        for score in ["A", "B"]:
            score_prompts.append(
                inputs[idx] + feedback_text + " [RESULT] " + str(score)
            )

    scoring_params = params.copy()
    scoring_params["max_tokens"] = 1
    scoring_params["prompt_logprobs"] = 1

    scoring_results = model.generate(score_prompts, use_tqdm=True, **scoring_params)

    # Process scoring results to find the best score for each feedback
    final_output = []
    for i in range(0, len(scoring_results), 2):
        batch = scoring_results[i : i + 2]
        prompt_logprobs_list = [result.prompt_logprobs for result in batch]

        try:
            log_prob_a = _get_logprob_of_token(prompt_logprobs_list[0][-1], "A")
            log_prob_b = _get_logprob_of_token(prompt_logprobs_list[1][-1], "B")
        except:
            log_prob_a = random.random()
            log_prob_b = random.random()

        log_probs = [log_prob_a, log_prob_b]

        best_score_idx = log_probs.index(max(log_probs))
        final_output.append(batch[best_score_idx].prompt.split("[/INST]")[-1].strip())

    # Parse the final output to get the scores
    feedbacks = []
    scores = []
    for output in final_output:
        feedback, score = output.split("[RESULT]")
        feedbacks.append(feedback.strip())
        scores.append(score.strip())

    assert len(inputs) == len(
        feedbacks
    ), f"Length of inputs ({len(inputs)}) does not match length of feedbacks ({len(feedbacks)})"
    assert len(inputs) == len(
        scores
    ), f"Length of inputs ({len(inputs)}) does not match length of scores ({len(scores)})"

    return feedbacks, scores


def _parse_output(outputs, mode: str):
    parts = outputs.split("[RESULT]")
    if len(parts) == 2:
        feedback, result = parts[0].strip(), parts[1].strip()
        if mode == "absolute":
            if result.isdigit() and result in ["1", "2", "3", "4", "5"]:
                return feedback, int(result)
        elif mode == "relative":
            if result in ["A", "B"]:
                return feedback, result
    return None, None


def batch_completions_with_retries(
    model: VLLM,
    inputs,
    mode: str,
    max_retries: int = 10,
    params: dict = None,
):
    if params is None:
        params = {
            "max_tokens": 2048,
            "repetition_penalty": 1.03,
            "best_of": 1,
            "temperature": 1.0,
            "top_p": 0.9,
        }

    total_len = len(inputs)

    batched_outputs = model.completions(inputs, **params, use_tqdm=True)

    to_retry_inputs = []
    to_retry_indices = []
    for i, output in enumerate(batched_outputs):
        feedback, score = _parse_output(output, mode=mode)
        if feedback is None:
            to_retry_inputs.append(inputs[i])
            to_retry_indices.append(i)

    # Retry logic with progress bar
    retries = 0
    while to_retry_inputs and retries < max_retries:
        retries += 1
        print(f"Retrying failed batches: Attempt {retries}/{max_retries}")
        retry_outputs = model.completions(to_retry_inputs, **params, use_tqdm=True)

        new_to_retry_inputs = []
        new_to_retry_indices = []
        for idx, (retry_idx, output) in enumerate(zip(to_retry_indices, retry_outputs)):
            feedback, score = _parse_output(output, mode=mode)
            if feedback is None:  # Still failing
                new_to_retry_inputs.append(to_retry_inputs[idx])
                new_to_retry_indices.append(to_retry_indices[idx])
            else:
                batched_outputs[retry_idx] = output  # Update with successful retry

        to_retry_inputs = new_to_retry_inputs
        to_retry_indices = new_to_retry_indices

    outputs_len = len(batched_outputs)
    print(f"Processed {outputs_len}/{total_len} instances.")

    if outputs_len < total_len:
        warnings.warn("Some instances failed to generate feedback.")
        warnings.warn("They will be written as None in the output file.")

    feedbacks = []
    scores = []

    for output in tqdm(batched_outputs, desc="Finalizing"):
        feedback, score = _parse_output(output, mode=mode)
        if feedback is not None:
            feedbacks.append(feedback)
            scores.append(score)
        else:
            feedbacks.append("Failed to generate feedback")
            scores.append(None)

    return feedbacks, scores
