# Portal review and recovery fixes

## Goal and decisions

Implement the user-approved plan for accurate Git diffs, collapsible file
comparisons, automatic repository refresh, navigation cancellation, timing
recovery after inactive tabs, and reliable planning-answer submission.

- Git supplies exact changed-line ranges for Unified and Split; CodeMirror
  remains the display and Shiki remains the syntax highlighter. Character
  highlighting stays inside the changed ranges.
- Put Automatic archival under Session settings in the left sidebar, leaving
  the conversation height available to Codex (additional user request).
- Unified is the fallback; explicit URLs and saved Split choices take priority.
- Files with more than 2,000 added plus deleted lines start hidden and do not
  fetch content or initialize editors until requested. Every diff is collapsible.
  Explicit file/line navigation expands its target. Choices survive layout and
  comparison navigation within the page.
- Repository histories refresh automatically in batches. Open comparisons stay
  frozen until the user requests the latest comparison.
- Cancel stale reads before navigation unloads the document. Restore polling on
  return and ignore obsolete responses.
- Keep timing visible during recovery from an inactive tab, stop stale
  extrapolation, and wait ten visible seconds before availability warnings.
- Fix stale App Server request admission and connection retirement. Bind answers
  to exact prompt identities, preserve drafts during recovery, replace question
  submission/snooze alerts with inline status, and allow one automatic retry only
  after a definitely-unsent failure and restoration of the exact same question.
  Uncertain delivery or changed questions never cause automatic resubmission.

## Affected repositories and ownership

codex-web owns the App Server connection/request lifecycle and conversation HTTP
and browser contracts. dev-workspace owns repository reading/rendering, timing,
session details, question UI and the consuming provider pin. vpsfree-dev-workspace
and the workspace consume the runtime through Nix pins. Use the initiative slug
2026-09-14-portal-review-fixes for all branches/worktrees. No configuration
repository change is currently required. The organization extension also updates
the mandatory review instructions to gpt-6-astra, retaining xhigh effort, as
requested by the user.

## Evidence

The deployed renderer calculates +1091/-981 for oauth2_config.rb in vpsadmin
7159fec1390e04156836797cfae1206b99d71531; Git and GitHub report +116/-6. The live
API's blobs exactly match Git. Removing CodeMirror limits gives the correct
counts but takes approximately 0.8 seconds for one file. The configured
scanLimit=500 and timeout=100 permit an approximate fallback.

Firefox reproduces the details NetworkError before pagehide during delayed
navigation. Activity polling stops when hidden, but the renderer calls every
snapshot older than 15 seconds unavailable immediately on return. The portal
logs show two kernel-history-fix answer failures at 16:51:59 and 16:52:11 UTC on
September 14, both rejected before writing because the connection changed.
The reader can admit requests after its connection is retired.

## Compatibility and deployment

Preserve saved comparison URLs, manifests, operation journals, activity state,
database schemas and Codex protocol version. Git range and prompt/error metadata
are additive HTTP/browser contracts. Exact prompt tokens protect updated clients;
unsupported mixed browser/server generations must request reload. No answer is
blindly replayed onto a replacement connection. Keep secret answers memory-only.

Trust the local development operator, retain remote-client authorization, exact
origins, request bounds and immutable repository resolution. No host/node
coordination or persisted-state migration is required. Update pins in order:
codex-web -> dev-workspace -> vpsfree-dev-workspace -> workspace. Deploy the
reviewed application with workspace-host switch from the feature worktree;
retain the previous user profile for rollback. Do not add the application to
system configuration. Keep this session and feature branches open after delivery.

## Verification

Add the reported file as a regression fixture and require exact +116/-6 in both
layouts. Cover line identity, context, renames, Unicode, newline/CRLF cases,
2000/2001-line boundaries, collapsed loading and explicit navigation. Exercise
batched refresh and stale responses while the open comparison remains frozen.
Use deterministic transport tests for retired readers, reissued request IDs,
claims and unknown sends. Browser checks cover retained answer drafts, inline
recovery, no duplicate answers, Firefox/Chromium navigation and hidden-tab timing.

Run focused checks before commits and mandatory adaptive review (gpt-6-astra,
xhigh, all applicable lanes) before long packaged/live tests. Apply the user-facing
writing skill directly to final copy. Push feature branches, inspect CI and fix
failures; validate an isolated App Server before profile deployment and then
exercise the original URL and question recovery on the deployed package.

## Approved presentation follow-up

Reuse this initiative and retained branches for three focused presentation commits:
keep file headings sticky in Unified, Split and full-file views, with compact
paths and visible linked lines; automatically use the 58px sidebar only while
an open repository comparison is visible; format Automatic archival as labelled
fields and readable blockers with a closed Technical details disclosure.
Keep the file tree, accessible sidebar actions and limits popover. Restore the
normal sidebar on overview/other tabs and retain existing mobile behavior.
No fullscreen toggle or new preference is needed.

Archival presentation remains a browser adapter over the existing API. Preserve
raw diagnostics in the disclosure, retain the last successful settings on read
failure, label scan time, and show Not before only when enabled and not held.
The merged tier describes a conditional policy, not evidence of merged branches.
No state, API, archival decisions, fingerprint or schema changes are intended.

Verify sticky boundaries, line links, long paths, keyboard navigation, compact
sidebar transitions and archival states. Run gpt-6-astra/xhigh review after quick
checks and committed changes, then browser/package checks and CI. Update runtime
pins through the organization extension and workspace and deploy the user-profile
package. Leave branches unmerged and session open; refresh verification artifacts.

The final CI check exposed a pre-existing pagination-fixture failure. Its Git
runner discarded bounded stderr, so add standard exec.ExitError diagnostic
metadata without changing public error text, and report it in the failing test.
Trace evidence shows background commit-graph maintenance at the 100-commit
boundary. Disable maintenance only in that disposable fixture, consistent with
the existing bulk-rename test; keep production Git configuration unchanged.
These small CI remediations are separate from the presentation commits and get
focused checks and a bounded General/Architecture review before final deployment.


## Accepted integration

The user authorized integration into all default branches and worktree cleanup.
Fetch defaults, rebase if necessary, capture final comparisons, and fast-forward
the independent projects through temporary target worktrees. Integrate workspace
from the shared master checkout, preserving unrelated changes. Retain feature
branches and the session. No behavior, API, state or deployment change is intended
by integration; verify any rebased source against the reviewed package.
