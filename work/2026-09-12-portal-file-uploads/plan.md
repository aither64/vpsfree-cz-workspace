# Portal file uploads

## Goal and ownership

Add resumable prompt attachments to existing conversations and the new-session
form. Implement shared attachment HTTP/browser support in codex-web; keep private
storage, authorization scopes, creation and lifecycle policy in dev-workspace.
Affected projects: codex-web, dev-workspace, vpsfree-dev-workspace (runtime pin),
and workspace (organization package pin). Use branch/worktree group
2026-09-12-portal-file-uploads. The user authorized implementation and subsequent
deployment to aitherdev. Default-branch integration and archival are excluded.

## Accepted behavior

- Drag/drop and file picker; multiple file cards with name, size, progress,
  status, retry and removal; keyboard and responsive support.
- Upload immediately; submit only when every selected file is ready. Support
  attachment-only initial prompts, Send, active-turn steering and Queue next.
- Browser payloads use opaque attachment IDs. The server resolves authorized
  files and appends filenames, sizes and absolute paths to the same prompt.
  All types including images use paths; no inline content or archive extraction.
- Freeze exact prompt text and attachment IDs before submission. Retain existing
  Codex submission receipts and retry semantics. Render trusted attachment
  associations in transcript and queue without parsing arbitrary message paths.
- Creation uploads begin in a private draft scope. Bind it to the accepted
  creation request and keep paths and initial prompt stable across recovery.
- Limits: 1 GiB/file, 10 files and 2 GiB/prompt, 10 GiB/session, 100 GiB/workspace,
  4 MiB chunks, two concurrent browser transfers, 1 GiB free-space reserve.
  Reserve pending bytes atomically. Metadata and record counts are also bounded.
- Use bounded streaming, durable offsets, checksums, atomic completion and
  retryable transfers. Reload keeps completed files; incomplete files require
  reselection and prefix verification before resuming. Browser storage contains
  metadata, never complete file contents.
- Store bytes and metadata under private user state outside every workspace
  checkout/worktree. Use generated IDs, private permissions, immutable completed
  files, exact-origin checks, authentication and scope authorization.
- Remove draft files immediately. Confirm sent-file deletion and allow it only
  while referencing conversations are idle with no queued/unresolved use.
  Keep a removed-file record; deletion cannot undo content already read by Codex.
- Keep sent files across archive/revive; archive remains read-only. Explicit
  session deletion removes owned uploads through recoverable lifecycle handling.
- Forks inherit references without copies. Include them in display, busy checks
  and deletion confirmation. Expire unsubmitted uploads after seven idle days;
  protect accepted creations and queued/unresolved submissions.

## Compatibility and deployment

Keep existing creation receipts, lifecycle journals and Codex submission ledger
formats unchanged; attachment associations live in independent private state.
Older packages ignore this state, retain bytes, and keep text conversations usable.
Forward reconciliation uses completed deletion evidence, never absent directories.
Initial tracking may contain path references, never uploaded bytes or transfer
metadata. Keep App Server protocol and selected Codex version unchanged. No
database/client/daemon/NixOS option migration or coordinated node update is needed.
Four MiB requests fit the existing nginx 16 MiB bound; keep prompt JSON limits.

Commit/pin providers before consumers: codex-web -> dev-workspace -> organization
package -> workspace package. Deploy from the feature worktrees through the user
profile on aitherdev, not through system configuration. Preserve rollback state
and leave branches and session open for follow-up.

## Verification

Focused Go/Ruby/browser/protocol checks cover boundary sizes, empty files,
duplicate names, interrupted and repeated chunks, checksum failures, concurrent
quotas, disk exhaustion, cancellation, reload and restart recovery. Exercise
initial creation failure/retry, attachment-only input, Send/steer/queue response
loss, deletion races, cross-scope authorization, archive/revive, forks, slug reuse
and rollback. Verify real browsers at desktop/narrow sizes and a 1 GiB transfer
with bounded memory. Apply the writing skill before committing UI prose.

Commit all intended changes and pass quick checks before mandatory review:
high risk; general, architecture, scope and risk lanes; gpt-5.6-sol xhigh.
Reconcile findings before long integration/package/live App Server checks.
Push feature branches, investigate and monitor CI, then deploy and verify the
live portal. Maintain tracking and the stable session URL; do not archive.
