# 01 — Overview

## Context

The *Parliament Graph Architecture* project (undergraduate thesis) produced a
reproducible pipeline for analyzing parliamentary co-authorship networks,
statistically validated against null models (hypothesis H1, `p < 0.005` across
four consecutive years, 2022–2025). That thesis is intentionally **closed** as a
scientific artifact: its responsibility ends at generating auditable indicators
(`analysis_{year}.json`, per-deputy metrics CSV, GEXF, and SQLite).

The **Parliament Insights API** is a *separate system* that consumes those
artifacts as a **read-only data source** and adds a product layer: a traditional
backend API (NestJS) combined with a Generative-AI layer (RAG, agents, and
LLM-based summarization) — **without ever altering the thesis's statistical
validation core**.

## Objectives

- Demonstrate Software Engineering competence in a system that integrates a
  traditional backend, AI-agent orchestration, and vector-data infrastructure.
- Serve as technical-portfolio material aligned with Generative-AI Data
  Scientist / Engineer roles: Transformer architecture, RAG, agents, and
  HPC-readiness practices (containerization, queues, separation of compute
  layers).
- Preserve the methodological integrity of the thesis, treating it as an
  **immutable source of truth**.

## Scope

**In scope:** functional & non-functional requirements, use cases, layered
architecture, data model, main flows, API design, technology stack, testing
strategy, security & infrastructure considerations, and roadmap.

**Out of scope:** the thesis's statistical methodology (documented in its own
README) and, until implementation begins, full production source code.

## Target Audience

Technical recruiters, portfolio reviewers, the academic advisor, and the author
himself as an implementation reference.
