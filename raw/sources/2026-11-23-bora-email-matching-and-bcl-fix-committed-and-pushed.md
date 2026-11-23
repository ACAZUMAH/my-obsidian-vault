# Bora: email matching and BCL sign-in fix committed and pushed

Date: 2026-11-23
Source: owner instructions and Git results in a Claude Code session on `bora-capital-backend`, branch `feature/updates`.

## The owner's words (verbatim)

- To "Commit this change?" (the case-insensitive email matching): "Commit it".
- Then: "push".
- After the BCL sign-in 403 fix: "commit and push".

## Results

| Commit | What | Pre-commit suite |
| --- | --- | --- |
| `1ab2559` | `feat(users): match account emails ignoring letter case` | 216 suites, 2,023 tests |
| `6f053be` | `fix(bcl): stop a sign-in 403 from hanging every BCL call` | 217 suites, 2,026 tests |

- **First push** (`2809bb1..1ab2559`), on the owner's "push": it carried `ca3cfa1` (the deposit and withdrawal backlog) and `1ab2559`.
- **Second push** (`1ab2559..6f053be`), on "commit and push": it carried `6f053be`.
- **After the second push:** `feature/updates` matches `origin/feature/updates`.
- **Not done:** no pull request was opened, and nothing was deployed.
- **The owner reported done (2026-11-23):**
  - the read-only production email audit was run (the result was not shared with the agent);
  - `docs/frontend-handoff-2026-11-22-emails.md` was sent.
