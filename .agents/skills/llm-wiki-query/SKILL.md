---
name: llm-wiki-query
description: Retrieve and answer questions from the canonical Obsidian vault with stable provenance. Use when asked what the vault knows, to find project decisions or preferences, to answer from existing notes, or to file a durable answer.
---

# LLM Wiki Query

## Authority

1. Read the live [vault authority](../../../AGENTS.md), [index](../../../index.md), and [query workflow](../../../schema/workflows.md).
2. Follow [vault-maintenance](../vault-maintenance/SKILL.md) only when the query is authorized to create or update durable vault content.

## Retrieval Workflow

1. Start with `index.md`, then search the wiki with `rg` before consulting raw evidence.
2. Read the smallest relevant set of synthesis, project, concept, question, and Source Record pages.
3. Consult `raw/sources/` only to verify exact evidence, resolve ambiguity, or fill a documented gap.
4. Distinguish current fact, historical source claim, contradiction, and inference. Verify temporally unstable implementation facts against live systems or repositories when they are in scope.
5. Answer directly with stable vault links or raw-evidence links as appropriate. Do not ask the user to repeat an established preference or decision that the vault already records.

## Filing Decision

- Remain read-only for ordinary questions.
- File an answer only when the user explicitly requests it or the durable-capture rules in `AGENTS.md` authorize automatic promotion.
- Prefer updating an existing page over creating a competing page.
- When filing, follow `vault-maintenance`, update `index.md` when navigation changes, append exactly one `log.md` entry, and run the canonical validator.
- Do not create a Source Record unless new evidence is actually being ingested.

## Completion Criteria

- Answer from the smallest sufficient evidence set.
- Cite provenance and label uncertainty or inference.
- Leave the vault unchanged when filing is not authorized.
- Validate and report the exact durable changes when filing occurs.
