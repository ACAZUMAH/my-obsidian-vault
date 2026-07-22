---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, ceqa, call-center, location, altin, tooling]
sources:
  - ../../raw/sources/2026-07-21-call-center-shared-brain-hermes-audit.md
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
---

# C.E.Q.A Call Center Hermes Supplement — 2

## Source

- Raw report: [2026-07-21-call-center-shared-brain-hermes-audit.md](../../raw/sources/2026-07-21-call-center-shared-brain-hermes-audit.md)
- Exact project session: `20260709_202251_e5340a`
- Target repository: Call Center Web App

## Core Claims

- Location autocomplete and selected-place coordinate resolution are one provider session: create one token when search begins, reuse it for suggestions and resolution, then clear it after consuming the selected place.
- Require three characters before querying autocomplete.
- Use cached location-list, coordinate-resolution, and reverse-geocoding operations rather than deprecated operations.
- Preserve latitude and longitude in their correctly named fields during reverse geocoding.
- Normalize both list-wrapped and direct Altin estimate response shapes while retaining a usable estimate identifier.
- The project adopted the sibling Keks flat ESLint, Commitlint, Commitizen, and Husky tooling baseline.

## Useful Details

## Historical Verification Boundary

- The session reported five focused location tests passing, then a corrected production build passing.
- The full suite reported four files and ten assertions passing but exited nonzero because of two pre-existing unhandled router/request errors.
- Lint eventually exited zero under `--quiet` after relevant rules were demoted to warnings; this is not a clean-lint claim.
- Commit-message acceptance/rejection and the hook were historically exercised, followed by a passing build.
- No current command was rerun during this harvest.

## Current Reconciliation

- Current clean `develop` source at the inspected commit contains the cached location hooks, three-character threshold, provider-session token lifecycle, coordinate regression test, flexible estimate normalization, and tooling files.
- The session response claimed several direct-payment delivery fields were added to one order mutation, but current source and the containing commit show only `location` in that selection set. The broader subclaim remains unsupported/incomplete.

## Connections

- [[../projects/call-center-web-app|Call Center Web App]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Exit-zero quiet lint does not establish absence of warnings.
- Generated GraphQL types containing fields do not prove a handwritten operation selects them.
- This session extends earlier Codex-backed location work but is independent direct-Hermes evidence rather than a duplicate.

## Open Questions

- Should the direct-payment mutation deliberately request the omitted delivery-fee, timing, and courier fields, or was the broader historical completion claim incorrect?
