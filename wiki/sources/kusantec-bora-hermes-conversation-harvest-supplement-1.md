---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [kusantec, bora-capital, hermes, security, authorization, project-knowledge]
sources:
  - ../../raw/sources/2026-07-21-kusantec-bora-hermes-conversation-harvest-supplement-1.md
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
---

# Kusantec/Bora Hermes Conversation Harvest — Supplement 1

## Source

- Raw file: [2026-07-21-kusantec-bora-hermes-conversation-harvest-supplement-1.md](../../raw/sources/2026-07-21-kusantec-bora-hermes-conversation-harvest-supplement-1.md)
- Date: 2026-07-21
- Author: Hermes read-only evidence audit
- Ingested: 2026-07-21

## Core Claims

- Seven exact Hermes sessions were classified: six substantive and one interrupted precursor.
- Bora security remediation is risk-ranked, evidence-backed, one issue at a time, and review-gated. Migrations and cron placement remain outside remediation scope unless explicitly reopened.
- Financial writes and provider-backed reads bind to the authenticated principal and verify owned investment accounts or wallets before external BCL calls.
- Wallet lookup uses owner-scoped queries and a non-enumerating not-found result. Wallet list/create compatibility inputs are overwritten with canonical principal identity after caller data so user-controlled IDs cannot win.
- Auto-top-up reads and transitions are owner-scoped. Incoming IDs first resolve current documents; downstream calls use the fetched documents’ canonical identity.
- A question about continuing is not authorization to edit. Wait for the user’s explicit `next` during paced remediation.
- Rollbar was replaced by Sentry with disabled-by-default sending when DSN is absent, no default PII, and event redaction.
- DigitalOcean-compatible wallet credential encryption uses exactly `WALLET_CREDENTIAL_ENCRYPTION_KEY` and `WALLET_CREDENTIAL_ACTIVE_KEY_VERSION`; a JSON key-ring abstraction was explicitly rejected.

## Useful Details

- Interrupted precursor: `20260713_173225_73e447`.
- Substantive sessions: `20260713_191745_a48077`, `20260713_194431_64df24`, `20260713_205301_72152d`, `20260713_213541_c58421`, `20260714_133535_83849e`, and `20260720_193333_054b33`.
- The initial audit’s broad “high risk” conclusion is historical; later sessions and current source repaired many authorization findings.
- Historical verification progressed from 17 suites/102 tests through focused transaction, statement, wallet, and auto-top-up authorization work. The July 20 session reported 60 suites and more than 300 tests around Sentry/encryption changes. These results were not rerun.
- Current transaction, wallet, and auto-top-up source supports the reviewed authorization outcomes.
- Sentry and wallet-encryption changes exist only in the current dirty working tree; the historical plan is present in `HEAD` history but deleted locally.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[kusantec-bora-project-knowledge-harvest-batch-1|Kusantec/Bora Project Knowledge Harvest — Batch 1]]
- [[../syntheses/personal-operating-manual|Personal Operating Manual]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- The broad July 13 security plan is a historical snapshot, not a current risk assessment.
- The current auto-top-up helper still supports an internal ownerless `findById` path when no user ID is supplied. Public GraphQL paths are scoped, but the helper is not universally fail-closed.
- Sentry and encryption changes are uncommitted, so current working-tree presence is not reproducible release provenance.
- The simplified single-key encryption design requires coordinated re-encryption for rotation; it is not online multi-key rotation.
- Current repository state was inspected statically only. No build, test, migration, external provider, deployment, or live security validation was run.

## Open Questions

- Should the internal ownerless auto-top-up lookup be removed or explicitly constrained to trusted callers?
- When will the Sentry and wallet-encryption changes be committed and revalidated from a clean tree?
- What coordinated procedure will rotate the single wallet encryption key and re-encrypt existing credentials?
