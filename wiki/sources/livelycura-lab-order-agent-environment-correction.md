---
type: source
status: active
created: 2026-09-09
updated: 2026-09-09
tags: [livelycura, mls, sales, orders, agent, environments]
sources:
  - ../../raw/sources/2026-09-09-livelycura-lab-order-agent-environment-correction.md
  - ../../raw/sources/2026-09-09-livelycura-lab-sale-non-stock-correction.md
---

# LivelyCura Lab Sale And Agent Environment Corrections

## Source

- Earlier raw evidence: [Order POS direction, later withdrawn](../../raw/sources/2026-09-09-livelycura-lab-order-agent-environment-correction.md)
- Latest raw evidence: [Sale POS and non-stock correction](../../raw/sources/2026-09-09-livelycura-lab-sale-non-stock-correction.md)
- Date: 2026-09-09
- Author: User; implementation context checked by Codex.
- Ingested: 2026-09-09

## Core Claims

- Sale POS creates test requests for lab-linked sale items, including non-stock laboratory services. Merely placing an Order POS order does not create a test request. This later correction explicitly withdraws the earlier order trigger.
- Agent availability should include local development and staging, exclude production, and retain ordinary access permissions.

## Useful Details

- Product sync must preserve laboratory-service non-stock behavior; creating the service must not require finished-product inventory.
- Keep commercial provenance on the sale and one idempotent request per lab-linked sale item. Ordinary sales and accounting retain their existing responsibilities.
- Check the persisted product stock flag before changing workflows to solve an inventory error. Lab sync must explicitly choose non-stock behavior instead of inheriting the catalog's stock default. Regression tests must exercise a priced lab service with zero inventory records.
- Ordinary non-stock products skip inventory; non-stock bundles can still consume stocked components. Do not conflate these cases.
- A deployment environment is not the same as an optimized build mode. Staging also uses a production-optimized Vite build; use the explicit application environment for the Agent gate.
- Local verification does not establish staging deployment or justify modifying existing staging records automatically.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]] owns transactional creation, version pinning, identity, and commercial linkage.
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]] owns Sale POS, sale-based request provenance, and consistent Agent visibility across Home and the main shell.

## Contradictions Or Tensions

- The user first selected Order POS, then explicitly requested its reversal in favor of Sale POS. Retain the earlier raw evidence as history; the later sale correction is authoritative. Agent environment guidance remains unchanged.
- The inventory error was reproducible for a product marked as stock with no available batches, while the ordinary non-stock sale path worked. It did not justify moving the clinical trigger to orders.
- Deployment state must be rechecked in live source and runtime, not inferred from this durable decision.

## Open Questions

- Check each environment's existing product flags separately; local code changes do not automatically repair stored catalog records or authorize deployment.
