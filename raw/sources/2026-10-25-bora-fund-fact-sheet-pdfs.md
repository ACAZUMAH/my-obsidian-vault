# Bora fund fact-sheet PDFs: private storage, published with the draft

Date: 2026-10-24 (decisions and implementation), recorded 2026-10-25
Source: Direct user decisions in a Claude Code session on `bora-capital-backend` (`feature/updates`), answering Kusantec's 23 Oct handoff "Handoff for Caleb: fund fact sheets", plus the implemented change.

## Request

The user asked to add uploading the official fact-sheet document to storage (section 1 of the Kusantec handoff). In their words, versioning "isn't really necessary to me cus they will have to make sure they go through it before they publish", and converting the fields from the PDF and updating the funds will be done at the frontend.

## User decisions

- No version history, no `SUPERSEDED` state, no version collection (section 3 of the Kusantec handoff is out of scope). Staff review before they publish.
- PDF field extraction stays in the admin portal (section 4 out of scope). Section 2 (customer facts such as `asOfDate`) was not part of the request.
- PDFs are capped at 3 MiB so the existing 5 MB `express.json` body limit stays. Real Bora fact sheets are 445–552 KB; 15 MB would have needed a ~21 MB body limit for every caller.
- Publishing is refused when the PDF that would go live (the draft PDF, or else the current published PDF) has a different as-of date from the facts being published.
- The 2026-10-22 frontend handoff was already sent, so the contract goes in a new `docs/frontend-handoff-2026-10-24.md`.
- The user's uncommitted GraphQL input `setFundVisibilityInput` is renamed `SetFundVisibilityInput`, matching every other input. The service input interfaces stay lowercase as the user wrote them (`publishFundInput`, `setFundVisibilityInput`).

## Implemented design

- `Fund` gains `draftFactSheet` and `publishedFactSheet` sub-documents: `uploadId` (ref `uploads`), `fileName`, `asOfDate`, `sizeBytes`, `sha256`, `uploadedBy`, `uploadedAt`. A draft PDF exists only while `draftFacts` exists.
- `uploadFundFactSheet(data: UploadFundFactSheetInput!)` (funds.update, 10 uploads per minute per staff member): base64 or data-URL PDF, `%PDF-` at byte 0 and `%%EOF` in the last 1024 bytes, `asOfDate` exactly 00:00 UTC, file name reduced to a safe basename ending in `.pdf`. Order: validate, load the fund, store privately in `funds/fact-sheets`, then an optimistic swap on `{ _id, draftFacts exists, draftUpdatedAt }` that bumps `draftUpdatedAt`. Uploading again replaces the draft PDF.
- `deleteFundDraftFactSheet(portfolioId)`, `discardFundDraft` and `publishFund` clear or move the slots; `publishFund` deletes the PDF a new one replaces. Old files are deleted, never kept.
- Every fact-sheet file delete goes through one reference-checked, best-effort helper: it deletes only if no fund's draft or published slot references the upload, and it logs instead of failing. Reason (review finding): a thrown `findOneAndUpdate` can still have committed under MongoDB retryable writes, so deleting on any error could leave a fund pointing at a missing file.
- Private files are served only as signed GET URLs (`@aws-sdk/s3-request-presigner` 3.1089.0, 600 s), pinned to `StorageDirectory.FundFactSheets`, with an ASCII-only RFC 6266 `inline` Content-Disposition (`filename` fallback plus `filename*`).
- Admin: `AdminFund.draftFactSheet` / `publishedFactSheet` (`FundFactSheet` with a lazily signed `url`). Customer: `CISFundDetails.officialFactSheet { asOfDate fileName sizeBytes }` with no link, and a separate `getCISFundFactSheetUrl(portfolioId)` query (isAuthenticated) that signs only the published PDF of a visible published fund. A link inside the cached details would expire in the Apollo cache, a refetch would call BCL, and a link failure would blank the fund screen.
- Audit events `FUND_FACT_SHEET_UPLOADED`, `FUND_FACT_SHEET_PUBLISHED`, `FUND_FACT_SHEET_DELETED`; `uploadId` and `sha256` added to the audit metadata allowlist.
- The customer app must not add any `digitaloceanspaces.com` host to its trusted web hosts: path-style Spaces URLs share a regional host with every DigitalOcean customer.

## Verification

- `yarn generate` (offline: codegen loads `src/graphql/index.ts`, no server needed, but the new dependency must be installed first), `yarn build`, focused specs, and full Jest: 171 suites, 1202 tests passing. All mocked; no live Spaces upload, signing, or expiry was exercised.
- Staging banner uploads already return 502 ("storage rejected the image"); fact-sheet uploads share that storage, so live checks wait for the staging `SPACES_*` settings to be fixed.
