"""Summarizer Tool (FR03, FR07).

Batch/offline: collects the summaries of all propositions co-authored by a
Louvain community, generates a thematic summary via the LLM, and caches it in
CommunitySummary so the API serves it with no new LLM call (FR07). Runs in a
stateless worker (NFR03). SKELETON — no queue/DB wired yet.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SummaryJob:
    community_id: int
    year: int


def summarize_community(job: SummaryJob) -> str:
    """Generate (and cache) the thematic summary for a community/year."""
    raise NotImplementedError(
        "fetch proposition summaries -> LLM summarize -> INSERT CommunitySummary"
    )
