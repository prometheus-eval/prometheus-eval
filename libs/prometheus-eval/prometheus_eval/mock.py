from typing import List, Union
import asyncio


class MockLLM:
    def __init__(self) -> None:
        print("Mock LLM initialized")

    def validate_mockllm(self):
        return True

    def generate(
        self,
        prompts: List[str],
        use_tqdm: bool = False,
        **kwargs,
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
        self,
        prompts: List[str],
        use_tqdm: bool = False,
        **kwargs,
    ) -> List[str]:
        # This mirrors the generate function in the mock
        return self.generate(prompts, use_tqdm, **kwargs)

    async def async_completions(
        self,
        prompts: List[str],
        use_tqdm: bool = False,
        **kwargs,
    ) -> List[str]:
        # Async version of the completions function
        await asyncio.sleep(0)  # Simulating async behavior
        return self.generate(prompts, use_tqdm, **kwargs)
