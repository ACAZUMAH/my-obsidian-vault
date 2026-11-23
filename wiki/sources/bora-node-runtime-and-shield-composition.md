---
type: source
status: active
created: 2026-11-04
updated: 2026-11-04
tags: [bora-capital, backend, node, ci, deployment, graphql-shield]
sources:
  - ../../raw/sources/2026-11-04-bora-node-26-and-shield-chain.md
  - ../../raw/sources/2026-11-04-bora-dependency-advisories-cleared.md
---

# Bora Node Runtime And Shield Composition

## Source

- Raw files:
  - [2026-11-04-bora-node-26-and-shield-chain.md](../../raw/sources/2026-11-04-bora-node-26-and-shield-chain.md)
  - [2026-11-04-bora-dependency-advisories-cleared.md](../../raw/sources/2026-11-04-bora-dependency-advisories-cleared.md)
- Date: 2026-11-04
- Author: User decisions on a production incident, plus the resulting change
- Ingested: 2026-11-04

## Core Claims

- Production is built by the DigitalOcean App Platform Node.js buildpack, which installs the newest Node satisfying `package.json` `engines`. The Dockerfile is for local and Compose use only.
- The backend runs Node 26 LTS everywhere: `engines.node` `>=26.12.1 <27`, CI Node `26`, and Dockerfile `node:26-bookworm-slim`. The floor excludes the versions fixed by the October 2026 security release. The cap keeps production on LTS and on what CI tests. Move all four together when the next LTS ships.
- Do not use graphql-shield `chain()` or `race()`. They call `util.isUndefined`, which Node 23 removed, and graphql-shield is unmaintained. Compose ordered checks with `allInOrder(...)` from `src/graphql/shield/general.ts`. A unit test enforces this.
- The user's rule: fix library incompatibilities in code rather than holding the project on an older or vulnerable Node.
- Since 2026-11-04 the production audit shows only one low advisory: `deepmerge` through `@react-email/render`, unreachable and with no upstream fix. The unused nodemailer senders and package were removed, `fast-uri` is pinned to 3.1.9, and `qs`, `@protobufjs/utf8` and `uuid` were refreshed.

## Useful Details

- The incident: `addUserExpoPushToken`, `enableBiometricLogin` and `uploadFundFactSheet` returned 500 in production from 2026-10-30, when `chain()` rate limits were added, until the fix.
- Checks are plain functions returning `true` or an `Error`: `requireSession`, `requireCustomerApp`, `rateLimitCheck`, `permissionCheck`. Rule wrappers stay for single checks.

## Connections

- [[wiki/projects/bora-capital-backend|Bora Capital Backend]]
- [[wiki/sources/bora-production-ci-audit-scope|Bora Production CI Audit Scope]]

## Contradictions Or Tensions

- The user dislikes upper version bounds. The `<27` cap is kept because the buildpack would otherwise install odd-numbered non-LTS releases that CI does not test. Patch releases still arrive automatically.

## Open Questions

- None open. Recheck `deepmerge` when `@react-email/render` or `html-to-text` drops it.
