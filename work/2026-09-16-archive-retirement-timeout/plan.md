# 2026-09-16-archive-retirement-timeout

## Goal

Fix automatic archive retirement timing and surface worker failures in the portal.
Recover 2026-09-15-abuse-uceprotect and leave it archived. Deployment is authorized;
default-branch integration and archival of this new initiative are not requested.

## Affected repositories

- dev-workspace: retirement deadline, error context, portal presentation, tests/docs.
- vpsfree-dev-workspace: runtime input pin.
- workspace: extension input pin in its dedicated feature worktree.
- No vpsfree-cz-configuration change: application deployment belongs to the user profile.

## Approach

Keep ordinary automatic scan commands at 60 seconds. Scope a 210-second timeout
around thread retirement, whose internal deadline is 180 seconds. Restore the
previous deadline even on failure. Add stage context to retirement errors.

Use existing operation and automatic-archive endpoints to show the last completed
phase and the last failed automatic attempt with separate timestamps. Match both
journal operation ID and conversation identity; ignore stale records and clear
failures on completion. Keep raw diagnostics in Settings. Poll at most every
30 seconds while visible and coalesce requests. Explain read-only pending archives.

## Decisions

The user selected reliability and clear errors, not history-lookup optimization,
and wants the source session left archived. The measured exact-directory lookup
took 70.453 seconds; direct thread read and latest-turn read took 7 ms each.
The 60-second automatic worker wrapper introduced in d9e3800 overrides the
180-second thread timeout established by 7ceab9a. Eight retries failed at this step.

## Compatibility and deployment

No persisted-format, database/schema, API, protocol, client, Terraform, node or
NixOS module contract changes. Preserve identities, ambiguity/idle/merge checks,
journal phases and retry semantics. Old/new readers and rollback use the same state.

After quick checks, committed mandatory review and packaged tests, resume the exact
existing archive with installed dev-session archive ... --as-is. This manual path
has no worker's 60-second wrapper. Do not edit its journal or tracking. Confirm
retirement, journal removal and retained branches before the package switch, which
refuses pending lifecycle journals. Update the runtime/extension/workspace chain,
then workspace-host switch --source the initiative workspace worktree. Preserve
Codex/tmux process identity and the previous profile. No restart of shared Codex,
system deployment, new retention policy, or session revival is intended.

## Documentation

Runtime operators/maintainers: docs/dev-sessions.md owns deadlines and recovery.
Exact recovery/deployment results belong in this initiative's rollout.md and state.
Record a reusable timeout lesson in notes/dev-workspace. Apply the user-facing
writing skill to final UI/docs text before committing.

## Testing plan

Subprocess regression with short test-only deadlines proves slow retirement passes,
real timeout remains bounded and restores ordinary limits; separately inspect
the 60/180/210 production hierarchy. Review accepted the lack of an automated
cross-language deadline-drift check; keep the hierarchy documented together. Test retry from tracking_committed without another
tracking commit. Test stage errors and identity-bound UI diagnostics, refresh errors,
running retry, completion and missing composer. Run Nix-based focused Ruby/Go/browser
checks, commit, all four gpt-6-astra/xhigh review lanes, then packaged and isolated
archive acceptance checks. Push feature branches and inspect applicable CI. Verify
deployed package/assets/services and the recovered source archive before handoff.
