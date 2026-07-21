---
type: entity
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, livelycura, expo, courier, mobile]
sources:
  - ../../sources/livelycura-project-knowledge-harvest-batch-1.md
confidence: medium
---

# LivelyCura Courier Mobile

## Summary

Expo dispatch application for delivery riders in the LivelyCura/SERLP delivery network.

## Purpose

Current feature ownership covers available/assigned tasks, task details, station and address context, pickup/drop-off verification, notifications, profile setup, account status, and performance.

## Stack

- Expo SDK 54, React Native 0.81, React 19, TypeScript.
- React Navigation, Apollo Client/GraphQL, Redux Toolkit.
- Shared mobile design system, GraphQL Codegen, EAS.
- Yarn.

## Architecture

`App.tsx` composes providers; `src/navigation` owns routing. Task, station, profile, performance, login, and notification areas own their screens and local logic. `apollo`, `redux`, `theme`, `providers`, and `design-system` own cross-feature runtime/presentation.

## Folder Ownership

- `tasks`, `task`, `today`: work discovery and execution.
- `station`, `addresses`: route/fulfillment context.
- `profile`, `profileSetup`, `accountStatus`, `performance`: rider lifecycle.
- `notifications`, `posthog`: operational feedback and instrumentation.

## Commands

- `yarn start`, `yarn ios`, `yarn android`, `yarn web`
- `yarn generate`
- `yarn type-check`
- `yarn format:check`

## Runtime/Deployment

Expo/EAS application with CI, preview, and production GitHub workflows.

## Durable Conventions

- The product is not pharmacy-only; riders serve any ERP merchant.
- Courier companies and standalone riders are distinct provider modes.
- One courier handles all stops in an accepted multi-pickup route.
- Customer delivery fee, provider quote, rider payout, collected amount, and remittance are separate monetary concepts.
- Delivery progress and cash-remittance state are separate lifecycles.

## Constraints

- COD may involve cash or mobile money and requires an exact collection amount.
- Provider acceptance precedes company rider assignment; standalone acceptance combines provider and rider responsibility.
- Proof and remittance policy are contract/configuration driven, not one hard-coded rule.

## Decisions And Rationale

The separation supports prepaid and COD orders, courier-company fleets, and standalone riders without treating the rider’s earnings as the merchant-facing delivery fee.

## Verification Expectations

Run codegen, type check, and platform checks. Verify the full task journey and state synchronization with backend and ERP portal. A 2026-07-20 audit recorded a passing mobile type check, but this harvest did not rerun it.

## Evidence

- Current package, source layout, EAS configuration, and workflows.
- Session `019f7d44…` in [[../../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].

## Contradictions

The approved network/payment model exceeds the current backend task schema and therefore should not be described as shipped behavior.

## Confidence

High for current mobile structure; medium for target workflow until backend and portal implementation land.

## Open Questions

- Which screens and GraphQL contracts will own provider acceptance versus rider acceptance?
- How will proof, COD confirmation, and remittance be represented offline and reconciled safely?
