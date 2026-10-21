---
type: source
status: active
created: 2026-09-18
updated: 2026-09-18
tags: [bora-capital, ci, dependencies]
sources:
  - ../../raw/sources/2026-09-18-bora-production-ci-audit-scope.md
---

# Bora Production CI Audit Scope

## Source

- Raw file: [Direct user instruction](../../raw/sources/2026-09-18-bora-production-ci-audit-scope.md)
- Date: 2026-09-18
- Author: User
- Ingested: 2026-09-18

## Core Claims

- Run `yarn audit:production` only in the production CI workflow, not the reusable workflow shared by PR and staging CI.

## Useful Details

- Production deployment remains gated by both the reusable build/test job and a production-owned dependency audit job.
- This changes CI placement; it does not remove the audit script or change local package scripts.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]

## Contradictions Or Tensions

- Supersedes the earlier placement of the production dependency audit in the shared reusable workflow.

## Open Questions

- None for the requested workflow scope.
