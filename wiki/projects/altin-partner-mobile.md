---
type: project
status: active
created: 2026-07-21
updated: 2026-10-20
tags: [project, ceqa, altin, expo, react-native, partner-operations]
sources:
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-1.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-3.md
  - ../sources/hermes-persistent-memory-import.md
  - ../sources/ceqa-altin-hermes-conversation-harvest-supplement-1.md
  - ../sources/altin-mistitled-casual-greeting-continuations.md
  - ../sources/altin-orders-mobile-web-reference.md
  - ../sources/altin-outlets-mobile.md
  - ../sources/altin-mobile-brand-system.md
  - ../sources/altin-search-browse-grouping.md
  - ../sources/altin-theme-navigation-runtime-corrections.md
  - ../sources/altin-permission-gating.md
  - ../sources/altin-module-builds-and-scope-corrections.md
  - ../sources/altin-profile-support.md
  - ../sources/altin-profile-support-ui-corrections.md
  - ../sources/altin-profile-inline-edit-correction.md
  - ../sources/altin-formik-onsubmit-correction.md
  - ../sources/altin-support-chat-first-redo.md
  - ../sources/altin-profile-separate-editors-correction.md
  - ../sources/altin-reports-mobile.md
confidence: high
---

# Altin Partner Mobile

## Summary

Altin Partner Mobile is an Expo application scaffold for authenticated partner operations across orders, outlets, fleet, team, accounting, and billing. Orders has an organization-aware overview, Delivery Orders and Tips lists, record details, and API-integrated creation and issue reporting. Outlets now has overview/list/details, create/edit, and CSV bulk-import API integration, with live testing reserved to the user. Fleet has a first pass: overview, six section lists, details, and permission-gated courier-group create/edit, with native/live verification pending. Team (members, invite, change role, remove, roles with create/edit), Accounting (Today card, transactions, wallet statement), and Billing (current billing, invoices, settlements) are built, as are API keys and Webhooks on More, and Notifications with support-ticket details and reply. Home analytics, Search, and organization selection are implemented. Profile (view and in-place edit of photo, phone number with inline OTP change or verification, and alternate phone) and Support (ticket list, Raise a ticket with attachments and order links, ticket details) open from More. The Reports tab (built 2026-10-18; the unused `ComingSoon` component was deleted on 2026-10-20) lists the permitted web reports, six SHIPPER then four FLEET, as one mobile card per record, with Print, PDF, and CSV exports that match the web partner app's. Push notifications are deferred. Guarded screens use `withPermission`; Profile and Support are deliberately ungated, as on the web.

## Purpose

Provide mobile partners a single Altin-authenticated entry point to operational modules and their future concrete workflows.

## Stack

- Yarn, Expo 54, React Native 0.81, React 19, and TypeScript 5.9.
- React Navigation 7; no Expo Router.
- Apollo Client 3 and GraphQL.
- Redux Toolkit, Redux Persist, and AsyncStorage.
- Styled Components, React Native Elements, safe-area context, gesture handler, Reanimated/worklets, and Toast.
- Expo Auth Session/Web Browser with OAuth/OIDC Authorization Code and PKCE.

## Architecture

- `App.tsx` composes Redux, theme, Apollo, gesture handling, and navigation.
- The root stack selects Login or authenticated routes from persisted authentication state.
- The authenticated bottom tabs are Home, Search, Reports, and More. The center Apps action opens a root-stack directory with a header Back button and preserves the selected tab underneath. Notifications is a root-stack screen opened from the Home header bell. See [[../sources/altin-theme-navigation-runtime-corrections|the Reports tab correction]].
- The Apps directory links to Orders, Outlets, Fleet, Team, Accounting, and Billing stacks.
- Apollo reads the current Redux access token, attaches the bearer header, and sends operations to the configured API. Verify live client configuration before assuming token refresh or additional headers.
- Access and refresh tokens, expiry, user, and settings are currently persisted through Redux Persist/AsyncStorage.

## Folder Ownership

- Outlets owns the overview plus sibling `outletList`, `outletDetail`, `outletCreate`, `outletEdit`, and `outletBulkImport`; The user explicitly rejected the `outletForm` layer; create/edit screens and hooks own their forms using shared primitive controls. The exact 2026-09-12 correction requires direct Apollo operation hooks across Orders, Outlets and Fleet; screen hooks own refresh/pagination interactions.

