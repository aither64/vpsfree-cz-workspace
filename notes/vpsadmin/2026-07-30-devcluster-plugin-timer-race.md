# Dev-cluster API timer can run before plugin links are ready

Related initiative: `work/2026-06-15-vpsadmin-events`

## Symptom

During a fresh `devcluster start`, the
`vpsadmin-api-incident-reports.service` timer fired while the services VM was
still completing its first activation. The rake task failed with:

```text
LoadError: cannot load such file -- /var/lib/vpsadmin/api/plugins/webui/meta.rb
```

## Cause

The timer can run before the development plugin tree under
`/var/lib/vpsadmin/api/plugins` is fully linked. The later readiness/activation
stage installs the links, so this is a startup-order race rather than an
application migration or Event-system failure.

## Workaround and verification

Wait for `devcluster start` to complete, then inspect the exact timer unit
instead of accepting or rerunning it blindly:

```sh
bin/devcluster ssh SLUG services -- \
  systemctl status vpsadmin-api-incident-reports.service --no-pager
bin/devcluster ssh SLUG services -- \
  journalctl -b -u vpsadmin-api-incident-reports.service --no-pager
```

In this initiative, the next two scheduled executions completed with status
0 after the final services activation. `systemctl --failed` was empty and the
API service had no error-priority entries after activation.
