---
type: source
status: active
created: 2026-10-09
updated: 2026-10-09
tags: [ceqa, call-center, location, hooks, ui, codebase-consistency]
sources:
  - ../../raw/sources/2026-10-09-call-center-wider-search-hook-and-action-correction.md
---

# Call Center Wider Search Hook And Action Correction

## Source

- Raw file: [2026-10-09-call-center-wider-search-hook-and-action-correction.md](../../raw/sources/2026-10-09-call-center-wider-search-hook-and-action-correction.md)
- Date: 2026-10-09
- Author: direct user correction; interpretation labeled separately.
- Ingested: 2026-10-09

## Core Claims

- The user rejected a new request hook that declared an inline response interface and a custom error class: the codebase does not do this.
- The user rejected an `UnstyledButton` text row as a dropdown action because agents would not recognise it as clickable.

## Useful Details

- Sibling location hooks are the template: fetch-based `useMutation`, non-OK responses logged, the reply cast to the generated GraphQL type, a `handle<Operation>` wrapper that logs and returns `undefined` on failure, and `{ handle<Operation>, ...mutation }` returned. Callers check `response?.success`.
- Operational interpretation: put request/response contracts in the feature `interface` folder, never inline in a hook file.
- Dropdown/list actions use a Mantine `Button` (light variant, `radius="lg"`, icon in `leftSection`) rather than an unstyled row.

## Connections

- [[../projects/call-center-web-app|Call Center Web App]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Contradictions Or Tensions

- `useAuthenticationDataQuery` defines `AccountRequestError`; the user's correction makes the sibling location hooks, not that file, the template for new feature request hooks.

## Open Questions

- None.
