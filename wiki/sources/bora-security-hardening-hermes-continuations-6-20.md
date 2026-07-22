---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, bora, security, graphql, authentication, wallets]
sources:
  - ../../raw/sources/2026-07-21-bora-security-hardening-continuations-6-10.txt
  - ../../raw/sources/2026-07-21-bora-security-hardening-continuations-11-15.txt
  - ../../raw/sources/2026-07-21-bora-security-hardening-continuations-16-20.txt
confidence: high
---

# Bora Security Hardening Hermes Continuations 6–20

## Source

- Raw files: three sanitized fast-mode reports under `../../raw/sources/2026-07-21-bora-security-hardening-continuations-*`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Fifteen consecutive Bora backend sessions are substantive evidence-bearing security continuations. They progress from principal-bound GraphQL contracts through wallet/provider credential isolation, resolver/service ownership, financial notification isolation, and purpose-aware authentication recovery. Inherited “disappeared chat” context adds no independent Hermes recovery result.

## Useful Details

### Exact Record Coverage

- `20260714_213232_242ff1` — principal-bound profile update; unsafe arbitrary-user query removed.
- `20260715_002615_32b411` — public wallet list/create inputs stripped of caller-selected identity.
- `20260715_005953_b67276` — owner-first goal lookup and subject-correlated one-time-code completion.
- `20260715_181830_be101e` — atomic code consumption and fail-closed JWT configuration; broader saved task not complete.
- `20260715_201033_443f8f` — immutable principal and deny-by-default GraphQL policy core; closure belongs to successor.
- `20260715_204220_9f3dd0` — principal/policy closure plus atomic owner-scoped wallet mutations.
- `20260716_011320_32adde` — verified Paystack credential writer separated from generic wallet writes; encryption opened.
- `20260716_040411_a5d7e6` — race-safe provider-wallet upsert and fingerprint uniqueness; rotation review incomplete.
- `20260716_041205_9a9677` — rotation race fixed historically; withdrawal identity work opened.
- `20260716_042317_bee1bf` — withdrawal review closed and resolver/service refactor begun; final closure belongs to successor.
- `20260716_052127_c0e9a7` — resolver refactor, DataLoader removal, account-goal enrichment, and notification isolation closed; authentication hardening opened.
- `20260716_134549_6f6505` — first purpose-aware recovery implementation; material review defects remained.
- `20260716_142249_3aba14` — stale-resend protection, password validation/hashing, transactions, and separate recovery/change paths; failed-attempt persistence still flawed.
- `20260716_144609_559128` — corrected transaction/error classification and historically closed purpose-aware recovery.
- `20260716_150130_fcc0ef` — authentication structural cleanup; plaintext-code remediation belongs to successors.

All fifteen are substantive; none is a shell or unrelated-project pivot.

## Durable Architecture

### Principal And Authorization

- Self-scoped public operations omit caller-selected identity. Server-derived principal identity is applied after public input spreading so client fields cannot override it.
- Owner-protected resources are filtered by owner in the initial query and return indistinguishable not-found behavior for absent and cross-owner records.
- HTTP and subscription contexts use an immutable principal; disabled users are rejected.
- Every GraphQL root field requires explicit policy coverage under a deny fallback. Arbitrary-user access remains absent until a real privileged identity and policy model exists.

### Wallet And Provider Credentials

- Owner scope remains in the final atomic wallet mutation, not only in a preliminary read.
- Generic/public wallet services reject provider-managed fields. Verified Paystack processing uses a dedicated internal credential writer.
- Provider credentials are encrypted before persistence, excluded from default projections, bound to owner/provider context, and decrypted only at charge time.
- DigitalOcean encrypted environment storage was accepted as the interim home for application key material; payment credentials remain encrypted in MongoDB.

### Service Ownership And Financial Outcomes

- GraphQL resolvers adapt arguments/principal identity, call one owning service, and return. Loading, authorization, whitelisting, persistence, provider calls, enrichment, and notifications belong to services.
- Batch goal enrichment belongs behind the investment-account service rather than a GraphQL DataLoader layer.
- Notification failure after an accepted BCL transaction is logged but cannot convert financial success into failure or prevent core synchronization.

### Authentication Recovery

- Authentication challenges bind subject, purpose, and observed state through attempt reservation, cleanup, consumption, and resend replacement.
- Authenticated password change remains separate from public rate-limited recovery.
- Recovery validates/hashes the password before consumption, issues no login tokens, and transactionally couples successful consumption with password/session revocation.
- Expected verification failures commit attempt tracking/cleanup; unexpected database or user-update failures roll back consumption.
- A focused sub-control does not complete a broader saved hardening task; roadmap order and acceptance criteria remain authoritative.

## Current Static Boundaries

- Current source retains principal-bound contracts, owner-first lookup, hashed purpose-aware challenges, explicit policy coverage, thin resolvers, no `src/dataLoaders`, and refresh-token families.
- Historically accepted rotation-safe key-ring/fingerprint-key separation is superseded in the dirty working tree by one scalar root key with derived subkeys and active-version-only envelopes. Reconcile before deployment.
- Temporary plaintext credential compatibility and its migration remain incomplete.
- One-challenge-per-user uniqueness exists, but production duplicate preflight/migration evidence was not found.
- Challenge identifiers remain absent, and rate limiting remains process-local rather than shared across replicas.
- Saved hardening plans are deleted in the dirty working tree; preserve their decisions as historical evidence without claiming the live plan paths remain.
- Historical tests, builds, generation, and reviews belong to these records; no current project command was run during harvesting.

## Connections

- [[bora-canonical-identity-authorization-hermes-chain|Bora Canonical Identity And Authorization Hermes Chain]]
- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Historical rotation architecture and current dirty-tree encryption behavior differ materially.
- Local green checks in intermediate records did not close review-discovered concurrency, transaction, compatibility, or deployment defects.
- The current unique challenge index lacks documented duplicate-data rollout preparation.
- Current user-reviewed files outrank replayed or earlier assistant versions.

## Open Questions

- Which encryption/key-rotation design should ship after reconciling current dirty source with the reviewed historical design?
- How will legacy plaintext provider credentials and duplicate challenge records be migrated safely?
- Should rate limiting and challenge identity become shared/durable for multi-replica deployment?
- What unique work begins in successor `20260716_171024_ddce8b`?
