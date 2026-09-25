# Documentation Index

Software-engineering documentation for the **Parliament Insights API**, derived
from the Software Architecture Document (SAD) in
[`parliament-insights-api_SAD_en.pdf`](parliament-insights-api_SAD_en.pdf)
(PT-BR version also available). The PDFs are the canonical, signed artifact; the
Markdown files below are the living, versioned working copy the team edits.

> **Scope reminder.** Parliament Insights is a *separate product layer* that
> consumes the artifacts produced by the *Parliament Graph Architecture* thesis
> ([fvilhalva/parliament-graph-architecture](https://github.com/fvilhalva/parliament-graph-architecture),
> monograph mirrored at [`PFC_Felipe.pdf`](PFC_Felipe.pdf)) as a **read-only
> source of truth**. It never modifies the thesis's statistical validation core.

## Contents

| # | Document | What it covers |
|---|----------|----------------|
| 01 | [Overview](01-overview.md) | Context, objectives, scope, audience |
| 02 | [Requirements](02-requirements.md) | Functional (FR01–FR10) & non-functional (NFR01–NFR10) |
| 03 | [Architecture](03-architecture.md) | Layered design, patterns, dependency rule |
| 04 | [Data Model](04-data-model.md) | Entities, ER diagram, data dictionary |
| 05 | [API Design](05-api-design.md) | REST endpoints and contracts |
| 06 | [Use Cases](06-use-cases.md) | UC01–UC05 and main flows |
| 07 | [Testing Strategy](07-testing-strategy.md) | Test levels and coverage targets |
| 08 | [Security](08-security.md) | Secrets, rate limiting, prompt-injection |
| 09 | [Infrastructure & HPC-Readiness](09-infrastructure-hpc.md) | Containers, batch, queue-as-scheduler |
| 10 | [Roadmap](10-roadmap.md) | V1 → V5 delivery plan |
| 11 | [Thesis Artifacts](11-thesis-artifacts.md) | Artifact→entity mapping, `Proposition.summary_text` source, sync flow (no deploy) |
| — | [ADR-0001: Monorepo](adr/ADR-0001-monorepo.md) | Monorepo vs. poly-repo decision |

## How this maps to the code

| Layer (see [Architecture](03-architecture.md)) | Folder |
|---|---|
| API (NestJS) | [`../api`](../api) |
| Agent Orchestration + Tools (Python/LangGraph) | [`../agent`](../agent) |
| Data (Postgres + pgvector, artifacts, schema) | [`../data`](../data) |
