---
type: source
status: active
created: 2026-10-16
updated: 2026-10-16
tags: [bora-capital, backend, mongodb, refactor, conventions]
sources:
  - ../../raw/sources/2026-10-16-bora-single-user-update-path.md
  - ../../raw/sources/2026-10-16-bora-user-update-transaction-split.md
source_date: 2026-10-16
ingested: 2026-10-16
confidence: high
---

# Bora User-Update Paths

## Source

- Raw file: [Single user-update path](../../raw/sources/2026-10-16-bora-single-user-update-path.md)
- Raw file: [User updates split by transaction](../../raw/sources/2026-10-16-bora-user-update-transaction-split.md)
- Date: 2026-10-16
- Author: User correction, implemented by the agent
- Ingested: 2026-10-16

## Core Claims

- Single-user writes have exactly two paths in `src/services/users`, and services never call `userModel.findOneAndUpdate`, `findByIdAndUpdate`, `updateOne`, or `user.save()` directly (user correction, 2026-10-16):
  - `updateUserInSession(filter, update, session)` is used only inside a transaction, and the session is a required parameter.
  - `updateUser(filter, update, options?)` is used outside transactions, and its options type rejects a session.
- Both accept a user ID or a conditional filter and return the updated user without `password` or `refreshToken`. The shared filter and options live once in `helpers/userUpdate.ts`.
- The profile mutation service is `updateUserProfile`; the GraphQL mutation keeps the name `updateUser`.
- The rule behind it is general: when the same operation and options repeat across services, write it once and import it.

## Useful Details

- `updateUser` passes other options through, for example `upsert` with `setDefaultsOnInsert`, or `runValidators`; callers cannot override the credential projection. Mongoose `QueryOptions` has an index signature that survives `Omit`, so the session ban is typed as `session?: never`.
- Files outside `services/users` import from `src/services/users/updateUser` or `src/services/users/updateUserInSession` directly, not through the barrel, to avoid circular imports.
- Bulk `updateMany` maintenance and migrations are out of scope.
- Caller tests mock whichever function the caller uses; each function's own spec owns the defaults.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[bora-kyc-supervision-and-statement-update|Bora KYC Supervision And Statement Update]]

## Contradictions Or Tensions

- Supersedes the same day's first version, in which one `updateUserInSession` took an optional `{ session }` and served every caller.

## Open Questions

- None.
