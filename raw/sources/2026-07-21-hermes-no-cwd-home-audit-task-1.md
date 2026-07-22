## Sanitized read-only evidence report

**Scope:** exactly two sessions from `/Users/acazumah/.hermes/profiles/coder/state.db`, opened with SQLite read-only mode. Evidence after the **2026-07-21 17:12:06 GMT cutoff** was excluded.

### 1. `20260621_005833_de3cc9`

| Field | Finding |
|---|---|
| Profile | `coder` store; legacy row has no `profile_name` value |
| Date | 2026-06-21 00:59 UTC |
| Historical cwd | `/Users/acazumah` |
| Indexed title | `Hermes Model Identification` |
| Source / archive state | `tui`; active (`archived=0`) |
| Classification | **duplicate** |
| Promotion status | **reference-only** — supports existing knowledge; no new promotion recommended |
| Confidence | **Medium-high** — the preference is explicit, but its deliberately broad wording does not establish detailed operating authority |
| Target repository | None; this was a personal workflow preference, not project work |
| Minimal safe quotation | None |

**Actual request and durable evidence**

- After asking which model was active, the user established Hermes as a continuing software-engineering counterpart or “second self.”
- This supports a durable preference for sustained engineering partnership rather than isolated question answering.
- The assistant expanded that role into architecture, debugging, review, and production-quality support. Those details are assistant interpretation, not separate explicit user constraints.

**Transcript-reported outcome and verification**

- The session’s memory tool reported that one preference operation was successfully applied.
- The assistant acknowledged the continuing engineering-partner role.
- No repository change, build, test, or runtime verification occurred.
- The historical memory write is evidence of acknowledgement, **not** evidence that the preference was promoted into Obsidian.

**De-duplication against the vault**

The durable meaning is already covered more strongly by:

- `wiki/syntheses/personal-operating-manual.md` — canonical second-brain and working-preference rules.
- `wiki/sources/hermes-obsidian-second-brain-kickoff.md`.
- `wiki/sources/shared-brain-all-agents-directive.md`.
- `wiki/syntheses/software-development-operating-manual.md` — communication and execution agreements.

The exact session ID currently appears only in the metadata coverage manifest, not as independently promoted evidence.

**Contradiction / boundary**

- “Second self” must not be interpreted as unlimited authority to make changes. Later explicit rules require scoped action and, for review-gated work, explicit authorization before continuing.

**Reusable rule**

- Supports the existing engineering-partner/second-brain stance; adds no new reusable rule.

**Recommended vault action**

- Mark the ID classified in the harvest checkpoint.
- At most, attach it as supporting provenance to the Personal Operating Manual; do not create a new page or duplicate the existing rule.

---

### 2. `20260721_164555_84be3a`

| Field | Finding |
|---|---|
| Profile | `coder` |
| Date | Session metadata starts 2026-07-21 16:48 UTC; first in-scope user request was at 17:08 UTC |
| Historical cwd | `NULL` / no cwd |
| Indexed title | `Approved Wiki Project Cleanup` |
| Source / archive state | `unknown`; active (`archived=0`) |
| Classification | **process-control** |
| Promotion status | **reference-only** for the durable correction already captured in the vault; **incomplete** for the requested audit outcome at the cutoff |
| Confidence | **High** |
| Target repository | None; the canonical vault and Hermes archive process were the subjects |
| Minimal safe quotation | None |

**Actual request and durable correction**

- The user challenged the claim that Hermes knowledge had been fully harvested because project pages appeared primarily Codex-derived.
- The durable correction is that:
  - Hermes and Codex histories are separate evidence archives even when the same agent/model is used.
  - Stored sessions and compact memory do not equal vault integration.
  - Direct Hermes conversation evidence must be audited and promoted deliberately.
  - Completion claims must reflect actual archive coverage.

**Outcome at the snapshot cutoff**

Before **17:12:06 GMT**, the session had:

- Read the vault governance, operating manuals, checkpoint, and relevant harvesting rules.
- Inspected the coder and default Hermes state stores read-only.
- Confirmed that the two stores were separate and that substantial unclassified history remained.
- Dispatched three read-only project-family evidence workers.

At the cutoff:

- The delegated workers had not returned.
- There was no final assistant outcome.
- There was no completed promotion, checkpoint update, or vault validation attributable to the in-scope portion.
- Later messages and resulting work exist in the live database, but they are post-cutoff and were deliberately excluded.

**De-duplication against the current vault**

The durable process correction is now already represented by:

- `wiki/sources/hermes-session-coverage-audit-2026-07-21.md`.
- `wiki/syntheses/project-knowledge-harvest-status.md`.
- `wiki/syntheses/personal-operating-manual.md`.
- `wiki/concepts/hermes-obsidian-memory-architecture.md`.
- The immutable metadata manifest `raw/sources/2026-07-21-hermes-session-coverage-audit.md`.

Therefore, this session adds no new project claim. Its primary value is process-control provenance and checkpoint classification.

**Contradictions / boundaries**

- The indexed title suggests an approved cleanup, but the actual user request was a Hermes-coverage correction and audit challenge.
- Same agent identity does not merge Hermes and Codex archives.
- The current vault documents a completed later coverage audit, but that later state must not be presented as this session’s completed outcome at the stated cutoff.

**Reusable rule**

- Supports the existing rule that archive-specific conversation evidence is required before claiming knowledge-harvest completion; adds no new reusable rule.

**Recommended vault action**

- Mark the session ID classified as process-control.
- Retain the existing coverage-audit and checkpoint pages as the canonical targets.
- Do not promote it to any project page.
- Preserve the cutoff distinction if adding exact-session provenance.

## Completion

- **Exact IDs processed:** 2 of 2.
- **Classifications:** 1 duplicate; 1 process-control.
- **Promotion results:** no new durable rule; one reference-only preference record; one process correction already captured, with its cutoff-time execution incomplete.
- **Logical locator:** `/Users/acazumah/.hermes/profiles/coder/state.db` → `sessions.id` and `messages.session_id`.
- **Verification:** historical session evidence plus current static vault de-duplication only; no builds, tests, services, or project repositories were exercised.
- **Sanitization:** no system prompts, full transcripts, secrets, environment values, private payloads, or tool chatter reproduced.
- **Files created or modified:** **none**.
- **Issue encountered:** the vault working tree was already heavily dirty from pre-existing or concurrent work, so Git status cannot establish a clean baseline. This audit used only read operations and `sqlite3 -readonly`; it made no file changes.