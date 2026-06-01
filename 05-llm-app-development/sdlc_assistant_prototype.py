"""
SDLC Assistant Prototype

Purpose:
A lightweight local prototype showing how an LLM-powered SDLC assistant
could route different software engineering tasks.

This version does not call an external LLM. It returns deterministic sample
outputs for academic demonstration.
"""

from enum import Enum


class TaskType(str, Enum):
    USER_STORY = "user_story"
    TEST_CASES = "test_cases"
    DOCUMENTATION = "documentation"


def generate_user_story(requirement: str) -> str:
    return f"""
User Story:
As a user, I want {requirement.lower()} so that I can complete my intended task.

Acceptance Criteria:
- The system should provide the described capability.
- The system should handle valid and invalid inputs.
- The system should provide clear feedback to the user.
""".strip()


def generate_test_cases(requirement: str) -> str:
    return f"""
Test Cases for Requirement:
{requirement}

| Test Case ID | Scenario | Expected Result |
|---|---|---|
| TC001 | Valid input | System completes the operation successfully. |
| TC002 | Missing input | System displays a validation message. |
| TC003 | Invalid input | System rejects the request and shows an error. |
""".strip()


def generate_documentation(requirement: str) -> str:
    return f"""
Feature Documentation Draft

Feature Summary:
{requirement}

User Guidance:
The user should follow the application instructions to complete this feature.

Notes:
This draft should be reviewed by a domain expert before publication.
""".strip()


def route_task(task_type: TaskType, requirement: str) -> str:
    if task_type == TaskType.USER_STORY:
        return generate_user_story(requirement)
    if task_type == TaskType.TEST_CASES:
        return generate_test_cases(requirement)
    if task_type == TaskType.DOCUMENTATION:
        return generate_documentation(requirement)

    raise ValueError(f"Unsupported task type: {task_type}")


def main() -> None:
    requirement = "users should be able to upload documents and search them using natural language"

    print("=== User Story Output ===")
    print(route_task(TaskType.USER_STORY, requirement))

    print("\n=== Test Cases Output ===")
    print(route_task(TaskType.TEST_CASES, requirement))

    print("\n=== Documentation Output ===")
    print(route_task(TaskType.DOCUMENTATION, requirement))


if __name__ == "__main__":
    main()
