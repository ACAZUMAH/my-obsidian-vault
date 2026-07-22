---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [compflow, livelycura, checkcity, hermes, project-knowledge, provenance]
sources:
  - ../../raw/sources/2026-07-21-compflow-checkcity-hermes-conversation-harvest-supplement-1.md
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
---

# CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1

## Source

- Raw file: [2026-07-21-compflow-checkcity-hermes-conversation-harvest-supplement-1.md](../../raw/sources/2026-07-21-compflow-checkcity-hermes-conversation-harvest-supplement-1.md)
- Date: 2026-07-21
- Author: Hermes read-only evidence audit
- Ingested: 2026-07-21

## Core Claims

- Three new coder-profile Hermes sessions were substantive. The already processed default-profile CompFlow scaffold session was used only as a duplicate/predecessor control.
- For CompFlow, “spin up the project” means install and wire the actual stack, establish exact provider/runtime/file ownership, follow saved skill references, and prove the applications work. Minimal renderable stubs or green builds that violate architecture are not accepted completion.
- The accepted CompFlow backend separates process entry, startup orchestration, Express creation, Apollo HTTP, GraphQL subscriptions, error formatting, database ownership, JWT middleware, request context, and DataLoader creation.
- CompFlow authentication is OTP-only and mirrors LivelyCura: email/phone login creates a stored OTP, `completeLoginWithToken` verifies it, and JWT issuance follows successful verification. Winston, AJV, Resend, and React Email are the accepted supporting boundaries.
- Internal admin and business client portal are separate product surfaces. The session’s final client-portal request has no supported completion outcome and must not be presented as session-completed work.
- CheckCity’s accepted bottom navigation has Menu, Search, and Orders in one track with Cart as a detached action. Profile/More was explicitly removed from the tabs; profile access is limited to the intended Menu, Cart, and Orders header paths.

## Useful Details

- CompFlow sessions: `20260710_190402_e7ba9f` and `20260711_165753_68ff6f`.
- CheckCity session: `20260707_234259_178721`.
- De-duplicated predecessor: `20260710_173537_54b264`, already covered by CompFlow Hermes Supplement 1.
- Current CompFlow code retains the accepted startup/auth boundaries but has unresolved stale database-bypass documentation, absent Codegen/schema artifacts, removed backend `adminOverview`, an admin fallback that still queries it, and an empty DataLoader set.
- Current CheckCity source preserves three track tabs, detached cart geometry/badge placement, reduced-motion transitions, profile opt-in defaults, and branch-selector-only background/elevation while scrolling.
- Historical checks, tests, builds, bundle results, and browser/simulator observations are not fresh runtime proof.

## Connections

- [[../projects/compflow|CompFlow Public Frontend]]
- [[../projects/compflow-admin|CompFlow Admin]]
- [[../projects/compflow-client-portal|CompFlow Client Portal]]
- [[../projects/compflow-backend|CompFlow Backend]]
- [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]]
- [[compflow-hermes-project-knowledge-harvest-supplement-1|CompFlow Hermes Project Knowledge Harvest — Supplement 1]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- CompFlow public/admin/backend have historical scaffold and later direct Hermes provenance; the client portal remains current repository evidence plus a product-boundary decision, not a completed implementation outcome from the reviewed session.
- The documented CompFlow database bypass and generation inputs are stale or absent in current code.
- Current CheckCity contains notification registration/handling elsewhere, so the session-era statement that notification backend support was unavailable is historical only.
- CheckCity’s current type-check status is unknown because the audit intentionally ran no project command.

## Open Questions

- Should CompFlow remove stale database-bypass and Codegen documentation or restore the missing implementation/artifacts?
- What current backend operation replaces the removed `adminOverview` contract?
- Which CompFlow client-portal services should be converted from demo/static behavior first?
- Are current CheckCity generated GraphQL errors still blocking a clean full type-check?
