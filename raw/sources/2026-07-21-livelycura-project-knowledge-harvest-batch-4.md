# LivelyCura Project Knowledge Harvest — Batch 4 Evidence Manifest

Date: 2026-07-21

## Scope

- Family: LivelyCura.
- Live repository root: `/Users/acazumah/Documents/LivelyCura`.
- Affected repositories: `livelycura-backend`, `livelycura-pharmacy-portal`, `livelycura-courier-mobile`, and `livelycura-check-city-app`.
- Repository writes: none.
- Codex sessions processed: exactly 8, as fixed by the batch-3 checkpoint.
- Transcript handling: only metadata, sanitized user corrections, durable claims, rejected approaches, and reported verification outcomes are preserved. Full transcripts, images, binary artifacts, tool chatter, and private identifiers are excluded.
- Secret-bearing files and values were not inspected or copied. Environment/auth files, credentials, tokens, certificates, private keys, connection strings, generated GraphQL output, dependencies, build output, and caches were excluded.

## Processed Codex Sessions

| Date | Session ID | Working directory | Indexed title |
| --- | --- | --- | --- |
| 2026-05-13 | `019e239f-dd9e-73a3-b75d-e37d13bd22ff` | `.../livelycura-backend` | Research lab feature approach |
| 2026-05-06 | `019dfdd7-8f8d-7901-a34a-09301f861b50` | `.../livelycura-courier-mobile` | Fix Android OTP input |
| 2026-05-06 | `019dfdba-34ef-7692-8e90-4259a7d2f55f` | `.../livelycura-courier-mobile` | Fix App Store auth rejection |
| 2026-05-06 | `019dfd88-68ed-7420-b3dd-f3f150e1c73f` | `/Users/acazumah/Documents/LivelyCura` | Fix App Store review issues |
| 2026-05-01 | `019de5bd-34c3-72d0-817d-15a59e470c01` | `.../livelycura-check-city-app` | Add BackgroundDecoration |
| 2026-05-01 | `019de35a-9685-7462-bb90-739847980b24` | `.../livelycura-pharmacy-portal` | Fix delivery task type bug |
| 2026-05-01 | `019de13d-bcbd-7c50-bba1-6b62fd64e064` | `.../livelycura-courier-mobile` | Create Play Store feature graphic |
| 2026-04-29 | `019dda04-807b-70a3-96b5-ff1cfae7eaa5` | `.../livelycura-check-city-app` | Fix bottom tab label overflow |

## Minimal Sanitized Conversation Evidence

- `019e239f…`: the initial lab research compared sale-first, request-first, order-bridge, and hybrid models. The user then corrected the recommendation: LivelyCura must reuse its existing POS, inventory, manufacturing, sale, invoice, and payment flows rather than create a lab-specific selling path. A later exploration proposed a generic JIT/backflush BOM mode that would sell a lab test without finished inventory and consume components when testing starts. That proposal was research, not an implementation outcome.
- `019dfdd7…`: the reported Android issue evolved from apparent OTP text bleed to the login button’s platform rendering. The user rejected duplicate phone/OTP validation logic and retained the original Formik behavior while keeping a native `TouchableOpacity` presentation path. The same session removed heavy Android elevation from the station, task-list, performance, today, and single-task card surfaces to match iOS; corrected task navigation to one `taskId` route parameter; and explicitly rejected an `id`/`taskId` fallback inside the task screen.
- `019dfdba…`: an attempted App Review-facing login-copy change was explicitly scrapped after the user clarified that login was not the rejection issue and the OTP fix already existed. This session therefore supplies negative evidence: do not promote its temporary copy change as the surviving implementation.
- `019dfd88…`: the App Store plan established that the public product is `SERLP Dispatch`, available to eligible couriers rather than a private employee-only app. Courier operations require profile approval for safety/compliance, but account discovery and sign-up are public. The plan required courier-specific camera/photo/location purpose strings, iPad support, a native controlled four-digit OTP input, and a real reviewer-accessible seeded courier account without storing its credentials in project knowledge. A later correction kept the backend push payload unchanged and mapped its existing nested task ID to the app’s canonical `taskId` route parameter.
- `019de5bd…`: `BackgroundDecoration` was extended across CheckCity profile, branch selection, login/address modals, and order/checkout surfaces. Modal decoration stays behind foreground content and theme-derived text remains readable. Android bottom sheets must draw into system-bar space to avoid a bottom gap. The user also corrected shared category ownership so callers pass contextual layout styles, and corrected pull-to-refresh so lists remain full-screen beneath floating headers while safe-area-aware refresh controls stay visible on iOS and Android.
- `019de35a…`: standalone delivery creation must omit multi-stop metadata. A root task with non-empty children is multi-pickup; a task with a parent is a pickup stop; an empty child array alone does not make a root task multi-pickup. Table/detail classification shares one helper and types live in the courier interface folder. Tests use absolute imports, and the create mutation refetches the correctly cased operation.
- `019de13d…`: the repository name `livelycura-courier-mobile` is internal; public artwork and store copy use `SERLP Dispatch`. The Play featured graphic is `1024x500` and uses the courier identity rather than a generic box card. The same session implemented production-only, dynamically loaded store update checks, courier-specific iOS permission strings, and App Store-compatible phone/tablet artwork. Historical screenshot outputs were stored outside the repository; no binaries were copied into this manifest.
- `019dda04…`: active bottom tabs receive more flex space while inactive tabs shrink, but the spread must remain modest so a far-end active tab does not create a large visual gap. The corrected values were active `1.45` and inactive `0.85`, with single-line overflow guards and preserved accessibility state.

## Current-Code Verification

### LivelyCura Backend

