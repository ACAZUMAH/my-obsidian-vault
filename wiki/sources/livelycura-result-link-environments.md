---
type: source
status: active
created: 2026-09-10
updated: 2026-09-14
tags: [livelycura, backend, mls, notifications]
sources:
  - ../../raw/sources/2026-09-10-livelycura-result-link-environments.md
  - ../../raw/sources/2026-09-10-livelycura-result-email-sender-correction.md
  - ../../raw/sources/2026-09-14-livelycura-result-pdf-and-otp-correction.md
---

# LivelyCura Result Link Environments

## Source

- Raw file: [User result-link routing instruction](../../raw/sources/2026-09-10-livelycura-result-link-environments.md).
- Related correction: [SMS-only sender scope](../../raw/sources/2026-09-10-livelycura-result-email-sender-correction.md).
- Related correction: [PDF attachment and result-access OTP contract](../../raw/sources/2026-09-14-livelycura-result-pdf-and-otp-correction.md).
- Date: 2026-09-10.
- Author: user, direct project conversation.
- Ingested: 2026-09-10.

## Core Claims

Laboratory result links must target the customer portal for the sending backend's environment: local uses `http://localhost:5173/`, staging uses `https://staging.livelycura.com/`, and production uses `https://livelycura.com/`.

SMS sender identity, email sender address, and result-link origin are independent. The user authorized the LivelyCura sender change for SMS only; it must not switch email to the livelycura.com domain.

Result emails must include an actual finalized-report PDF attachment alongside the secure online link. Both result-link SMS and result-access OTP use the LivelyCura SMS identity.

## Useful Details

The mapping is for result delivery, not ERP portal navigation or unrelated notification links. Preserve the result-access path and token beneath the selected origin; SMS and email must agree.

At the 2026-09-10 correction, the central LivelyCura branding uses `LivelyCura <no-reply@serlp.com>` for email, matching the working customer-login path. Result delivery must reuse that email identity rather than a separate `noreply@livelycura.com` fallback or result-only override. Provider verification and inbox delivery must not be inferred from mocked unit-test success.

Resending the same result revokes earlier active links. The generic OTP-request acceptance response protects recipient privacy and does not prove that a text was sent. The UI must explain that the link must be current and the number must match, with guidance to open the newest result email or SMS.

Attachment verification covers real PDF generation, visible finalized fields, pagination, and serialized provider payload. Online OTP protection is separate from possession of the emailed PDF; do not describe an attachment as OTP-gated.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]] owns result-link creation and notification delivery.
- [[../projects/livelycura-customer-portal|LivelyCura Customer Portal]] owns public, OTP-gated result access.

## Contradictions Or Tensions

A staging result link must not fall back to localhost or the ERP portal. This decision does not change unrelated environment URLs.

The result-email implementation had a separate livelycura.com sender despite the central branding's serlp.com address. The user's later correction rejects that mismatch; do not treat a customer-portal URL as authorization to change the sending domain.

The inspected email path was link-only. An unchanged browser PDF-download feature was insufficient evidence for the earlier assurance about email attachments.

## Open Questions

None for the requested origin mapping. Deployment verification remains separate from the convention.
