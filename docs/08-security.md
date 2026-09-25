# 08 — Security Considerations

- **Secrets management (NFR06).** External LLM-provider API keys are **never**
  committed to version control — managed via environment variables / `.env`
  (following the same pattern used in the thesis with `pydantic-settings`).
  See [`.env.example`](../.env.example) for the required variables.
- **Rate limiting (FR08).** Per-API-key rate limiting mitigates abusive use and
  contains the cost of external LLM calls.
- **Prompt-injection mitigation.** Input sanitization before composing prompts,
  mitigating injection via proposition text or user questions.
- **Least privilege.** The ingestion endpoint (`/v1/admin/ingest`) is restricted
  to an administrative role and never publicly exposed.
- **Read-only source (NFR10).** The thesis artifacts are treated as read-only
  throughout the ingestion pipeline — no reverse writes are allowed.
- **Transport.** All external communication over HTTPS.

## Operational notes

- Keep dependency scanning and secret scanning enabled on the repository.
- Never log full secrets; LLM-call logs (NFR05) capture prompt/model/tokens/
  latency but must redact any credential material.
