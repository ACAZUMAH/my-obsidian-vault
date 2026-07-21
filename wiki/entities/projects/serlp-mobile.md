---
type: entity
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, serlp, expo, erp, mobile]
sources:
  - ../../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../../sources/livelycura-project-knowledge-harvest-batch-3.md
confidence: high
---

# SERLP Mobile

## Summary

Expo mobile application for SERLP ERP operators, adapted from the established LivelyCura mobile architecture.

## Purpose

Provides mobile access to workspace, dashboard, selling, buying, inventory, accounting, HRM, CRM, courier, marketplace, manufacturing, approvals, prescriptions, reports, and configuration concerns.

## Stack

- Expo SDK 54, React Native 0.81, React 19, TypeScript.
- React Navigation, Apollo Client/GraphQL.
- Redux Toolkit plus redux-persist.
- `styled-components/native`, GraphQL Codegen, EAS.
- Yarn.

## Architecture

Uses `expo/AppEntry.js` and `App.tsx`, not Expo Router. `src/navigation` owns stacks/tabs. Apollo operations live with feature hooks. Feature/domain folders live directly under `src`; shared infrastructure is limited to navigation, Apollo, Redux, theme, system, components, hooks, helpers, and constants.

## Folder Ownership

- `apps` owns application-directory/navigation metadata.
- Each operational domain owns its screens and local logic.
- `apollo`, `redux`, `navigation`, `theme`, `system` own application infrastructure.

## Commands

- `yarn start`, `yarn ios`, `yarn android`, `yarn web`
- `yarn generate`
- `yarn type-check`
- `yarn format:check`

## Runtime/Deployment

Expo/EAS application with CI, preview, and production GitHub workflows.

## Durable Conventions

- Follow `livelycura-loop-app` architecture, not Expo Router.
- Use Pharmacy Portal as the ERP GraphQL/domain reference, adapted to mobile interaction rather than copied as desktop UI.
- Apollo hooks own GraphQL operations; Redux persistence owns auth, workspace, and settings state.
- Shared components remain presentation-focused; domains own operational behavior.
- Distribution artwork uses the exact identity “SERLP” and real application screenshots. Do not add “SERLP Mobile,” “by LivelyCura,” an invented rounded badge, phone shadows, dark backing, or a fabricated dashboard. Proven exports are `1242x2688` for iPhone, `2048x2732` for iPad, and `1024x500` for the Play featured graphic, all RGB without alpha.

## Constraints

- Native dependencies must stay compatible with Expo SDK 54.
- Do not introduce a parallel routing architecture.
- Historical distribution renderers and exported images are not present in the current repository; treat their output as historical rather than current deployment state.

## Decisions And Rationale

Reusing the proven family mobile shell reduces divergent navigation, state, and GraphQL patterns while allowing SERLP operator features to remain mobile-specific.

## Verification Expectations

Run codegen, type check, formatting, and intended native platform. Verify auth persistence, workspace selection, navigation, dashboard, selling, inventory, reports, safe areas, and EAS compatibility.

## Evidence

- Current `AGENTS.md`, package, README, app entry, source structure, EAS configuration, and workflows.
- [[../../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Session `019edbb8…` in [[../../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]].

## Contradictions

README uses npm examples, while the repository has a Yarn lockfile and Yarn is the established family package manager. Treat live lockfile/scripts and repository instructions as authoritative. Historical store-artwork files were removed or relocated; only the corrected branding/export convention is current knowledge.

## Confidence

High; explicit repository instructions match the current structure.

## Open Questions

- Which operational modules are production-ready versus scaffolded/mobile-adapted?
- Should repeatable store-artwork renderers be restored here or owned by a separate deployment/design workspace?
