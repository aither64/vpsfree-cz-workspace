# Executed aitherdev rollout — 2026-10-11

Deployment and live verification succeeded. Source branches remain unmerged;
exact runtime a8934bda, workspace 45aba9bf and configuration 3faee82a are recorded
in [final-heads.json](final-heads.json). Independent review and all browser,
package, host-build and exact-head CI checks passed before deployment.

The parent launched `rollout.sh` through the named transient user service
`portal-mode-refresh-rollout-20261011.service` with an explicit command PATH.
A fresh Luna/low utility observed the existing operation. The script guarded
exact heads, clean tracked content, session identity, successful host verification,
selected baseline profiles and the unchanged native executable. Ordinary
lifecycle/package transition refusals remained in force.

The configuration step ran in its Nix environment with the locked Bundler cache:

```text
confctl deploy --yes --no-interactive --dry-activate-first --no-reboot --enable-auto-rollback cz.vpsfree/machines/aitherdev switch
```

After successful system activation and baseline rechecks, the application step
ran through the stable user-profile launcher:

```text
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-portal-mode-refresh/workspace
```

Selected outputs, confirmed by [post-deploy.json](post-deploy.json):

- System generation `2026-10-11--20-27-19`:
  `/nix/store/2049p019hn0vl21j2a45n8hi1wa2gndz-nixos-system-aitherdev-26.05.20261010.6fcc160`.
- Application profile:
  `/nix/store/sfsck9wxbhkrzl5qygcxxm096bmhdg5v-dev-workspace-0.2.0`.
- Native Codex executable:
  `/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0`.

Live read-only checks used the portal UNIX socket without credentials in logs.
Health returned ok; served JS and CSS exactly matched final runtime source;
the owned session template selected app.js?v=35. Portal and router were active.
Codex PID 1204139/start 10709341732141 and tmux PID 435397/start 8424847130197
matched the pre-deployment snapshot. No native or tmux restart occurred.
Existing loaded tabs need one reload to receive the updated script.

`rollout.status` is 0 and `rollout.phase` is complete. Independent unit inspection
recorded Result=success and ExecMainStatus=0 in `rollout-unit-result.txt`. Only
that completed utility unit was stopped afterward; session services remain active.
The launching client's D-Bus wait returned "Connection reset by peer" after
activation. Actual unit status and post-deployment assertions proved success,
so deployment was not repeated. The transport cause is inferred, not established;
see the [launcher lesson](../../notes/dev-workspace/2026-10-11-systemd-run-dbus-during-host-activation.md).

No state formats changed. This system activation used automatic rollback.
Application user-profile recovery remains forward-only: ordinary interrupted
switch recovery or selection of a corrected newer package, without selecting
an older profile generation. No recovery was required for this rollout.
