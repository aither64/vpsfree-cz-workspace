# Live preflight, 2026-11-10

Implementer1 package B, read-only live checks. No deployment, build, copy,
credential generation, production file write, permission/ACL change, service
action, machine claim, source edit or Git mutation was performed. HTTP probes
used no credentials and discarded bodies. Private keys, password files, root
authorized keys, log contents, journals and full environments were not inspected.

## Findings for the rollout plan

- Both root SSH targets are accessible. Logger trust was already present. Proxy
  required lead-authorized first-use trust, described below.
- Neither access feature is installed: logger reader/group/keyfile/helper are
  absent; proxy has no dedicated routes/auth path and no dedicated credential
  directory/file. The aitherdev client credential directory/file are absent.
- Existing November 2 proxy artifacts would remove already-live blog.org routing
  and upload behavior. Do not activate that artifact. Compare a fresh candidate
  from the final reviewed source against these exact live profiles first.
- Logger metadata scope is small and had no reconciliation refusal flags in this
  observation. Required readers still need operator confirmation before changing
  the world-readable local messages files to group-only access.
- Nginx supports reload. Rsyslog has no systemd reload operation. A pure nginx
  configuration update can use its existing reload mechanism, but whole-system
  activation must be checked for other unit changes. Logger configuration and
  historical metadata work need a scheduled ingestion interruption.

## Identity and exact profiles

`dev-session current` returned the bound session; both `DEV_SESSION_SLUG` and
`DEV_SESSION_WORKSPACE` were absent. The retained roster identifies implementer1
as Sol/xhigh, workspace-write, under full-access execution policy.

| Target | Configured selector | Address / container |
| --- | --- | --- |
| `log.int.prg.vpsfree.cz` | `cz.vpsfree/containers/prg/int.log` | `172.16.4.1`, VPS 14004 |
| `proxy.prg.vpsfree.cz` | `cz.vpsfree/containers/prg/proxy` | `172.16.9.140`, VPS 14096 |

Both remote `id -u` calls returned 0 and `hostname -f` matched the requested
hostname. On each host, `/run/current-system` and
`/nix/var/nix/profiles/system` resolve to the same store path:

| Target | Numeric profile link | Exact live store path |
| --- | --- | --- |
| Logger | `system-142-link` | `/nix/store/wpffkjx6cmnhm5ql9n4xv9nf62a9kl6f-nixos-system-log-26.05.20261026.718f670` |
| Proxy | `system-148-link` | `/nix/store/dbzws4cm00afxm7il48airihxc1w3srm-nixos-system-proxy-26.05.20261026.718f670` |

The configured selectors/addresses came from the repository modules; they are
not host-key verification. Initial strict proxy SSH failed because no ED25519
host key was known. `ssh-keygen -F` found no entry for the exact FQDN,
`172.16.9.140`, or short alias `proxy`. The lead explicitly authorized conventional
first use: one connection used `StrictHostKeyChecking=accept-new` and added the
proxy ED25519 key to local known_hosts. This was first-use trust, without
independent fingerprint verification. Changed-key checking remained enabled;
all subsequent probes used strict checking. No production trust file changed.

## Proxy

- Nginx 1.30.6 is active/running; unit result and reload result are success.
  Active since November 1, 20:23:58 CET. `CanReload=yes`, `Restart=always`,
  restart delay 10s; unit declares `X-StopIfChanged=false` and `ExecReload`.
- Process executable:
  `/nix/store/smpkfhyjj22b4zy1f0cprzfhr0nimllr-nginx-1.30.6/bin/nginx`.
  The process configuration argument is `/etc/nginx/nginx.conf`, which resolves
  to `/nix/store/0jh3k73bwd52fcswlqiyjwz36k02y83s-nginx.conf`.
- `nginx-config-reload.service` is loaded, inactive/dead, result success.
  HAProxy is active/running with reload support and `Restart=always`.
  Varnish is active/running, has no reload operation and uses `Restart=always`
  with a 5s restart delay. Syslog is active/running.
