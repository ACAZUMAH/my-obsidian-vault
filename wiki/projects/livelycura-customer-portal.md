---
type: project
status: active
created: 2026-07-21
updated: 2026-09-14
tags: [project, livelycura, customer, web, laboratory-results]
sources:
  - ../sources/livelycura-result-link-environments.md
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/customer-portal-support-rendering-conventions.md
confidence: high
---

# LivelyCura Customer Portal

## Summary

Responsive customer web portal for LivelyCura commerce, care, prescriptions, and secure laboratory-result access.

## Purpose

Supports product discovery, cart/checkout/payment, orders, prescriptions, settings, and Ghana-focused customer journeys. It also hosts a public OTP-gated finalized laboratory-report flow.

## Stack

- TypeScript, React 19, Vite 5.
- Mantine 9, Apollo Client, Redux Toolkit, React Router 6.
- Vitest, Storybook, GraphQL Codegen.
- Static client plus top-level crawler SSR package.
- Yarn is used by scripts, but an npm lockfile also exists.

## Architecture

The authenticated support center implements the marketplace customer side of [[../concepts/livelycura-customer-support-architecture|LivelyCura Customer Support Architecture]], while public phone, WhatsApp, and Instagram contact information remains visible before login. Support replies can reach registered browsers through strict case-thread deep links.

`src/app`, `providers`, `redux`, `router`, and `services` compose shared runtime. Customer domains live directly under `src`. `ssr/` is a separate crawler package.

The public `LabResultAccess` route is mounted before and outside `MainLayout`. The feature owns access state, phone and OTP forms, report presentation, explanation, and PDF generation.

## Folder Ownership

- `home`, `product(s)`, `cart`, `checkout`, `payment`, `user-order(s)`: commerce.
- `prescription(s)`, `get-care`, `labResult`: care and results.
- `authentication`, `settings`, `privacy`, `terms`: identity and trust.
- `components`, `layouts`, `hooks`, `helpers`, `services`: shared presentation/runtime.

## Commands

- `yarn start`
- `yarn generate`
- `yarn lint`, `yarn format:check`
- `yarn test`
- `yarn build`
- `yarn ssr`, `yarn build:ssr:local`
- `yarn storybook`

## Runtime/Deployment

Vite static application with Docker/Compose files and a separately buildable SSR package. No current GitHub workflow directory was found in this repository during the batch.

## Durable Conventions

- Current audience and copy are Ghana-focused.
- Extend the portal’s existing theme and interaction language; do not introduce an unrelated visual system.
- Public flows may sit outside the authenticated app shell while retaining the product theme and their own task-explaining page header.
- Complex features own focused components, hooks, helpers, interfaces, and PDF code rather than one monolithic page.
- Use the existing `Conditional` component for conditional JSX rather than ternary/null rendering; keep optional child expressions safe. Support CSS belongs in `src/support/styles`. Preserve the user's accepted layout, and show the latest chat in support-history rows rather than the case number. See [[../sources/customer-portal-support-rendering-conventions|Customer Portal Support Rendering Conventions]].

## Constraints

- The public laboratory-result flow omits the main application header, not the page-level explanatory header.
- Online access uses the customer phone plus OTP before exposing a finalized report. An emailed PDF is a separate attached copy.
- Do not turn a generic OTP-request accepted response into an unconditional claim that an SMS was sent. Explain current-link and matching-number requirements and point to the newest result email/SMS because resending revokes earlier links. See [[../sources/livelycura-result-link-environments|Result Link Environments]].
- Internal AI findings and staff-only notes are not customer report content.
- Explanation failure must not block the report.

## Decisions And Rationale

Laboratory results are accessible without a customer account because recipients arrive from a secure delivery link. The standalone route avoids authenticated-app chrome while preserving trust, facility identity, clear instructions, explanation, and PDF download.

## Verification Expectations

Run codegen, lint/format, Vitest, static build, and SSR build when relevant. Exercise phone, OTP, invalid/expired access, report, explanation retry, PDF download, responsive layout, and direct route loading.

## Evidence

- Current package, router, `src/labResult`, SSR package, Docker/Compose, and README.
- Sessions `019f61b7…` and `019f5cbd…` in [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].

## Contradictions

- Both `yarn.lock` and `package-lock.json` exist. Do not regenerate either casually; resolve package-manager ownership explicitly.
- README recommends Node 14 and describes a simpler Vite app, while current package versions and SSR/result features are newer.

## Confidence

High for current architecture and laboratory-result decisions; medium for wider portal product positioning.

## Open Questions

- Should Yarn become the sole lockfile authority?
- Should current CI/deployment workflows be restored or documented elsewhere?
