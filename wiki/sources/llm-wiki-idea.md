---
type: source
status: active
created: 2026-05-13
updated: 2026-05-13
tags: [llm-wiki, knowledge-management, second-brain]
sources:
  - ../../raw/sources/2026-05-13-llm-wiki-idea.md
source_date: 2026-05-13
ingested: 2026-05-13
---

# LLM Wiki Idea

## Source

- Raw file: [2026-05-13-llm-wiki-idea.md](../../raw/sources/2026-05-13-llm-wiki-idea.md)
- Date: 2026-05-13
- Author: User-provided idea file
- Ingested: 2026-05-13

## Core Claims

The source argues that many document-based LLM workflows behave like query-time RAG: they retrieve chunks from raw files and synthesize answers on demand. That can work, but the system repeatedly reconstructs knowledge rather than accumulating it.

The proposed alternative is an LLM-maintained markdown wiki. New sources are integrated into durable wiki pages once, including source summaries, entity pages, concept pages, comparisons, contradictions, and evolving syntheses. The wiki becomes a compounding artifact that improves with each source and each durable question.

The human remains responsible for curation, exploration, and judgment. The LLM is responsible for maintenance: summarizing, linking, updating, filing, contradiction tracking, and bookkeeping.

## Useful Details

- The architecture has three layers: immutable raw sources, an LLM-owned wiki, and an operating schema such as `AGENTS.md`.
- The main operations are ingest, query, and lint.
- `index.md` should be content-oriented and help the agent navigate the wiki before answering.
- `log.md` should be chronological and append-only, with parseable headings.
- Obsidian can act as the human-facing IDE for browsing, graph view, linking, and plugins.
- Durable query answers can be filed back into the wiki so exploration compounds rather than disappearing into chat history.
- Optional tools include local markdown search, qmd, Obsidian Web Clipper, local attachment downloads, Marp, Dataview, and git.

## Connections

- [[../concepts/persistent-compounding-wiki|Persistent Compounding Wiki]]
- [[../concepts/raw-source-wiki-schema-architecture|Raw Source, Wiki, Schema Architecture]]
- [[../concepts/ingest-query-lint-workflows|Ingest, Query, Lint Workflows]]
- [[../entities/obsidian|Obsidian]]
- [[../syntheses/llm-wiki-operating-model|LLM Wiki Operating Model]]

## Contradictions Or Tensions

No contradictions have been found yet because this is the first ingested source.

Potential tension: the source says the LLM owns the wiki entirely, but in practice the user may sometimes want manual edits. This schema resolves that by treating `wiki/` as LLM-maintained by default while not forbidding explicit user-directed edits.

## Open Questions

- At what wiki size does `index.md` plus `rg` stop being sufficient?
- Should this vault eventually use Dataview frontmatter conventions more heavily?
- Should durable query answers be filed automatically by default, or only when explicitly requested?
- What domains will this second brain prioritize first?
