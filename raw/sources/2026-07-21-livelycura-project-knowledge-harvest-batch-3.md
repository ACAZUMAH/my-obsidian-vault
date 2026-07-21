# LivelyCura Project Knowledge Harvest — Batch 3 Evidence Manifest

Date: 2026-07-21

## Scope

- Family: LivelyCura.
- Live repository root: `/Users/acazumah/Documents/LivelyCura`.
- Affected repositories: `livelycura-backend`, `livelycura-admin-portal`, `livelycura-pharmacy-portal`, `livelycura-check-city-app`, `livelycura-loop-app`, and `serlp-mobile`.
- Repository writes: none.
- Codex sessions processed: exactly 8, as fixed by the batch-2 checkpoint.
- Transcript handling: only session metadata, sanitized user corrections, durable claims, and reported verification outcomes are preserved. Full transcripts, routine tool chatter, private organization identifiers, and attachment contents are excluded.
- Secret-bearing files and values were not inspected or copied. Environment files, auth data, tokens, credentials, certificates, private keys, connection strings, generated output, dependencies, build output, caches, and binaries were excluded.

## Processed Codex Sessions

| Date | Session ID | Working directory | Indexed title |
| --- | --- | --- | --- |
| 2026-06-18 | `019edbb8-c050-7422-acd5-5d6423e29599` | `/Users/acazumah/Documents/LivelyCura` | Update iOS mockups with screenshots |
| 2026-06-18 | `019edb14-5a4c-7203-b874-732d0046b020` | `.../livelycura-loop-app` | Update iOS screens |
| 2026-06-02 | `019e88a0-484c-7ea1-998a-92fd115116db` | `.../livelycura-backend` | Delete seed data except orgs |
| 2026-05-11 | `019e191c-5c93-7970-98a5-97ad9fe7bf05` | `.../livelycura-check-city-app` | Update iOS screens and logos |
| 2026-05-07 | `019e02a9-1c7a-76b2-b722-61d9fe53fda3` | `/Users/acazumah/Documents/LivelyCura` | Add dynamic app banners |
| 2026-05-07 | `019e0007-1015-7c22-875e-dae188fa0ccb` | `/Users/acazumah/Documents/LivelyCura` | Add live activity support |
| 2026-05-07 | `019dffe9-809c-7051-8e17-accb646dcdf6` | `.../livelycura-check-city-app` | Fix ExpoInAppUpdates crash |
| 2026-05-06 | `019dfea2-359d-7182-91d6-be1d54e0dd3c` | `.../livelycura-check-city-app` | Stretch active bottom tab |

## Minimal Sanitized Conversation Evidence

- `019edbb8…`: SERLP store artwork must use the supplied real application screenshots and the exact product identity “SERLP,” without “SERLP Mobile,” “by LivelyCura,” an invented rounded logo badge, phone drop shadows, or dark backing. App Store iPhone images were required at `1242x2688`, iPad images at `2048x2732`, and the Play featured graphic at `1024x500`, all RGB without alpha. The six supplied screenshots, not an invented dashboard, were the source material.
- `019edb14…`: Loop artwork must use the actual transparent app icon and the identity “Loop by SERLP” on a solid green background. The user corrected an unrelated-app logo, border, gradient, and mispositioned screenshots. iPhone artwork was required at `1242x2688`; the Play direction settled on a realistic three-phone composition with a large center phone and smaller side phones. The final working location was an external Downloads folder rather than another app repository.
- `019e88a0…`: the requested one-time backend cleanup removed seeded MLS catalog data for every organization except two explicitly allow-listed organizations. The intended scope included Samples, the seeded LAB Department, TestDefinitions and version snapshots, matching Categories, and linked Product references. The private organization identifiers are intentionally represented only as `[two allow-listed organizations]` in this manifest.
- `019e191c…`: CheckCity store imagery must use real app screenshots, CheckCity colors, and the correct project logo. Artificial black phone backing, bright borders, and heavy decorative lines were rejected in favor of clean edges and restrained decoration. The historical output was later moved outside the repository.
- `019e02a9…`: custom-app assignment belongs to the Admin Portal. The Pharmacy Portal manages banners only for apps already assigned to its organization, and customer mobile apps consume only the assigned and enabled organization/app pair. Reads must not create assignments. The managed-app set is a fixed enum, initially including CheckCity. Banner configuration includes content, ordering, schedule, CTA/deep link, targeting, draft/publish lifecycle, and analytics. The user also required repository-native form, hook, interface, modal, and mutation ownership rather than mutations in generic form submission glue.
- `019e0007…`: the desired order-progress capability is iOS Live Activities/Dynamic Island plus Android live/progress notifications. CheckCity push registration uses the CheckCity managed-app identity. The latest correction deferred the feature to local `feature/live-activities` branches and chose Software Mansion’s maintained Expo Live Activity package for resumed work instead of a new internal Expo module; unrelated cart, profile, bottom-tab, and push-token work was to remain on the active branches.
- `019dffe9…`: an optional native in-app-update module must not crash startup when it is unlinked. The historical correction broke a Loader import cycle, dynamically imported the native module only on the supported production path, and emitted Google-services config only when a path resolved. Native configuration checks passed in that session; unrelated pre-existing type errors were not represented as fixed.
- `019dfea2…`: the active bottom tab should retain sufficient width by shrinking inactive tabs, not by squeezing the active tab. Cart rows show descriptions and use a reduced-motion-aware swipe-to-delete interaction whose behavior belongs in a hook. System theme requires native automatic appearance plus `expo-system-ui`; choosing system resets the React Native override, and a native rebuild—not a JavaScript reload—is required after the config change.

## Current-Code Verification

### LivelyCura Backend

