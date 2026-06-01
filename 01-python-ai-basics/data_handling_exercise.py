"""
Data Handling Exercise

Purpose:
This script demonstrates how Python can be used to structure, process,
and summarize simple learning or experiment records.

Relevance:
AI Native SDLC research may involve analyzing prompts, experiments,
developer activities, code-generation results, or evaluation logs.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class LearningArtifact:
    module: str
    topic: str
    hours_spent: float
    relevance_score: int


def calculate_total_hours(artifacts: List[LearningArtifact]) -> float:
    """Calculate total learning hours from artifact records."""
    return sum(artifact.hours_spent for artifact in artifacts)


def get_high_relevance_topics(
    artifacts: List[LearningArtifact],
    threshold: int = 4,
) -> List[LearningArtifact]:
    """Return topics with relevance score greater than or equal to threshold."""
    return [
        artifact
        for artifact in artifacts
        if artifact.relevance_score >= threshold
    ]


def print_summary(artifacts: List[LearningArtifact]) -> None:
    """Print a compact summary report."""
    print("Learning Artifact Summary")
    print("-" * 30)

    for artifact in artifacts:
        print(
            f"{artifact.module}: {artifact.topic} "
            f"({artifact.hours_spent} hrs, relevance={artifact.relevance_score}/5)"
        )

    print("\nTotal Hours:", calculate_total_hours(artifacts))

    print("\nHigh-Relevance Topics")
    print("-" * 30)
    for artifact in get_high_relevance_topics(artifacts):
        print(f"- {artifact.topic}")


def main() -> None:
    artifacts = [
        LearningArtifact("Python Basics", "Functions and data structures", 4.0, 4),
        LearningArtifact("Prompt Engineering", "Prompt design patterns", 6.0, 5),
        LearningArtifact("LLM APIs", "API-based LLM application calls", 5.0, 5),
        LearningArtifact("RAG", "Knowledge retrieval workflow", 5.0, 5),
    ]

    print_summary(artifacts)


if __name__ == "__main__":
    main()
