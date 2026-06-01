# Prompt Engineering Patterns for AI Native SDLC

## 1. Role-Based Prompting

Role-based prompting gives the LLM a specific responsibility.

Example:

```text
Act as a senior software requirements analyst. Review the following feature description and identify missing requirements, ambiguities, and assumptions.
```

## 2. Structured Output Prompting

Structured output prompting requests responses in a defined format.

Example:

```text
Convert the following requirement into user stories. Return the output as a Markdown table with columns: Actor, Goal, Benefit, Acceptance Criteria.
```

## 3. Constraint-Based Prompting

Constraint-based prompting limits the response according to rules.

Example:

```text
Generate only functional test cases. Do not include performance, security, or usability test cases.
```

## 4. Chain-of-Review Prompting

This pattern asks the model to review an artifact against criteria.

Example:

```text
Review the following generated test cases for completeness, duplication, and traceability to the original requirement.
```

## 5. SDLC Artifact Transformation

This pattern transforms one SDLC artifact into another.

Examples:

- Requirement to user story
- User story to acceptance criteria
- Acceptance criteria to test cases
- Code snippet to documentation
- Bug report to reproduction steps

## Relevance to AI Native SDLC

Prompt patterns can help structure AI-assisted activities across requirements, design, development, testing, documentation, and maintenance.
