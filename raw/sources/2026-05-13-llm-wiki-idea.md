# LLM Wiki

A pattern for building personal knowledge bases using LLMs.

This source was provided by the user on 2026-05-13 as the seed idea file for this vault. It describes an LLM-maintained wiki architecture with three layers: immutable raw sources, an LLM-owned markdown wiki, and a schema file that governs maintenance behavior.

## Core Idea

Most LLM document workflows resemble RAG: upload files, retrieve chunks at query time, and generate answers. This works, but the LLM rediscovers knowledge from scratch on every question. The proposed alternative is a persistent wiki that is incrementally built and maintained by the LLM.

When a new source is added, the LLM reads it, extracts key information, and integrates it into the existing wiki by updating entity pages, concept pages, summaries, contradictions, and syntheses. The wiki becomes a persistent, compounding artifact.

## Applications

The source proposes many use cases:

- Personal goals, health, psychology, and self-improvement.
- Research projects that accumulate papers, reports, and evolving theses.
- Book companion wikis for chapters, characters, themes, plot threads, and references.
- Business or team wikis fed by Slack, meetings, project documents, and customer calls.
- Competitive analysis, due diligence, trip planning, course notes, and hobby research.

## Architecture

The architecture has three layers:

1. Raw sources: immutable curated files and assets.
2. The wiki: LLM-generated markdown pages, summaries, entity pages, concept pages, comparisons, and syntheses.
3. The schema: an instruction document such as `AGENTS.md` that tells the LLM how the wiki is structured and how to operate.

## Operations

The source defines three main operations:

- Ingest: read a new source, summarize it, update affected pages, cross-reference, and log the work.
- Query: answer questions against the wiki, using the index first, then relevant pages, and optionally filing durable answers back into the wiki.
- Lint: periodically health-check the wiki for contradictions, stale claims, orphans, missing pages, weak links, and research gaps.

## Indexing And Logging

The source recommends two special files:

- `index.md`: content-oriented catalog of wiki pages.
- `log.md`: chronological append-only record of ingests, queries, lint passes, and maintenance.

## Optional Tools

The source mentions optional tooling such as local markdown search, Obsidian Web Clipper, local image downloads, Obsidian graph view, Marp, Dataview, and git.

## Rationale

The source argues that humans abandon wikis because maintenance is tedious. LLMs can handle repetitive bookkeeping such as cross-references, contradictions, and summaries, while humans focus on source curation and high-level thinking.
