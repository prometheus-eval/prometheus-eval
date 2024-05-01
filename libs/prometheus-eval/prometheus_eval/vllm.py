from typing import List, Optional, Union

from vllm import LLM, SamplingParams


class VLLM:
    def __init__(
        self,
        name: str,
        quantization: Optional[str] = None,
        tokenizer_name: Optional[str] = None,
        tokenizer_revision: Optional[str] = None,
        num_gpus: int = 1,
        download_dir: Optional[str] = None,
    ) -> None:
        dtype: str = "auto"
        self.name: str = name

        max_model_len: Optional[int] = None
        gpu_memory_utilization: float = 0.8

        self.model: LLM = LLM(
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
        use_tqdm: bool = False,
        **kwargs: Union[int, float, str]
    ) -> List[str]:
        prompts = [prompt.strip() for prompt in prompts]
        params = SamplingParams(**kwargs)

        outputs = self.model.generate(prompts, params, use_tqdm=use_tqdm)
        outputs = [output.outputs[0].text for output in outputs]
        return outputs

    def generate(
        self,
        prompts: List[str],
        use_tqdm: bool = False,
        **kwargs: Union[int, float, str]
    ) -> List[str]:
        params = SamplingParams(**kwargs)
        return self.model.generate(prompts, params, use_tqdm=use_tqdm)


class MockVLLM:
    def __init__(
        self,
    ) -> None:
        print("Mock VLLM initialized")

    def generate(
        self, prompts: List[str], params: Optional[dict] = None, use_tqdm: bool = False
    ) -> List[str]:
        results = []
        for prompt in prompts:
            if "A or B" in prompt:
                results.append("Hello [RESULT] A")
            elif "1 and 5" in prompt:
                results.append("Hello [RESULT] 5")
            else:
                results.append("Response to: " + prompt)  # default fallback
        return results

    def completions(
        self, prompts: List[str], params: Optional[dict] = None, use_tqdm: bool = False
    ) -> List[str]:
        # This mirrors the generate function in the mock
        return self.generate(prompts, params, use_tqdm)
