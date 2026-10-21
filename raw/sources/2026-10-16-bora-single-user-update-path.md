# Bora single user-update path

Date: 2026-10-16
Source: The user's correction during the Bora backend KYC and cash movement work, and the resulting refactor.

## User correction

After the KYC restructure, the user asked for one shared user-update function: "create a singleUpdateUserInSession write all the updates there and import and use, please you duplicating plenty things when we can write once somewhere and import it and use it across".

## Implemented

- `src/services/users/updateUserInSession.ts` exports `updateUserInSession(filter, update, options)`. The filter is a user ID (string or ObjectId) or a conditional query. It always returns the updated document (`new: true`) without `password` or `refreshToken`. Callers pass `{ session }` to join a transaction, plus other query options such as `upsert`/`setDefaultsOnInsert` or `runValidators`.
- Every single-user write now goes through it: auth sign-in, refresh-token rotation, logout, both password resets, profile update, BCL upsert, identity link, account-number linking and caching, push-token add/remove, legacy KYC approval, KYC submit/restore/approval, staff invite/complete/update/disable, and the bootstrap-admin script (which previously used `user.save()`).
- Before the change, no caller read `password` or `refreshToken` from an update result, so the projection changes no behavior.
- Bulk `userModel.updateMany` calls (invalid push-token cleanup, migrations) are outside its scope.
- Caller unit tests mock `updateUserInSession` and assert what the caller passes; `updateUserInSession.spec.ts` covers ID normalization, defaults, session, and option passthrough. Suite: 157 suites, 1046 tests passing; tsc clean.
