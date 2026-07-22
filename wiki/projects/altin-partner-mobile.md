---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, ceqa, altin, expo, react-native, partner-operations]
sources:
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-1.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-3.md
  - ../sources/hermes-persistent-memory-import.md
  - ../sources/ceqa-altin-hermes-conversation-harvest-supplement-1.md
  - ../sources/altin-mistitled-casual-greeting-continuations.md
confidence: high
---

# Altin Partner Mobile

## Summary

Altin Partner Mobile is an Expo application scaffold for authenticated partner operations across orders, outlets, fleet, team, accounting, and billing. Its runtime foundation is present, but most product surfaces remain placeholders or navigation shells.

## Purpose

Provide mobile partners a single Altin-authenticated entry point to operational modules and their future concrete workflows.

## Stack

- Yarn, Expo 54, React Native 0.81, React 19, and TypeScript 5.9.
- React Navigation 7; no Expo Router.
- Apollo Client 3 and GraphQL.
- Redux Toolkit, Redux Persist, and AsyncStorage.
- Styled Components, React Native Elements, safe-area context, gesture handler, Reanimated/worklets, and Toast.
- Expo Auth Session/Web Browser with OAuth/OIDC Authorization Code and PKCE.

## Architecture

- `App.tsx` composes Redux, theme, Apollo, gesture handling, and navigation.
- The root stack selects Login or authenticated routes from persisted authentication state.
- The authenticated bottom tabs are Home, Search, Apps, Notifications, and More.
- The Apps directory links to Orders, Outlets, Fleet, Team, Accounting, and Billing stacks.
- Apollo obtains a valid access token, attaches bearer and public application-context headers, and sends operations to the configured API.
- Access and refresh tokens, expiry, user, and settings are currently persisted through Redux Persist/AsyncStorage.

## Folder Ownership

- `src/navigation`: stack, tabs, route registration, navigation types, and safe-area/tab presentation.
- `src/login`: OAuth flow, token refresh/revocation, claims mapping, login UI, and auth contracts.
- `src/apollo`: authenticated GraphQL client/provider.
- `src/redux`: persisted auth/settings state and typed store hooks.
- `src/apps`: active module-directory metadata plus tracked legacy generic shell files that currently have no route or barrel consumers.
- `src/orders`, `src/outlets`, `src/fleet`, `src/team`, `src/accounting`, `src/billing`: module-owned roots, drawers, constants/styles, and feature screens.
- `src/components`: reusable presentation primitives such as module headers, drawers, sections, entity lists, and filters.
- Shared list primitives own mechanics and presentation; module feature screens own future query/data, filter state and controls, entity types, row rendering, and navigation.

## Commands

- `yarn start`: Expo development server.
- `yarn android`: native Android run.
- `yarn ios`: native iOS run.
- `yarn web`: Expo web mode.
- `yarn type-check`: TypeScript without emission.
- `yarn format` / `yarn format:check`: Prettier.
- No test, lint, production-build, or Codegen script is currently defined.

## Runtime/Deployment

- `expo/AppEntry.js` is the runtime entry point.
- App variants change display name and native identifier for local/development, preview, and production-like builds.
- Public API/auth/application identifiers are configuration inputs; no secret values belong in the repository or vault.
- No EAS configuration, CI workflow, or deployment pipeline was found.

## Durable Conventions

- Use React Navigation under `src/navigation`; do not introduce Expo Router.
- Preserve Altin primary `#F40F1B` and background `#F9F1EF`.
- Treat SERLP Mobile as an architecture/configuration reference only. Preserve Altin typography, spacing, radii, shadows, modules, and product identity rather than copying SERLP visual tokens.
- Keep Home, Search, raised-center Apps, Notifications, and More as the accepted five-route tab contract. Render active state and order from React Navigation route state plus one typed route configuration rather than a parallel ordering array.
- Derive React Native Elements and styled-components themes from one Redux-controlled light/dark state.
- Keep safe-area, status-bar, and home-indicator backgrounds consistent.
- Feature folders own logic through hooks/services and keep screens thin.
- Desired architecture: every module owns its root, drawer, sections, constants, styles, hooks, data, and concrete feature screens. `Apps` owns directory metadata and root navigation only; shared components remain presentation-only.
- OAuth uses Authorization Code with PKCE. Tokens are never placed in URLs; refresh/revocation and API headers stay centralized.

