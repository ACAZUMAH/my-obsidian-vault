---
type: source
status: active
created: 2026-11-02
updated: 2026-11-02
tags: [livelycura, apollo, graphql, mutations, conventions, correction]
sources:
  - ../../raw/sources/2026-11-02-livelycura-refetch-queries-after-mutation.md
source_date: 2026-11-02
ingested: 2026-11-02
confidence: high
---

# LivelyCura Refetch Queries After Mutation

## Source

- Raw file: [LivelyCura: refresh screen data with refetchQueries after a mutation](../../raw/sources/2026-11-02-livelycura-refetch-queries-after-mutation.md)
- Date: 2026-11-02
- Author: The user (verbatim message)
- Ingested: 2026-11-02

## Core Claims

- After a GraphQL mutation, the LivelyCura client apps (SERLP portal, serlp-mobile, Loop) refresh screen data with Apollo `refetchQueries`. This is the project-wide pattern.
- The short moment after Save when the old value still shows, until the refetch lands, is accepted.
- Don't propose `awaitRefetchQueries`, returning extra fields for cache writes, or `cache.modify` to change it.

## Useful Details

- Raised on the HRM Employees page in the portal, where the old value showed for about 2–3 seconds after Save; the session had offered to remove the delay.
- Repository check on 2026-11-02 (agent inspection, not the user's statement): `refetchQueries` appears in about 388 portal, 191 serlp-mobile and 9 Loop source files.

## Connections

- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]], [[../projects/serlp-mobile|SERLP Mobile]] and [[../projects/livelycura-loop-app|LivelyCura Loop App]] carry the convention.
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]] (LivelyCura Family): mutation hooks already use typed `useMutation` with relevant `refetchQueries`.
- [[livelycura-hrm-feature-by-feature-review|LivelyCura HRM Feature-By-Feature Review Scope]] and [[livelycura-match-existing-ui|LivelyCura Match Existing UI]] come from the same Employees review.

## Contradictions Or Tensions

- The same check found a few existing files that already use `awaitRefetchQueries` (portal 8, serlp-mobile 1) or `cache.modify` (portal 1, Loop 1). The rule covers proposals to change the refetch pattern; the user said nothing about those existing usages.

## Open Questions

- None.
