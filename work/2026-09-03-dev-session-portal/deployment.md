# Workspace portal deployment

This runbook deploys the portal at
`https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/`. The implementation
session does not deploy aitherdev or the internal DNS servers.

## Revisions

- Workspace source branch: `2026-09-03-dev-session-portal`
- Workspace source: `e561db24d8ec7aaa4abc0e47a0c40e7284ccaef6`
- Configuration branch: `2026-09-03-dev-session-portal`
- Configuration source: `484baf8e48aa05c56a077472d2a4d2fbb0478f8d`

Check both revisions against `state.md` before running any helper or deployment
command:

```sh
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace rev-parse HEAD
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration rev-parse HEAD
test "$(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace rev-parse HEAD)" = \
  e561db24d8ec7aaa4abc0e47a0c40e7284ccaef6
test "$(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration rev-parse HEAD)" = \
  484baf8e48aa05c56a077472d2a4d2fbb0478f8d
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
set -o pipefail
{
  date --iso-8601=seconds
  for server in 172.16.9.90 172.19.9.90; do
    soa="$(dig "@$server" vpsfree.cz SOA +time=5 +tries=2 +noall +answer)"
    test -n "$soa"
    printf '%s\n' "$soa"
    cname="$(dig "@$server" vpsfree-cz-workspace.aitherdev.int.vpsfree.cz CNAME +time=5 +tries=2 +noall +answer)"
    printf '%s\n' "$cname"
  done
} | tee "$rollback_dns"
test "${PIPESTATUS[0]}" -eq 0
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
auth=/var/lib/vpsfree-workspace-portal-auth/htpasswd
sudo test ! -e "$auth" || { echo "password file already exists" >&2; exit 1; }
tmp="$(sudo mktemp /var/lib/vpsfree-workspace-portal-auth/.htpasswd.XXXXXX)"
nix shell nixpkgs#apacheHttpd -c sudo htpasswd -cB -C 12 "$tmp" aither
sudo chown root:nginx "$tmp"
sudo chmod 0640 "$tmp"
sudo mv -T "$tmp" "$auth"
```

Create the private CA and first leaf certificate from the reviewed workspace
revision:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace
sudo bin/workspace-pki init \
  --state-dir /var/lib/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
sudo bin/workspace-pki verify \
  --state-dir /var/lib/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
sudo bin/workspace-pki inspect \
  --state-dir /var/lib/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
sudo bin/workspace-pki install-server \
  --state-dir /var/lib/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz \
  /var/lib/vpsfree-workspace-portal-tls
```

The encrypted CA key and source leaf key remain in the root-only
`/var/lib/vpsfree-workspace-pki`. The portal process cannot read either key.
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
sudo bin/workspace-pki export-ca \
  --state-dir /var/lib/vpsfree-workspace-pki \
  /tmp/vpsfree-workspace-ca.pem
```

Do not copy the CA key, a server key, or the CA passphrase to a client.

## 3. Build and deploy aitherdev

First verify that the live workspace has integrated the reviewed helper. This
prevents an older `bin/dev-session` from mutating a portal-managed initiative:

```sh
workspace=/home/aither/workspace/ai/vpsfree.cz
git -C "$workspace" merge-base --is-ancestor \
  e561db24d8ec7aaa4abc0e47a0c40e7284ccaef6 master
test "$(git -C "$workspace" show master:bin/dev-session | sha256sum)" = \
  "$(git -C "$workspace" show e561db24d8ec7aaa4abc0e47a0c40e7284ccaef6:bin/dev-session | sha256sum)"
```

From the reviewed configuration worktree:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration
if ! systemctl cat workspace-portal-tmux.service >/dev/null 2>&1; then
  test ! -e /run/vpsfree-workspace-tmux/tmux.sock || {
    echo "inspect and remove the pre-existing portal tmux socket first" >&2
    exit 1
  }
