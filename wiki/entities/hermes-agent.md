---
type: entity
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [hermes, agent, tooling, memory]
sources:
  - ../sources/hermes-obsidian-second-brain-kickoff.md
  - ../sources/shared-brain-all-agents-directive.md
  - ../sources/hermes-persistent-memory-import.md
aliases: [Hermes]
---

# Hermes Agent

## Summary

Hermes Agent is the model-facing operator for this second brain. It can read, search, create, and update the Obsidian vault while retaining a compact persistent memory across conversations.

## Known Facts

- The `default`, `coder`, `devops`, `personal`, and `researcher` profiles resolve this vault through `OBSIDIAN_VAULT_PATH`.
- Hermes built-in memory is bounded and best suited to compact, high-value facts and pointers.
- The Obsidian vault is the long-form source of truth for linked personal workflows and durable operating knowledge.
- Each profile retains a compact role-specific layer while shared knowledge is promoted to the vault.
- Codex uses the same vault through global instructions, creating one knowledge plane across tools.
- Hermes session search remains useful for reconstructing prior conversations, but conversation history alone is not the durable knowledge base.
- Reusable exact procedures can be stored as Hermes skills when they become stable enough.

## Related

- [[obsidian|Obsidian]]
- [[codex|Codex]]
- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Obsidian Memory Architecture]]
- [[../concepts/persistent-compounding-wiki|Persistent Compounding Wiki]]
- [[../syntheses/personal-operating-manual|Personal Operating Manual]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Supporting Sources

- [[../sources/hermes-obsidian-second-brain-kickoff|Hermes–Obsidian Second Brain Kickoff]]
- [[../sources/shared-brain-all-agents-directive|Shared Brain Across Hermes Profiles And Codex]]
- [[../sources/hermes-persistent-memory-import|Hermes Persistent Memory Import]]

## Open Questions

- Which workflows recur often enough to become dedicated Hermes skills?
- Should additional Hermes profiles be connected to this same vault or maintain role-specific vaults?
