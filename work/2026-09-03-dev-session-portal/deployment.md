# Workspace portal deployment

This runbook deploys the portal at
`https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/`. The implementation
session does not deploy aitherdev or the internal DNS servers.

## Revisions

- Workspace source branch: `2026-09-03-dev-session-portal`
- Workspace source: `4dbad1fef784d66bf3c851584498412437a50c46`
- Configuration branch: `2026-09-03-dev-session-portal`
- Configuration source: `8f756aca60f3b795694d73d65cfc307dc9be6447`

Check both revisions against `state.md` before running any helper or deployment
command:

```sh
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace rev-parse HEAD
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration rev-parse HEAD
test "$(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace rev-parse HEAD)" = \
  4dbad1fef784d66bf3c851584498412437a50c46
test "$(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration rev-parse HEAD)" = \
  8f756aca60f3b795694d73d65cfc307dc9be6447
```

## 0. Establish an exclusive change window

Current `confctl` releases and older NixOS generations do not share a stable
per-machine activation mutex. This rollout therefore requires an
operator-enforced change freeze for aitherdev, `prg/int.ns1`, and `brq/int.ns1`.
Arrange the freeze with every operator and automation owner before capturing
rollback state. Pause scheduled or agent-driven deployments to these three
machines, do not run `confctl deploy`, `nixos-rebuild`, or an unguarded
`switch-to-configuration` from another shell, and retain the freeze through
successful validation or complete rollback of all three machines.

The freeze must also exclude unmanaged clients that connect directly to the
dedicated Codex App Server socket as user `aither`. Portal-managed browser and
terminal sessions participate in the lifecycle gate; arbitrary same-user
socket clients do not. Stop those clients before the rollback drain and do not
start another until the change window is released.

After coordinating the freeze, record the explicit acknowledgement. The
process checks below catch an activation already in progress; operator
coordination prevents a new one from starting after the check:

```sh
set -euo pipefail
active_pattern='[c]onfctl deploy|[n]ixos-rebuild|[s]witch-to-configuration'
test -z "$(pgrep -af "$active_pattern" || true)"
for server in 172.16.9.90 172.19.9.90; do
  test -z "$(ssh root@"$server" pgrep -af "$active_pattern" || true)"
done
read -r -p 'Type EXCLUSIVE-PORTAL-CHANGE-WINDOW to confirm the freeze: ' freeze
test "$freeze" = EXCLUSIVE-PORTAL-CHANGE-WINDOW
freeze_dir=/var/lib/vpsfree-workspace-portal-deploy
freeze_record="$freeze_dir/exclusive-change-window.active"
sudo install -d -o root -g root -m 0700 "$freeze_dir"
sudo test ! -e "$freeze_record"
{
  date --iso-8601=seconds
  id
  printf '%s\n' 'aitherdev prg/int.ns1 brq/int.ns1'
} | sudo tee "$freeze_record" >/dev/null
sudo chown root:root "$freeze_record"
sudo chmod 0600 "$freeze_record"
```

## 1. Record rollback state

First build the helper from the exact reviewed configuration commit, not from a
mutable checkout. The expected store path and NAR hash attest the resulting
closure before it is used with `sudo`:

```sh
set -euo pipefail
config_revision=8f756aca60f3b795694d73d65cfc307dc9be6447
portal_package="$(nix build --no-link --print-out-paths \
  "github:vpsfreecz/vpsfree-cz-configuration/$config_revision#workspace-portal")"
test "$portal_package" = \
  /nix/store/6ya1g5alpc99mj8s869n46z4laag7svf-workspace-portal-0.1.0
test "$(nix path-info --json-format 1 --json "$portal_package" | \
  jq -r 'to_entries[0].value.narHash')" = \
  'sha256-4wHWkm18tJRikNfkLxVHPa2APCqCdqyio/SR0rqDEFM='
rollout_helper="$portal_package/bin/workspace-portal-rollout"
test "$(stat -c %U:%G "$rollout_helper")" = root:root
test $((8#$(stat -c %a "$rollout_helper") & 8#022)) -eq 0
```