- `src/navigation`: stack, tabs, route registration, navigation types, and safe-area/tab presentation.
- `src/login`: OAuth flow, token refresh/revocation, claims mapping, login UI, and auth contracts.
- `src/apollo`: authenticated GraphQL client/provider.
- `src/redux`: persisted auth/settings state and typed store hooks.
- `src/apps`: active module-directory metadata plus tracked legacy generic shell files that currently have no route or barrel consumers.
- `src/orders`, `src/outlets`, `src/fleet`, `src/team`, `src/accounting`, `src/billing`: module-owned roots, drawers, constants/styles, and feature screens.
- `src/more/apikeys`, `src/more/webhooks`, and `src/more/profile` own the More-tab screens; `src/notifications` owns the inbox; `src/support` owns `ticketList`, `ticketCreate`, and `ticketDetail`. File uploads use the shared `src/helpers/uploadBlob.ts`, and `src/components/toastHost` renders toasts at the root and inside mutation-running modals.
- `src/reports` owns the Reports tab, its catalog, and the shared report layout, filters, builders and export service; each report is a sibling feature folder with its own operation hook, screen hook, builder and screen. See [[../sources/altin-reports-mobile|the Reports record]].
- Shared hooks in `src/hooks` include `usePermissions`, `useSheetTransition` (bottom-sheet motion), `useCopyText` (lazy `expo-clipboard`), and `useUnreadNotificationCount`. Combined permission rules live in `src/constants/permissions.ts`.
- Orders lists belong to `deliveryOrders` and `tips`; read-only detail features belong to sibling `deliveryOrderDetail` and `tipDetail` folders. Do not put the detail screen and list screen in the same feature folder.
- `src/components`: reusable presentation primitives such as Conditional, skeletons, module headers, drawers, sections, entity lists, and filters.
- Shared list primitives own mechanics and presentation; module feature screens own future query/data, filter state and controls, entity types, row rendering, and navigation.

## Commands

- `yarn start`: Expo development server.
- `yarn android`: native Android run.
- `yarn ios`: native iOS run.
- `yarn web`: Expo web mode.
- `yarn type-check`: TypeScript without emission.
- `yarn format` / `yarn format:check`: Prettier.
- `yarn generate`: GraphQL schema type generation.
- `yarn test:orders`, `yarn test:outlets`, and `yarn test:fleet` remain in `package.json`, but the `tests/` directory they run was deleted in commit `e4c14fa`. See [[../sources/altin-module-builds-and-scope-corrections|the module builds record]].
- No dedicated lint or production-build script is currently defined.

## Runtime/Deployment

- `expo/AppEntry.js` is the runtime entry point.
- The running app uses the production API, explicitly confirmed by the user on 2026-09-10. Development mode does not imply a staging backend; keep verification read-only and use local tests for risky or artificial scenarios.
- App variants change display name and native identifier for local/development, preview, and production-like builds.
- Public API/auth/application identifiers are configuration inputs; no secret values belong in the repository or vault.
- No EAS configuration, CI workflow, or deployment pipeline was found.

## Durable Conventions

- Mutation hooks own business/API validation and transport error toasts, including returned field messages. Remove assertion/ApiError/unwrapping layers and rethrows; forms keep client Yup validation and drafts, and advance only on successful results. Current mobile hooks expose named actions and loading. Use Apollo loading and `form.isValid` instead of saving refs; Formik never submits requests (superseded 2026-10-09, see [[../sources/altin-formik-onsubmit-correction|the Formik onSubmit correction]]). See [[../sources/altin-orders-mobile-web-reference|the latest mutation error correction]].

- Do not recreate the rejected outlet/group form-feature layers or extra edit-form wrappers. Bind fields in the owning screens, keep straightforward field rules in the form hooks and prefer built-in numeric Yup validators. The supplied multi-schema/promise-controller code is rejected evidence. Preserve the user’s `src/orders/createOrder` rename. See [[../sources/altin-orders-mobile-web-reference|the latest form-layer correction]].

- Cross-project consistency means matching the actual form structure, not just installing Formik/Yup: named create/edit form hooks with private Yup schemas and typed Formik (since 2026-10-09 the screens, not `onSubmit`, call the mutations; see [[../sources/altin-formik-onsubmit-correction|the Formik onSubmit correction]]); shared components render passed forms with direct field bindings. The initial library-only migration was explicitly rejected. Preserve necessary workflow guards without adding an alternate callback/promise controller. See [[../sources/altin-orders-mobile-web-reference|the form-structure follow-up]].

- Forms use Formik and Yup: typed useFormik hooks with validationSchema, validateOnMount and an empty onSubmit, following the pharmacy portal and Check City (see [[../sources/altin-formik-onsubmit-correction|the Formik onSubmit correction]]). Return the real form to shared UI; Formik owns editable values, touched/errors, dirty/valid/submitting state. Keep schemas feature-owned and reusable for create/edit/import validation. Do not substitute custom draft/error state or duplicate field rules; preserve scope, side-effect and navigation guards. See [[../sources/altin-orders-mobile-web-reference|the Formik/Yup correction]].

