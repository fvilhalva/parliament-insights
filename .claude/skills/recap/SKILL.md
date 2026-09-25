---
name: recap
description: Recap and review the Parliament Insights project — read all engineering docs and CLAUDE.md, then report what the project is, its requirements/architecture, the working rules, and the current state (git + roadmap). Use when the user runs /recap or asks for a project recap, refresher, or "where are we".
---

# /recap — Project recap & review

Goal: give the user (and yourself) a fast, accurate refresher on **what
Parliament Insights is, how it must be built, and where it currently stands** —
without changing any files. This skill is **read-only**.

## Steps

1. **Read the working agreement.** Read [`CLAUDE.md`](../../../CLAUDE.md) in full
   — especially the git/branching rules and architectural guardrails.

2. **Read the engineering docs.** Read every Markdown file under
   [`docs/`](../../../docs/), starting with `docs/README.md`, then `01`…`10` and
   `docs/adr/*`. These mirror the SAD (PDFs in `docs/`). Extract:
   - purpose & scope (01),
   - functional/non-functional requirements (02),
   - architecture & layering (03),
   - data model (04), API design (05), use cases (06),
   - testing/security/HPC (07–09), roadmap & current status (10),
   - accepted ADRs (`docs/adr/`).

3. **Inspect current state (read-only git).** Run:
   ```bash
   git branch --show-current
   git log --oneline -10
   git status --short
   gh pr list --state open        # if gh is available
   ```
   Note the current branch, whether it's a protected branch, open PRs, and any
   uncommitted work.

4. **Cross-check the roadmap.** Compare `docs/10-roadmap.md` "Current status"
   against what the code/branches actually show, and flag drift.

## Output

Produce a concise recap with these sections:

- **What it is** — one paragraph.
- **Rules in force** — the branching model (`main → develop → feat/*`) and the
  hard rule: never merge `main`/`develop` without a PR + the owner's approval;
  always start a new task on a new branch off `develop`.
- **Requirements & architecture** — the essentials (FR/NFR highlights, the
  layered design, key guardrails NFR01/NFR07/NFR10/FR06).
- **Where we are now** — current branch, open PRs, roadmap milestone (V1…V5),
  and any TODO/drift.
- **Suggested next step** — the single most sensible next action, and (if it's a
  new task) the branch name you'd create for it.

Keep it tight. Do **not** edit files, commit, push, or merge during a recap.
