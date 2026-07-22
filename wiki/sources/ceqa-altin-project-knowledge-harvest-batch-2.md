---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [ceqa, altin, keks, call-center, project-knowledge, codex]
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
sources:
  - ../../raw/sources/2026-07-21-ceqa-altin-project-knowledge-harvest-batch-2.md
---

# C.E.Q.A/Altin Project Knowledge Harvest — Batch 2

## Source

- Raw file: [2026-07-21-ceqa-altin-project-knowledge-harvest-batch-2.md](../../raw/sources/2026-07-21-ceqa-altin-project-knowledge-harvest-batch-2.md)
- Date: 2026-07-21
- Author: Codex, derived from three read-only local checkouts and eight bounded historical records
- Ingested: 2026-07-21

## Core Claims

- Keks report filters follow the endpoint contract: employee/user reports omit `scope`, branch and exceptions reports retain supported scope behavior, and exception details are human-formatted.
- Report date filtering uses a system-native dropdown with separate helpers/interfaces and defaults or resets to the present day.
- Call-center product selection consumes family dimensions and per-variant preferences, but current modal-owned mapping loops conflict with the explicit component-ownership correction.
- Call-center checkout splits exact-location pricing by courier type, keeps Formik/Yup validity authoritative, commits pinned locations only after reverse geocoding, and requires a current Altin estimate where applicable.
- Sixteen of 21 direct current/legacy C.E.Q.A/Pizzaman records are now classified; five remain.

## Useful Details

- All three repositories remained clean at the same branches and base commits recorded in batch 1. No project command or external integration was run.
- Historical verification results remain attributed to their sessions rather than presented as current test results.
- The supplied `familyConfig` admin guide was reference-only; no current repository documentation file was found for it.
- Settings evolved after the historical task from a tab shell into separate nested settings routes, so current source outranks that intermediate UI result.

## Connections

- [[../projects/keks-admin-portal|Keks Admin Portal]]
- [[../projects/call-center-web-app|Call Center Web App]]
- [[../projects/altin-partner-mobile|Altin Partner Mobile]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Current Keks settings are nested routes, not the historical Profile/Appearance/Tenant tab shell.
- Current call-center product selection separates hooks, helpers, interfaces, and item components, but `SelectProductModal.tsx` again owns three mapped lists that the user explicitly asked to move into imported list components.
- The family-config guide describes the intended contract, but its original session completed no repository change and current checkout contains no corresponding guide file.
- Historical builds and focused tests passed at different task endpoints; no fresh project build or test was run during this read-only harvest.

## Open Questions

- Should the call-center modal restore list-level components so iteration ownership matches the explicit structural convention?
- Should the product family and preference contract be added as maintained repository documentation?
- Are Keks nested settings routes the settled replacement for the earlier Chakra-tab direction?
- Which claims in the final five C.E.Q.A/Altin records remain current?
