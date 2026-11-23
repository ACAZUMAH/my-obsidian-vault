# Bora Nalo adapter: recipients without a plus

Date: 2026-10-21
Source: The user's correction later in the same Claude Code session as `2026-10-21-bora-nalo-sms-simplification.md`, plus the user's own edits to the Bora Nalo adapter and `sendSms` (uncommitted on `feature/updates`).

## User correction

- Nalo does not accept a recipient number with a leading `+`; the user cited the Nalo Postman collection (7705958/Uyr7Hydn). The user restated that LivelyCura's backend is the reference.
- LivelyCura's adapter removes the plus inside the adapter: `msisdn: data.to.replace("+", "")`. Bora's Hubtel adapter does the same. The simplified Bora Nalo adapter had joined the numbers without removing it and relied on callers to strip it.

## Current Bora state

- The user rewrote `sms/nalo.ts` in their own style (the user said it is not matched to LivelyCura):
  - JSON POST with a `Content-Type` header and no timeout.
  - `1701` returns true.
  - Any other status, or a request error, is logged and returns false. There is no API-key check.
- The user also removed the `HUBTEL_SMS_SENDER_ID` override. Hubtel now always sends from `BoraCapital`.
- Fix applied on top: the adapter strips the plus from each number before joining them, `data.to.map(to => to.replace('+', '')).join(',')`.
- The worker now checks the returned boolean, so a false result retries the group instead of being marked SENT.
- Verification: TypeScript build, Prettier on the changed files, and full Jest at 168 suites and 1130 tests, all with mocked gateways.
