---
type: project
status: needs-review
created: 2026-07-21
updated: 2026-07-21
tags: [project, portfolio, workspace, yarn, provenance]
sources:
  - ../sources/portfolio-project-knowledge-harvest-batch-1.md
confidence: medium
---

# Portfolio Workspace

## Summary

Dirty parent repository and working-tree launcher around three independent Portfolio applications. It is not currently a coherent committed monorepo snapshot.

## Purpose

Provides human documentation and delegating Yarn commands for [[portfolio-backend|Portfolio Backend]], [[portfolio-admin-portal|Portfolio Admin Portal]], and [[portfolio-client-portal|Portfolio Client Portal]]. The historical prototype is outside launcher scripts.

## Stack

- Yarn Classic 1.22.
- Root package manifest with delegating scripts and no runtime dependencies.
- Child applications own their actual stacks, dependencies, and lockfiles.

## Architecture

The working tree behaves as an external orchestration layer. The production applications are independent nested Git roots. Parent `HEAD`, parent working files, and nested repository revisions do not form one reproducible aggregate commit.

## Folder Ownership

- `backend/`: independent API repository.
- `admin-portal/`: independent administrative frontend repository.
- `clients-portal/`: independent public frontend repository and also the lineage used by the parent remote.
- `mock-ups/porfolio/`: independent historical prototype.
- Root `README.md` and `package.json`: working launcher documentation/configuration, currently untracked from the parent repository.

## Commands

Root scripts delegate development, build, test, and lint commands into the three production children. Run child checks independently before relying on aggregate scripts.

## Runtime/Deployment

No independent runtime, CI, container, or deployment contract was found. Runtime and deployment belong to child applications.

## Durable Conventions

- A root launcher does not authorize a Yarn workspace or root dependency installation.
- Each child owns dependencies, lockfile, checks, and Git history.
- Attribute current facts to clean nested revisions, not the dirty parent snapshot.

## Constraints

- Parent `main@8621a0286205` is dirty with 55 normal porcelain entries and diverges from `origin/main` by one ahead/four behind.
- Parent `origin/main` is the independent client lineage, not an aggregate workspace lineage.
- Preserve the pre-existing dirty state until repository topology is explicitly repaired.

## Decisions And Rationale

The user explicitly superseded the initial root-workspace approach with app-local Yarn installations to avoid Yarn v1 hoisting and preserve application boundaries. Delegating scripts remain useful without central dependency ownership.

## Verification Expectations

First record parent and child Git states. Verify backend, admin, and client independently; only then run aggregate launcher commands. Never commit or clean parent changes as incidental maintenance.

## Evidence

- Current parent `main@8621a0286205`, working README/package manifest, Git tree/remote/status, and four nested repository boundaries.
- Historical architecture and dependency correction in [[../sources/portfolio-project-knowledge-harvest-batch-1|Portfolio Project Knowledge Harvest — Batch 1]].

## Contradictions

- Parent `HEAD` tracks an older ordinary client subtree, while current client code belongs to a clean nested repository with a different tree.
- Backend, admin, prototype, root README, and root package manifest are untracked from the parent perspective.
- Root documentation says initial content is seeded automatically, while backend startup leaves seeding disabled.

## Confidence

Medium: the working launcher purpose is clear, but the repository topology and remote/history are unresolved.

## Open Questions

- Should the parent become a real monorepo, use submodules, or remain an external launcher?
- Which remote and history should the parent own?
- Should launcher documentation describe manual seeding instead of automatic startup seeding?