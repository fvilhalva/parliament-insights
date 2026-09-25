"""Orchestration state machine (LangGraph).

SKELETON: describes the intended graph shape without importing langgraph (an
optional 'runtime' dependency). The real implementation builds a StateGraph:

    classify -> {structured_query | rag | summarizer} -> aggregate

Each node delegates to a tool in ``parliament_agent.tools``; the graph keeps no
shared in-memory state between requests (NFR03).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .router import Intent, classify


@dataclass
class AgentState:
    question: str
    context: dict[str, Any] = field(default_factory=dict)
    intent: Intent | None = None
    answer: str | None = None
    sources: list[dict[str, Any]] = field(default_factory=list)
    generated_by_llm: bool = False


def route(state: AgentState) -> AgentState:
    """First node: classify intent (FR05)."""
    state.intent = classify(state.question)
    return state


def build_graph():  # noqa: ANN201 - returns a langgraph object when runtime deps present
    """Construct the compiled LangGraph. Requires the 'runtime' extra."""
    raise NotImplementedError(
        "Install runtime deps and implement the StateGraph: "
        "classify -> tool -> aggregate (see docs/06-use-cases.md)."
    )
