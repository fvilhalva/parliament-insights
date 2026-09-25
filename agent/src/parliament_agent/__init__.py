"""Parliament Insights — Agent Orchestration + Tools layer.

See ../../docs/03-architecture.md. This package classifies question intent
(FR05), routes to a tool (structured query / RAG / summarizer), and aggregates
the result. It never touches the database directly — the tools do.
"""

__version__ = "0.1.0"
