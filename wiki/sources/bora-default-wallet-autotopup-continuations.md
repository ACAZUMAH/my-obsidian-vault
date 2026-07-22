---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, bora, wallets, authorization, auto-top-up]
sources:
  - ../../raw/sources/2026-07-21-bora-default-wallet-autotopup-final-chain.txt
confidence: high
---

# Bora Default-Profile Wallet And Auto-Top-Up Continuations

## Source

- Raw file: `../../raw/sources/2026-07-21-bora-default-wallet-autotopup-final-chain.txt`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Six substantive default-profile Bora continuations complete owner-scoped wallet update/deactivation, remove provider-managed fields from public wallet contracts, enforce wallet eligibility for auto-top-up selection, centralize owner-scoped canonical wallet lookup, and owner-scope auto-top-up updates.

## Useful Details

- `20260714_004726_db109b` — substantive; owner-bound wallet update closed.
- `20260714_012250_ad27cc` — substantive; owner-bound wallet deletion/deactivation closed.
- `20260714_012850_992578` — substantive; provider-managed fields removed from public wallet create.
- `20260714_023558_3a7c70` — substantive; public wallet update fields removed and create-side auto-top-up eligibility closed.
- `20260714_032503_c35046` — substantive; update-side replacement eligibility and shared canonical owner-scoped lookup closed.
- `20260714_040859_2b8be1` — substantive; owner-scoped auto-top-up record update closed and historically verified after a temporary interruption.

### Durable Boundaries

- Wallet mutation and deactivation bind the authenticated owner at resolver and service boundaries; missing and cross-owner records share not-found behavior.
- Public wallet contracts exclude provider-managed credentials/metadata; verified provider ingestion owns a separate trusted writer.
- Auto-top-up wallet selection requires authenticated ownership plus active, reusable, and payment-method eligibility before mutation.
- Resolve known IDs through a shared owner-scoped service, apply domain-specific checks, and persist the fetched canonical ID.
- Auto-top-up record mutation first resolves the record under authenticated ownership.

## Current Static Boundaries

- Current source retains these outcomes and strengthens final wallet mutation predicates with owner and active state.
- Provider credential writes now use a dedicated encrypted internal path; generic create/update reject provider-managed fields.
- Public auto-top-up paths pass authenticated identity.
- `getAutoTopUpById` still permits an ownerless internal `findById` fallback when identity is omitted, so the helper itself is not universally fail-closed.
- Historical checks were not rerun against current source.

## Connections

- [[bora-canonical-identity-authorization-hermes-chain|Bora Canonical Identity And Authorization Hermes Chain]]
- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Public calls are scoped, but the internal auto-top-up helper retains an ownerless fallback.

## Open Questions

- Should every `getAutoTopUpById` caller be required to provide an owner/principal or use an explicitly named privileged internal operation?
