# Host VM batch at runtime35d6: failed, settled

The single authorized batch ran once and exited **1** after **1m55s**, from
`2026-10-27T10:50:26Z` to `10:52:21Z`. The original command and fresh watcher
`/root/host_35d6_watcher` both settled. No operation is running or uncertain.
The utility slot is free, but dependent system/profile builds remain held for
runtime-owner diagnosis and lead disposition. No retry or CI poll occurred.

```sh
nix build --no-link --print-build-logs .#checks.x86_64-linux.host-module-idempotency .#checks.x86_64-linux.session-recovery-boot
```

The runtime worktree was clean at
`35d6073e42c2110ee4a99fa902815d26495c6078`, tree
`481cbc23c9c85fea9d930114509609786a59f425`. Fresh SSH confirmed this feature
head and default `fffbd0d59fffc09667cb39878d9f7da8bdcd3806` before launch.
Nix source `/nix/store/a1blnn9r75zrpjxm5d2yi53lkwk9i9l3-source` has NAR hash
`sha256-u19yGqG9Vk+XHCrSZVR57tGOwwF2OIUTk7T9Dh/yBkg=`.
The retained policy catalog `3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41`
selects the fresh Luna/low verification utility, max1, full-access/never.

| Requested check | Derivation | Output (not valid after batch) |
| --- | --- | --- |
| host-module-idempotency | `/nix/store/m9q5gqjfn8yqcvyw05l78hg775l64w8d-vm-test-run-dev-workspace-host-module-idempotency.drv` | `/nix/store/apfrvraxc5szzskp68bigip5i0i3vypr-vm-test-run-dev-workspace-host-module-idempotency` |
| session-recovery-boot | `/nix/store/47wsmlp1ykbf9mm9l4irw3pz6r2cag0p-vm-test-run-dev-workspace-session-recovery-boot.drv` | `/nix/store/sskabii2wx0pzbhpac7b15lbdfvwkkzr-vm-test-run-dev-workspace-session-recovery-boot` |

The host-module VM began booting, but neither final output is valid. The session
recovery test was blocked by a failed package dependency. This is not a completed
host acceptance result. A read-only store-validity query printed both outputs
as invalid after the original command settled.

The shared `dev-workspace-workspace_host` Ruby dependency reported 235 runs,
2643 assertions, **1 failure, 4 errors, 3 skips**. The original log at
lines1361–1404 records two reconciliation tests failing on missing `systemctl`,
an activation fixture's zero-argument `configure_user_services` receiving one
argument, a registry fixture's `nil +` error, and a pending-evidence assertion
missing `[:restarted]`. Failed derivation:
`/nix/store/xfgbg3wfc7phpykdc3kf639l994ilrg3-dev-workspace-workspace_host-0-of-1.drv`.
These are observations for owner0's diagnosis; no failing test was rerun here.
No unexpected local kernel derivation build appeared; Linux boot output belongs
to the disposable VM. No cancellation was performed.

Evidence: [complete combined output](host-module-idempotency-session-recovery-boot.log),
[command, timing and exit](host-module-idempotency-session-recovery-boot.meta),
[exact source metadata](flake-metadata.json),
[two check derivations](check-derivations.json).
Lead, owner0 and owner1 received the failure and final settlement directly.
Client255 CI/vendor/native evidence remains unchanged at its original scope.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-codex-upgrade-naming/
