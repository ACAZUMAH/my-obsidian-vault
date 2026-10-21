# Claude Code Shared Brain Integration

Captured: 2026-09-29
Origin: User directive in a Claude Code desktop session started from the `bora-capital-backend` repository.

## User Directive

> before we start with what I want us to do, I want you install the obsidian skills and make sure you connected to my obsidian vault how I do things are stored there

## Integration Performed

- Claude Code had no global instruction file and no vault pointer before this session; only Hermes profiles and Codex were connected.
- `~/.claude/CLAUDE.md` was created as the Claude Code global instruction layer. It mirrors the Codex global pointer (vault path, index, `AGENTS.md`, personal and software-development manuals, shared architecture page), communication preferences, capture and exclusion rules, concurrent-agent rules, and instruction precedence.
- `~/.claude/settings.json` now exposes `OBSIDIAN_VAULT_PATH=/Users/acazumah/Documents/Work Space` to Claude Code environments, matching the Codex `config.toml` setting.
- The nine project-local vault skills (`obsidian-markdown`, `obsidian-bases`, `json-canvas`, `obsidian-cli`, `defuddle`, `vault-maintenance`, `llm-wiki-ingest`, `llm-wiki-query`, `llm-wiki-lint`) were exposed to Claude Code as symlinks from `~/.claude/skills/<name>` to `<vault>/.agents/skills/<name>`. No upstream download was performed; the vendored `kepano/obsidian-skills` revision already recorded in the vault was reused.
- The symlinks point from the machine-local Claude Code profile into the vault, not from the vault outward, so the vault itself remains portable.

## Verified Behavior

- Claude Code loaded all nine skills in the same session after the symlinks were created.
- Obsidian CLI 1.13.7 answered searches against the vault while the Obsidian app was running.
- Run from a directory outside the vault, `obsidian help` returned `Vault not found.`; passing `vault="Work Space"` as the first parameter resolved the vault from any directory.
