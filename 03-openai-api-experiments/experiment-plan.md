# LLM API Experiment Plan

## Objective

To understand how LLM APIs can support AI Native SDLC workflows such as requirements refinement, user story generation, test case generation, code explanation, and documentation.

## Experiment Categories

| Experiment | Input | Expected Output |
|---|---|---|
| Requirement to user story | Informal feature requirement | Structured user stories |
| User story to test cases | User story and acceptance criteria | Functional test cases |
| Code explanation | Small code snippet | Explanation and documentation |
| Bug report analysis | Bug description | Reproduction steps and possible causes |
| Documentation drafting | Feature summary | User-facing documentation draft |

## Evaluation Criteria

- Completeness
- Correctness
- Clarity
- Traceability to input
- Usefulness for SDLC task
- Need for human review

## Safety and Security Considerations

- Do not send confidential code or sensitive data to external APIs.
- Do not commit API keys to the repository.
- Validate all generated outputs before academic or professional use.
