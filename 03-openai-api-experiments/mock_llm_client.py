"""
Mock LLM Client

Purpose:
This mock client allows local experimentation with LLM-style workflows
without calling an external API.

Relevance:
Useful for testing application flow, prompt construction, logging, and
SDLC automation prototypes before integrating a real model provider.
"""

from dataclasses import dataclass


@dataclass
class MockLLMResponse:
    prompt: str
    response: str
    model: str = "mock-llm"


class MockLLMClient:
    """A simple mock LLM client."""

    def generate(self, prompt: str) -> MockLLMResponse:
        if "test case" in prompt.lower():
            response = "Generated mock test cases: TC001, TC002, TC003."
        elif "user story" in prompt.lower():
            response = "As a user, I want to complete the requested task so that I receive value."
        else:
            response = "Mock response generated for the provided prompt."

        return MockLLMResponse(prompt=prompt, response=response)


def main() -> None:
    client = MockLLMClient()
    response = client.generate("Generate user story and test cases for login.")
    print(response)


if __name__ == "__main__":
    main()
