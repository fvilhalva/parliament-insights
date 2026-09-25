# 09 — Infrastructure and HPC-Readiness

Although this project's scope does not require a real HPC cluster, the
architecture is designed to reflect the principles that make a system
**HPC-ready**, addressing the "nice-to-have" SLURM/containers requirement of the
reference job posting:

- **Stateless compute layer.** The embedding/summarization worker keeps no
  in-memory state between runs — each job is independent, analogous to a SLURM
  *job array*.
- **Batch-first.** Embedding generation runs in batch over all pending
  propositions, not one at a time on demand (**FR10**).
- **Containerization.** Every service runs in an isolated Docker image;
  migrating to Apptainer/Singularity (common in academic HPC) would only require
  swapping the container runtime, not the code (**NFR04**).
- **Queue as a scheduler abstraction.** The Redis/BullMQ queue fulfils, at a
  smaller scale, the same role a SLURM scheduler fulfils in a cluster —
  distributing jobs across available workers (**NFR03**).

## Local topology (`docker-compose.yml`)

| Service | Image | Role |
|---------|-------|------|
| `api` | NestJS | Public HTTP API |
| `agent` | Python/LangGraph | Orchestration + tools |
| `worker` | Python | Batch embedding/summarization consumer |
| `db` | `pgvector/pgvector` | PostgreSQL + pgvector |
| `redis` | `redis` | Queue / cache |
| `ollama` *(optional)* | `ollama/ollama` | Local LLM |

See [`../docker-compose.yml`](../docker-compose.yml) for the concrete
composition.
