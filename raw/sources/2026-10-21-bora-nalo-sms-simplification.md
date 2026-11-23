# Bora Nalo SMS cut back to the LivelyCura reference

Date: 2026-10-21
Source: The user's correction later in the same Claude Code session as `2026-10-21-bora-nalo-sms-provider.md`, and the resulting simplified Bora backend change (uncommitted on `feature/updates` at the time of writing).

## User correction

After the first build, the user said it was too much over-engineering and full of unnecessary things. They had named the LivelyCura backend as the reference precisely so that the work would follow it rather than add complexity. They approved cutting the build back to the reference.

## Removed from the first build

- Outcome classification (REJECTED/UNKNOWN tags and the unknown-outcome-no-resend rule), job-ID sanitising, and the fallback that read Nalo's `code` field.
- The per-recipient resend after a batch was rejected with 1706, the send-time budget, and the `SMS_SEND_DEFERRED` retries.
- The startup credential check and `SMS_PROVIDER` validation in `src/config/env.ts`, plus the `NALO_SMS_SENDER_ID` override.
- About a dozen new interfaces, a separate SMS helpers file, a separate bulk-send file, and most of the new tests.

## Simplified implementation

- `sms/nalo.ts` follows LivelyCura's `naloSendSimpleSms`:
  - It POSTs `{key, msisdn, message, sender_id}` with a 15-second timeout, and `msisdn` holds the comma-joined recipients.
  - Status `1701` returns true; anything else throws 502.
  - Logs carry only the error type, error code, HTTP status, and provider status, per the Bora logging rule.
- `sendSms` uses Nalo unless `SMS_PROVIDER` is exactly `hubtel`. The sender is `Boradvisors` for Nalo and stays `BoraCapital` (or `HUBTEL_SMS_SENDER_ID`) for Hubtel.
- `sendBulkSms` sends one Nalo request to many recipients.
- Under Nalo the worker leases up to 100 SMS per 30-second cycle, rejects invalid numbers first, groups identical texts, and sends one request per group. Success marks every delivery in the group SENT; failure retries them all, matching Hubtel's existing behaviour.
- Under Hubtel the worker still sends one SMS per 30 seconds. The campaign SMS hold is unchanged.

## Verification

- TypeScript build passed. Prettier passed on the changed files.
- Full Jest passed: 168 suites, 1132 tests, all with mocked gateways.

## Accepted trade-off

- A Nalo timeout is retried like any other provider error, so a message may occasionally be sent twice. This matches Hubtel and LivelyCura's simple adapter.
