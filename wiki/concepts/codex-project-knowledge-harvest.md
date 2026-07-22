---
type: concept
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [codex, project-knowledge, ingestion, second-brain]
sources:
  - ../sources/project-knowledge-completion-and-bootstrap-directive.md
  - ../sources/hermes-conversation-harvest-scope-correction.md
  - ../sources/hermes-project-bootstrap-git-continuation-batch-1.md
confidence: high
---

# Codex Project Knowledge Harvest

## Working Definition

A Codex project-knowledge harvest is a bounded, resumable process that compares live repositories with historical Codex conversations and promotes only durable, sourced knowledge into the canonical Obsidian vault.

It is not a bulk transcript summary. Repositories provide current implementation evidence; conversations provide intent, corrections, rejected approaches, rationale, and conventions that code alone cannot explain.

The initial procedure and bootstrap artifacts were produced and focused-validated in default-profile Hermes continuation `20260721_001007_1b1aea`. That session created the machinery but explicitly did not complete full archive ingestion; later family batches remain independent evidence.

## Current Synthesis

### Archive scope is part of provenance

Use this procedure only when Codex conversations are explicitly requested. A Hermes-conversation harvest must search Hermes history instead. In either case, a discovered repository without a directly relevant conversation cannot independently justify a conversation-derived project page or durable claim; repository inspection verifies current implementation after conversation scope is established.

### Why the harvest must be staged

The local archive contains dozens of Codex sessions and project manifests. Feeding everything into one context would cause omissions, weak provenance, duplicated pages, and accidental hardening of stale claims. Each run should process one project family or at most eight relevant sessions, update a checkpoint, and stop with a clear next batch.

### Source precedence

When evidence conflicts, preserve the disagreement and use this decision order:

1. The latest explicit user correction defines the desired convention.
2. Live repository code and current repository instructions define current implementation reality.
3. Recent successful session outcomes explain why the current implementation exists.
4. Older conversations are historical evidence, not current truth.
5. Agent inference is labeled as inference and never promoted as a user preference without support.

### Knowledge classifications

Every promoted claim should be identified as one of:

- **User-stated convention** — explicitly requested or corrected by the user.
- **Observed implementation** — currently present in a repository.
- **Repeated pattern** — observed in at least two relevant repositories or sessions.
- **Project-specific decision** — applies only to one product or repository.
- **Inference** — plausible but not yet confirmed.
- **Unknown** — evidence is incomplete or contradictory.

## Paste-Ready Master Prompt For Codex

Open Codex with `/Users/acazumah/Documents` as the workspace so it can inspect the project families and write into the nested `Work Space` vault. Then paste this prompt:

```text
Perform a staged, provenance-preserving project-knowledge harvest into my canonical Obsidian brain.

Canonical vault:
/Users/acazumah/Documents/Work Space

Read first:
- /Users/acazumah/Documents/Work Space/AGENTS.md
- /Users/acazumah/Documents/Work Space/index.md
- /Users/acazumah/Documents/Work Space/log.md
- /Users/acazumah/Documents/Work Space/wiki/syntheses/software-development-operating-manual.md
- /Users/acazumah/Documents/Work Space/wiki/syntheses/new-project-bootstrap-operating-manual.md
- /Users/acazumah/Documents/Work Space/wiki/concepts/codex-project-knowledge-harvest.md

Evidence locations:
- /Users/acazumah/Documents — live repositories and project files
- /Users/acazumah/.codex/session_index.jsonl — Codex thread names and IDs
- /Users/acazumah/.codex/sessions — active Codex rollout transcripts
- /Users/acazumah/.codex/archived_sessions — archived Codex rollout transcripts

Goal:
Complete the Project Knowledge in the software-development operating manual by discovering durable project architecture, conventions, commands, constraints, corrections, decisions, and rationale that are supported by live repositories and my Codex conversations.

Safety and scope rules:
1. Work read-only in project repositories. Write only inside the canonical Obsidian vault.
2. Never read, copy, summarize, or store secrets. Skip .env files, auth.json, tokens, credentials, certificates, private keys, connection strings, and secret-bearing config. Replace any accidentally encountered value with [REDACTED].
3. Exclude node_modules, vendor directories, build/dist output, coverage, caches, generated GraphQL files, binary assets, and ordinary tool chatter.
4. Do not install dependencies, run migrations, start production services, modify Git state, or change application code during this knowledge harvest.
5. Do not dump full conversations into Obsidian. Preserve only minimal sanitized evidence: session ID, date, working directory, thread title, short relevant user quotations when safe, and extracted durable claims.
6. Historical conversations can be stale. Verify implementation claims against current repository files. Preserve contradictions instead of silently choosing one.
7. The latest explicit user correction outranks older conversation assumptions. Live code establishes current behavior; conversation evidence explains intent and rationale.
8. Reread every shared vault note immediately before editing it. Use focused anchored edits because Hermes and other Codex sessions may edit the vault concurrently.
9. Do not create a project page solely because a repository exists. A conversation-harvest page requires a directly relevant conversation unless the user separately requests repository-inventory knowledge.

Batching:
- Do not process the entire archive in one run.
- Process one project family OR at most 8 relevant Codex sessions per run.
- Prefer this family order unless the checkpoint says otherwise: LivelyCura, CompFlow, Kusantec/Bora, C.E.Q.A/Altin, Portfolio, then standalone projects.
- Create or update /Users/acazumah/Documents/Work Space/wiki/syntheses/project-knowledge-harvest-status.md with discovered projects, transcript IDs, completed batches, pending batches, conflicts, and next action.

For the current batch:
1. Inventory the selected project family: repositories/apps, purpose, stack, package manager, runtime, local commands, deployment files, architecture, and repository instructions.
2. Match Codex sessions to the family using session cwd, thread title, and mentioned repository paths.
3. Extract only durable user preferences, corrections, architecture decisions, do-not-change rules, successful verification patterns, and project-specific domain knowledge.
4. Verify each implementation claim against current package.json, README/AGENTS.md, config, and representative source files.
5. Create or update one project page per directly conversation-supported repository under wiki/projects/<project-slug>.md with frontmatter `type: project`. Do not create pages for unmatched roots. Include: Summary, Purpose, Stack, Architecture, Folder Ownership, Commands, Runtime/Deployment, Durable Conventions, Constraints, Decisions And Rationale, Verification Expectations, Evidence, Contradictions, Confidence, and Open Questions.
6. Create one sanitized batch evidence manifest under raw/sources/ and one source summary under wiki/sources/. The manifest must contain provenance, not full transcripts or secrets.
7. Update software-development-operating-manual.md only with cross-project rules and a compact project map. Keep detailed facts in the project pages.
8. Update new-project-bootstrap-operating-manual.md only when the batch proves a reusable scaffolding convention. Label project-specific alternatives instead of forcing one default.
9. Update index.md and append exactly one new entry at the top of log.md.
10. Validate touched frontmatter and real wikilinks. Ignore literal example links inside code.

Final report:
- Project family and transcript IDs processed.
- Files created or updated.
- New durable knowledge promoted.
- Contradictions or uncertain claims.
- Exact checkpoint and recommended next batch.

Begin by reading the checkpoint if it exists. If it does not exist, create the inventory and process only the first bounded batch. Continue autonomously within that batch; do not ask me to restate information available in the repositories or transcripts.
```

## Resume Prompt

After the first batch, this shorter prompt is enough:

```text
Resume the staged Codex project-knowledge harvest from:
/Users/acazumah/Documents/Work Space/wiki/syntheses/project-knowledge-harvest-status.md

Follow /Users/acazumah/Documents/Work Space/AGENTS.md and the full procedure in [[wiki/concepts/codex-project-knowledge-harvest]]. Process exactly the next pending project-family batch, preserve provenance, redact secrets, update project pages plus the two operating manuals only where supported, validate links, update the checkpoint, and append exactly one log entry.
```

## Supporting Sources

- [[../sources/project-knowledge-completion-and-bootstrap-directive|Project Knowledge Completion And Bootstrap Directive]]
- [[../sources/hermes-conversation-harvest-scope-correction|Hermes Conversation Harvest Scope Correction]]
- [[../sources/hermes-project-bootstrap-git-continuation-batch-1|Hermes Project Bootstrap And Git Continuation — Batch 1]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]

## Related

- [[hermes-obsidian-memory-architecture|Hermes–Codex–Obsidian Shared Brain Architecture]]
- [[../entities/codex|Codex]]
- [[persistent-compounding-wiki|Persistent Compounding Wiki]]

## Open Questions

- Whether a later scheduled job should continue batches automatically after the manual workflow proves reliable.
- Whether project pages should remain repository-scoped or add product-family overview pages above them.
