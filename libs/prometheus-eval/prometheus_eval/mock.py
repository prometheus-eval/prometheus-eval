import asyncio
from typing import List, Union


class MockLLM:
    def __init__(self, mode: str = None) -> None:
        assert mode in ["absolute", "relative", None]
        self.mode = mode
        print("Mock LLM initialized")

    def validate_mockllm(self):
        return True

    def generate(
        self,
        prompts: List[str],
        use_tqdm: bool = False,
        **kwargs,
    ) -> List[str]:
        if self.mode == "absolute":
            results = ["Hello [RESULT] 5"] * len(prompts)
        elif self.mode == "relative":
            results = ["Hello [RESULT] A"] * len(prompts)
        else:
            results = ["Hello World!"] * len(prompts)

        return results

    def completions(
        self,
        prompts: List[str],
        use_tqdm: bool = False,
        **kwargs,
    ) -> List[str]:
        # This mirrors the generate function in the mock
        return self.generate(prompts, use_tqdm, **kwargs)


class AsyncMockLLM(MockLLM):
    async def completions(
        self,
        prompts: List[str],
        use_tqdm: bool = False,
        **kwargs,
    ) -> List[str]:
        # Async version of the completions function
        await asyncio.sleep(0)  # Simulating async behavior
        return self.generate(prompts, use_tqdm, **kwargs)