Capture the running generations as structured data in a root-owned directory.
The helper validates every value and refuses to replace an existing record; it
is never sourced as shell code:

```sh
set -euo pipefail
rollout_helper=/nix/store/6ya1g5alpc99mj8s869n46z4laag7svf-workspace-portal-0.1.0/bin/workspace-portal-rollout
config_git=/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git
git --git-dir="$config_git" fetch origin master
previous_config_revision=$(git --git-dir="$config_git" rev-parse origin/master)
previous_aitherdev_system=$(readlink -f /run/current-system)
previous_prg_dns_system=$(ssh root@172.16.9.90 readlink -f /run/current-system)
previous_brq_dns_system=$(ssh root@172.19.9.90 readlink -f /run/current-system)
sudo "$rollout_helper" capture \
  --configuration-revision "$previous_config_revision" \
  --aitherdev-system "$previous_aitherdev_system" \
  --prg-dns-system "$previous_prg_dns_system" \
  --brq-dns-system "$previous_brq_dns_system"
dns_capture="$(mktemp)"
trap 'rm -f -- "$dns_capture"' EXIT
{
  date --iso-8601=seconds
  for server in 172.16.9.90 172.19.9.90; do
    soa="$(dig "@$server" vpsfree.cz SOA +time=5 +tries=2 +noall +answer)"
    test -n "$soa"
    printf '%s\n' "$soa"
    cname="$(dig "@$server" vpsfree-cz-workspace.aitherdev.int.vpsfree.cz CNAME +time=5 +tries=2 +noall +answer)"
    printf '%s\n' "$cname"
  done
} | tee "$dns_capture"
test "${PIPESTATUS[0]}" -eq 0
sudo install -o root -g root -m 0600 "$dns_capture" \
  /var/lib/vpsfree-workspace-portal-deploy/dns-before.txt
sudo test -s /var/lib/vpsfree-workspace-portal-deploy/rollback.json
sudo test -f /var/lib/vpsfree-workspace-portal-deploy/rollback.json.lock
test "$(sudo stat -c '%U:%G %a' \
  /var/lib/vpsfree-workspace-portal-deploy/rollback.json.lock)" = 'root:root 600'
sudo test -s /var/lib/vpsfree-workspace-portal-deploy/dns-before.txt
```

Read individual fields through the strict parser when they are needed. Confirm
that all three captured generations still provide a rollback executable:

```sh
set -euo pipefail
rollout_helper=/nix/store/6ya1g5alpc99mj8s869n46z4laag7svf-workspace-portal-0.1.0/bin/workspace-portal-rollout
previous_aitherdev_system="$(sudo "$rollout_helper" get previous_aitherdev_system)"
previous_prg_dns_system="$(sudo "$rollout_helper" get previous_prg_dns_system)"
previous_brq_dns_system="$(sudo "$rollout_helper" get previous_brq_dns_system)"
test -x "$previous_aitherdev_system/bin/switch-to-configuration"
ssh root@172.16.9.90 \
  test -x "$previous_prg_dns_system/bin/switch-to-configuration"
ssh root@172.19.9.90 \
  test -x "$previous_brq_dns_system/bin/switch-to-configuration"
```

The running system paths, not a local Git reference, are the rollback authority
for each machine. The root-owned SOA and CNAME capture identifies the DNS state
that was active with those paths.

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

Use the already attested immutable package to create the private CA and first
leaf certificate. Do not run a writable worktree script as root:

```sh
set -euo pipefail
portal_package=/nix/store/6ya1g5alpc99mj8s869n46z4laag7svf-workspace-portal-0.1.0
pki_helper="$portal_package/bin/workspace-pki"
test "$(stat -c %U:%G "$pki_helper")" = root:root
test $((8#$(stat -c %a "$pki_helper") & 8#022)) -eq 0
sudo "$pki_helper" init \
  --state-dir /var/lib/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
sudo "$pki_helper" verify \
  --state-dir /var/lib/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
sudo "$pki_helper" inspect \
  --state-dir /var/lib/vpsfree-workspace-pki \
  --hostname vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
sudo "$pki_helper" install-server \
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
sudo install -d -o root -g root -m 0755 /var/tmp/vpsfree-workspace-portal-ca
sudo "$pki_helper" export-ca \
  --state-dir /var/lib/vpsfree-workspace-pki \
  /var/tmp/vpsfree-workspace-portal-ca/ca.pem
```

