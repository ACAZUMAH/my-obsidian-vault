# Bora SMS provider switched to Nalo, Hubtel kept behind a switch

Date: 2026-10-21
Source: The user's requirements and plan approval in a Claude Code session on the Bora backend (`feature/updates`, uncommitted at the time of writing), the LivelyCura backend's current Nalo routing code, and Nalo's published Postman collection (7705958/Uyr7Hydn).

## User requirements

- Nalo Solutions becomes Bora's SMS service. Hubtel stays in the code so the two can always be switched between.
- The Nalo secret key is the `NALO_API_KEY` environment variable. The sender ID is `Boradvisors`.
- The LivelyCura backend's Nalo integration is the reference implementation.
- Use Nalo's bulk sending where it helps, for example many recipients at once in the notification worker or campaigns, instead of one request per message.

## Decisions the user approved (all five recommended options)

1. `SMS_PROVIDER` selects `nalo` or `hubtel`; when unset it defaults to `nalo`.
2. Staging and production refuse to start without the selected provider's credentials (`NALO_API_KEY`, or both `HUBTEL_CLIENT_ID` and `HUBTEL_CLIENT_SECRET`). Development and tests do not require them.
3. The rule that an unknown send outcome fails and is never resent applies to Nalo only for now. Hubtel keeps its existing retry-on-any-provider-error behaviour.
4. Nalo pacing: the worker leases up to 100 SMS every 30 seconds and sends at most 100 recipients per request. Hubtel pacing is unchanged: one SMS every 30 seconds.
5. The campaign SMS hold is unchanged. `CAMPAIGN_SMS_ENABLED` must still be exactly `true`, and the user flips it after live bulk checks.

## Nalo API facts used

- `POST https://sms.nalosolutions.com/smsbackend/Resl_Nalo/send-message/` with a JSON body `{key, msisdn, message, sender_id}`. The key travels in the body, not the URL, but an HTTP client error object still carries the request body.
- Bulk sending means a comma-separated `msisdn` list with one shared message. The response has one `status` and one `job_id`; there is no result per recipient and no personalized bulk endpoint.
- `1701` means accepted. 1702–1709, 1025, and 1026 are documented refusals. 1710 means internal error. No rate limit and no maximum recipients per request are published.
- LivelyCura's current routing code classifies 4xx responses other than 408 as refusals; timeouts, 5xx responses, 1710, and undocumented bodies are unknown and never replayed. LivelyCura does not use multi-recipient sends; it sends to each recipient separately.

## Implemented in Bora

- `parseSmsProvider` in `src/config/env.ts` is used both at boot and on every send. `sendSms` remains the single entry point for every direct caller (OTP, welcome, transaction, withdrawal, resend, mobile wallet) and still returns true or throws.
- A new Nalo adapter (`sms/nalo.ts`) sets a 15-second timeout. Errors are tagged `smsOutcome` REJECTED or UNKNOWN with a sanitized `smsCode`; 1706 maps to `INVALID_RECIPIENT`. Logs carry only the error type, error code, HTTP status, numeric provider status, and outcome; they never include the key, recipients, message, or the raw error.
- `sendBulkSms` is Nalo-only and takes 1 to 100 recipients.
- Sender IDs are per provider: Nalo defaults to `Boradvisors` and can be overridden by `NALO_SMS_SENDER_ID`; Hubtel keeps `BoraCapital` and `HUBTEL_SMS_SENDER_ID`.
- The worker under Nalo checks numbers first, groups deliveries by identical text, and sends each group in requests of up to 100 recipients.
  - Accepted: every delivery is SENT, with the job ID as the provider message ID.
  - Refused: the deliveries are retried.
  - 1706 on a multi-recipient request: each recipient is resent on its own.
  - Unknown: FAILED `SMS_OUTCOME_UNKNOWN`, never resent.
  - No new request starts after half the 2-minute lease; the remaining deliveries are retried with `SMS_SEND_DEFERRED`.
- Under Hubtel the worker path is unchanged.

## Verification

- TypeScript build passed. Prettier passed on the changed files; `format:check` flagged only a file inside an untracked local `.claude/worktrees/` copy.
- Full Jest passed: 169 suites, 1177 tests. Tests use mocked gateways.

## Still to check live before production

- Whether Nalo rejects a whole batch with 1706 when one number is bad, or partly accepts it. The resend-each fallback assumes the whole batch was refused and nothing was sent.
- The rate limit on the Nalo account.
- Approval of the `Boradvisors` sender ID on the Nalo account, and one controlled delivery to a number the user owns.
