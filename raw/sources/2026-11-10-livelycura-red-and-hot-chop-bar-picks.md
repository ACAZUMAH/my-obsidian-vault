# LivelyCura Red and Hot app: Chop Bar part picks and build

Date: 2026-11-10
Source: the owner's choices on the Chop Bar picker page in a Claude Code session in `/Users/acazumah/Documents/LivelyCura`, and the build that followed (paraphrased).

## Picks

The owner chose, on `design-probes/red-and-hot-app/b-picker.html`: tab bar option 1 "Signboard plank" (flat bar docked to the bottom, four equal tabs Menu, Search, Orders, Cart with names always shown, current tab red with a palm-oil brush stroke), product card option 1 "Edge to edge" (photo fills the card top, price sticker and add button on the photo edge), item screen option 1 "Torn paper" (edge-to-edge photo, torn cream info sheet, sticky bar with stepper and a wide "Add to cart" button), item photo "Fill". The owner said reading explanations does not help them choose; they want to see options and click.

## Build

The Chop Bar design with these picks was built into `livelycura-red-and-hot-app` on 2026-11-10: theme tokens, Lilita One and Nunito fonts, paper background replacing the drifting icon wallpaper, shared PriceSticker, BrushUnderline and StatusStamp components, the three picks, and restyled Menu, Cart, Checkout and Orders. Type check, 204 tests and Prettier pass; a diff review against Check City found no behaviour change. Screens were not yet viewed on the device because the backend had no `RED_AND_HOT_STOREFRONT` custom app record, so the app stops at its load error screen.

A `RED_AND_HOT_STOREFRONT` definition (display name, placeholder web domain, SERLP sender, "Red and Hot" email name) was added to the backend's custom app definitions, uncommitted on the `feature/hrm` branch.