fi
nix develop -c confctl build -y cz.vpsfree/machines/aitherdev
nix develop -c confctl deploy -y cz.vpsfree/machines/aitherdev
sudo systemctl restart nginx
```

The configuration forces nginx restarts on switches because a reload cannot
refresh supplementary groups. The explicit restart above also makes the
credential boundary unambiguous if deployment tooling behavior changes.

Check nginx, the local socket, and the TLS files before testing Codex:

```sh
systemctl status workspace-portal workspace-portal-tmux \
  workspace-codex-app-server nginx --no-pager
test "$(systemctl show workspace-portal -p Group --value)" = \
  workspace-portal-proxy
test "$(systemctl show workspace-portal -p KillMode --value)" = mixed
sudo nginx -t
sudo -u nginx curl --fail --unix-socket \
  /run/vpsfree-workspace-portal/portal.sock http://localhost/healthz
sudo lxc-attach -n vscode -- \
  test ! -e /run/vpsfree-workspace-portal/portal.sock
sudo -u nginx test -r \
  /var/lib/vpsfree-workspace-portal-tls/current/server-key.pem
portal_pid="$(systemctl show workspace-portal -p MainPID --value)"
portal_groups="$(awk '/^Groups:/{print $0}' "/proc/$portal_pid/status")"
nginx_gid="$(getent group nginx | cut -d: -f3)"
case " $portal_groups " in *" $nginx_gid "*) exit 1 ;; esac
nginx_pid="$(systemctl show nginx -p MainPID --value)"
proxy_gid="$(getent group workspace-portal-proxy | cut -d: -f3)"
nginx_groups="$(awk '/^Groups:/{print $0}' "/proc/$nginx_pid/status")"
case " $nginx_groups " in *" $proxy_gid "*) ;; *) exit 1 ;; esac
sudo -u aither test ! -r \
  /var/lib/vpsfree-workspace-portal-auth/htpasswd
sudo -u aither test ! -r \
  /var/lib/vpsfree-workspace-portal-tls/current/server-key.pem
portal_cgroup="$(systemctl show workspace-portal -p ControlGroup --value)"
mapfile -t portal_processes < "/sys/fs/cgroup${portal_cgroup}/cgroup.procs"
test "${#portal_processes[@]}" -eq 1
test "${portal_processes[0]}" = "$portal_pid"
codex_pid="$(systemctl show workspace-codex-app-server -p MainPID --value)"
codex_cgroup="$(systemctl show workspace-codex-app-server -p ControlGroup --value)"
test "$codex_pid" -gt 1
test "$codex_cgroup" != "$portal_cgroup"
sudo -u aither test -S \
  /run/vpsfree-workspace-codex/app-server.sock
sudo -u aither test -S \
  /run/vpsfree-workspace-tmux/tmux.sock
```

The independently supervised Codex service runs the same pinned package that
the Nix assertion checks. Prove that passive pages remain available while it is
stopped, then let systemd recover it:

```sh
sudo systemctl stop workspace-codex-app-server
sudo -u nginx curl --fail --unix-socket \
  /run/vpsfree-workspace-portal/portal.sock http://localhost/healthz
sudo systemctl start workspace-codex-app-server
systemctl is-active --quiet workspace-codex-app-server
sudo -u aither test -S \
  /run/vpsfree-workspace-codex/app-server.sock
```

The service uses the pinned `codex app-server` binary directly; it does not
depend on an installer-managed standalone Codex path. The portal checks the App
Server version during its protocol handshake. Restart the service after a Codex
upgrade or rollback, then check it again:

```sh
sudo systemctl restart workspace-codex-app-server
systemctl is-active --quiet workspace-codex-app-server
```

Validate every persisted manifest through both implementations before DNS is
published. This catches schema migrations that a health-only probe cannot see:

```sh
sudo -u aither -H dev-session \
  --workspace /home/aither/workspace/ai/vpsfree.cz validate
sudo -u aither -H workspace-portal validate \
  --workspace /home/aither/workspace/ai/vpsfree.cz
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

