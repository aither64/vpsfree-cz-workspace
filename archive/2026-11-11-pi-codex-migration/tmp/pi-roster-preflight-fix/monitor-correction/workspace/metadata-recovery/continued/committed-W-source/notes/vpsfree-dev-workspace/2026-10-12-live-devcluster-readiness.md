# Guest readiness in live cluster checks

The vpsAdminOS runner marks a cluster ready after OSVM's control shell becomes
available. Networking, SSH host-key generation and the tank service can still
be starting. An immediate SSH file write can fail with No route to host even
after Start returns successfully.

Before testing persistent data over SSH, probe the guest services with a bounded
wait, for example:

```sh
vpsadminos-devcluster ssh "$slug" node1 -o ConnectTimeout=5 -o BatchMode=yes \
  -- 'zpool list tank >/dev/null'
```

Keep failed attempt logs and inspect guest startup evidence before retrying.
The probe retries a readiness query; it does not retry Start. Apply it after
both initial startup and a portal Start when checking disk retention.

The helper requires `--` before a remote command. Without it, the command is
passed among SSH options before the destination and can be interpreted as a
hostname. The documented separator resolved that earlier invocation failure.

Related initiative: work/2026-10-11-cluster-controls/.
