# parliament-insights

Generative-AI and backend layer (RAG, agents, LLM) over the validated
**Parliament Graph Architecture** dataset.

Parliament Insights is a product layer — a NestJS API plus a Python/LangGraph
agent — that consumes the thesis's research artifacts as a **read-only source of
truth** and exposes structured queries, semantic search (RAG), and thematic
community summaries. It never alters the thesis's statistical validation core.

## Repository layout (monorepo — see [ADR-0001](docs/adr/ADR-0001-monorepo.md))

| Path | Layer |
|------|-------|
| [`api/`](api) | NestJS — public HTTP contract, auth, validation (no AI logic) |
| [`agent/`](agent) | Python + LangGraph — intent routing + tools (structured query / RAG / summarizer) |
| [`data/`](data) | Postgres + pgvector schema; read-only thesis artifacts |
| [`docs/`](docs/README.md) | Software-engineering documentation (mirrors the SAD) |

## Documentation

Start at [`docs/README.md`](docs/README.md): requirements, architecture, data
model, API design, use cases, testing, security, HPC-readiness, and roadmap.
The canonical SAD PDFs (EN + PT-BR) are in [`docs/`](docs).

## Quick start (dev)

```bash
cp .env.example .env            # fill secrets — never commit .env
docker compose up -d db redis   # Postgres+pgvector and Redis

# API
cd api && npm install && npm run build && npm test

# Agent
cd agent && pip install -e ".[dev]" && ruff check src tests && pytest
```

## Contributing & workflow

Branching model: `main → develop → feat/*`. Protected branches require a PR with
green CI. See [`CONTRIBUTING.md`](CONTRIBUTING.md); AI-assistant rules are in
[`CLAUDE.md`](CLAUDE.md). Run `/recap` (Claude skill) for a project refresher.

## Status

Scaffolding stage — skeleton + engineering docs + CI. Implementation follows the
[roadmap](docs/10-roadmap.md) (V1: ingestion + Structured Query Tool).

## License

See [`LICENSE`](LICENSE).
