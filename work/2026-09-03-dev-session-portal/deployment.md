# Workspace portal deployment

This runbook deploys the portal at
`https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/`. The implementation
session does not deploy aitherdev or the internal DNS servers.

## Revisions

- Workspace source branch: `2026-09-03-dev-session-portal`
- Workspace source: use the final head recorded in `state.md`
- Configuration branch: `2026-09-03-dev-session-portal`
- Configuration source: use the final head recorded in `state.md`

Check both revisions against `state.md` before running any helper or deployment
command:

```sh
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace rev-parse HEAD
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration rev-parse HEAD
```

## 1. Record rollback state

Run these commands in the configuration worktree before deployment. Keep their
output until the portal and both DNS servers pass the smoke tests.

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration
previous_config_revision=$(git rev-parse origin/master)
previous_aitherdev_system=$(readlink -f /run/current-system)
printf 'configuration: %s\naitherdev system: %s\nDNS serial: %s\n' \
  "$previous_config_revision" \
  "$previous_aitherdev_system" \
  "$(git show "$previous_config_revision":configs/internal-dns/zone.vpsfree.cz. | sed -n '4s/[^0-9]*\([0-9][0-9]*\).*/\1/p')"
rollback_checkout=$(mktemp -d)
rmdir "$rollback_checkout"
git worktree add --detach "$rollback_checkout" "$previous_config_revision"
```

The rollback checkout holds the exact previous DNS configuration. Do not
remove it until deployment is complete.

## 2. Prepare authentication and TLS on aitherdev

Create the nginx password file:

```sh
sudo install -d -o root -g nginx -m 0750 \
  /var/lib/vpsfree-workspace-portal-auth
nix shell nixpkgs#apacheHttpd -c sudo htpasswd -c \
  /var/lib/vpsfree-workspace-portal-auth/htpasswd aither
sudo chown root:nginx \
  /var/lib/vpsfree-workspace-portal-auth/htpasswd
sudo chmod 0640 \
  /var/lib/vpsfree-workspace-portal-auth/htpasswd
```

Create the private CA and first leaf certificate from the reviewed workspace
revision:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace
bin/workspace-pki init
bin/workspace-pki verify
bin/workspace-pki inspect
sudo bin/workspace-pki install-server \
  --state-dir /home/aither/.local/state/vpsfree-workspace-pki \
  /var/lib/vpsfree-workspace-portal-tls
```

The encrypted CA key remains at
`/home/aither/.local/state/vpsfree-workspace-pki/authority/ca-key.pem`.
The nginx certificate and key are selected together through
`/var/lib/vpsfree-workspace-portal-tls/current`.

Export the public CA and install it as a trusted TLS root on each VPN client:

```sh
bin/workspace-pki export-ca /tmp/vpsfree-workspace-ca.pem
```

Do not copy the CA key, a server key, or the CA passphrase to a client.

## 3. Build and deploy aitherdev

From the reviewed configuration worktree:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration
nix develop
confctl build -y cz.vpsfree/machines/aitherdev
confctl deploy -y cz.vpsfree/machines/aitherdev
```

Check the local service and the Codex daemon versions:

```sh
systemctl status workspace-portal nginx --no-pager
curl --fail http://127.0.0.1:2460/healthz
sudo -u aither -H codex app-server daemon version
```

The version result must report `status` as `running`, and `cliVersion` and
`appServerVersion` must both match the version supported by the deployed
portal. Restart the daemon after a Codex upgrade or rollback, then check again:

```sh
sudo -u aither -H codex app-server daemon restart
sudo -u aither -H codex app-server daemon version
```

Test HTTPS and Basic Authentication before publishing DNS. Curl prompts for
the password without placing it in shell history:

```sh
curl --fail --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /tmp/vpsfree-workspace-ca.pem \
  -u aither \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz
```

Also confirm that the same request without `-u aither` returns HTTP 401.

## 4. Deploy both internal DNS servers

Deploy DNS only after the pre-DNS HTTPS test succeeds:

```sh
confctl build -y cz.vpsfree/containers/prg/int.ns1
confctl build -y cz.vpsfree/containers/brq/int.ns1
confctl deploy -y cz.vpsfree/containers/prg/int.ns1
confctl deploy -y cz.vpsfree/containers/brq/int.ns1
```

Query both servers directly:

```sh
dig @172.16.9.90 vpsfree-cz-workspace.aitherdev.int.vpsfree.cz CNAME +short
dig @172.19.9.90 vpsfree-cz-workspace.aitherdev.int.vpsfree.cz CNAME +short
```

Both commands must return `aitherdev.int.vpsfree.cz.`. The zone TTL is one
hour.

If either DNS deployment or query fails, use the rollback checkout to redeploy
both DNS servers immediately:

```sh
cd "$rollback_checkout"
nix develop -c confctl deploy -y cz.vpsfree/containers/prg/int.ns1
nix develop -c confctl deploy -y cz.vpsfree/containers/brq/int.ns1
```

Verify both servers again against the expected previous state. Keep the portal
virtual host running for at least one TTL after restoring DNS so clients with a
cached record do not reach an unrelated service.

## 5. Smoke test from a VPN client

With the public CA installed and trusted:

```sh
curl --fail --cacert /path/to/vpsfree-workspace-ca.pem \
  -u aither \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz
```

Open the portal in a browser and check this initiative page. Create a
disposable session with a harmless initial request. Confirm all of the
following:

- retrying the same short name does not create another session;
- the terminal attach command resumes the browser thread;
- messages sent from either client appear in the other;
- an approval shows the complete request and related item before any decision;
- archived or finalized sessions do not show mutation controls.

Archive or abandon the disposable initiative through the normal workspace
workflow. Remove the rollback checkout after all checks pass:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration
git worktree remove "$rollback_checkout"
```

## Certificate renewal

Use the helper installed by the active NixOS system so renewal uses the pinned
workspace revision:

```sh
workspace-pki renew
workspace-pki verify
sudo workspace-pki install-server \
  --state-dir /home/aither/.local/state/vpsfree-workspace-pki \
  /var/lib/vpsfree-workspace-portal-tls
sudo systemctl reload nginx
```

Old certificate pairs remain in their version directories. Record the current
symlink target before renewal. If reload validation fails, atomically restore
that target and reload nginx again.

## Rollback

Inspect failures first:

```sh
journalctl -u workspace-portal -u nginx --since today
```

If DNS has not been deployed, restore the exact aitherdev system recorded in
step 1:

```sh
sudo "$previous_aitherdev_system/bin/switch-to-configuration" switch
sudo -u aither -H codex app-server daemon restart
```

If DNS has been deployed, redeploy both DNS servers from `$rollback_checkout`,
verify them directly, and wait one hour before restoring the old aitherdev
system. This ordering keeps cached portal records on the authenticated TLS
virtual host until they expire.

The portal service uses `KillMode=process` because tmux panes and the managed
Codex App Server must survive a portal service restart. A portal deployment
therefore does not update those long-lived processes. The version checks and
explicit daemon restart above prevent an old App Server from being used with a
new portal adapter.
