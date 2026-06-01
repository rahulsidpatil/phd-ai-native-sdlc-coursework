# RAG Concept Notes

## What is RAG?

Retrieval-Augmented Generation combines information retrieval with text generation. Instead of relying only on model memory, a RAG system retrieves relevant documents or chunks and uses them as context for generating an answer.

## Basic RAG Workflow

1. Collect documents.
2. Split documents into chunks.
3. Convert chunks into searchable representations.
4. Retrieve relevant chunks for a user query.
5. Generate an answer using the retrieved context.
6. Cite or reference the source chunks where possible.

## Why RAG Matters for AI Native SDLC

RAG can help software teams use project-specific knowledge, such as:

- Requirements documents
- Architecture decision records
- API documentation
- Coding standards
- Test plans
- Defect reports
- Release notes

## Example SDLC Use Cases

| Use Case | RAG Benefit |
|---|---|
| Requirements analysis | Retrieve related requirements and constraints. |
| Codebase onboarding | Answer questions using project documentation. |
| Test design | Retrieve acceptance criteria and prior test cases. |
| Maintenance | Retrieve historical bug reports and fixes. |
| Documentation | Generate drafts grounded in existing docs. |

## Limitation

RAG quality depends on document quality, chunking, retrieval accuracy, and answer validation.
