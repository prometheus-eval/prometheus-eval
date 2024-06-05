from typing import List, Union


class VLLMError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)


try:
    from vllm import LLM, SamplingParams
except ImportError as e:
    raise VLLMError(
        status_code=1,
        message="Failed to import 'vllm' package. Make sure it is installed correctly.",
    ) from e


class VLLM:
    def __init__(
        self,
        model: str,
        **vllm_kwargs,
    ) -> None:
        self.model: str = model

        self.model: LLM = LLM(
            model=self.model,
            **vllm_kwargs,
        )

    def validate_vllm(self):
        return True

    def completions(
        self,
        prompts: List[str],
        use_tqdm: bool = True,
        **kwargs: Union[int, float, str],
    ) -> List[str]:
        prompts = [prompt.strip() for prompt in prompts]
        params = SamplingParams(**kwargs)

        outputs = self.model.generate(prompts, params, use_tqdm=use_tqdm)
        outputs = [output.outputs[0].text for output in outputs]
        return outputs
