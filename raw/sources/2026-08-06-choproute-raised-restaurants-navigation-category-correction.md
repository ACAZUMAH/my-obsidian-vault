# ChopRoute Raised Restaurants Navigation And Category Correction

Date: 2026-08-06
Author: User

## Direct Correction

- Preserve live user edits. Before changing a file, reread its current contents and adapt the requested change around newer user-authored work; do not restore an earlier agent-authored version over it.
- ChopRoute does not use five equal bottom tabs. Home, Explore, Cart, and Orders remain the actual bottom-tab routes.
- Restaurants replaces the supplied reference's raised center action. It opens its own root-stack screen outside the bottom navigator, and that screen needs a clear Back action.
- The bottom navigation should follow the supplied full-width shelf with two controls on each side of the raised center action. The newest reference keeps labels visible.
- Marketplace category discovery must not be derived only from categories attached to returned products. Active ordinary ERP categories owned by organizations with active ChopRoute marketplace access must be readable directly.
- Same-name organization categories may be merged into one customer-facing marketplace filter while retaining all underlying ERP category IDs for product filtering.

## Evidence

- Reference, dark variant: `../assets/2026-08-06-choproute-raised-center-navigation-dark.jpeg`
- Reference, light variant: `../assets/2026-08-06-choproute-raised-center-navigation-light.jpeg`
- Direct conversation correction and implementation verification in the active Codex task on 2026-08-06.
