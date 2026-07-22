---
type: synthesis
status: active
created: 2026-07-20
updated: 2026-07-22
tags: [personal-workflows, preferences, operating-manual, second-brain]
sources:
  - ../sources/hermes-obsidian-second-brain-kickoff.md
  - ../sources/shared-brain-all-agents-directive.md
  - ../sources/hermes-persistent-memory-import.md
  - ../sources/hermes-conversation-harvest-scope-correction.md
  - ../sources/hermes-session-coverage-audit-2026-07-21.md
  - ../sources/kusantec-bora-hermes-conversation-harvest-supplement-1.md
  - ../sources/hermes-generalized-skills-courier-recovery-harvest-batch-1.md
  - ../sources/graphql-product-bora-paystack-hermes-chain.md
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
- Do not agree automatically. When a proposed approach is technically wrong or unsafe, say so plainly, explain why, and recommend the stronger design.

### Change And Remediation Work

- Handle security remediation one issue at a time.
- Explain each fix and verify it before starting the next issue.
- Prefer a paced sequence that avoids confusion and overload over a large batch of simultaneous changes.
- A question about whether work can continue is not authorization to edit. During a paced sequence, wait for an explicit next instruction.

### Project-Specific Constraints

- For `bora-capital-backend` security remediation, leave migrations and cron jobs in their current placement.
- Do not treat those migrations or cron jobs as remediation targets unless the user explicitly changes that instruction.

### Knowledge And Memory

- Use this Obsidian vault as the canonical long-form, linked second brain across every Hermes profile and Codex.
- Keep compact, high-value preferences and a vault pointer in each Hermes profile and in Codex global instructions so every agent can find the detailed context.
- Consult existing notes before asking the user to repeat an established workflow or preference.
- Promote stable, repeatable procedures into Hermes skills when exact operational steps would be useful.
- Preserve exact project skill libraries for project fidelity, and synthesize recurring conventions into generalized backend, frontend-web, and frontend-mobile skills when they represent how the user builds across future projects. Keep source inventories so generalized rules remain auditable.
- Expect multiple agents to operate simultaneously; reread shared notes before editing and preserve concurrent changes.
- When asked to add guidance, documentation, conventions, checklists, or skills “to the vault,” create or update linked, indexed wiki content. Repository files alone do not satisfy that request, even when they are tracked and structurally valid.
- For a Hermes-conversation knowledge harvest, require a directly relevant Hermes conversation before creating a project page or promoting durable claims. Filesystem and Git-root discovery alone are not evidence; repository inspection may verify conversation-derived claims but must not replace them.
- Expect every substantive Hermes conversation to be evaluated for durable project or workflow knowledge and promoted into this vault in the same session when safe. If promotion is deferred, preserve the exact session ID in the harvest checkpoint. Hermes session storage and compact profile memory are not substitutes for Obsidian integration.

## Evidence

- [[../sources/hermes-obsidian-second-brain-kickoff|Hermes–Obsidian Second Brain Kickoff]] records the initial integration request and the first preferences imported from Hermes memory.
- [[../sources/shared-brain-all-agents-directive|Shared Brain Across Hermes Profiles And Codex]] establishes the cross-profile and Codex consistency requirement plus the user's communication preference.
- [[../sources/hermes-persistent-memory-import|Hermes Persistent Memory Import]] preserves previously isolated profile knowledge that has been promoted into the shared vault.
- [[../sources/hermes-conversation-harvest-scope-correction|Hermes Conversation Harvest Scope Correction]] records the direct correction that repository discovery cannot substitute for Hermes conversation evidence.
- [[../sources/hermes-session-coverage-audit-2026-07-21|Hermes Session Coverage Audit — 2026-07-21]] proves that the archive contained 130 unique non-subagent conversations after cross-store ID de-duplication while only one direct Hermes project conversation had been explicitly processed before the audit.
- [[../sources/kusantec-bora-hermes-conversation-harvest-supplement-1|Kusantec/Bora Hermes Conversation Harvest — Supplement 1]] provides direct Hermes provenance for one-issue-at-a-time security remediation, explicit `next` authorization, and the Bora migrations/cron exclusion.
- [[../sources/hermes-generalized-skills-courier-recovery-harvest-batch-1|Hermes Generalized Skills And Courier Recovery Harvest — Batch 1]] records the direct correction requiring a cross-project generalized skill layer in addition to project-specific imports.
- [[../sources/graphql-product-bora-paystack-hermes-chain|GraphQL Product And Bora Paystack Hermes Chain]] records the explicit correction to disagree directly when technical reasoning warrants it rather than reflexively affirming.

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
- [[../concepts/vault-workflow-guide|Vault Workflow Guide]]
- [[../concepts/project-local-agent-skills|Project-Local Agent Skills]]
- [[../entities/hermes-agent|Hermes Agent]]
- [[../entities/codex|Codex]]
- [[../entities/obsidian|Obsidian]]

## Sources

- [[../sources/hermes-obsidian-second-brain-kickoff|Hermes–Obsidian Second Brain Kickoff]]
- [[../sources/shared-brain-all-agents-directive|Shared Brain Across Hermes Profiles And Codex]]
- [[../sources/hermes-persistent-memory-import|Hermes Persistent Memory Import]]
- [[../sources/hermes-conversation-harvest-scope-correction|Hermes Conversation Harvest Scope Correction]]
- [[../sources/hermes-session-coverage-audit-2026-07-21|Hermes Session Coverage Audit — 2026-07-21]]
- [[../sources/kusantec-bora-hermes-conversation-harvest-supplement-1|Kusantec/Bora Hermes Conversation Harvest — Supplement 1]]
- [[../sources/hermes-generalized-skills-courier-recovery-harvest-batch-1|Hermes Generalized Skills And Courier Recovery Harvest — Batch 1]]
- [[../sources/graphql-product-bora-paystack-hermes-chain|GraphQL Product And Bora Paystack Hermes Chain]]

## Open Questions

- Which recurring development, review, deployment, and research workflows should be documented next?
- Which project deserves the first dedicated operating page?
