import asyncio

from aiolimiter import AsyncLimiter
from litellm import acompletion, completion
from tqdm.asyncio import tqdm_asyncio
from tqdm.auto import tqdm


class LiteLLM:
    def __init__(self, name, api_base: str = None):
        """Initialize the LiteLLM with basic configurations."""
        self.name = name
        self.api_base = api_base

    def validate_litellm(self):
        return True

    def completions(self, messages, **kwargs):
        """Generate completions for a list of messages using synchronous batch processing."""
        # messages: List of list of dictionaries containing messages
        assert isinstance(messages, list)  # Ensure messages are provided as a list
        assert all(
            isinstance(message, list) for message in messages
        ), "Message format error."
        assert all(
            isinstance(msg, dict) and set(msg.keys()) == {"role", "content"}
            for message in messages
            for msg in message
        ), "Message format error."

        result_responses = []

        for message in tqdm(messages):
            response = completion(model=self.name, api_base=self.api_base, messages=message, **kwargs)
            result_responses.append(response.choices[0].message.content.strip())

        return result_responses


class AsyncLiteLLM:
    def __init__(self, name, batch_size: int = 100, requests_per_minute: int = 100, api_base: str = None):
        """Initialize the LiteLLM with basic configurations."""
        self.name = name
        self.batch_size = batch_size  # Define batch size for batch processing
        self.requests_per_minute = requests_per_minute  # Rate limit: 100 requests per minute
        self.limiter = AsyncLimiter(
            self.requests_per_minute, 60
        )  # Set up the rate limiter
        self.api_base = api_base

    def validate_litellm(self):
        return True

    async def _get_completion_text_async(self, message, **kwargs):
        """Fetch completion text for a single message asynchronously."""
        async with self.limiter:  # Apply rate limiting
            try:
                completion = await acompletion(
                    model=self.name, api_base=self.api_base, messages=message, request_timeout=60
                )
                return completion.choices[
                    0
                ].message.content.strip()  # Extract the first completion choice
            except Exception as e:
                print(f"Error during LiteLLM API call: {e}")
                return ""

    async def completions(self, messages, **kwargs):
        """Generate completions for a list of messages using asynchronous batch processing."""
        assert isinstance(messages, list)  # Ensure messages are provided as a list
        assert all(
            isinstance(message, list) for message in messages
        ), "Message format error."
        assert all(
            isinstance(msg, dict) and set(msg.keys()) == {"role", "content"}
            for message in messages
            for msg in message
        ), "Message format error."

        result_responses = []

        # Process the messages in batches with progress visualization
        for start_idx in tqdm(
            range(0, len(messages), self.batch_size), desc="Processing batches"
        ):
            end_idx = start_idx + self.batch_size
            batch_prompts = messages[start_idx:end_idx]

            # Fetch responses for all prompts in the current batch asynchronously
            batch_responses = await tqdm_asyncio.gather(
                *[
                    self._get_completion_text_async(prompt, **kwargs)
                    for prompt in batch_prompts
                ]
            )
            result_responses.extend(batch_responses)

        return result_responses


async def _test():
    """Test function for LiteLLM."""
    model = LiteLLM("openrouter/openai/gpt-3.5-turbo")
    batch_messages = [{"role": "user", "content": "good morning?"}] * 10

    responses = await model.completions(batch_messages)
    print(responses)

    return responses


if __name__ == "__main__":
    asyncio.run(_test())
