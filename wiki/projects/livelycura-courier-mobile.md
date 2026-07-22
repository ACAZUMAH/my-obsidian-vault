---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, livelycura, expo, courier, mobile]
sources:
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/livelycura-project-knowledge-harvest-batch-4.md
  - ../sources/hermes-generalized-skills-courier-recovery-harvest-batch-1.md
  - ../sources/courier-mobile-evening-work-hermes-chain.md
confidence: high
---

# LivelyCura Courier Mobile

## Summary

Expo dispatch application publicly branded as `SERLP Dispatch`; `livelycura-courier-mobile` is the internal repository/package identity.

## Purpose

Lets eligible couriers sign up and, after operational approval, manage available/assigned tasks, task details, station and address context, pickup/drop-off verification, notifications, profile setup, account status, and performance.

## Stack

- Expo SDK 54, React Native 0.81, React 19, TypeScript.
- React Navigation, Apollo Client/GraphQL, Redux Toolkit.
- Shared mobile design system, GraphQL Codegen, Expo Updates plus optional store-driven binary updates, EAS.
- Yarn.

## Architecture

`App.tsx` composes providers; `src/navigation` owns routing. Task, station, profile, performance, login, and notification areas own their screens and local logic. `apollo`, `redux`, `theme`, `providers`, and `design-system` own cross-feature runtime/presentation.

## Folder Ownership

- `tasks`, `task`, `today`: work discovery and execution.
- `station`, `addresses`: route/fulfillment context.
- `profile`, `profileSetup`, `accountStatus`, `performance`: rider lifecycle.
- `notifications`, `posthog`: operational feedback and instrumentation.
- `login`, `components/ui`: phone/OTP authentication and reusable/native input presentation.
- `navigation`: one typed `taskId` route contract plus production-only store-update checks.
- `design-system`: minimal cross-feature presentation tokens; the current barrel exposes a radii contract used by shared courier components.

## Commands

- `yarn start`, `yarn ios`, `yarn android`, `yarn web`
- `yarn generate`
- `yarn type-check`
- `yarn format:check`

## Runtime/Deployment

Expo/EAS application with CI, preview, and production GitHub workflows. Public app/config naming is `SERLP Dispatch`, including development/preview variants; iPad remains supported.

## Durable Conventions

- The product is not pharmacy-only; riders serve any ERP merchant.
- Courier companies and standalone riders are distinct provider modes.
- One courier handles all stops in an accepted multi-pickup route.
- Customer delivery fee, provider quote, rider payout, collected amount, and remittance are separate monetary concepts.
- Delivery progress and cash-remittance state are separate lifecycles.
- Notification taps map the backend’s existing nested task identifier to the app’s one canonical `{ taskId }` route parameter. In-app cards and `TaskScreen` use the same name; do not introduce `id`/`taskId` fallbacks for one concept.
- Authentication uses native controlled numeric input behavior for the four-digit OTP, with paste/autofill and tablet/Android behavior included in platform QA.
- Match iOS card restraint on Android by auditing `elevation` separately from iOS shadow properties; station, task, today, performance, and single-task card surfaces intentionally use zero elevation.
- When untracked design-system files are lost, inspect actual consumers and a compatible sibling implementation, then restore the minimum required contract. Do not claim Git recovery for a path that was never tracked.
- Binary store updates are production-only and dynamically load the optional native module. Android starts only an allowed immediate flow; iOS prompts; failures never block startup. OTA `expo-updates` remains separate.
- Public store artwork and copy use `SERLP Dispatch`, never the internal repository name. The Play featured graphic uses the courier identity at `1024x500`; current phone/tablet screenshot artifacts are external release assets.
- When exact sibling behavior is requested, transfer the real component, dependency, theme, and form contract, then adapt only Courier-owned mutations and navigation. Do not substitute a visual approximation.
- Preserve Courier’s flat tab/header layout when the request concerns color consistency. Normalize every mounted layer—root, safe area, status bar, navigation theme, scene/tab containers, screens, and headers—rather than redesigning the navigation.
- Rounded bottom header borders may need an absolute overlay with bottom/side borders and matching radii; a bottom border alone does not paint rounded side arcs reliably.

