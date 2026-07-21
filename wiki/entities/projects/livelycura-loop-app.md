---
type: entity
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, livelycura, expo, workforce, mobile]
sources:
  - ../../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../../sources/livelycura-project-knowledge-harvest-batch-3.md
confidence: medium
---

# LivelyCura Loop App

## Summary

Employee/workforce Expo application in the LivelyCura family.

## Purpose

Current features support workspace selection, announcements, attendance, schedules and shifts, leave, payroll, personal information, profiles, and notifications.

## Stack

- Expo SDK 54, React Native 0.81, React 19, TypeScript.
- React Navigation, Apollo Client/GraphQL, Redux Toolkit.
- Shared design system, GraphQL Codegen, EAS.
- Yarn.

## Architecture

`App.tsx` composes providers; `src/navigation` owns route structure. Workforce domains live directly under `src` with shared runtime in `apollo`, `redux`, `theme`, `system`, `hooks`, and `design-system`.

## Folder Ownership

- `workspace`, `profile`, `personal-info`, `login`: employee context.
- `attendance`, `schedule`, `shifts`, `leave`, `payroll`: workforce operations.
- `announcements`, `announcementDetails`, `notifications`: communication.

## Commands

- `yarn start`, `yarn ios`, `yarn android`, `yarn web`
- `yarn generate`
- `yarn type-check`, `yarn format:check`
- EAS profile-specific Android and iOS build commands in `package.json`

## Runtime/Deployment

Expo/EAS application with CI and preview/production deployment workflows.

## Durable Conventions

- This repository is a reference for the family’s Expo plus React Navigation structure.
- Keep workforce features locally owned; shared design-system components remain presentational.
- Distribution artwork uses the actual transparent app icon and the identity “Loop by SERLP,” with real app screenshots rather than invented UI. The proven iPhone export is `1242x2688` RGB without alpha; the Play composition uses one large center phone and two smaller side phones on solid brand green.

## Constraints

- Historical store-artwork outputs were kept in an external Downloads folder and are not present in the repository. Do not infer a current deployment-assets folder from the session.

## Decisions And Rationale

An independent workforce app gives employees a focused surface without exposing the ERP operator portal.

## Verification Expectations

Run codegen, type check, formatting, and intended native platform. Verify workspace/auth persistence, attendance, schedules, leave, payroll, announcements, and notifications when changed.

## Evidence

- Current package, source folders, EAS configuration, and GitHub workflows.
- [[../../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Session `019edb14…` in [[../../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]].

## Contradictions

No root README exists; purpose is inferred from live feature ownership. Historical artwork iterations used an unrelated logo, bordered icon, gradient, and unrealistic framing; the latest corrections reject those iterations. No current repository artifacts remain to verify visually.

## Confidence

High for stack, structure, and store-artwork convention; medium for product rationale.

## Open Questions

- Should distribution artwork live in a dedicated design/deployment repository or remain external to the app repository?
