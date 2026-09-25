# Contributing

Solo-maintained portfolio project, but it follows a disciplined team-style flow.

## Branching model

```
main (stable)  ◄── PR ── develop (integration)  ◄── PR ── feat/* | fix/* | docs/* | chore/*
```

- **`main`** and **`develop`** are protected: no direct pushes, no force-push, no
  deletion; a PR with green CI is required to merge.
- Start every task on a fresh branch off `develop`:
  ```bash
  git checkout develop && git pull
  git checkout -b feat/<short-slug>
  ```
- Open a PR into `develop` (`gh pr create --base develop`). Promote to `main`
  via a `develop → main` PR when a milestone is stable.

## Commit messages

Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.

## Before opening a PR

- `api/`: `npm install && npm run build && npm test`
- `agent/`: `pip install -e ".[dev]" && ruff check . && pytest`
- Fill in the PR template; note any manual generation-quality evaluation
  (FR02/FR03) that CI cannot cover.

## For AI assistants

See [`CLAUDE.md`](CLAUDE.md) — assistants may open PRs but must **never** merge
into `main`/`develop`.
