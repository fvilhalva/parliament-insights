# agent — Orchestration + Tools (Python + LangGraph)

Classifies question intent (FR05) and dispatches to one of three tools:
Structured Query (deterministic), RAG (semantic search + generation), and
Summarizer (batch). See [`../docs/03-architecture.md`](../docs/03-architecture.md)
and [`../docs/06-use-cases.md`](../docs/06-use-cases.md).

## Dev

```bash
pip install -e ".[dev]"          # lint + test deps (lean, used by CI)
pip install -e ".[runtime,dev]"  # + langgraph, sentence-transformers, psycopg
ruff check src tests
pytest
```

## Status

Skeleton: intent `router`, `AgentState`/`route` graph node, and stub tools
(`structured_query`, `rag`, `summarizer`) raising `NotImplementedError`. The
LangGraph `StateGraph` and DB/LLM wiring are TODO.
