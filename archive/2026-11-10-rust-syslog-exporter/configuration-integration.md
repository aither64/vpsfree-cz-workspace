# Package C: configuration integration investigation

Owner: implementer1. Planning and source inspection only, 2026-11-10. Architect0
owns the design; implementer0 owns the exact Ruby/parser/HTTP/metric contract.
No project edits, commits, evaluations, builds, deployment, production SSH or
external mutations were performed. This document proposes later work, not an
approved rollout.

## Evidence and baseline

Session identity was verified with `dev-session current` and both environment
identity variables: `2026-11-10-rust-syslog-exporter`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. The live same-session roster preserves
implementer1 Sol/xhigh/workspace_write and architect0 Astra/xhigh/workspace_write.

Canonical configuration source: `repos/vpsfree-cz-configuration.git`, remote default
`origin/master` **3c088a4b71881b3649441ce3c4e92c71757708e6**, freshly fetched by
the lead. Initial local master inspection was at
`86e19685313270d88e4db30038c056ce4b807abd`; the scoped comparison and fresh reads
supersede that baseline. Exporter package/service, overlay, logging sender modules,
AGENTS.md and syslog alert rules have no changes between those revisions. The log
host gains log-reader permissions, and input pins advance. All configuration paths
below refer to the fresh remote default unless otherwise stated. No peer session
worktrees, records or transcripts were used.

Relevant instructions and entry point inspected: workspace AGENTS.md,
`docs/agent-teams.md`, project/session/git/documentation/deployment/verification
procedures, dev-session-documentation and dev-session-handoff skills, configuration
AGENTS.md and README.md. Searches were limited to log host, exporter, rsyslog,
metrics and input/packaging references, followed by focused source reads and the
lead-requested baseline reconciliation.

## Source, package and input graph

| Edge | Inspected source / exact identity |
| --- | --- |
| Host | `cluster/cz.vpsfree/containers/prg/int.log/module.nix`: NixOS, container 14004, `log.int.prg.vpsfree.cz`, IPv4 `172.16.4.1/32`, channels `nixos-stable` and `os-staging`, `auto-update` tag |
| Stable channel | `flake.nix`: `nixos-stable.nixpkgs = nixpkgsStable`; root `nixpkgs` follows `nixpkgsStable` |
| Stable lock | `flake.lock`: nixpkgs **718f670e845328e9c2cecdd832835712b2cbd065**, `nixos-26.05`, narHash `sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=` |
| OS channel | `flake.nix`: `os-staging.vpsadminos = vpsadminosOsStaging`; lock **dd188397abe37d0bc33f4c5dfb3605206ce5e326**, narHash `sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=`; its nixpkgs follows root stable |
| Unstable edge | OS input's nixpkgsUnstable follows root `nixpkgsUnstable`, which resolves to lock node `nixpkgsUnstable_2`, **31ecbaca1bdefa45dffc409f0250bd8039ea0010**, narHash `sha256-dhoW6VgFWlaodSY5jrBn+CF2FLmaUvDVgM7+C7T2+NM=` |
| Deployment tooling | `confctl` **7bee58a52372b95c2198ce3f2a719807a3c2c66b**, narHash `sha256-gh1tmTv8aAO1OA3HX2NEYnRALMK2i666Lxey8hxD0QM=`; its nixpkgs follows its own vpsadminos input, not root stable |
| Site overlay | `environments/base.nix` → `overlays/default.nix` → `overlays/packages.nix`: `syslog-exporter = super.callPackage ../packages/syslog-exporter { };` |
| Exporter source | `packages/syslog-exporter/{Gemfile,Gemfile.lock,gemset.nix}`: Git **7c5a8e74e44a704cceb99cd05716af6800d78efd**, version **0.13.4**, fetch hash `1vc02bpvwnq6kb1z0bcg4h2vk1kig23q0iqhph755rlsq3cb7fdy` |
| Exporter derivation | `packages/syslog-exporter/default.nix`: `bundlerEnv`, `gemdir = ./.`; no exporter flake input or confctl channel |
| Ruby dependencies | Lock/gemset: Puma 8.0.2, Rack 3.2.7, prometheus-client 4.2.5, nio4r 2.7.5, base64 0.3.0; Bundler lock 2.7.2 |