- `src/models/customApps`, `src/services/customApps`, `src/graphql/customApps`, and the matching Shield rules currently implement organization/app assignment, banner lifecycle, targeting, and event analytics.
- Organization custom-app reads return existing assignments; assignment and unassignment are explicit service operations. Banner creation requires an assigned app, while the active-banner read additionally requires an enabled assigned configuration, published/active state, valid schedule, and matching target filters.
- The managed-app enum includes CheckCity. CheckCity-targeted order push paths use the customer audience plus the CheckCity app identity.
- `scripts/migrations/migrateDeleteSeedLabCatalogExceptAllowedOrgs.ts` still contains the historical cleanup operations and allow-list boundary. It is not registered in the current migration index, so it is not described as an active migration. A repeated property in one deletion filter also makes the preserved file unsuitable as unquestioned executable evidence.
- A local `feature/live-activities` branch exists and contains Live Activity persistence, GraphQL, authorization, APNs, and FCM work. The current active branch contains no Live Activity implementation.

### LivelyCura Admin Portal

- Organization administration currently owns custom-app assignment UI and focused GraphQL hooks. Assignment is explicit and separate from banner management.
- The working tree already contained unrelated modified generated GraphQL files before the harvest. Generated files were excluded and left untouched.

### LivelyCura Pharmacy Portal

- Current custom-app management lives under `src/apps/customApps`, not the older historical `src/settings/customApps` path.
- The portal derives tabs from the organization’s active assignments, uses per-app forms and focused mutation hooks, and exposes banner content/analytics without creating organization/app assignments.
- When no custom app is assigned, navigation is hidden or the route safely returns to Home. The implemented page uses the current two-column management/analytics arrangement and a theme-aware empty state.

### LivelyCura CheckCity App

- `src/banner` queries active banners with the CheckCity app identity and optional facility/platform context, renders nothing for loading/error/empty results, and records impression/click events before opening supported CTAs.
- Push-token registration uses the CheckCity managed-app identity.
- The active branch contains no Live Activity implementation. Its local `feature/live-activities` branch contains the earlier `src/liveActivities` work, widget code, and a custom local Expo module. That branch snapshot therefore needs rework to follow the later explicit Software Mansion package decision.
- `useOpenStoreAppUpdate` dynamically imports `expo-in-app-updates`. `app.config.ts` conditionally includes the Google-services path only when the selected variant resolves one.
- Current bottom-tab styles give the non-floating active item more flex than inactive items. Cart swipe behavior is isolated in `useCartItemSwipe`, includes a first-item hint, supports full-swipe removal, and respects reduced motion.
- Theme preference supports `system`, `light`, and `dark`; native appearance is automatic and `expo-system-ui` is configured. System preference clears the React Native color-scheme override.

### Loop And SERLP Mobile

- Current repositories retain their established Expo/React Navigation application structures.
- Neither repository currently contains the historical deployment/store-artwork folders or renderer outputs. Those artifacts are historical deliverables, not current repository assets; only the verified design/export conventions are promoted.

## Reported Historical Verification

- The catalog-cleanup session reported a successful backend build and registration of the one-time migration, but also reported that it was not run against live data. Current source inspection supersedes the registration claim because the migration is no longer in the index.
- The custom-app sessions reported backend and portal generation/type/build/test work plus live browser verification. The harvest itself verified present source ownership and behavior but did not rerun those suites.
- The in-app-update session reported passing public Expo config checks. Its broader type check retained unrelated pre-existing failures.
- The bottom-tab/cart/theme session reported successful CheckCity type and formatting checks and required a new native build for the appearance configuration.
- The store-artwork sessions reported platform-sized RGB exports without alpha. The harvest did not inspect binaries and found no current repository artifact directories.

## Contradictions And Uncertainty

- The cleanup migration was historically reported as registered and build-passing, but the current migration index does not register it and the preserved file contains a questionable repeated filter property. It is historical/stale code, not a current runnable migration contract.
- Historical custom-app paths and early ownership placed more behavior in Pharmacy Portal settings. Current source and the latest correction place assignment in Admin Portal, banner management in Pharmacy Portal `src/apps/customApps`, and consumption in CheckCity.
- The latest Live Activities decision selects an external maintained package, while the deferred app branch still preserves the earlier custom-module implementation. The active branches contain no feature, so Live Activities are not current production behavior.
- Historical store-artwork outputs were moved outside repositories or later removed. Exact export and branding rules remain evidence-backed, but the resulting files are not asserted to exist now.
- Historical store-image iterations included incorrect logos, gradients, borders, dark backing, and invented UI. Those iterations are rejected approaches, not reusable design conventions.

## Follow-Up Boundary

The next bounded batch remains LivelyCura and should process exactly these eight indexed sessions:

1. `019e239f-dd9e-73a3-b75d-e37d13bd22ff` — Research lab feature approach.
2. `019dfdd7-8f8d-7901-a34a-09301f861b50` — Fix Android OTP input.
3. `019dfdba-34ef-7692-8e90-4259a7d2f55f` — Fix App Store auth rejection.
4. `019dfd88-68ed-7420-b3dd-f3f150e1c73f` — Fix App Store review issues.
5. `019de5bd-34c3-72d0-817d-15a59e470c01` — Add BackgroundDecoration.
6. `019de35a-9685-7462-bb90-739847980b24` — Fix delivery task type bug.
7. `019de13d-bcbd-7c50-bba1-6b62fd64e064` — Create Play Store feature graphic.
8. `019dda04-807b-70a3-96b5-ff1cfae7eaa5` — Fix bottom tab label overflow.

After batch 4, triage the remaining indexed session that appears unrelated to project knowledge and the four unindexed LivelyCura-working-directory sessions for unique evidence before declaring the family complete or intentionally deferred.
