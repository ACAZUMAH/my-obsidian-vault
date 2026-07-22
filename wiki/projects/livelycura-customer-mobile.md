---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, livelycura, expo, customer, mobile]
sources:
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
confidence: medium
---

# LivelyCura Customer Mobile

## Summary

Customer-facing Expo application for LivelyCura shopping and care journeys.

## Purpose

Current feature ownership includes home/product discovery, categories, favorites, cart/checkout, orders, prescriptions, care access, loyalty, profile, addresses, walkthrough, and notifications.

## Stack

- Expo SDK 54, React Native 0.81, React 19, TypeScript.
- React Navigation, Apollo Client/GraphQL, Redux Toolkit.
- GraphQL Codegen, persistent client state, EAS.
- Yarn.

## Architecture

`App.tsx` composes native providers. `src/navigation` owns route structure. Customer domains live directly under `src`; shared infrastructure remains in `apollo`, `redux`, `theme`, `system`, `components`, `hooks`, and `helpers`.

## Folder Ownership

- `home`, `products`, `productDetails`, `categories`, `favorites`: discovery.
- `cart`, `checkout`, `orders`, `orderDetails`: commerce.
- `prescriptions`, `prescriptionDetails`, `get-care`: health/care.
- `login`, `profile`, `addresses`, `loyalty`, `notifications`: customer identity and engagement.

## Commands

- `yarn start`, `yarn ios`, `yarn android`, `yarn web`
- `yarn generate`
- `yarn type-check`
- `yarn format:check`

## Runtime/Deployment

Expo/EAS application with CI, preview, and production GitHub workflows.

## Durable Conventions

- Follow the family React Navigation and feature-owned mobile architecture.
- Keep Apollo server state, Redux application/session state, and local screen state deliberately separate.
- Preserve native safe-area, status-bar, and theme behavior.

## Constraints

- No processed batch-1 session establishes a customer-mobile-specific product correction; current code is the primary evidence.

## Decisions And Rationale

The independent repository keeps consumer shopping/care interaction separate from ERP operations and workforce/courier apps.

## Verification Expectations

Run codegen, type check, formatting, and the intended native platform. Exercise authentication persistence, navigation, cart/checkout, order state, prescriptions, and notification behavior when touched.

## Evidence

- Current package, source layout, EAS configuration, and GitHub workflows.
- [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].

## Contradictions

There is no root README, so purpose is inferred from live folders and routes.

## Confidence

High for stack and current folder ownership; medium for broader domain wording and historical rationale.

## Open Questions

- Which older Codex sessions contain the latest customer-mobile-specific interaction rules?
- Is secure laboratory-result history intentionally web-only or planned for this app later?
