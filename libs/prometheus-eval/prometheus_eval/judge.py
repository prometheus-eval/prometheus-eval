from typing import Any, Dict, List, Tuple, Union

from fastchat.conversation import get_conv_template

from .prompts import (
    ABS_SYSTEM_PROMPT,
    ABSOLUTE_PROMPT_WO_REF,
    REL_SYSTEM_PROMPT,
    RELATIVE_PROMPT_WO_REF,
)
from .utils import (
    batch_absolute_grade,
    batch_completions_with_retries,
    batch_relative_grade,
)
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
        is_test: bool = False,  # For debugging purposes
        dtype: str = "auto",
        **kwargs,
    ):
        self.model_id = model_id
        self.num_gpus = num_gpus
        self.download_dir = download_dir
        if "###Reference Answer (Score 5):" not in absolute_grade_template:
            warnings.warn(
                "Reference answer was not given in Absolute Grading mode. This might lead to nonoptimal performances."
            )
        if "###Reference Answer:" not in relative_grade_template:
            warnings.warn(
                "Reference answer was not given in Relative Grading mode. This might lead to nonoptimal performances."
            )

        self.absolute_grade_template = absolute_grade_template
        self.relative_grade_template = relative_grade_template
        self.model = (
            VLLM(
                model_id,
                num_gpus=num_gpus,
                download_dir=download_dir,
                dtype=dtype,
                **kwargs,
            )
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

    def single_absolute_grade(
        self,
        instruction: str,
        response: str,
        rubric: str,
        reference_answer: str = None,
        params: Dict[str, Any] = {},
    ) -> Tuple[str, int]:
        """
        Grades a single response absolutely based on the provided instruction and response.

        :param instruction: The instruction for the response.
        :param response: The response to grade.
        :param rubric: The rubric to use for grading.
        :param reference_answer: Optional reference answer to aid in grading.
        :param params: Additional parameters for the model completion requests.
        :return: A tuple containing the feedback and score.
        """
        feedbacks, scores = self.absolute_grade(
            instructions=[instruction],
            responses=[response],
            rubric=[rubric],
            reference_answers=[reference_answer] if reference_answer else [None],
            params=params,
        )
        return feedbacks[0], scores[0]

    def single_relative_grade(
        self,
        instruction: str,
        response_A: str,
        response_B: str,
        rubric: str,
        reference_answers: Tuple[str, str] = (None, None),
        params: Dict[str, Any] = {},
    ) -> Tuple[str, int]:
        """
        Grades two responses relatively based on a single instruction.

        :param instruction: The instruction for the paired responses.
        :param response_A: First response to compare.
        :param response_B: Second response to compare.
        :param rubric: The rubric to use for grading.
        :param reference_answers: Optional tuple of reference answers for each response.
        :param params: Additional parameters for the model completion requests.
        :return: A tuple containing the feedbacks and scores.
        """
        feedbacks, scores = self.relative_grade(
            instructions=[instruction],
            responses_A=[response_A],
            responses_B=[response_B],
            rubric=[rubric],
            reference_answers=list(reference_answers),
            params=params,
        )
        return feedbacks[0], scores[0]

    def absolute_grade(
        self,
        *,
        instructions: List[str],
        responses: List[str],
        params: Dict[str, Any],
        rubric: List[str] | str,
        reference_answers: List[str] = None,
    ) -> Tuple[List[str], List[int]]:
        """
        Grades a batch of responses absolutely based on the provided instructions and responses.

        :param instructions: List of instructions corresponding to each response.
        :param responses: List of responses to grade.
        :param params: Parameters for the model completion requests.
        :return: A tuple containing lists of feedbacks and scores.
        """
        if len(instructions) != len(responses):
            raise ValueError(
                "Length of instructions must match the length of responses"
            )

        # If rubric is a list, check its length matches the length of instructions
        if isinstance(rubric, list) and len(rubric) != len(instructions):
            raise ValueError("Length of rubric must match the length of instructions")
        else:
            rubric = [rubric] * len(
                instructions
            )  # Apply the same rubric to all if it's not a list

        # Handle reference answers
        if isinstance(reference_answers, list) and len(reference_answers) != len(
            instructions
        ):
            raise ValueError(
                "Length of reference answers must match the length of instructions"
            )
        else:
            reference_answers = [None] * len(
                instructions
            )  # Default to None if not provided

        inputs = []
        for idx, (instruction, response) in enumerate(zip(instructions, responses)):
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
        instructions: List[str],
        responses_A: List[str],
        responses_B: List[str],
        params: Dict[str, Any],
        rubric: List[str] | str,
        reference_answers: List[str] = None,
    ) -> Tuple[List[str], List[int]]:
        """
        Grades a batch of responses relatively based on the provided instructions and paired responses.

        :param instructions: List of instructions for each paired responses.
        :param responses_A: List of first responses in each pair.
        :param responses_B: List of second responses in each pair.
        :param params: Additional parameters for the model completion requests.
        :return: A tuple containing lists of feedbacks and scores.
        """
        if len(instructions) != len(responses_A) or len(responses_A) != len(
            responses_B
        ):
            raise ValueError(
                "Length of instructions, responses_A, and responses_B must all match"
            )

        # Handle rubric and reference answers similar to absolute_grade
        if isinstance(rubric, list) and len(rubric) != len(instructions):
            raise ValueError("Length of rubric must match the length of instructions")
        else:
            rubric = [rubric] * len(instructions)

        if isinstance(reference_answers, list) and len(reference_answers) != len(
            instructions
        ):
            raise ValueError(
                "Length of reference answers must match the length of instructions"
            )
        else:
            reference_answers = [None] * len(instructions)

        inputs = []
        for idx, (instruction, response_a, response_b) in enumerate(
            zip(instructions, responses_A, responses_B)
        ):
            rubric_ = rubric[idx]
            reference_answer = reference_answers[idx]
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

        feedbacks, scores = batch_completions_with_retries(
            self.model,
            inputs,
            mode="relative",
            params=params,
        )

        return feedbacks, scores
