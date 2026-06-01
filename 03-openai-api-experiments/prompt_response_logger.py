"""
Prompt Response Logger

Purpose:
This utility demonstrates how prompt-response experiments can be logged
for later analysis.

The output file is JSONL, where each line is one experiment record.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict


def create_log_record(
    prompt: str,
    response: str,
    use_case: str,
    model_name: str = "mock-llm",
) -> Dict[str, str]:
    """Create a structured prompt-response log record."""
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "model_name": model_name,
        "use_case": use_case,
        "prompt": prompt,
        "response": response,
    }


def append_jsonl(record: Dict[str, str], path: str = "prompt_response_log.jsonl") -> None:
    """Append a record to a JSONL file."""
    output_path = Path(path)
    with output_path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


def main() -> None:
    record = create_log_record(
        prompt="Generate test cases for password reset.",
        response="TC001: Valid email. TC002: Unregistered email. TC003: Empty email.",
        use_case="test-case-generation",
    )

    append_jsonl(record)
    print("Log record written to prompt_response_log.jsonl")


if __name__ == "__main__":
    main()
