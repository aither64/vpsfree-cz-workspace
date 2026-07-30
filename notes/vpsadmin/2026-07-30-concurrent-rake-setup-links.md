# Concurrent rake setup can transiently remove plugin links

Related initiative:
`work/2026-06-15-vpsadmin-events/`.

## Symptom

Shortly after a dev-cluster service update, two periodic API rake services
failed with `LoadError` for plugin `meta.rb` files under
`/var/lib/vpsadmin/api/plugins/`. The named links existed when inspected and
the main API remained healthy.

## Cause

Every rake service runs the shared API setup as `ExecStartPre`. Setup itself is
serialized with `/var/lib/vpsadmin/api/.setup.lock`, but the lock is released
before the rake process loads plugins. If another timer starts immediately,
its setup can replace plugin links after the first service has left setup but
before it finishes loading the plugin registry.

## Workaround and verification

Wait until the concurrent setup has completed, then retry the failed oneshot
services and clear the recorded failed state. In this initiative,
`vpsadmin-api-payments-process.service` and
`vpsadmin-api-auth-tokens.service` both succeeded on retry, after which
`systemctl --failed` was empty.

A durable fix should make plugin-link replacement atomic from readers'
perspective or retain the setup lock while the rake process loads its plugin
registry. Do not mistake this race for a missing plugin in a newly built API
package without first checking the resolved links and a serialized retry.
