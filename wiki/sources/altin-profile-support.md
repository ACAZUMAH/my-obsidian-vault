---
type: source
status: active
created: 2026-10-08
updated: 2026-10-08
tags: [altin, mobile, profile, support, apollo, react-native]
sources:
  - ../../raw/sources/2026-10-08-altin-profile-support.md
confidence: high
---

# Altin Profile and Support

## Source

- Raw file: [Altin profile and support](../../raw/sources/2026-10-08-altin-profile-support.md)
- Date: 2026-10-08
- Author: user, through an Altin Partner Mobile Claude Code session
- Ingested: 2026-10-08

## Core Claims

- Support and Profile are membership- or user-level, matching the web: their routes have no `withPermission`, and More shows both to every member. Order linking in Support needs `VIEW_ORDERS`; reply and reference edits follow the filing membership's rules.
- Ticket triage is super-admin only and is not built for partners. In-app password change is not built: the API has no mutation and the web hides it.
- The profile query on `currentUser` must use `no-cache` and never refetch `System`, because System gates navigation on that cached field and an unnormalized envelope can be replaced even when ids match.
- The user chose `expo-image-picker` for profile photos, accepting a native rebuild.
- File uploads go through one shared REST helper (`/blobs`, field `blob`, success on 200); the mobile path is unverified against the backend.

## Useful Details

- Importing a package whose native module is missing from the installed binary is a fatal error under Metro, not a rejected promise; check `requireOptionalNativeModule` before the dynamic import.
- A native React Native `Modal` covers the root toast host; a modal that runs mutations needs its own host while open.
- The current native build lacks `expo-clipboard` and `expo-image-picker` until the user runs `yarn ios`.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[altin-permission-gating|Altin Permission Gating]].
- [[altin-module-builds-and-scope-corrections|Altin Module Builds and Scope Corrections]].
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].

## Contradictions Or Tensions

- Supersedes the earlier statement that the More Profile and Support rows are placeholders.

## Open Questions

- The correct REST path for blob uploads (`/v1/blobs` or `/blobs`).
- Whether `updateProfile` accepts partner members and whether a null alternate phone clears it.
