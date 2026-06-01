# LLM Application Architecture for AI Native SDLC

## Objective

Design a simple LLM-powered assistant that supports SDLC activities such as requirements refinement, user story generation, test case generation, and documentation drafting.

## Logical Components

```text
User Interface
   |
Application Service Layer
   |
Prompt Builder ---- Context Retriever
   |                     |
LLM Client          Knowledge Base
   |
Response Validator
   |
Output Formatter / Logger
```

## Component Responsibilities

| Component | Responsibility |
|---|---|
| User Interface | Accepts user input and displays generated SDLC artifacts. |
| Application Service Layer | Coordinates request handling and workflow execution. |
| Prompt Builder | Converts user input into structured prompts. |
| Context Retriever | Retrieves relevant project knowledge when needed. |
| LLM Client | Sends prompts to the model provider or mock client. |
| Response Validator | Checks for missing sections, unsupported claims, or formatting issues. |
| Output Formatter | Produces Markdown, JSON, or table outputs. |
| Logger | Stores prompt-response metadata for evaluation. |

## AI Native SDLC Relevance

This architecture supports practical experimentation with AI-assisted SDLC workflows while keeping concerns such as logging, retrieval, validation, and output formatting separate.
