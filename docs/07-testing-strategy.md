# 07 — Testing Strategy

Target coverage: **≥ 80%** in the API and Tools layers (**NFR08**), with
integration tests covering the three main flows (FR01–FR03).

| Level | Approach |
|-------|----------|
| **Unit** | *Structured Query Tool:* 100% of query-parameter combinations tested against an in-memory DB / fixture. *RAG Tool:* mocked embedding provider and vector store. |
| **Integration** | Full **API → Agent → Tool → Database** flow for UC01–UC03, with a test database populated from a fixed sample of thesis artifacts. |
| **Contract** | Request/response schema validation for each endpoint (FR08) via automated contract tests. |
| **Generation quality** | For FR02/FR03, manual sample-based evaluation (not automatable in CI) of retrieved-document relevance and summary fidelity. |
| **Cost regression** | Tests that log tokens/latency per LLM call, alerting if the average per query exceeds a defined threshold (NFR05/NFR09). |

## CI enforcement

- Unit, integration, and contract tests run in CI (see
  [`.github/workflows/ci.yml`](../.github/workflows/ci.yml)) on every PR to
  `main` and `develop`; a green CI run is a **required status check** for merge.
- Generation-quality evaluation is performed manually and recorded in the PR
  description — it is *not* a CI gate.

## Requirement → test mapping

| Requirement | Verified by |
|-------------|-------------|
| FR01, FR04, NFR01 | Structured Query unit tests (deterministic values) |
| FR02, FR06 | RAG unit + integration tests (citations present) |
| FR03, FR07 | Summarizer + cache integration tests |
| FR08 | Contract + auth tests |
| NFR02 | Latency assertions in integration tests |
| NFR05, NFR09 | Cost-regression tests |
