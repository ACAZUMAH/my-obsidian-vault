# Project-Local Agent Skills

This directory follows the Agent Skills convention and makes vault-specific capabilities available from the repository itself. It complements, rather than replaces, profile-local Hermes skills.

The canonical schema-layer catalog and selection guidance lives in [schema/local-skills.md](../../schema/local-skills.md). Skill implementations remain in this directory.

## Vendored Obsidian Skills

The following skills are vendored from [`kepano/obsidian-skills`](https://github.com/kepano/obsidian-skills) at revision `a1dc48e68138490d522c04cbf5822214c6eb1202`:

- `obsidian-markdown`
- `obsidian-bases`
- `json-canvas`
- `obsidian-cli`
- `defuddle`

They were installed through Hermes from the `skills.sh` registry and received a `SAFE` scanner verdict before being copied here. See `LICENSE.obsidian-skills` for the upstream MIT license.

## Local Skills

- `vault-maintenance` connects agents to `AGENTS.md`, `schema/vault-structure.json`, `_template/`, and `scripts/validate_vault.py`.
- `llm-wiki-ingest` integrates authorized evidence into raw files, Source Records, linked knowledge, navigation, and the operation log.
- `llm-wiki-query` retrieves vault-backed answers and routes authorized filing through `vault-maintenance`.
- `llm-wiki-lint` audits structural and semantic health read-only by default and routes authorized repairs through `vault-maintenance`.

## Discovery

Skills-compatible agents should discover `SKILL.md` files recursively below `.agents/skills/`. Already-running agents may cache their startup catalog; restart or begin a new session after changing this directory.

## Updating Vendored Skills

1. Inspect and reinstall the exact upstream skill into the intended Hermes profile.
2. Confirm the scanner verdict and upstream revision.
3. Copy only the skill's `SKILL.md` and linked support files into the matching directory here.
4. Update this revision record and license if upstream changed them.
5. Run `python3 scripts/validate_vault.py`.
6. Review the Git diff before committing because the repository is public.
