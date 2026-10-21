---
type: source
status: active
created: 2026-09-14
updated: 2026-09-14
tags: [livelycura, doordrop, mobile, branding, assets]
sources:
  - ../../raw/sources/2026-09-14-doordrop-rebrand-and-asset-structure.md
confidence: high
---

# doorDrop Rebrand And Asset Structure

## Source

- Raw file: [2026-09-14-doordrop-rebrand-and-asset-structure.md](../../raw/sources/2026-09-14-doordrop-rebrand-and-asset-structure.md)
- Date: 2026-09-14
- Author: user
- Ingested: 2026-09-14

## Core Claims

- The consumer food-marketplace app formerly branded ChopRoute is now named
  doorDrop.
- Static app images live directly under `assets/`; nested image folders are not
  accepted.
- Runtime image imports are centralized through `assets/images.js`.

## Useful Details

- The repository path is `/Users/acazumah/Documents/LivelyCura/livelycura-door-drop`.
- The rebrand updates the Expo name, slug, scheme, native identifiers, package
  name, visible copy, analytics label, and generated native project.
- The existing `CHOPROUTE_MARKETPLACE` backend client key remains unchanged for
  compatibility. Renaming the backend marketplace identity is a separate,
  coordinated migration rather than an automatic consequence of the app rebrand.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura doorDrop App]]
- [[choproute-marketplace-stage-one-correction|ChopRoute Marketplace Stage-One Correction]]

## Contradictions Or Tensions

Earlier project records use ChopRoute as both the public app name and backend
marketplace identity. The public name is superseded by doorDrop; the backend
identity remains temporarily valid for compatibility.

## Open Questions

- Will the backend marketplace record and `CHOPROUTE_MARKETPLACE` client key be
  renamed in a later coordinated migration?
