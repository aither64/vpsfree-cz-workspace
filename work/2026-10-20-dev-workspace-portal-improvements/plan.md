# 2026-10-20-dev-workspace-portal-improvements

## Goal

I'd like several dev-workspace portal improvements:

- Upon loading the index page, I see "Session status is loading" at the top for >5 seconds. I shouldn't see such things, it is distracting. It should take so long and don't bother me unless there's a problem.
- codex output sometimes shows "Older history is unavailable on this server" at the top, overlapping the content. is it using the shared fetch timeout? It shouldn't bother me.
- the portal sometimes fails to submit my inputs to codex, opens alert window with 502 error
- I'd like codex output to use different colors for messages between team members, so that it differs from my own messages and messages meant to me. The filter at the top (All/Messages/Activity) should allow me to hide team communication.
- use markdown to format messages entered by the user
- links to workspace files in codex messages should have target=_blank
- links to workspace files aren't real links, I can't do "Open in new tab"
- the file content viewer should allow me to easily copy all content to clipboard or to download the file
- in artifact list, the list of artifact names is too distinct and uses too much space. make it more compact, like a file tree view... some sessions have hundreds of artifacts
- artifact viewer should also allow me to copy content to clipboard, Download button can be more compact, just an icon, like for copy
- maybe artifact list should scroll independently from the content viewer, since when the list is too long, I have to scroll to top after clicking on selected artifact

## Affected repositories

- `dev-workspace`: portal loading, submission integration, file and artifact UI.
- `codex-web`: shared Codex history, message rendering and filters.
- `workspace`: final package source pins, after the two implementation packages.
- Configuration pins and deployment are outside the current implementation scope.

## Approach

Architect investigates current behavior and writes the technical design before
implementation. Two retained implementers own independent packages, including
source, tests, technical docs, quick checks, commits and review fixes. The lead
coordinates scope, tracking, acceptance and user-facing wording. Final committed
heads receive independent review before long integration checks. Publish feature
branches; default-branch integration requires explicit user direction.

## Decisions

- Suppress routine loading/capability noise while keeping actionable failures.
- Diagnose intermittent submission errors; preserve input and prevent duplicate
  turns rather than adding blind mutation retries.
- Make workspace links native anchors, and large artifact catalogs compact with
  independently scrollable navigation and accessible copy/download actions.

## Compatibility and deployment

Preserve persisted sessions and existing Codex protocol contracts. The architect
will establish exact browser/server compatibility, mixed-version behavior and
rollback constraints. No database or state migration is intended. Deployment is
not yet requested; keep the selected runtime usable and unchanged during tests.
No lifecycle cleanup is authorized.

## Documentation

Readers are portal users and maintainers of the shared Codex browser module.
Durable behavior and failure semantics belong in the owning repository docs;
this directory holds design, checks, review and eventual rollout evidence.

## Testing plan

Use repository Nix environments and targeted regression checks for loading and
history, submission failure/recovery, team filtering, Markdown, native file links,
copy/download, and large artifact navigation. After quick checks and independent
review, use a fresh policy utility watcher for long or uncertain checks.
