---
type: synthesis
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project-knowledge, harvest, checkpoint, codex]
sources:
  - ../sources/project-knowledge-completion-and-bootstrap-directive.md
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/livelycura-project-knowledge-harvest-batch-2.md
  - ../sources/livelycura-project-knowledge-harvest-batch-3.md
confidence: high
---

# Project Knowledge Harvest Status

## Thesis

This is the canonical resumable checkpoint for staged project-knowledge harvesting from live repositories and Codex history. A completed repository inventory does not imply that all historical sessions for that family have been processed.

## Current Checkpoint

- Last completed batch: LivelyCura batch 3 on 2026-07-21.
- Repositories inventoried: 10.
- LivelyCura working-directory sessions discovered: 37.
- Sessions processed: 24.
- LivelyCura sessions not yet processed: 13.
- Repository mutations: none.
- Latest vault evidence: [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]].

## Discovered Project Families

| Family | Known repository/app surface | Status |
| --- | --- | --- |
| LivelyCura | Backend, admin portal, pharmacy ERP portal, customer portal/mobile, courier mobile, CheckCity mobile, Loop mobile, SERLP web/mobile | Batches 1–3 complete; history remains pending |
| CompFlow | Public frontend, admin, client portal, backend | Pending |
| Kusantec/Bora | Kusantec/Bora Capital repositories and apps | Pending |
| C.E.Q.A/Altin | Altin mobile and related C.E.Q.A repositories | Pending |
| Portfolio | Portfolio frontend/backend or platform repositories | Pending |
| Standalone projects | Remaining repositories under `/Users/acazumah/Documents` | Pending inventory after named families |

## Completed Batches

### LivelyCura Batch 1

Processed session IDs:

- `019f7d44-11d6-7052-8733-59ca06469788` — Audit courier module completeness.
- `019f7af0-4a79-77d3-9bef-9c1abd7a74e0` — Optimize launchpad header.
- `019f7714-8636-77c0-b544-e62372205fd7` — Polish results and test requests.
- `019f6d9c-efe2-79c0-9c92-aaca88309bc3` — Update model defaults to OpenAI.
- `019f62a3-cea2-7951-9a24-8710d6c68304` — Update pharmacy portal layout.
- `019f61b7-40b7-7023-b62c-b60a729ec375` — Use impeccable.
- `019f5cbd-0621-7cb0-b4b8-24dfcec53987` — Add AI result validation.
- `019f56a3-70f8-7ab3-a3e4-ff932654a075` — Update Checkcity order screen.

Created project pages:

- [[../entities/projects/livelycura-admin-portal|LivelyCura Admin Portal]]
- [[../entities/projects/livelycura-backend|LivelyCura Backend]]
- [[../entities/projects/livelycura-check-city-app|LivelyCura CheckCity App]]
- [[../entities/projects/livelycura-courier-mobile|LivelyCura Courier Mobile]]
- [[../entities/projects/livelycura-customer-mobile|LivelyCura Customer Mobile]]
- [[../entities/projects/livelycura-customer-portal|LivelyCura Customer Portal]]
- [[../entities/projects/livelycura-loop-app|LivelyCura Loop App]]
- [[../entities/projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../entities/projects/serlp|SERLP]]
- [[../entities/projects/serlp-mobile|SERLP Mobile]]

### LivelyCura Batch 2

Processed session IDs:

- `019ec6f5-89f0-79f2-9dc7-25a94e6afe70` — Add lab requests to sales.
- `019eb927-e9a8-70e1-b559-9b35bffb628b` — Review backend against PDF.
- `019ea1d1-ae47-7340-8842-0ee5e5d83363` — Fix test builder renderer.
- `019e9562-55d4-7830-868d-b7a8484cd26c` — Polish rendering engine UI.
- `019e78b1-163a-70f0-b619-b4f90e4110f3` — Plan lab test definition rollout.
- `019e7553-e228-76a2-b842-d69fa817be5c` — Add samples section.
- `019e4af8-1012-79d3-b679-346a61c1dff6` — Add lab test builder.
- `019e28e5-be8d-7912-be33-816f759c9db7` — Add animations and theme toggle.

Updated project pages:

- [[../entities/projects/livelycura-backend|LivelyCura Backend]]
- [[../entities/projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../entities/projects/livelycura-check-city-app|LivelyCura CheckCity App]]

### LivelyCura Batch 3

Processed session IDs:

- `019edbb8-c050-7422-acd5-5d6423e29599` — Update iOS mockups with screenshots.
- `019edb14-5a4c-7203-b874-732d0046b020` — Update iOS screens.
- `019e88a0-484c-7ea1-998a-92fd115116db` — Delete seed data except orgs.
- `019e191c-5c93-7970-98a5-97ad9fe7bf05` — Update iOS screens and logos.
- `019e02a9-1c7a-76b2-b722-61d9fe53fda3` — Add dynamic app banners.
- `019e0007-1015-7c22-875e-dae188fa0ccb` — Add live activity support.
- `019dffe9-809c-7051-8e17-accb646dcdf6` — Fix ExpoInAppUpdates crash.
- `019dfea2-359d-7182-91d6-be1d54e0dd3c` — Stretch active bottom tab.

