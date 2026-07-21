# Hermes Persistent Memory Import

Captured: 2026-07-20
Origin: Existing built-in Hermes `USER.md` and `MEMORY.md` stores from the default and coder profiles before shared-brain consolidation.

This file preserves the imported statements as evidence. The wiki pages derived from it are the maintainable synthesis.

## Default Profile — User Preferences

- Security remediation proceeds one issue at a time, with each fix explained and verified before starting the next.
- For `bora-capital-backend` security remediation, migrations and cron jobs remain in their current placement and are not remediation targets.
- Obsidian is the long-form second brain. Hermes should consult it before asking the user to repeat established workflows and update it selectively with durable preferences, procedures, decisions, corrections, and project conventions.
- The user is technical and prefers straight-to-the-point, sophisticated information that explains how the pieces fit together.

## Coder Profile — User Preferences

- Prefer direct, respectful fixes in plain language.
- In TypeScript projects, every new or exported function requires JSDoc.
- Catch blocks should map to one deliberate `http-errors` outcome and should not rethrow unchanged errors with `throw error`.
- UI and scaffolding should mirror exact references rather than invent layouts or structure.
- React Native mobile work uses Expo and React Navigation under `src/navigation`, not Expo Router; mirror existing apps and preserve text contrast plus safe-area, status-bar, and home-indicator backgrounds.
- Payment and subaccount setup must preserve money separation: each portfolio or subaccount needs its own settlement account details.
- Bora “go live” or “finish once” means freeze scope and complete one pass; long-term roadmap items are not launch blockers, and withdrawal code is not touched unless explicitly requested.
- Follow `.hermes/plans` only within requested scope; preserve architecture, contracts, runtime, canonical IDs, `OTP=email+code`, and the native mobile app's empty CORS whitelist.
- GraphQL resolvers stay thin: delegate input and principal identity only; user loading, input whitelisting, authorization, and business logic belong in services.
- The user manually edits code during review; reread live files before editing and preserve those changes.

## Coder Profile — Project And Environment Knowledge

- LivelyCura stock and sales: `SaleItem` is one customer-facing product line per sale; batch and component relief belongs in `InventoryMovement`. `SaleItem.lineCost` is the exact COGS source and `unitCost` is a derived summary. Returns use `saleItemId`, restore from original `SALE` movements, and `SALE_RETURN` movement `sourceItemId` points to the `SaleReturnItem` ID.
- CompFlow app roles: `compflow` is the public frontend; `compflow-admin` is the internal team portal; `compflow-client-portal` is the business payroll and compliance workspace; `compflow-backend` is the Express/Apollo API.
- Saved skills and linked references are execution checklists, including exact file responsibilities and project-specific patterns, not background reading.
- CompFlow backend mirrors LivelyCura authentication: Winston logger, AJV validation, OTP login (`login`, `loginWithEmail`, or `loginWithPhoneNumber`, followed by `completeLoginWithToken`), with no password sign-in.
- CompFlow onboarding and payments mirror LivelyCura `platformSubscriptions`: public `platformPlans` → `startPlatformSignup` OTP → `completePlatformSignupVerification` JWT → authenticated `startPlatformSubscriptionCheckout` → Paystack verification or webhook → organization and owner creation pending document review. Admin manual subscription is back-office only.
- CompFlow list operations use `getPageConnection` plus `limit + 1`; by-ID operations accept only the ID; Admin and SuperAdmin bypass organization membership while tenant users remain scoped.
- Altin mobile preserves `#F40F1B` as primary and `#F9F1EF` as background. SERLP is architecture and configuration only. Each app module owns its root screen, local drawer, sections, constants, styles, hooks, data, and concrete feature screens. `Apps` provides only directory metadata and root navigation; shared components are presentation-only. Do not centralize modules in `AppModuleScreen`, `AppFeatureScreen`, or a module resolver.
- Bora backend resolves incoming Mongo IDs and then uses fetched documents' canonical IDs in downstream queries and writes.
