# Workspace portal deployment

This runbook deploys the portal at
`https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/`. The implementation
session does not deploy aitherdev or the internal DNS servers.

## Revisions

- Workspace source branch: `2026-09-03-dev-session-portal`
- Workspace source: `d269a6ca57b46ac0a2c86279ce76120eb0948f3d`
- Configuration branch: `2026-09-03-dev-session-portal`
- Configuration source: `7b7d3489ab6a079b04a48a2f4a645ed8dfa9c354`

Check both revisions against `state.md` before running any helper or deployment
command:

```sh
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace rev-parse HEAD
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration rev-parse HEAD
test "$(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace rev-parse HEAD)" = \
  d269a6ca57b46ac0a2c86279ce76120eb0948f3d
test "$(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration rev-parse HEAD)" = \
  7b7d3489ab6a079b04a48a2f4a645ed8dfa9c354
```

## 1. Record rollback state

Run these commands in the configuration worktree before deployment. They save
the rollback paths in a mode-`0600` shell file, so a new shell or
`nix develop -c` command does not lose them. Keep both files after deployment.

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration
previous_config_revision=$(git rev-parse origin/master)
previous_aitherdev_system=$(readlink -f /run/current-system)
previous_prg_dns_system=$(ssh root@172.16.9.90 readlink -f /run/current-system)
previous_brq_dns_system=$(ssh root@172.19.9.90 readlink -f /run/current-system)
rollback_state=/var/tmp/vpsfree-cz-workspace-portal-rollback.env
rollback_dns=/var/tmp/vpsfree-cz-workspace-portal-dns-before.txt
umask 077
{
  printf 'previous_config_revision=%q\n' "$previous_config_revision"
  printf 'previous_aitherdev_system=%q\n' "$previous_aitherdev_system"
  printf 'previous_prg_dns_system=%q\n' "$previous_prg_dns_system"
  printf 'previous_brq_dns_system=%q\n' "$previous_brq_dns_system"
} > "$rollback_state"
{
  date --iso-8601=seconds
  for server in 172.16.9.90 172.19.9.90; do
    dig "@$server" vpsfree.cz SOA +noall +answer
    dig "@$server" vpsfree-cz-workspace.aitherdev.int.vpsfree.cz CNAME +noall +answer
  done
} | tee "$rollback_dns"
chmod 0600 "$rollback_state" "$rollback_dns"
test -s "$rollback_state" && test -s "$rollback_dns"
```

Load and validate the saved paths before any deployment:

```sh
. /var/tmp/vpsfree-cz-workspace-portal-rollback.env
[[ "$previous_config_revision" =~ ^[0-9a-f]{40}$ ]]
for path in \
  "$previous_aitherdev_system" \
  "$previous_prg_dns_system" \
  "$previous_brq_dns_system"; do
  [[ "$path" = /nix/store/*-nixos-system-* ]]
done
test -x "$previous_aitherdev_system/bin/switch-to-configuration"
ssh root@172.16.9.90 \
  test -x "$previous_prg_dns_system/bin/switch-to-configuration"
ssh root@172.19.9.90 \
  test -x "$previous_brq_dns_system/bin/switch-to-configuration"
```

The running system paths, not a local Git reference, are the rollback authority
for each machine. The saved SOA and CNAME answers identify the DNS state that
was active with those paths.

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
bin/workspace-pki init \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
bin/workspace-pki verify \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
bin/workspace-pki inspect \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
sudo bin/workspace-pki install-server \
  --state-dir /home/aither/.local/state/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz \
  /var/lib/vpsfree-workspace-portal-tls
```

The encrypted CA key remains at
`/home/aither/.local/state/vpsfree-workspace-pki/authority/ca-key.pem`.
The nginx certificate and key are selected together through
`/var/lib/vpsfree-workspace-portal-tls/current`.

Confirm that nginx can traverse the installed directories and read the pair:

```sh
stat -c '%U:%G %a %n' \
  /var/lib/vpsfree-workspace-portal-tls \
  /var/lib/vpsfree-workspace-portal-tls/pairs \
  /var/lib/vpsfree-workspace-portal-tls/current/server-key.pem
sudo -u nginx test -r \
  /var/lib/vpsfree-workspace-portal-tls/current/server-key.pem
sudo -u nginx test -r \
  /var/lib/vpsfree-workspace-portal-tls/current/server.pem
```

The directories must be `root:nginx` with mode `0750`; the installed key must
be `root:nginx` with mode `0640`.

Export the public CA and install it as a trusted TLS root on each VPN client:

```sh
bin/workspace-pki export-ca /tmp/vpsfree-workspace-ca.pem
```

Do not copy the CA key, a server key, or the CA passphrase to a client.

## 3. Build and deploy aitherdev

From the reviewed configuration worktree:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration
nix develop -c confctl build -y cz.vpsfree/machines/aitherdev
nix develop -c confctl deploy -y cz.vpsfree/machines/aitherdev
```

Check nginx, the local socket, and the TLS files before testing Codex:

```sh
systemctl status workspace-portal nginx --no-pager
sudo nginx -t
sudo -u nginx curl --fail --unix-socket \
  /run/vpsfree-workspace-portal/portal.sock http://localhost/healthz
sudo lxc-attach -n vscode -- \
  test ! -e /run/vpsfree-workspace-portal/portal.sock
sudo -u nginx test -r \
  /var/lib/vpsfree-workspace-portal-tls/current/server-key.pem
```

The status pages remain available if the Codex daemon is stopped or has the
wrong version. Interactive session operations require a matching daemon. Check
it separately:

```sh
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
Check the name-specific HTTP redirect and HSTS header as well:

```sh
curl --silent --show-error --head --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:80:172.16.106.40 \
  http://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz | \
  grep -i '^location: https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz'
curl --silent --show-error --head --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /tmp/vpsfree-workspace-ca.pem -u aither \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz | \
  grep -i '^strict-transport-security: max-age=31536000'
```

## 4. Deploy both internal DNS servers

Deploy DNS only after the pre-DNS HTTPS test succeeds:

```sh
nix develop -c confctl build -y cz.vpsfree/containers/prg/int.ns1
nix develop -c confctl build -y cz.vpsfree/containers/brq/int.ns1
nix develop -c confctl deploy -y cz.vpsfree/containers/prg/int.ns1
nix develop -c confctl deploy -y cz.vpsfree/containers/brq/int.ns1
```

Query both servers directly:

```sh
dig @172.16.9.90 vpsfree-cz-workspace.aitherdev.int.vpsfree.cz CNAME +short
dig @172.19.9.90 vpsfree-cz-workspace.aitherdev.int.vpsfree.cz CNAME +short
```

Both commands must return `aitherdev.int.vpsfree.cz.`. The zone TTL is one
hour.

If either DNS deployment or query fails, switch both DNS servers back to the
exact running system paths recorded before deployment:

```sh
. /var/tmp/vpsfree-cz-workspace-portal-rollback.env
[[ "$previous_prg_dns_system" = /nix/store/*-nixos-system-* ]]
[[ "$previous_brq_dns_system" = /nix/store/*-nixos-system-* ]]
ssh root@172.16.9.90 \
  "$previous_prg_dns_system/bin/switch-to-configuration switch"
ssh root@172.19.9.90 \
  "$previous_brq_dns_system/bin/switch-to-configuration switch"
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
- a command or file-change approval shows the complete request and related item
  before any decision;
- a permission approval is rejected by the portal and remains available in the
  terminal client;
- archived or finalized sessions do not show mutation controls.

Archive or abandon the disposable initiative through the normal workspace
workflow. Keep the captured system paths in the deployment record after all
checks pass.

## Certificate renewal

Use the helper installed by the active NixOS system so renewal uses the pinned
workspace revision:

```sh
workspace-pki renew \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
workspace-pki verify \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
sudo workspace-pki install-server \
  --state-dir /home/aither/.local/state/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz \
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
. /var/tmp/vpsfree-cz-workspace-portal-rollback.env
[[ "$previous_aitherdev_system" = /nix/store/*-nixos-system-* ]]
test -x "$previous_aitherdev_system/bin/switch-to-configuration"
sudo "$previous_aitherdev_system/bin/switch-to-configuration" switch
sudo -u aither -H codex app-server daemon restart
```

If DNS has been deployed, switch each DNS server to its separately captured
system path, verify its SOA and CNAME answers directly, and wait one hour before
restoring the old aitherdev system. This ordering keeps cached portal records
on the authenticated TLS virtual host until they expire.

The portal service uses `KillMode=process` because tmux panes and the managed
Codex App Server must survive a portal service restart. A portal deployment
therefore does not update those long-lived processes. The version checks and
explicit daemon restart above prevent an old App Server from being used with a
new portal adapter.