## Constraints

- COD may involve cash or mobile money and requires an exact collection amount.
- Provider acceptance precedes company rider assignment; standalone acceptance combines provider and rider responsibility.
- Proof and remittance policy are contract/configuration driven, not one hard-coded rule.
- Public account creation does not mean unrestricted task access: identity/profile approval can gate operational courier features for safety and compliance.
- iOS camera, photo-library, and location purpose strings must describe concrete courier uses. App Review must receive a reviewer-accessible approved account with representative profile/task data, while credentials stay out of the vault and repository documentation.

## Decisions And Rationale

The separation supports prepaid and COD orders, courier-company fleets, and standalone riders without treating the rider’s earnings as the merchant-facing delivery fee. Public distribution and operational approval are intentionally separate: anyone eligible can discover/sign up for SERLP Dispatch, while approval protects delivery operations.

## Verification Expectations

Run codegen, type check, and platform checks. Verify phone and OTP entry, paste/delete/autofill, button state, keyboard clearance, and successful/error submission on Android, iPhone, and supported iPad layouts. Exercise notification taps from logged-in/logged-out states, canonical `taskId` navigation, all task/station/performance surfaces, every system-background layer, rounded header arcs, Android/iOS shadow parity, purpose-string output, production store-update behavior, and the full task journey with backend/ERP state synchronization. A 2026-07-20 audit recorded a passing mobile type check, but this harvest did not rerun it.

## Evidence

- Current package, source layout, EAS configuration, and workflows.
- Session `019f7d44…` in [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Sessions `019dfdd7…`, `019dfdba…`, `019dfd88…`, and `019de13d…` plus current app/auth/navigation/notification/task source in [[../sources/livelycura-project-knowledge-harvest-batch-4|LivelyCura Project Knowledge Harvest — Batch 4]].
- Direct Hermes session `20260622_115444_d37ddc` plus current static `src/design-system` source in [[../sources/hermes-generalized-skills-courier-recovery-harvest-batch-1|Hermes Generalized Skills And Courier Recovery Harvest — Batch 1]]. Historical type checking removed the missing-module error but retained unrelated failures; this harvest did not rerun commands.
- Direct sessions `20260621_210927_566f24` and `20260621_234644_f9a795` plus current clean source in [[../sources/courier-mobile-evening-work-hermes-chain|Courier Mobile Evening Work Hermes Chain]] establish the sibling-derived phone contract, restored flat navigation, color-token layering, and rounded-border overlay; exact-session visual acceptance remained unresolved.

## Contradictions

- The approved network/payment model exceeds the current backend task schema and therefore should not be described as shipped behavior.
- The App Store auth-copy session ended with an explicit revert. Current auth later contains a public-sign-up hint, but that session is negative evidence rather than the provenance of current copy.
- A reusable `CustomOtpInput` was historically integrated and still exists, but current `Auth.tsx` uses an inline native controlled `TextInput`; treat the unused component as unresolved cleanup, not current auth architecture.
- Historical store identifiers and external screenshot outputs changed. Current config is authoritative, and external/binary artifacts were not validated by this harvest.
- `HomeHeader` and `AnimatedTabItem` remain tracked but unimported after the rejected floating-tab redesign. They are dormant residue, not current UI behavior.

## Confidence

High for current structure, public identity, auth/update/task routing, and platform styling; medium for the target provider/payment workflow until backend and portal implementation land.

## Open Questions

- Which screens and GraphQL contracts will own provider acceptance versus rider acceptance?
- How will proof, COD confirmation, and remittance be represented offline and reconciled safely?
- Should the unused `CustomOtpInput` be removed or restored after current Android/iPad regression testing?
- Is the seeded App Review account verified as approved and populated in the current release process without documenting its credentials?
