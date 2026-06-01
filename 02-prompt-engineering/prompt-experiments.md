# Prompt Experiments

## Experiment 1: Generic Prompt vs Structured Prompt

### Generic Prompt

```text
Write user stories for a login system.
```

### Structured Prompt

```text
Act as a business analyst. Convert the following login requirement into user stories. Return the output as a Markdown table with columns: User Role, User Story, Acceptance Criteria, Priority.
Requirement: Users should be able to log in using email and password.
```

### Observation

The structured prompt is more useful for SDLC documentation because it asks for role, format, acceptance criteria, and priority.

## Experiment 2: Test Case Generation

### Prompt

```text
Generate functional test cases for the following requirement:
Users should be able to reset their password using a registered email address.

Return the output as a table with columns:
Test Case ID, Scenario, Preconditions, Steps, Expected Result.
```

### Observation

Specifying the table structure improves readability and makes the output easier to review.

## Experiment 3: Ambiguity Detection

### Prompt

```text
Review the following requirement and identify ambiguous terms, missing details, and assumptions:
The system should quickly notify users about failed payments.
```

### Observation

This prompt is useful in requirements engineering because terms such as "quickly" and "notify" need clarification.

## Learning Outcome

Prompt quality directly influences the usefulness of AI-generated SDLC artifacts.
