---
type: concept
status: active
created: 2026-05-13
updated: 2026-07-22
tags: [workflow, llm-wiki]
sources:
  - ../sources/llm-wiki-idea.md
---

# Ingest, Query, Lint Workflows

## Working Definition

Ingest, query, and lint are the three recurring operating modes of the LLM Wiki.

## Current Synthesis

Ingest adds new evidence to the knowledge base. The agent reads a raw source, creates a source summary, updates relevant pages, adds links, flags contradictions, updates the index, and appends to the log.

Query uses the maintained wiki to answer user questions. The agent reads `index.md`, searches the wiki, consults relevant pages, verifies against raw sources when needed, and files durable answers back into the wiki when useful.

Lint maintains wiki health. The agent looks for broken links, stale claims, missing concept pages, contradictions, orphan pages, duplicated pages, weak citations, and research gaps.

Detailed execution guidance lives in [[vault-workflow-guide|Vault Workflow Guide]]. The structural, semantic, provenance, security, and Git completion checks are maintained in [[vault-lint-checklist|Vault Lint Checklist]].

## Supporting Sources

- [[../sources/llm-wiki-idea|LLM Wiki Idea]]

## Related

- [[persistent-compounding-wiki|Persistent Compounding Wiki]]
- [[raw-source-wiki-schema-architecture|Raw Source, Wiki, Schema Architecture]]
- [[vault-workflow-guide|Vault Workflow Guide]]
- [[vault-naming-conventions|Vault Naming Conventions]]
- [[vault-lint-checklist|Vault Lint Checklist]]
- [[project-local-agent-skills|Project-Local Agent Skills]]

## Open Questions

- How often should linting be run?
- What should count as a durable query answer worth filing?
- Should ingest always include a user review step, or should low-risk sources be processed automatically?
