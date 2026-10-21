---
type: source
status: active
created: 2026-10-19
updated: 2026-10-19
tags: [bora-capital, admin-portal, ci, github-actions, netlify, correction]
sources:
  - ../../raw/sources/2026-10-19-bora-admin-portal-ci-cd-convention.md
source_date: 2026-10-19
ingested: 2026-10-19
confidence: high
---

# Bora Admin Portal CI/CD Convention

## Source

- Raw file: [Bora admin portal CI/CD convention](../../raw/sources/2026-10-19-bora-admin-portal-ci-cd-convention.md)
- Date: 2026-10-19
- Author: User corrections, implemented by the agent
- Ingested: 2026-10-19

## Core Claims

- Web portal CI/CD copies the `livelycura-pharmacy-portal` workflows: a PR `ci.yml` calling a reusable CI workflow, plus self-contained `staging.yml` (push to `develop`) and `production.yml` (push to `main`), each with a build job that uploads `dist/` as an artifact and a deploy job with `environment:` that runs `netlify-cli deploy --prod` against its own site.
- API URLs are repository-level variables with the environment in the name (`STAGING_API_BASE_URL` / `PRODUCTION_API_BASE_URL` in the pharmacy portal, `STAGING_API_URL` / `PRODUCTION_API_URL` in the Bora admin portal). Never hardcode API URLs in workflow YAML, and never use one variable name scoped per GitHub environment.
- Secrets are repository-level and environment-named: `NETLIFY_AUTH_TOKEN`, `NETLIFY_STAGING_SITE_ID`, `NETLIFY_PRODUCTION_SITE_ID`. GitHub environments carry only protection rules, such as production reviewers.

## Useful Details

- The Bora backend follows the same naming (`DIGITALOCEAN_STAGGING_BACKEND_ID`, `DIGITALOCEAN_PRODUCTION_BACKEND_ID`).
- Setup for the admin portal is documented in its `docs/admin-portal/CI_CD.md`.

## Connections

- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Contradictions Or Tensions

- None.

## Open Questions

- None.
