# Dev cluster master expects unmerged notification options

## Symptom

The vpsAdmin development cluster on workspace commit `cf437a5` failed NixOS
evaluation against vpsAdmin master `8028e5032` with missing options including
`vpsadmin.api.managedNotificationTemplates`, `vpsadmin.api.notifications`, and
`vpsadmin.haproxy.telegram-receiver`.

## Cause

Workspace master contains the notification-stack development-cluster changes,
but the corresponding vpsAdmin module options are still on an unmerged feature
branch. A vpsAdmin feature based on current `origin/master` therefore cannot be
evaluated by the newest harness even when no notification-template worktree is
selected; `lib.mkIf false` does not make an undeclared NixOS option valid.

## Workaround

For `work/2026-07-13-security-advisory-automation/`, the clean integration used
the last compatible committed harness baseline `a98bdb9` and applied only the
initiative's 47-line exact source-revision plumbing from `cf437a5`. Product
inputs remained detached clean worktrees at their final commits, and the
cluster used the bridge network.

Once the vpsAdmin notification modules merge, use workspace master normally.
Alternatively, the harness could conditionally add whole modules instead of
assigning unavailable options through `mkIf`.
