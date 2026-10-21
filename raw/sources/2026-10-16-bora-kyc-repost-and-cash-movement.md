# Bora KYC re-post after rejection, and Grow Wealth cash movement statement

Date: 2026-10-16
Source: BCL's answers in the shared WhatsApp group (relayed by the user as screenshots and text), the user's decisions, and the approved implementation plan.

## KYC

Asked whether customers could update rejected KYC data, BCL replied that the workflow belongs to the partner. Store the KYC, fetch the status, update the stored data based on the reject reason if it is rejected, and push the KYC again with the amended fields to restart the process. "Once it's rejected on the IMS you can re-post it." Partners have no rights to amend data on the core IMS, whether it is under supervision or not, because any posted data has to be supervised. Asked whether the same email, phone number, and ID number would be flagged as duplicates on re-post, BCL said no.

This supersedes the 2026-10-13 note that resubmission had to wait for a BCL update endpoint. No such endpoint will exist; re-posting through `addindividualidentity_bcl` is BCL's intended workflow.

User decisions:

- A separate `updateKyc` mutation for `REJECTED` customers. All fields are optional and merged with the saved form; `createKyc` stays first-submission only.
- Saved images stay in private storage and are reused unless replaced; the app is only told which images are on file.
- The saved form is deleted after approval.

Implemented:

- A `kycSubmissions` collection with one document per user, holding the text fields and relations plus Upload references for the seven images. Images are stored in the private `kyc/documents` folder exactly as sent. A storage read helper (`readFileFromStorage`) was added.
- `submitKycToBcl` is shared by `createKyc` and `updateKyc`: the claim, the post, saving the reference, restore on a BCL 400 (including the rejection reason), and reconciliation when the outcome is uncertain.
- `User.kycSubmission` is returned to its owner only.

## Grow Wealth cash movement statement

The request is `fetchdata` with `RequestID: "LinkedPortfolioCMS"`, and `xmlDetail` takes `IdentityID`, `PortfolioID`, `FromDate`, and `ToDate` in `DD MMM YYYY`. Each response row has `ValueDate`, `EntryType` (`Debit`, `Credit`, or empty for the Opening and Closing Balance rows), `Description`, `Amount`, and `Balance`. Amounts are strings with thousands separators, such as "17,636.60".

The user chose a structured result: `openingBalance` and `closingBalance`, plus entries with parsed numbers, a `DEBIT`/`CREDIT` type, and UTC-midnight dates. Implemented as `getMyGrowWealthCashMovementStatement(filters: { portfolioId, fromDate, toDate })`, scoped to the customer's linked portfolios and returning null otherwise.

Correction (same day): the user rejected the first implementation as messy and off-architecture, with too many try/catch blocks, and asked for Mongo transactions because atomicity matters. It was restructured to the repository pattern: one exported function per service file, pure helpers in `services/users/helpers`, and `Model.db.startSession()` with `withTransaction`. Images moved from Spaces into the `kycSubmissions` document, so the supervision reference and the saved form commit in one transaction, and approval deletes the form in the same transaction as the approval. The Spaces read helper, the KYC storage directory, and the best-effort cleanup were removed. The user's own edit removed the post-acceptance reconciliation try/catch in `submitKycToBcl`; a failed save after BCL acceptance now surfaces as an error with the claim kept.

For the cash movement statement, the user objected that their full six-row sample had not been tested. The output for that sample was correct, but the test fixture had dropped two rows. The test now uses the exact sample. Balance rows are identified by position (the first and last rows without an entry type) rather than by their English wording, and single-digit days are accepted.
