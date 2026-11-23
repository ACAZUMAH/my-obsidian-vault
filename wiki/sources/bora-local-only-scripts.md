---
type: source
status: active
created: 2026-10-17
updated: 2026-11-22
tags: [bora-capital, backend, git, ci, scripts]
sources:
  - ../../raw/sources/2026-10-17-bora-local-only-scripts.md
  - ../../raw/sources/2026-11-22-bora-backlog-committed-and-deposits-script-gitignored.md
source_date: 2026-10-17
ingested: 2026-10-17
confidence: high
---

# Bora Local-Only Scripts

## Source

- Raw file: [Local-only operational scripts](../../raw/sources/2026-10-17-bora-local-only-scripts.md)
- Date: 2026-10-17
- Author: User request and decisions, implemented by the agent
- Ingested: 2026-10-17
- Raw file: [Backlog committed and the deposits script made local-only](../../raw/sources/2026-11-22-bora-backlog-committed-and-deposits-script-gitignored.md) (owner decision, 2026-11-22)

## Core Claims

- `scripts/bootstrap`, `scripts/paystack_staging`, `scripts/paystack_production`, and `scripts/seeds` are gitignored and never pushed. The specs `tests/unit/scripts/bootstrapAdmin.spec.ts` and `tests/unit/scripts/seedFundCatalog.spec.ts` are also ignored.
- `scripts/deposits_production` (the owner's `inspectDeposit.ts` diagnostic, README and pasted constants) is gitignored too (owner decision, 2026-11-22), like `scripts/funds_production`, `scripts/admin_production` and `scripts/nia_staging`. A new `*_production` scripts folder belongs in `.gitignore` before any commit.
- Committed code, tests, and package.json scripts must not reference those files, because CI type-checks `src`, `tests`, and `scripts` from a fresh checkout and then runs Jest.
- Fund-service tests use the synthetic `tests/fixtures/fundFacts.ts`, never the seed catalog.

## Useful Details

- Run the local scripts directly, for example `npx ts-node -r tsconfig-paths/register scripts/paystack_production/setupBalancedPortfolio.ts`.
- Untracking does not rewrite history: the folders remain in 3 earlier commits on GitHub. No key-like strings were found in them.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-production-ci-audit-scope|Bora Production CI Audit Scope]]

## Contradictions Or Tensions

- None.

## Open Questions

- None.