Do not copy the CA key, a server key, or the CA passphrase to a client.

## 3. Build and deploy aitherdev

Before the first deployment, drain development sessions from the legacy default
tmux server. The deployed portal uses a separate server and the immutable
`workspace-dev-session` wrapper. Do not use a checkout-local helper to migrate
or mutate a portal-managed initiative:

```sh
{ tmux list-sessions -F '#{session_name}\t#{@vpsfree_dev_session}' 2>/dev/null || true; } | \
  awk -F '\t' '$2 == "1" { found = 1; print > "/dev/stderr" } END { exit found }'
```

Start every machine operation from a fresh detached checkout of the exact
reviewed commit. Build and deploy each machine from that same checkout so
`confctl deploy --generation` activates the exact generation that was already
inspected and recorded. Generated `.confctl`, `.bin`, and `.bundle` state may
appear only after the initial cleanliness check:

```sh
set -euo pipefail
config_git=/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git
config_revision=8f756aca60f3b795694d73d65cfc307dc9be6447
git --git-dir="$config_git" fetch origin 2026-09-03-dev-session-portal
test "$(git --git-dir="$config_git" rev-parse \
  origin/2026-09-03-dev-session-portal)" = "$config_revision"
new_reviewed_checkout() {
  checkout="$(mktemp -d /var/tmp/vpsfree-workspace-config.XXXXXX)"
  git clone --quiet --shared --no-checkout "$config_git" "$checkout"
  git -C "$checkout" checkout --quiet --detach "$config_revision"
  test "$(git -C "$checkout" rev-parse HEAD)" = "$config_revision"
  test -z "$(git -C "$checkout" status --porcelain=v1 \
    --untracked-files=all)"
  printf '%s\n' "$checkout"
}
if ! systemctl cat workspace-portal-tmux.service >/dev/null 2>&1; then
  test ! -e /run/vpsfree-workspace-tmux/tmux.sock || {
    echo "inspect and remove the pre-existing portal tmux socket first" >&2
    exit 1
  }
fi
aitherdev_checkout="$(new_reviewed_checkout)"
(cd "$aitherdev_checkout" && \
  nix develop -c confctl build -y cz.vpsfree/machines/aitherdev)
aitherdev_generation_link="$aitherdev_checkout/.confctl/generations/cz.vpsfree:machines:aitherdev/current"
test -L "$aitherdev_generation_link"
aitherdev_generation="$(basename "$(readlink "$aitherdev_generation_link")")"
target_aitherdev_system="$(readlink -f "$aitherdev_generation_link/toplevel")"
test -x "$target_aitherdev_system/bin/switch-to-configuration"
# Abort if another deployment advanced the host after rollback capture. The
# captured generation must still be the immediate predecessor.
rollout_helper=/nix/store/6ya1g5alpc99mj8s869n46z4laag7svf-workspace-portal-0.1.0/bin/workspace-portal-rollout
captured_aitherdev_system="$(sudo "$rollout_helper" get previous_aitherdev_system)"
test "$(readlink -f /run/current-system)" = "$captured_aitherdev_system" || {
  echo "aitherdev changed after rollback capture; aborting deployment" >&2
  exit 1
}
test "$target_aitherdev_system" != "$captured_aitherdev_system"
# Record the exact built target before activation. A caller can disconnect or
# return failure after the generation has already become live.
sudo "$rollout_helper" record-deployed \
  --machine aitherdev --system "$target_aitherdev_system"
if ! (cd "$aitherdev_checkout" && \
  nix develop -c confctl deploy -y \
    --generation "$aitherdev_generation" cz.vpsfree/machines/aitherdev); then
  observed_aitherdev_system="$(readlink -f /run/current-system)"
  case "$observed_aitherdev_system" in
    "$captured_aitherdev_system")
      # Activation may have changed services before leaving the profile on the
      # predecessor. Reapply it instead of treating this as a no-op.
      sudo "$captured_aitherdev_system/bin/switch-to-configuration" switch
      ;;
    "$target_aitherdev_system")
      portal_command="$(dirname "$rollout_helper")/workspace-portal"
      sudo "$rollout_helper" rollback-host \
        --authority-dir /run/vpsfree-workspace-authority \
        --codex-socket /run/vpsfree-workspace-codex/app-server.sock \
        --portal-command "$portal_command" \
        --dedicated-tmux-socket /run/vpsfree-workspace-tmux/tmux.sock
      ;;
    *)
      echo "aitherdev reached an unrecognized generation; manual recovery required" >&2
      exit 1
      ;;
  esac
  exit 1
fi
deployed_aitherdev_system="$(readlink -f /run/current-system)"
test "$deployed_aitherdev_system" = "$target_aitherdev_system"
sudo systemctl restart nginx
```

