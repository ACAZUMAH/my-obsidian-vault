---
type: project
status: active
created: 2026-11-10
updated: 2026-11-10
tags: [project, livelycura, expo, mobile, ordering, red-and-hot]
sources:
  - ../sources/livelycura-red-and-hot-app-kickoff.md
  - ../sources/livelycura-red-and-hot-ui-direction.md
confidence: medium
---

# LivelyCura Red And Hot App

## Summary

Branded Expo ordering app for a second food business, started on 2026-11-10 as a copy of [[livelycura-check-city-app|LivelyCura CheckCity App]]. Logic is identical to Check City; only brand identity has changed in code so far. The owner chose the "Chop Bar" UI direction on 2026-11-10, and the UI must look totally different from Check City.

## Purpose

Customer ordering for Red and Hot: branch selection, menu and category browsing, search, cart and checkout, orders, delivery, profile, addresses, banners, notifications and organization-owned support, exactly as in Check City.

## Stack

Same as Check City at `984f2a6`: Expo SDK 57, React Native 0.86, React 19, TypeScript 6, React Navigation 7, Apollo Client 3 with graphql-ws, Redux Toolkit with redux-persist, styled-components, Reanimated 4, PostHog, expo-updates, EAS, Jest (jest-expo), Prettier, Yarn 1.

## Architecture

Identical to Check City. The backend picks the tenant from the `client` header (`CLIENT_NAME = "RED_AND_HOT_STOREFRONT"`), and the whole app waits on the `GetCurrentCustomApp` bootstrap; without an enabled Custom App record it shows the launch error screen.

## Folder Ownership

As in Check City. Brand values live in `app.config.ts` (`BRAND` block), `app.json`, `src/constants/brand.ts` (`BRAND_NAME`, `BRAND_WEB_DOMAIN`), `src/constants/index.ts` (`CLIENT_NAME`), `src/posthog/config.ts` (`app_name`) and `package.json`. `eas.json` takes `ascAppId` once the App Store record exists.

## Commands

- `yarn start`, `yarn ios`, `yarn android`, `yarn web`
- `yarn type-check`, `yarn format:check`, `yarn test`

## Runtime/Deployment

- Not yet buildable for release: no EAS project, no `updates.url`, no App Store id, no Firebase files or push credentials. The README "Before first run" and "Before first build" checklists list every step.
- `eas init` writes only `extra.eas.projectId`; add `updates.url` to `app.json` by hand afterwards.
- EAS builds do not receive `.env`; set the variables in the project's EAS environments.
- GitHub deploy workflows are manual-only until the repository, `EXPO_TOKEN` secret and EAS project exist.

## Durable Conventions

- Logic stays exactly like Check City. Change looks and brand only; a logic fix is made in both apps, never silently in one.
- Keep the diff from Check City brand-only and centralised so fixes port cleanly. Never copy the brand files across whole.
- Do not run `eas`, submit, update or push from this folder until its own EAS project and store records exist.
- Restyles follow the owner's direction when given; existing content stays.
- The UI must look totally different from Check City. Direction: "Chop Bar" (paper cream, chilli red, palm-oil price stickers, Lilita One and Nunito, roasted-brown dark mode). Product-card price sticker and add button stay as drawn in the Chop Bar mockup; the tab bar, product card image and item detail screen get new designs that do not reuse Check City's shapes. Tab destinations and screen content stay. Picks: tab bar "Signboard plank", card "Edge to edge", item screen "Torn paper" (photo fill). See [[../sources/livelycura-red-and-hot-ui-direction|the UI direction record]].
- Before changing the palette, repoint every use of the `black` token as plain text or shadow colour; the new palette makes `black` the ink on the primary colour.

## Constraints

- Brand assets not received; icon and logos are a grey "R&H" placeholder.
- Identity values (client key, ids, slug, version, web domain) are session defaults pending owner confirmation.
- The colour palette, curated menu picks, delivery thresholds and support contact are still Check City's until the owner decides.

## Decisions And Rationale

- 2026-11-10: copy Check City and change identity only, so behaviour matches and fixes port. See [[../sources/livelycura-red-and-hot-app-kickoff|the kickoff record]].
- Check City's EAS project id, update URL and App Store id were removed rather than replaced, and app links stay off until a real domain exists, so nothing built from this folder can reach Check City's project, listing or updates.
- CheckCity-prefixed code names became neutral names, so the two apps share wording and later fixes diff cleanly.
- 2026-11-10: the owner chose direction B "Chop Bar" over "Ember" (the session's recommendation) and "Clean Heat", because it differs most from Check City. Mockups live in `/Users/acazumah/Documents/LivelyCura/design-probes/red-and-hot-app`.

## Verification Expectations

- `yarn type-check`, `yarn format:check`, `yarn test`, and `expo config` per variant after changes.
- Runtime checks need a `.env` and an enabled `RED_AND_HOT_STOREFRONT` Custom App record.

## Evidence

- [[../sources/livelycura-red-and-hot-app-kickoff|LivelyCura Red And Hot App Kickoff]]: build, checks and adversarial review on 2026-11-10.
- [[../sources/livelycura-red-and-hot-ui-direction|LivelyCura Red And Hot UI Direction]]: the owner's choice of Chop Bar and the three parts to redesign.

## Contradictions

- Inherited Check City defects (profile save refetching a non-existent `me` query, duplicate `GetProducts` operation name, "facility" in the order-placed toast) stay unchanged to keep the apps identical; fixes belong in both.

## Confidence

Medium: the code state is verified and the UI direction is chosen, but the identity values and the final screen designs are not yet confirmed by the owner, and the app has not been run against a backend.

## Open Questions

- Device review of the built Chop Bar screens; brand assets.
- Confirmation of identity defaults; real web domain; support phone and WhatsApp number.
- Own or shared PostHog and Maps keys; whether customer push tokens are kept separate per custom app in the backend.
