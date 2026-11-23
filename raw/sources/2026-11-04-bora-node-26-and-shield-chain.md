# Bora backend moves to Node 26 LTS and drops graphql-shield chain()

Date: 2026-11-04
Source: Production error the user reported, the user's decisions on `bora-capital-backend`, and the resulting change.

## Incident

- Production logged `TypeError: (0 , util_1.isUndefined) is not a function` from `graphql-shield/cjs/rules.js` for `addUserExpoPushToken`, with status 500.
- Cause: production is built by the DigitalOcean App Platform Node.js buildpack (stack paths under `/workspace`), not by the repository Dockerfile. The buildpack installs the newest Node that satisfies `engines`, which was `>=22.13.0`, so production ran Node 23 or later.
  - Node 23 removed `util.isUndefined`.
  - graphql-shield 7.6.5, the latest release (2022), calls it inside `chain()` and `race()`.
  - CI and the Dockerfile used Node 22, so no test caught it.
  - `chain()` first appeared on 2026-10-30, in the per-user rate limits for `addUserExpoPushToken`, `enableBiometricLogin` and `uploadFundFactSheet`. All three returned 500 in production.
- The user also shared a Node security advisory: the 20–21 Oct 2026 releases fix high-severity vulnerabilities, one of them remote code execution. Patched versions: 22.23.4, 24.22.1 and 26.12.1.

## User decisions

- Do not hold the project on an older Node to avoid the library bug. Replace `chain()` instead, so the code is not tied to a Node version.
- Use whichever Node has no known vulnerabilities and causes no trouble for the dependencies or the project.

## Implementation

- `allInOrder(...checks)` in `src/graphql/shield/general.ts` is one graphql-shield `rule()` that runs plain checks (`ctx => true | Error`) in order and stops at the first refusal. Later checks, such as rate limits, only count calls the earlier checks allowed.
- The checks are `requireSession`, `requireCustomerApp`, `rateLimitCheck` and `permissionCheck`. The existing rules (`isAuthenticated`, `rateLimitRule`, `requirePermission`) are built from them.
- A unit test fails if any shield file imports `chain` or `race` from graphql-shield.
- Node policy: Node 26 LTS everywhere.
  - `engines.node` is `>=26.12.1 <27`: the patched floor, and the cap keeps the buildpack off odd-numbered non-LTS releases.
  - CI (`reusable.yml` and the production audit job) uses Node `26`.
  - The Dockerfile uses `node:26-bookworm-slim`.
  - Patch releases arrive automatically. The major version moves deliberately, in those four places, when the next LTS ships (Node 28, October 2027).
- Checks before choosing Node 26:
  - All 1,373 installed packages accept Node 26.
  - `bcrypt` 6 uses N-API prebuilds.
  - A clean frozen install on Node 26 passes yarn's engine checks.
  - Build, type-check and all 1,585 tests pass on Node 26 and on Node 22.
  - The production audit shows 0 critical, 0 high, 20 moderate and 7 low dependency advisories.
