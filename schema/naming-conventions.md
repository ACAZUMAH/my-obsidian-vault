# Vault Naming Conventions

These conventions keep filenames stable, page titles readable, links predictable, and content ownership visible from its path.

## Wiki Page Filenames

Use lowercase kebab-case and place each file under the directory owned by its page type.

| Page type | Pattern | Example |
| --- | --- | --- |
| Source Record | `wiki/sources/source-title.md` | `wiki/sources/llm-wiki-idea.md` |
| Concept | `wiki/concepts/concept-name.md` | `wiki/concepts/persistent-compounding-wiki.md` |
| Entity | `wiki/entities/entity-name.md` | `wiki/entities/obsidian.md` |
| Project | `wiki/projects/project-name.md` | `wiki/projects/compflow-backend.md` |
| Question | `wiki/questions/question-slug.md` | `wiki/questions/first-ingest-example.md` |
| Synthesis | `wiki/syntheses/synthesis-title.md` | `wiki/syntheses/software-development-operating-manual.md` |

The filename is the stable ID. The first H1 is the human-readable title and may use capitalization, punctuation, or a fuller product name.

## Link Naming

- Use Obsidian wikilinks for vault notes: `[[path/to/page|Readable Label]]`.
- Prefer explicit paths when duplicate stems or cross-directory ownership could be ambiguous.
- Use relative Markdown links for raw evidence and repository files.
- Link project knowledge to `wiki/projects/`, never to a parallel `entities/projects` tree.

## Templates, Skills, Contracts, And Schema Documents

- Templates live in `_template/` and use `*-template.md` filenames.
- A local skill lives at `.agents/skills/<skill-name>/SKILL.md`; its frontmatter `name` must equal the directory name.
- Supporting skill material lives below that skill, normally under `references/`.
- Machine contracts and canonical schema guidance use descriptive lowercase filenames under `schema/`.

## Evidence Naming

Keep imported filenames when provenance depends on them. For agent-created harvest manifests, prefer a date-prefixed descriptive name such as `YYYY-MM-DD-project-purpose-batch-N.md`. Never put credentials, private identifiers, or secret values in filenames.

Source Records use the most stable descriptive identity for the evidence set they cover. One record may aggregate multiple raw files, and one raw file may support multiple records, when the relationships are explicit and the records serve distinct retrieval purposes.

## Rename Discipline

Renaming a stable page ID requires updating inbound links, `index.md`, schema/template references when applicable, and the operation log. Do not create an alias page merely to avoid fixing links.

## References

- [Vault operating authority](../AGENTS.md)
- [Structural contract](vault-structure.json)
- [Schema reference](README.md)
