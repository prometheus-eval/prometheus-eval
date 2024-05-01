"""
This script produces completions for roughly any AutoModelForCausalLM.
"""
from typing import List
from vllm import LLM, SamplingParams


class VLLM:
    def __init__(
        self,
        name,
        quantization=None,
        tokenizer_name=None,
        tokenizer_revision=None,
        num_gpus=1,
        download_dir=None,
        enable_lora=False,
    ):
        dtype = "auto"

        self.name = name

        max_model_len = None
        gpu_memory_utilization = 0.8

        self.model = LLM(
            model=self.name,
            tokenizer=tokenizer_name,
            quantization=quantization,
            dtype=dtype,
            max_model_len=max_model_len,
            tokenizer_revision=tokenizer_revision,
            trust_remote_code=True,
            tensor_parallel_size=num_gpus,
            gpu_memory_utilization=gpu_memory_utilization,
            download_dir=download_dir,
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