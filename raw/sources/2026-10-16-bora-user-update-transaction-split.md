# Bora user updates split by transaction

Date: 2026-10-16
Source: The user's correction of the single `updateUserInSession` refactor recorded in `2026-10-16-bora-single-user-update-path.md`.

## User correction

"still wrong move the transactions into that function and pass the session as a param, and those that doesn't update with transactions use the normal updateUser function for that"

## Implemented

- `updateUserInSession(filter, update, session)`: the session is a required parameter. It is used only inside transactions: sign-in refresh-token save, refresh-token rotation, reset password with code, staff invitation completion, KYC approval, and saving the KYC supervision reference.
- `updateUser(filter, update, options?)` is now the generic update outside transactions: logout, password change, BCL upsert, identity link, account-number linking and caching, push tokens, legacy KYC approval, the KYC claim and restore, staff invite/update/disable, and the bootstrap-admin script. Its options type rejects a session (`session?: never`), because Mongoose `QueryOptions` has an index signature that survives `Omit`.
- Both share `toUserFilter` and `userUpdateOptions` from `services/users/helpers/userUpdate.ts`: ID or conditional filter, `new: true`, and a projection without `password` and `refreshToken` that callers cannot override.
- The former profile service `updateUser(data: UpdateUserInput)` became `updateUserProfile`. The GraphQL mutation is still named `updateUser`; its resolver calls `updateUserProfile`.
- Verified: tsc clean; 158 suites, 1048 tests passing; a type probe confirmed both misuse cases fail to compile.
