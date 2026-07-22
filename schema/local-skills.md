# Project-Local Agent Skills

Project-local Agent Skills are repository-tracked procedures under `.agents/skills/` that make vault-specific formats and maintenance behavior portable across compatible agents. This page documents them; the skill implementations remain in `.agents/skills/`.

## Available Skills

| Skill | Use |
| --- | --- |
| [`obsidian-markdown`](../.agents/skills/obsidian-markdown/SKILL.md) | Obsidian Markdown, wikilinks, properties, embeds, and callouts |
| [`obsidian-bases`](../.agents/skills/obsidian-bases/SKILL.md) | Obsidian Bases files, views, filters, formulas, and summaries |
| [`json-canvas`](../.agents/skills/json-canvas/SKILL.md) | JSON Canvas nodes, groups, edges, and connections |
| [`obsidian-cli`](../.agents/skills/obsidian-cli/SKILL.md) | Operations against a running Obsidian vault and plugin/theme development |
| [`defuddle`](../.agents/skills/defuddle/SKILL.md) | Clean Markdown extraction from web pages before ingest |
| [`vault-maintenance`](../.agents/skills/vault-maintenance/SKILL.md) | Vault schema, templates, concurrency, validation, navigation, and Git-review workflow |
| [`llm-wiki-ingest`](../.agents/skills/llm-wiki-ingest/SKILL.md) | Source ingestion, conversation harvests, Source Records, promotion, and provenance closure |
| [`llm-wiki-query`](../.agents/skills/llm-wiki-query/SKILL.md) | Retrieval-first vault answers and authorized durable filing |
| [`llm-wiki-lint`](../.agents/skills/llm-wiki-lint/SKILL.md) | Read-only structural and semantic audits plus explicitly authorized repair routing |

The first five skills are vendored from `kepano/obsidian-skills` at the revision recorded in the [local skills catalog](../.agents/skills/README.md). The four repository-owned skills separate operation intent from shared mutation mechanics: `llm-wiki-ingest`, `llm-wiki-query`, and `llm-wiki-lint` route the task, while `vault-maintenance` owns structural maintenance and completion checks.

## Selection Rules

- Use the smallest skill set that covers the task.
- Always read the selected `SKILL.md` before acting and follow linked references required by the task.
- Repository instructions and explicit user direction outrank generic skill examples.
- Use `llm-wiki-ingest` for new evidence or durable evidence promotion.
- Use `llm-wiki-query` for retrieval and vault-backed answers; add `vault-maintenance` only when filing is authorized.
- Use `llm-wiki-lint` for audit and health checks; add `vault-maintenance` only when repairs are explicitly requested.
- Use `vault-maintenance` for durable edits, moves, validation, templates, index/log updates, or shared-page maintenance.
- Use format skills only when their file type or Obsidian-specific syntax is in scope.

## Portability And Updates

- Keep skills as real tracked files, not symlinks to profile-local directories.
- Preserve upstream license and revision provenance for vendored skills.
- Copy only the selected skill and its required support files.
- Validate skill name/frontmatter and support-file links with the canonical vault validator.
- Review upstream changes before updating; do not silently replace local workflow rules.

Already-running agents may cache their skill catalog. Restart or start a new session after adding or renaming a project-local skill.

## References

- [Schema reference](README.md)
- [Workflow guide](workflows.md)
- [Local skills catalog](../.agents/skills/README.md)
- [Required skill contract](vault-structure.json)
