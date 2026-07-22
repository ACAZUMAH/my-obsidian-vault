# Vault Lint Checklist

Vault linting combines canonical structural validation with semantic, provenance, security, navigation, and Git review before a durable change is complete.

## Canonical Command

```bash
python3 scripts/validate_vault.py
```

A zero exit code proves the configured structural checks passed. It does not prove that claims are correct, secrets are absent, or the change is semantically complete.

## Structural Checklist

- [ ] Required directories, schema documents, and configured templates exist and are linked from `index.md`.
- [ ] Obsidian core Templates points to `_template/`.
- [ ] Frontmatter contains required keys, valid page type/status, and `YYYY-MM-DD` dates.
- [ ] Each wiki page lives in the directory assigned to its type.
- [ ] Required sections are present.
- [ ] Every Source Record references existing raw evidence and is linked from `index.md`.
- [ ] Every non-hidden file under `raw/sources/` is covered by at least one Source Record.
- [ ] Project-local skills have valid `SKILL.md` frontmatter and resolvable support links.
- [ ] JSON configuration parses.
- [ ] Real wikilinks resolve.
- [ ] No active reference uses the retired `wiki/templates/` path.

## Semantic And Provenance Checklist

- [ ] Claims are supported by a source, current repository evidence, or an explicitly labeled inference.
- [ ] Historical outcomes are not presented as fresh verification.
- [ ] Contradictions and superseded behavior remain visible.
- [ ] No duplicate page or competing ownership path was introduced.
- [ ] Source Records are concise provenance/retrieval nodes and connect to affected project, concept, and synthesis pages without copying exhaustive raw evidence.
- [ ] `index.md` describes every new durable page.
- [ ] Exactly one appropriate `log.md` entry records the operation.

## Security And Hygiene Checklist

- [ ] No credentials, tokens, private keys, connection strings, private identifiers, or secret-bearing configuration were copied.
- [ ] Generated files, dependencies, caches, binaries, and unrelated tool chatter were excluded.
- [ ] Raw evidence was not rewritten without explicit authorization.
- [ ] Markdown and JSON contain no malformed or accidental placeholder syntax.

## Git Checklist

- [ ] `git status --short` contains only understood changes.
- [ ] `git diff --check` passes.
- [ ] The exact diff was reviewed after concurrent-writer rereads.
- [ ] Only intended paths are staged.
- [ ] The commit message states the durable outcome.
- [ ] Push is performed only when requested.

Report the canonical validator result separately from semantic review, secret scanning, and Git checks. Do not compress them into an unsupported “everything passed” claim.

## References

- [Vault operating authority](../AGENTS.md)
- [Validator documentation](../scripts/README.md)
- [Canonical validator](../scripts/validate_vault.py)
- [Vault-maintenance verification checklist](../.agents/skills/vault-maintenance/SKILL.md)
