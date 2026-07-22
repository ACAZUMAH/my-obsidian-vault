---
type: concept
status: active
created: 2026-07-22
updated: 2026-07-22
tags: [vault, agent-skills, obsidian, tooling]
sources: []
---

# Project-Local Agent Skills

## Working Definition

Project-local Agent Skills are repository-tracked procedures under `.agents/skills/` that make vault-specific formats and maintenance behavior portable across compatible agents.

## Current Synthesis

### Available skills

| Skill | Use |
| --- | --- |
| `obsidian-markdown` | Obsidian Markdown, wikilinks, properties, embeds, and callouts |
| `obsidian-bases` | Obsidian Bases files, views, filters, formulas, and summaries |
| `json-canvas` | JSON Canvas nodes, groups, edges, and connections |
| `obsidian-cli` | Operations against a running Obsidian vault and plugin/theme development |
| `defuddle` | Clean Markdown extraction from web pages before ingest |
| `vault-maintenance` | This vault’s schema, templates, concurrency, validation, navigation, and Git-review workflow |

The first five skills are vendored from `kepano/obsidian-skills` at the revision recorded in [.agents/skills/README.md](../../.agents/skills/README.md). `vault-maintenance` is the repository-owned integration layer that connects those format/tool skills to this vault’s contracts.

### Selection rules

- Use the smallest skill set that covers the task.
- Always read the selected `SKILL.md` before acting and follow linked references required by the task.
- Repository instructions and explicit user direction outrank generic skill examples.
- Use `vault-maintenance` for durable edits, moves, validation, templates, index/log updates, or shared-page maintenance.
- Use format skills only when their file type or Obsidian-specific syntax is in scope.

### Portability and updates

- Keep skills as real tracked files, not symlinks to profile-local directories.
- Preserve upstream license and revision provenance for vendored skills.
- Copy only the selected skill and its required support files.
- Validate skill name/frontmatter and support-file links with the canonical vault validator.
- Review upstream changes before updating; do not silently replace local workflow rules.

> [!warning] Discovery cache
> Already-running agents may cache their skill catalog. Restart or start a new session after adding or renaming a project-local skill.

## Supporting Sources

- [Project-local skills catalog](../../.agents/skills/README.md)
- [Vault-maintenance skill](../../.agents/skills/vault-maintenance/SKILL.md)
- [Required skill contract](../../schema/vault-structure.json)

## Related

- [[vault-schema-reference|Vault Schema Reference]]
- [[vault-workflow-guide|Vault Workflow Guide]]
- [[vault-naming-conventions|Vault Naming Conventions]]
- [[vault-lint-checklist|Vault Lint Checklist]]
- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]

## Open Questions

- Which repeated vault operations deserve their own repository-local skill instead of another documentation page?
- Should vendored skill updates be automated only after a human-reviewed diff and validator pass?