Updated project pages:

- [[../entities/projects/livelycura-backend|LivelyCura Backend]]
- [[../entities/projects/livelycura-admin-portal|LivelyCura Admin Portal]]
- [[../entities/projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../entities/projects/livelycura-check-city-app|LivelyCura CheckCity App]]
- [[../entities/projects/livelycura-loop-app|LivelyCura Loop App]]
- [[../entities/projects/serlp-mobile|SERLP Mobile]]

## Conflicts And Uncertain Claims

- Courier desired architecture versus live implementation: provider companies, standalone network behavior, separate payout, COD collection, and remittance are approved product direction; current storage remains a simpler task model.
- Customer Portal contains both Yarn and npm lockfiles.
- Pharmacy Portal README uses npm instructions while current repository scripts and lockfile use Yarn.
- Backend README retains stale Mocha/OpenAPI/boilerplate claims; current package scripts and source use Vitest and the present server architecture.
- The older MLS PDF proposal grouped many tests under one clinical request and draft invoice; later explicit decisions and current code create one request per lab-linked sale item inside the ordinary sale transaction.
- TestDefinition builder layout changed repeatedly; current `TestDefinitionWizard` and `DefinitionRenderer` outrank historical tab, stepper, split-pane, and accordion variants.
- App purposes inferred from source ownership without a dedicated current README remain medium confidence.
- The seeded-MLS cleanup migration was historically reported as registered, but current source leaves it out of the migration index and preserves a questionable repeated filter property. It is not current runnable behavior and was not reported as run against live data.
- Current custom-app ownership supersedes historical paths: Admin Portal assigns apps, Pharmacy Portal `src/apps/customApps` manages assigned-app banners, and CheckCity consumes its enabled app pair.
- Live Activities are absent from active CheckCity/backend branches. The deferred app branch still contains a custom local module that conflicts with the later maintained-package direction.
- SERLP, Loop, and CheckCity historical store-artwork outputs are absent from current repositories; their corrected branding and export rules remain durable, but file existence is not asserted.
- Unindexed Codex sessions may be child, evaluation, or approval sessions; they remain pending triage and are not assumed to add unique durable knowledge.

## Pending Batches

### Next: LivelyCura Batch 4

Process exactly these eight sessions:

1. `019e239f-dd9e-73a3-b75d-e37d13bd22ff` — Research lab feature approach.
2. `019dfdd7-8f8d-7901-a34a-09301f861b50` — Fix Android OTP input.
3. `019dfdba-34ef-7692-8e90-4259a7d2f55f` — Fix App Store auth rejection.
4. `019dfd88-68ed-7420-b3dd-f3f150e1c73f` — Fix App Store review issues.
5. `019de5bd-34c3-72d0-817d-15a59e470c01` — Add BackgroundDecoration.
6. `019de35a-9685-7462-bb90-739847980b24` — Fix delivery task type bug.
7. `019de13d-bcbd-7c50-bba1-6b62fd64e064` — Create Play Store feature graphic.
8. `019dda04-807b-70a3-96b5-ff1cfae7eaa5` — Fix bottom tab label overflow.

After those eight, triage the remaining indexed session that appears unrelated to project knowledge plus four unindexed sessions for unique evidence. Move to CompFlow only after the LivelyCura checkpoint explicitly says its relevant history is complete or intentionally deferred.

## Next Action

Resume from this page and perform LivelyCura batch 4 only. Re-verify implementation claims against live code, update existing project pages rather than creating duplicates, create one new batch manifest and source summary, update the two operating manuals only if new cross-project or scaffolding rules are proven, validate links/frontmatter, and prepend exactly one log entry.

## Evidence

- [[../sources/project-knowledge-completion-and-bootstrap-directive|Project Knowledge Completion And Bootstrap Directive]]
- [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]]
- [[../sources/livelycura-project-knowledge-harvest-batch-2|LivelyCura Project Knowledge Harvest — Batch 2]]
- [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]]

## Implications

- Agents can resume without rescanning or overstating completed coverage.
- Contradictions stay visible until code or an explicit correction resolves them.

## Contradictions Or Tensions

- Family order favors finishing LivelyCura, but the eight-session cap requires multiple LivelyCura batches.

## Related

- [[../concepts/codex-project-knowledge-harvest|Codex Project Knowledge Harvest]]
- [[software-development-operating-manual|Software Development Operating Manual]]

## Sources

- [[../sources/project-knowledge-completion-and-bootstrap-directive|Project Knowledge Completion And Bootstrap Directive]]
- [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]]
- [[../sources/livelycura-project-knowledge-harvest-batch-2|LivelyCura Project Knowledge Harvest — Batch 2]]
- [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]]

## Open Questions

- How many unindexed LivelyCura sessions contain unique user corrections rather than duplicated child/evaluation context?
