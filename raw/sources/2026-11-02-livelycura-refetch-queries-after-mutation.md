# LivelyCura: refresh screen data with refetchQueries after a mutation

- Date: 2026-11-02
- Author: the user (product owner), during the LivelyCura HRM Employees review in a Claude Code session
- Recorded from: the user's own message (quoted verbatim), relayed by the session agent

## Context

On the HRM Employees page in the SERLP portal (`livelycura-pharmacy-portal`), after Save the old value stays on screen for about 2–3 seconds, until the mutation's `refetchQueries` request returns. The session offered to remove that delay, for example by awaiting the refetch (`awaitRefetchQueries`), returning extra fields from the mutation so Apollo writes them to the cache, or updating the cache with `cache.modify`.

## The user's words (verbatim)

- "we use refetch queries for updating after a mutation and it's across the project so leave it like that"

## Rule

1. After a GraphQL mutation, the LivelyCura client apps (SERLP portal `livelycura-pharmacy-portal`, `serlp-mobile`, `livelycura-loop-app`) refresh screen data with Apollo `refetchQueries`. This is the project-wide pattern.
2. The short moment after Save when the old value still shows, until the refetch lands, is accepted.
3. Don't propose `awaitRefetchQueries`, returning extra fields for cache writes, or `cache.modify` to change it.
