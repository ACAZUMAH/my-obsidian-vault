---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [software-development, project-knowledge, codex, scaffolding]
sources:
  - ../../raw/sources/2026-07-21-project-knowledge-completion-and-bootstrap-directive.md
confidence: high
---

# Project Knowledge Completion And Bootstrap Directive

## Source

- Raw file: [2026-07-21-project-knowledge-completion-and-bootstrap-directive.md](../../raw/sources/2026-07-21-project-knowledge-completion-and-bootstrap-directive.md)
- Date: 2026-07-21
- Author: User
- Ingested: 2026-07-21

## Core Claims

- The current Project Knowledge synthesis is incomplete because earlier promotion relied mainly on Hermes memory rather than Codex history and all live repositories.
- Codex should perform a staged, evidence-preserving harvest across accessible conversations and projects.
- The shared brain needs a separate operating manual for making backend, web, and mobile projects structurally complete and runnable before feature implementation.
- A project “spin up” means a working engineering foundation, not placeholder files or a minimal screen.

## Useful Details

### Recoverable evidence located

- Codex thread index: `/Users/acazumah/.codex/session_index.jsonl` with 67 indexed threads at inspection time.
- Codex transcript stores: `/Users/acazumah/.codex/sessions/` and `/Users/acazumah/.codex/archived_sessions/`; 77 JSONL transcript/index files were located at inspection time.
- Project roots: `/Users/acazumah/Documents/`; 39 `package.json` manifests were located at inspection time, excluding no projects but including some dependency copies that a harvest must filter.
- Representative project families include LivelyCura, CompFlow, Kusantec/Bora, C.E.Q.A/Altin, Portfolio, and smaller standalone applications.

### Existing scaffolding evidence consulted

- Coder-profile `project-scaffolding-workflows` skill and its full-stack correction, CompFlow portal, mobile-module, and Docker references.
- `LivelyCura/livelycura-backend/package.json`.
- `compFlow/compflow-backend/package.json` and server startup files.
- `compFlow/compflow-admin/package.json` and source layout.
- `C.E.Q.A/altin-partner-mobile/package.json`, `AGENTS.md`, and source layout.

### Coverage boundary

This source does not claim that all Codex conversations have already been ingested. It establishes where they live and defines the need for bounded, resumable harvesting. Live repositories remain the authority for current implementation; conversations supply intent, corrections, rationale, and historical decisions.

## Connections

- [[../concepts/codex-project-knowledge-harvest|Codex Project Knowledge Harvest]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../entities/codex|Codex]]

## Contradictions Or Tensions

- Historical conversations can describe superseded implementations. They must not silently override newer code or later user corrections.
- A comprehensive harvest must avoid credentials, `.env` values, auth files, generated output, dependency trees, and temporary task state.

## Open Questions

- Which project family should be harvested first after the initial inventory: LivelyCura, CompFlow, Kusantec/Bora, C.E.Q.A/Altin, or Portfolio?
- Which conventions are universal across project families and which should remain project-specific?
