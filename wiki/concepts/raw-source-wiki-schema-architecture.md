---
type: concept
status: active
created: 2026-05-13
updated: 2026-05-13
tags: [architecture, llm-wiki]
sources:
  - ../sources/llm-wiki-idea.md
---

# Raw Source, Wiki, Schema Architecture

## Working Definition

The raw source, wiki, schema architecture separates evidence, generated knowledge, and operating rules into three layers.

## Current Synthesis

The architecture prevents source drift and makes the agent's responsibilities explicit. `raw/` stores immutable evidence. `wiki/` stores the maintained interpretation of that evidence. `AGENTS.md` defines the conventions and workflows that keep the wiki coherent across sessions.

This separation matters because the agent can aggressively maintain the wiki without corrupting original sources. It can revise summaries, add links, and update synthesis pages while leaving the raw evidence intact for verification.

## Supporting Sources

- [[../sources/llm-wiki-idea|LLM Wiki Idea]]

## Related

- [[persistent-compounding-wiki|Persistent Compounding Wiki]]
- [[ingest-query-lint-workflows|Ingest, Query, Lint Workflows]]
- [[../syntheses/llm-wiki-operating-model|LLM Wiki Operating Model]]

## Open Questions

- Should raw sources be organized by date, domain, source type, or project?
- Should source metadata live only in wiki summaries, or should raw sources also receive sidecar metadata files?
