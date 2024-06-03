import random
import warnings
from typing import List

from tqdm import tqdm

from .vllm import VLLM


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
    if params is None or params == {}:
        params = {
            "max_tokens": 1024,
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
        warnings.warn("Try increasing `max_model_len` to avoid parsing failures.")

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
