# Pice Shared Menu Item Correction

- Date: 2026-08-05
- Source: Direct user corrections in Codex
- Project root: `/Users/acazumah/Documents/LivelyCura/livelycura-pice-app`

## User Corrections

> the product card is supposed to be the menu item and very soon I will add test items from the backend use it so I don't know why you just did for only the home?. so that means items loaded from the backend will be using the old ui or what? cus those ones still exist and build a new horizontal product card for the favorite or recent orders sections

> don't fucking change what was there I like you had just make general and use it. I didn't say redesign it

## Evidence Boundary

The approved vertical product card is the canonical shared `MenuItem`; generalizing it means moving its existing implementation into shared ownership without changing its visual design. Home products and backend-loaded Menu products must use that same component. Favourites and recent/order-again use a separate horizontal menu-item variant. An ownership refactor is not permission to redesign an approved component.