Assert missing and wrong credentials return HTTP 401. Check the name-specific
HTTP redirect and HSTS header as well:

```sh
test "$(curl --silent --output /dev/null --write-out '%{http_code}' --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /tmp/vpsfree-workspace-ca.pem \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz)" = 401
test "$(curl --silent --output /dev/null --write-out '%{http_code}' --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /tmp/vpsfree-workspace-ca.pem -u aither:wrong-password \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz)" = 401
curl --silent --show-error --head --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:80:172.16.106.40 \
  http://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz | \
  grep -i '^location: https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz'
curl --silent --show-error --head --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /tmp/vpsfree-workspace-ca.pem -u aither \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz | \
  grep -i '^strict-transport-security: max-age=31536000'
curl --fail --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /tmp/vpsfree-workspace-ca.pem -u aither \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/
curl --fail --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /tmp/vpsfree-workspace-ca.pem -u aither \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/2026-09-03-dev-session-portal/
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

From a test host that is not connected to WireGuard, the direct resolved probe
must fail to connect:

```sh
if curl --connect-timeout 5 --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /path/to/vpsfree-workspace-ca.pem \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz; then
  echo "portal was reachable outside WireGuard" >&2
  exit 1
fi
```

Open the portal in a browser and check this initiative page. Create a
disposable session with a harmless initial request. Confirm all of the
following:

- retrying the same short name does not create another session;
- the terminal attach command resumes the browser thread;
- messages sent from either client appear in the other;
- a command or file-change approval shows the complete request and related item
  before any decision;
- a permission approval is shown as terminal-only, receives no portal response,
  and remains available in the terminal client;
- archived or finalized sessions do not show mutation controls.

Archive or abandon the disposable initiative through the normal workspace
workflow. Keep the captured system paths in the deployment record after all
checks pass.

## Certificate renewal

Use the helper installed by the active NixOS system so renewal uses the pinned
workspace revision:

```sh
sudo workspace-pki renew \
  --state-dir /var/lib/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
sudo workspace-pki verify \
  --state-dir /var/lib/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
sudo workspace-pki install-server \
  --state-dir /var/lib/vpsfree-workspace-pki \
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
journalctl -u workspace-portal -u workspace-codex-app-server \
  -u workspace-portal-tmux -u nginx --since today
```

If DNS has not been deployed, restore the exact aitherdev system recorded in
step 1. The old system has no keeper service, so first stop, finalize, or move
every browser-created session that must survive. The guard below refuses a
destructive rollback while any managed session remains:

```sh
. /var/tmp/vpsfree-cz-workspace-portal-rollback.env
[[ "$previous_aitherdev_system" = /nix/store/*-nixos-system-* ]]
test -x "$previous_aitherdev_system/bin/switch-to-configuration"
active_sessions="$(sudo -u aither tmux \
  -S /run/vpsfree-workspace-tmux/tmux.sock list-sessions \
  -F '#{session_name}' 2>/dev/null | \
  grep -vx __workspace_portal_keeper || true)"
test -z "$active_sessions" || {
  printf 'refusing rollback with active portal sessions:\n%s\n' \
    "$active_sessions" >&2
  exit 1
}
sudo "$previous_aitherdev_system/bin/switch-to-configuration" switch
```

If DNS has been deployed, switch each DNS server to its separately captured
system path, verify its SOA and CNAME answers directly, and wait one hour before
restoring the old aitherdev system. This ordering keeps cached portal records
on the authenticated TLS virtual host until they expire.

The portal web service uses `KillMode=mixed`: systemd signals the Go main
process first, allowing it to wait for active HTTP creation handlers, then kills
any residual child only after the stop timeout. Browser-created tmux sessions
live in a separate keeper whose definition does not depend on the workspace
source pin. The App Server has its own systemd unit and cgroup. An ordinary
portal restart therefore tears down neither tmux sessions nor the App Server.
