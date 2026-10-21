# Altin Refresh And Tip Text

Date: 2026-09-11
Source: direct user report in Codex, followed by scoped repository and existing iOS runtime inspection.

## Direct report

> so part of the tip price is hidden, and also the refresh controls are having some issues, it refreshes loading without end

## Verified implementation lesson

The custom tip amount used larger text inside the shared plain-title fixed line box. Custom title content now owns its line metrics through a layout slot; plain string titles keep compact truncation.

Automatic focus reloads were also activating the native pull control during Back navigation. Request state had already completed while the native refresh presentation remained visible. Focus reloads now keep explicit refreshing false. Explicit refresh clears on success, failure, blur, and scope changes; stale requests remain ignored. This is a state-ownership correction, not a claim that production queries never time out.

Verification used local tests and necessary read-only navigation in the existing iOS runtime. User visual acceptance and untested gestures/platforms are not inferred.
