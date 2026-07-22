---
name: vault-maintenance
description: Use when creating, moving, validating, or maintaining content and infrastructure in this canonical Obsidian vault. Enforces the vault schema, template paths, concurrent-writer rules, and post-change validation.
version: 1.1.0
author: ACAZUMAH
license: MIT
metadata:
  hermes:
    tags: [obsidian, knowledge-management, validation, templates, concurrent-editing]
    related_skills: [obsidian-markdown, obsidian-bases, json-canvas, obsidian-cli, defuddle]
---

# Vault Maintenance

## Overview

Use the repository's own contracts rather than inventing a parallel structure. `AGENTS.md` is the human-readable operating authority; `schema/vault-structure.json` is the machine-readable path and page contract.

## Workflow

1. Read `AGENTS.md`, `index.md`, and the relevant synthesis or project pages before editing. Completion criterion: the applicable schema and current knowledge are known.
2. Search before creating pages. Completion criterion: no duplicate page or conflicting path already exists.
3. Use `_template/` for source, concept, entity, question, and synthesis page scaffolds. Completion criterion: the created page has required frontmatter and sections.
4. Reread every shared page immediately before patching because Hermes, Codex, Obsidian, and other agents may write concurrently. Completion criterion: focused edits preserve unrelated live changes.
5. Keep raw evidence immutable unless the user explicitly requests a raw-source change. Completion criterion: `raw/` changes are intentional and attributable.
6. Update `index.md` and append exactly one `log.md` entry for durable wiki or structural maintenance. Completion criterion: navigation and history describe the resulting state.
7. Run `python3 scripts/wiki_tool.py check`. Completion criterion: canonical validation exits zero and advisory audit findings remain separate from structural status.
8. Review `git status` and the exact diff. Completion criterion: no unrelated concurrent work is staged, discarded, or claimed as part of the change.

## Path Contract

- Evidence: `raw/sources/`, `raw/assets/`
- Durable knowledge: curated Source Records in `wiki/sources/`, plus `wiki/concepts/`, `wiki/entities/`, `wiki/questions/`, and `wiki/syntheses/`
- Templates: `_template/`
- Machine-readable contracts: `schema/`
- Project-local skills: `.agents/skills/`
- Automation and validation: `scripts/`
- Navigation and history: `index.md`, `log.md`

## Pitfalls

- Do not recreate `wiki/templates/`; Obsidian's core Templates plugin is configured for `_template/`.
- Do not use symlinks to profile-local skill folders; they are machine-specific and break repository portability.
- Do not rewrite `index.md`, `log.md`, manuals, or checkpoints wholesale while another agent may be active.
- Do not call an ad-hoc probe the canonical suite. `scripts/validate_vault.py` is the repository's canonical structural validator.
- Do not stage all dirty files in this public repository without reviewing concurrent harvest work and secret hygiene.

## Verification Checklist

- [ ] Required directories in `schema/vault-structure.json` exist.
- [ ] Obsidian core Templates points to `_template`.
- [ ] No references to `wiki/templates` remain outside historical log records.
- [ ] Every project-local skill has valid `SKILL.md` frontmatter and resolvable support-file links.
- [ ] Wiki pages contain required frontmatter and sections.
- [ ] Every raw source is covered by an indexed Source Record, and every Source Record resolves to raw evidence.
- [ ] Real wikilinks resolve.
- [ ] `python3 scripts/wiki_tool.py check` preserves a passing canonical result and separate advisory findings.
- [ ] Git diff contains only intended work.
