# api — NestJS layer

Public HTTP contract for Parliament Insights. **No AI logic here** — controllers
validate input, handle auth/rate-limiting, and delegate to the Agent
Orchestration layer via `OrchestrationClient` (the single Node→Python boundary).

See [`../docs/05-api-design.md`](../docs/05-api-design.md) for endpoints and
[`../docs/03-architecture.md`](../docs/03-architecture.md) for layering.

## Dev

```bash
npm install
npm run build      # tsc
npm test           # jest
npm run start:dev  # ts-node src/main.ts
```

## Status

Skeleton: `main.ts` bootstrap, `AppModule`, and stub controllers
(`/v1/health`, `/v1/query`, `/v1/metrics/*`). Endpoints return
`not_implemented` placeholders until wired to the agent and data layers.
