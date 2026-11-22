# Dev-cluster plugin symlink race during a services switch

## Symptom

While `devcluster start` enabled Telegram and switched the already-running
services VM to the rebuilt configuration, a scheduled API rake unit failed:

```text
LoadError: cannot load such file -- /var/lib/vpsadmin/api/plugins/webui/meta.rb
```

The API and event services were otherwise healthy.

## Cause

The timer fired during the short interval in which API pre-start replaced the
persistent plugin symlinks. By the time the NixOS switch completed,
`/var/lib/vpsadmin/api/plugins/webui` pointed to the new package and its
`meta.rb` existed. This was a switch-time race, not a missing file in the
vpsAdmin source or Nix package.

## Workaround

Wait for the services switch to finish. Verify both the persistent symlink and
its Nix store target, then rerun only the failed rake unit. Do not reset the
cluster or database for this symptom.

For this occurrence:

```shell
systemctl start vpsadmin-api-payments-process.service
systemctl list-units --failed --no-legend --plain
```

## Verification

The rerun succeeded, the packaged `plugins/webui/meta.rb` was present, and no
failed units remained.

Related initiative: `work/2026-06-15-vpsadmin-events`.
