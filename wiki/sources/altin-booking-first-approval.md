---
type: source
status: active
created: 2026-11-28
updated: 2026-11-28
tags: [altin, mobile, react-native, expo, navigation, permissions, decision]
sources:
  - ../../raw/sources/2026-11-28-altin-booking-first-approval.md
confidence: high
---

# Altin Booking-First Plan Approval

## Source

- Raw file: [Altin booking-first plan approved, phase 0 started](../../raw/sources/2026-11-28-altin-booking-first-approval.md)
- Date: 2026-11-28
- Author: the user, reporting their boss's approval in an Altin Partner Mobile Claude Code session; repository brief `docs/partner-booking-app.md` and plan `docs/proposals/booking-first/plan.md`
- Ingested: 2026-11-28

## Core Claims

- Approved 2026-11-28, in progress, not built: Altin Partner Mobile becomes the separate, phone-first, booking-first partner app; the web partner portal stays the back office.
- The organization type chooses the tab set; permissions decide what shows inside it:
  - Shipper: Book · Orders · Money · More
  - Outlet-limited staff (membership `isOutletRestricted` and the role isn't ADMIN): Book · My orders · More
  - Fleet: Today · Riders · Orders · Money · More
- The tab bar skips tabs the member can't open, but every route stays registered behind `withPermission`. Outlet-limited members get the web's `usablePermissions` (role permissions intersected with `LIMITED_MEMBER_PERMISSIONS`), so `can()` respects outlet limits everywhere.
- The boss accepted all five new recommendations in plan section 10:
  - Built owner features stay under More → Owner tools: Reports, CSV import, custom roles, API keys, webhooks, Tips, vehicles, availability sessions.
  - Keep the current onboarding gate.
  - Retire Home analytics.
  - Use a mobile-restricted Google Places/Maps key and `react-native-maps` (needed in phase 1).
  - No Book tab for fleets; fleet members with CREATE_ORDERS get a "Book a delivery" row in More.
- Phase 0 started on `feature/booking-first`: regenerate the schema, apply outlet limits, add the organization-type tab sets, move modules into the tabs and More, and retire Home analytics, the Search tab, the centre Apps button and directory, and the module overviews.
- Once phase 0 lands, the five-control bar rule (Home, Search, raised-centre Apps, Reports, More) and the Reports-tab and Apps-directory navigation conventions stop applying.

## Useful Details

- The tab set is picked at the root with a composite navigation key such as `${org}:${type}`, the onboarding gate's mechanism. Switching organization swaps the set and opens its first tab; if the first tab is hidden, the next visible one becomes home. The notifications bell moves to the first tab's header.
- Tab gates: Book needs CREATE_ORDERS, Orders/My orders VIEW_ORDERS, Today and Riders VIEW_FLEET_COURIERS; each Money card checks its own permission; More always shows; ADMIN passes every check.
- API facts the plan established:
  - The mobile schema copy was out of date; `organization.order.confirmCashReceipt` exists but was missing from it.
  - `order.cancel(orderId, {reason})` exists and only the admin app uses it; partner access is unconfirmed.
  - The `orderUpdated` and `courierLocation` subscriptions exist; mobile has neither subscriptions nor polling yet.
- Mobile gaps the plan established: the app ignored `isOutletRestricted`, and booking took the dropoff as typed latitude and longitude, with no address search, map pin, stops, discount code or sponsored amount.
- Later phases: 1 shipper Book, Orders and cash; 2 fleet Today, Riders and Orders; 3 More additions; 4 notifications and tracking; 5 money actions and cancel.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]]
- [[altin-onboarding-gate|Altin Onboarding and the Post-Sign-In Gate]]: the gate stays, and its composite navigation key is the model for choosing the tab set.
- [[altin-permission-gating|Altin Permission Gating]]: `withPermission` routes and `can()` checks carry over; outlet limits narrow what `can()` returns.
- [[altin-reports-mobile|Altin Reports Mobile]]: Reports move from a tab to More → Owner tools, unchanged.
- [[altin-search-browse-grouping|Altin Search Browse Grouping]] and [[altin-orders-mobile-web-reference|Altin Orders Mobile and Web Reference]]: the Search tab and the Apps stack directory they describe retire in phase 0.

## Contradictions Or Tensions

- Supersedes, once phase 0 lands, the five-control bottom bar from [[altin-orders-mobile-web-reference|the 2026-09-11 Apps instruction]] and the Reports tab from [[altin-theme-navigation-runtime-corrections|the theme and navigation corrections]]. Until then those rules describe the built app.
- The plan file's own status line still reads "draft for review"; the approval is recorded from the user's chat report.

## Open Questions

- May partners call `order.cancel`? Cancel moves into phase 1 if the backend confirms it sooner.
- Were section 10's brief questions 3 to 5 (outlet staff choosing "Recipient pays cash", who confirms cash at a branch, a tip after delivery) settled as recommended? The user's report covered recommendations 6 to 10.
