# LivelyCura Project Knowledge Harvest — Batch 1 Evidence Manifest

Date: 2026-07-21

## Scope

- Family: LivelyCura.
- Live repository root: `/Users/acazumah/Documents/LivelyCura`.
- Repository writes: none.
- Codex sessions processed: 8.
- Transcript handling: only session metadata, short sanitized user statements, durable claims, and verification outcomes are preserved here. No full transcript is copied.
- Secret-bearing files and values were excluded. Generated output, dependencies, build output, caches, binary assets, and routine tool chatter were excluded.

## Repository Inventory

| Repository | Purpose supported by current files | Primary live evidence |
| --- | --- | --- |
| `livelycura-admin-portal` | Internal administration for organizations, facilities, users, roles, products, orders, courier, and system concerns | `package.json`, source folders, Docker/Compose files, GitHub workflows |
| `livelycura-backend` | Shared API and domain runtime for ERP, commerce, mobile, MLS, courier, notifications, and agent workflows | `package.json`, README, `src/main.ts`, `src/app.ts`, `src/graphql`, `src/services`, `src/models`, Docker/Compose, GitHub workflows |
| `livelycura-check-city-app` | Branded Expo ordering app with menu, cart, orders, branches, delivery, and notifications | `package.json`, `App.tsx`, feature folders, `eas.json`, GitHub workflows |
| `livelycura-courier-mobile` | Dispatch/rider Expo app for delivery tasks, station, profile, performance, and verification flows | `package.json`, `App.tsx`, feature folders, `eas.json`, GitHub workflows |
| `livelycura-customer-mobile` | Customer Expo app for shopping, care, prescriptions, loyalty, orders, and notifications | `package.json`, `App.tsx`, feature folders, `eas.json`, GitHub workflows |
| `livelycura-customer-portal` | Responsive customer commerce/care portal, including secure public laboratory-result access | `package.json`, README, `src/router`, `src/labResult`, SSR package, Docker/Compose |
| `livelycura-loop-app` | Workforce Expo app for attendance, schedules, shifts, leave, payroll, announcements, and workspace access | `package.json`, `App.tsx`, feature folders, `eas.json`, GitHub workflows |
| `livelycura-pharmacy-portal` | Multi-domain ERP web and desktop application | `package.json`, README, `src/home`, `src/layouts`, `src/mls`, `src/courier`, Electron, Docker/Compose, GitHub workflows |
| `serlp` | Public SERLP marketing, product-storytelling, SEO, and crawler SSR site | `AGENTS.md`, `package.json`, README, `src`, `ssr`, GitHub workflows |
| `serlp-mobile` | SERLP ERP operator mobile application following the LivelyCura Expo architecture | `AGENTS.md`, `package.json`, README, `App.tsx`, `src`, `eas.json`, GitHub workflows |

Every listed directory contains its own `.git` directory and package manifest. The family is therefore a set of independently versioned repositories, not a root monorepo.

## Processed Codex Sessions

| Date | Session ID | Working directory | Indexed title |
| --- | --- | --- | --- |
| 2026-07-20 | `019f7d44-11d6-7052-8733-59ca06469788` | `/Users/acazumah/Documents/LivelyCura` | Audit courier module completeness |
| 2026-07-19 | `019f7af0-4a79-77d3-9bef-9c1abd7a74e0` | `.../livelycura-pharmacy-portal` | Optimize launchpad header |
| 2026-07-18 | `019f7714-8636-77c0-b544-e62372205fd7` | `.../livelycura-pharmacy-portal` | Polish results and test requests |
| 2026-07-17 | `019f6d9c-efe2-79c0-9c92-aaca88309bc3` | `/Users/acazumah/Documents/LivelyCura` | Update model defaults to OpenAI |
| 2026-07-14 | `019f62a3-cea2-7951-9a24-8710d6c68304` | `/Users/acazumah/Documents/LivelyCura` | Update pharmacy portal layout |
| 2026-07-14 | `019f61b7-40b7-7023-b62c-b60a729ec375` | `.../livelycura-customer-portal` | Use impeccable |
| 2026-07-13 | `019f5cbd-0621-7cb0-b4b8-24dfcec53987` | `/Users/acazumah/Documents/LivelyCura` | Add AI result validation |
| 2026-07-12 | `019f56a3-70f8-7ab3-a3e4-ff932654a075` | `/Users/acazumah/Documents/LivelyCura` | Update Checkcity order screen |

## Minimal Sanitized Conversation Evidence

