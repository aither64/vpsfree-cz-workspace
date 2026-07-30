# Dev-cluster HaveAPI client credentials can be stale

Related initiative: `work/2026-06-15-vpsadmin-events`

## Symptom

After a services-only activation of the vpsAdmin development cluster, both
`vpsadminctl` using the root configuration and a direct request using
`/etc/haveapi-client.yml` returned HTTP 401. The API and WebUI HTTPS health
checks still returned HTTP 200, and all application services were healthy.

## Safe investigation

Do not print either client configuration or use `devcluster urls`, because the
output may contain credentials. It is safe to inspect configuration key names
or server URLs, and to make an authenticated request that prints only the
response status.

When the credentials are not relevant to the feature under test, avoid
resetting accounts or authentication state. A read-only Ruby script loaded
through `vpsadmin-api-ruby` can inspect the deployed API registry directly.
Place a temporary ignored script under the mounted vpsAdmin worktree, run it
from `/mnt/vpsadmin`, and remove it afterwards.

## Verification

The runtime inspection loaded the exact deployed revision, refreshed the Event
Type catalog, and checked its counts, topics, exclusions, typed resource
descriptors, and field examples. The temporary script was removed and the
vpsAdmin worktree remained clean.
