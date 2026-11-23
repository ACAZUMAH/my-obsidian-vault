---
type: source
status: active
created: 2026-09-04
updated: 2026-11-12
tags: [livelycura, customer-portal, frontend, conventions]
sources:
  - ../../raw/sources/2026-09-04-customer-portal-support-rendering-conventions.md
  - ../../raw/sources/2026-11-12-livelycura-customer-portal-account-pages-approved.md
---

# Customer Portal Support Rendering Conventions

## Source

- Raw file: [Direct user correction](../../raw/sources/2026-09-04-customer-portal-support-rendering-conventions.md)
- Raw file: [Account pages built and approved](../../raw/sources/2026-11-12-livelycura-customer-portal-account-pages-approved.md)
- Date: 2026-09-04.
- Author: user, direct Codex conversation.
- Ingested: 2026-09-04.

## Core Claims

- Preserve the user's updated Customer Portal support layout.
- Use the existing conditional components instead of JSX ternary/null rendering.
- Keep support styles in a feature-owned styles folder.
- Support history rows should preview the latest chat, not the case number. Updated 2026-11-12: the owner approved the Green Room support inbox, where rows keep the latest-chat preview and also show the case number and a status chip, so similar cases can be told apart.

## Useful Details

Current source identifies the shared component as `Conditional` from `src/components` and the support styles folder as `src/support/styles`. Conditional children still require safe optional access because JSX expressions are evaluated before the wrapper renders.

## Connections

- [[../projects/livelycura-customer-portal|LivelyCura Customer Portal]] owns these conventions.
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]] supplies the broader feature-ownership and safe optional-rendering rules.

## Contradictions Or Tensions

Earlier support JSX used ternary/null rendering and scattered CSS files. The explicit user correction supersedes that implementation pattern; it does not request removal of value-selection ternaries in application logic.

## Open Questions

None for these scoped conventions.