Retain the detached checkout until deployment validation and rollback testing
are complete. They contain no rollback authority; the root-owned JSON record
does.

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

Migrate this initiative onto the dedicated runtime before validating all
manifests. The recorded thread ID is authoritative: the helper resumes that
exact conversation and refreshes its working directory and complete deployed
environment. It does not select another thread by working directory.

```sh
sudo -u aither -H workspace-dev-session start \
  2026-09-03-dev-session-portal --as-is --no-attach
```

Validate every persisted manifest through both implementations before DNS is
published. This catches schema migrations that a health-only probe cannot see:

```sh
sudo -u aither -H workspace-dev-session validate
sudo -u aither -H workspace-portal validate \
  --workspace /home/aither/workspace/ai/vpsfree.cz
```

The portal controls are authorized by host-only runtime records, not by the
workspace-owned manifests. Confirm the authority directory cannot be reached
from the development container and that an ordinary session creates an
owner-only record:

```sh
test "$(stat -c '%U:%G %a' /run/vpsfree-workspace-authority)" = \
  'aither:users 700'
test "$(stat -c '%U:%G %a' /run/vpsfree-workspace-authority.lock)" = \
  'aither:users 600'
sudo lxc-attach -n vscode -- \
  test ! -e /run/vpsfree-workspace-authority
sudo lxc-attach -n vscode -- \
  test ! -e /run/vpsfree-workspace-authority.lock
smoke_session="$(sudo -u aither -H workspace-dev-session \
  start portal-authority-smoke --no-attach --no-codex --json)"
smoke_slug="$(printf '%s' "$smoke_session" | jq -er '.slug')"
test -n "$smoke_slug"
authority=/run/vpsfree-workspace-authority/$smoke_slug.json
test "$(stat -c '%U:%G %a' "$authority")" = 'aither:users 600'
sudo lxc-attach -n vscode -- test ! -e "$authority"
sudo -u aither -H workspace-dev-session \
  stop "$smoke_slug" --as-is
test ! -e "$authority"
```

The smoke initiative remains active but stopped so its tracking can be
inspected. Finalize or abandon it through the normal workflow after the rest of
the deployment checks.

Test HTTPS and Basic Authentication before publishing DNS. Curl prompts for
the password without placing it in shell history:

```sh
curl --fail --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /var/tmp/vpsfree-workspace-portal-ca/ca.pem \
  -u aither \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz
```

Assert missing and wrong credentials return HTTP 401. Check the name-specific
HTTP redirect and HSTS header as well:

