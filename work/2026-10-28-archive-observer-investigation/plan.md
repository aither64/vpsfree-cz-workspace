# 2026-10-28-archive-observer-investigation

## Goal

Explain why `2026-10-28-observer-progress-guidance` failed to archive and propose
a recurrence-preventing correction. Investigation only: do not retry archival,
change the target session, implement a fix or deploy a package.

## Affected repositories

Generic `dev-workspace`, specifically explicit archive shutdown and managed turn
retry admission. This coordination workspace owns the investigation records.

## Approach

Correlate the archive worker journal, portal preparation receipt, retained roster,
held-prompt metadata and native watcher timeline with the exact deployed source.
Inspect existing test coverage and identify a bounded corrective design.

## Decisions

The caller had no current session or environment binding. Created a separate
threadless investigation using `dev-session start archive-observer-investigation
--no-attach --no-codex --json`. Do not adopt the affected session's roster.
No application edits or delegated implementation are involved.

## Compatibility and deployment

Any proposed correction must preserve native ancestry proof, queue retention,
goal pausing, retry cancellation/reconciliation, lifecycle locks and retryable
recovery. Native utilities must not gain managed submission/retry authority merely
because archival can stop them. Prefer no stored-format change. Implementation,
review and deployment are future work outside this request.

## Documentation

Readers: operator and runtime maintainers. Evidence and proposed correction belong
in `findings.md`; current status in `state.md`; concise reusable diagnosis in
`notes/dev-workspace/2026-10-28-archive-active-native-watcher.md`. Existing project
contracts already describe descendant shutdown correctly, so no product-doc edit
is needed for this investigation.

## Testing plan

Read-only correlation of independent journal, native metadata and source evidence.
Do not reproduce by interrupting a live agent or retrying archival. Recommend
regression cases for the future fix; no build or test run is needed for findings.
