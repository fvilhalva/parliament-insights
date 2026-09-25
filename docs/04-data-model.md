# 04 — Data Model

The operational schema is a **read-only projection** of the thesis artifacts
plus fields generated at this layer (embeddings, cached summaries). The
canonical DDL lives in [`../data/schema.sql`](../data/schema.sql). See
[11 — Thesis Artifacts](11-thesis-artifacts.md) for the exact artifact-to-entity
mapping and how those files reach this repo.

## 4.1 Entity–Relationship (summary)

```
Deputy (deputy_id PK) ──1..N── CommunityAssignment ──N..1── (community_id, year)
   │                                   
   └──N..N (via CoauthorshipEdge) ── Deputy
Proposition (proposition_id PK, embedding vector(384))
AnalysisResult (year PK)  ──1..N── CommunitySummary (cache)
```

## 4.2 Entities

| Entity | Key fields | Source | Notes |
|--------|-----------|--------|-------|
| **Deputy** | `deputy_id` (int, PK), `name`, `party_code(10)`, `state_code(2)` | Imported (metrics CSV) | Natural key preserved from original Chamber data. |
| **Proposition** | `proposition_id` (int, PK), `type(5)`, `year`, `summary_text`, `embedding vector(384)` | `summary_text`: raw Chamber metadata CSV (ementa) — **not** produced by the thesis pipeline. `embedding`: generated at this layer. | Neither field exists in the thesis's analytical output; see [11 — Thesis Artifacts §11.2](11-thesis-artifacts.md#112-the-one-gap-propositionsummary_text). |
| **CoauthorshipEdge** | `edge_id` (uuid, PK), `deputy_id_a` (FK), `deputy_id_b` (FK), `weight` (float), `year` | Imported (GEXF) | Normalized replica of the co-authorship graph edges for efficient relational querying. |
| **CommunityAssignment** | `assignment_id` (uuid, PK), `deputy_id` (FK), `year`, `community_id`, `method(20)` | Imported (metrics CSV) | Louvain / Label Propagation assignment per deputy/year. |
| **AnalysisResult** | `year` (int, PK), `n_nodes`, `n_edges`, `density`, `modularity_louvain`, `p_value`, `raw_json` (jsonb) | Imported (`analysis_{year}.json`) | **Append-only**; never rewritten, only versioned by year — guarantees **NFR10**. |
| **CommunitySummary** *(cache)* | `summary_id` (uuid, PK), `year` (FK), `community_id` (FK), `generated_text`, `model_used`, `created_at` | Generated at this layer | LLM-result cache; includes `model_used` for cost auditing (**NFR05**). |

## 4.3 Integrity rules

- **NFR10:** ingestion is read-only at the source. `AnalysisResult` is
  append-only and keyed by year; existing rows are never mutated.
- `embedding`, `CommunitySummary`, and `Proposition.summary_text` (ementa) are
  the only fields *not* produced by the thesis's analytical pipeline —
  `summary_text` comes from the raw Chamber metadata CSV, `embedding` and
  `CommunitySummary` are generated at this layer. Everything else is a
  faithful projection of thesis output. See
  [11 — Thesis Artifacts](11-thesis-artifacts.md).
- Modeling constants inherited from the thesis (edge weight `1/(n_p-1)`,
  `max_authors=30`, proposition types, Louvain `seed=42`) must be preserved
  as metadata, never recomputed — see
  [11 — Thesis Artifacts §11.3](11-thesis-artifacts.md#113-modeling-parameters-to-preserve-nfr01--nfr10).
