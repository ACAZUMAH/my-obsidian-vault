# LivelyCura Backend GraphQL Test Organization Decision

Date: 2026-07-31

## User Correction

> just rewrite those tests those ones was introduced by you and they are failing, also when you check the graphql all the tests are grouped into folders so why did you do different things there

## Failure Evidence

- Backend CI unit shard 2/4 failed all 30 cases in `courierContracts.test.ts` with `ENOENT`.
- The test read GraphQL hooks from sibling Pharmacy Portal and Courier Mobile repositories that were present locally but were not checked out by backend CI.
- Backend build, lint, integration, and the other three unit shards passed in the failing workflow.

## Verified Repair

- Removed the cross-repository file-reading test.
- Grouped courier GraphQL tests under `tests/unit/graphql/courier/`.
- Kept order-owned dispatch schema coverage under `tests/unit/graphql/selling/`.
- Rewrote contract coverage against the backend executable schema and Shield map.
- Focused tests passed 96 of 96; CI unit shard 2/4 passed 696 of 696; lint and build passed.
