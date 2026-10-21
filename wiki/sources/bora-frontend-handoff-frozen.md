---
type: source
status: active
created: 2026-10-12
updated: 2026-10-17
tags: [bora-capital, backend, frontend-handoff, workflow]
sources:
  - ../../raw/sources/2026-10-12-bora-frontend-handoff-frozen.md
  - ../../raw/sources/2026-10-13-bora-one-handoff-per-unpushed-batch.md
  - ../../raw/sources/2026-10-17-bora-frontend-handoff-2026-10-17.md
source_date: 2026-10-12
ingested: 2026-10-12
confidence: high
---

# Bora Frontend Handoffs Frozen Once Sent

## Source

- Raw file: [Direct user correction](../../raw/sources/2026-10-12-bora-frontend-handoff-frozen.md)
- Raw file: [Restored sent handoff and 2026-10-17 handoff](../../raw/sources/2026-10-17-bora-frontend-handoff-2026-10-17.md)
- Date: 2026-10-12
- Author: Direct user correction
- Ingested: 2026-10-12
- Refinement: [One handoff per unpushed batch](../../raw/sources/2026-10-13-bora-one-handoff-per-unpushed-batch.md), direct user correction on 2026-10-13.

## Core Claims

- A frontend handoff the user has sent to the frontend developer must never be edited.
- All backend updates not yet committed and pushed form one batch with ONE handoff, `docs/frontend-handoff-YYYY-MM-DD.md`. The same file is extended and corrected in place while the batch is unpushed, so it reflects the final state; a new file starts only after the batch is pushed and sent. Items are marked for the customer app or the admin portal.
- Corrections to sent items are stated in the next handoff, not patched into the old one.

## Useful Details

- This replaces the 2026-10-01 convention of keeping two living handoff files (`frontend-handoff-app.md`, `frontend-handoff-admin.md`) and updating them with every change.
- `docs/frontend-handoff-2026-10-13.md` was pushed in `fc3fa4a` and sent; it is frozen at that content. It covers KYC rejection reason, error format, malformed-request messages, expired codes, sign-in lock, one-at-a-time refresh, signup limit, existing-customer accounts, currencies and rates, lookup filters, Grow Wealth provider errors, and notification sound.
- On 2026-10-16 the agent extended the sent 2026-10-13 file, and the extension was pushed in `3bea375`. On 2026-10-17 the file was restored to its sent content, and the additions moved to `docs/frontend-handoff-2026-10-17.md`: a correction of the sent "no correction form" item, rejected-KYC correction through `updateKyc`/`kycSubmission`, and the Grow Wealth cash movement statement. Check `git reflog show origin/<branch>` before extending any dated handoff.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-biometric-login-and-handoff-docs|Bora Biometric Login And Consolidated Frontend Handoff]]

## Contradictions Or Tensions

- Supersedes the 2026-10-01 instruction to update the two handoff files in place.
- On 2026-10-12 one unpushed batch was split across two dated files; the user corrected that on 2026-10-13, and they were merged.

## Open Questions

- None.
