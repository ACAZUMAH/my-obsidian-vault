# LivelyCura lab ordering and Agent environment correction

Date: 2026-09-09
Source: Direct user correction in the LivelyCura Codex conversation.

## User evidence

> sales are only for products that tracks inventory, so the sale pos isn't what is supposed to create the test requests it's the order Pos cos that one sells items that don't track inventory. also the agent tap on the main header is supposed to be only disabled in production not local and staging but on staging I don't see it

## Evidence boundary

This states the user's intended lab workflow, not a verified claim that every existing sale service rejects non-stock products. Inspection found automatic request generation in the sale transaction, no equivalent facility-order hook, and Agent visibility tied to Vite's production-build flag. Existing generic sales support non-stock items. These implementation facts explain the discrepancy; they do not override the correction. No patient identifiers, credentials, or temporary demo records are retained here.
