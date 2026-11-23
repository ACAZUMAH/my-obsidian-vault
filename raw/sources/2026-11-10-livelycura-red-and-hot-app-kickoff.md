# LivelyCura Red and Hot app: kickoff and identity port from Check City

Date: 2026-11-10
Source: the owner's request in a Claude Code session in `/Users/acazumah/Documents/LivelyCura`, plus what that session built and checked (paraphrased; the owner's words are summarised, not quoted).

## Owner's request

The owner started a new project, Red and Hot: a custom branded ordering app for another food business, in the folder `livelycura-red-and-hot-app` that they had already created. It is to be exactly like the Check City app: the logic stays the same as Check City and only the UI will change. Brand assets had not been received, so the app is built now with placeholders that are replaced later. No UI direction had been given yet.

## What was built

- The folder was filled from `livelycura-check-city-app` at `origin/main` commit `984f2a6` (v1.2.3, 2026-10-18). The folder is not a git repository yet; nothing was committed.
- Only brand identity changed. Display name "Red and Hot"; backend client key `RED_AND_HOT_STOREFRONT` (sent as the `client` header, so the backend picks the tenant from a Custom App record); bundle id and Android package `com.livelycura.redandhot` with `.dev` and `.preview` variants; slug and URL scheme `red-and-hot`; version `1.0.0`; PostHog `app_name` `red_and_hot_app`. These values are the session's defaults and are not yet confirmed by the owner.
- The display name and web domain sit in `src/constants/brand.ts`; `app.config.ts` repeats them in a `BRAND` block because it cannot import from `src/`.
- Check City's EAS project id, OTA update URL and App Store id were removed rather than replaced. App links (Android intent filters, iOS associated domains) and the App Store id are switched off until a real domain and App Store record exist. The web domain `redandhot.app` is a placeholder. The GitHub deploy workflows were made manual-only.
- Names that carried "CheckCity" became neutral: deep-link helpers, the order notification id parser, the support GraphQL operation and fragment names (including `refetchQueries` strings), the push installation storage key and the share-image file prefix.
- Copy: "Check City Support" now uses the brand name; the profile footer shows the brand name and the real app version instead of a hardcoded "Check City • v1.0.9"; one checkout error said "pharmacy" and now says "branch".
- The icon and logos are a neutral grey "R&H" placeholder.

## Checks

- Type check, Prettier, and Jest (18 suites, 141 tests) passed; an iOS JavaScript bundle exported cleanly and contains no Check City text; `expo config` for production, preview, development and local resolves to Red and Hot ids with no Check City project, update URL or App Store id.
- A five-lens adversarial review (logic drift, release cross-contamination, leftover brand, rename integrity, docs accuracy) with one skeptic per finding found no logic drift and no remaining route from the folder to Check City's EAS project, store listing, updates, analytics or tenant. Its real findings were in the new README checklist and one code comment, and were fixed: `eas init` restores only `extra.eas.projectId`, not `updates.url`, which has to be added by hand or the store binary ships with over-the-air updates off; EAS builds do not receive `.env`, so the variables must be set in the EAS environments; `ascAppId` in `eas.json` is needed for the automated iOS submit.
- Not run by the session: the app itself. It cannot get past its launch screen until a `.env` exists and an enabled `RED_AND_HOT_STOREFRONT` Custom App record exists in the backend.

## Inherited issues found (identical in Check City, left unchanged)

- Saving the profile refetches an operation named `me`, which does not exist (the real one is `System`), so the edited profile is not refreshed until the next system poll or restart.
- Two different queries share the operation name `GetProducts` (menu and search).
- The order-placed toast says "The facility will review…", ERP wording shown to customers.
- The login phone validation message shows a real-looking example number.
- Unused LivelyCura social links, prescription helpers and a mock menu remain in the code.
- On localhost web, both apps share browser storage keys, so running both on the same port carries the login and cart across.

## Owner decisions still open

UI direction; confirmation of the identity values; the real web domain; the support phone and WhatsApp number; curated home menu picks and delivery warning thresholds; own or shared PostHog and Maps keys; EAS project, App Store and Play records, Firebase files and push credentials; GitHub repository and secrets; Terms and Privacy links; whether customer push tokens are kept separate per app in the backend.
