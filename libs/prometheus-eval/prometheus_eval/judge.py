from typing import Any, Dict, List, Tuple, Union

from fastchat.conversation import get_conv_template

from .prompts import (ABS_SYSTEM_PROMPT, ABSOLUTE_PROMPT_WO_REF,
                      REL_SYSTEM_PROMPT, RELATIVE_PROMPT_WO_REF)
from .utils import (batch_absolute_grade, batch_completions_with_retries,
                    batch_relative_grade)
from .vllm import VLLM, MockVLLM
import warnings


class PrometheusEval:
    def __init__(
        self,
        model_id: str = "prometheus-eval/prometheus-7b-v2.0",
        num_gpus: int = 1,
        download_dir: str = None,
        absolute_grade_template: str = ABSOLUTE_PROMPT_WO_REF,
        relative_grade_template: str = RELATIVE_PROMPT_WO_REF,
        is_test: bool = False,
    ):
        self.model_id = model_id
        self.num_gpus = num_gpus
        self.download_dir = download_dir
        if "###Reference Answer (Score 5):" not in absolute_grade_template:
            warnings.warn("Reference answer was not given in Absolute Grading mode. This might lead to nonoptimal performances.")
        if "###Reference Answer:" not in relative_grade_template:
            warnings.warn("Reference answer was not given in Relative Grading mode. This might lead to nonoptimal performances.")

        self.absolute_grade_template = absolute_grade_template
        self.relative_grade_template = relative_grade_template
        self.model = (
            VLLM(model_id, num_gpus=num_gpus, download_dir=download_dir)
            if not is_test
            else MockVLLM()
        )

    def _get_conversation_prompt(self, messages: List[Dict[str, str]]):
        """
        From filled prompt, convert it into llama-2 conversation prompt
        """
        conv = get_conv_template("mistral")

        for message in messages:
            if message["role"] == "system":
                conv.set_system_message(message["content"])
            elif message["role"] == "user":
                conv.append_message(conv.roles[0], message["content"])

        conv.append_message(conv.roles[1], None)
        prompt = conv.get_prompt()
        return prompt


    def single_absolute_grade(self, instruction: str, response: str, rubric: str, reference_answer: str|None) -> Tuple[str, int]:
        content = self.absolute_grade_template.format(
                instruction=instruction,
                response=response,
                score_rubric=rubric_,
                reference_answer=reference_answer
            )

        messages = [
            {"role": "user", "content": ABS_SYSTEM_PROMPT + "\n\n" + content},
        ]
        input_ = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

        feedbacks, scores = batch_completions_with_retries(
            self.model, [input_], mode="absolute", params=None
        )
        
        return feedbacks, scores

    def single_relative_grade(self, instruction: str, response_A: str, response_B: str, rubric: str, reference_answer: str|None) -> Tuple[str, int]:
        content = self.relative_grade_template.format(
            instruction=instruction,
            response_A=response_a,
            response_B=response_b,
            score_rubric=rubric_,
            reference_answer=reference_answer
        )

        messages = [
            {"role": "user", "content": REL_SYSTEM_PROMPT + "\n\n" + content},
        ]
        input_ = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

        feedbacks, scores = batch_completions_with_retries(
            self.model, [inputs], mode="relative", params=None
        )

        return feedbacks, scores

    def absolute_grade(
        self,
        *,
        data: List[Dict[str, str]],
        params: Dict[str, Any],
        rubric: List[str] | str,
        reference_answers: List[str] = None
    ) -> Tuple[List[str], List[int]]:
        """
        Grades a batch of responses absolutely based on the provided data.

        :param data: A list of dictionaries, each containing 'instruction' and 'response'.
        :param params: Parameters for the model completion requests.
        :return: A tuple containing lists of feedbacks and scores.
        """
        # Validate the input data format
        for entry in data:
            if (
                not isinstance(entry, dict)
                or "instruction" not in entry
                or "response" not in entry
            ):
                raise ValueError(
                    "Each entry in the data list must be a dictionary with 'instruction' and 'response' keys"
                )

        # If rubric is a list, assume its a entry-wise rubric
        if isinstance(rubric, list):
            if len(rubric) != len(data):
                raise ValueError("Length of rubric must match the length of data")
        else:
            rubric = [rubric] * len(data)

        # If reference answer is given, assume its a entry-wise reference answer
        if isinstance(reference_answers, list):
            if len(reference_answers) != len(data):
                raise ValueError(
                    "Length of reference_answers must match the length of data"
                )
        else:
            reference_answers = [None] * len(data)

        inputs = []
        for idx, entry in enumerate(data):
            instruction = entry["instruction"]
            response = entry["response"]
            rubric_ = rubric[idx]
            reference_answer = reference_answers[idx]

            content = self.absolute_grade_template.format(
                instruction=instruction,
                response=response,
                rubric=rubric_,
                reference_answer=reference_answer,
            )

            messages = [
                {"role": "system", "content": ABS_SYSTEM_PROMPT},
                {"role": "user", "content": content},
            ]
            input_ = self._get_conversation_prompt(messages)
            inputs.append(input_)

        # TODO: Ensure no parsing errors by running the batch_absolute_grade in the last run
        feedbacks, scores = batch_completions_with_retries(
            self.model,
            inputs,
            mode="absolute",
            params=params,
        )

        return feedbacks, scores

    def relative_grade(
        self,
        *,
        data: List[Dict[str, str]],
        params: Dict[str, Any],
        rubric: List[str] | str,
        reference_answers: List[str] = None
    ) -> Tuple[List[str], List[int]]:
        """
        Grades a batch of responses relatively based on the provided data.

        :param data: A list of dictionaries, each containing 'instruction', 'response_A', and 'response_B'.
        :param params: Additional parameters for the model completion requests.
        :return: A tuple containing lists of feedbacks and scores.
        """
        # Validate the input data format
        for entry in data:
            if (
                not isinstance(entry, dict)
                or "instruction" not in entry
                or "response_A" not in entry
                or "response_B" not in entry
            ):
                raise ValueError(
                    "Each entry in the data list must be a dictionary with 'instruction', 'response_A', and 'response_B' keys"
                )

        # If rubric is a list, assume its a entry-wise rubric
        if isinstance(rubric, list):
            if len(rubric) != len(data):
                raise ValueError("Length of rubric must match the length of data")
        else:
            rubric = [rubric] * len(data)

        # If reference answer is given, assume its a entry-wise reference answer
        if isinstance(reference_answers, list):
            if len(reference_answers) != len(data):
                raise ValueError(
                    "Length of reference_answers must match the length of data"
                )
        else:
            reference_answers = [None] * len(data)

        inputs = []
        for idx, entry in enumerate(data):
            instruction = entry["instruction"]
            response_a = entry["response_A"]
            response_b = entry["response_B"]
            rubric_ = rubric[idx]
            reference_answer = reference_answers[idx]

            # Formatting the input for the relative grading
            content = self.relative_grade_template.format(
                instruction=instruction,
                response_A=response_a,
                response_B=response_b,
                rubric=rubric_,
                reference_answer=reference_answer,
            )

            messages = [
                {"role": "system", "content": REL_SYSTEM_PROMPT},
                {"role": "user", "content": content},
            ]
            input_ = self._get_conversation_prompt(messages)
            inputs.append(input_)

        # TODO: Ensure no parsing errors by running the batch_absolute_grade in the last run
        feedbacks, scores = batch_completions_with_retries(
            self.model, inputs, mode="relative", params=params
        )

        return feedbacks, scores
