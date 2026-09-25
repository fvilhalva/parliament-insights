# 10 — Roadmap and Future Work

Delivery is incremental; each version is a shippable slice with its own PRs into
`develop`.

| Version | Deliverable |
|---------|-------------|
| **V1 (MVP)** | Thesis-artifact sync (submodule + `scripts/sync-thesis-artifacts.sh`, see [11 — Thesis Artifacts](11-thesis-artifacts.md)) + ingestion + Structured Query Tool + `/v1/metrics` endpoint. |
| **V2** | RAG over proposition summaries + `/v1/search` and `/v1/query` endpoints. |
| **V3** | Batch community summarization + cache + `/v1/communities` endpoint. |
| **V4 (extension)** | Lightweight fine-tuning (LoRA/PEFT) of a small model specialized in the legislative domain; compare quality/cost vs. generic Ollama. |
| **V5 (extension)** | Extract the `agent/` module as a reusable Python package for other graph projects. |

## Current status

> Update this section as milestones land (the `/recap` skill reads it).

- [x] SAD authored (`docs/*.pdf`) and mirrored to Markdown (`docs/*.md`).
- [x] Repository scaffolding: monorepo skeleton (`api/`, `agent/`, `data/`),
      CI, branch protection, `CLAUDE.md` workflow rules.
- [x] Thesis-artifact mapping documented ([11 — Thesis Artifacts](11-thesis-artifacts.md));
      upstream source confirmed as [parliament-graph-architecture](https://github.com/fvilhalva/parliament-graph-architecture).
- [ ] **V1** — thesis submodule + sync script + ingestion + Structured Query
      Tool + `/v1/metrics`.
- [ ] V2 — RAG (embeddings over proposition ementas).
- [ ] V3 — batch summarization.
