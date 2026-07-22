# Vault Schema Reference

This directory owns the canonical operational documentation and machine-readable contracts for the Obsidian knowledge vault. Wiki pages may explain the architecture, but they do not duplicate schema ownership.

## Authority And Enforcement

| Layer | File | Responsibility |
| --- | --- | --- |
| Human authority | [AGENTS.md](../AGENTS.md) | Meaning, workflow, naming, citation, concurrency, index, and log rules |
| Operational references | This directory | Schema, workflows, naming, lint, and local-skill guidance |
| Structural contract | [vault-structure.json](vault-structure.json) | Canonical paths, required directories, Source Record coverage policy, schema documents, templates, skills, statuses, page locations, and sections |
| Property contract | [wiki-frontmatter.schema.json](wiki-frontmatter.schema.json) | Frontmatter types, required properties, dates, statuses, and confidence values |
| Enforcement | [validate_vault.py](../scripts/validate_vault.py) | Checks the live vault against the structural contract |

`AGENTS.md` is authoritative when a semantic rule cannot be represented in JSON. Stable structural changes must update the human and machine contracts together.

## Operational Documents

- [Workflow guidance](workflows.md)
- [Naming conventions](naming-conventions.md)
- [Lint checklist](lint-checklist.md)
- [Project-local skills](local-skills.md)

## Canonical Path Map

| Content | Location |
| --- | --- |
| Immutable text evidence | `raw/sources/` |
| Source assets | `raw/assets/` |
| Curated Source Records | `wiki/sources/` |
| Reusable concepts | `wiki/concepts/` |
| Named entities | `wiki/entities/` |
| Repository/application knowledge | `wiki/projects/` |
| Durable answers | `wiki/questions/` |
| Cross-source synthesis | `wiki/syntheses/` |
| Page templates | `_template/` |
| Schema documentation and contracts | `schema/` |
| Project-local skill implementations | `.agents/skills/` |
| Validation scripts | `scripts/` |

## Wiki Page Contract

Every wiki page requires `type`, `status`, `created`, `updated`, `tags`, and `sources`. Allowed statuses are `seed`, `active`, `needs-review`, and `superseded`. Dates use `YYYY-MM-DD`.

The page type determines its directory and required sections. Project pages live directly in `wiki/projects/`; they are not entities.

## Coordinated Changes

A Source Record policy, schema-document, directory, template, page-type, status, skill, or required-section change is incomplete until `AGENTS.md`, `schema/vault-structure.json`, affected templates or documentation, `index.md`, and validation agree.

## Validation

Run from the vault root:

```bash
python3 scripts/validate_vault.py
```

The validator uses only the Python standard library. It checks the live structure, index connections for registered schema documents, templates, and Source Records, complete raw-evidence coverage, Source Record raw-link existence and aggregation policy, Obsidian template configuration, project-local Agent Skills, wiki frontmatter/sections, JSON files, stale template paths, and real wikilinks.
