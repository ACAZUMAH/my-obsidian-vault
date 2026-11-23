# Bora backend dependency advisories cleared

Date: 2026-11-04
Source: User-approved triage and upgrade on `bora-capital-backend` (the user said "Yes, apply them").

## Triage

The production audit on Node 26 reported 20 moderate and 7 low findings: 17 unique advisories in 6 packages. None was reachable from our code.

- `nodemailer` 10.0.12: no callers. All mail goes through Resend.
- `qs` 6.14.0: `express.urlencoded` uses `extended: false`; `googleapis` only formats our outgoing requests with it.
- `fast-uri` 3.1.8: ajv uses it only for schema `$id`/`$ref`, which our schemas don't have. It was pinned in `resolutions` (commit 2abde13, 2026-09-29).
- `uuid` 13.0.0: we only call `v4()`.
- `@protobufjs/utf8` 1.1.0: Apollo usage reporting is not configured.
- `deepmerge` 4.3.1: reached through `@react-email/render` → `html-to-text`, merging only our own options. No upstream fix exists.

## Changes

- Removed the unused senders `src/services/notifications/nodeMailer.ts` and `gmail/index.ts`, and their exports `sendEmailViaGmail` and `sendEmailViaNodeMailer`.
  - The Gmail sender had a personal address hard-coded as the sender.
  - Also removed the `nodemailer` and `@types/nodemailer` packages. The types pulled in an old `@aws-sdk/client-sesv2` tree.
- Raised the `fast-uri` resolution pin to 3.1.9.
- Refreshed lockfile entries to `qs` 6.17.1, `@protobufjs/utf8` 1.1.2 and `uuid` 13.0.2.
- Result: the audit shows 0 critical, 0 high, 0 moderate and 1 low (`deepmerge`, accepted).
- Frozen install, type-check, build and all 1,585 tests pass on Node 26 and on Node 22.
- Lesson: after yarn 1 removes a package tree, a local `node_modules` can keep orphaned nested copies, such as an old `@smithy/core`, that break module resolution. Reinstall local `node_modules` from scratch; CI and the buildpack always install from scratch.