- Exact Apollo architecture: private complete gql document in each operation hook; direct generated-type useQuery; context/filters, memoized named data/pageInfo, display flags, then `...result`. Mutations use direct useMutation, relevant refetchQueries, a generated-input named action, try/catch success/error feedback, returned successful server data and loading; API errors are consumed by Toast in the hook. Compose independent reads in screen hooks; no aliased count/list overview bundles or imperative resource wrappers. This applies to Orders, Outlets and Fleet. Use the user's supplied Customers/Menu Products and Add Customer/Add Employee examples and consult reference projects/Obsidian before implementation. Web source supplies product/API contracts, not mobile architecture. See [[../sources/altin-orders-mobile-web-reference|the exact hook correction]].

- All text inputs include useful placeholder examples or expected formats, including optional fields and cleared edit fields. Preserve labels; never submit placeholder copy as a default. Shared FormField requires explicit placeholder text. See [[../sources/altin-outlets-mobile|the input placeholder correction]].

- SERLP create/edit references include visible form layouts and inputs. Reuse shared bordered fields, compact uppercase labels, field-shaped selectors and form panels with Altin tokens; keyboard avoidance wraps Screen and save actions use its footer. Changing mutation hooks alone does not satisfy a form UI request. See [[../sources/altin-outlets-mobile|the form/input correction]].

- Bulk import is an explicitly requested Outlets action and feature. Keep it in both overview and drawer, require both create/update permissions, and preserve the 500-row atomic CSV contract. See [[../sources/altin-outlets-mobile|Outlets bulk import]].

- Module overviews omit redundant organization headings. A feature-owned action definition supplies both Quick actions and drawer actions; View all uses the shared Orders treatment. The explicit correction adds Create order and order-linked Report an issue, superseding their earlier deferral. See [[../sources/altin-orders-mobile-web-reference|the module-action correction]].
- Inspect the cloned web project before asking the user to explain its product behavior. Use Apollo useMutation directly in feature mutation hooks, with named actions and shared form controls. Forms own client validation and submission state; the mutation hook owns API error toasts, as the inspected SERLP mutation does. The user explicitly requested deletion of useMutationResource; do not replace it with another generic wrapper. See [[../sources/altin-outlets-mobile|the direct mutation correction]].

- All status badges use the shared full round radius. Outlets includes overview/list/details and create/edit, with VIEW_ALL_OUTLETS plus separate CREATE_OUTLETS/UPDATE_OUTLETS permissions or ADMIN for both organization types. See [[../sources/altin-outlets-mobile|the Outlets scope]].
- For the Outlets implementation, use offline checks and mocks only: the user will change the API and test live. This explicitly excludes production API testing for this pass.

- Keep background focus reloads separate from explicit pull-to-refresh state; reset the latter on completion, failure, blur, and scope changes. Custom row titles own their text metrics rather than inheriting a smaller plain-title line box. See [[../sources/altin-orders-mobile-web-reference|the refresh and tip-text correction]].