- On-disk nginx configuration contains no `/codex/api/v1/`, dedicated auth path
  or `prometheus_codex_rate`. It retains the existing human monitor protection.
- `/var/lib/nginx-auth` and
  `/var/lib/nginx-auth/prometheus-codex.htpasswd` are absent, by lstat only.
  Human password files were not opened or read.
- Four public HTTPS GET probes returned 401: mon1 and mon2 at
  `/codex/api/v1/query`, and both at `/`. No Authorization header was supplied.
  These statuses alone do not establish dedicated-route presence: the live
  generic human-authenticated location also returns 401 for that prefix.
- Both live blog HTTPS vhosts point to `http://172.16.8.4:80`, have their own
  matching Host headers and forwarded-proto settings. Blog.cz has a 512m body
  limit; the global body limit is 10m. Blog.org is already present. The existing
  newadmin forwarded-host header policy is present too. Only selected public
  routing/header/size facts were emitted, never a full configuration dump.
- `nginx -t` was not run: its startup/config-test path can open/create logs or
  missing runtime directories. This read-only package did not establish a
  write-free invocation. Running status is not a new syntax-validation result,
  and on-disk configuration identity is not a dump of worker memory.

### Existing artifact versus live system

The locally retained November 2 artifact is build
`2026-11-02--16-39-38`, store path
`/nix/store/12q4fmldfi4zj92kj24k4ffwhn44kgik-nixos-system-proxy-26.05.20261026.718f670`.
Its nginx source is `/nix/store/inshx34y4qnwra7s3nkb9388n1k24g8c-nginx.conf`.
It contains the dedicated query policy but lacks blog.org and the live 512m
setting. This is evidence about the retained artifact, not certification of the
currently rebased or future candidate.

Read-only comparison of generated service/socket/timer symlink identities found
267 live entries versus 264 in that artifact: 228 unchanged, 36 changed, no
additions and these three removals:

- `acme-blog.vpsfree.org.service`
- `acme-order-renew-blog.vpsfree.org.service`
- `acme-renew-blog.vpsfree.org.timer`

Changed identities included 33 renewal timers, `acme-setup.service`,
`nginx-config-reload.service` and `vpsadmin-download-mounter.service`.
The primary nginx, HAProxy and Varnish unit identities were unchanged.
Changed store identities are a risk inventory, not proof of semantic changes
or an exact activation/restart plan. Neither live system closure is present
locally; no closure was copied to expand this comparison.

## Aitherdev client

Metadata-only checks found both
`/home/aither/.config/vpsfree-observability` and its `prometheus.curlrc` absent.
No client config, password manager or default curl configuration was opened.

## Logger

- `log-reader`, `log-readers`,
  `/etc/ssh/authorized_keys.d/log-reader`, and
  `/run/current-system/sw/bin/log-reader-reconcile` are absent. No reader-specific
  key material was read. Root authorized keys were not inspected; the user's
  manual grant-removal step remains separate.
- Syslog service and socket are active/running, result success, since November 1
  around 21:19 CET. `syslog.service` has `CanReload=no`, `Restart=no`.
  Its executable is rsyslog 8.2610.0 and its configuration path is
  `/nix/store/1s10pirx6in7y8139dkyrr99iaq2j0p6-syslog.conf`.
  The new File/Dir creation-policy directives were absent.
- Actual exporter unit is `prometheus-syslog-exporter.service` (the generic
  `syslog-exporter.service` name is not found). It is active/running, success,
  as `syslog-exporter` UID 997/GID 991, with only its primary group.
  Restart policy is on-failure after 30s; no reload operation.
  `http://127.0.0.1:9102/metrics` returned 200; its body was discarded.
- Exporter FIFO `/var/log/rsyslog.pipe` is root:GID991, mode 0640.
  It was statted without opening it and is outside the reconciliation scope.
- `logrotate.timer` is active/waiting; last trigger November 10 at 15:00 CET,
  next at 16:00 CET when observed. `logrotate.service` is inactive/dead with
  successful exit status 0. `sshd.service` is active, reload-capable, and has
  `X-StopIfChanged=false`.
