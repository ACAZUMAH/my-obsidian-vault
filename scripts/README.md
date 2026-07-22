# Vault Scripts

Repository-owned automation lives here. Scripts must be safe to run from the vault root, avoid external dependencies where practical, and never mutate raw evidence unless explicitly designed and invoked for that purpose.

## Canonical Validation

```bash
python3 scripts/validate_vault.py
```

`validate_vault.py` checks:

- Required directories and template files from `schema/vault-structure.json`.
- Obsidian core Templates configuration.
- Project-local Agent Skills and their linked support files.
- Wiki frontmatter keys, types, statuses, and required sections.
- JSON syntax for tracked vault configuration.
- Stale references to the removed `wiki/templates/` path.
- Real Obsidian wikilinks while ignoring fenced and inline code examples.

A zero exit code is the canonical structural validation result. It does not replace content review, secret scanning, or application-specific checks.
