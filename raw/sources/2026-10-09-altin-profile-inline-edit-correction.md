# Altin Partner Profile Inline Edit Correction — 2026-10-09

Sanitized record of direct user corrections to the Altin Partner Mobile Profile edit flow in a Claude Code session. No credentials, tokens, or personal identifiers are included.

## The route was too long

- After the previous correction, changing the phone number meant Profile → header Edit → Edit profile screen → tap the phone row → a separate Change phone number screen.
- The user called it bad UI and asked why they had to go through that long route instead of doing it on the profile screen.
- Fix: the Profile screen edits in place. The header pencil switches the same screen to Edit profile; Back cancels and discards the draft. Photo, phone number, and alternate phone are fields. A changed number sends an SMS code and the code field appears inline under it, with Change number and Resend code; verification of an unverified number uses the same inline step. The separate edit, change-number, and verification routes were deleted.

## The form hook ignored the repo's own structure

- The user also said the `useFormik` code was messy and did not follow their structure and architecture.
- The agent then looked at SERLP for form structure. The user corrected: this codebase already has Formik hooks written the way they want; there is no need to go to SERLP.
- The user's committed hooks (for example `useEditOutletForm`, `useEditCourierGroupForm`, `useCreateCourierGroupForm`, `useReportOrderIssueForm`) share one shape: a private module-level `validationSchema`; a parameterless `use…Form()` that owns its query resource, `useScreenRefresh`, and named mutation hooks; typed `useFormik` with `validateOnMount` and a guarded async `onSubmit` that calls the named mutation; and a `{ form, loading, resource, ... }` return. Screens bind Formik fields directly.
- The rejected hook had added seeding refs, a manually computed "changed" flag, picker state, upload-and-retry logic inside `onSubmit`, and navigation helpers.
- The rewritten hook follows the committed shape. The photo upload became a named action hook with Toast errors, like the mutation hooks.
