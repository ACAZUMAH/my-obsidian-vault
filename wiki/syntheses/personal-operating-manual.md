---
type: synthesis
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [personal-workflows, preferences, operating-manual, second-brain]
sources:
  - ../sources/hermes-obsidian-second-brain-kickoff.md
  - ../sources/shared-brain-all-agents-directive.md
  - ../sources/hermes-persistent-memory-import.md
confidence: high
---

# Personal Operating Manual

## Thesis

This page is the central map of durable knowledge about how the user prefers to work. It should remain concise and link outward to detailed workflows, projects, and decision records rather than becoming an unstructured diary.

## Current Working Preferences

### Communication And Learning

- Be straight to the point and technically sophisticated.
- Explain architecture, relationships, and rationale so the user can see how the pieces fit together and learn along the way.
- Avoid generic tutorial padding; connect explanation directly to the current decision or implementation.

### Change And Remediation Work

- Handle security remediation one issue at a time.
- Explain each fix and verify it before starting the next issue.
- Prefer a paced sequence that avoids confusion and overload over a large batch of simultaneous changes.

### Project-Specific Constraints

- For `bora-capital-backend` security remediation, leave migrations and cron jobs in their current placement.
- Do not treat those migrations or cron jobs as remediation targets unless the user explicitly changes that instruction.

### Knowledge And Memory

- Use this Obsidian vault as the canonical long-form, linked second brain across every Hermes profile and Codex.
- Keep compact, high-value preferences and a vault pointer in each Hermes profile and in Codex global instructions so every agent can find the detailed context.
- Consult existing notes before asking the user to repeat an established workflow or preference.
- Promote stable, repeatable procedures into Hermes skills when exact operational steps would be useful.
- Expect multiple agents to operate simultaneously; reread shared notes before editing and preserve concurrent changes.

## Evidence

- [[../sources/hermes-obsidian-second-brain-kickoff|Hermes–Obsidian Second Brain Kickoff]] records the initial integration request and the first preferences imported from Hermes memory.
- [[../sources/shared-brain-all-agents-directive|Shared Brain Across Hermes Profiles And Codex]] establishes the cross-profile and Codex consistency requirement plus the user's communication preference.
- [[../sources/hermes-persistent-memory-import|Hermes Persistent Memory Import]] preserves previously isolated profile knowledge that has been promoted into the shared vault.

## Implications

- Corrections and recurring preferences should update this manual or a linked domain page.
- Project-specific details should move to focused pages as they accumulate.
- New notes should preserve provenance and distinguish durable rules from temporary task state.
- All agent-specific startup contexts should point here rather than maintain divergent long-form copies.

## Contradictions Or Tensions

- Automatic capture is valuable only when selective. Capturing everything would bury important operating knowledge in noise.
- Some information may be durable but too sensitive for the vault. Secrets and credentials remain excluded unless the user explicitly requests secure handling outside ordinary notes.
- Simultaneous agent access improves continuity but requires focused edits and live rereads to avoid overwriting concurrent changes.

## Related

- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]
- [[llm-wiki-operating-model|LLM Wiki Operating Model]]
- [[software-development-operating-manual|Software Development Operating Manual]]
- [[../entities/hermes-agent|Hermes Agent]]
- [[../entities/codex|Codex]]
- [[../entities/obsidian|Obsidian]]

## Sources

- [[../sources/hermes-obsidian-second-brain-kickoff|Hermes–Obsidian Second Brain Kickoff]]
- [[../sources/shared-brain-all-agents-directive|Shared Brain Across Hermes Profiles And Codex]]
- [[../sources/hermes-persistent-memory-import|Hermes Persistent Memory Import]]

## Open Questions

- Which recurring development, review, deployment, and research workflows should be documented next?
- Which project deserves the first dedicated operating page?