```sh
test "$(curl --silent --output /dev/null --write-out '%{http_code}' --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /var/tmp/vpsfree-workspace-portal-ca/ca.pem \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz)" = 401
test "$(curl --silent --output /dev/null --write-out '%{http_code}' --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /var/tmp/vpsfree-workspace-portal-ca/ca.pem -u aither:wrong-password \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz)" = 401
curl --silent --show-error --head --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:80:172.16.106.40 \
  http://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz | \
  grep -i '^location: https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz'
curl --silent --show-error --head --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /var/tmp/vpsfree-workspace-portal-ca/ca.pem -u aither \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz | \
  grep -i '^strict-transport-security: max-age=31536000'
curl --fail --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /var/tmp/vpsfree-workspace-portal-ca/ca.pem -u aither \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/
curl --fail --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /var/tmp/vpsfree-workspace-portal-ca/ca.pem -u aither \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/2026-09-03-dev-session-portal/
```

## 4. Deploy both internal DNS servers

Deploy DNS only after the pre-DNS HTTPS test succeeds. Re-establish the exact
source check even when this is a new shell, and give every build and deploy its
own clean checkout:

```sh
set -euo pipefail
config_git=/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git
config_revision=8f756aca60f3b795694d73d65cfc307dc9be6447
git --git-dir="$config_git" fetch origin 2026-09-03-dev-session-portal
test "$(git --git-dir="$config_git" rev-parse \
  origin/2026-09-03-dev-session-portal)" = "$config_revision"
new_reviewed_checkout() {
  checkout="$(mktemp -d /var/tmp/vpsfree-workspace-config.XXXXXX)"
  git clone --quiet --shared --no-checkout "$config_git" "$checkout"
  git -C "$checkout" checkout --quiet --detach "$config_revision"
  test "$(git -C "$checkout" rev-parse HEAD)" = "$config_revision"
  test -z "$(git -C "$checkout" status --porcelain=v1 \
    --untracked-files=all)"
  printf '%s\n' "$checkout"
}
prg_dns_checkout="$(new_reviewed_checkout)"
(cd "$prg_dns_checkout" && \
  nix develop -c confctl build -y cz.vpsfree/containers/prg/int.ns1)
prg_dns_generation_link="$prg_dns_checkout/.confctl/generations/cz.vpsfree:containers:prg:int.ns1/current"
test -L "$prg_dns_generation_link"
prg_dns_generation="$(basename "$(readlink "$prg_dns_generation_link")")"
target_prg_dns_system="$(readlink -f "$prg_dns_generation_link/toplevel")"
test -x "$target_prg_dns_system/bin/switch-to-configuration"
brq_dns_checkout="$(new_reviewed_checkout)"
(cd "$brq_dns_checkout" && \
  nix develop -c confctl build -y cz.vpsfree/containers/brq/int.ns1)
brq_dns_generation_link="$brq_dns_checkout/.confctl/generations/cz.vpsfree:containers:brq:int.ns1/current"
test -L "$brq_dns_generation_link"
brq_dns_generation="$(basename "$(readlink "$brq_dns_generation_link")")"
target_brq_dns_system="$(readlink -f "$brq_dns_generation_link/toplevel")"
test -x "$target_brq_dns_system/bin/switch-to-configuration"
rollout_helper=/nix/store/6ya1g5alpc99mj8s869n46z4laag7svf-workspace-portal-0.1.0/bin/workspace-portal-rollout
captured_prg_dns_system="$(sudo "$rollout_helper" get previous_prg_dns_system)"
test "$(ssh root@172.16.9.90 readlink -f /run/current-system)" = \
  "$captured_prg_dns_system" || {
  echo "prg internal DNS changed after rollback capture; aborting deployment" >&2
  exit 1
}
test "$target_prg_dns_system" != "$captured_prg_dns_system"
sudo "$rollout_helper" record-deployed \
  --machine prg-dns --system "$target_prg_dns_system"
if ! (cd "$prg_dns_checkout" && \
  nix develop -c confctl deploy -y \
    --generation "$prg_dns_generation" cz.vpsfree/containers/prg/int.ns1); then
  observed_prg_dns_system="$(ssh root@172.16.9.90 readlink -f /run/current-system)"
  case "$observed_prg_dns_system" in
    "$captured_prg_dns_system"|"$target_prg_dns_system")
      ssh root@172.16.9.90 \
        "$captured_prg_dns_system/bin/switch-to-configuration switch"
      ;;
    *)
      echo "prg internal DNS reached an unrecognized generation; manual recovery required" >&2
      exit 1
      ;;
  esac
  exit 1
fi
deployed_prg_dns_system="$(ssh root@172.16.9.90 readlink -f /run/current-system)"
test "$deployed_prg_dns_system" = "$target_prg_dns_system"
captured_brq_dns_system="$(sudo "$rollout_helper" get previous_brq_dns_system)"
test "$(ssh root@172.19.9.90 readlink -f /run/current-system)" = \
  "$captured_brq_dns_system" || {
  echo "brq internal DNS changed after rollback capture; aborting deployment" >&2
  exit 1
}
test "$target_brq_dns_system" != "$captured_brq_dns_system"
sudo "$rollout_helper" record-deployed \
  --machine brq-dns --system "$target_brq_dns_system"
if ! (cd "$brq_dns_checkout" && \
  nix develop -c confctl deploy -y \
    --generation "$brq_dns_generation" cz.vpsfree/containers/brq/int.ns1); then
  observed_brq_dns_system="$(ssh root@172.19.9.90 readlink -f /run/current-system)"
  case "$observed_brq_dns_system" in
    "$captured_brq_dns_system"|"$target_brq_dns_system")
      ssh root@172.19.9.90 \
        "$captured_brq_dns_system/bin/switch-to-configuration switch"
      ;;
    *)
      echo "brq internal DNS reached an unrecognized generation; manual recovery required" >&2
      exit 1
      ;;
  esac
  exit 1
fi
deployed_brq_dns_system="$(ssh root@172.19.9.90 readlink -f /run/current-system)"
test "$deployed_brq_dns_system" = "$target_brq_dns_system"
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
set -euo pipefail
rollout_helper=/nix/store/6ya1g5alpc99mj8s869n46z4laag7svf-workspace-portal-0.1.0/bin/workspace-portal-rollout
previous_prg_dns_system="$(sudo "$rollout_helper" get previous_prg_dns_system)"
deployed_prg_dns_system="$(sudo "$rollout_helper" get deployed_prg_dns_system)"
previous_brq_dns_system="$(sudo "$rollout_helper" get previous_brq_dns_system)"
deployed_brq_dns_system="$(sudo "$rollout_helper" get deployed_brq_dns_system)"
current_prg_dns_system="$(ssh root@172.16.9.90 readlink -f /run/current-system)"
current_brq_dns_system="$(ssh root@172.19.9.90 readlink -f /run/current-system)"
test "$current_prg_dns_system" = "$previous_prg_dns_system" || \
  test "$current_prg_dns_system" = "$deployed_prg_dns_system"
test "$current_brq_dns_system" = "$previous_brq_dns_system" || \
  test "$current_brq_dns_system" = "$deployed_brq_dns_system"
ssh root@172.16.9.90 \
  "current=\$(readlink -f /run/current-system); \
   test \"\$current\" = '$previous_prg_dns_system' && exit 0; \
   test \"\$current\" = '$deployed_prg_dns_system' && \
   exec '$previous_prg_dns_system/bin/switch-to-configuration' switch"
ssh root@172.19.9.90 \
  "current=\$(readlink -f /run/current-system); \
   test \"\$current\" = '$previous_brq_dns_system' && exit 0; \
   test \"\$current\" = '$deployed_brq_dns_system' && \
   exec '$previous_brq_dns_system/bin/switch-to-configuration' switch"
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

From a routed test host that is not connected to WireGuard, first prove the
path to aitherdev with the separately allowed SSH port, then prove both portal
ports are blocked. If the positive control fails, the negative probes are
inconclusive and must not be accepted as firewall validation:

```sh
set -euo pipefail
ip route get 172.16.106.40
nix shell nixpkgs#netcat -c nc -vz -w 5 172.16.106.40 2222
if curl --connect-timeout 5 --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:80:172.16.106.40 \
  http://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz; then
  echo "portal HTTP was reachable outside WireGuard" >&2
  exit 1
