# Optional devcluster worktrees can require newer vpsAdmin options

Related initiative: `work/2026-07-20-security-advisory-review/`

`dev-clusters/vpsadmin/bin/devcluster` automatically includes optional project
sources when a matching directory exists under the initiative worktree group.
Adding a `vpsfree-notification-templates` worktree made the cluster evaluate
`vpsadmin.api.managedNotificationTemplates`, but the initiative's older
vpsAdmin feature base did not define that option. Evaluation failed before any
running machine was changed.

When the optional component is not part of the deployment being tested, keep
its clean, pushed branch but temporarily remove its linked worktree with
`bin/dev-session worktree remove`. Run the scoped cluster update, then restore
the worktree with `bin/dev-session worktree add` on the existing branch. Do not
edit shared devcluster configuration merely to mask this version mismatch.