- Current sale creation formats ordinary sale items, creates one test request per qualifying lab-linked sale item inside the same transaction, creates normal inventory movements, posts COGS, and creates the invoice. No `JIT_BOM`, fulfillment-mode, backflush, or lab-specific consumption implementation exists.
- Courier task push payloads still send the task identifier in the existing nested details object. The batch’s temporary backend compatibility fields were correctly reverted.

### LivelyCura Pharmacy Portal

- Standalone delivery payloads omit `childTaskIds` and `stopOrder`; multi-pickup parent payloads send an empty child array and `stopOrder: 0`.
- `getDeliveryTaskType` returns pickup-stop when `parentTaskId` exists, multi-pickup only when child IDs or child records are non-empty, and standalone otherwise. Table and detail surfaces use the shared helper.
- Delivery-task type contracts live under `src/courier/interfaces`; focused tests use absolute `src/...` imports. The create mutation refetches `GetDeliveryTasks`.

### LivelyCura Courier Mobile / SERLP Dispatch

- `app.json` and variant config use `SERLP Dispatch` publicly; the repository/package name remains internal. iPad support remains enabled.
- Current iOS photo, camera, and location purpose strings describe concrete courier identity, vehicle, proof-of-delivery, nearby-task, and route-progress uses.
- The login screen currently uses a native controlled numeric `TextInput` for the four-digit OTP. A reusable `CustomOtpInput` file remains in the repository but is not used by the current auth screen, so the historical component integration is not asserted as current.
- The current login action is a styled native `TouchableOpacity`. Current source also contains a public-sign-up hint, but the processed copy-change session itself ended in a revert; current source establishes presence, not that session’s rationale.
- Notification handling reads the backend’s existing nested task ID, maps it to `{ taskId }`, and stores/navigates with that one route contract. In-app task cards also pass `taskId`; `TaskScreen` reads only `taskId`, and its query skips when missing.
- Main station, tasks, performance, today, and single-task card surfaces use zero Android elevation. Other distinct controls may retain elevation and are not covered by the correction.
- Store-update checks are production/web guarded, dynamically import the optional native module, use immediate Android updates only when allowed, prompt on iOS, and swallow failures so startup is not blocked.
- A Play featured-graphic PNG exists under `assets`; binary content/dimensions were excluded from this harvest. Historical phone/iPad screenshot sets remain external deliverables.

### LivelyCura CheckCity App

- `BackgroundDecoration` is present on profile, branch, login/address modals, checkout/order, menu/search, cart, categories, and related detail screens. Modal content is layered above the decoration.
- Login and address bottom-sheet modals use screen dimensions plus translucent Android status/navigation bars and theme-aware bottom insets.
- Menu, Search, and Orders keep their lists under floating headers, disable automatic content inset adjustment, and use explicit safe-area-aware content insets/offsets and themed refresh controls. Orders keeps one list mounted for loading, empty, error, and data states.
- `CategoryFilter` accepts caller style; Menu supplies bottom spacing while Search explicitly supplies none.
- The shared menu-description fallback remains present. The historical six-item grid loader does not: current `MenuLoader` is a three-item horizontal loader, so the older loader layout is not promoted.
- Current bottom-tab styles preserve the corrected `1.45`/`0.85` active/inactive flex ratio, `minWidth: 0`, single-line label overflow handling, and selected accessibility state.

## Reported Historical Verification

- The lab research session was planning-only and performed no repository mutations.
- Pharmacy Portal reported focused Vitest runs, type checking, and targeted lint passing after the delivery-type fixes.
- Courier sessions reported formatting checks on touched files, backend builds where the backend was inspected, and commits/pushes for selected historical mobile changes. Mobile type checking still had unrelated baseline failures at that time.
- CheckCity sessions reported formatting and diff checks; full type checking retained unrelated historical failures.
- Store artwork sessions reported exact platform sizes, but this harvest did not inspect or reproduce binary artifacts.
- These are transcript-reported May 2026 outcomes. The harvest itself performed read-only source inspection and did not rerun repository tests, builds, apps, or store workflows.

## Contradictions And Uncertainty

- The JIT/backflush lab proposal is the latest idea inside `019e239f…`, but later explicit implementation sessions and current code use the ordinary sale/inventory/COGS path with one test request per sale item. The proposal remains historical research, not desired current behavior.
- The App Store auth-copy session ended with an explicit revert. Current auth later contains public-sign-up text, so the public-distribution fact is supported by a separate explicit plan and current code, not by the reverted change.
- The reusable courier `CustomOtpInput` was historically integrated, but current `Auth.tsx` uses a different native controlled input and leaves that component unused.
- A historical store-update configuration referenced an older store identifier. Current config differs and is authoritative; raw identifiers are intentionally omitted from this manifest.
- Historical CheckCity loader corrections do not match current `MenuLoader`. Current source outranks the earlier six-item grid instruction.
- Historical screenshot and featured-graphic outputs were partly external and partly binary. Only public naming, current asset presence, and durable export conventions are asserted.

## Follow-Up Boundary

The next and final LivelyCura coverage batch should triage exactly these five remaining working-directory sessions for unique project evidence:

1. `019ec706-5050-7182-9435-08c5498de8f2` — Create personalized pet.
2. `019f7cca-d23b-7122-9d0d-f1490f7c22d1` — Unindexed session from 2026-07-19.
3. `019f76eb-d661-7ef2-8f4d-4f854ebc9f1a` — Unindexed session from 2026-07-18.
4. `019f6de5-6dff-7712-a264-c0edb24a595c` — Unindexed session from 2026-07-17.
5. `019f5e0d-5fe9-7de3-9c3e-f873b39fcd17` — Unindexed session from 2026-07-14.

That batch should classify each as unique project evidence, duplicate/child/evaluation context, or unrelated work. Move to CompFlow only after this five-session triage makes the LivelyCura completion boundary explicit.
