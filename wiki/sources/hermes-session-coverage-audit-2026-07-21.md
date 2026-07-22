---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, session-history, project-knowledge, coverage-audit, correction]
sources:
  - ../../raw/sources/2026-07-21-hermes-session-coverage-audit.md
  - standalone-scope-correction-ownership-chain.md
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
---

# Hermes Session Coverage Audit — 2026-07-21

## Source

- Raw file: [2026-07-21-hermes-session-coverage-audit.md](../../raw/sources/2026-07-21-hermes-session-coverage-audit.md)
- Date: 2026-07-21
- Author: Hermes state-store audit prompted by a direct user correction
- Ingested: 2026-07-21

## Core Claims

- The vault was not a complete harvest of Hermes conversations.
- The audited coder and default Hermes state stores contained 225 store records at snapshot time: 132 non-subagent records with user messages, 90 `source='subagent'` records with user messages, and three empty coder-profile alias records.
- Five IDs occur in both stores. After ID de-duplication, the snapshot contains 220 unique IDs: a frozen ledger of 130 non-subagent exact IDs and 90 subagent exact IDs. Three empty coder aliases resolve to populated default conversations, but [[standalone-scope-correction-ownership-chain|later collision analysis]] proves that at least one shared ID (`20260721_164555_84be3a`) has two materially different populated bodies and must not be described as one physical conversation.
- Only one direct Hermes project session had been explicitly documented as processed before this audit: CompFlow session `20260710_173537_54b264`.
- Codex-derived project batches, repository inspection, Hermes persistent memory, and stored Hermes sessions are different evidence sources. None automatically substitutes for ingesting the Hermes archive into Obsidian.
- The immediate frozen-ledger backlog was 129 non-subagent exact IDs without documented direct-Hermes classification, while the 90 subagent exact IDs require duplicate-versus-independent-evidence triage rather than blind promotion.

## Useful Details

- The coder profile contained the overwhelming majority of stored Hermes history; the default profile also contained project conversations, including the already processed CompFlow session and additional Bora sessions.
- Explicit project working directories identified 16 primary sessions, but missing cwd metadata is common and cannot be used to classify the remaining sessions as unrelated.
- Hermes `source='subagent'` is the reliable subagent classification boundary for this snapshot. `parent_session_id` also links ordinary CLI, TUI, and Desktop continuations, so treating every linked record as an agent child would incorrectly discard user-facing conversation continuations.
- Coverage counts currently use exact session IDs. Store-qualified physical rows remain necessary for collision auditing; exact-ID totals must not be presented as physically faithful conversation totals when populated bodies differ across stores.
- Session titles are discovery metadata only. Durable promotion requires reading user corrections, relevant outcomes, and historical verification, followed by current-code reconciliation when present behavior matters.
- Hermes persistent memory is bounded and selective. It can point agents to the vault but is not a transcript-ingest or project-knowledge-harvest mechanism.
- Sharing the same model or operating instructions across Codex and Hermes does not merge their separate archives.

## Connections

- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]
- [[../syntheses/personal-operating-manual|Personal Operating Manual]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../concepts/hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]
- [[hermes-conversation-harvest-scope-correction|Hermes Conversation Harvest Scope Correction]]
- [[standalone-scope-correction-ownership-chain|Standalone Scope Correction Ownership Chain]]

## Contradictions Or Tensions

- Earlier vault language described some project-family histories as complete even though those classifications were mainly Codex records. Those statements remain valid only for their named Codex/discovered-record sets, not for Hermes archive coverage.
- Capturing all durable knowledge does not mean copying every transcript. Ordinary chat, tool chatter, secrets, temporary task status, and duplicate subagent context remain excluded.
- The inventory proves archive presence and the size of the backlog; it does not itself promote architecture or implementation claims from unreviewed sessions.
- The immutable raw manifest preserves the original per-store record counts. This integrated page corrects their interpretation by de-duplicating IDs across stores; it does not rewrite the raw evidence.
- Exact-ID de-duplication undercounts materially different populated same-ID bodies. The 130 denominator remains frozen for continuity until a centralized store-qualified recount is designed; it is an exact-ID ledger, not a guaranteed physical-conversation count.

## Open Questions

- Which no-cwd primary sessions contain project evidence that title-based discovery would miss?
- Which subagent records contain independent corrections or verification rather than duplicate parent-task context?
- What automated end-of-session or scheduled mechanism should enforce future Hermes-to-vault ingestion without producing noise or concurrent-write conflicts?
- Should future coverage use `(store/profile, session_id)` composites, and what is the recalculated denominator after semantic duplicate detection?
