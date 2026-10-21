---
type: source
status: active
created: 2026-08-07
updated: 2026-08-07
tags: [livelycura, choproute, mobile, marketplace, redux, architecture, correction]
sources:
  - ../../raw/sources/2026-08-07-choproute-system-marketplace-ownership-custom-app-removal.md
source_date: 2026-08-07
ingested: 2026-08-07
confidence: high
---

# ChopRoute System Marketplace Ownership And Custom-App Removal

## Source

- Raw file: [2026-08-07-choproute-system-marketplace-ownership-custom-app-removal.md](../../raw/sources/2026-08-07-choproute-system-marketplace-ownership-custom-app-removal.md)
- Date: 2026-08-07
- Author: user correction plus verified implementation
- Ingested: 2026-08-07

## Core Claims

- ChopRoute must not retain a client-side custom-app feature.
- Current marketplace and access-organization loading is application startup work owned by `src/system`, parallel to user loading.
- General marketplace Redux access belongs in one top-level `src/hooks/useMarketPlace.ts` hook.
- `src/marketplace` owns catalog/domain behavior, not global bootstrap, provider gates, or a competing general state hook.

## Useful Details

- `SystemProvider` invokes the user and marketplace startup queries and gates child rendering until Redux is synchronized.
- The marketplace system query loads the marketplace and organizations together, initializes Redux, resets it on errors, and checks that query and Redux identities agree before declaring startup complete.
- CustomApp symbols remaining only in generated GraphQL output reflect the shared backend schema and do not justify restoring client feature files.
- The implementation launched successfully in the iOS Simulator; focused formatting, relaxed-unused TypeScript, and `git diff --check` passed.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-redux-marketplace-state-correction|ChopRoute Redux Marketplace State Correction]]
- [[choproute-marketplace-stage-one-correction|ChopRoute Marketplace Stage-One Correction]]

## Contradictions Or Tensions

This supersedes the temporary implementation where `src/marketplace` owned marketplace bootstrap and a general selector hook. It also removes the historical custom-app client feature from this generic marketplace repository; custom-app support elsewhere in the shared LivelyCura backend remains unaffected.

## Open Questions

- When should Home product and category reads move from the temporary shared catalog query into separate Home-owned query files?
