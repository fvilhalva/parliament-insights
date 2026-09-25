"""Structured Query Tool (FR01, FR04).

Deterministic: returns thesis-validated numbers verbatim from the database. The
LLM NEVER computes a validated metric (NFR01). SKELETON — no DB wired yet.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MetricResult:
    year: int
    field: str
    value: float
    source: str  # e.g. "AnalysisResult"


def query_metric(year: int, metric: str) -> MetricResult:
    """Run a parameterized query for a validated metric. Not implemented yet."""
    raise NotImplementedError(
        "SELECT ... FROM analysis_result WHERE year = %(year)s (see data/schema.sql)"
    )
