---
type: concept
status: active
created: 2026-07-22
updated: 2026-07-22
tags: [vault, naming, conventions, paths]
sources: []
---

# Vault Naming Conventions

## Working Definition

Vault naming conventions keep filenames stable, page titles readable, links predictable, and content ownership visible from its path.

## Current Synthesis

### Wiki page filenames

Use lowercase kebab-case and place the file under the directory owned by its page type.

| Page type | Pattern | Example |
| --- | --- | --- |
| Source | `wiki/sources/source-title.md` | `wiki/sources/llm-wiki-idea.md` |
| Concept | `wiki/concepts/concept-name.md` | `wiki/concepts/vault-schema-reference.md` |
| Entity | `wiki/entities/entity-name.md` | `wiki/entities/obsidian.md` |
| Project | `wiki/projects/project-name.md` | `wiki/projects/compflow-backend.md` |
| Question | `wiki/questions/question-slug.md` | `wiki/questions/first-ingest-example.md` |
| Synthesis | `wiki/syntheses/synthesis-title.md` | `wiki/syntheses/software-development-operating-manual.md` |

The filename is the stable ID. The first H1 is the human-readable title and may use capitalization, punctuation, or a fuller product name.

### Link naming

- Use Obsidian wikilinks for vault notes: `[[path/to/page|Readable Label]]`.
- Prefer explicit paths when duplicate stems or cross-directory ownership could be ambiguous.
- Use relative Markdown links for raw evidence and repository files.
- Link project knowledge to `wiki/projects/`, never to a parallel `entities/projects` tree.

### Templates, skills, and contracts

- Templates live in `_template/` and use `*-template.md` filenames.
- A local skill lives at `.agents/skills/<skill-name>/SKILL.md`; its frontmatter `name` must equal the directory name.
- Supporting skill material lives below that skill, normally under `references/`.
- Machine contracts use descriptive lowercase filenames under `schema/`.

### Evidence naming

Keep imported filenames when provenance depends on them. For agent-created harvest manifests, prefer a date-prefixed descriptive name such as `YYYY-MM-DD-project-purpose-batch-N.md`. Never put credentials, private identifiers, or secret values in filenames.

> [!note] Rename discipline
> Renaming a stable page ID requires updating inbound links, `index.md`, schema/template references when applicable, and the operation log. Do not create an alias page merely to avoid fixing links.

## Supporting Sources

- [File naming and directory conventions](../../AGENTS.md)
- [Canonical path contract](../../schema/vault-structure.json)

## Related

- [[vault-schema-reference|Vault Schema Reference]]
- [[vault-workflow-guide|Vault Workflow Guide]]
- [[vault-lint-checklist|Vault Lint Checklist]]
- [[project-local-agent-skills|Project-Local Agent Skills]]

## Open Questions

- Should date-prefixed raw-manifest naming become a machine-enforced convention?
- Should aliases be required when a project’s public name differs materially from its repository name?
