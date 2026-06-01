"""
LLM API Call Template

Purpose:
This file shows a safe structure for LLM API integration without including
real API keys or vendor-specific secrets.

Note:
Replace the placeholder client logic with the relevant SDK or HTTP call
when running in a real environment.
"""

import os
from typing import Dict


def build_prompt(requirement: str) -> str:
    """Build a structured prompt for an SDLC use case."""
    return f"""
Act as a software engineering assistant.
Convert the following requirement into:
1. User story
2. Acceptance criteria
3. Possible test scenarios

Requirement:
{requirement}
""".strip()


def call_llm_api(prompt: str) -> Dict[str, str]:
    """
    Placeholder function for calling an LLM API.

    In a real implementation:
    - Read API key from environment variables
    - Use the official SDK or HTTPS API
    - Handle errors and retries
    - Log prompt-response metadata
    """
    api_key = os.getenv("LLM_API_KEY")

    if not api_key:
        return {
            "status": "mock",
            "response": "No API key configured. This is a safe placeholder response.",
        }

    return {
        "status": "placeholder",
        "response": "Replace this block with actual LLM API integration.",
    }


def main() -> None:
    requirement = "Users should be able to reset their password using registered email."
    prompt = build_prompt(requirement)
    result = call_llm_api(prompt)

    print("Prompt:")
    print(prompt)
    print("\nResult:")
    print(result)


if __name__ == "__main__":
    main()
