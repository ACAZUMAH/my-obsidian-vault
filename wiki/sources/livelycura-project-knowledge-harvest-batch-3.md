---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [livelycura, project-knowledge, codex, mobile, custom-apps]
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
sources:
  - ../../raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-3.md
---

# LivelyCura Project Knowledge Harvest — Batch 3

## Source

- Raw file: [2026-07-21-livelycura-project-knowledge-harvest-batch-3.md](../../raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-3.md)
- Date: 2026-07-21
- Author: Codex, from user-directed repository and transcript evidence
- Ingested: 2026-07-21

## Core Claims

- Custom-app ownership is explicit: Admin Portal assigns a fixed managed-app enum to organizations, Pharmacy Portal manages banners only for assigned apps, and CheckCity consumes only its assigned and enabled organization/app configuration. Reads never create assignments.
- Store-distribution artwork should be derived from real application screenshots and correct project identity, exported to exact platform dimensions in RGB without alpha, and avoid invented UI, wrong logos, artificial heavy frames, or backing.
- Live Activities are deferred on dedicated local branches, not present on active branches. The latest package decision supersedes the preserved app branch’s custom native-module implementation.
- Optional native modules must fail softly when unavailable; variant-specific native config paths should be emitted only when resolved.
- System theme support is a native configuration concern as well as JavaScript state: automatic native appearance and `expo-system-ui` require a native rebuild.
- Interaction logic such as swipe-to-delete belongs in focused hooks and must honor reduced motion; active navigation items keep space by compacting inactive items.

## Useful Details

- The backend’s historical MLS catalog cleanup file remains present but unregistered, and therefore is not current migration behavior. The two exception organizations are intentionally recorded only as `[two allow-listed organizations]`.
- Banner configuration supports content, schedule, ordering, CTA/deep link, targeting, publish state, and impression/click analytics.
- Current Pharmacy Portal ownership is `src/apps/customApps`; the older `src/settings/customApps` path is historical.
- CheckCity dynamically imports its in-app-update native dependency and conditionally emits the selected variant’s Google-services path.
- Historical deployment artwork was moved outside or removed from the repositories, so the batch promotes its design/export rules without claiming current artifacts exist.

## Connections

- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/livelycura-admin-portal|LivelyCura Admin Portal]]
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]]
- [[../projects/livelycura-loop-app|LivelyCura Loop App]]
- [[../projects/serlp-mobile|SERLP Mobile]]

## Contradictions Or Tensions

- The catalog cleanup was historically reported as registered and build-passing, but current source leaves it out of the migration index and retains a questionable repeated filter property.
- The deferred CheckCity Live Activities branch still contains the earlier custom local Expo module even though the latest explicit direction is to use Software Mansion’s maintained package when work resumes.
- Historical custom-app paths and ownership were revised; current source plus the latest user correction define Admin assignment, ERP banner management, and mobile consumption.
- Store-artwork conventions are durable, but historical output files are not present in the current project repositories.

## Open Questions

- Should the stale catalog-cleanup migration be repaired and registered, or removed after confirming whether it ever ran in an intended environment?
- When Live Activities resume, which parts of the deferred app branch can survive replacement of the custom module with the maintained package?
- Should store-artwork renderers live in a dedicated design/deployment repository rather than application repositories?
