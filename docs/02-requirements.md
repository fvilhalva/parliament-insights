# 02 — Requirements

## 2.1 Functional Requirements

| ID | Name | Description |
|----|------|-------------|
| **FR01** | Structured metric query | Query, in natural language, already-validated structural metrics (density, modularity, centralities) filtered by year, returning the **exact source value** with no numeric generation by the LLM. |
| **FR02** | Semantic search over propositions | Search legislative propositions by meaning similarity (not just keyword), with optional filtering by community (Louvain) and year. |
| **FR03** | Thematic community summary | Generate and expose a textual summary of the thematic pattern of a community of deputies, based on the summaries of propositions co-authored by its members. |
| **FR04** | Year-over-year comparison | Compare the same indicator (e.g. modularity, density) across multiple years of the 2022–2025 period. |
| **FR05** | Intent routing | Automatically classify the intent of a question (structured query, semantic search, or summary) and route it to the appropriate tool. |
| **FR06** | Source traceability | Any response involving LLM generation must cite the source propositions/documents used as context. |
| **FR07** | Summary caching | Already-generated community summaries are cached and reused, avoiding a new LLM call for the same community/year. |
| **FR08** | Authentication & authorization | API access is authenticated (API key or JWT) with per-client rate limiting. |
| **FR09** | Thesis artifact ingestion | Periodically import the artifacts produced by the thesis pipeline (JSON/CSV/GEXF) into the operational database, **without modifying them at the source**. |
| **FR10** | Batch embedding processing | Embedding generation for proposition summaries runs asynchronously / in batch, decoupled from the API's synchronous request path. |

## 2.2 Non-Functional Requirements

| ID | Category | Description |
|----|----------|-------------|
| **NFR01** | Accuracy / Reliability | Structured-query responses (FR01, FR04) must be deterministically correct w.r.t. the source data; the LLM acts only as a language-interpretation layer, **never** as the source of the numeric value. |
| **NFR02** | Performance | Structured queries respond within **1 s (p95)**; RAG queries within **5 s (p95)**, including the LLM call. |
| **NFR03** | Scalability | The embedding-generation & summarization layer is horizontally scalable via independent workers (no shared in-memory state). |
| **NFR04** | Portability / HPC-readiness | All services runnable as containers (Docker), stateless at the compute layer, compatible with batch execution (SLURM-style scheduling). |
| **NFR05** | Observability | Every LLM call is logged with prompt, model, tokens consumed, and latency, for cost auditing. |
| **NFR06** | Security | External communication over HTTPS; secrets (LLM API keys) managed via env vars / a secret manager, never committed. |
| **NFR07** | Maintainability | Strict layer separation (API / Orchestration / Tools / Data) following the thesis's Dependency Rule. |
| **NFR08** | Testability | Automated coverage **≥ 80%** in the API and tools layers, with integration tests covering the three main flows (FR01–FR03). |
| **NFR09** | Cost | The architecture allows switching between a local LLM (Ollama) and a paid LLM API, enabling per-query cost comparison. |
| **NFR10** | Source-data integrity | The system **never** writes to or alters the thesis's original artifacts; all ingestion is read-only at the source. |

## Traceability

Requirements are traced to use cases in [06 — Use Cases](06-use-cases.md) and to
verification in [07 — Testing Strategy](07-testing-strategy.md).
