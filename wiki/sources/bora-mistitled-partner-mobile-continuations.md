---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, bora, sessions, security, release]
sources:
  - ../../raw/sources/2026-07-21-bora-mistitled-partner-mobile-continuations.txt
confidence: high
---

# Bora Mistitled Partner-Mobile Continuations

## Source

- Raw file: `../../raw/sources/2026-07-21-bora-mistitled-partner-mobile-continuations.txt`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Two coder records titled “Partner Mobile App Setup” actually belong to Bora Capital Backend. They close inherited refresh-session verification and validate/correct a production-hardening plan. Altin content in their replay is ancestor-owned and adds no new Altin evidence.

## Useful Details

- `20260718_022740_80c5a4` — substantive Bora record. Closed inherited authentication repair and wrote a production-hardening plan; plan validation remained pending.
- `20260718_030844_e9e1dc` — substantive Bora record. Validated/corrected the plan, including the Yarn Classic `yarn run check` gate, and closed historical repository checks with time-bounded dependency exceptions.

### Durable Boundaries

- Refresh rotation uses atomic session-scoped compare-and-swap, hash-only token persistence, and family revocation on confirmed reuse without changing public GraphQL response contracts.
- Do not add a production route merely to satisfy a CORS test; rerun and diagnose the actual contract first.
- Fintech release gates prioritize secret-safe logging/rotation, server-verified payment proof, truthful provider/OTP failure handling, provider idempotency, durable contribution bookkeeping, safe reconciliation, transport-complete revocation, and supply-chain controls.
- Under Yarn Classic, invoke the repository script explicitly as `yarn run check`.

## Current Static Boundaries

- Session rotation remains current.
- Open Bora concerns include unredacted Winston output plus a `productions` typo, public client-supplied `depositCash`, and Resend configuration/failure semantics.
- The historical plan is deleted in the dirty tree; CodeQL/Dependabot files are also absent. It is provenance, not a current operational manual.
- Rollbar steps are stale under later Sentry work, though logger redaction remains independently relevant.
- No fresh tests/builds were run during harvesting.

## Connections

- [[bora-quality-deployment-continuations-51-52|Bora Quality And Deployment Continuations 51–52]]
- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Stored titles and replay suggest Partner Mobile/Altin, but unique work is Bora backend.
- Historical production-hardening plan is not current source truth.

## Open Questions

- Which remaining logger, deposit-input, and Resend defects are still intended pre-production blockers?
