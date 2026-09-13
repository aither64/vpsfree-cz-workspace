# Portal file uploads

## Goal and ownership

Add resumable prompt attachments to existing conversations and the new-session
form. Implement shared attachment HTTP/browser support in codex-web; keep private
storage, authorization scopes, creation and lifecycle policy in dev-workspace.
Affected projects: codex-web, dev-workspace, vpsfree-dev-workspace (runtime pin),
workspace (organization package pin), and vpsfree-cz-configuration (host-module pin). Use branch/worktree group
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
package -> workspace package. Deploy the aitherdev host-module pin from the configuration feature worktree
and the application from the workspace user-profile package. Preserve rollback state
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

## Deployment clarification

The user additionally requested deployment through vpsfree-cz-configuration.
Its aitherdev host-module input is pinned through confctl on this initiative
branch. The application still deploys from the workspace user-profile package.
Build and deploy both from their feature worktrees, retaining default branches.


## Review decisions

Reclaim obsolete metadata while retaining sent history and fork tombstones.
Use the existing Codex deletion ledger for recoverable provider completion;
editable queue refresh reconciles already absent entries through an explicit
POST under mutation authority; GET remains observational. Finish pending queue
cancellations before rollback. If an older generation clears such a receipt,
rolling forward retains the file until owner-session deletion. This is a
retention-only limit, with no state-format change or loss of file contents.
See review-reconciliation.md for findings, fixes and focused regression results.

## Follow-up: compact attachment menu (2026-09-13)

The user accepted placing a + icon beside Send and Create session in both
forms. It opens an overlay with Attach files; the picker still accepts multiple
files. Empty card/error areas are hidden and the permanent limits prose is
removed. Actual rejection errors and all limits remain enforced.

The reusable menu belongs to codex-web mountUploads, with optional controlsRoot
to place controls independently of cards. Existing callers retain a working
default root. Native popover dismissal plus keyboard/focus behavior is shared;
destroy removes only owned controls. No upload protocol, persisted state, Codex
version, security policy, or server behavior changes. Browser assets deploy
together through existing pins; rollback can read the unchanged upload state.

Verify quick syntax/contract/Go checks, commit and run all applicable required
review lanes, then desktop and narrow Firefox acceptance covering both forms,
menu placement/focus, picker/drop/removal, empty layout, limit errors and lock/
cleanup behavior. Repeating large-file and live Codex lifecycle acceptance is
unnecessary for this UI-only follow-up. Push retained feature branches, update
downstream pins, build/deploy user profile and aitherdev from the configuration
feature worktree. Keep all branches unmerged and the initiative open.
