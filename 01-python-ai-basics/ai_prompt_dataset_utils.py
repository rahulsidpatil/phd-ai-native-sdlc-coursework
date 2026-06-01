"""
AI Prompt Dataset Utilities

Purpose:
This file contains small utility functions for preparing simple prompt-response
examples. These utilities are representative of basic preprocessing that may be
needed before evaluating LLM behavior.

Note:
This is a lightweight educational example and does not use external libraries.
"""

from typing import Dict, List


PromptRecord = Dict[str, str]


def clean_prompt(prompt: str) -> str:
    """Remove extra whitespace from a prompt."""
    return " ".join(prompt.strip().split())


def validate_record(record: PromptRecord) -> bool:
    """Check whether a prompt-response record contains required fields."""
    required_fields = ["prompt", "response", "category"]
    return all(field in record and bool(record[field].strip()) for field in required_fields)


def filter_by_category(records: List[PromptRecord], category: str) -> List[PromptRecord]:
    """Filter prompt records by category."""
    return [
        record
        for record in records
        if record.get("category", "").lower() == category.lower()
    ]


def prepare_records(records: List[PromptRecord]) -> List[PromptRecord]:
    """Clean and validate prompt-response records."""
    prepared_records = []

    for record in records:
        if not validate_record(record):
            continue

        prepared_records.append(
            {
                "prompt": clean_prompt(record["prompt"]),
                "response": record["response"].strip(),
                "category": record["category"].strip().lower(),
            }
        )

    return prepared_records


def main() -> None:
    sample_records = [
        {
            "prompt": "  Generate test cases for a login feature.  ",
            "response": "Positive, negative, and boundary test cases should be considered.",
            "category": "testing",
        },
        {
            "prompt": "Summarize this requirement into user stories.",
            "response": "As a user, I want...",
            "category": "requirements",
        },
        {
            "prompt": "",
            "response": "Invalid example because prompt is empty.",
            "category": "misc",
        },
    ]

    prepared = prepare_records(sample_records)

    print("Prepared Records")
    print("-" * 20)
    for record in prepared:
        print(record)

    print("\nTesting Category Records")
    print("-" * 20)
    for record in filter_by_category(prepared, "testing"):
        print(record)


if __name__ == "__main__":
    main()
