# Pice Delivery Address And Branch Separation

- Date: 2026-08-05
- Source: Direct user correction in Codex
- Project root: `/Users/acazumah/Documents/LivelyCura/livelycura-pice-app`

## User Correction

> selecting a delivery location shouldn't open a branch modal

## Evidence Boundary

The Home `Deliver to` control opens delivery-address search and GPS selection, not the visible branch selector. The branch header owns explicit branch selection. Choosing a delivery address may silently recalculate the nearest fulfilling branch in the background, but it must not ask the customer to select a branch as a substitute for selecting an address.
