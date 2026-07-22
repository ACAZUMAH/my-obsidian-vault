---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, bora, identity, authorization, deposits, auto-topup]
sources:
  - ../../raw/sources/2026-07-21-bora-canonical-identity-authorization-chain.txt
confidence: high
---

# Bora Canonical Identity And Authorization Hermes Chain

## Source

- Raw file: `../../raw/sources/2026-07-21-bora-canonical-identity-authorization-chain.txt`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Four replay-heavy Bora backend continuations complete canonical fetched-identity handling, owner-scoped auto-top-up cancellation, principal-bound deposit initialization, and principal-bound investment-account lookup. The “disappeared chat” title is inherited process context; all unique implementation belongs to Bora.

## Useful Details

### Classified Records

- `20260714_183503_dea58d` — substantive canonical-ID implementation continuation; focused closure only.
- `20260714_185052_a2dc32` — substantive execution continuation completing canonical-ID work and full historical verification without a fresh directive.
- `20260714_191715_4cf650` — substantive auto-top-up authorization closure plus interrupted deposit-identity fix.
- `20260714_202812_edffb3` — substantive deposit/codegen closure and investment-account authorization completion.

### Canonical Identity

Externally supplied IDs are resolved at the responsible service boundary. Downstream operations use canonical IDs and relationships from fetched documents rather than caller-supplied aliases or repeated lookups. The correction spans auth, notifications, goals, wallets, auto-top-ups, portfolios, and accounts.

### Authorization Fixes

- Auto-top-up cancellation binds identity to authenticated context, owner-scopes lookup before mutation, and mutates by fetched canonical ID.
- Public deposit initialization omits `userId`; authenticated backend context supplies identity.
- Trusted internal provider/wallet input remains separate from public GraphQL input.
- `getMyInvestmentAccount` binds to authenticated context and public input omits `userId`.

### Historical Verification

- Canonical-ID closure: 24 suites/139 tests, build, formatting, and diff check passed.
- Auto-top-up cancellation: 24 suites/143 tests plus build/format/diff passed.
- Deposit closure: 25 suites/145 tests plus generation/build/format/diff and temporary-server cleanup passed.
- Investment-account closure: 26 suites/147 tests plus generation/build/format/diff passed.

These are historical session outcomes, not current verification of the later dirty backend tree.

## Connections

- [[kusantec-bora-hermes-conversation-harvest-supplement-1|Kusantec/Bora Hermes Conversation Harvest — Supplement 1]]
- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../projects/bora-capital-mobile-app|Bora Capital Advisors Mobile App]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Earlier contracts accepted explicit deposit/account `userId`; these records and current source derive identity from authenticated principal context.
- Historical context used `user._id`; current source uses immutable `principal.userId`, a later hardening rather than a reversal.
- Deposit Fix 17 is incomplete in `20260714_191715_4cf650`; generation, compatibility cleanup, full verification, and server cleanup belong to its successor.
- An internal auto-top-up helper still supports a trusted ownerless path even though public GraphQL paths are scoped.
- Current mobile code complies, but one utility comment still describes the superseded explicit-user-ID contract.
- A later aggregate security commit carries many paths but cannot be mapped one-to-one to these records.

## Open Questions

- Should the stale mobile deposit comment be corrected?
- Should the trusted ownerless auto-top-up helper receive a narrower typed/internal-only boundary?
- What unique work begins in successor `20260714_213232_242ff1`?
