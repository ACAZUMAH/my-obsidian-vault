# Altin Partner Profile and Support — 2026-10-08

Sanitized record of a Claude Code session on Altin Partner Mobile (`feature/apps`). It records the user's request, decision, the contracts taken from the web app and API, and the verified result. No credentials, tokens, environment values, or personal identifiers are included.

## User request

- The user had added Profile and Support rows to the More screen and asked to build both: check `altin-web-apps`, follow the usual conventions, and add permissions where needed.
- Asked how to pick profile photos, the user chose "Add expo-image-picker (Recommended)" over the installed document picker, accepting a native rebuild.

## Contracts found

- Web partner Support routes are deliberately ungated: filing a ticket needs bare membership and every member sees at least their own tickets; `VIEW_SUPPORT_TICKETS` and `MANAGE_SUPPORT_TICKETS` only widen what the server returns and which controls appear. Ticket triage (status, assignment, priority, close/resolve/reopen, watchers) is super-admin only and lives in the admin app.
- The `supportTickets` list is not scoped to the active organization, and the API rejects the four staff-only filters for members.
- Web partner Profile has no permissions; its save is a stub, Change Password is hidden, and the schema the mobile app uses has no password mutation. The API supports `user.updateProfile` (with a required `profilePictureId`), phone change by OTP, and phone verification by OTP. No web client calls `updateProfile`.
- Files upload over REST to `{base}/blobs` with multipart field `blob`, a Bearer token, and success only on status 200. The mobile REST base ends in `/v1` while the web posts to the bare host; the correct path is unverified.
- The System query reads `currentUser` without ids. A second query on `currentUser` that writes the cache replaces that field and can unmount navigation; even matching ids leaves the unnormalized envelope replaceable. The profile query therefore uses `no-cache`.

## Implemented result

- Support (`src/support`): ticket list with search, status/category filters, sort, cursor pagination, and an explicit scope label; Raise a ticket with attachments and order links (order linking requires `VIEW_ORDERS`); ticket details with reply attachments, order-reference summaries, and linking/removing references under the existing reply rules. No triage.
- Profile (`src/more/profile`): profile view, photo and alternate-phone edit, phone-number change, and phone verification when unverified. No password change.
- The More Settings section is visible to every member; API keys and Webhooks keep their own permission gates. Search gained Profile and Support entries and a Raise a ticket action.
- Shared pieces: `src/helpers/uploadBlob.ts` replaces two diverging upload copies; `ToastHost` lets a native modal that runs mutations show toasts, since modals cover the root host.
- Dynamic imports of a native module missing from the installed binary report a fatal error instead of rejecting, so the image picker and clipboard now check `requireOptionalNativeModule` first. The current native build (per `ios/Podfile.lock`) includes neither `expo-clipboard` nor `expo-image-picker`; the user must run `yarn ios`.
- Verification: scouting, two build-review-fix workflows, and a final two-lens review; all actionable findings were fixed except one rejected (it conflicted with the established organization-guard pattern in mutation hooks). Type-check and formatting pass. No upload, ticket, profile, or OTP mutation was run against production. The user's Metro stopped serving bundles after the package install, so on-device checks wait for the rebuild.