fi
if curl --connect-timeout 5 --resolve \
  vpsfree-cz-workspace.aitherdev.int.vpsfree.cz:443:172.16.106.40 \
  --cacert /path/to/vpsfree-workspace-ca.pem \
  https://vpsfree-cz-workspace.aitherdev.int.vpsfree.cz/healthz; then
  echo "portal HTTPS was reachable outside WireGuard" >&2
  exit 1
fi
```

On aitherdev, inspect `sudo iptables -nvL nixos-fw` before and after these
probes and confirm the rejected packets increment the non-VPN path while the
allow rule is limited to source subnet `172.16.107.0/24`. A timeout alone is
not evidence of the intended rule.

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

## Release the exclusive change window

Release the externally coordinated freeze only after all aitherdev and DNS
validation succeeds, or after rollback of every changed machine is complete.
Retain the acknowledgement as an audit record, then resume paused automation:

```sh
set -euo pipefail
freeze_dir=/var/lib/vpsfree-workspace-portal-deploy
sudo test -f "$freeze_dir/exclusive-change-window.active"
completed="exclusive-change-window.completed-$(date -u +%Y%m%dT%H%M%SZ)"
sudo mv -T "$freeze_dir/exclusive-change-window.active" \
  "$freeze_dir/$completed"
sudo test -f "$freeze_dir/$completed"
```

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

If DNS has been deployed, first switch each DNS server to its separately
captured system path by reading it through `workspace-portal-rollout get`,
verify its SOA and CNAME answers directly, and wait one hour. Whether DNS was
deployed or not, use the guarded host rollback below immediately before
restoring aitherdev. The old system has no keeper service, so first stop and
finalize or abandon every session created after deployment that must survive.
This includes terminal-created sessions: the deployed environment records all
of them in the host-only authority directory. Keep the exclusive change window
active until every changed machine has been restored and verified. Also stop
every unmanaged same-user client of the dedicated App Server socket; such a
client does not participate in the portal authority gate and could otherwise
start a turn between the idle scan and service shutdown.

Stopping the portal drains active creation handlers before the checks. If a
host authority record, managed session, or App Server turn remains active, the
block restarts the App Server and portal and refuses the destructive rollback:

```sh
set -euo pipefail
rollout_helper=/nix/store/6ya1g5alpc99mj8s869n46z4laag7svf-workspace-portal-0.1.0/bin/workspace-portal-rollout
portal_command="$(dirname "$rollout_helper")/workspace-portal"
sudo "$rollout_helper" rollback-host \
  --authority-dir /run/vpsfree-workspace-authority \
  --codex-socket /run/vpsfree-workspace-codex/app-server.sock \
  --portal-command "$portal_command" \
  --dedicated-tmux-socket /run/vpsfree-workspace-tmux/tmux.sock
```

The helper first verifies that the current host generation is exactly the
recorded deployment; the recorded predecessor is an idempotent no-op and any
third generation is refused. It then stops and drains the portal, takes the
exclusive host lifecycle gate, requires the authority directory to be empty,
requires the dedicated tmux server to contain only its keeper, verifies every
thread currently loaded in the dedicated App Server is idle, stops the App
Server, and switches to the exact predecessor. The loaded-thread enumeration
includes portal, exec, subagent, and ephemeral in-memory threads without
depending on persisted-list source or archive filters. Terminal helper commands
take a shared gate and use this same tmux server. The rollback helper restarts
the App Server and portal on any failed pre-switch check and never reads
rollback authority from the workspace.

The DNS-first ordering keeps cached portal records on the authenticated TLS
virtual host until they expire. Do not restore aitherdev after DNS rollback by
using an unguarded switch command.

The portal web service uses `KillMode=mixed`: systemd signals the Go main
process first, allowing it to wait for active HTTP creation handlers, then kills
any residual child only after the stop timeout. Browser-created tmux sessions
live in a separate keeper whose definition does not depend on the workspace
source pin. The App Server has its own systemd unit and cgroup. An ordinary
portal restart therefore tears down neither tmux sessions nor the App Server.
