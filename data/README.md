# data — Data layer

- [`schema.sql`](schema.sql) — operational DDL (Postgres + pgvector). Mirrors
  [`../docs/04-data-model.md`](../docs/04-data-model.md).
- `artifacts/` — **read-only** import location for the thesis output
  (`analysis_{year}.json`, metrics CSV, GEXF, SQLite). Git-ignored (only
  `.gitkeep` is tracked); the ingestion job (FR09) reads from here and **never
  writes back** (NFR10).

Bring up the database via [`../docker-compose.yml`](../docker-compose.yml); the
schema is applied from `schema.sql` on first init.
