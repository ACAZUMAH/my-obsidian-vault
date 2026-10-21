# Altin Partner Module Builds and Scope Corrections — 2026-10-07 to 2026-10-08

Sanitized record of a Claude Code session on Altin Partner Mobile (`feature/apps`) that built the remaining partner modules and corrected agent behavior. It records user instructions, answers, corrections, and verified outcomes. No credentials, tokens, or personal identifiers are included.

## Module builds the user requested

- Team: the user asked to build the next app and chose "Full: views + all actions". They pointed to `altin-web-apps` for the remove gate and the permissions picker, and chose to port the SERLP action sheet for confirmations. The user then asked where "remove from the organization" and "invite member" were, and to finish everything left in the apps. Result: overview, members list and details, invite, change role, remove member, roles list and details, and role create/edit with a permissions picker.
- Accounting and Billing: built after Team. The user then asked to improve the Accounting Today card, the transaction rows, and the Billing current-billing card. Billing is SHIPPER-only; its outstanding total sums invoices only when every outstanding invoice has loaded. Billing "Statements" became "Settlements".
- API keys and Webhooks on the More tab: lists, details, creation, and webhook editing; pause, resume, and revoke for keys; secret rotation and delete for webhooks. The user chose to add `expo-clipboard` for copying one-time secrets, which requires a native rebuild (`yarn ios`). Secrets stay in local screen state and are never cached.
- Notifications: the user chose "Inbox + ticket + reply". Result: an inbox opened from the Home bell with an unread badge, mark-as-read on tap, mark all read, and support-ticket details with conversation and reply. Reply is limited to the reporter, ADMIN, or members with both view and manage support-ticket permissions, and only while the ticket is open. Push notifications were deferred because they need Firebase/FCM, APNs, and a rebuild.

## UI corrections

- Orders: the Arrived at destination badge was not visible; arrival statuses now use the pending tone. The selected filter chip in light mode was too red and now uses the subtle brand background. The status history became a collapsible accordion with checked markers for passed statuses and tighter spacing. The user rejected the first collapse design ("why don't you know how to design an accordion?"), and the rebuilt version shows a header with the latest status and update count. The user asked to hide the "By :" actor label.
- Bottom sheets: the user asked filter and action sheets to slide up from the bottom when opened and slide back down when cancelled. Reduce Motion skips the movement.
- The filter sheet could not scroll and its switches did not respond, because a Pressable wrapped the sheet panel and claimed touches. The backdrop is now a separate Pressable behind the panel.

## Bugs and lessons

- Team screens bounced back to Home when opening View all, members, or roles. Root cause: a Team query selected the organization member's `user` without `id`, so Apollo replaced the normalized object the System query shares. That triggered a System refetch and a remount of the navigation. Selecting `id` on every object shared with the System query fixed it.
- Primary buttons became invisible because the pressed-style function returned `backgroundColor: undefined`, overriding the styled fill. Pressed styles now set the color only while pressed.
- `useSystemQuery` no longer shows its blocking loader during a background refetch. The user deferred further hardening ("I don't understand that so we will come back to that later").

## Scope corrections

- The agent renamed and restyled parts of Team member details that the user had not asked to change. The user objected strongly ("I didn't ask you to change anything in the team details"). The change was reverted, and the rule became: change only what was requested, and treat an unanswered proposal as declined.
- On 2026-10-08 the user said "update them and update the vaults". The agent updated the stale documents and recorded the permission work, then asked whether to also record the module builds. The user objected: "I said do it, why do some and leave to come ask if I want you to? What does update mean?" An explicit instruction to update covers everything it reasonably includes; do all of it rather than part of it followed by a question.

## Environment facts

- The session folder was the `C.E.Q.A` parent directory, which is not a Git repository, so the desktop diff pane showed nothing. Moving the session to `altin-partner-mobile` fixed review.
- The `tests/` directory was deleted in commit `e4c14fa` ("fleet features"); `package.json` still defines `test:orders`, `test:outlets`, and `test:fleet` against it.
- Verification stayed read-only against the production API. Tapping a notification marks it read, a production write, so notification rows were not tapped during verification.

## Open items

- Push notifications (Firebase/FCM, APNs, rebuild).
- `useSystemQuery` first-load-only hardening, deferred by the user.
- Android keyboard avoidance in the shared keyboard-avoiding view for the ticket reply composer, which needs approval and Android testing.
- The More tab's user-added Profile and Support rows do not open screens yet.
