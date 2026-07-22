---
name: llm-wiki-lint
description: Audit the canonical Obsidian vault for structural, provenance, semantic, navigation, and knowledge-health defects. Use when asked to lint, audit, validate, health-check, find broken links or orphans, detect duplication or stale claims, or prioritize vault repairs.
---

# LLM Wiki Lint

## Authority

1. Read the live [vault authority](../../../AGENTS.md), [lint checklist](../../../schema/lint-checklist.md), and [workflow guide](../../../schema/workflows.md).
2. Treat [the canonical validator](../../../scripts/validate_vault.py) as the structural suite, not as proof of semantic correctness.
3. Follow [vault-maintenance](../vault-maintenance/SKILL.md) only when the user explicitly requests repairs.

## Audit Workflow

1. Run `python3 scripts/wiki_tool.py check`; preserve the validator's exact pass/fail result and treat the audit output as an advisory baseline rather than an exhaustive semantic review.
2. Inspect semantic health separately: unsupported or stale claims, contradictions, duplicate ownership, orphan pages, weak provenance, missing concepts, uncovered raw evidence, excessive Source Record duplication, and research gaps.
3. Inspect security and hygiene boundaries without claiming that pattern scans prove secrets are absent.
4. Report prioritized findings with exact file or page evidence, impact, and a bounded remediation. Distinguish confirmed defects from recommendations and open questions.
5. Keep the audit read-only unless the request explicitly includes implementation.

## Repair Workflow

When repairs are authorized:

1. Apply the smallest coherent fix and preserve raw evidence and concurrent work.
2. Update affected navigation, schema contracts, and linked pages only where required.
3. Append exactly one appropriate `log.md` entry for the repair operation.
4. Rerun the canonical validator, relevant focused checks, secret hygiene, and exact diff review.

## Completion Criteria

- Report structural validation separately from semantic review.
- Support every finding with reproducible evidence.
- Leave the vault unchanged for audit-only requests.
- Verify and accurately report every authorized repair.
