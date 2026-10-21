# Altin Orders implementation corrections

Date: 2026-09-09
Source: direct user corrections in the active Altin Partner Mobile implementation conversation.
Scope: technical directives only. Screenshots, business records, names, phone numbers, identifiers, and emotional language are intentionally excluded.

## Direct technical instructions

- Use the existing Conditional component for conditional UI rendering.
- Follow SERLP Mobile's feature structure: keep list and detail screens in separate feature folders, with interfaces, components, hooks, helpers, constants, and styles separately owned.
- Use skeleton loaders for loading states.
- Preserve changes the user made after assistant updates; do not restore removed elements or overwrite intervening edits.
- The user rejected the initially supplied delivery order rows, Current work layout, and details UI. A prior agent review is not user visual acceptance.
- Inspect and use the app and emulator already running. Do not start another emulator or Expo/fixture app when the current runtime is available.
- Remove the Orders drawer from the list header.
- Keep order items as separate cards; improving their internal arrangement does not authorize combining them into a shared divider list.
- Remove the route arrow. Put location icons beside the pickup/drop-off names and space those groups cleanly.
- Remove the deliveryOrders/graphql fragment folder. Write the complete GraphQL operation inside its owning hook rather than splitting its string into another imported file.

## Scoped repository verification

The user had already created the shared skeleton components and sibling deliveryOrderDetail and tipDetail folders before the corrective pass. These existing changes are authoritative starting points, not assistant additions to restore or undo. The latest specific UI directives override earlier plan text requesting drawer access on every screen.
