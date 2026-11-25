---
type: synthesis
status: active
created: 2026-07-20
updated: 2026-11-25
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
  - ../sources/altin-module-builds-and-scope-corrections.md
  - ../sources/altin-profile-support-ui-corrections.md
  - ../sources/bora-bcl-error-passthrough-and-secret-files.md
  - ../sources/think-like-a-user-direction.md
  - ../sources/livelycura-hrm-feature-by-feature-review.md
  - ../sources/no-project-copies-direction.md
  - ../sources/whole-fix-and-no-dev-test-people-direction.md
  - ../sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md
  - ../sources/agent-context-handoffs-directive.md
  - ../sources/vault-capture-first-auto-publish-directive.md
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
- Keep explanations in plain words. An overcomplicated explanation of a simple change gets rejected. See [[../sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog|the 2026-11-20 Bora corrections]].
- When putting an item to the owner for a decision, explain the issue (how it works today, with an example person), list numbered options with what each covers or leaves out (including ones that won't work, and why), then give "My recommendation" with the reasons. A lone recommendation is not enough. See [[../sources/livelycura-hrm-feature-by-feature-review|the 2026-11-25 HRM follow-ups correction]].
- Once the owner decides or rejects a finding, never raise it again in later reviews or audits. Record decided items and brief reviewers with them as known non-issues. See [[../sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog|the 2026-11-21 Bora decisions]].
- A document for an outside party, such as a partner's API team, covers only what that party asked for. It must not carry decisions for either side, the owner's own to-do lists, or unrelated topics. See [[../sources/bora-deposit-withdrawal-flow-decisions-and-fix-backlog|the 2026-11-20 BCL flow document correction]].

### Change And Remediation Work

- Handle security remediation one issue at a time.
- Explain each fix and verify it before starting the next issue.
- Prefer a paced sequence that avoids confusion and overload over a large batch of simultaneous changes.
- A question about whether work can continue is not authorization to edit. During a paced sequence, wait for an explicit next instruction.
- Change only what was asked for. Treat an unanswered proposal as declined; a broader instruction does not approve it. See [[../sources/altin-module-builds-and-scope-corrections|the Altin scope corrections]].
- When the user says to update or do something, complete its whole reasonable scope. Do not do part of it and then ask whether to do the rest. See [[../sources/altin-module-builds-and-scope-corrections|the Altin scope corrections]].
- When the owner approves a fix, deliver it whole: every app, screen, message and follow-on effect it touches, including what a review of that fix finds. Never come back with "leftovers" to ask about; only separate features or decisions that are truly the owner's (such as exact wording) go back as a question. See [[../sources/whole-fix-and-no-dev-test-people-direction|the 2026-11-19 whole-fix direction]].
- Never create test users, employees or organizations on a shared dev database to check a flow on screen, and don't offer to. Verify with tests that seed their own data and with fake client-side state on a separate origin. See [[../sources/whole-fix-and-no-dev-test-people-direction|the 2026-11-19 whole-fix direction]].
- Do not report UI work done until every new or changed screen has been viewed on the running device; type-checks and code review are not enough. If the device is unavailable, say the UI is unverified. Mirror the reference app's fields and explain any that cannot work instead of dropping them. See [[../sources/altin-profile-support-ui-corrections|the Altin UI corrections]].
- Never read `.env` or other secret-bearing files in any project, even to make a live provider call; the user runs credentialed calls. See [[../sources/bora-bcl-error-passthrough-and-secret-files|the 2026-10-11 secret-file direction]].
- Judge proposed fixes and decisions by how real users would behave, not only by what the system allows. Don't propose guards against things users would realistically never do, and explain options in the app's own words rather than internal terms. See [[../sources/think-like-a-user-direction|the 2026-10-25 think-like-a-user direction]].
- In a feature-by-feature review, report and decide only the current feature's items. A finished feature stays closed, even when the current feature's change caused a new finding there. Items for a later feature are parked silently and raised only when that feature is reached; never list them to the user. An item that only appears on the current feature's screen (a Products permission box on the Roles page) still belongs to its own module. Don't call a message vague, or flag it for rewording, when it already tells the user what happened. See [[../sources/livelycura-hrm-feature-by-feature-review|the 2026-11-01 feature-by-feature correction]].
- Never make a copy of a project folder (a git worktree) to do work, and never start side sessions that do. Work in the existing folder, on the current branch or a branch made there. If uncommitted work or a running dev server stands in the way of a separate branch, say so plainly before acting and offer in-place choices; a "second folder" mentioned inside an option's description is not consent. See [[../sources/no-project-copies-direction|the 2026-11-12 no-project-copies direction]].

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
- The user switches agent accounts often, so in-flight work must be resumable by the next agent. Use the `agent-context` skill: save a snapshot to `raw/agent-contexts/` after verified milestones, decisions, and authorization changes, and when the user says they are switching. Check for an open handoff before starting repository work. Snapshots stay local and never contain secrets. See [[../sources/agent-context-handoffs-directive|the 2026-11-23 agent-context handoffs directive]].
- Capture first, report after: when something belongs in the vault, add it straight away and tell the user what was added, rather than asking first. Push every vault change in the same turn with `python3 scripts/wiki_tool.py publish`, which commits only the named files behind secret-scan and validation gates. Ask first only before deleting, merging, renaming, or moving pages, or changing raw evidence. See [[../sources/vault-capture-first-auto-publish-directive|Vault Capture-First Auto-Publish Directive]].
- When asked to add guidance, documentation, conventions, checklists, or skills “to the vault,” place each artifact in its canonical vault layer and connect it through `index.md`. A tracked file in the wrong ownership layer does not satisfy the request.
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
- [Vault Workflow Guide](../../schema/workflows.md)
- [Project-Local Agent Skills](../../schema/local-skills.md)
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
- [[../sources/altin-module-builds-and-scope-corrections|Altin Module Builds and Scope Corrections]]
- [[../sources/altin-profile-support-ui-corrections|Altin Profile and Support UI Corrections]]
- [[../sources/bora-bcl-error-passthrough-and-secret-files|Bora BCL Error Passthrough And Secret-File Boundary]]
- [[../sources/think-like-a-user-direction|Think Like A User Direction]]
- [[../sources/livelycura-hrm-feature-by-feature-review|LivelyCura HRM Feature-By-Feature Review Scope]]
- [[../sources/no-project-copies-direction|No Project Copies Direction]]
- [[../sources/agent-context-handoffs-directive|Agent Context Handoffs Directive]]
- [[../sources/vault-capture-first-auto-publish-directive|Vault Capture-First Auto-Publish Directive]]

## Open Questions

- Which recurring development, review, deployment, and research workflows should be documented next?
- Which project deserves the first dedicated operating page?
