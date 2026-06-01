# Test Case Generation Prompt Templates

## Template 1: Functional Test Cases

```text
Act as a QA engineer. Generate functional test cases for the following requirement.

Requirement:
[Insert requirement here]

Return the output as a table with:
- Test Case ID
- Scenario
- Preconditions
- Test Steps
- Expected Result
- Priority
```

## Template 2: Boundary and Negative Test Cases

```text
Generate boundary and negative test cases for the following requirement.

Requirement:
[Insert requirement here]

Focus on invalid input, missing data, edge conditions, and error handling.
```

## Template 3: Traceability-Oriented Test Cases

```text
Generate test cases for the following user story and maintain traceability.

User Story:
[Insert user story here]

Acceptance Criteria:
[Insert acceptance criteria here]

Return:
- Requirement ID
- Test Case ID
- Linked Acceptance Criterion
- Test Scenario
- Expected Result
```

## Relevance

AI-generated test cases can support faster test design in AI Native SDLC, but human review remains necessary for correctness, coverage, and domain suitability.
