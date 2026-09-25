# 11 — Thesis Artifacts: Source Mapping & Sync Flow

This document maps the concrete output of the upstream thesis pipeline
(*Parliament Graph Architecture*,
[fvilhalva/parliament-graph-architecture](https://github.com/fvilhalva/parliament-graph-architecture))
to the entities in [04 — Data Model](04-data-model.md), and describes how those
artifacts get from the thesis repo into this system without ever standing up
the thesis as a running service.

> The thesis pipeline is **not a service**. It is a batch job: run it, it emits
> files, it exits (15–25 min for the full 2022–2025 series on desktop
> hardware). Nothing in Parliament Insights depends on it being "up" — only on
> its output files existing under [`../data/artifacts/`](../data/artifacts).

## 11.1 Artifact → Entity mapping

| Thesis artifact | Contents | SAD entity | Enables | Transform needed |
|---|---|---|---|---|
| `data/analysis/analysis_{year}.json` | `n_nodes`, `n_edges`, `density`, `modularity_louvain` (Q), Louvain + Label Propagation partition summaries, Adjusted Rand Index, weighted null-model result (`Q_null` mean, p-value, 200 permutations), run metadata (`timestamp`, `max_authors=30`, `seed=42`) | `AnalysisResult` | FR01, FR04 | None — direct load into `raw_json`; scalar columns extracted 1:1 |
| Per-deputy metrics CSV | `deputy_id`, `name`, `party_code`, `state_code`, 4 centralities (degree/strength, betweenness, closeness, eigenvector), `community_louvain` | `Deputy` + `CommunityAssignment` | Centrality lookups, community filtering | None |
| Co-authorship edges CSV | `deputy_id_a`, `deputy_id_b`, raw weight, normalized weight (`1/(n_p-1)`), `year` | `CoauthorshipEdge` | GraphRAG structural filter (FR02) | None |
| GEXF graph | Nodes/edges/weights/community, Gephi-compatible | — (cross-validation / future viewer) | Roadmap item: interactive network viewer | None (not loaded into Postgres in V1) |
| SQLite DB | Same per-deputy metrics, upserted by `(year, deputy_id)` | Alternate read path | Not used by V1 ingestion (CSV is primary) | — |

## 11.2 The one gap: `Proposition.summary_text`

The thesis persists `Proposition` as `(id, year, author_ids, type)` only — it
**does not** store the proposition's text, because its scope ends at structural
metrics. It **does** already download and cache the raw Chamber metadata CSV
(via `ChamberExtractor`), which includes each proposition's **ementa**
(legislative abstract) — the thesis's own "Future Work" section names exactly
this gap (NLP over ementas).

Resolution used by this project:

- `Proposition.summary_text` (SAD §04) = the **ementa**, sourced from the raw
  Chamber metadata CSV — **not** from the thesis's analytical artifacts.
- `Proposition.embedding vector(384)` is generated **at this layer**
  (`sentence-transformers/all-MiniLM-L6-v2`, 384-d) — confirmed consistent with
  the model already declared in [`.env.example`](../.env.example).

## 11.3 Modeling parameters to preserve (NFR01 / NFR10)

These are the thesis's validated constants. Ingestion must **carry them
through as metadata**, not recompute or silently override them — any UI/API
response derived from `AnalysisResult` should be able to surface them for
audit:

| Parameter | Value | Why it matters here |
|---|---|---|
| Edge weight | `1 / (n_p - 1)` | Explains why raw co-authorship counts ≠ edge weights |
| `max_authors` filter | `30` | **No PEC enters the network** — all PECs exceed 30 signers; a query about PECs must return "excluded by design", not "not found" |
| Proposition types | `PL`, `PEC`, `PLP`, `PDL`, `EMC` | Any other type was never in the source network |
| Author scope | Federal deputies only (author type code `10000`) | |
| Community detection seed | `42` (Louvain) | Reproducibility — same input always yields the same partition |
| Null-model permutations | `200`, `α = 0.05` | Basis for the p-value already stored in `AnalysisResult` |
| Centrality representation | Betweenness/closeness on **unweighted** topology; degree/eigenvector on **weighted** graph | Prevents mixing incompatible centrality semantics in a comparison endpoint |

## 11.4 Sync flow (no deploy required)

```
vendor/parliament-graph-architecture/         (git submodule, pinned commit)
        │
        │  docker compose up pipeline_chamber   (manual, on demand — ~15-25 min)
        ▼
vendor/parliament-graph-architecture/data/{analysis,csv,gexf,sqlite}/
        │
        │  scripts/sync-thesis-artifacts.sh      (copy, read-only at destination)
        ▼
data/artifacts/{analysis,csv,gexf,sqlite}/     (this repo — FR09 reads from here)
        │
        │  ingestion job (FR09)
        ▼
PostgreSQL (data/schema.sql)
```

**Why a submodule, not a live integration:** the thesis's own scope statement
(SAD §01) is that it is "intentionally closed as a scientific artifact." A
submodule pinned to a commit keeps that boundary explicit in version control —
upgrading the thesis's analysis (e.g. a new year, a re-run with a different
`max_authors`) is a deliberate, reviewable submodule bump, never an implicit
live dependency.

**Cadence:** run manually today (2022–2025 backfill) and thereafter roughly
once per year when new legislative data is published — not a scheduled job.
Automating the sync (e.g. as a CI step or a cron-triggered ingestion) is a
candidate for V2+, not a V1 requirement.

## 11.5 What this does *not* require

- No deployment of the thesis pipeline as a service.
- No network dependency between Parliament Insights and the thesis at runtime.
- No modification of thesis code or its output files (NFR10) — `sync-thesis-
  artifacts.sh` only copies *from* the submodule checkout *into*
  `data/artifacts/`, never the reverse.
