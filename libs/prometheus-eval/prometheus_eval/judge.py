from typing import List, Union, Dict, Any, Tuple
from .prompts import ABSOLUTE_PROMPT_WO_REF, RELATIVE_PROMPT_WO_REF, ABS_SYSTEM_PROMPT, REL_SYSTEM_PROMPT
from transformers import AutoTokenizer
from .vllm import VLLM
from .utils import batch_completions_with_retries, batch_absolute_grade, batch_relative_grade


class PrometheusEval:
    def __init__(self, model_id: str = "prometheus-eval/prometheus-7b-v2.0", num_gpus: int = 1, download_dir: str=None, absolute_grade_template: str = ABSOLUTE_PROMPT_WO_REF, relative_grade_template: str = RELATIVE_PROMPT_WO_REF):
        self.model_id = model_id
        self.num_gpus = num_gpus
        self.download_dir = download_dir
        self.model = VLLM(model_id, num_gpus=num_gpus, download_dir=download_dir)
        # TODO: Add warning message for not using reference answer
        self.absolute_grade_template = absolute_grade_template
        self.relative_grade_template = relative_grade_template
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    # TODO: Implement single absolute grade and relative grade

    def absolute_grade(self, data: List[Dict[str, str]],  params: Dict[str, Any], rubric: List[str]|str, reference_answers: List[str]|None) -> Tuple[List[str], List[int]]:
        """
        Grades a batch of responses absolutely based on the provided data.

        :param data: A list of dictionaries, each containing 'instruction' and 'response'.
        :param params: Parameters for the model completion requests.
        :return: A tuple containing lists of feedbacks and scores.
        """
        # Validate the input data format
        for entry in data:
            if not isinstance(entry, dict) or 'instruction' not in entry or 'response' not in entry:
                raise ValueError("Each entry in the data list must be a dictionary with 'instruction' and 'response' keys")
        
        
        # If rubric is a list, assume its a entry-wise rubric
        if isinstance(rubric, list):
            if len(rubric) != len(data):
                raise ValueError("Length of rubric must match the length of data")
        else:
            rubric = [rubric] * len(data)
        
        # If reference answer is given, assume its a entry-wise reference answer
        if isinstance(reference_answer, list):
            if len(reference_answer) != len(data):
                raise ValueError("Length of reference_answer must match the length of data")
        else:
            reference_answer = [None] * len(data)
        
        inputs = []
        for idx, entry in enumerate(data):
            instruction = entry["instruction"]
            response = entry["response"]
            rubric_ = rubric[idx]
            reference_answer = reference_answers[idx]
            
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
            inputs.append(input_)
        
        
        feedbacks, scores = batch_completions_with_retries(
                self.model, inputs, mode="absolute", params=params,
            )
        
        return feedbacks, scores

    def relative_grade(self, data: List[Dict[str, str]], params: Dict[str, Any], rubric: List[str]|str, reference_answers: List[str]|None) -> Tuple[List[str], List[int]]:
        """
        Grades a batch of responses relatively based on the provided data.

        :param data: A list of dictionaries, each containing 'instruction', 'response_A', and 'response_B'.
        :param params: Additional parameters for the model completion requests.
        :return: A tuple containing lists of feedbacks and scores.
        """
        # Validate the input data format
        for entry in data:
            if not isinstance(entry, dict) or 'instruction' not in entry or 'response_A' not in entry or 'response_B' not in entry:
                raise ValueError("Each entry in the data list must be a dictionary with 'instruction', 'response_A', and 'response_B' keys")
            
        # If rubric is a list, assume its a entry-wise rubric
        if isinstance(rubric, list):
            if len(rubric) != len(data):
                raise ValueError("Length of rubric must match the length of data")
        else:
            rubric = [rubric] * len(data)
        
        # If reference answer is given, assume its a entry-wise reference answer
        if isinstance(reference_answer, list):
            if len(reference_answer) != len(data):
                raise ValueError("Length of reference_answer must match the length of data")
        else:
            reference_answer = [None] * len(data)

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
                score_rubric=rubric_,
                reference_answer=reference_answer
            )

            messages = [
                {"role": "user", "content": REL_SYSTEM_PROMPT + "\n\n" + content},
            ]
            input_ = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            inputs.append(input_)

        feedbacks, scores = batch_completions_with_retries(
            self.model, inputs, mode="relative", params=params
        )

        return feedbacks, scores

