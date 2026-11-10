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
- Provision manually: enter the same strong secret at interactive `htpasswd`
  prompts (`-B -C 8`, never `-b` argv) and in the private client config using an
  editor. No generated/distributed secret automation or inline Python is required.
  Prepare the server file before activation and preserve the stated modes.
  Only string runtime paths belong in Nix: no `basicAuth` attrset, `readFile`,
  `writeText`, or Home Manager content/source containing plaintext or hash material.
- Rotation updates the hash entry and private client config; a brief 401 gap is
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

## Deployment documentation refresh (2026-11-02)

Scope remains the two existing operation pages in `vpsfree-cz-configuration`;
README and MkDocs already link both. No feature redesign or new procedure framework.
Implementer0 owns rebase, final documentation edits and their checks; this brief
does not authorize live access, provisioning, deployment or integration.

- Add concrete repository deployment steps for `cz.vpsfree/containers/prg/int.log`
  (`log.int.prg.vpsfree.cz`) and `cz.vpsfree/containers/prg/proxy`
  (`proxy.prg.vpsfree.cz`), using pinned confctl commands and recorded prior
  generations. The two packages are independent; no monitor or aitherdev system
  deployment is required. Verify any explicit-generation rollback syntax locally.
- Provision the proxy runtime hash and aither-owned home curl configuration before
  activating proxy access. The manual procedure below supersedes the earlier
  automated recipe and its temporary remote Python prerequisite.
- Make logger quiescing/reconciliation restore ingestion and the rotation timer
  on inventory/apply failure or interruption, as well as success. Preserve the
  private inventory, manual review and bounded downtime; do not blindly reuse a
  stale inventory after ingestion resumes. No automatic historical reconciliation.
- Keep bounded live acceptance for current/historical/new logs, both HTTPS routes
  and existing human access. State the confirmed manual root-key grant accurately;
  only the user removes that root entry after acceptance.
- Separate configuration rollback from permissions recovery and credential
  revocation; preserve logs, exporter behavior and the private recovery inventory.
  Remove workspace watcher/review orchestration from these operator pages while
  retaining useful repository verification references. Final source checks should
  confirm target names, unit names, provisioning prerequisites and rollback syntax.

## Operator procedure simplification (2026-11-02)

Implementer0 owns only the two existing access guides. No application/helper,
authentication, runtime-path or deployment-target changes are needed. The previous
Python recipe automated distribution, metadata checks and atomic replacement;
those mechanisms are unnecessary for an operator entering one secret on two hosts.

- Proxy: ordinary `install -d -o root -g nginx -m 0750`, `umask 077`, interactive
  `htpasswd -c -B -C 8 FILE codex-aitherdev` for initial creation, then
  `chown root:nginx FILE` and `chmod 0640 FILE`. Rotation omits `-c`.
  Remove all inline Python and temporary Python/Nix environment preparation.
- Aitherdev: create the dedicated directory/file as aither with `0700`/`0600`,
  edit the curl config privately with the same password, then show the existing
  fixed-URL GET/form-POST commands. Retain strong-secret guidance and curl defaults;
  no plaintext in shell history, arguments, environment, captured output or Git.
- Logger: retain the existing scoped inventory/apply helper unchanged. Put its
  short maintenance-window happy path first, with review and a compact restart
  guard; put refusal/recovery details after it. Active ingestion/rotation can
  change identities; existing group/ACL readers must be preserved. Keep the
  private inventory and user-owned root-key removal; no recursive blanket chmod.
- Check only the changed snippets: shell syntax/restart behavior, interactive
  htpasswd flags, final modes and curl-config parsing with synthetic credentials.
  No live commands or secrets during documentation checks; no new test framework.

## Deployment preparation (2026-11-10)

This is a plan, not authorization to activate, provision credentials, change live
permissions, stop/reload services or merge. Architect0 owns this brief;
implementer0 owns rebase/evidence and implementer1 owns read-only live preflight.
Existing operation guides remain the reusable procedures. This session holds
individual revisions, system paths, preflight results and later execution receipts.

Targets are `cz.vpsfree/containers/prg/int.log` (`log.int.prg.vpsfree.cz`) and
`cz.vpsfree/containers/prg/proxy` (`proxy.prg.vpsfree.cz`). Deploy independently,
logger first; no monitor or aitherdev system deployment. No migration or log/TSDB
format change is involved. Runtime credentials and historical file metadata are
independent of Nix generation rollback.

Reported preflight: logger is generation 142 at
`/nix/store/wpffkjx6cmnhm5ql9n4xv9nf62a9kl6f-nixos-system-log-26.05.20261026.718f670`;
proxy is generation 148 at
`/nix/store/dbzws4cm00afxm7il48airihxc1w3srm-nixos-system-proxy-26.05.20261026.718f670`.
Each profile matches its running system. Logger syslog/socket, rotation timer and
syslog exporter are active; reader account/group/helper are absent. Remote root
is `root:root 0700`; messages is `0644`. Proxy nginx is running and supports reload;
client credential file/directory are absent. Proxy SSH used lead-authorized
first-use trust, not independent host-key verification. Unauthenticated monitor
401 responses alone do not establish that the dedicated routes exist.
Exact observations and limitations are in
[live preflight](live-preflight-2026-11-10.md).

