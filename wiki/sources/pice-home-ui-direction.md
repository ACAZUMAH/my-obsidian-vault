---
type: source
status: active
created: 2026-08-05
updated: 2026-08-06
tags: [livelycura, pice, food-ordering, product-design, mobile-ui]
sources:
  - ../../raw/sources/2026-08-05-pice-home-ui-direction.md
  - ../../raw/sources/2026-08-05-pice-ui-correction-bottom-tabs-background.md
  - ../../raw/sources/2026-08-05-pice-component-state-correction.md
  - ../../raw/sources/2026-08-05-pice-inactive-tab-label-correction.md
  - ../../raw/sources/2026-08-05-pice-home-menu-naming-correction.md
  - ../../raw/sources/2026-08-05-pice-shared-menu-item-correction.md
  - ../../raw/sources/2026-08-05-pice-cart-active-state-correction.md
  - ../../raw/sources/2026-08-05-pice-delivery-address-branch-separation.md
confidence: high
---

# Pice Home UI Direction

## Source

- Raw file: [2026-08-05-pice-home-ui-direction.md](../../raw/sources/2026-08-05-pice-home-ui-direction.md)
- Correction: [2026-08-05-pice-ui-correction-bottom-tabs-background.md](../../raw/sources/2026-08-05-pice-ui-correction-bottom-tabs-background.md)
- Component-state correction: [2026-08-05-pice-component-state-correction.md](../../raw/sources/2026-08-05-pice-component-state-correction.md)
- Inactive-label correction: [2026-08-05-pice-inactive-tab-label-correction.md](../../raw/sources/2026-08-05-pice-inactive-tab-label-correction.md)
- Naming correction: [2026-08-05-pice-home-menu-naming-correction.md](../../raw/sources/2026-08-05-pice-home-menu-naming-correction.md)
- Shared-menu-item correction: [2026-08-05-pice-shared-menu-item-correction.md](../../raw/sources/2026-08-05-pice-shared-menu-item-correction.md)
- Cart active-state correction: [2026-08-05-pice-cart-active-state-correction.md](../../raw/sources/2026-08-05-pice-cart-active-state-correction.md)
- Delivery/branch correction: [2026-08-05-pice-delivery-address-branch-separation.md](../../raw/sources/2026-08-05-pice-delivery-address-branch-separation.md)
- Date: 2026-08-05
- Author: User
- Ingested: 2026-08-05

## Core Claims

- Pice must have a visibly independent interface rather than presenting as a CheckCity reskin.
- The home screen order is branch/notification/profile header, delivery-location search row, primary promotional banner, categories, popular picks, secondary marketing banner, and recent or favourite orders.
- Match the supplied bottom-tab composition directly: Home, Menu, Cart, and Orders inside one full-width rounded bar; omit Profile from the tab bar. Cart never floats beyond the bar.
- Cart presentation follows route selection, not item quantity. Only an active Cart uses the filled circle and filled icon; an inactive Cart remains an outline icon even when its item-count badge is visible.
- Only the currently selected bottom tab shows its label. Every inactive tab is icon-only; when Cart is selected, its `Cart` label is visible regardless of item count.
- Home and Menu names are not interchangeable: Home owns the home route, screen, and composition; Menu owns the menu route and browsing screen. Search is functionality inside Menu, not the Menu tab's route identity.
- The delivery control is a compact card with a pin, two-line address, inline chevron, and search action. Categories are a direct six-item circular-photo strip without a heading, outline selection treatment, or View-all control.
- The Home `Deliver to` control selects a delivery address through search or GPS; it must never open the visible branch-selection modal. Explicit branch selection belongs to the branch header.
- Pice must not render decorative background patterns, floating icon motifs, or screen/modal background-decoration layers.
- The current palette is explicitly provisional because the final Pice color system has not been selected.
- The approved vertical product card is the shared `MenuItem` for Home and backend-loaded Menu products; generalization must preserve its existing visual design. Favourites and recent/order-again use a separate horizontal variant.

## Useful Details

- Two full mobile references and three focused component crops establish a compact commerce hierarchy with image-led campaign cards, circular category media, horizontally scrollable product cards, and a fixed rounded navigation surface.
- Profile remains reachable from the home header even though it is removed from bottom navigation.
- The earlier detached-right and permanently raised Cart interpretations came from inherited code and are explicitly superseded by the state-aware in-bar Cart.
- Generated Pice food photography should support, not determine, the future brand palette.
- Code ownership mirrors the product language: home-only UI lives under `src/home`, menu browsing and `/menu` live under `src/menu`, and reusable search controls and queries remain under `src/search`; `/search` is compatibility-only.
- Approved UI must be generalized through component ownership, not visual reinterpretation. A refactor does not authorize new dimensions, spacing, typography, elevation, or styling unless the user explicitly requests redesign.
- The Cart badge communicates quantity independently from selection. It never triggers the active fill or label by itself.
- Address selection may silently recalculate the nearest fulfilling branch, but branch resolution remains background orchestration rather than a customer-facing substitute for address selection.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[pice-project-bootstrap-directive|Pice Project Bootstrap Directive]]
- [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]]

## Contradictions Or Tensions

- CheckCity remains the technical scaffold, but its home-screen composition is no longer an acceptable visual reference for Pice.
- The implemented coral, aubergine, and cream colors are useful for design validation but cannot be treated as approved brand tokens.
- The inherited global pattern and background-decoration components were removed from the Pice source after all render sites were cleared.
- The earlier interpretation that Cart-with-items could trigger filled emphasis is superseded by the direct active-state correction: only the selected route is filled and labeled.
- The inherited behavior that routed the Home delivery control to `BranchSelector` is superseded: the control opens delivery-address search/GPS while the branch header remains the explicit branch selector.
- The later ChopRoute marketplace correction supersedes the explicit branch header for this repository: Home now owns only delivery-location selection, while delivery facility resolution moves fully behind the server boundary. See [[choproute-marketplace-stage-one-correction|ChopRoute Marketplace Stage-One Correction]].

## Open Questions

- What final palette, typography, logo treatment, and food-photography direction should become the Pice brand system?
- Should recent orders or explicit customer favourites take precedence when both datasets are available?
