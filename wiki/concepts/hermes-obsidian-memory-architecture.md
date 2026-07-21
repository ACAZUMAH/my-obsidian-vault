---
type: concept
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [hermes, codex, obsidian, memory, second-brain, multi-agent]
sources:
  - ../sources/hermes-obsidian-second-brain-kickoff.md
  - ../sources/shared-brain-all-agents-directive.md
  - ../sources/hermes-persistent-memory-import.md
aliases: [Hermes–Obsidian Memory Architecture]
confidence: high
---

# Hermes–Codex–Obsidian Shared Brain Architecture

## Working Definition

A multi-agent knowledge architecture in which Obsidian is the canonical long-form knowledge plane, while each Hermes profile and Codex carries a compact tool-native pointer that retrieves relevant context from the same indexed vault.

## Current Synthesis

### Canonical Knowledge Plane

The Obsidian vault at `/Users/acazumah/Documents/Work Space` is the durable source of truth for linked workflows, preferences, project conventions, decisions, corrections, reusable lessons, sources, contradictions, and syntheses.

The main retrieval path is:

1. `index.md` — content map.
2. `wiki/syntheses/personal-operating-manual.md` — user working preferences.
3. `wiki/syntheses/software-development-operating-manual.md` — development and project conventions.
4. Focused source, concept, entity, question, or synthesis pages linked from those maps.
5. Raw sources only when evidence or exact provenance is needed.

### Hermes Integration Layer

Every Hermes profile has:

- `OBSIDIAN_VAULT_PATH` configured in its profile environment;
- a compact `USER.md` containing shared communication and capture expectations;
- a compact `MEMORY.md` pointing to the canonical index and operating manuals;
- optional role-specific memory describing how that profile contributes without duplicating the vault.

Profiles retain specialization, but shared long-form knowledge is promoted to Obsidian instead of copied between profiles.

### Codex Integration Layer

Codex uses its officially supported global instruction chain:

- `~/.codex/AGENTS.md` provides the shared-brain pointer, retrieval and capture rules, communication style, and concurrency policy for every Codex run.
- `~/.codex/config.toml` exposes `OBSIDIAN_VAULT_PATH` to Codex shell environments.
- Repository and subdirectory `AGENTS.md` files layer project-specific rules over the global context and remain more specific.

### Skills And Session History

- Hermes skills hold mature executable procedures with exact steps, tools, pitfalls, and verification.
- Repository instructions hold project-local rules.
- Session history holds temporary conversation and task progress.
- None of these replaces the canonical long-form knowledge plane.

## Capture Threshold

Capture information when it is likely to be useful again, especially when the user:

- explains a recurring way of working;
- states a stable preference or correction;
- defines a decision rule or quality standard;
- establishes a project convention or non-obvious constraint;
- teaches a reusable procedure;
- resolves a recurring failure with a durable lesson.

Do not capture credentials, API keys, secrets, raw private identifiers, short-lived task progress, or ordinary chat noise by default. Update an existing page instead of creating a duplicate when the concept already exists.

## Retrieval Rule

Before asking the user to repeat an established workflow, preference, project convention, or decision, consult `index.md`, search the wiki, and read only the relevant pages. Current code and live system state remain authoritative for facts that may have changed.

## Concurrent Write Rule

Hermes profiles and Codex may run simultaneously. Before editing a shared note, reread its live contents. Prefer focused anchored patches, preserve concurrent changes, avoid whole-file rewrites when unnecessary, and keep `index.md` plus `log.md` synchronized with durable wiki operations.

## Failure Modes And Controls

- **Divergent profile memory:** promote shared facts to the vault and retain only pointers or role hints locally.
- **Stale project knowledge:** verify against live repositories and preserve uncertainty.
- **Vault noise:** apply the capture threshold and avoid task diaries.
- **Concurrent overwrite:** reread before editing and use narrow anchored changes.
- **Context overload:** retrieve relevant pages instead of injecting the entire vault into every prompt.
- **Instruction collision:** global shared-brain guidance yields to more specific repository and subdirectory instructions.

## Supporting Sources

- [[../sources/hermes-obsidian-second-brain-kickoff|Hermes–Obsidian Second Brain Kickoff]]
- [[../sources/shared-brain-all-agents-directive|Shared Brain Across Hermes Profiles And Codex]]
- [[../sources/hermes-persistent-memory-import|Hermes Persistent Memory Import]]

## Related

- [[persistent-compounding-wiki|Persistent Compounding Wiki]]
- [[raw-source-wiki-schema-architecture|Raw Source, Wiki, Schema Architecture]]
- [[ingest-query-lint-workflows|Ingest, Query, Lint Workflows]]
- [[../entities/hermes-agent|Hermes Agent]]
- [[../entities/codex|Codex]]
- [[../entities/obsidian|Obsidian]]
- [[../syntheses/personal-operating-manual|Personal Operating Manual]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]

## Open Questions

- When should a workflow graduate from a wiki page into a Hermes or Codex-operable skill?
- At what edit volume would the shared vault benefit from a coordinated write queue or conflict detector?