- Use React Navigation under `src/navigation`; do not introduce Expo Router.
- The repository's `docs/app-theme-guide.md` is the theme authority for palette, light/dark semantic colors, typography, spacing, and radii, implemented in `src/theme/constants.ts`; the user's later tuning in that file wins. Typography uses system fonts. The brand-book palette and Plus Jakarta Sans / IBM Plex fonts were rejected as the app theme; never reintroduce them or the old look. Keep the supplied [[../sources/altin-mobile-brand-system|brand-book]] lockups and 1024-pixel app icons; do not retype or recolor the mark. See [[../sources/altin-theme-navigation-runtime-corrections|the theme correction]].
- Primary-colored icons in icon wells use the `brandIconBackground*` tokens: primary-red glyph on a subtle red well in both modes, deep red in dark mode, never white glyphs or neutral wells. Notification, back, and other neutral controls keep `neutralIcon*` tokens. Card and card-skeleton borders are 0.3 wide; input, selection, and navigation outlines keep their widths. Change only the visual detail requested.
- OAuth testing requires the development build; Expo Go's redirect is not registered. Never leave a background Metro server on port 8081 after verification.
- Treat SERLP Mobile as an architecture/configuration reference only. Preserve Altin typography, spacing, radii, shadows, modules, and product identity rather than copying SERLP visual tokens.
- Search owns its styles and row presentation while reading Apps directory metadata. With an empty query, show one grouped Browse section for available apps, followed by Actions and Suggestions. After typing starts, preserve the existing browse/search sections and feature previews; keep the Apps directory’s own grouping separate. See [[../sources/altin-search-browse-grouping|the direct Search corrections]].
- Keep five visible bottom-bar controls: Home, Search, raised-center Apps, Reports, and More. The user intentionally replaced Notifications with Reports; never restore it as a tab. Apps pushes the directory on the root stack instead of selecting a tab; Back returns to the previous tab. Derive the four real tabs and active state from React Navigation route state, with one typed configuration for all controls.
- Derive React Native Elements and styled-components themes from one Redux-controlled light/dark state.
- Keep safe-area, status-bar, and home-indicator backgrounds consistent.
- Feature folders own logic through hooks/services and keep screens thin.
- Reuse Conditional for conditional JSX and the shared skeleton loader system. Keep optional expressions safe before constructing JSX children.
- Keep component rendering, interfaces, helpers, constants, hooks, and styles in their owned files. Each full GraphQL operation lives in one hook, without an imported fragment folder.
- Declare function components with `React.FC<Props>` or `React.FC` for no-props components. Import their props interfaces from the owning interface file instead of annotating the function parameter; preserve typed filter values across shared string-valued controls. See [[../sources/altin-orders-mobile-web-reference|the direct Orders component-typing correction]].
- Preserve separate compact delivery order cards with a few scan fields; tap opens the full details. The later compact-card request supersedes the prior two-column pickup/drop-off row. Do not replace independent cards with a combined divider surface.
- Read `/Users/acazumah/Documents/LivelyCura/serlp-mobile` for actual shared Screen/list-row composition. Reuse shared screen, row/skeleton, state, detail-summary/section, and detail-field presentation under `src/components`; features keep operations, filters, navigation, and domain-specific presentation. Orders shares payment presentation between Order and Tip details.
- List headers have back/search/filter controls without a drawer button. All detail screens also omit drawers; Order details place Report an issue on the right of the header. Preserve the user's removal of the Overview drawer entry.
- Use the running app and simulator for native verification before considering another runtime. Do not launch extra QA emulators or Expo servers while the user's app is already available.
- Change only what the user asked for, and treat an unanswered proposal as declined. When the user says to update or do something, finish its whole reasonable scope instead of doing part and asking about the rest. See [[../sources/altin-module-builds-and-scope-corrections|the module builds record]].
- Profile and Support follow the web: no route permission, More shows both to every member, order linking needs `VIEW_ORDERS`, and ticket triage and in-app password change are not built. The profile's `currentUser` query stays `no-cache` and never refetches `System`. Photos use `expo-image-picker`, chosen by the user, which needs a native rebuild. See [[../sources/altin-profile-support|the Profile and Support record]].
- Profile views and edits on one screen: the header pencil switches it into edit mode, and a phone change or verification shows its SMS code field inline. There are no separate edit or phone-number screens; the user rejected that route as too long. See [[../sources/altin-profile-inline-edit-correction|the inline edit correction]].
- Formik `onSubmit` never calls the backend: form hooks hold only state (`onSubmit: () => {}`; edit forms take the record with memoized initial values and `enableReinitialize`), and screens or `use…Screen` hooks own `handleSubmit`. Follow the pharmacy portal, admin portal, and Check City, not SERLP. All 17 form hooks were converted on 2026-10-09. See [[../sources/altin-formik-onsubmit-correction|the Formik onSubmit correction]].
- Support was redone chat-first on 2026-10-09, following Check City. The thread is the screen; one composer starts and continues conversations; the subject is derived from the selected category (user decision); and Report an issue opens an order's existing live conversation instead of raising another (user decision). See [[../sources/altin-support-chat-first-redo|the Support redo]].
- Profile's photo, phone number and alternate phone each change on their own, in place, like the admin portal's section editors. They use different APIs, so they are never one form or one Save. Phone inputs take local numbers converted with `awesome-phonenumber` (`src/helpers/phoneNumbers.ts`). See [[../sources/altin-profile-separate-editors-correction|the separate editors correction]].
- The header Edit covers the photo, alternate phone, phone-number change, and verification. Name, email, city, and about are not editable: no web app saves them (partner, admin, and ERP saves are stubs) and `updateProfile` accepts only the photo and alternate phone. See [[../sources/altin-profile-support-ui-corrections|the UI corrections]].
- Never report UI done without viewing every new or changed screen on the simulator. Support's reply bar follows SERLP's composer, and Support uses dashed add tiles instead of secondary buttons on cards. See [[../sources/altin-profile-support-ui-corrections|the UI corrections]].
- Check `requireOptionalNativeModule` before dynamically importing a native package: on a binary built before the package was added, the import is a fatal error, not a rejected promise. See [[../sources/altin-profile-support|the Profile and Support record]].
- Every object a screen query shares with the System query must select `id`; a missing `user.id` replaced the normalized member, refetched System, and remounted navigation back to Home. See [[../sources/altin-module-builds-and-scope-corrections|the module builds record]].
- Bottom sheets (filters and detail actions) slide up on open and back down on close through `useSheetTransition`, skipping motion under Reduce Motion. The backdrop is a separate Pressable behind the panel so scrolling and switches work. See [[../sources/altin-module-builds-and-scope-corrections|the module builds record]].
- API-key and webhook secrets are shown once from local screen state, fetched without caching, and copied with `expo-clipboard`, which needs a native rebuild. See [[../sources/altin-module-builds-and-scope-corrections|the module builds record]].
- Notifications open from the Home bell with an unread badge; tapping marks the notification read and opens its support ticket. Ticket reply is limited to the reporter, ADMIN, or members with both view and manage support-ticket permissions while the ticket is open; linked orders open only in the same organization with order access. See [[../sources/altin-module-builds-and-scope-corrections|the module builds record]].
- The Orders status history is a collapsible accordion with the latest status and update count in its header, checked markers for passed statuses, and no actor label. Arrival statuses use the pending tone; the selected light-mode filter chip uses the subtle brand background. See [[../sources/altin-module-builds-and-scope-corrections|the module builds record]].
- Reread current files before every edit and preserve user changes made since previous assistant updates, including removals. An earlier plan never authorizes restoring a later removed element.
- Reports follow the web Reports page order and permissions: six SHIPPER reports, then four FLEET reports. Each has a named `permissionRules` entry (permission plus organization type) used by the catalog, `withPermission`, and the query `skip`. Revenue & commission stays, with a caveat that its query is deprecated. See [[../sources/altin-reports-mobile|the Reports record]].
- The report screen is mobile-native: one card per record (period, courier, or leaderboard) holds all its figures and status breakdowns. No horizontal-scrolling tables, no separate status tables, and no "Summary" label on the totals card. Each report's loading skeleton matches the shape of its own cards. On screen, missing values show "—", never 0, and rates come from counts. See [[../sources/altin-reports-mobile|the Reports record]].
- Print, PDF, and CSV are the web partner app's exports, not a mobile design: the web's `PrintAdminReportModal` page and `exportToCSV` rows, columns, formatting, and file names, with Print printing the generated PDF. Order funnel, Payment attempts, and Assignment efficiency use A4 landscape, the rest portrait, as on the web, and Print passes the matching orientation to the print sheet. The only differences are the documented deliberate ones: backend rate fractions scaled to percentages, a UTF-8 BOM written as bytes, doubled embedded quotes, CSV headings from all rows, plain-text courier lines that keep the web `CourierCell` wording ("Pending Verification", "No ratings"), and a 297 × 210 mm sheet for landscape reports (`print.landscape`). One builder per report returns `{ preview, print, csv }` from the same data. See [[../sources/altin-reports-mobile|the Reports record]].
- Report exports scale backend rate fractions to percentages (user decision, 2026-10-18). The backend sends rates such as `acceptanceRate`, `successRate`, and `commissionRate` as fractions (0.5275 = 52.75%). Print, PDF, and CSV for Assignment efficiency, Payment attempts, and Revenue & commission scale them with `fractionToPercent`, which moves the decimal point two places in the Decimal string instead of multiplying a float. The web's percent format and "%" headings stay. See [[../sources/altin-reports-mobile|the Reports record]].
- Report dates use the six web presets with the web's day ranges: Last 7 and Last 30 days start 7 and 30 days before today, and This month runs to its last day. The range is computed once per "Generate report" and stored in `useReportFilters`; the query, the scope line, and every export use that stored range, and refresh moves it forward after midnight. Receivables aging has no date filter, so refresh always just refetches it. See [[../sources/altin-reports-mobile|the Reports record]].

