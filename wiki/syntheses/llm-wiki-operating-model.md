---
type: synthesis
status: active
created: 2026-05-13
updated: 2026-07-20
tags: [llm-wiki, second-brain, operating-model]
sources:
  - ../sources/llm-wiki-idea.md
  - ../sources/hermes-obsidian-second-brain-kickoff.md
confidence: medium
---

# LLM Wiki Operating Model

## Thesis

This vault should operate as a maintained second brain where sources are preserved, wiki pages are continuously synthesized, and durable answers become part of the knowledge base. The system works because it assigns the tedious maintenance work to the LLM while preserving human control over source selection and interpretive direction.

## Evidence

The seed source defines a clear distinction between query-time retrieval and persistent knowledge accumulation. It argues that RAG-like workflows repeatedly rediscover information, while an LLM-maintained wiki preserves synthesized knowledge as durable markdown.

The source also defines practical operating primitives: immutable raw sources, LLM-owned wiki pages, a schema file, an index, a log, and recurring ingest/query/lint workflows.

## Implications

The agent should treat wiki maintenance as a first-class obligation, not as an optional side effect. When a source is ingested, the work is incomplete until affected pages, `index.md`, and `log.md` are updated.

The user should be able to browse the wiki in Obsidian and see the knowledge graph become richer over time. Important answers should not stay trapped in chat history when they can become reusable wiki pages.

Durable information about how the user works should be captured selectively and linked through the personal operating manual. Hermes memory provides the always-loaded pointer and compact preferences; the vault provides the detailed, maintainable source of truth.

## Contradictions Or Tensions

The source emphasizes that the LLM owns the wiki, but real use may involve user edits. The current policy is pragmatic: the agent maintains `wiki/` by default, but must preserve and work with user edits rather than overwrite them casually.

## Related

- [[../concepts/persistent-compounding-wiki|Persistent Compounding Wiki]]
- [[../concepts/raw-source-wiki-schema-architecture|Raw Source, Wiki, Schema Architecture]]
- [[../concepts/ingest-query-lint-workflows|Ingest, Query, Lint Workflows]]
- [[../entities/obsidian|Obsidian]]
- [[../entities/hermes-agent|Hermes Agent]]
- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Obsidian Memory Architecture]]
- [[personal-operating-manual|Personal Operating Manual]]

## Sources

- [[../sources/llm-wiki-idea|LLM Wiki Idea]]
- [[../sources/hermes-obsidian-second-brain-kickoff|Hermes–Obsidian Second Brain Kickoff]]

## Open Questions

- Which domain should this second brain ingest next?
- What threshold should trigger adding a proper local search tool?
