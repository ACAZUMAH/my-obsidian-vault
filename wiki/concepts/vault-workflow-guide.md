---
type: concept
status: active
created: 2026-07-22
updated: 2026-07-22
tags: [vault, workflow, maintenance, obsidian]
sources: []
---

# Vault Workflow Guide

## Working Definition

The vault workflow is the repeatable sequence for retrieving existing knowledge, integrating new evidence, maintaining shared pages safely, validating the result, and committing only the intended change.

## Current Synthesis

### Before editing

1. Read `index.md` and the relevant project, concept, or synthesis pages.
2. Search with `rg` before creating a page so existing ownership and terminology are reused.
3. Read the live `AGENTS.md`, relevant local skill, and machine contract.
4. Identify the evidence boundary and exclude secrets, private identifiers, generated output, dependencies, and unrelated tool chatter.
5. Check Git status and reread every shared note immediately before patching.

### Ingest workflow

1. Preserve raw evidence under `raw/` without rewriting it.
2. Create or update one source summary.
3. Promote only supported claims into existing concept, entity, project, question, and synthesis pages.
4. Preserve contradictions, current-versus-historical differences, confidence, and open questions.
5. Update `index.md` and append exactly one `log.md` entry.
6. Run the canonical validator and review the exact diff.

Conversation harvests require direct conversation evidence before project knowledge is promoted. A repository match, saved session, profile-memory write, or agent inference is not equivalent to an integrated source.

### Query workflow

1. Start with `index.md` and search the wiki.
2. Read the smallest relevant page set.
3. Consult raw evidence only to verify ambiguity or fill a documented gap.
4. Cite stable vault pages and distinguish fact, source claim, and inference.
5. File the answer only when it is durable and useful beyond the immediate exchange.

### Maintenance and commit workflow

1. Apply focused edits; never overwrite unrelated concurrent work.
2. Run [[vault-lint-checklist|Vault Lint Checklist]].
3. Review `git status`, `git diff --check`, and the exact diff.
4. Stage explicit intended paths rather than every dirty file.
5. Commit with a scoped message that describes the durable outcome.
6. Push only when explicitly requested.

> [!warning] Shared-writer rule
> Hermes, Codex, Obsidian, and other agents may edit the vault concurrently. A clean read from earlier in a task is not sufficient; reread each shared note immediately before modifying it.

## Supporting Sources

- [Vault operating authority](../../AGENTS.md)
- [Vault-maintenance skill](../../.agents/skills/vault-maintenance/SKILL.md)
- [Canonical validator documentation](../../scripts/README.md)

## Related

- [[ingest-query-lint-workflows|Ingest, Query, Lint Workflows]]
- [[vault-schema-reference|Vault Schema Reference]]
- [[vault-naming-conventions|Vault Naming Conventions]]
- [[vault-lint-checklist|Vault Lint Checklist]]
- [[project-local-agent-skills|Project-Local Agent Skills]]

## Open Questions

- Which recurring maintenance checks should become automated without making the validator overly prescriptive?
- When should a frequently repeated workflow graduate into a dedicated local skill?
