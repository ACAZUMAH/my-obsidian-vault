---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [kusantec, bora-capital, project-knowledge, codex, repository-inventory]
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
sources:
  - ../../raw/sources/2026-07-21-kusantec-bora-project-knowledge-harvest-batch-1.md
  - hermes-conversation-harvest-scope-correction.md
---

# Kusantec/Bora Project Knowledge Harvest — Batch 1

## Source

- Raw file: [2026-07-21-kusantec-bora-project-knowledge-harvest-batch-1.md](../../raw/sources/2026-07-21-kusantec-bora-project-knowledge-harvest-batch-1.md)
- Date: 2026-07-21
- Author: Codex, from user-directed repository inventory and sanitized historical-session reconciliation
- Ingested: 2026-07-21

## Core Claims

- Bora Capital is implemented as an independently versioned backend and Expo mobile application; Let's Ride Backend under the same parent folder is a separate product.
- Six directly matched Bora backend sessions establish Fidelity onboarding responsibilities, push/email behavior, Oye restrictions, KYC test maintenance, Paystack deposit architecture, and strict repository ownership conventions.
- Paystack is the current implemented deposit path: each portfolio requires a subaccount, the backend verifies provider results/webhooks, a generic transaction nests provider data, and BCL synchronization is idempotent and reconciliation-aware.
- Fidelity remains onboarding/planning evidence rather than active code.
- The live mobile app uses authenticated-principal identity for deposits, while a historical explicit correction required `userId` in the protected input. That conflict remains visible.

## Useful Details

- Backend repository skills require thin typed resolvers, one service operation per file, domain-owned helpers/interfaces/models, BCL normalization, local JSDoc style, and user-scoped data access.
- Resend is the default email provider, while Gmail/SMTP alternatives remain because the user explicitly rejected deleting adjacent sending code.
- Expo push tokens and lifecycle notifications are wired end to end across backend and mobile for signup/signin completion, KYC, deposit, withdrawal, and goal reminders.
- Oye is restricted to Bora information and general financial education; it refuses personal advice, recommendations, predictions, unrelated content, and unverifiable facts.
- Reusable financial rule: Mongo sessions protect related local writes, but external provider calls require atomic claims, idempotency, durable webhook state, and reconciliation rather than pretending they are part of a database transaction.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../projects/bora-capital-mobile-app|Bora Capital Advisors Mobile App]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../concepts/codex-project-knowledge-harvest|Codex Project Knowledge Harvest]]

## Contradictions Or Tensions

- Historical input-owned `userId` direction conflicts with the current principal-derived GraphQL/mobile contract and current repository review skill.
- Historical Oye fallback/key-validation expectations do not match current string-interpolated environment handling.
- Fidelity documents and an empty integration boundary coexist with a fully implemented Paystack flow.
- Both repositories were dirty before inspection; historical green builds/tests do not verify the current working trees.
- Mobile OTA machinery exists while updates are disabled in current app configuration.

## Open Questions

- Should deposit identity remain principal-derived, or should the historical explicit `userId` input contract be restored with ownership validation?
- Is Fidelity still planned as a second deposit provider, and which documented collection path has provider approval?
- Should Oye and Resend configuration be repaired to reject missing values reliably while preserving the user-chosen module structure?
- When will the current backend/mobile dirty work be stabilized into reproducible commits?
