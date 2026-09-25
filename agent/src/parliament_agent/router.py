"""Intent router (FR05).

Classifies a natural-language question into one of the supported intents so the
orchestration graph can dispatch to the right tool. The heuristic below is a
deterministic placeholder; the real router will use the LLM classifier.
"""

from __future__ import annotations

from enum import StrEnum


class Intent(StrEnum):
    STRUCTURED_QUERY = "structured_query"   # FR01 / FR04
    SEMANTIC_SEARCH = "semantic_search"     # FR02
    COMMUNITY_SUMMARY = "community_summary"  # FR03


_STRUCTURED_HINTS = ("modularity", "density", "centrality", "compare", "p-value", "metric")
_SUMMARY_HINTS = ("summary", "summarize", "thematic", "community pattern")


def classify(question: str) -> Intent:
    """Return the routed :class:`Intent` for a question (placeholder heuristic)."""
    q = question.lower()
    if any(h in q for h in _SUMMARY_HINTS):
        return Intent.COMMUNITY_SUMMARY
    if any(h in q for h in _STRUCTURED_HINTS):
        return Intent.STRUCTURED_QUERY
    return Intent.SEMANTIC_SEARCH
