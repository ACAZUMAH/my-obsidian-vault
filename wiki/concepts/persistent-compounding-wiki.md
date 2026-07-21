---
type: concept
status: active
created: 2026-05-13
updated: 2026-05-13
tags: [knowledge-management, llm-wiki, synthesis]
sources:
  - ../sources/llm-wiki-idea.md
---

# Persistent Compounding Wiki

## Working Definition

A persistent compounding wiki is a knowledge base where an LLM incrementally integrates sources into durable, interlinked markdown pages. It differs from basic retrieval workflows because synthesis, contradictions, cross-references, and summaries are maintained over time rather than regenerated from scratch on each question.

## Current Synthesis

The key move is to place a maintained wiki between the user and the raw source collection. Raw documents remain immutable evidence, while the wiki becomes the current working model of what those sources collectively imply.

This makes knowledge compound in three ways. First, new sources update existing pages instead of creating isolated summaries. Second, useful answers to user questions can become new wiki pages. Third, maintenance operations can strengthen links, expose contradictions, and turn scattered notes into reusable synthesis.

The human role is not eliminated. The user still selects sources, directs emphasis, evaluates judgment calls, and asks meaningful questions. The LLM handles the maintenance burden that usually causes personal wikis to decay.

## Supporting Sources

- [[../sources/llm-wiki-idea|LLM Wiki Idea]]

## Related

- [[raw-source-wiki-schema-architecture|Raw Source, Wiki, Schema Architecture]]
- [[ingest-query-lint-workflows|Ingest, Query, Lint Workflows]]
- [[../syntheses/llm-wiki-operating-model|LLM Wiki Operating Model]]

## Open Questions

- What level of automation gives the best balance between velocity and user trust?
- Which page types should be added once a real domain emerges?
- How should confidence and contradiction status be represented across many pages?