- Desired architecture: every module owns its root, drawer, sections, constants, styles, hooks, data, and concrete feature screens. `Apps` owns directory metadata and root navigation only; shared components remain presentation-only.
- OAuth uses Authorization Code with PKCE. Tokens are never placed in URLs; refresh/revocation and API headers stay centralized.

- Use the sibling `altin-web-apps/apps/partner` as behavior, permission, and API-contract reference while preserving mobile architecture and identity.
- Modules provide current work, recent activity, and Browse entry points before section lists; the right drawer preserves overview → list → detail hierarchy.
- Orders requires VIEW_ORDERS or ADMIN in the active membership. Fleet is FLEET-only, Billing SHIPPER-only; Orders, Outlets, Team, and Accounting support both organization types. Directory entries, pinned apps, route guards, and query hooks apply the same policy through `usePermissions().can(...)`: an inline permission for a single check, a named `permissionRules` entry for combined permissions or organization-type limits. Every route stays registered and `withPermission` shows a No access screen on a failed check; never gate by unregistering a route. See [[../sources/altin-permission-gating|the permission gating decision]].
- Mutation hooks do not check permissions: gate the triggering button or screen and leave authorization to the backend; organization-context guards stay. Query hooks keep a permission `skip`, and Home analytics gates each report and its refetch, because Apollo Client 3 `refetch()` still sends a skipped query. See [[../sources/altin-permission-gating|the user correction]].
- Organization switches discard module routes, local filters, and stale request results and return Home. Every nested authenticated route group retains the active organization navigation key.
- Tips initially spans accessible organizations with an explicit scope label. Order/Courier selectors are scoped to the selected organization; Courier selection requires FLEET plus VIEW_FLEET_COURIERS or ADMIN. Linked orders display their returned organization.
- Use backend totals, explicit missing-data labels, cursor pagination, draft filters, and focus/pull refresh. Keep the initial Orders release read-only.

