# Bora service functions take one input object

Date: 2026-10-20
Source: The user's correction during the Bora push-notification fix (paraphrased; the user's wording was emphatic).

## User correction

The agent had added a second positional parameter to `register(data, ip, app)`. The user rewrote it to take one object and objected to splitting parameters: functions receive everything through a single input object typed by an interface, not as separate positional arguments.

## Implemented

- `register(data: RegisterInput)`, where `RegisterInput extends CreateUserInput` with `ip` and an optional `app`. `register` strips those before `createUser`, whose validator rejects unknown fields; adding them to the shared `CreateUserInput` had broken signup and staff invites.
- Converted at the user's request: `verifyOtpAndSignJwt`, `revokeSession`, `revokeAllUserSessions`, `revokeSessionFamily`, `getUserPushTokens`, and `getPushTokensByUserIds`, each with its own input interface, plus every caller and test.