The fresh stable nixpkgs source already exists at
`/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source` (path derived from the
locked recursive hash). Inspected `pkgs/top-level/all-packages.nix:4324` and
`pkgs/development/compilers/rust/{1_95,1_97,1_98}.nix`: default `rust`,
`rustPackages`, `rustc`, `cargo` and `rustPlatform` use **1.95.0**; explicit
`rustPackages_1_97`/`rustPackages_1_98` provide **1.97.1**/**1.98.1**. Default
`rustPlatform.buildRustPackage` is the minimal packaging choice, subject to
candidate dependency MSRV. No toolchain build/evaluation was run.

`pkgs/by-name/rs/rsyslog/package.nix` in that source selects **8.2610.0**, tarball
hash `sha256-e9+V6B6mwO5dWGNC1X0qbjlbCJ+zxnMYoNxVWBbeQEs=`. The tarball is
not locally available; compiled-in template/queue/size behavior was not inspected.

## Runtime and transport

`modules/services/monitoring/prometheus/conf-exporters/syslog.nix` owns
`services.prometheus.confExporters.syslog` options: enable, package, user, group,
listenAddress, port, stateDir and freeform JSON settings. Defaults:

- Package `pkgs.syslog-exporter`; user/group `syslog-exporter`.
- Bind `0.0.0.0:9102`; state/working directory `/var/syslog-exporter`, tmpfiles
  directory mode 0750, owned by exporter user/group.
- `settings.syslog_pipe = /var/log/rsyslog.pipe` via `mkDefault`; tmpfiles creates
  FIFO mode **0640 root:syslog-exporter**. Preserve this independently of log-reader
  file ownership.
- JSON is generated by `pkgs.formats.json`. Rackup loads
  `SyslogExporter::Rackup.app(configurationJson)`; Puma config binds address/port.
- Unit `prometheus-syslog-exporter.service`: network.target ordering only,
  multi-user.target, `RACK_ENV=production`, `Type=notify`, `WatchdogSec=10`,
  `Restart=on-failure`, `RestartSec=30`, ExecStart package `/bin/puma -C ...`.
  There is no explicit ordering/dependency between exporter and rsyslog.
- Host health checks require both `syslog.service` and this exporter unit active.

`cluster/cz.vpsfree/containers/prg/int.log/config.nix` computes settings.hosts
from logging-enabled non-carrier machines: key is machine name, values alias,
fqdn, OS spin and optional `vpsadmin_webui` collector for the two WebUI hosts.
The firewall allows exporter port from monitoring machines' primary addresses.

Rsyslog receives remote TCP **11514** and UDP **11515** using `remote-file` ruleset.
It writes `/var/log/remote/%HOSTNAME%/log` first, then calls `remote-pipe` containing
`action(type="ompipe" Pipe="...rsyslog.pipe")`. Local selectors write
`-/var/log/messages` then `|...rsyslog.pipe`. The `remote-log-file` template
controls the pathname only; **no message template is explicitly selected for
either FIFO action**. No newline escaping, maximum-message-size, input rate limit,
action queue, disk queue, retry or overflow settings are explicit on this host.
Do not infer lossless delivery, durable replay, or a numeric limit from this file.
Exact default rendering/newline/max-size and full/no-reader FIFO behavior remain
pinned-rsyslog verification questions. Architect reports having consulted upstream
ompipe documentation; this package does not independently certify runtime behavior.

Pinned nixpkgs `nixos/modules/services/logging/rsyslogd.nix` prepends imuxsock,
`/run/systemd/journal/syslog` and `/var/spool/rsyslog`, then host defaultConfig and
extraConfig; `syslog.service` runs rsyslogd with that generated file. It adds no
explicit template, queue or rate-limit override. A spool working directory by
itself does not establish durable FIFO delivery.

Fresh host configuration preserves the new `log-readers` group, file mode 0640,
directory mode 0750 and umask 0027; `log-reader.nix` owns its restricted SSH user.
Keep these and logrotate retention/HUP behavior intact.

Sender compatibility: site `modules/system/logging/nixos.nix` sends TCP using
`RSYSLOG_SyslogProtocol23Format`; `shared.nix` chooses the local-location logger or
first logger. Site vpsAdminOS sender sets `services.rsyslogd.forward`. Directly
required canonical pinned vpsAdminOS source
`dd188397abe37d0bc33f4c5dfb3605206ce5e326:os/modules/services/logging/rsyslog.nix`
uses TCP with that same template, linkedlist forwarding queue, filename
`fwdRule1`, 1g maximum disk space and infinite action retries. **That sender queue
does not establish a queue/replay guarantee for the central ompipe action.**
No sender/node update is needed if the central FIFO format remains compatible.

## HTTP consumers and metrics

`modules/services/definitions.nix` declares exporter 9102 and syslog TCP/UDP ports.
`modules/clusterconf/monitor/default.nix` discovers monitored logger machines,
scrapes job **log** every **60s**, and adds `logger_alias`/`logger_fqdn` labels.
No per-job scheme, path or timeout override is present: preserve the standard
HTTP `/metrics` endpoint expected by this configuration; exact Ruby response
routing/content negotiation belongs to implementer0's contract. Preserve exporter
host labels separately from logger target labels.

`modules/clusterconf/monitor/rules/syslog.nix` consumes:

- `up{job="log"} == 0` for 10m (`SyslogExporterDown`).
- `syslog_nodectld_crash`, `syslog_nodectld_segfault`,
  `syslog_nodectld_zfs_stream_receive_error`, `syslog_osctld_internal_error`,
  `syslog_vpsadmin_webui_fatal_error`, `syslog_lxc_start_failed`,
  `syslog_lxc_start_netns_limit`, `syslog_kernel_bug{type="nullptr"}`,
  `syslog_kernel_gpf`, `syslog_kernel_emergency`, `syslog_zfs_panic`: all compare
  to **1**, so replacing pulse/reset behavior with counters would break alerts.
- `rate(syslog_kernel_oom_count[10m])` thresholds 10, 50 and 100.
- WebUI annotations consume `fqdn` and `error_type`. Other annotations carry
  instance/all labels; full label and timer semantics must match the Ruby contract.

No other syslog metric consumer appeared in the bounded configuration grep.
External dashboards, ad hoc queries and production-only consumers remain unknown.
A healthy scrape proves HTTP availability, not that the FIFO is being drained.

## Proposed minimal integration and removal boundary

Subject to architect acceptance and later execution authorization:

1. Keep the local overlay/package name and replace
   `packages/syslog-exporter/default.nix` with a pinned-source
   `rustPlatform.buildRustPackage`, exact Git revision/hash plus locked Cargo
   dependencies/hash. Reuse consumer stable toolchain 1.95.0 if supported. No
   flake input, channel or fleet vpsAdminOS bump is required for this approach.
2. Keep service option names, generated JSON, hosts mapping, FIFO ownership,
   working directory, address/port, unit name, health checks and scrape rules.
   Replace Rackup/Puma generation and ExecStart with the agreed Rust CLI.
   Retain notify/watchdog only if the binary implements their semantics;
   otherwise explicitly use simple and remove watchdog. Do not retain a notify
   unit around a non-notifying process.
3. Remove this package's Gemfile, Gemfile.lock and gemset.nix; remove only
   `syslog-exporter` from the daily-update.yml Ruby-package refresh loop.
   Root development Ruby/Bundler, geminabox, ssh-exporter, other Ruby packages
   and node Ruby runtimes are unrelated and remain. Do not remove FIFO or state
   contents during switching. Exact state files and rollback readability are
   dependent on implementer0's audit, not established by stateDir alone.
4. Preserve transport/template and log-reader/logrotate behavior. No disk queue,
   new wire protocol, metrics rename, new alert or sender update is needed for
   a compatible initial replacement. If measured transport loss requires policy
   changes, route that separate design decision through architect/lead.

## Compatibility, rollout and rollback proposal

One central exporter change can coexist with old senders and monitoring hosts if
FIFO parsing, JSON config, HTTP endpoint, metric names/types/labels/reset and
retention semantics remain identical. There is no identified DB/API/client schema
change. Existing on-disk exporter state must be inventoried before asserting
rollback safety; avoid a new incompatible format or in-place migration.

Build/test candidate without replacing the live FIFO reader. Two consumers of one
FIFO compete for records; parallel comparison requires a replay fixture or
explicit duplicated rsyslog actions into separate FIFOs/ports in a disposable test.
Keep one live reader during production switching. Stopping the old reader,
startup gaps, exporter crashes and any rsyslog restart can lose or delay metric
events; archived log files are not an automatic exporter replay source. Measure
this and document the accepted window; HTTP `up` alone does not detect it.

A future authorized rollout should retain exact old/new system closures and source
input receipts, build before acquiring machine ownership, dry-activate, then switch
only log.int.prg and verify units, FIFO draining, continuing file writes and scrape
behavior over multiple 60s scrapes. Prefer no rsyslog configuration change/restart
in the minimal cutover. If an activation does restart it, test and account for that
explicitly. Integration and deployment require their separate lead-owned approval
and coordination; this investigation reserves no resources.

Rollback should activate the retained Ruby system closure with the same FIFO,
state directory, permissions, endpoint and alerts. Stop the Rust reader before
starting Ruby. Validate any existing state can still be read, unit health,
file logging and metric semantics after rollback. In-memory counters/pulses may
reset; do not claim cross-restart metric continuity without evidence. Rollback
does not recover events already lost through the pipe. Preserve original file
retention and log-reader recovery rules.

## Meaningful later verification (not run)

- **Quick evaluation:** from an authorized feature worktree/Nix environment,
  inspect `confctl ls` and inputs; evaluate the exact log machine's package,
  generated JSON, tmpfiles and unit. Assert unchanged options/hosts/permissions,
  correct Rust ExecStart/type/watchdog, no unintended channel/pin changes. Keep
  configuration/Rust source and full input graph receipts.
- **Package:** build the Rust package with pinned stable rustPlatform and locked
  Cargo dependencies; verify packaged binary/CLI. A package build is sufficient
  for toolchain/MSRV uncertainty before any full host build.
- **Host:** `nix develop -c confctl build cz.vpsfree/containers/prg/int.log` is the
  repository-declared host build. Run existing `log-reader-access` check when
  touching host rsyslog config; it protects ownership/rotation and validates
  rsyslog syntax. It is not exporter end-to-end coverage.
- **Pinned-rsyslog disposable fixture:** use actual generated host config and
  rsyslog 8.2610.0; send TCP and UDP records and local records to separate test
  ports. Capture FIFO bytes: timestamp/hostname/tag/message shape, newline,
  controls, blank/malformed records and message sizes around observed limits.
  Check archived file bytes/counts separately from consumed FIFO records.
- **Burst/slow reader:** send a finite, sequence-marked known corpus, first below
  saturation, then overload (for example 100k records with several lengths,
  up to 64 KiB inputs). Count accepted, file-written, FIFO-observed and parsed
  records independently; distinguish upstream truncation from parser rejection.
  Pause reader beyond pipe capacity, stop/restart reader, restart rsyslog, send
  SIGTERM during backlog; report gaps, recovery, bounded RSS/CPU, scrape latency,
  HTTP status and shutdown time. No unmeasured zero-loss claim. Do not emit fake
  fatal metrics into production monitoring.
- **Differential/consumer:** replay identical captured FIFO bytes to isolated Ruby
  and Rust processes. Compare metric names/types/labels and ordered timer/pulse
  effects over multiple scrapes and expiry windows; include every alert above,
  WebUI collector host selection, unknown hosts and OOM rates. Use promtool on
  exposition and alert fixtures. Acceptance thresholds for throughput, memory
  and scrape latency belong in architect's verification brief.
- **Runtime later:** only with explicit execution authorization, follow repository
  dry-activate guidance and lead-owned machine claims. Long/uncertain builds or
  tests require the monitor skill's fresh watcher; no such work ran here.

Open gaps: pinned rsyslog default template/newline/max size and overflow behavior;
exact deployed production generation/source versus repository default; Ruby state
and HTTP/timer contract; Rust dependency MSRV; actual burst distribution/capacity
thresholds; external consumers. These do not justify changing transport preemptively.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/>.
