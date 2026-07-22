---
type: concept
status: active
created: 2026-05-13
updated: 2026-07-22
tags: [architecture, llm-wiki]
sources:
  - ../sources/llm-wiki-idea.md
---

# Raw Source, Wiki, Schema Architecture

## Working Definition

The raw source, wiki, schema architecture separates immutable evidence, curated knowledge, and operating rules into three layers.

## Current Synthesis

The architecture prevents source drift and makes the agent's responsibilities explicit. `raw/` stores immutable evidence. `wiki/` stores the maintained interpretation of that evidence. Within the wiki, Source Records under `wiki/sources/` provide concise provenance and retrieval nodes that point back to raw files; they are not second copies of the evidence. `AGENTS.md` defines the conventions and workflows that keep the wiki coherent across sessions.

This separation matters because the agent can aggressively maintain the wiki without corrupting original sources. It can refine Source Records, add links, and update synthesis pages while leaving the raw evidence intact for exact verification. Aggregated records and shared evidence are valid when every relationship stays explicit.

The operational schema is documented in the canonical [Vault Schema Reference](../../schema/README.md), including the authority hierarchy, path map, frontmatter contract, page-type ownership, and coordinated-update rule.

## Supporting Sources

- [[../sources/llm-wiki-idea|LLM Wiki Idea]]

## Related

- [[persistent-compounding-wiki|Persistent Compounding Wiki]]
- [[ingest-query-lint-workflows|Ingest, Query, Lint Workflows]]
- [Vault Schema Reference](../../schema/README.md)
- [Vault Naming Conventions](../../schema/naming-conventions.md)
- [Project-Local Agent Skills](../../schema/local-skills.md)
- [[../syntheses/llm-wiki-operating-model|LLM Wiki Operating Model]]

## Open Questions

- Should raw sources be organized by date, domain, source type, or project?
- Should semantic concision checks for Source Records remain human-reviewed, or can a stable subset eventually be automated?
