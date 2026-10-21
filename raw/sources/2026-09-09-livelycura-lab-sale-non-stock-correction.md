# LivelyCura Sale POS and non-stock laboratory correction

Date: 2026-09-09
Source: Later direct user correction in the same LivelyCura Codex conversation.

## User evidence

> revert the the sale and order issue, the sale pos is supposed to also create the test request not the order pos, if the product is non stock item the sale is supposed to be created without the error it produced no inventory so revert and check the code well for bug and let's see who made that mistake

## Verified implementation context

The sale formatter already bypasses inventory allocation for an ordinary non-stock product. Test-definition product sync omitted `isStockItem`, so newly synced products inherited `true`. The stock-behavior commit `5035b54d` dated 2026-06-27 introduced that default without updating the older MLS sync path. The old sync integration fixture created inventory and therefore did not test the zero-inventory service case. Git attribution identifies recorded authorship, not whether a human or assistant originally wrote the code.

## Interpretation boundary

This later correction explicitly withdraws the earlier Order POS request trigger. It does not withdraw the separate Agent local/staging-versus-production rule or authorize staging deployment, live sales, or bulk data repair. Non-stock bundles remain distinct because their stocked components may require inventory.
