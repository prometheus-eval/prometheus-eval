"""
This script produces completions for roughly any AutoModelForCausalLM.
"""

from typing import List

import torch
from vllm import LLM, SamplingParams

from src import CACHE_DIR


class VLLM:
    def __init__(
        self,
        name,
        tokenizer_name=None,
        tokenizer_revision=None,
        num_gpus=1,
        cache_dir=CACHE_DIR,
        enable_lora=False,
    ):
        dtype = "float16"
        if torch.cuda.is_bf16_supported():
            dtype = "bfloat16"

        self.name = name

        max_model_len = None
        gpu_memory_utilization = 0.9

        if "prometheus" in self.name:
            # For ratio experiments
            max_model_len = 4900
            gpu_memory_utilization = 0.8

        # gpu_memory_utilization = 0.8
        # if "autoj" in self.name:
        #     max_model_len = 7000
        #     gpu_memory_utilization = 0.85
        # elif "meta-llama" in self.name or "prometheus-v1.0" in self.name:
        #     max_model_len = 4096
        #     if "70b" in self.name:
        #         gpu_memory_utilization = 0.85
        #     else:
        #         gpu_memory_utilization = 0.85
        # elif "mixtral" in self.name or "Mixtral" in self.name:
        #     max_model_len = 7000
        #     gpu_memory_utilization = 0.85
        # elif "prometheus" in self.name:
        #     # max_model_len = 7000
        #     gpu_memory_utilization = 0.85
        # else:
        #     max_model_len = None  # Let vllm automatically bring the max model length

        self.model = LLM(
            model=self.name,
            tokenizer=tokenizer_name,
            dtype=dtype,
            max_model_len=max_model_len,
            tokenizer_revision=tokenizer_revision,
            trust_remote_code=True,
            tensor_parallel_size=num_gpus,
            gpu_memory_utilization=gpu_memory_utilization,
            download_dir=cache_dir,
        )

    def completions(
        self,
        prompts: List[str],
        use_tqdm=False,
        **kwargs,
    ):
        prompts = [prompt.strip() for prompt in prompts]
        params = SamplingParams(**kwargs)
        outputs = self.model.generate(prompts, params, use_tqdm=use_tqdm)
        outputs = [output.outputs[0].text for output in outputs]
        return outputs

    def generate(self, prompts: List[str], use_tqdm=False, **kwargs):
        params = SamplingParams(**kwargs)
        return self.model.generate(prompts, params, use_tqdm=use_tqdm)


def main():
    model = VLLM(
        "kaist-ai/prometheus-7b-v2.0",
        num_gpus=1,
        cache_dir=CACHE_DIR,
        enable_lora=True,
    )
    prompts = [
        "###Task Description:\nAn instruction (might include an Input inside it), a response to evaluate, a reference answer that gets a score of 5, and a score rubric representing a evaluation criteria are given.\n1. Write a detailed feedback that assess the quality of the response strictly based on the given score rubric, not evaluating in general.\n2. After writing a feedback, write a score that is an integer between 1 and 5. You should refer to the score rubric.\n3. The output format should look as follows: \"Feedback: (write a feedback for criteria) [RESULT] (an integer number between 1 and 5)\"\n4. Please do not generate any other opening, closing, and explanations.\n\n###The instruction to evaluate:\nHow can I improve my time management skills?\n\n###Response to evaluate:\nImproving your time management skills can help you to be more productive, reduce stress, and achieve your goals. Here are some tips to help you improve your time management skills:\n\n1. Prioritize your tasks: Make a to-do list at the beginning of each day and prioritize the most important tasks. This will help you to focus on what's most important and avoid wasting time on low-priority tasks.\n2. Use a calendar or planner: Use a calendar or planner to schedule your tasks and appointments. This will help you to stay organized and ensure that you have enough time for everything you need to do.\n3. Set goals: Set realistic goals for yourself and break them down into smaller, manageable tasks. This will help you to stay focused and motivated.\n4. Eliminate distractions: Identify the things that distract you the most, such as social media or email notifications, and find ways to eliminate them. This could be as simple as turning off your phone or logging out of social media during work hours.\n5. Take breaks: Taking regular breaks can help you to stay focused and avoid burnout. Take a few minutes every hour to stretch, go for a walk, or do something that you enjoy.\n6. Learn to say no: Don't overcommit yourself by taking on too many tasks or responsibilities. Learn to say no to requests that don't align with your goals or values.\n7. Review and adjust: Regularly review your schedule and priorities to ensure that you are making the most of your time. Adjust your plans as needed to accommodate changes in your workload or personal life.\n\nBy implementing these tips, you can improve your time management skills and become more productive and efficient.\n\n###Reference Answer (Score 5):\nTo improve your time management skills, start by setting clear goals. Understand what you want to achieve and by when. This will give you a roadmap to follow. Next, prioritize your tasks based on their importance and urgency. Use tools like the Eisenhower Box to help you with this. Break down larger tasks into smaller, manageable parts to prevent feeling overwhelmed. \n\nEstablish a routine and stick to it. This could be a daily, weekly, or monthly routine depending on your goals. Use tools like calendars, planners, or apps like Google Calendar to schedule your tasks and set reminders. \n\nAvoid multitasking as it can lead to mistakes and inefficiency. Instead, focus on one task at a time until it's complete. \n\nFinally, take regular breaks to avoid burnout. Techniques like the Pomodoro Technique, where you work for 25 minutes then take a 5-minute break, can be very effective. Remember, managing your time effectively also involves taking care of your mental health.\n\n###Score Rubrics:\n[Does the response provide detailed and actionable steps grounded on real-world scenarios?]\nScore 1: The response lacks detail and provides no actionable steps or real-world context.\nScore 2: The response provides limited detail and few actionable steps, with minimal real-world grounding.\nScore 3: The response has some detailed and actionable steps, though not all are grounded in real-world scenarios.\nScore 4: The response is detailed with mostly actionable steps, and the majority are grounded in real-world scenarios.\nScore 5: The response is comprehensive, offering detailed and actionable steps, all of which are firmly grounded on real-world scenarios.\n\n###Feedback: "
    ]

    params = {
        "max_tokens": 2048,
        "repetition_penalty": 1.03,
        "best_of": 1,
        "temperature": 1.0,
        "top_p": 0.9,
    }

    completions = model.completions(prompts, **params)

    feedback = completions[0]
    feedback = feedback.split("[RESULT]")[0].strip()

    prompts = []
    for score in [1, 2, 3, 4, 5]:
        prompts.append(feedback + " [RESULT] " + str(score))

    print(prompts)

    choice_params = {
        "max_tokens": 1,
        "repetition_penalty": 1.03,
        "best_of": 1,
        "temperature": 1.0,
        "top_p": 0.9,
    }

    completions = model.generate(prompts, **choice_params)

    cum_log_probs = [output.outputs[0].cumulative_logprob for output in completions]
    print(cum_log_probs)

    # print(completions)


if __name__ == "__main__":
    main()
