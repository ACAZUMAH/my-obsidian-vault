---
type: source
status: active
created: 2026-10-25
updated: 2026-10-26
tags: [bora-capital, backend, funds, storage, uploads]
sources:
  - ../../raw/sources/2026-10-25-bora-fund-fact-sheet-pdfs.md
  - ../../raw/sources/2026-10-26-bora-staging-storage-already-fixed.md
source_date: 2026-10-24
ingested: 2026-10-25
confidence: high
---

# Bora Fund Fact-Sheet PDFs

## Source

- Raw file: [Bora fund fact-sheet PDFs](../../raw/sources/2026-10-25-bora-fund-fact-sheet-pdfs.md)
- Date: 2026-10-24
- Author: User decisions, implemented by the agent
- Ingested: 2026-10-25
- Correction: [Staging storage was already fixed](../../raw/sources/2026-10-26-bora-staging-storage-already-fixed.md), direct user correction on 2026-10-26. The raw record's statement that staging banner uploads return 502 came from Kusantec's 23 Oct handoff and was stale. The 502 was Sentry issue BORA-CAPITAL-V: `SPACES_ENDPOINT` was deployed without `https://` (`ERR_INVALID_URL`). It was diagnosed in the Claude Code session "Error investigation" on 2026-10-23, where the user said they had updated the envs.

## Core Claims

- **One draft PDF and one published PDF per fund, with no versions.** The official fact-sheet PDF attaches to the fund draft and goes live with `publishFund`. A replaced or discarded PDF is deleted (user decision; staff review before publishing).
- **Field extraction from the PDF stays in the admin portal.** The backend stores and serves the file only.
- **Publishing is refused when the live PDF and the facts carry different as-of dates.** The live PDF is the draft PDF, or else the published one.
- **PDFs are capped at 3 MiB** to keep the 5 MB JSON body limit.
- **Private files are served only as short-lived signed URLs** pinned to their storage folder. Fact-sheet file deletes go through a reference check, so a fund never points at a missing file.
- **Customers get the PDF's description in the fund details and the signed link from a separate query.** The link is never cached inside the details.

## Useful Details

- **Contract:**
  - `uploadFundFactSheet(data: UploadFundFactSheetInput!)` (funds.update, 10 per minute per staff member)
  - `deleteFundDraftFactSheet(portfolioId)`
  - `AdminFund.draftFactSheet` / `publishedFactSheet` (`FundFactSheet`, with a lazy `url`)
  - `CISFundDetails.officialFactSheet { asOfDate fileName sizeBytes }`
  - `getCISFundFactSheetUrl(portfolioId)`, which is `isAuthenticated` and returns only a visible published fund's published PDF
- **Upload checks:**
  - `%PDF-` at byte 0 and `%%EOF` in the last 1024 bytes
  - `asOfDate` at exactly 00:00 UTC
  - a basename-only file name ending in `.pdf`
- **Upload order:** validate, then load the fund, then store, then an optimistic swap on `draftUpdatedAt`.
- **Why deletes check references first:** a thrown `findOneAndUpdate` may still have committed under retryable writes, so cleanup deletes only files no fund references. The delete is best effort and logged.
- **Signing:** `@aws-sdk/s3-request-presigner` 3.1089.0, 600 s, with an ASCII-only `inline` Content-Disposition that carries both `filename` and RFC 6266 `filename*`.
- **Audit events:** `FUND_FACT_SHEET_UPLOADED`, `FUND_FACT_SHEET_PUBLISHED` and `FUND_FACT_SHEET_DELETED`. Their `uploadId` and `sha256` are on the metadata allowlist.
- **GraphQL input rename:** the user's `setFundVisibilityInput` became `SetFundVisibilityInput`. The lowercase TypeScript service input interfaces are kept.
- **Customer app:** never trust a `digitaloceanspaces.com` host. Path-style URLs share a regional host with every DigitalOcean customer.
- **Stale local install after `yarn add`.** Adding the presigner with `yarn add` left stale `@smithy/*` folders nested under the hoisted `@aws-sdk/core` in local `node_modules`. Real signing then failed with `buildQueryString is not a function`, while the mocked specs passed. A fresh `--frozen-lockfile` install was correct, so the lockfile was fine; rebuilding `node_modules` fixed it. `tests/unit/services/storage/storageSigning.spec.ts` now signs offline with the real SDK to catch this.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-fund-administration-access-control|Bora Fund Administration And Access Control]]
- [[bora-notifications-marketing|Bora Notifications, Campaigns, And Banners]] (LivelyCura-style uploads that the banners introduced)
- [[bora-frontend-handoff-frozen|Bora Frontend Handoffs Frozen Once Sent]] (the contract is in `docs/frontend-handoff-2026-10-24.md`)
- [[bora-single-input-object-convention|Bora Service Functions Take One Input Object]]

## Contradictions Or Tensions

- Kusantec proposed an `Upload!` scalar, document kinds and statuses, `SUPERSEDED` retention, a 15 MB limit, and a 409 when a draft document exists. The implemented contract replaces all of these, and the handoff explains why.
- Publish and discard act on the draft as it is when clicked. A client-sent `expectedDraftUpdatedAt` is deferred along with versioning.

## Open Questions

- Should Bora be able to withdraw a published PDF without replacing it?
- Live upload, signing, and expiry on staging have not been exercised yet.
