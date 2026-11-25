# Altin Partner Mobile: app feature names stay on one line

- Date: 2026-11-25
- Author: the user, through an Altin Partner Mobile Claude Code session
- Repository: `altin-partner-mobile`, uncommitted when recorded

## The user's correction (verbatim, 2026-11-25)

> No showing all the names under an app module on the card is wrong we limit them to one line so don't show them, redo on the search screen and the apps tab

## Context and decision

During the UI improvement, an audit finding ("Fleet's six features are cut to one line") led the session to let the feature-name line under each app wrap to three lines on the Search tab (Browse and Apps results) and in the Apps directory. The user rejected it: the feature names under an app row are deliberately limited to one line and truncated. The session reverted both screens to one line and recorded the rule in the repository `AGENTS.md` Search section.