## Constraints

- SERLP is an architecture/configuration reference only, not a source of Altin branding or business modules.
- Do not centralize business behavior in `AppModuleScreen`, `AppFeatureScreen`, or a module resolver.
- Start from a functional login and authenticated navigation foundation, then grow concrete workflows inside module ownership boundaries.
- Do not copy web-only storage/session guidance directly into React Native.

## Decisions And Rationale

- Repository instructions override the generic create-expo-app README: this app intentionally uses `expo/AppEntry.js` and React Navigation.
- The user corrected the first scaffold to start with login and the minimum authenticated shell rather than eagerly implementing the full documented product.
- OAuth redirects preserve the `altinpartner` scheme and `redirect` path with Authorization Code plus PKCE.
- The 2026-09-11 Apps instruction supersedes the earlier five-route shell: four real tabs plus the center Apps stack action retain five visible controls. The fixed floating-track geometry remains unchanged. See [[../sources/altin-orders-mobile-web-reference|the direct Apps navigation correction]].
- A successful Expo export proves asset inclusion, not native rendering. The September 2026 brand pass replaced the broken inline-logo reference with supplied light/dark lockup PNGs, fixed-weight font instances, and official 1024-pixel app icons; iOS login was visually checked in both appearances. See [[../sources/altin-mobile-brand-system|the brand source]]. The user then rejected that pass's palette and fonts; the fixed-weight fonts were removed in favor of the app theme guide and system typography, while the lockups and icons remain.
- A module directory is useful for discovery, but module-local roots/drawers prevent generic shells from becoming a business-aware central runtime.
- PKCE is appropriate for a public mobile client because no client secret can be safely embedded in the app.

- The Orders implementation follows [[../sources/altin-orders-mobile-web-reference|the approved web-reference and mobile-architecture decisions]]. Web sidebar sections become mobile overview/drawer/list/detail experiences rather than a copied desktop layout.
- Reports split the screen from the documents (user corrections, 2026-10-18). The first build copied the web's wide tables with horizontal scrolling and a separate status table; the user replaced it with one card per record, because on a phone each record's figures belong together. The exports went the other way: Print, PDF, and CSV stay identical to the web's, so a report reads the same from either app. Each deliberate difference fixes a defect in the web output: Excel needs the BOM to read "GH₵", unescaped quotes break the CSV, first-row headings drop status columns, and the web's courier cell loses its styles in the print page. Rate scaling is the same kind of fix: the web prints the backend's fractions unscaled, so its exports show "0.53%" for a 52.75% rate. So is the landscape sheet: the web keeps its 210 mm sheet inside a landscape page and lets the browser shrink the table, but iOS clips it, which cut off Payment attempts' last columns until the sheet became 297 × 210 mm. See [[../sources/altin-reports-mobile|the Reports record]].
- Revenue & commission is kept despite the schema's deprecation (it overcounts cash COD), because its replacement, `revenueSummary`, is super-admin only. See [[../sources/altin-reports-mobile|the Reports record]].

## Verification Expectations

- Run `yarn type-check` and `yarn format:check`.
- Reuse the running Expo app/simulator for necessary read-only checks. Avoid repeated production requests; verify failure, permission, and stale-response cases through local tests. Do not create or mutate production records for validation.
- Do not tap notification rows during verification: opening one marks it read, a production write. Run agent sessions from the repository root so diff review works; the parent `C.E.Q.A` folder is not a Git repository.
- After adding a native module (for example `expo-print` and `expo-sharing` for Reports), rebuild and confirm the rebuild actually happened. `pod install` fails silently without a UTF-8 locale, so set `LANG=en_US.UTF-8`; a stale binary red-boxes with `Cannot find native module`. See [[../sources/altin-reports-mobile|the Reports record]].
- Reports were checked live (read-only, production) on 2026-10-18: every report screen, the tab and the filters, plus exports for seven reports read back from the app cache. COD reconciliation and Receivables aging data and exports were not checked. A 2026-10-20 device check confirmed the web date presets, the Assignment efficiency landscape PDF and Print sheet, all 14 Payment attempts columns on the landscape sheet, three per-report skeletons, and Dispatch backlog's PDF, CSV, and Print. The next device pass still needs dark mode, Android, the remaining PDF and Print exports (Order funnel's PDF since the sheet change), and the COD reconciliation and Receivables aging data and exports; the SHIPPER reports need a SHIPPER organization selected. 37 offline checks run from outside the repository.
- Exercise safe areas and tab/navigation backgrounds on iOS and Android.
- Verify configured API/auth endpoints without printing tokens or identifiers.
- Add tests and a release pipeline before calling the scaffold production-ready.

