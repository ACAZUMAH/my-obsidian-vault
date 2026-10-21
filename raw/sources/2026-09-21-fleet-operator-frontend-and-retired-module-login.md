# Fleet Operator Frontend And Retired Module Login

- Date: 2026-09-21
- Source: Direct user request in Codex
- Projects: LivelyCura Backend and LivelyCura Pharmacy Portal

## Direct Request

- Complete the Fleet operator frontend before moving to another Fleet feature.
- The Pharmacy Portal login failed because `CompleteLoginWithToken` attempted to serialize a persisted organization module value of `COURIER` after that value had been removed from the GraphQL `Module` enum.

## Established Context Applied

- Use the general Fleet operator name for people who may be riders, drivers, or both.
- The frontend must use the actual Fleet operator GraphQL contract and `fleet.operators.*` permissions rather than the rejected driver CRUD contract, revision fields, or generic save mutation.
- Keep operator profile, lifecycle, and live work state separate. Company staff need visibility into online status, availability, capacity, load, and last location, while profile registration covers the person's contact, engagement, emergency, identity, licensing, qualification, document, and note information.
- Continue rebuilding Fleet one feature at a time according to the Pharmacy Portal's established feature structure.

## Compatibility Boundary

Retired organization-module values may remain in existing database records while migrations are deferred. GraphQL serialization should omit values that the current `Module` enum cannot represent; it must not restore company Courier as an organization module.

