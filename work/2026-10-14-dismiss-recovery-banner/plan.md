# 2026-10-14-dismiss-recovery-banner

## Goal

Allow dismissing the restored-session banner without sending a continuation
message or activating saved work. The user selected server-persisted dismissal,
keeping queued prompts/goals paused, and a fresh notice after a new restoration.

## Affected repositories

- dev-workspace: notice API, private metadata, browser control and recovery docs.
- workspace: composed application runtime selection.
- vpsfree-cz-configuration: matching devWorkspace host runtime selection.

## Approach

Add an accessible X for waiting recovery notices. POST dismiss-recovery with the
current noticeId, persist acknowledgement separately from execution permission,
and expose additive noticeId/noticeDismissed recovery fields. Bind the notice to
the exact session/root and restoration cycle. Serialise dismissal with recovery
operations and reject stale identities. Preserve held execution and all existing
Send/Continue/queue Start behavior. Render saved dismissal initially and during
refresh; a failed save keeps a retryable notice. Completed work must never receive
a continuation message merely because the notice was dismissed.

## Decisions

- Dismissal persists across browsers, reloads and portal-only restarts.
- New runtime restoration resets the notice; errors/stopped controls stay visible.
- Separate additive private records avoid schema changes to strict recovery files.
- No migrations, lifecycle transitions or Codex protocol changes.
- No default-branch integration or archive is authorized.
- Idle retained tracking conversation has no team; external lead implements.
- Notice identity uses existing canonical terminal identity, covering CLI restore
  and interrupted portal recovery without adding recovery-schema fields.

## Compatibility and deployment

Old packages ignore the additive notice metadata and keep existing recovery
semantics. Old clients ignore additive response fields. Existing recovery state,
submission receipts and manifests remain readable unchanged. Normal application
profile selection remains forward-only; recover with the same or newer compatible
package. Deploy the exact reviewed runtime through both the workspace nested
override and confctl dev-workspace/devWorkspace channel. Check composed locks.
Prepare builds outside claims, then use coordinated machine/profile activation
under vpsfree:aitherdev ownership. Preserve old/new browser execution holds.

## Documentation

Update dev-workspace recovery guidance for portal users and future maintainers;
keep exact rollout revisions and evidence in this initiative. Apply the writing
skill directly. Keep the stable portal link in handoffs.

## Testing plan

Quick JavaScript syntax, focused Go recovery/API/private-record tests and existing
browser contract checks in Nix. Independent final whole-branch review after
commits/quick checks, before Playwright and packaged integration verification.
Exercise empty queues, saved queues and active goals without native activation;
cross-browser/portal restart persistence; stale/repeated requests; new restoration;
failure paths; desktop/mobile keyboard dismissal; unchanged composer drafts and
explicit activation. Long checks/builds use a fresh Luna/low monitor.
