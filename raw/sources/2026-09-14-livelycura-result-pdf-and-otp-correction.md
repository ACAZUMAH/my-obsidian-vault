# LivelyCura result PDF and OTP correction

Date: 2026-09-14. Source: direct project conversation and inspected implementation. Sanitized; no recipient identifiers, result values, access links, or verification codes retained.

## User requirement

The user reported that result emails contained no attached PDF and reiterated that result-access verification SMS must use the LivelyCura sender. This is separate from the earlier instruction to preserve the established serlp.com email sender.

## Evidence and durable lesson

The inspected result-email implementation was link-only; preserving the portal's PDF-download implementation did not establish that the email contained an attachment. The delivery contract requires the finalized report as an actual PDF attachment as well as the online link.

The backend already selected LivelyCura for result-access OTP. The browser was using an older result link from a thread containing a newer result email. Using the newest link produced an OTP, and the user confirmed receipt from LivelyCura. No recipient or token is recorded here.

The inspected backend revokes earlier active links when the same result is resent. Its privacy-preserving accepted response can also cover invalid or inactive links and is not proof that an SMS was sent. The UI must avoid unconditional delivery claims and direct recipients to the newest link.

## Verification standard

Generate and visually inspect real PDFs, check visible finalized fields and pagination, and verify the serialized email attachment payload. Keep local checks, deployment, provider acceptance, and confirmed inbox/device receipt distinct.
