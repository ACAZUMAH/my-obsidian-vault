# Vault Schemas

This directory contains machine-readable contracts for the canonical Obsidian knowledge vault.

## Files

- `vault-structure.json` — canonical paths, required directories, templates, project-local skills, statuses, frontmatter keys, and required sections.
- `wiki-frontmatter.schema.json` — JSON Schema representation of the YAML frontmatter contract for wiki pages and templates.

`AGENTS.md` remains the human-readable operating authority. These files encode the stable structural subset used by automation; they must be updated in the same change whenever directory conventions or required page sections change.

## Validation

Run from the vault root:

```bash
python3 scripts/validate_vault.py
```

The validator uses only the Python standard library. It checks the live structure, Obsidian template configuration, project-local Agent Skills, wiki frontmatter/sections, JSON files, stale template paths, and real wikilinks.
