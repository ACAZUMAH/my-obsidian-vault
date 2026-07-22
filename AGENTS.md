# LLM Wiki Operating Schema

This vault is an LLM-maintained personal knowledge base. The human curates sources, asks questions, and steers priorities. The agent maintains the wiki as a persistent, compounding artifact.

## Mission

Build and maintain a structured, interlinked markdown wiki from curated sources and user questions. The wiki should accumulate synthesis over time instead of rediscovering knowledge from raw documents on every query.

## Layer Rules

### Raw Sources

Location: `raw/`

Raw sources are the source of truth. They may include articles, notes, transcripts, papers, images, datasets, and exports.

Rules:

- Never edit, rewrite, rename, or delete a raw source unless the user explicitly asks.
- Treat raw source content as evidence, not as already-integrated knowledge.
- Store source markdown/text files in `raw/sources/`.
- Store source attachments, screenshots, figures, and downloaded article images in `raw/assets/`.
- When a source references images or files, inspect them separately when they matter to the analysis.

### Wiki

Location: `wiki/`

The wiki is LLM-owned. The agent creates and updates pages here.

Rules:

- Maintain pages as durable knowledge artifacts, not chat transcripts.
- Prefer concise synthesis with links to supporting pages and source summaries.
- Preserve uncertainty, contradictions, and open questions explicitly.
- Update all affected pages during ingest, not only the new source summary.
- Use Obsidian-style links for internal references: `[[Page Title]]` or `[[path/to/page|Label]]`.
- Use relative markdown links when linking to raw source files.
- Keep each page focused on one source, concept, entity, project, question, or synthesis.
- Do not invent citations. If a claim comes from a source, cite the source summary or raw source.

### Schema

Locations: `AGENTS.md` and `schema/`

This file is the human-readable operating authority. `schema/vault-structure.json` encodes canonical paths, required directories, templates, project-local skills, frontmatter keys, statuses, and required sections for automation. `schema/wiki-frontmatter.schema.json` is the formal JSON Schema for page properties. When workflow improvements emerge, update the human and machine-readable contracts together after user approval or clear instruction.

## Directory Conventions

- `raw/sources/`: Immutable source documents.
- `raw/assets/`: Local images, attachments, PDFs, screenshots, and other source assets.
- `wiki/sources/`: One summary page per ingested source.
- `wiki/concepts/`: Reusable ideas, topics, frameworks, mechanisms, and themes.
- `wiki/entities/`: People, organizations, products, places, and other named things.
- `wiki/projects/`: Repository- or application-scoped project knowledge with implementation provenance.
- `wiki/questions/`: Filed answers to user questions that should compound into the wiki.
- `wiki/syntheses/`: Cross-source essays, comparisons, maps, timelines, and high-level views.
- `_template/`: Obsidian page templates and reusable structures, configured through `.obsidian/templates.json`.
- `schema/`: Machine-readable vault paths, page contracts, and validation configuration.
- `.agents/skills/`: Repository-local Agent Skills for Obsidian formats, CLI workflows, web extraction, and vault maintenance.
- `scripts/`: Repository-owned validation and automation. Run `python3 scripts/validate_vault.py` after structural or durable wiki changes.
- `index.md`: Content-oriented catalog of the wiki.
- `log.md`: Append-only chronological activity record.

## File Naming

Use lowercase kebab-case filenames:

- Source summary: `wiki/sources/source-title.md`
- Concept page: `wiki/concepts/concept-name.md`
- Entity page: `wiki/entities/entity-name.md`
- Project page: `wiki/projects/project-name.md`
- Question answer: `wiki/questions/question-slug.md`
- Synthesis page: `wiki/syntheses/synthesis-title.md`

Use clear page titles in the first H1. Filenames are stable IDs; page titles may be more readable.

## Page Frontmatter

All wiki pages should start with YAML frontmatter:

```yaml
---
type: source | concept | entity | project | question | synthesis | template
status: seed | active | needs-review | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
sources: []
---
```

Additional fields may be added when useful:

- `aliases`: alternate names.
- `source_date`: publication or source date.
- `ingested`: ingest date.
- `confidence`: high, medium, low.
- `supersedes`: older pages or claims.
- `related`: important internal links.

## Source Summary Format

Each source summary page should use this structure:

