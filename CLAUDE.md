# CLAUDE.md — Working agreement for AI assistants

This file governs how Claude (and any AI assistant) works in this repository.
**Read it before making changes**, and re-read it whenever the user runs the
`/recap` skill.

## What this project is

**Parliament Insights API** — a product layer (traditional backend + Generative
AI) built *on top of* the read-only artifacts of the *Parliament Graph
Architecture* thesis. Full software-engineering documentation lives in
[`docs/`](docs/README.md); start there ([`docs/README.md`](docs/README.md)) for
requirements, architecture, data model, API design, and roadmap.

Monorepo layout: `api/` (NestJS), `agent/` (Python + LangGraph tools),
`data/` (Postgres + pgvector, schema, read-only thesis artifacts).

---

## 🔒 Git & branching rules — NON-NEGOTIABLE

1. **Never merge into a protected branch without a PR *and* the owner's explicit
   approval.** The protected branches are **`main`** and **`develop`**. Claude
   must **never** run `git merge`, `git push` to these branches, or `gh pr merge`
   for them. Only **the owner (Felipe)** clicks merge, after reviewing the PR.
2. **Branching model:** `main` → `develop` → `feat/*` (or `fix/*`, `chore/*`,
   `docs/*`, `refactor/*`, …).
   - `main` — production/stable. Only receives PRs **from `develop`**.
   - `develop` — integration branch. Receives PRs from task branches.
   - task branches — one per task, branched **from `develop`**.
3. **Start every new task on a new branch.** When the user begins a new task,
   Claude first creates a fresh branch off the latest `develop`:
   ```bash
   git checkout develop && git pull
   git checkout -b feat/<short-task-slug>
   ```
   Never commit new-task work directly onto `develop` or `main`.
4. **PR flow Claude may perform:** create the branch, commit, push the branch,
   and **open** the PR (`gh pr create --base develop`). Claude then **stops** and
   asks the owner to review/merge. Merging is the owner's action.
5. **CI must be green** before a PR is mergeable — CI is a required status check
   (see [`.github/workflows/ci.yml`](.github/workflows/ci.yml)).

### Branch naming

| Prefix | Use |
|--------|-----|
| `feat/` | new feature |
| `fix/` | bug fix |
| `docs/` | documentation only |
| `chore/` | tooling, deps, config |
| `refactor/` | internal change, no behavior change |

### Commits

- Conventional Commits style: `feat: …`, `fix: …`, `docs: …`, `chore: …`.
- Keep commits scoped and descriptive.

---

## Architectural guardrails (from the SAD)

- **NFR01 / no statistical hallucination:** the Structured Query Tool returns
  thesis-validated numbers verbatim from the database. The LLM never *computes*
  a validated metric.
- **NFR10 / read-only source:** never write to or mutate the thesis artifacts;
  `AnalysisResult` is append-only, keyed by year.
- **NFR07 / layering:** respect the Dependency Rule — API → Orchestration →
  Tools → Data, each depending only on the layer below. The Node↔Python boundary
  is API → Orchestration only.
- **FR06 / traceability:** any LLM-generated answer must cite its sources.
- **NFR06 / secrets:** never commit secrets; use `.env` (git-ignored).

## Conventions

- Prefer editing existing files over adding new ones; match surrounding style.
- Update [`docs/10-roadmap.md`](docs/10-roadmap.md) "Current status" when a
  milestone lands.
- Tests: target ≥ 80% coverage in `api/` and the tools layer (NFR08).
