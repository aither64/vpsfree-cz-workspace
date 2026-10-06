# Upload display and prompt file limits

Implement the user's accepted plan in dev-workspace and codex-web. Session
creation must show every selected file in normal page flow, without the upload
component's 12rem internal height cap. Conversation upload lists retain their
existing cap. The shared upload component shows selected file count and full
total size, plus completed count while uploads are incomplete.

Raise the default prompt file count from 10 to 50, including browser creation
draft recovery and server preparation validation. Preserve the 100-ID generic
validation ceiling, 1,000 stored files per scope, 10,000 records per catalog
category, all byte quotas, transfer concurrency and prompt-reference bounds.

## Compatibility and delivery

Preserve API fields, catalog/preparation schemas and submission identities.
New versions read existing records. An older package rejects unfinished creation
records containing more than 10 attachments. Recover unresolved requests under
the new package; normal terminal compaction removes the attachment snapshot.
These reader prerequisites do not authorize downgrade: workspace switching is
forward-only. Clear browser drafts through normal completion.
Completed sessions and upload catalogs retain existing formats. No database,
NixOS configuration or node fleet migration is required.

Update codex-web first and pin dev-workspace's Go and Nix inputs to its feature
revision. Advance changed browser asset versions. Documentation belongs in the
owning repositories: upload behavior in their README/reference, rollback limits
in session preparation guidance. This initiative owns exact revisions and
verification/rollout evidence.

Implementation authorization is the user's "Implement the plan." No default
branch integration has been authorized. Prepare reviewed feature branches; keep
the initiative active until exact final heads are integrated on explicit user
direction. Deployment, if performed, uses the user profile package.

## Acceptance and checks

- 50 files succeed and file 51 is rejected; byte quotas still apply.
- Summary handles empty, single, multiple, zero-byte, partial, failed, removed,
  restored and submitted selections using existing binary size formatting.
- Creation and identical-request recovery work with more than 10 attachments.
- Desktop/narrow creation lists have no internal vertical scrollbar, all file
  actions and Create session remain reachable; conversation cap is preserved.
- Run focused Go/browser checks, commit intended changes, inventory the complete
  branch series and migrations, then mandatory independent final review.
- Resolve findings before long packaged/browser checks through a fresh utility
  watcher. Preserve all results in state and link the stable portal URL.

## Authorized deployment and integration follow-up

The user authorized aitherdev deployment using vpsfree-cz-configuration, followed
by integration into default branches. Keep this initiative and retained roster.
Generic runtime feature3edc605 and provider3d07cf6 remain reviewed/tested.
The host configuration's generic runtime input currently predates the installed
application (924c0ec versus6a972b9). Align host and profile to3edc605 using only
mechanical deployment input updates: preserve the existing extension revision
and override its nested runtime in the consuming workspace flake, plus update
configuration dev-workspace/devWorkspace channel. The extension pin includes
another initiative's unmerged feature and must not be moved or integrated here. Use separate
worktrees and scoped commits. Build/check matching host/profile, dry-activate,
switch host configuration and guarded user profile, verify serving behavior,
then fast-forward approved default branches. Forward-only workspace recovery;
preserve generation, journals, credentials, clusters and retained sessions.
Exact revisions, current generation, commands and results belong in rollout.md.