## Evidence

- [[../sources/altin-reports-mobile|Altin Reports Mobile]]: direct user corrections and decisions on 2026-10-18 and user-approved fixes on 2026-10-20, the repository's `docs/reports.md` and `AGENTS.md` Reports section, offline checks, and a read-only simulator check of every report screen and most exports. The work was uncommitted on `feature/apps` when recorded.
- [[../sources/altin-profile-separate-editors-correction|Altin Profile Separate Editors Correction]]: direct user correction on 2026-10-09 and the LivelyCura phone helpers.
- [[../sources/altin-support-chat-first-redo|Altin Support Chat-First Redo]]: user decisions on 2026-10-09, the Check City reference, an adversarial review, and simulator checks.
- [[../sources/altin-formik-onsubmit-correction|Altin Formik onSubmit Correction]]: direct user correction on 2026-10-09, the LivelyCura reference apps, and the Check City Support comparison.
- [[../sources/altin-profile-inline-edit-correction|Altin Profile Inline Edit Correction]]: direct user corrections on 2026-10-09 and the repository's committed form hooks.
- [[../sources/altin-profile-support-ui-corrections|Altin Profile and Support UI Corrections]]: direct user corrections with screenshots on 2026-10-08, the web profile code, and the live staging schema.
- [[../sources/altin-profile-support|Altin Profile and Support]]: direct user request and photo-picker decision on 2026-10-08, with web, API, and Apollo source verification and three review passes.
- [[../sources/altin-module-builds-and-scope-corrections|Altin Module Builds and Scope Corrections]]: direct user requests, answers, UI corrections, and scope corrections from 2026-10-07 to 2026-10-08, with read-only simulator verification.
- [[../sources/altin-permission-gating|Altin Permission Gating]]: direct user request, mutation-check correction, and per-step approvals on 2026-10-08; repository `AGENTS.md`, `docs/fleet.md`, and `docs/outlets.md` were updated the same day.

- [[../sources/altin-theme-navigation-runtime-corrections|Altin Theme, Navigation, and Runtime Corrections]]: direct user corrections from shared Codex chats, confirmed 2026-10-07; repository `AGENTS.md`, `DESIGN.md`, and `PRODUCT.md` were updated the same day.

- [[../sources/altin-mobile-brand-system|Altin Mobile Brand System]]: supplied brand book and direct user correction; repository `PRODUCT.md` and `DESIGN.md` record the implemented mobile identity.

- [[../sources/altin-outlets-mobile|Altin Outlets Mobile]]: direct scope/testing instruction and scoped implementation evidence; `docs/outlets.md` records contracts and the unverified native/live boundary.

- Historical July repository inspection: `/Users/acazumah/Documents/C.E.Q.A/altin-partner-mobile`, branch `main`, base commit `f05077b67018`, clean at that inspection.
- [[../sources/altin-orders-mobile-web-reference|Altin Orders Mobile and Web Reference]]: direct approved September plan and scoped current-code verification; repository `AGENTS.md` and `docs/orders.md` record the implementation contract.
- Current `AGENTS.md`, package manifest, entry point, navigation, auth, Apollo, Redux, theme, module folders, runtime config, and reference documentation.
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-1|C.E.Q.A/Altin Project Knowledge Harvest — Batch 1]].
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-3|C.E.Q.A/Altin Project Knowledge Harvest — Batch 3]] repository reconciliation; no batch-3 Codex record targeted Altin.
- Direct Hermes sessions `20260630_230125_403524`, `20260718_201747_c255ab`, and `20260718_223853_6755f9` in [[../sources/ceqa-altin-hermes-conversation-harvest-supplement-1|C.E.Q.A/Altin Hermes Conversation Harvest — Supplement 1]].
- Direct continuations `20260719_015234_50d0c5` and `20260719_035336_d709a6` in [[../sources/altin-mistitled-casual-greeting-continuations|Altin Mistitled Casual-Greeting Continuations]] establish Apps-directory ownership, reject centralized generic module shells, and compose fourteen module-owned feature screens from shared list primitives.

## Contradictions

