---
type: question
status: active
created: 2026-05-13
updated: 2026-05-13
tags: [workflow, ingest-example]
sources:
  - ../sources/llm-wiki-idea.md
---

# First Ingest Example

## Short Answer

The seed source, "LLM Wiki," was ingested by preserving the original idea as a raw source, creating a source summary, extracting core concepts, creating one tool/entity page, writing a starter synthesis, updating the index, and logging the operation.

## Analysis

The ingest followed the schema's three-layer model. The raw source lives at [2026-05-13-llm-wiki-idea.md](../../raw/sources/2026-05-13-llm-wiki-idea.md) and should not be modified during normal wiki maintenance.

The source summary lives at [[../sources/llm-wiki-idea|LLM Wiki Idea]]. It captures the core claims, useful details, connections, tensions, and open questions from the raw source.

The ingest created three concept pages:

- [[../concepts/persistent-compounding-wiki|Persistent Compounding Wiki]]
- [[../concepts/raw-source-wiki-schema-architecture|Raw Source, Wiki, Schema Architecture]]
- [[../concepts/ingest-query-lint-workflows|Ingest, Query, Lint Workflows]]

It also created one entity page for [[../entities/obsidian|Obsidian]], because Obsidian is a named tool with recurring operational importance.

Finally, the ingest created [[../syntheses/llm-wiki-operating-model|LLM Wiki Operating Model]] to preserve the high-level operating thesis of the system. `index.md` now catalogs all starter pages, and `log.md` records the setup operation chronologically.

## Citations

- [[../sources/llm-wiki-idea|LLM Wiki Idea]]
- [Raw seed source](../../raw/sources/2026-05-13-llm-wiki-idea.md)

## Follow-Up Questions

- What real source should be ingested next?
- Which domain should this second brain prioritize first?
- Should durable query answers be filed automatically by default?
