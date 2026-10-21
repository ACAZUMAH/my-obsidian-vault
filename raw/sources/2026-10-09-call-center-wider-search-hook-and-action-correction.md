# Call Center Wider Search Hook And Action Correction

Date: 2026-10-09
Source: direct user feedback in the call-center-web-app Claude Code task implementing `searchLocationWider` ("Search wider") in the exact-location field.

## Context

The first implementation added `src/cart/hooks/useSearchLocationWider.ts` with an inline GraphQL response interface and a custom `WiderSearchRequestError` class, unlike the sibling location hooks (`useFindLocationCoordinate`, `useFindLocationAddress`). It also rendered the "Not here? Search wider" action as an `UnstyledButton` row with plain text inside the suggestions dropdown.

## User corrections (verbatim)

On the dropdown action:

> how you did this the agents won't know it's clickerble

On the hook:

> fucking follow the codebase, I don't do this

## Resolution

- The action became a Mantine `Button` (`fullWidth`, `variant="light"`, `radius="lg"`, icon in `leftSection`).
- The hook was rewritten to the sibling-hook shape: fetch-based `useMutation`, `console.log` on a non-OK response, `result.data.<field> as <GeneratedType>`, a `handle<Operation>` wrapper that logs and returns `undefined` on failure, and `{ handle<Operation>, ...mutation }` returned. No inline interfaces or error classes in the hook; contracts stay in the feature `interface` folder.

## Interpretation for future work

New code copies the nearest existing sibling's structure rather than introducing patterns the codebase does not use. Interactive controls inside dropdowns and lists must look interactive.
