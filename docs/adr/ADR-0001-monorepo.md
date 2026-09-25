# ADR-0001 — Monorepo vs. multiple repositories

| Field | Content |
|-------|---------|
| **Status** | Accepted |
| **Date** | 2026-09-25 |

## Context

The project spans two languages (TypeScript / Python) and four logical layers.
It is an individual portfolio project, not a multi-team system.

## Decision

Adopt a **monorepo** with `api/`, `agent/`, `data/` folders, communicating via
internal HTTP, instead of separate repositories per layer.

## Alternatives considered

1. Poly-repo — one repository per layer.
2. Monorepo with integrated workspaces (npm/uv).

## Consequences

**Positive**
- Unified reading of the architecture by an external reviewer.
- Less cross-repository versioning overhead.
- Single deployment via `docker-compose`.

**Negative**
- Weaker per-layer ownership isolation (irrelevant for a single-author context).
- Should the `agent/` module need to become a reusable library
  ([roadmap V5](../10-roadmap.md)), it will be extracted into its own repository
  at that point.
