from parliament_agent.graph import AgentState, route
from parliament_agent.router import Intent, classify


def test_structured_intent():
    assert classify("What was the modularity in 2024?") is Intent.STRUCTURED_QUERY


def test_summary_intent():
    assert classify("Give me a thematic summary of community 3") is Intent.COMMUNITY_SUMMARY


def test_semantic_default():
    assert classify("environmental proposals by community 3") is Intent.SEMANTIC_SEARCH


def test_route_sets_intent_on_state():
    state = route(AgentState(question="compare density across years"))
    assert state.intent is Intent.STRUCTURED_QUERY
