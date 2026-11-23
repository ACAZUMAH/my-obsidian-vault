---
type: source
status: active
created: 2026-11-10
updated: 2026-11-10
tags: [livelycura, red-and-hot, check-city, expo, mobile, ordering, branding, custom-app]
sources:
  - ../../raw/sources/2026-11-10-livelycura-red-and-hot-app-kickoff.md
source_date: 2026-11-10
ingested: 2026-11-10
confidence: high
---

# LivelyCura Red And Hot App Kickoff

## Source

- Raw file: [LivelyCura Red and Hot app: kickoff and identity port from Check City](../../raw/sources/2026-11-10-livelycura-red-and-hot-app-kickoff.md)
- Date: 2026-11-10
- Author: The owner (request, paraphrased), with the implementing Claude Code session's build and check results
- Ingested: 2026-11-10

## Core Claims

- Red and Hot is a custom branded ordering app for a second food business. Its logic is to stay exactly like Check City's; only the UI changes. Brand assets had not arrived, so placeholders are used until they do.
- The repository `livelycura-red-and-hot-app` was filled from `livelycura-check-city-app` at `origin/main` `984f2a6` (v1.2.3). Only brand identity changed in the first pass; the restyle has not started.
- Identity defaults chosen by the session and not yet confirmed: client key `RED_AND_HOT_STOREFRONT`, ids `com.livelycura.redandhot` (+ `.dev`, `.preview`), slug and scheme `red-and-hot`, version `1.0.0`, placeholder web domain `redandhot.app`.
- The backend needs an enabled Custom App record for `RED_AND_HOT_STOREFRONT`; the app stops on its launch error screen without it. No backend code change is needed.
- Check City's EAS project id, update URL and App Store id were removed, not replaced; app links and the App Store id stay off until real values exist; the GitHub deploy workflows are manual-only. An adversarial review found no logic drift and no remaining route to Check City's project, store listing, updates, analytics or tenant.

## Useful Details

- `src/constants/brand.ts` holds `BRAND_NAME` and `BRAND_WEB_DOMAIN`; `app.config.ts` repeats name and domain in a `BRAND` block because it cannot import from `src/`. The tenant key lives in `src/constants/index.ts` (`CLIENT_NAME`) and the analytics name in `src/posthog/config.ts`.
- `eas init` writes only `extra.eas.projectId`. `updates.url` (`https://u.expo.dev/<project id>`) must be added to `app.json` by hand, or the first store binary ships with over-the-air updates off and only a new binary can fix it.
- EAS builds do not receive `.env` (`.easignore`); the `EXPO_PUBLIC_*` variables and the `GOOGLE_SERVICES_JSON` file variable must be set in the new EAS project's environments, and account-wide variables in the shared Expo account would leak into this project.
- The automated iOS submit needs `submit.production.ios.ascAppId` in `eas.json`; it fails closed while empty.
- Neutral renames replaced CheckCity-prefixed names (deep-link helpers, notification id parser, support GraphQL operations and fragment, push installation storage key, share-image prefix). The backend does not key on those operation names.
- Checks passed: type check, Prettier, Jest 18 suites / 141 tests, iOS bundle export, `expo config` for all four variants. The app was not run by the session.

## Connections

- [[../projects/livelycura-red-and-hot-app|LivelyCura Red And Hot App]] carries the conventions.
- [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]] is the source app whose logic Red and Hot keeps.
- [[../projects/livelycura-backend|LivelyCura Backend]] resolves the tenant from the `client` header through its Custom App records.

## Contradictions Or Tensions

- Keeping logic identical means a second copy of the same code: every logic fix has to be made in both apps. Best interpretation (high confidence): accepted by the owner's "exactly like Check City" request; the diff is kept brand-only so fixes port cleanly.
- Several inherited Check City defects were found (profile save refetches a non-existent `me` query, duplicate `GetProducts` operation name, "facility" wording in the order-placed toast). They were left unchanged so the two apps stay identical; any fix belongs in both.

## Open Questions

- What is the UI direction for Red and Hot?
- Are the identity defaults (client key, ids, slug, version) confirmed?
- What are the real web domain, support phone and WhatsApp number, curated menu picks and delivery thresholds?
- Does Red and Hot get its own PostHog and Maps keys?
- Are customer push tokens kept separate per custom app in the backend?