Full logger metadata scan found 4,395 entries (4,300 files `0644`, 95 directories
`0700`), all root:root, maximum depth 5, and no helper refusal flags including
ACLs, links, mounts or foreign groups. On Nov10 the user answered the existing
reader question: "No other readers that I know of". The known-reader prerequisite
is resolved; unexpected ownership, ACLs or readers still require inventory review.
Live proxy already has the blog aliases, 10m/512m body limits and newadmin
forwarded-host policy, but lacks the codex routes/rate zone/auth path; dedicated
server credential paths are absent. The old Nov2 candidate lacks live blog.org
configuration and would remove three ACME units: discard it as a deployment
candidate, preserving it only as historical verification evidence.
The live syslog service has no systemd reload operation; rotation's HUP only
reopens logs and is not evidence of configuration application. Plan a scheduled
logger interruption, preserving the exporter FIFO (`root:GID991 0640`). The
0.496-second metadata scan was neither quiesced nor the helper's final inventory;
it does not bound apply, restart, review time or sender loss.

Rebase target reported by implementer0 is master
`0f3897b5b7dc53edee33f1289cbda25ec28910f5` (+27 commits): nixpkgs/confctl unchanged,
seven other lock nodes changed; proxy baseline adds blog and route/header/upload
changes. Logger source baseline is unchanged. The mechanical rebase head is
`54b4f2737461ecca88d4e62c68df5e89f6f01ea9`, tree
`8bdfa6b5b7ada0201caed2dcd9cbdb7faaca7814`; implementer0 proved aggregate-patch
equivalence apart from registration/context resolutions. The final guide commit
is frozen for review at `959e1d54cabc7ac5530dac6179acacb077a57754`; quick checks
passed. Exact input/rebase evidence is in
[the refresh receipt](rebase-refresh-2026-11-10.md). Both targets include changed
`vpsadminosOsStaging`; proxy also selects changed `vpsadminServices`. All four
fixture derivations match Nov2 success receipts, but their realized outputs are
absent locally: this is retained evidence, not a fresh runtime check. Neither
exact live closure nor a new candidate closure is currently available locally.

1. Finish the mechanical rebase and record base/head, input graph and patch
   equivalence. Reuse prior independent review only for equivalent covered work;
   changed inputs limit runtime-check reuse. Routine session planning requires no
   independent review. A substantive guide correction follows normal final review.
2. Prefer pure evaluation for an initial delta assessment; before any later
   activation, build/check exact target closures as needed and preserve the
   live rollback closures and generation mappings, and compare the whole live
   system with the candidate: packages, units, activation actions and nginx config.
   `confctl diff` compares inputs, not service effects. Native `dry-activate`
   invokes candidate switch/dry-activation scripts: use it only after preparation
   and later execution approval, not as a read-only check in this planning turn.
   Validate candidate nginx config with its runtime TLS/auth files before switch.
   Unrelated proxy
   changes not already live require explicit disposition; stop for broader service
   restarts, network changes, reboot or outage beyond the agreed nginx reload/brief
   restart. Do not turn this access change into a global update or bypass restart
   handling. Source diff or `enableReload = true` alone does not prove safety.
3. Once execution is authorized, stage artifacts before machine reservations;
   acquire/verify each exact confctl target near mutation. Preserve rollback and
   ordinary confctl health checks. Deploy logger, then use the existing inventory/
   apply helper during a brief ingestion/rotation pause with restart traps.
   First account for existing world-readable-message consumers and any newly
   discovered groups/ACL readers or scope refusals; review the expected scope
   before stopping ingestion so the final inventory review stays short;
   retain private original metadata. No blanket chmod, forced rotation or helper
   expansion. On refusal/partial failure, restore ingestion and inspect recorded
   metadata; renewed ingestion requires a fresh inventory before another attempt.
4. Provision the dedicated proxy hash interactively with `htpasswd -B -C 8`
   (`-c` only for a new file); preserve root:nginx `0640`, parent `0750`.
   Enter the same strong random password in aither's private curl config (`0600`,
   parent `0700`) using the existing guide. No inline Python or secret output.
   Keep the human auth file untouched. Complete this before proxy activation.
5. Validate the candidate nginx configuration, then activate with reload preferred
   and old workers serving; a brief nginx restart is acceptable only within the
   user's stated outage bound. No deliberate proxy stop/maintenance window.
   Check existing proxy sites immediately; failure to return promptly to baseline
   means restore the recorded known-good generation, not prolonged live repair.