- The Reports build supersedes the statement that the Reports tab is a placeholder. Its card-per-record correction replaces the first build's horizontally scrolling tables. See [[../sources/altin-reports-mobile|the Reports record]].
- Scaling rate fractions is a user-approved departure from exports identical to the web's, because the web's rates are 100 times too small. Since 2026-10-20 the repository's `docs/reports.md` and `AGENTS.md` say exports print the web's values except rates, which are scaled to percentages. See [[../sources/altin-reports-mobile|the Reports record]].
- The inline edit correction replaces the separate Edit profile, Change phone number, and Verify phone screens with in-place editing on Profile. See [[../sources/altin-profile-inline-edit-correction|the inline edit correction]].
- The UI corrections move phone change and verification from the Profile view into Edit profile, and replace the first Support composer and order rows. See [[../sources/altin-profile-support-ui-corrections|the UI corrections]].
- The Profile and Support build supersedes the statement that the More Profile and Support rows are placeholders. See [[../sources/altin-profile-support|the Profile and Support record]].
- The module builds supersede the summary that Team, Accounting, and Billing were placeholders, and the Commands claim that Orders and Outlets test suites exist. See [[../sources/altin-module-builds-and-scope-corrections|the module builds record]].
- The permission gating decision supersedes applying availability by registering module routes and the deleted Apps-owned `getAppAccess` flags. Apps keeps directory metadata; each entry declares its own `permission`. See [[../sources/altin-permission-gating|the recorded decision]].

- The theme correction supersedes the brand-book palette and fonts as the implemented app theme, and the Reports tab supersedes the Notifications tab recorded in older sources. See [[../sources/altin-theme-navigation-runtime-corrections|the recorded corrections]].

- The latest mutation Toast correction supersedes assistant-authored requirements for full mutation-result spreading, API field-error mapping into Formik and saving refs. Keep read-query results and client Yup validation; do not infer blanket removal of all errors or refs. See [[../sources/altin-orders-mobile-web-reference|the direct correction]].

- The direct mutation correction explicitly authorizes removing useMutationResource, superseding the earlier interpretation that the user had only asked for an explanation. The later exact Apollo hook correction also replaces the remaining imperative read-resource wrappers. See [[../sources/altin-outlets-mobile|the recorded correction]].

- The earlier five-route tab contract is superseded by the direct 2026-09-11 instruction: Apps opens a separate stack screen with Back. Historical source records remain evidence of the earlier decision, not current route ownership.

- The user rejected the initial Orders UI and a later combined-card replacement. Prior assistant visual review does not establish acceptance. The later explicit correction removes the drawer from list headers and all detail screens, overriding the earlier all-screen drawer plan. See [[../sources/altin-orders-mobile-web-reference|the recorded corrections]].

- Current source still includes `AppModuleScreen`, `AppFeatureScreen`, and `useAppModule`, but current reference checks found no active route or barrel consumer. They are legacy/inactive code that still conflicts structurally with the desired module-local architecture, not the active runtime owner.
- The generic README says Expo Router, an `app/` directory, npm installation, and a reset script; none describes the current Yarn/React Navigation application or its defined commands.
- Earlier notes described Home and Orders as placeholders. Current Home analytics and the approved Orders workflow supersede that description, and the October 2026 module builds replaced the remaining shells except the Reports tab and the More Profile and Support rows. Profile and Support were built on 2026-10-08 and the Reports tab on 2026-10-18.
- Earlier `app.config.ts` forced light appearance despite `app.json` requesting automatic and the icon configuration differed. The September 2026 mobile brand pass aligned the icon, splash, and automatic appearance settings; API configuration remains a separate concern.
- Auth tokens are persisted in AsyncStorage; the security posture should be reviewed before production use.
- Earlier inspection found no tests. Focused Orders, Outlets, and Fleet tests were later added, then deleted with the `tests/` directory in commit `e4c14fa`; the `test:*` scripts remain. CI, EAS release configuration, and a production build command remain unestablished here.
- Current Ionicons and registered module destinations supersede the sessions’ Material Community Icons and temporarily unavailable-destination details while preserving the accepted route/theme ownership.

## Confidence

High for current static architecture and explicit repository conventions; medium for authentication/runtime behavior because no device flow, server, build, or external provider was exercised.

## Open Questions

- When should push notifications be added? They need Firebase/FCM, APNs, and a rebuild.
- Do dark mode, Android, and the remaining unchecked Reports exports hold up in the next device pass? Should Reports add custom date ranges, the courier filter, or per-report Search entries?
- Should the web partner app scale its rates too, so both apps' exports match?
- Is the blob upload path `/v1/blobs` (the mobile REST base) or `/blobs` (the web)? Does `updateProfile` accept partner members?
- When will the backend add name, city, and about to `updateProfile` and make the photo optional?
- Should `useSystemQuery` block only on its first load? The user deferred this hardening.
- Should the shared keyboard-avoiding view change for Android so the ticket reply composer stays visible?
- When will the generic module-shell files be removed after module-local screens replace them?
- Should token persistence move to platform secure storage before production?
- Which config file and public environment contract should be canonical?
