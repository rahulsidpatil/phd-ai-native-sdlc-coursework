"""
Simple RAG-Style Prototype

Purpose:
This script demonstrates the basic idea of Retrieval-Augmented Generation
using local text chunks and keyword matching.

Note:
This is an educational prototype. It does not use embeddings or external LLM APIs.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class DocumentChunk:
    chunk_id: str
    source: str
    text: str


def tokenize(text: str) -> set[str]:
    """Convert text into a simple lowercase token set."""
    return set(text.lower().replace(".", "").replace(",", "").split())


def retrieve(query: str, chunks: List[DocumentChunk], top_k: int = 2) -> List[DocumentChunk]:
    """Retrieve chunks using simple token overlap."""
    query_tokens = tokenize(query)

    scored_chunks = []
    for chunk in chunks:
        chunk_tokens = tokenize(chunk.text)
        score = len(query_tokens.intersection(chunk_tokens))
        scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)
    return [chunk for score, chunk in scored_chunks[:top_k] if score > 0]


def generate_answer(query: str, retrieved_chunks: List[DocumentChunk]) -> str:
    """Generate a simple grounded answer from retrieved chunks."""
    if not retrieved_chunks:
        return "No relevant context was found for the query."

    context = "\n".join(
        f"- [{chunk.source}::{chunk.chunk_id}] {chunk.text}"
        for chunk in retrieved_chunks
    )

    return f"""
Query: {query}

Retrieved Context:
{context}

Draft Answer:
Based on the retrieved context, the answer should be prepared using the cited source chunks above.
""".strip()


def main() -> None:
    chunks = [
        DocumentChunk(
            "REQ-001",
            "requirements.md",
            "AI Native SDLC uses AI assistance for requirements analysis and user story generation.",
        ),
        DocumentChunk(
            "TEST-001",
            "testing.md",
            "LLM-based tools can generate functional test cases from acceptance criteria.",
        ),
        DocumentChunk(
            "DOC-001",
            "documentation.md",
            "RAG can retrieve project documents and support grounded documentation generation.",
        ),
    ]

    query = "How can RAG support documentation in AI Native SDLC?"
    retrieved = retrieve(query, chunks)
    answer = generate_answer(query, retrieved)

    print(answer)


if __name__ == "__main__":
    main()