- `/var` and `/var/log` are root:root 0755; `/var/log/remote` is root:root 0700.
  `/var/log/messages` is root:root 0644, about 7.9 MB, with mtime
  `2026-11-10T14:44:25.333976+00:00` when observed. No contents were read.

### Historical metadata scope

An aggregate scanner inspected lstat and xattr names only, without following
symlinks or reading log contents. Scope was `/var/log/remote/**` and local
messages/current archives. Explicit bounds: 100,000 entries, depth 32,
10 elapsed seconds. It completed in 0.496s without reaching a bound:

| Observation | Result |
| --- | --- |
| Entries | 4,395 |
| Regular files | 4,300, all root:root 0644 |
| Directories | 95, all root:root 0700 |
| Maximum relative depth | 5 |
| Non-root owners or foreign groups | 0 |
| Extended/default POSIX ACL xattr names | 0 |
| Symlinks, special files, hard-linked regular files | 0 |
| Foreign-device entries, scoped mount points | 0 |
| Special mode bits or group/other writes | 0 |
| Races or permission errors observed | 0 |

The scan was not quiesced, is not an authoritative helper inventory and cannot
prove future safety. Fresh inventory/review during the authorized maintenance
window remains necessary. The helper will need the deployed `log-readers` group
before it can run. Its target changes group/modes only; it leaves the FIFO and
unrelated log trees alone.

No metadata refusal was found, so a short planned window appears reasonable.
The 0.496s metadata scan does not measure apply writes, service restart, human
review time or sender buffering. Do not promise a fixed outage duration from it.
Stop both syslog socket/service and the rotation timer/service in the eventual
procedure, and retain the documented restart traps. Remote senders may queue or
lose messages while ingestion is stopped. Rsyslog HUP used by rotation reopens
logs; systemd reload support was absent and configuration application must not
be assumed from that HUP.

`adm` and `systemd-journal` groups have no listed supplementary members, which
does not establish who reads local logs. Existing users, services and operator
tools relying on readable `/var/log/messages*` still need confirmation before
restricting access. Membership, mode and ACL inspection cannot prove that list.

## Commands, evidence and limitations

SSH used `BatchMode=yes`, `ConnectTimeout=8`, `UpdateHostKeys=no`, and strict host
checking except the explicitly authorized first proxy connection. Read-only
commands comprised `id`, `hostname`, `readlink`, selected `systemctl show`
properties, unit-name listing, `stat`/lstat, public NSS account/group queries,
metadata-only Python snippets and limited reads of generated configuration.
Python ran from an already-installed immutable store executable, with code on
stdin; no remote script was installed. Unit environment settings were not dumped.

Typical profile/status probes were:

```sh
readlink -f /run/current-system
readlink /nix/var/nix/profiles/system
readlink -f /nix/var/nix/profiles/system
systemctl show nginx.service -p ActiveState -p SubState -p Result \
  -p MainPID -p CanReload -p Restart -p RestartUSec -p ReloadResult -p FragmentPath
```

HTTPS probes used curl's first option `-q`, normal TLS verification,
`--proto '=https' --connect-timeout 5 --max-time 10 --output /dev/null`, and
`--write-out` for the status only. Selected host configuration was parsed into
booleans or public route facts rather than printed. Neither `nginx -T`, a
production inventory/apply command, nor dry activation was run.

Current workspace deployment/verification/documentation/session procedures and
both feature guides were read. Installed coordination guide selected package
`/nix/store/pyjk7mlk77yxqagi8yyd9c0w6jjp9712-dev-workspace-0.2.0`, catalog
`sha256:51d991c0f8b111fa35c95ab070c78d902a762ec24307a2dcdfde18dc782e4f43`.
No ownership was requested. The lead and architect received early findings and
the old-candidate regression gate. No claim of deployability, credential
acceptance, complete sender health or semantic whole-system equivalence is made.

Next step: review the final live-to-fresh-candidate delta and rollback artifact,
resolve required logger readers, and obtain authorization for the concrete
credential/deployment/reconciliation plan. All live changes remain pending.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-21-aitherdev-observability-access/)
