# Altin Partner Mobile: booking-first plan approved, phase 0 started

- Date: 2026-11-28
- Author: the user, through an Altin Partner Mobile Claude Code session; the user reported their boss's approval in chat
- Repository: `altin-partner-mobile`, branch `feature/booking-first` (phase 0 started this day; nothing built when recorded)
- Repository records: the boss's brief `docs/partner-booking-app.md`; the plan `docs/proposals/booking-first/plan.md` (sections 0, 2, 3, 8, 9 and 10), with `mockups.html` and `screens/` beside it

## What happened

The boss wrote a brief for a booking-first partner app: shippers book a ride and see where the parcel is; fleets run their riders and those riders' orders; it should feel like a tool picked up for a job, not a control room. Its first open question was whether this is a separate app or a mode inside the web partner portal (`altin-web-apps/apps/partner`).

The session wrote a plan for applying the brief to the mobile app and asked for approval before building. The plan's status line said "draft for review, 28 November 2026. Nothing has been built or changed in the app." The user then reported in chat that the boss approved the plan and accepted all five recommendations in its section 10. Phase 0 started the same day on branch `feature/booking-first`.

## The decision

- The mobile app is the separate, phone-first booking app. The web partner portal stays the back office (the brief's section 6). Approving the plan settled the brief's "separate app or a mode" question.
- The organization type chooses the tab set at the root (a navigation key such as `${org}:${type}`, the same mechanism as the onboarding gate). Permissions decide what shows inside it:
  - Shipper (`organization.type = SHIPPER`): Book · Orders · Money · More
  - Outlet-limited staff (membership `isOutletRestricted` and the role isn't ADMIN; the web's `isOutletLimited`): Book · My orders · More
  - Fleet (`organization.type = FLEET`): Today · Riders · Orders · Money · More
- Inside a set, the tab bar does not draw a tab the member can't open; every route stays registered behind `withPermission`. If the first tab is hidden, the next visible one becomes home. Switching organization swaps the whole set and opens its first tab.
- Outlet-limited members get the web's `usablePermissions`: their role's permissions intersected with `LIMITED_MEMBER_PERMISSIONS`, so `usePermissions().can()` respects outlet limits everywhere.
- Tab gates: Book needs CREATE_ORDERS; Orders and My orders need VIEW_ORDERS; Today and Riders need VIEW_FLEET_COURIERS (FLEET); each Money card has its own check; More always shows; ADMIN passes every check.
- The notifications bell moves to the header of the first tab (Book or Today).

## Section 10 recommendations the boss accepted

- (6) Already-built owner features stay under More → Owner tools rather than being deleted: Reports with their exports, outlet CSV import, custom roles, API keys, webhooks, Tips, vehicles and availability sessions.
- (7) Keep today's onboarding gate, where pending organizations see onboarding and nothing else, instead of the brief's banner with the app open behind it.
- (8) Retire Home analytics. The same figures stay in Reports; the brief keeps charts and KPIs in the portal.
- (9) Use a Google Places/Maps key restricted to the mobile app, plus `react-native-maps`. Needed in phase 1 for address search and the map pin.
- (10) No Book tab for fleets. Fleet members with CREATE_ORDERS get a "Book a delivery" row in More.

Section 10's first five items (the brief's questions) carried recommendations too; the user's report covered the five new ones above.

## Phase 0 (foundations), started 2026-11-28

- Regenerate the mobile GraphQL schema.
- Apply outlet limits (`isOutletRestricted`, `outlets`, `usablePermissions`).
- Add the organization-type tab sets with permission-aware tab bars.
- Move existing modules into the tabs and More.
- Retire Home analytics, the Search tab, the centre Apps button and directory, and the module overview screens.
- Update the repository rules (AGENTS.md, DESIGN.md, PRODUCT.md), which currently fix the five-control bar.

Later phases: 1 shipper Book, Orders and cash (needs the Maps key); 2 fleet Today, Riders and Orders; 3 More additions; 4 notifications and tracking; 5 money actions and cancel.

## What the plan's research established

- The mobile app's copy of the GraphQL schema was out of date; `organization.order.confirmCashReceipt` exists in the API but was missing from it.
- `order.cancel(orderId, { reason })` exists, but only the admin app uses it. Whether partners may call it is unconfirmed; the backend team must confirm.
- The `orderUpdated(orderId)` and `courierLocation(orderId)` subscriptions exist; the web order page uses the first. Mobile has no subscription or polling today.
- `rateCourier` and the fleet order actions (`updateStatus`, `markDeliveryAsComplete`, `assignToCourier`) exist.
- Mobile ignored `isOutletRestricted`, so an outlet-limited member saw screens their server access would refuse.
- Mobile booking took the dropoff as typed latitude and longitude: no address search, no map pin, and no stops, discount code or sponsored amount.

## Superseded once phase 0 lands

- "Keep five visible bottom-bar controls: Home, Search, raised-center Apps, Reports, and More."
- The Reports-tab and Apps-directory navigation conventions (Reports moves to More → Owner tools; Search and the Apps directory retire).
