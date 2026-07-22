---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, bora, authentication, sessions, secrets, logging]
sources:
  - ../../raw/sources/2026-07-21-bora-auth-session-hardening-continuations-21-25.txt
  - ../../raw/sources/2026-07-21-bora-auth-session-hardening-continuations-26-30.txt
  - ../../raw/sources/2026-07-21-bora-auth-session-hardening-continuations-31-35.txt
confidence: high
---

# Bora Authentication And Session Hardening Continuations 21–35

## Source

- Raw files: three concise fast-mode reports under `../../raw/sources/2026-07-21-bora-auth-session-hardening-continuations-*`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Fifteen substantive Bora continuations harden authentication-code storage and attempts, transactional login, refresh rotation, JWT verification, environment hygiene, and structured redaction. A frontend challenge-ID branch was explicitly rejected and removed. Later runtime/topology proposals were provisional or rejected; current Bora architecture retains Node 22, GraphQL subscriptions, operation-specific limits, and app-managed migrations/crons.

## Useful Details

### Exact Record Coverage

- `20260716_171024_ddce8b` — hashed authentication-code storage opened; review/resend closure incomplete.
- `20260716_173700_e3851f` — plaintext-code remediation closed; atomic attempts opened; live-file reread correction reinforced.
- `20260716_181502_464de1` — exact-state atomic attempt reservation and fifth-attempt race closed.
- `20260716_190101_fc7c91` — transactional login begun; retry and post-commit behavior incomplete.
- `20260716_195151_d31746` — transactional login closed; challenge-ID branch opened but not accepted.
- `20260716_213123_3e04a2` — transactional-login verification closed; challenge-ID work continued provisionally.
- `20260716_220448_5c8635` — challenge-ID work reviewed, then explicitly rejected by the user.
- `20260716_221628_2126ad` — challenge-ID contract removed while preserving OTP hardening.
- `20260716_224305_4b2a58` — password-change revocation closed; refresh rotation opened with review defects.
- `20260716_232659_ef9122` — atomic refresh defects closed; shared REST/GraphQL transport consistency added with final sign-off pending.
- `20260717_000211_40b097` — shared refresh/JWT/environment controls closed narrowly.
- `20260717_104556_c85f75` — recursive structured redaction added; historical Rollbar sink is superseded by Sentry.
- `20260717_111529_f0e89d` — Apollo shutdown handle fixed; wider runtime work remained provisional.
- `20260717_120442_3d7a6d` — AJV build blocker resolved; failed financial-control patch changed nothing.
- `20260717_125037_b7fd83` — audit snapshot completed but independent review returned NO-GO; historical secrets and unauthorized topology changes identified.

All fifteen are substantive; none is a shell or unrelated-project pivot.

### Authentication And Session Architecture

- Persist authentication codes only as hashes. Exact-state reservation and consumption predicates bind the observed hash/state so stripped undefined values cannot broaden writes.
- Every expensive comparison follows successful atomic attempt reservation. Concurrency preserves the allowed fifth attempt while preventing an exhausted competing request from deleting it.
- Login couples OTP consumption and session persistence in one retry-safe transaction. Expected verification outcomes commit attempt bookkeeping; unexpected persistence failures roll back.
- Transaction callbacks return discriminated per-invocation results rather than mutating outer state across retries.
- Sessions close before best-effort notifications; notification failure cannot mask committed login.
- Bora’s approved OTP contract is email plus OTP. Do not add a frontend challenge identifier without a new product/security decision.
- Password changes revoke refresh capability and require sign-in again.
- Refresh is one-time atomic rotation through one owning service shared by REST and GraphQL. Generate replacement credentials before compare-and-swap, use POST for state-changing REST refresh, and sanitize credential versus operational failures.
- Current source has advanced to `sid`, `familyId`, and `jti` session families with family revocation on reuse.

### JWT, Secrets, Logging, And Runtime

- JWT verification constrains issuer, audience, algorithm, and distinct access/refresh secrets.
- Environment templates contain names/placeholders only; real `.env*` files remain ignored.
- Deleting a tracked secret-bearing artifact is not credential rotation or Git-history cleanup.
- Structured logs and monitoring payloads are recursively redacted before transport; never attach full users, credentials, tokens, or raw provider payloads.
- Retain GraphQL subscriptions, operation-specific Shield limits, Node 22 compatibility, and app-managed startup migrations/crons unless an explicitly approved topology change replaces them.
- Existing folder ownership and one-service-operation-per-file conventions outrank provisional monolithic hardening patches.

## Current Static Boundaries

- Current source confirms hash-only OTPs, exact-state attempts, transactional login, email-plus-OTP, POST refresh, shared transport delegation, refresh-token families, no-cache responses, and structured redaction.
- Password reset currently revokes session records separately before password/legacy-token update; session-family revocation and password mutation are not one database transaction.
- Likely real historical credentials existed under JWT access, JWT refresh, Rollbar, and Expo variable names. Values are intentionally excluded; rotation and Git-history disposition remain unresolved.
- Removing the tracked environment file did not prove external credential rotation or historical purge.
- Rollbar is historical and superseded by Sentry.
- Broad “repository complete” claims from this sequence are not production-readiness evidence because independent review found financial/runtime blockers.
- Historical test/build/review results remain session-attributed; no current project command was run during harvesting.

## Connections

- [[bora-security-hardening-hermes-continuations-6-20|Bora Security Hardening Hermes Continuations 6–20]]
- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Challenge-ID implementation reached green intermediate checks but was explicitly rejected and removed; it is superseded history, not an outstanding feature.
- A green repository snapshot was followed by a NO-GO security review and cannot establish readiness.
- Historical runtime/topology edits were later corrected back to the project’s existing architecture.
- Password reset/session-family revocation is not fully transactionally coupled in current static source.

## Open Questions

- Have every historical JWT/Rollbar/Expo credential been rotated at its provider, and what Git-history cleanup decision was made?
- Should password mutation and full session-family revocation become one transaction?
- What unique durable work begins in successor `20260717_160904_8adba5`?