6. Verify bounded SSH reads of current/archive remote logs and messages, normal
   ingestion and exporter health, new-directory modes and scheduled rotation.
   Observe normal creation/rotation; record any still-pending live check explicitly.
   On both monitor HTTPS names, verify small GET and form-POST queries, intended
   distinct backends, missing/wrong-credential rejection and unchanged human access
   and other proxy sites. Use private curl config; no destructive denial probes,
   load tests or credential/header output. The user removes the manual logger root
   key only after reader acceptance; no automation edits root authorized_keys.
7. Rollback configuration via the retained exact generation. Revoke dedicated
   credentials separately if needed; restore historical metadata only for reviewed
   matching inodes with reader access disabled and ingestion safely quiesced.
   Retain logs/exporter state. Reconcile uncertain commands. Machine release follows
   verified deployment plus integrated deployed lineage; integration needs separate
   explicit approval. This plan acquires no claim and performs no live mutation.

Documentation assessment: existing README links and both operation pages satisfy
the updated placement rules; no relocation/new page is needed. At most add a short
reusable proxy deployment note about comparing live/candidate changes, preferring
reload and stopping for broader disruption. Keep Nov10 paths/revisions here.

## Authorized execution and workspace usage guide (2026-11-10)

The user's later instruction, "ok, deploy it and then once it is verified, the
work can be merged", supersedes the planning-only phase above: lead owns claims,
activation and configuration/master integration after verified deployment. The
known-reader answer remains resolved. Configuration source stays frozen at
`959e1d54cabc7ac5530dac6179acacb077a57754` unless a concrete defect requires correction.

Implementer1 owns one documentation package in the requested
`aither64/vpsfree-cz-workspace` repository, using its registered initiative
worktree. No adequate usage guide or README exists. Files:

- Add `docs/how-to/observability-access.md`: prerequisites on aitherdev, bounded
  `ssh -T log-reader@log.int.prg.vpsfree.cz` examples for current/archive logs and
  messages; fixed mon1/mon2 HTTPS `curl -q --config` GET/form-POST query examples,
  using `/home/aither/.config/vpsfree-observability/prometheus.curlrc`, bounded
  ranges and `timeout=20s`. Explain ordinary shell access to logs and shared
  host-user credential scope briefly. Missing access goes to the maintainer,
  without routine root/sudo fallback or credential exposure.
- Add one opening-paragraph link in `AGENTS.md`; no new README or routing framework.
- Correct the current-access recommendation in
  `notes/vpsfree-cz-configuration/2026-09-14-central-node-log-investigation.md`
  with a short guide pointer, preserving the historical fact that that investigation
  used root and retaining its layout/attribution findings.

Link provisioning/revocation authority to the two configuration operation guides
at immutable GitHub commit `959e1d54cabc7ac5530dac6179acacb077a57754`, valid before
and after integration. Do not copy account setup, password entry, permission
repair, deployment or rollback instructions into this usage guide; no passwords,
new wrapper, API service, input changes or system deployment. Describe prerequisites,
not an unverified claim that access is already live. Preserve all API/auth/runtime
paths. Updated documentation/knowledge-base procedures and documentation skill
apply; lead owns the final prose pass before commit. Acceptance is usable bounded
commands, correct links and unchanged technical meaning; check examples against
the frozen runbooks and do local syntax/link checks, without live probes, secrets,
builds or a new test harness. Independent final review covers this docs package.

## Native rollback for the retained live generations (2026-11-10)

No local confctl build NAME matches either live system. This rollout can use the
existing remote system profile generations: logger 142 and proxy 148, guarded by
the exact store paths recorded above and rechecked by the lead. Retain those
generation links and closures; do not prune during rollout or invent local build
metadata. On the affected host, the recovery sequence is native
`nix-env --profile /nix/var/nix/profiles/system --switch-generation NUMBER`, then
the recorded old closure's `bin/switch-to-configuration switch`. A profile change
alone does not reactivate services. Verify both the system profile and
`/run/current-system` resolve to the old closure and repeat host/service acceptance.
If activation fails, inspect the actual partial state and keep the machine claim;
do not declare recovery from the profile pointer alone or retry blindly.

This uses the documented [Nix profile generation operation](https://nix.dev/manual/nix/2.34/command-ref/nix-env/switch-generation)
and the same exact-closure activation primitive as pinned confctl
`7bee58a52372b95c2198ce3f2a719807a3c2c66b` (`lib/confctl/nix_legacy.rb:274-277`,
`libexec/auto-rollback.rb:55-61`). Confctl's local selector instead reads
`Generation::BuildList` (`lib/confctl/cli/cluster.rb:1302-1317`); remote 142/148
must never be passed as supposed local build names. Keep normal deployment
auto-rollback and health checks. Credentials and historical log metadata remain
separate recovery concerns.

Record this explicit alternative to the guides' confctl-NAME precondition in the
individual rollout receipt. No source correction is required before deployment:
the frozen guides describe the confctl path, while this verified recovery uses
retained native profiles. A generic fallback expansion is unnecessary for this
bounded execution package; keep configuration source frozen.