- `019f7d44…`: audit courier completeness across the backend, ERP portal, and dispatch app. The user confirmed a business-agnostic courier network: courier companies or standalone riders, prepaid or cash-on-delivery orders, one courier for all stops, separate rider payout, delivery and cash state tracked separately, provider/network quotes, configurable proof, and explicit remittance.
- `019f7af0…`: the ERP launchpad header was too crowded; the latest correction rejects placing breadcrumbs in the sidebar and asks for an optimized header.
- `019f7714…`: reduce excessive boxed presentation on result details and place test-request status history in an accordion.
- `019f6d9c…`: OpenAI is the selected provider for the project agent model defaults.
- `019f62a3…`: global search, fullscreen, and logout must remain reachable without first entering an app; the home header must not become congested. Five launchpad columns are for very large screens/monitors, not normal laptop widths. Do not add disposable screenshots or markdown artifacts to repositories.
- `019f61b7…`: the customer portal currently targets Ghanaian users and should extend its established product language rather than inventing an unrelated design system.
- `019f5cbd…`: laboratory results follow draft, AI validation, scientist review/override, finalization, explicit send, phone plus OTP access, report, and explanation. AI validation and result delivery own separate folders/interfaces/models; marketplace bidding must remain untouched; MLS uses the existing agent workflow system; result email uses existing templates; public result access is outside the authenticated shell but still follows the customer portal theme; backend tests use Vitest after the Jest migration.
- `019f56a3…`: CheckCity order screens expose reorder and delivery OTP behavior; feature code is split into focused files. Its six-item menu ordering is an explicit temporary home-grid-only frontend rule until a general backend solution exists.

## Current-Code Verification

- All ten repositories use TypeScript and have `yarn.lock`; `livelycura-customer-portal` also has `package-lock.json`, a lockfile conflict to resolve rather than normalize silently.
- Backend current runtime declares Node `>=22.13.0`; Pharmacy Portal declares Node `>=22.12.0`.
- Backend uses Vitest unit and integration configurations. Its README still mentions Mocha and older boilerplate paths, so `package.json` and current tests outrank the README.
- MLS AI validation is implemented under `src/services/mls/resultAIValidation` and calls `src/services/agent/domains/mls/workflows/resultValidation`.
- MLS delivery has separate interfaces, models, and services; result email calls the existing `testResultAvailableEmail` template.
- Finalization checks the exact values hash reviewed by AI, requires a passing validation or an authorized reasoned override, locks the result, and pre-generates explanation without making explanation failure block finalization.
- The customer portal mounts `LabResultAccess` before and outside `MainLayout`; the page retains a dedicated explanatory `LabResultHeader`, OTP flow, report, explanation, and PDF download component.
- Pharmacy Portal current home exposes organization/facility context, global search, global actions, profile/logout, app filtering, and theme controls. Current CSS uses four columns normally and five only at `min-width: 120em`.
- Pharmacy Portal current module header keeps breadcrumbs in the header. MLS and courier are top-level owned feature folders.
- SERLP repository instructions require direct domain folders under `src`, a top-level crawler SSR package, and no Apollo/Redux/data-prefetch layer in SSR.
- SERLP Mobile repository instructions require Expo SDK 54, `expo/AppEntry.js`, React Navigation, Apollo hooks, Redux persistence, and `styled-components/native`; Expo Router is excluded.
- The courier audit historically recorded passing backend, portal, and mobile type checks plus 20 passing backend courier unit tests. That verification is transcript evidence from 2026-07-20, not a test run performed by this harvest.

## Contradictions And Uncertainty

- The approved courier-company/standalone-network and cash-remittance design is newer and broader than current code. The live task schema still models a simplified single pickup/drop-off, agent assignment, task pricing, payment allocations, and combined task status. Treat the network model as desired architecture, not implemented behavior.
- Customer Portal has both Yarn and npm lockfiles. Current scripts and family convention favor Yarn, but the conflict remains unresolved.
- Pharmacy Portal README uses npm examples while the live repository has Yarn scripts/lockfile and GitHub workflows. The manifest records Yarn as current operational evidence.
- Backend README contains stale boilerplate about Mocha, OpenAPI, and logger paths. Current package scripts and source structure are authoritative.
- Several app purposes without dedicated README files are inferred from current route/feature ownership; those purpose statements carry medium confidence.
- Thirty-seven sessions have a LivelyCura working directory. This batch processed only eight and does not claim full family-history coverage.

## Follow-Up Boundary

Next batch remains LivelyCura and should process exactly these eight indexed, high-value older sessions: `019ec6f5-89f0-79f2-9dc7-25a94e6afe70`, `019eb927-e9a8-70e1-b559-9b35bffb628b`, `019ea1d1-ae47-7340-8842-0ee5e5d83363`, `019e9562-55d4-7830-868d-b7a8484cd26c`, `019e78b1-163a-70f0-b619-b4f90e4110f3`, `019e7553-e228-76a2-b842-d69fa817be5c`, `019e4af8-1012-79d3-b679-346a61c1dff6`, and `019e28e5-be8d-7912-be33-816f759c9db7`.
