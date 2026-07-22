---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, portfolio, frontend, react, design]
sources:
  - ../sources/portfolio-project-knowledge-harvest-batch-1.md
  - ../sources/portfolio-featured-projects-hermes-chain.md
  - ../sources/portfolio-carousel-skills-livelycura-hermes-supplement.md
confidence: high
---

# Portfolio Client Portal

## Summary

Public React portfolio for engineering work, case studies, experience, skills, resume access, availability, and contact paths.

## Purpose

Helps potential clients, collaborators, recruiters, and technical partners understand the user’s capabilities and move into project details, resume, or contact actions.

## Stack

- React 19, Vite 6, strict TypeScript.
- Apollo Client, Mantine 8, React Router 7.
- Tailwind 3 and CSS Modules.
- GSAP, Framer Motion, Lenis, Three.js/React Three Fiber, Swiper, and Embla.
- GraphQL Codegen and Vitest configured to permit no tests.

## Architecture

Route/feature folders own home, projects, details, experience, contact, and blog surfaces. Apollo hooks query public portfolio/project data. The home aggregate renders Hero, About, skills, experience, featured projects, and contact sections. Reusable UI primitives live under `src/components/ui`.

## Folder Ownership

- `src/home`: home composition, feature components, hooks, helpers, and styles.
- `src/projects` and `src/project`: listing and project-detail routes.
- `src/experience`, `src/contact`, `src/blogs`: route-owned features.
- `src/services`: Apollo composition.
- `src/components/ui`: reusable presentation primitives.
- `PRODUCT.md` and tracked design instructions: product/design/accessibility contract.

## Commands

- `yarn dev` — Vite on port 5173.
- `yarn build` — TypeScript and Vite build.
- `yarn generate` — GraphQL operation generation.
- `yarn lint` — ESLint script; historical records reported missing flat config.
- `yarn test` — Vitest, currently allowed to pass with no tests.
- `yarn preview` — static preview.

## Runtime/Deployment

Static Vite frontend consuming the Portfolio GraphQL API. No tracked CI, container, conventional README, hosting manifest, or production deployment contract was found.

## Durable Conventions

- Use route/feature-owned folders and feature-local operations/hooks.
- Use references as inspiration, not templates; preserve the site’s authored visual language.
- Drive profile facts, education, skills, counts, projects, resume, and availability from CMS/API data with explicit fallbacks.
- Keep the home About introductory; exhaustive biography belongs on a dedicated page if that route is implemented.
- Preserve approved regions while iterating on unresolved regions.
- Validate actual asset formats, responsive overflow, broken assets, console output, and reduced-motion behavior.
- Use section-specific layout rails; do not globally squeeze a hero that requires full visual breathing room.
- Keep Featured Projects in a section-local feature that owns CMS selection, media fallbacks, project links, click tracking, responsive carousel behavior, and its Hero anchor. Do not collapse it into one oversized page file.
- Preserve equal responsive Swiper cards, autoplay/loop/pagination, and the established full-image-at-rest/details-on-hover interaction. Do not reintroduce coverflow, centered enlargement, neighbor dimming, or prominent navigation unless explicitly redesigned and accepted.
- Skills uses six API-aware groups/fallbacks with typed Framer Motion and visible defaults so anchor navigation cannot strand content at zero opacity.

## Constraints

- Product guidance targets WCAG AA, keyboard access, readable responsive typography, purposeful motion, and reduced-motion support.
- Current Hero uses CMS headline/social URLs but some displayed availability/location copy is hardcoded.
- Multiple overlapping animation, carousel, component, and 3D systems increase maintenance/bundle risk.
- No focused tracked Hero/About tests were found.
- A passing compile/build does not establish live visual acceptance; restart the dev server and verify the rendered result after alias or component-integration changes.
- Current Skills and Featured Projects need explicit reduced-motion behavior and focused anchor/carousel tests; current static motion code is not the same as accepted navigation-trigger behavior.

## Decisions And Rationale

The Hero/availability strip, CMS-driven About, Skills, and Featured Projects evolved through repeated visual correction. Dark/off-brand panels, copied reference layouts, a constrained global rail, decorative-only collage, mounted Threads background, oversized/sticky cards, lead/supporting cards, Gallery Hover Carousel, coverflow/enlarged-slide Swiper, and an over-designed glowing CTA were superseded. Current light hierarchy, responsive About, six-group motion-enabled Skills, equal-card Swiper transport, established hover details, and background-only project polish outrank those experiments.

## Verification Expectations

Run generation, lint, focused Hero/About/query tests, full tests, and build. Start backend/client and verify desktop, mobile, tablet, and ultra-wide behavior; no horizontal overflow; keyboard/focus paths; contrast; reduced motion; image/asset loading; console/network state; CTA clickability; and public visibility behavior.

## Evidence

- Clean `main@d54e1e4466d9`, current package/config/router/Apollo/Home/Hero/About/PRODUCT/design-instruction structure.
- Three focused UI records plus the initial build record reconciled in [[../sources/portfolio-project-knowledge-harvest-batch-1|Portfolio Project Knowledge Harvest — Batch 1]].
- Direct Hermes records `20260622_134719_b462b2`, duplicate shell `20260622_222345_4a9915`, and substantive repair continuation `20260622_222345_5303fa` in [[../sources/portfolio-featured-projects-hermes-chain|Portfolio Featured Projects Hermes Chain]].
- Four substantive records plus the already-classified undo shell in [[../sources/portfolio-carousel-skills-livelycura-hermes-supplement|Portfolio Carousel, Skills, And LivelyCura Hermes Supplement]] split ownership of the accepted Swiper baseline, Skills foundation/motion, and Featured Projects interaction preservation.

## Contradictions

- A dedicated comprehensive About page was intended, but current source has no About route and the home section is richer than the original teaser.
- Current `Home` passes skills/resume data to About, but current About does not visibly render every supplied field.
- Threads remains in source but is no longer mounted in Hero; About image exports remain but are not actively used.
- Historical builds alternated between passing and being blocked by unrelated TypeScript errors; no current command was run.
- The Hermes parent ended on an unresolved Gallery import failure; the final child repaired compile-time imports and reported a Vite build, but did not prove restarted live runtime and ended on a new unanswered visual rejection.
- Generic Gallery/Embla primitives remain present but are not imported by the active Swiper Featured Projects section.
- Historical Vite-only passes did not close the full TypeScript build, and Skills navigation-trigger animation lacks explicit user acceptance.
- The current design contract discourages repetitive scaffolding and invented metrics, so future changes should review current numbered/stat treatments against that guidance.

## Confidence

High for static current composition and historical corrections; medium-high for runtime behavior because no current build or browser verification was executed.

## Open Questions

- Is a dedicated About route still desired?
- Should hardcoded hero availability/location copy use the available CMS data?
- Which dormant animation/assets can be removed safely?
- What deployment, performance-budget, and focused test contracts should be added?