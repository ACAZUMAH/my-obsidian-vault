---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, bora, runtime, paystack, bcl, sessions]
sources:
  - ../../raw/sources/2026-07-21-bora-runtime-payments-continuations-36-40.txt
  - ../../raw/sources/2026-07-21-bora-runtime-payments-continuations-41-45.txt
  - ../../raw/sources/2026-07-21-bora-runtime-payments-continuations-46-50.txt
confidence: high
---

# Bora Runtime And Payment Safety Continuations 36–50

## Source

- Raw files: three concise fast-mode reports under `../../raw/sources/2026-07-21-bora-runtime-payments-continuations-*`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Fifteen substantive Bora continuations restore the approved single-API runtime, correct CORS/Helmet and release assumptions, move BCL/Paystack calls outside retryable MongoDB transactions, establish durable webhook/reconciliation boundaries, add server-side session families, and begin structural enum/interface cleanup. Broad GO claims and temporary control removals were later corrected; current static source retains the safety controls.

## Useful Details

### Exact Record Coverage

- `20260717_160904_8adba5` — approved runtime restored; global Mongoose filter sanitization removed; CORS/Helmet handoff incomplete.
- `20260717_181727_d2d2a0` — CORS/Helmet and originless-native behavior closed; historical Docker layout added but absent now.
- `20260717_185333_99a99e` — release path clarified; Gitleaks failure unresolved.
- `20260717_210544_8446e4` — broken Gitleaks job removed; BCL transaction-risk redesign opened.
- `20260717_231534_72cf41` — BCL claim/external/finalize/reconcile boundary historically closed.
- `20260717_235541_b19a5b` — deposit initialization and BCL boundary closed with durable sync states.
- `20260718_001950_896bb0` — signed-webhook trigger plus server verification closed.
- `20260718_003414_a6fd49` — durable webhook inbox/claim/outcome handling closed.
- `20260718_005111_f5dcf8` — go-live scope correction; proposed control removal superseded.
- `20260718_010140_297ee6` — partial verification/inbox removal interrupted and reversed by successor.
- `20260718_010657_7ecbd1` — controls restored/retained and split into focused modules; roadmap remained open.
- `20260718_012431_daf649` — BCL lookup and Paystack initialization moved outside transactions; premature GO rejected.
- `20260718_013411_326127` — webhook modules advanced; session-family integration incomplete.
- `20260718_023215_ef5e17` — session families and bounded reconciliation closed; structural cleanup opened.
- `20260718_032701_a0bb20` — interface/enum cleanup advanced but remained interrupted until successor.

All fifteen are substantive; none is a shell or unrelated-project pivot.

### Runtime And Delivery Decisions

- Preserve Bora’s approved single API process with GraphQL subscriptions, app-managed crons/migrations, `/` and `/health`, and straightforward startup/signal handling unless a new topology is explicitly approved.
- Allow configured development/staging browser origins, production whitelist checks, and originless React Native requests.
- An empty browser whitelist does not block ordinary React Native requests; Compose files have no effect unless invoked.
- Release flow is `feature/updates` to `develop`/staging to `main`/production.
- Security hardening must not silently replace startup, endpoint, CORS, Helmet, subscription, or mobile contracts.

### Payment And Reconciliation Architecture

- Use durable local claim, external provider call outside Mongo transactions, short transactional finalization, then post-commit notification.
- Keep BCL/Paystack lookups and checkout initialization outside retryable database transaction callbacks.
- Ambiguous external outcomes enter durable reconciliation state; never resubmit BCL money movement without a provider idempotency/status-lookup guarantee.
- A valid Paystack signature is only a trigger. Obtain reference, amount, currency, status, and provider ID through server-to-server verification before BCL credit.
- Persist safe webhook receipt metadata/digest before provider verification; atomically claim duplicates and support bounded retry, stale-claim recovery, processed/failed/dead-letter outcomes. Invalid signatures create no receipt.
- Split webhook receipt, claim, provider verification/post, BCL synchronization, finalization, reconciliation, and notification by failure/transaction boundary.
- Notifications occur after commit and cannot reverse financial success.

### Sessions And Structural Ownership

- Server-side sessions use `sid`, family, and JTI claims; store only refresh hashes and support atomic rotation, family revocation on reuse, device logout, password-reset revoke-all, and bounded legacy migration.
- Preserve the explicit instruction not to modify withdrawal while deposit/security scope is active.
- Shared interfaces and enums belong in established common ownership layers, not models/services/helpers. Persisted enum casing changes require a migration.
- Go-live claims must cover the agreed acceptance scope, not merely the latest green slice.

## Current Static Boundaries

- Current source retains modular webhook/BCL ownership, hourly reconciliation, session-family services, uppercase persisted enums, and the enum migration.
- BCL ambiguity remains manual/alert-only; reconciliation retries Paystack verification but does not resend money.
- Historical monotonic-finalization closure conflicts with current `bclSync/finalizeDeposit.ts`, which updates by transaction ID without requiring the expected processing/sync state; reconciliation marking remains state-guarded.
- Historical Docker/Compose and CodeQL/Dependabot files discussed here are absent now; Gitleaks also remains absent.
- Current repository is materially dirty, so historical green gates and clean/pushed branch claims are not current readiness evidence.
- Historical Rollbar alerts are superseded by Sentry.
- No current project command was run during harvesting.

## Connections

- [[bora-authentication-session-hardening-continuations-21-35|Bora Authentication And Session Hardening Continuations 21–35]]
- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- The control-removal branch in #44–#45 was reversed; verification and durable inbox controls remain current.
- Current successful BCL finalization lacks the historically reviewed exact-state guard.
- Automatic BCL resubmission remains blocked by missing external idempotency/status lookup.
- Broad historical GO claims were explicitly corrected and cannot establish production readiness.

## Open Questions

- Should successful BCL finalization restore an exact expected-state predicate?
- What provider contract can make BCL reconciliation safely automatable?
- What unique work and closure occur in successors `20260718_035439_fd6fd5` and `20260718_042843_74753d`?
