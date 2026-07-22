# Vault Workflow Guide

This is the canonical sequence for retrieving existing knowledge, integrating evidence, maintaining shared pages safely, validating the result, and committing only the intended change.

## Before Editing

1. Read `index.md` and the relevant project, concept, or synthesis pages.
2. Search with `rg` before creating a page so existing ownership and terminology are reused.
3. Read the live [AGENTS.md](../AGENTS.md), relevant local skill, and machine contract.
4. Identify the evidence boundary and exclude secrets, private identifiers, generated output, dependencies, and unrelated tool chatter.
5. Check Git status and reread every shared note immediately before patching.

## Ingest Workflow

1. Preserve raw evidence under `raw/` without rewriting it.
2. Create or update a concise Source Record that points to the preserved raw evidence; do not duplicate exhaustive evidence or transcript detail.
3. Promote only supported claims into existing concept, entity, project, question, and synthesis pages.
4. Preserve contradictions, current-versus-historical differences, confidence, and open questions.
5. Update `index.md` and append exactly one `log.md` entry.
6. Run the canonical validator and review the exact diff.

Conversation harvests require direct conversation evidence before project knowledge is promoted. A repository match, saved session, profile-memory write, or agent inference is not equivalent to an integrated source.

## Query Workflow

1. Start with `index.md` and search the wiki.
2. Read the smallest relevant page set.
3. Consult raw evidence only to verify exact evidence, resolve ambiguity, or fill a documented gap.
4. Cite stable vault pages and distinguish fact, source claim, and inference.
5. File the answer only when it is durable and useful beyond the immediate exchange.

## Maintenance And Commit Workflow

1. Apply focused edits; never overwrite unrelated concurrent work.
2. Run the [Vault Lint Checklist](lint-checklist.md).
3. Review `git status`, `git diff --check`, and the exact diff.
4. Stage explicit intended paths rather than every dirty file.
5. Commit with a scoped message that describes the durable outcome.
6. Push only when explicitly requested.

## Concurrent Writers

Hermes, Codex, Obsidian, and other agents may edit the vault concurrently. A clean read from earlier in a task is not sufficient; reread each shared note immediately before modifying it.

## References

- [Vault operating authority](../AGENTS.md)
- [Vault-maintenance skill](../.agents/skills/vault-maintenance/SKILL.md)
- [Canonical validator documentation](../scripts/README.md)
- [Naming conventions](naming-conventions.md)
- [Project-local skills](local-skills.md)
