# Bora: emails are kept exactly as the customer types them (owner correction)

Date: 2026-11-22
Source: direct owner statement in a Claude Code session on `bora-capital-backend`. It came right after the agent changed "Link your account" to store BCL's email lowercased ([that change](2026-11-22-bora-linked-account-email-case-fix.md)).

## The owner's words (verbatim)

> there is something you have to under here, bcl doesn't save customers emails in caps no, the save the email exactly as the customer types, so if my email starts ca you are saying bcl saves Ca no cus if the do that it's a wrong email and they can't send me a message through that, the app is not supposed to change the format of email so all we are supposed to is indicate it to the frontend, cus if my email starts with Ca and it converts it to ca that wouldn't be a valid email not what you did

## What it decides

- BCL stores an email exactly as the customer typed it.
- Neither Bora nor the app may change an email's letter case.
- The app's lowercasing of emails (`canonicalEmail`) goes to the frontend handoff, to be removed.
- The agent's lowercasing of the linked-account email is rejected.

## State at recording

- The agent's lowercasing change is still in the uncommitted working tree.
- The agent raised one consequence before changing anything. Every stored customer email is lowercase today, because the app has lowercased since 2025. Once case is kept as typed, the exact-match lookups (`getUserByEmail` for password recovery, `checkUserExist` at sign-up) would miss any customer who types different capitals. So those lookups must ignore letter case.
- The owner's answer on how to handle lookups was pending.
