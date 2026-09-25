"""RAG Tool (FR02, FR06).

GraphRAG: vector similarity (pgvector) ALWAYS combined with a structural filter
over graph metadata (community, year). Answers cite source proposition_ids
(FR06). SKELETON — no embedder/vector store wired yet.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RagResult:
    answer: str
    sources: list[dict[str, Any]] = field(default_factory=list)  # must be non-empty (FR06)
    model_used: str | None = None


def search_and_generate(
    question: str,
    *,
    community: int | None = None,
    year: int | None = None,
    top_k: int = 5,
) -> RagResult:
    """Embed the question, filter by (community, year), retrieve, then generate."""
    raise NotImplementedError(
        "embed_query -> similarity_search(top_k, metadata filter) -> LLM generate"
    )
