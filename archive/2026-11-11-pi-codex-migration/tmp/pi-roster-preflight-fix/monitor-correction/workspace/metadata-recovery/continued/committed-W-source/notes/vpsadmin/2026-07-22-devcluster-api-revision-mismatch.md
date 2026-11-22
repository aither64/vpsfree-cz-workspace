# Dev cluster WebUI can outrun the packaged API revision

Related initiative: `work/2026-06-15-vpsadmin-events/`

## Symptom

New WebUI pages were visible immediately from the live-mounted vpsAdmin
worktree, but API resources added by the same change were unavailable. PHP
failed with errors such as:

```text
Call to a member function list() on false
```

Restarting `vpsadmin-api.service` and the WebUI PHP-FPM pool did not help. The
services VM's `/etc/vpsadmin/build-info.json` still named an older vpsAdmin
revision, and the API service's `WorkingDirectory` was the corresponding
immutable Nix store path. The WebUI and API were therefore running different
revisions.

## Fix

When a change adds or modifies API resources, update the services VM instead
of only restarting its processes:

```sh
dev-clusters/vpsadmin/bin/devcluster update <slug> services
```

The update rebuilds and activates the packaged API revision while retaining
the cluster database and persistent state. A restart is sufficient only when
the already packaged code is correct.

## Verification

For this initiative, the services build information changed from vpsAdmin
`90291d533325774079e1e26a5b09d3a576f5abd6` to
`394064e71baaed8b3ab96ebbefac4b81f1f5520d`. A fresh admin browser session then
loaded the notification routes list, time intervals list, and default route
detail with HTTP 200 and their expected headings.
