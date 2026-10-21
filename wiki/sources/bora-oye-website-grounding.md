---
type: source
status: active
created: 2026-09-18
updated: 2026-09-18
tags: [bora-capital, oye, ai, grounding]
sources:
  - ../../raw/sources/2026-09-18-bora-oye-website-grounding.md
---

# Bora Oye Website Grounding

## Source

- Raw file: [Direct user instruction](../../raw/sources/2026-09-18-bora-oye-website-grounding.md)
- Date: 2026-09-18
- Author: User and live Bora Advisors public website
- Ingested: 2026-09-18

## Core Claims

- Oye must ground Bora-specific customer answers in current content retrieved from `https://boradvisors.com`.
- Unsupported or unavailable Bora facts require an explicit cannot-verify response rather than model-memory completion.
- General financial education remains allowed, but Oye cannot give personal advice or product recommendations.

## Useful Details

- Retrieve relevant official pages and posts at request time, clean their markup, briefly cache them, and cite exact official source URLs in Bora-specific answers.
- Treat retrieved content as untrusted reference data so website text cannot override system behavior.
- Preserve dates and risk qualifications for prices, rates, yields, and returns.
- Search the public site with allowlisted domain terms only; never send customer free-form text, names, phone numbers, account numbers, or similar private data.
- Reject retrieved source URLs outside the exact Bora Advisors origin and fail closed when retrieval cannot provide evidence.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]

## Contradictions Or Tensions

- Supersedes the generic prompt-only Oye design, which prohibited invention but supplied no authoritative Bora facts and therefore could not reliably answer customer questions.

## Open Questions

- A live model evaluation set based on real meeting questions would provide stronger answer-quality evidence than service and retrieval tests alone.

