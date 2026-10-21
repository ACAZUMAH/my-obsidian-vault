# Bora Handoff Delta, Current-User Permissions, And Customer Inbox Items — Decisions And Implementation

Date: 2026-10-01
Source: direct user direction in Claude Code during Bora backend work (2026-10-01)

## User Direction

- Withdrawals, investment accounts, and goals and top-ups had already been sent to the frontend developer, so the app handoff must not repeat them; it covers only what changed since the previous handoff.
- Finish the current-user permissions query, move the welcome, KYC, deposit, and withdrawal notifications into the inbox (explicitly approved, including the withdrawal flow), and commit.
- The user committed the earlier work in `3aa25fc`, including the deletion of the per-feature docs, `SECURITY.md`, and `auth-wallet-frontend-integration.md`.

## Agent Evidence

- The previous handoff covered withdrawals, investment accounts, goals and top-ups, existing-customer onboarding, KYC, Grow Wealth, and statements. The trimmed app handoff keeps biometric login, the Grow Wealth query renames, funds, support, notifications, marketing preferences, and banners.
- The welcome, KYC, deposit, and withdrawal flows send their own templated email and SMS, which read named transaction fields. Inbox items store only a title and body, so moving those sends into the delivery worker would lose the templates; the inbox item is added alongside the existing sends instead.
- `notifyUsers` dedupes by recipient and dedupe key and returns only newly created items.

## Implemented Scope

- `getMyPermissions` returns the signed-in user's permissions from enabled roles and direct grants, with wildcards expanded. Any signed-in user may call it; customers get an empty list. The admin handoff uses it for menus.
- `addCustomerInboxNotification` adds an inbox-only item (`channels: []`) and never throws. Signup welcome (keyed per user), KYC approval (keyed per user and KYC submission), deposit pending, deposit successful, and withdrawal requested (keyed by withdrawal request, transaction reference, or BCL reference) now create inbox items, and their pushes carry `notificationId`. `DEPOSIT_SUCCESSFUL` was added to `NotificationsType`. The sign-in welcome-back push stays out of the inbox.
- Verification: build passed; 142 test suites and 878 tests passed; 23 mutations were killed.
