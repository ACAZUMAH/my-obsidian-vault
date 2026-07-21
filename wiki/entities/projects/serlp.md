---
type: entity
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, serlp, marketing, web, seo]
sources:
  - ../../sources/livelycura-project-knowledge-harvest-batch-1.md
confidence: high
---

# SERLP

## Summary

Public website and brand/SEO surface for the general-purpose SERLP ERP platform.

## Purpose

Explains the product, industries, modules, pricing, trust, integrations, resources, and conversion paths while serving crawler-friendly metadata and HTML.

## Stack

- TypeScript, React 19, Vite 8, React Router 7.
- Mantine 9, CSS modules.
- Vitest, ESLint, Prettier.
- Static SPA plus a top-level SSR renderer package.
- Yarn.

## Architecture

The user-facing application is a static Vite SPA. Crawler rendering lives only in top-level `ssr/`. Route and SEO data are shared so SPA and SSR title, description, canonical, and Open Graph output remain aligned.

## Folder Ownership

- Domain/page folders live directly under `src`; do not add `src/pages`.
- Meaningful domains own local components, hooks, helpers, interfaces, styles, and tests.
- `src/app`, `router`, `components`, `constants`, `helpers`, `hooks`, `layouts`, `styles`, and `interfaces` own broad shared concerns.

## Commands

- `yarn start`
- `yarn test`, `yarn lint`, `yarn format:check`
- `yarn build`
- `yarn ssr`, `yarn build:ssr:local`

## Runtime/Deployment

Production canonical domain is `https://serlp.com`; staging is `https://staging.serlp.com`. GitHub workflows cover CI, staging, semantic release/SSR package publishing, and production deployment.

## Durable Conventions

- SERLP is public marketing/product storytelling, not the ERP portal.
- Keep SSR simple: no Apollo, Redux, data prefetch, or `src/ssr-safe` layer.
- Read project product/design references before changing copy, layout, pricing, modules, or style.
- Preserve an operational, modern, trustworthy, cross-industry brand and avoid generic decorative SaaS patterns.

## Constraints

- Backend services and crawler-routing infrastructure are outside this repository.
- Route, metadata, shared data, CSS-loading, and SSR changes require SSR verification.

## Decisions And Rationale

A static SPA plus narrowly scoped crawler renderer keeps the public experience interactive while preserving crawlable metadata without importing application state complexity into SSR.

## Verification Expectations

For TypeScript/routes run lint, tests, and build. For SEO/shared data/SSR/CSS delivery also run `build:ssr:local`. Inspect desktop and mobile for overlap, overflow, dropdowns, and cramped actions.

## Evidence

- Current `AGENTS.md`, package, README, source/SSR layout, and GitHub workflows.
- [[../../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].

## Contradictions

README status calls the repository an initial setup, but current source, package version, domains, SSR, and deployment workflows show a developed site. Current files are authoritative.

## Confidence

High; repository instructions are explicit and consistent with current structure.

## Open Questions

- Which product claims and pricing decisions remain deliberately staged versus production?
