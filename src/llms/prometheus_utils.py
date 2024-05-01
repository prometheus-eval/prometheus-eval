import random
from typing import List

from src.llms.vllm_utils import VLLM


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
