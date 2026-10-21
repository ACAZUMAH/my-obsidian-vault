# Fleet Deletion And Version Fields

Date: 2026-09-18
Source: direct user correction in the LivelyCura backend conversation.

## User evidence

> all those deleted at fields in the schemas remove them I don't really see the need, remove them and why do you have versions fields in most of the schema for what

## Context and interpretation

The discussion concerns the new independent Fleet backend schemas, following the explicit rejection of the operator's custom version field and the instruction to reuse existing archive conventions. The user explicitly requests removal of Fleet deletion timestamps and challenges the added revision counters. The implementation response removes Fleet `deletedAt`, custom `version`, and public `expectedVersion` contracts, while retaining existing archive metadata and transactional operation checks. This is scoped to Fleet, not unrelated domains or Mongoose's built-in metadata. No migration or deployment claim is made.
