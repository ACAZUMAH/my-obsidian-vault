---
name: llm-wiki-ingest
description: Integrate user-provided documents, conversation evidence, approved archive records, and project-knowledge harvests into the canonical Obsidian vault. Use when asked to ingest, import, harvest, promote, or add durable source-backed knowledge.
---

# LLM Wiki Ingest

## Authority

1. Read the live [vault authority](../../../AGENTS.md), [index](../../../index.md), and [workflow guide](../../../schema/workflows.md).
2. Follow [vault-maintenance](../vault-maintenance/SKILL.md) for every mutation, concurrent-writer reread, validation, index/log update, and Git review.
3. Use the applicable page template and any task-specific procedure, including the [Codex project-knowledge harvest](../../../wiki/concepts/codex-project-knowledge-harvest.md).

## Workflow

1. Establish the authorized source, archive, project-family, and batch boundary before extracting claims.
2. Preserve attributable evidence under `raw/` without rewriting an existing raw file. Exclude secrets, credentials, private identifiers, generated output, dependencies, and unrelated tool chatter.
3. Create or update a concise Source Record under `wiki/sources/` using the [Source Record template](../../../_template/source-summary-template.md). Reference every covered raw file and retain only decision-relevant claims, details, connections, tensions, and questions.
4. Promote supported knowledge into existing concept, entity, project, question, and synthesis pages. Search before creating, preserve contradictions, and distinguish historical evidence from current verification.
5. Update `index.md` for every new durable page and append exactly one `log.md` entry for the completed ingest operation.
6. Run `python3 scripts/validate_vault.py`, review the exact diff, and report evidence boundaries and verification accurately.

## Guardrails

- Require directly relevant conversation evidence before creating a project page during a conversation harvest. Use repository inspection only to verify conversation-derived claims.
- Never substitute a different archive, repository match, saved session, or agent inference for the requested evidence source.
- Never copy secret values, full private transcripts, private payloads, or sensitive identifiers into this public vault.
- Preserve existing raw evidence and concurrent changes unless the user explicitly authorizes a targeted change.
- Do not commit or push unless the user requests it.

## Completion Criteria

- Cover every new raw file with an indexed Source Record.
- Connect promoted claims to their provenance.
- Preserve contradictions, confidence, current-versus-historical boundaries, and open questions.
- Pass the canonical validator and applicable privacy, link, and diff checks.