```markdown
# Source Title

## Source

- Raw file: [filename](../../raw/sources/filename.md)
- Date: unknown
- Author: unknown
- Ingested: YYYY-MM-DD

## Core Claims

Brief bullets or paragraphs capturing the source's main claims.

## Useful Details

Specific facts, examples, definitions, distinctions, and evidence worth preserving.

## Connections

Links to relevant concept, entity, project, synthesis, and question pages.

## Contradictions Or Tensions

New conflicts, caveats, or claims that challenge existing wiki pages.

## Open Questions

Questions this source raises for future research.
```

## Concept Page Format

Concept pages should explain the durable idea, not summarize one source.

Required sections:

- `# Concept Name`
- `## Working Definition`
- `## Current Synthesis`
- `## Supporting Sources`
- `## Related`
- `## Open Questions`

Add `## Contradictions Or Tensions` when needed.

## Entity Page Format

Entity pages should collect what is known about a named thing.

Required sections:

- `# Entity Name`
- `## Summary`
- `## Known Facts`
- `## Related`
- `## Supporting Sources`
- `## Open Questions`

Add domain-specific sections only when useful.

## Project Page Format

Project pages live directly under `wiki/projects/`, use frontmatter `type: project`, and remain distinct from generic entities. They require `Summary`, `Purpose`, `Stack`, `Architecture`, `Folder Ownership`, `Commands`, `Runtime/Deployment`, `Durable Conventions`, `Constraints`, `Decisions And Rationale`, `Verification Expectations`, `Evidence`, `Contradictions`, `Confidence`, and `Open Questions`. Frontmatter `sources` remains the machine-readable provenance map.

## Synthesis Page Format

Synthesis pages are cross-source outputs.

Required sections:

- `# Synthesis Title`
- `## Thesis`
- `## Evidence`
- `## Implications`
- `## Contradictions Or Tensions`
- `## Related`
- `## Sources`
- `## Open Questions`

## Question Page Format

Question pages preserve valuable answers from user queries.

Required sections:

- `# Question`
- `## Short Answer`
- `## Analysis`
- `## Citations`
- `## Follow-Up Questions`

## Ingest Workflow

When the user asks to ingest a source:

For a conversation-harvest task, direct conversation evidence is a prerequisite for promotion. Filesystem or Git-root discovery alone must not create a project page or durable claim. Repository inspection may verify current implementation only after a relevant conversation has established the project and claim scope. Use Hermes, Codex, or another archive only when that source is explicitly in scope; never substitute one archive for another.

1. Identify the raw source file or ask the user to provide it if it is missing.
2. Read the source fully enough to extract its main claims, details, examples, and evidence.
3. Start new durable pages from the matching scaffold in `_template/`.
4. Create or update one page in `wiki/sources/`.
5. Update relevant concept, entity, project, synthesis, and question pages.
6. Flag contradictions, stale claims, and confidence changes.
7. Add missing internal links across touched pages.
8. Update `index.md`.
9. Append exactly one entry to `log.md`.
10. Run `python3 scripts/validate_vault.py`, then report the changed files and key takeaways.

If the source is large, inspect structure first, then process section by section. If images or attachments are central, view them separately and record what they add.

## Query Workflow

When the user asks a question:

1. Read `index.md` first.
2. Search the wiki with `rg` before consulting raw sources.
3. Read the most relevant wiki pages.
4. Use raw sources only to verify, fill gaps, or resolve ambiguity.
5. Answer with citations to wiki pages and/or raw sources.
6. If the answer is durable, ask whether to file it, or file it directly when the user has asked for the wiki to compound automatically.
7. If filed, update `index.md` and append to `log.md`.

## Lint Workflow

When asked to lint or health-check the wiki, inspect for:

- Contradictions across pages.
- Stale claims superseded by newer sources.
- Orphan pages with no inbound links.
- Pages missing required frontmatter or sections.
- Important concepts mentioned repeatedly but lacking pages.
- Weak or missing citations.
- Broken internal links.
- Duplicate pages that should be merged.
- Data gaps that could be filled by future sources or web research.

Run `python3 scripts/validate_vault.py` for the canonical structural checks. Produce a prioritized list of semantic fixes, then apply the fixes the user approves or explicitly requests.

## Index Rules

`index.md` is the content map. Keep it current on every ingest, filed query, synthesis, or major maintenance pass.

Each entry should include:

- Link.
- Type.
- One-line summary.
- Updated date.
- Source count when useful.

