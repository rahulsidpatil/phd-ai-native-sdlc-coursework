# Risks and Controls in LLM App Development

## Key Risks

| Risk | Description | Suggested Control |
|---|---|---|
| Hallucination | Model may generate unsupported information. | Use RAG, citations, and human review. |
| Data leakage | Sensitive data may be sent to external services. | Use data classification and redaction. |
| Prompt injection | Malicious input may override intended behavior. | Apply input validation and instruction hierarchy. |
| Over-reliance | Users may trust AI output without review. | Keep human approval gates. |
| Poor traceability | Generated artifacts may not link to source requirements. | Use IDs and structured logs. |
| Secret exposure | API keys may be committed accidentally. | Use environment variables and secret scanning. |

## AI Native SDLC Consideration

Risk controls should be built into the SDLC workflow itself. AI-generated artifacts should be treated as draft outputs requiring validation.
