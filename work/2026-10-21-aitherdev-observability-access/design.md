# Aitherdev observability access: accepted implementation design

User selected the credential-based plan and authorized “Implement the plan.”
Architect0 owns this brief; lead owns plan/state and assignment. Application changes,
technical docs and fixtures belong to the two implementers. Live secret provisioning,
deployment and default-branch integration are not authorized. No migrations.

## Scope and evidence

Change only the logger and existing Prague HTTPS proxy configuration, plus their
operational documentation and fixtures in `vpsfree-cz-configuration`. No aitherdev
system change, DNS/hosts mapping, custom client wrapper or new authentication service.
Source inventory was inspected at `37a338b25192d9271ee211110800c2dc6a094a57`; credential
refinement used locally available `38e7c837893695999e588a73f5d2a0088b8257b1`, without
fetching. Relevant logger/proxy/monitor configuration was unchanged between these.

| Current boundary | Evidence |
| --- | --- |
| Machine key is `confData.sshKeys.aither.aitherdev`, separate from human `aither.all`. | `data/ssh-keys.nix:11-27`; `configs/admins.nix:3-10` |
| Base root keys combine administrators/builders; logger imports that base. | `environments/base.nix:41-45,104`; `cluster/cz.vpsfree/containers/prg/int.log/config.nix:53-56` |
| Logger `172.16.4.1` writes `/var/log/remote/%HOSTNAME%/log` and `/var/log/messages`. | Logger `module.nix:10-23`; `config.nix:91-113` |
| Nodes/localhost rotate daily, 180 copies; other categories monthly, 13 copies; date suffixes, no compression, rsyslog HUP. | Logger `config.nix:48-50,124-183` |
| Mon1 `172.16.4.10:9090` retains up to 365d/500GB; mon2 `172.16.4.18:9090` up to 30d/60GB. | `cluster/cz.vpsfree/containers/prg/int.mon1/{module,config}.nix:15`; corresponding mon2 files `:15` |
| Raw monitor access is allowed to proxy/Grafana only; shared module listens on IPv4 9090. | Both monitor `config.nix`; `modules/services/definitions.nix:59`; `modules/clusterconf/monitor/default.nix:659-704` |
| Existing monitor HTTPS vhosts use human `/private/nginx/mon.htpasswd`; mon is a mon1 alias. | `cluster/cz.vpsfree/containers/prg/proxy/config.nix:199-213` |
| Proxy already installs Apache htpasswd tooling. | Proxy `config.nix:124-126` |

The user confirmed the machine key is manually installed in log's
`/root/.ssh/authorized_keys` and will remove it personally after log-reader works.
Do not edit that file, remove human keys, or investigate the now-resolved grant.
Keep this operator action visible; deploying the reader alone does not revoke root.

## Logger contract

- Create ordinary unprivileged `log-reader`, using the existing machine public key
  with `restrict` and **no `from=` source restriction**. Authenticate by public key
  only; enforce no forwarding, PTY, tunnels or user rc. Use root-managed authorized
  keys so the account cannot add unrestricted home keys. No sudo/wheel, Nix trust,
  broad journal/admin groups or privileged service-control permission.
- Grant dedicated `log-readers` group read/traverse access to `/var/log/remote/**`,
  `/var/log/messages` and messages archives. Keep regular files root-owned `0640`,
  directories root-owned `0750`, with necessary parent traversal. Preserve required
  existing readers and exclude exporter pipe, special files and unrelated log trees.
- Configure persistent rsyslog file/directory owner/group/modes and compatible umask;
  set logrotate replacement files to `0640 root log-readers`, preserving existing
  destinations, ingestion, rotation intervals/retention and exporter/HUP behavior.
  On the remote RainerScript `action(type="omfile" dynaFile="remote-log-file")`,
  set `fileOwner="root"`, `fileGroup="log-readers"`, `fileCreateMode="0640"`,
  `dirOwner="root"`, `dirGroup="log-readers"`, `dirCreateMode="0750"` explicitly.
  Retain `$Umask 0027` and legacy globals for the unchanged local messages selector;
  do not rely on those globals to supply the remote action's creation policy.
- Include a bounded, idempotent reconciliation of existing regular logs/directories
  and archives. Validate scope, ownership and ACL assumptions, do not follow symlinks
  or traverse foreign mounts, and do not recursively chmod all `/var/log`. Document
  inspection/recovery of pre-existing metadata and preserve required readers.
- Shell access permits remote grep/tail, home or `/tmp` writes, programs, sockets and
  ordinary log generation. The guarantee is no direct overwrite/truncate/unlink/rename
  of protected logs or production configuration, not a filesystem-read-only shell.
  Log contents are fully readable, without redaction or a resource sandbox.

