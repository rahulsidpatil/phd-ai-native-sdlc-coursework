"""
Python Foundations Practice

Purpose:
This script demonstrates foundational Python concepts used in AI and LLM
application development workflows.

Topics covered:
- Variables and data types
- Lists and dictionaries
- Functions
- Control flow
- Basic text processing
- Simple reporting
"""

from typing import Dict, List


def normalize_text(text: str) -> str:
    """Normalize user-entered text for simple downstream processing."""
    return " ".join(text.strip().lower().split())


def count_keywords(text: str, keywords: List[str]) -> Dict[str, int]:
    """Count occurrences of selected keywords in a text string."""
    normalized_text = normalize_text(text)
    return {keyword: normalized_text.count(keyword.lower()) for keyword in keywords}


def summarize_course_topics(topics: List[str]) -> None:
    """Print a simple numbered summary of course topics."""
    print("Course Topic Summary")
    print("-" * 20)
    for index, topic in enumerate(topics, start=1):
        print(f"{index}. {topic}")


def main() -> None:
    research_area = "AI Native Software Development Life Cycle"

    course_topics = [
        "Python programming for AI workflows",
        "Prompt engineering",
        "LLM API integration",
        "Retrieval-Augmented Generation",
        "LLM application development",
    ]

    sample_reflection = """
    Generative AI and LLM-based tools can support AI Native SDLC by assisting
    with requirements analysis, code generation, test case design, documentation,
    and knowledge retrieval.
    """

    keywords = ["ai", "llm", "sdlc", "code", "test"]

    print(f"Research Area: {research_area}\n")
    summarize_course_topics(course_topics)

    print("\nKeyword Counts")
    print("-" * 20)
    for keyword, count in count_keywords(sample_reflection, keywords).items():
        print(f"{keyword}: {count}")


if __name__ == "__main__":
    main()
