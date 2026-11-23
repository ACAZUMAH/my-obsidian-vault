# Vault Workflow Guide

This is the canonical sequence for retrieving existing knowledge, integrating evidence, maintaining shared pages safely, validating the result, and publishing exactly the intended change.

## Before Editing

1. Read `index.md` and the relevant project, concept, or synthesis pages.
2. Search with `rg` before creating a page so existing ownership and terminology are reused.
3. Read the live [AGENTS.md](../AGENTS.md), relevant local skill, and machine contract.
4. Identify the evidence boundary and exclude secrets, private identifiers, generated output, dependencies, and unrelated tool chatter.
5. Check Git status and reread every shared note immediately before patching.

## Ingest Workflow

Use [llm-wiki-ingest](../.agents/skills/llm-wiki-ingest/SKILL.md) for source ingestion, conversation harvests, and durable evidence promotion.

1. Preserve raw evidence under `raw/` without rewriting it.
2. Create or update a concise Source Record that points to the preserved raw evidence; do not duplicate exhaustive evidence or transcript detail.
3. Promote only supported claims into existing concept, entity, project, question, and synthesis pages.
4. Preserve contradictions, current-versus-historical differences, confidence, and open questions.
5. Update `index.md` and append exactly one `log.md` entry.
6. Run the canonical validator, review the exact diff, and publish (see Maintenance And Publish Workflow).

Conversation harvests require direct conversation evidence before project knowledge is promoted. A repository match, saved session, profile-memory write, or agent inference is not equivalent to an integrated source.

## Query Workflow

Use [llm-wiki-query](../.agents/skills/llm-wiki-query/SKILL.md) for retrieval, vault-backed answers, and authorized durable filing.

1. Start with `index.md` and search the wiki.
2. Read the smallest relevant page set.
3. Consult raw evidence only to verify exact evidence, resolve ambiguity, or fill a documented gap.
4. Cite stable vault pages and distinguish fact, source claim, and inference.
5. File the answer only when it is durable and useful beyond the immediate exchange. Then file it without asking, publish it, and tell the user where it went.

## Lint Workflow

Use [llm-wiki-lint](../.agents/skills/llm-wiki-lint/SKILL.md) with the canonical [lint checklist](lint-checklist.md). Separate structural validation from semantic review. Apply non-destructive repairs directly with `vault-maintenance` and report them; merges, deletions, renames, raw-evidence changes, and contradiction resolutions that discard a claim need approval.

## Maintenance And Publish Workflow

Capture first and publish every change in the same turn; see Capture And Publish in [AGENTS.md](../AGENTS.md).

1. Apply focused edits; never overwrite unrelated concurrent work.
2. Run `python3 scripts/wiki_tool.py check` and complete the [Vault Lint Checklist](lint-checklist.md).
3. Review `git diff --check` and the exact diff of the files you changed.
4. Publish exactly those files with a scoped message that describes the durable outcome: `python3 scripts/wiki_tool.py publish -m "<message>" -- <paths>`. It commits only the named paths, gates on a secret scan and on the canonical validator run against the exact committed tree, and pushes.
5. Tell the user what was added and the short commit hash. On `PUBLISH=BLOCKED`, fix the content and publish again; never bypass a gate. On `push=diverged`, stop and ask the user.

## Concurrent Writers

Hermes, Codex, Obsidian, and other agents may edit the vault concurrently. A clean read from earlier in a task is not sufficient; reread each shared note immediately before modifying it.

## References

- [Vault operating authority](../AGENTS.md)
- [Vault-maintenance skill](../.agents/skills/vault-maintenance/SKILL.md)
- [Canonical validator documentation](../scripts/README.md)
- [Naming conventions](naming-conventions.md)
- [Project-local skills](local-skills.md)
