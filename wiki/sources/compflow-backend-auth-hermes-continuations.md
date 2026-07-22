---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, compflow, auth, onboarding, payments, payroll, rbac]
sources:
  - ../../raw/sources/2026-07-21-compflow-backend-auth-continuations.txt
confidence: high
---

# CompFlow Backend Authentication Hermes Continuations

## Source

- Raw file: `../../raw/sources/2026-07-21-compflow-backend-auth-continuations.txt`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Five direct continuations after the already-classified auth root establish customer-driven subscription onboarding, Moolre plus Paystack provider ownership, dual-channel OTP delivery, payroll implementation, modular-domain correction, RBAC/Shield, and organization lifecycle. Continuation #6 has no fresh human request but carries meaningful closure and test evidence for #5.

## Useful Details

### Classified Records

- `20260711_221940_e79205` — substantive onboarding correction and implementation continuation.
- `20260712_021621_84e0f7` — substantive provider pivot plus payroll-MVP request handoff.
- `20260712_031059_c7fd2c` — substantive payroll implementation and modular-structure correction.
- `20260712_102048_b1481f` — substantive separation-of-concerns and RBAC/organization-lifecycle continuation.
- `20260712_155404_4a08ff` — human-intent shell with substantial inherited execution and verification; adds no new request.

### Onboarding And Payments

- Normal customer flow is public plan discovery → signup → OTP verification → authenticated checkout → verified payment/webhook → organization/owner provisioning → pending document review → admin review.
- Admin-created subscriptions remain possible but are not the primary customer path.
- Moolre SMS and payment adapters coexist with Paystack behind a provider switch.
- Email and SMS OTP delivery are attempted concurrently; identity flow proceeds when at least one configured channel succeeds and fails when all fail.
- Moolre callback-token validation is used because the supplied provider reference did not establish a native signature convention; Paystack keeps signature verification.
- Historical provider behavior was mocked/deterministic; no live payment execution was demonstrated.

### Payroll

- Payroll covers employees, salary setup, configurable annual tax rules, PAYE, SSNIT, payroll runs/items, draft/approve/paid lifecycle, reports, payslips, CSV, and PDFKit output.
- Money uses integer minor units.
- User correction split monolithic payroll ownership into separate models, action-per-file services, subdomains, and GraphQL modules.
- Four intended-to-delete legacy payroll files remain in current source because deletion approval was blocked; post-refactor verification did not complete in that exact record.

### RBAC And Organization Lifecycle

- User and organization create/update ownership belongs to dedicated services; subscription/auth orchestration should not access models inline.
- Auth, users, organizations, and subscription plans own separate GraphQL contracts.
- RBAC uses roles, permissions, custom role IDs, permission tree, assignments, organization lifecycle actions, tenant scope, and GraphQL Shield.
- Root-operation Shield coverage tests compensate for current `fallbackRule: allow`; unmapped operations must fail coverage.
- #6 reached an intermediate green full suite, then ended after later patches without final re-verification.

## Connections

- [[compflow-checkcity-hermes-conversation-harvest-supplement-1|CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1]]
- [[compflow-proper-stack-hermes-continuations|CompFlow Proper Stack Hermes Continuations]]
- [[../projects/compflow-backend|CompFlow Backend]]
- [[../projects/compflow-admin|CompFlow Admin Portal]]
- [[../projects/compflow-client-portal|CompFlow Client Portal]]
- [[../projects/compflow|CompFlow Public Frontend]]

## Contradictions Or Tensions

- The requested temporary Moolre period never ended in current defaults; Moolre remains default unless configured otherwise.
- Shield uses `fallbackRule: allow`, so safety depends on the root-operation coverage test remaining exhaustive.
- Four blocked legacy payroll files remain and create structural ambiguity.
- Historical `adminOverview` protection was later superseded by complete backend removal while Admin still queries it.
- The aggregate post-chain commit cannot be assigned to one exact continuation; no commit or push occurred inside the five records.
- Final #6 patches were not followed by a clean build/test rerun.

## Open Questions

- Should Moolre remain the default provider, or should the deferred Paystack switch be completed?
- Should Shield change to deny-by-default rather than relying on coverage tests around `fallbackRule: allow`?
- Can the four legacy payroll files be safely removed after import resolution is verified?
- What focused suite closes the final #6 authorization and permission-lookup patches?