## Constraints

- SERLP is an architecture/configuration reference only, not a source of Altin branding or business modules.
- Do not centralize business behavior in `AppModuleScreen`, `AppFeatureScreen`, or a module resolver.
- Start from a functional login and authenticated navigation foundation, then grow concrete workflows inside module ownership boundaries.
- Do not copy web-only storage/session guidance directly into React Native.

## Decisions And Rationale

- Repository instructions override the generic create-expo-app README: this app intentionally uses `expo/AppEntry.js` and React Navigation.
- The user corrected the first scaffold to start with login and the minimum authenticated shell rather than eagerly implementing the full documented product.
- OAuth redirects preserve the `altinpartner` scheme and `redirect` path with Authorization Code plus PKCE.
- The current five-tab shell supersedes the historical four-tab arrangement. A fixed floating-track geometry prevents stale flex rules from expanding the pill and collapsing tabs.
- A successful Expo export proves asset inclusion, not native rendering. Current `SvgXml` inline logo ownership supersedes the historically unsuccessful `SvgUri` attempt.
- A module directory is useful for discovery, but module-local roots/drawers prevent generic shells from becoming a business-aware central runtime.
- PKCE is appropriate for a public mobile client because no client secret can be safely embedded in the app.

## Verification Expectations

- Run `yarn type-check` and `yarn format:check`.
- Start Expo and verify login redirect/callback, refresh, logout/revocation, and authenticated route switching.
- Exercise safe areas and tab/navigation backgrounds on iOS and Android.
- Verify configured API/auth endpoints without printing tokens or identifiers.
- Add tests and a release pipeline before calling the scaffold production-ready.

## Evidence

- Current repository: `/Users/acazumah/Documents/C.E.Q.A/altin-partner-mobile`, branch `main`, base commit `f05077b67018`, clean at inspection.
- Current `AGENTS.md`, package manifest, entry point, navigation, auth, Apollo, Redux, theme, module folders, runtime config, and reference documentation.
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-1|C.E.Q.A/Altin Project Knowledge Harvest — Batch 1]].
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-3|C.E.Q.A/Altin Project Knowledge Harvest — Batch 3]] repository reconciliation; no batch-3 Codex record targeted Altin.
- Direct Hermes sessions `20260630_230125_403524`, `20260718_201747_c255ab`, and `20260718_223853_6755f9` in [[../sources/ceqa-altin-hermes-conversation-harvest-supplement-1|C.E.Q.A/Altin Hermes Conversation Harvest — Supplement 1]].
- Direct continuations `20260719_015234_50d0c5` and `20260719_035336_d709a6` in [[../sources/altin-mistitled-casual-greeting-continuations|Altin Mistitled Casual-Greeting Continuations]] establish Apps-directory ownership, reject centralized generic module shells, and compose fourteen module-owned feature screens from shared list primitives.

## Contradictions

- Current source still includes `AppModuleScreen`, `AppFeatureScreen`, and `useAppModule`, but current reference checks found no active route or barrel consumer. They are legacy/inactive code that still conflicts structurally with the desired module-local architecture, not the active runtime owner.
- The generic README says Expo Router, an `app/` directory, npm installation, and a reset script; none describes the current Yarn/React Navigation application or its defined commands.
- Home and many feature screens are placeholders despite broad module registration.
- `app.config.ts`, `app.json`, current API consumption, and reference docs use partially inconsistent config keys/assets; the dynamic and static Expo configs also select different icon assets.
- Auth tokens are persisted in AsyncStorage; the security posture should be reviewed before production use.
- No tests, CI, EAS release configuration, or production build command was found.
- Current Ionicons and registered module destinations supersede the sessions’ Material Community Icons and temporarily unavailable-destination details while preserving the accepted route/theme ownership.

## Confidence

High for current static architecture and explicit repository conventions; medium for authentication/runtime behavior because no device flow, server, build, or external provider was exercised.

## Open Questions

- Which module should be converted from placeholder to its first complete workflow?
- When will the generic module-shell files be removed after module-local screens replace them?
- Which module should receive the first real query/data implementation so its current honest empty-data shell becomes a complete workflow?
- Should token persistence move to platform secure storage before production?
- Which config file and public environment contract should be canonical?
