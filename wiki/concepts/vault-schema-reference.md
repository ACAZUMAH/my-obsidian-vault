---
type: concept
status: active
created: 2026-07-22
updated: 2026-07-22
tags: [vault, schema, reference, obsidian]
sources: []
---

# Vault Schema Reference

## Working Definition

The vault schema is the coordinated human-readable and machine-readable contract that defines where knowledge belongs, which page types exist, what metadata and sections they require, and how structural validity is checked.

## Current Synthesis

### Authority and enforcement

| Layer | File | Responsibility |
| --- | --- | --- |
| Human authority | [AGENTS.md](../../AGENTS.md) | Meaning, workflow, naming, citation, concurrency, index, and log rules |
| Structural contract | [vault-structure.json](../../schema/vault-structure.json) | Canonical paths, required directories, templates, local skills, statuses, page locations, and required sections |
| Property contract | [wiki-frontmatter.schema.json](../../schema/wiki-frontmatter.schema.json) | Formal frontmatter types, required properties, date formats, status values, and confidence values |
| Enforcement | [validate_vault.py](../../scripts/validate_vault.py) | Checks the live vault against the structural contract |

`AGENTS.md` is authoritative when a semantic rule cannot be represented in JSON. When a stable structural rule changes, update the human and machine contracts together and extend the validator when practical.

### Canonical path map

| Content | Location |
| --- | --- |
| Immutable text evidence | `raw/sources/` |
| Source assets | `raw/assets/` |
| Source summaries | `wiki/sources/` |
| Reusable concepts | `wiki/concepts/` |
| Named entities | `wiki/entities/` |
| Repository/application knowledge | `wiki/projects/` |
| Durable answers | `wiki/questions/` |
| Cross-source synthesis | `wiki/syntheses/` |
| Page templates | `_template/` |
| Machine contracts | `schema/` |
| Project-local skills | `.agents/skills/` |
| Validation scripts | `scripts/` |

### Required page properties

Every wiki page requires `type`, `status`, `created`, `updated`, `tags`, and `sources`. Allowed statuses are `seed`, `active`, `needs-review`, and `superseded`. Dates use `YYYY-MM-DD`.

The page type determines both its directory and required sections. Project pages are deliberately separate from entities and live directly in `wiki/projects/`.

> [!important] Coordinated changes
> A directory, template, page-type, status, or required-section change is incomplete until `AGENTS.md`, `schema/vault-structure.json`, affected templates, navigation, and validation agree.

## Supporting Sources

- [Human-readable schema](../../AGENTS.md)
- [Schema documentation](../../schema/README.md)
- [Structural contract](../../schema/vault-structure.json)
- [Frontmatter JSON Schema](../../schema/wiki-frontmatter.schema.json)

## Related

- [[raw-source-wiki-schema-architecture|Raw Source, Wiki, Schema Architecture]]
- [[vault-workflow-guide|Vault Workflow Guide]]
- [[vault-naming-conventions|Vault Naming Conventions]]
- [[vault-lint-checklist|Vault Lint Checklist]]
- [[project-local-agent-skills|Project-Local Agent Skills]]

## Open Questions

- Should source-link existence and frontmatter array values receive stricter machine validation?
- Which semantic checks are stable enough to move from review guidance into the canonical validator?