Creation-policy clarification: the VM at `5d910028` created the intended nested
remote path but used `root:root 0700` directories and a `root:root 0640` file;
reconciled historical paths were correct (`runtime-verification-01.log:2310-2317`).
Explicit action parameters correct the accepted permission contract without changing
paths, wire/log formats, pipe ownership, retention or HUP behavior. They apply to new
objects only; existing incorrect metadata still needs the separate reconciliation.
This requires no new user choice. Implementer0 owns the actual-group native probe,
source/docs/fixture correction and quick checks; subsequent review and VM acceptance
must establish the correction before claiming success.

## Prometheus API and authentication

Expose `https://mon1.prg.vpsfree.cz/codex/api/v1` and the equivalent mon2 base through
existing nginx vhosts and normal public HTTPS routing. Keep their backends separate.
Generate identical allowlist/auth/limit policy for both. No source-IP authentication,
bypass, private routing requirement or new raw-9090 allowance.

| Upstream `/api/v1` endpoint | Methods |
| --- | --- |
| `/query`, `/query_range`, `/series`, `/labels` | GET, POST |
| `/label/<single valid name>/values` | GET |
| `/metadata`, `/targets`, `/targets/metadata`, `/rules`, `/alerts` | GET |
| `/status/buildinfo`, `/status/runtimeinfo` | GET |

HEAD may accompany GET under nginx method semantics. Match exact paths and one
bounded valid label-name segment; deny every unlisted path/method by default.
This excludes admin/TSDB mutation, lifecycle reload/quit, receivers, config/flags,
debug/profiling, federation, remote-read and UI routes. Test URI normalization.
Allowed routes strip only `/codex`, preserve query strings and form POST bodies,
and clear `Authorization` before proxying so backend Prometheus never receives it.

Use native HTTP Basic username `codex-aitherdev` with a separately generated random
32-byte value encoded as 64 hex characters (256 bits) as password. Store only its
bcrypt cost-8 hash server-side. Allowed locations **override** inherited human auth
with dedicated Basic auth/file, not `auth_basic off`; do not add this user to the
human file. Main vhost routes retain existing human authentication. Missing/wrong
credentials cannot reach upstream; a missing runtime file fails closed. Do not
create placeholder/default credentials during build or activation.

## Secrets and client ergonomics

- Server: `/var/lib/nginx-auth/prometheus-codex.htpasswd`, `root:nginx`, mode `0640`;
  dedicated parent `root:nginx`, mode `0750`. Reject unexpected symlink/foreign path
  ownership during provisioning; do not modify `/private` traversal permissions.
- Client: `/home/aither/.config/vpsfree-observability/prometheus.curlrc`, owned by
  aither (normal users group), mode `0600`, parent directory `0700`. Provision outside
  Git/Nix. It contains Basic username/password and HTTPS-only curl defaults: fail,
  silent/show-error, connect timeout 5s, max time 45s. No redirect-following, insecure
  TLS, verbose/trace, token in argv/environment/output, or global default curlrc.
- Document `curl -q --config PATH` against fixed mon1/mon2 HTTPS URLs, with GET query
  and form POST examples (`--get --data-urlencode` and `--data-urlencode`). No wrapper
  is needed. Recommend PromQL query `timeout=20s` and bounded ranges. File permissions
  exclude other users, not other processes/sessions running as aither or root.
- Separate future provisioning generates the token without printing it, feeds
  htpasswd through stdin (`-i -B -C 8`, never `-b` argv), and writes both files
  atomically with stated ownership/modes. Prepare the server file before activation.
  Only string runtime paths belong in Nix: no `basicAuth` attrset, `readFile`,
  `writeText`, or Home Manager content/source containing plaintext or hash material.
- Rotation atomically replaces the hash entry and client config; a brief 401 gap is
  acceptable. Optional overlap requires distinct usernames, not duplicate entries.
  Revocation removes the old entry; new requests then fail, existing requests are
  not retroactively canceled. Direct htpasswd lookup needs no nginx restart for
  routine file rotation; acceptance checks must prove old/new credential behavior.

Repository evidence supports operator-provisioned runtime secrets, not automatic
GPG deployment: `gpg/README:1-17` only covers encrypted editing; router-specific
`network-config/Makefile:1-6,17-28` encrypts/decrypts its own exports. Do not reuse its
recipients or invent a generic hook. `docs/operations/newadmin-webui.md:34-56` documents
operator-supplied private runtime files; `environments/deploy.nix:75-99` copies node
secrets only. No new encrypted backup/escrow is required. Pinned nixpkgs nginx at
`8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f`, `default.nix:560-578`, renders
`basicAuthFile` as a direct runtime path but puts `basicAuth` values into the store.

## Scoped resource limits

Apply only to the new query locations, preserving human UI/Grafana behavior:

| Setting | Accepted initial value |
| --- | --- |
| Shared request-rate zone | 1 MiB, constant nonsecret key shared by both prefixes, 2 requests/s |
| Request burst | 5, `nodelay`; rejection HTTP 429 |
| Shared concurrency zone | 1 MiB, same fixed-key scope, 4 active requests; HTTP 429 |
| `client_max_body_size` / `client_body_timeout` | 64 KiB / 10s |
| `proxy_connect_timeout` / `proxy_send_timeout` / `proxy_read_timeout` | 5s / 15s / 30s |

Do not depend on authenticated-user variables being populated in nginx's earlier
limit phases. Fixed-key quotas also bound unauthenticated bursts but allow public
clients to exhaust the small quota; they protect load, not availability. Read timeout
is inactivity-based, not a hard PromQL CPU budget. Client query timeout is courtesy,
not enforced policy. Do not change global Prometheus query limits. Full metrics and
selected operational metadata remain readable; there is no tenant isolation.

## Compatibility, eventual rollout and recovery

No database/schema migration, TSDB/log-format conversion, exporter change or fleet
update. Preserve administrator access, logging, exporter pipe, Grafana and UI auth.
The eventual rollout requires separate authorization: prepare runtime credentials
and inspect historical metadata; deploy logger/proxy; verify reader and both APIs;
user removes the manual root key. No aitherdev system deployment is needed.
Both features can roll out independently; older proxy configuration denies the new
prefix to the dedicated credential. Credential changes are independent of Nix rollback.
Rollback disables new access/reverts configuration; metadata may need restoration
from recorded prior values. Retain logs/TSDB and never silently restore root access.

## Packages and acceptance

| Owner | Files/deliverable |
| --- | --- |
| implementer0 | `cluster/cz.vpsfree/containers/prg/int.log/config.nix`, optional adjacent reader module; logger fixture; `docs/operations/log-reader-access.md`. Own account, creation/rotation/history permissions and checks. |
| implementer1 | `cluster/cz.vpsfree/containers/prg/proxy/config.nix`, optional adjacent query-policy module; auth/proxy fixtures; `docs/operations/prometheus-query-access.md`. Own API/auth/limits, provisioning and fixed curl documentation. |

Lead serializes Git operations and assigns shared README/flake-check registration to
one owner. Material deviations return through lead/architect. No application edits
by architect0. Quick checks use pinned Nix tools, evaluated accounts/auth policy and
rsyslog/logrotate/nginx syntax. Commit completed changes and run independent final
review before long integration tests; watcher workflow owns long/uncertain checks.

Disposable fixtures, using synthetic credentials, must establish:

- Reader access to current/archive/new-host logs before/after rotation; no protected
  file or directory writes, sudo/escalation, SSH forwarding/PTY/tunnel/rc; no source
  restriction. Preserve ingestion/exporter behavior and required existing readers.
  For new-path creation, start with all nested host directories absent and assert
  every created ancestor is `root:log-readers 0750`, the file is `0640`, and SSH
  reading works before any reconciliation. Repeat ingestion/readability after
  rotation/HUP; verify local messages and the exporter pipe retain their policies.
  Quick syntax/evaluation checks must cover the explicit action, while a native
  actual-group probe and the VM establish behavior; root-substituted syntax checking
  alone is not evidence that `log-readers` ownership is applied.
- Both GET/form POST query/discovery paths and GET diagnostics map correctly; query
  arguments/bodies survive; Authorization is stripped. Wrong/missing credentials,
  unknown methods/paths and encoded-path escapes never reach even a permissive stub.
- Dedicated credentials do not unlock human routes; human credentials do not unlock
  dedicated routes; no IP-based bypass, new raw-port grant or client mapping.
- Body/rate/concurrency limits and rotation/revocation work, including keepalive or
  HTTP/2 requests; secrets do not enter generated Nix content, logs or command lines.

No live provisioning, deployment or merge is included in implementation approval.
Later authorized live acceptance uses bounded reads and ordinary rotation observation,
not destructive production probes. Record the user's manual root-key step separately.

References: [OpenSSH](https://man.openbsd.org/sshd_config.5),
[rsyslog](https://docs.rsyslog.com/doc/configuration/modules/omfile.html),
[Prometheus API](https://prometheus.io/docs/prometheus/latest/querying/api/),
[nginx Basic auth](https://nginx.org/en/docs/http/ngx_http_auth_basic_module.html),
[rate limits](https://nginx.org/en/docs/http/ngx_http_limit_req_module.html),
[connection limits](https://nginx.org/en/docs/http/ngx_http_limit_conn_module.html),
[htpasswd](https://httpd.apache.org/docs/2.4/programs/htpasswd.html),
[curl](https://curl.se/docs/manpage.html).