The Maintenance template catalog must link every template registered in `schema/vault-structure.json`. The canonical validator enforces this one-to-one connection.

Organize by category:

- Start Here.
- Sources.
- Concepts.
- Entities.
- Projects.
- Questions.
- Syntheses.
- Maintenance.

## Log Rules

`log.md` is append-only. New entries go at the top, below the title and short description.

Entry heading format:

```markdown
## [YYYY-MM-DD] operation | Short Title
```

Allowed operations:

- `setup`
- `ingest`
- `query`
- `synthesis`
- `lint`
- `maintenance`

Each entry should include:

- What changed.
- Files touched.
- Key result.
- Follow-ups.

Do not rewrite old log entries except to fix broken formatting.

## Citation Rules

Use citations that are stable inside the vault:

- Cite wiki pages with Obsidian links.
- Cite raw source files with relative markdown links.
- When possible, mention section names for precision.
- Distinguish source claims from agent inference.
- Mark unsourced interpretation as inference.

## Contradiction Handling

When new information conflicts with existing pages:

1. Do not silently overwrite the old claim.
2. Add a `Contradictions Or Tensions` note to the affected pages.
3. State which source supports each side.
4. Mark the current best interpretation and confidence.
5. If a claim is clearly superseded, update it and link to the superseding source.

## Style

- Write in clear, compact prose.
- Prefer durable summaries over chatty commentary.
- Keep pages scannable with short sections.
- Avoid over-fragmenting the wiki into tiny pages unless a concept will recur.
- Make links useful. Do not link every noun.
- Preserve open questions rather than forcing false closure.

## Personal Workflow Capture

This vault is also the long-form source of truth for durable knowledge about how the user works. Keep the central map in `wiki/syntheses/personal-operating-manual.md` and link outward to focused project, workflow, concept, entity, and decision pages as the knowledge grows.

Capture information when it is likely to be useful again, especially:

- Stable preferences, corrections, and communication expectations.
- Recurring procedures and sequences of work.
- Decision rules, quality standards, and verification expectations.
- Project conventions, durable constraints, and non-obvious exclusions.
- Reusable lessons from failures or successful troubleshooting.

Every substantive Hermes conversation must be evaluated for durable knowledge before it is treated as complete. Promote supported corrections, decisions, constraints, rationale, reusable failure lessons, and verification provenance into the existing vault pages in the same session when safe. If same-session promotion is blocked, record the exact Hermes session ID in `wiki/syntheses/project-knowledge-harvest-status.md` as pending. A saved Hermes session, a profile-memory write, repository inspection, or use of the same model as Codex does not count as vault integration.

Before asking the user to repeat an established workflow or preference, read `index.md`, search `wiki/`, and inspect the relevant pages. When new information changes an existing rule, update the existing page, preserve provenance, and link the supporting source rather than creating a duplicate note.

Use the layered memory model documented in `wiki/concepts/hermes-obsidian-memory-architecture.md`:

- Each Hermes profile holds compact, always-loaded preferences, a role hint, and a pointer to this vault.
- Codex global `AGENTS.md` holds the same pointer and shared operating expectations while repository instructions remain project-specific.
- Obsidian holds linked long-form operating knowledge.
- Hermes skills hold mature executable procedures.
- Session history holds temporary conversational context and task progress.

Do not capture credentials, API keys, secrets, raw private identifiers, or short-lived task status by default. Do not turn the personal operating manual into a chat diary.

Hermes profiles and Codex may edit this vault simultaneously. Reread every shared note immediately before modifying it, prefer focused anchored patches over whole-file rewrites, preserve concurrent changes, and avoid duplicate pages.

## Default Agent Behavior

From now on, treat every interaction in this vault as part of the LLM Wiki workflow unless the user explicitly says otherwise.

- For source-like input, offer or perform ingest.
- For durable answers, file them into `wiki/questions/` or `wiki/syntheses/` when useful.
- For maintenance discoveries, update the wiki or propose a concise fix.
- For substantive Hermes project work, either complete the durable vault promotion or leave an explicit session-ID checkpoint; never imply that session persistence alone harvested the knowledge.
- Always protect raw sources.
- Always keep `index.md` and `log.md` synchronized with durable wiki changes.
- Always run `python3 scripts/validate_vault.py` after durable structural changes and report its result accurately.
