# 03 — Software Architecture

## 3.1 Layered Overview

The architecture follows the same **Dependency Rule** adopted in the thesis: each
layer depends only on the layer immediately below it, never the reverse. The
crossing between technologies (Node.js ↔ Python) happens at a single,
well-defined boundary (**API → Orchestration**).

```
┌──────────────────────────────────────────────────────────────┐
│ Client Layer                                                   │
│ Frontend / Recruiter / External integration (HTTP/GraphQL)     │
└───────────────────────────────┬────────────────────────────────┘
                                 │ HTTP/GraphQL
┌───────────────────────────────▼────────────────────────────────┐
│ API Layer (NestJS)                                             │
│ Controllers (REST/GraphQL) · Auth & Rate Limiting · Validation │
│ (DTO/Pipes). Contains NO AI logic.                             │
└───────────────────────────────┬────────────────────────────────┘
                                 │ internal call (gRPC/HTTP)
┌───────────────────────────────▼────────────────────────────────┐
│ Agent Orchestration Layer (Python + LangGraph)                 │
│ Intent Router · State Machine (Graph) · Response Cache         │
│ Delegates to tools; never touches the DB directly.             │
└───────────────────────────────┬────────────────────────────────┘
                                 │ function invocation
┌───────────────────────────────▼────────────────────────────────┐
│ Tools Layer                                                    │
│ Structured Query (SQL/Pandas) · RAG (Embeddings + pgvector)    │
│ · Summarizer (LLM local/API)                                   │
└───────────────────────────────┬────────────────────────────────┘
                                 │ read/write
┌───────────────────────────────▼────────────────────────────────┐
│ Data Layer                                                     │
│ PostgreSQL + pgvector · Thesis Artifacts (JSON/CSV/GEXF, RO)   │
│ · Redis Cache (queue/optional)                                 │
└────────────────────────────────────────────────────────────────┘
```

## 3.2 Layer Descriptions

| Layer | Responsibility |
|-------|----------------|
| **API (NestJS)** | HTTP/GraphQL exposure, authentication, input validation (DTOs), rate limiting, and translation between the public API contract and the internal call to the orchestration service. **Contains no AI logic.** |
| **Agent Orchestration (Python + LangGraph)** | A state machine representing the agent's flow: receives the question, classifies intent (FR05), decides which tool(s) to invoke, aggregates the final result. **Does not access the database directly** — delegates to tools. |
| **Tools** | Three independent, individually testable implementations: **Structured Query Tool** (deterministic), **RAG Tool** (semantic search + generation), **Summarizer Tool** (batch summarization). Each encapsulates a single responsibility. |
| **Data** | PostgreSQL with the `pgvector` extension for embeddings; thesis artifacts as a read-only import source; Redis as an optional queue for asynchronous processing. |

## 3.3 Architectural Patterns and Decisions

- **Monorepo** with clear module boundaries (`api/`, `agent/`, `data/`) instead
  of multiple repositories — see [ADR-0001](adr/ADR-0001-monorepo.md).
- **Separation between numeric-value generation and language generation:** the
  Structured Query Tool never delegates the computation of a thesis-validated
  number to the LLM — this avoids statistical hallucination (**NFR01**).
- **GraphRAG:** semantic search always combines vector similarity with a
  structural filter over graph metadata (community, year), rather than pure
  vector search.
- **Decoupled batch processing** for summarization (**FR10**), preparing the
  system for a cluster-execution pattern (a job queue analogous to SLURM).
- **LLM-provider independence:** the Tools layer abstracts the provider (local
  Ollama or a paid API) behind a common interface, enabling cost/quality
  comparison (**NFR09**).

## 3.4 Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| HTTP/GraphQL API | **NestJS (TypeScript)** | Strong typing and modules aligned with the layering principle. |
| Agent orchestration | **Python + LangGraph** | Standard ecosystem for orchestrating agents with explicit state. |
| Embeddings | **sentence-transformers** | Local execution, no API cost, control over vector dimensionality (384). |
| Vector store | **PostgreSQL + pgvector** | Reuses the relational DBMS, avoiding a dedicated vector DB. |
| Local LLM | **Ollama (Llama 3.2 3B)** | Cost/quality comparison vs. a paid API (NFR09); local-deployment expertise. |
| Queue / async | **Redis + BullMQ** | Decouples embedding/summarization from the API's synchronous path (FR10). |
| Containerization | **Docker + Docker Compose** | Direct path to HPC-readiness (NFR04). |
