# Bora admin portal CI/CD: follow the pharmacy portal workflows

Date: 2026-10-19
Source: The user's corrections while the agent wrote GitHub Actions staging and production pipelines for `bora-admin-portal`.

## Sequence

1. The agent first put the API URL in one `VITE_API_URL` variable scoped per GitHub environment, read by a shared reusable deploy workflow.
2. The user objected that one name cannot tell production from staging and said they do not declare different environments' values in GitHub.
3. The agent then hardcoded the staging and production API URLs in `staging.yml` and `production.yml`.
4. The user rejected that: "look at the livelycura-pharmacy-portal workflows ... do you fucking see writing api urls in the ci yml". They had asked at the start to reuse conventions from their other projects.

## The reference pattern (`livelycura-pharmacy-portal/.github/workflows`)

- `ci.yml` (PRs into `main` and `develop`) calls a reusable CI workflow.
- `staging.yml` (push to `develop`) and `production.yml` (push to `main`) are self-contained: CI, a build job that uploads `dist/` as an artifact, and a deploy job with `environment: staging|production` that downloads it and runs `netlify-cli deploy --prod` against its own site.
- API URLs are repository-level variables: `vars.STAGING_API_BASE_URL`, `vars.PRODUCTION_API_BASE_URL`.
- Secrets are repository-level, with the environment in the name: `NETLIFY_AUTH_TOKEN`, `NETLIFY_STAGING_SITE_ID`, `NETLIFY_PRODUCTION_SITE_ID`.

## Implemented

`bora-admin-portal` now uses `vars.STAGING_API_URL` / `vars.PRODUCTION_API_URL`, those three Netlify secrets, and the pharmacy portal's job layout (SHA-pinned actions, least-privilege permissions, concurrency groups, production reviewers on the `production` environment).
