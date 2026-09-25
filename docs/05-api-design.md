# 05 — API Design

Base path: `/v1`. All external communication over HTTPS (**NFR06**), all access
authenticated with per-client rate limiting (**FR08**).

## 5.1 REST Endpoints

| Method | Route | Description | Traces |
|--------|-------|-------------|--------|
| `POST` | `/v1/query` | Single entry point for the agent; routes to FR01/FR02/FR03 by classified intent. | FR05 |
| `GET`  | `/v1/metrics/{year}` | Direct structured query (bypasses the agent); returns the raw `AnalysisResult`. | FR01 |
| `GET`  | `/v1/metrics/compare?years=2022,2025&metric=modularity` | Year-over-year comparison. | FR04 |
| `POST` | `/v1/search` | Direct semantic search (no text generation) — returns documents only. | FR02 |
| `GET`  | `/v1/communities/{year}/{id}/summary` | Retrieve a cached community summary; `202 Accepted` if still processing. | FR03, FR07 |
| `POST` | `/v1/admin/ingest` | Trigger ingestion of thesis artifacts; **admin role only**. | FR09 |

## 5.2 Contract example — `POST /v1/query`

**Request**
```json
{
  "question": "What was the network's modularity in 2024?",
  "context": { "preferred_language": "en-US" }
}
```

**Response (200) — structured intent** (`generated_by_llm: false`)
```json
{
  "intent": "structured_query",
  "answer": "In 2024, the observed (Louvain) modularity was 0.634, with p-value 0.005 (significant).",
  "source": { "type": "AnalysisResult", "year": 2024, "field": "louvain.modularity" },
  "generated_by_llm": false,
  "latency_ms": 340
}
```

**Response (200) — RAG intent** (`generated_by_llm: true`, cites sources per FR06)
```json
{
  "intent": "semantic_search",
  "answer": "Community 3 co-authored 4 environmental propositions in 2025 ...",
  "sources": [
    { "proposition_id": 88213, "type": "PL",  "year": 2025, "score": 0.87 },
    { "proposition_id": 88540, "type": "PEC", "year": 2025, "score": 0.81 }
  ],
  "generated_by_llm": true,
  "model_used": "llama3.2:3b",
  "latency_ms": 2130
}
```

## 5.3 Conventions

- **Traceability (FR06):** any `generated_by_llm: true` response must include a
  non-empty `sources[]`.
- **Observability (NFR05):** responses expose `latency_ms`; `model_used` is
  present whenever the LLM was invoked.
- **Determinism (NFR01):** structured answers set `generated_by_llm: false` and
  carry an explicit `source` pointer back to the thesis artifact.
