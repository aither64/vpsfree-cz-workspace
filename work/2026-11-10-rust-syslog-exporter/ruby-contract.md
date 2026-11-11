# Ruby exporter contract inventory

Package R, implementer0, 2026-11-10. Planning/investigation only; no application
edits, commits, builds, dependency installation, tests, fetches or deployments
were performed by this package. Session identity matched `dev-session current`,
both environment variables and the trusted binding. The live roster retained
implementer0 as Sol/xhigh with `workspace_write` access.

## Inspected revision and boundary

Canonical bare repository: `repos/syslog-exporter.git`. The inspected default
source is **`7c5a8e74e44a704cceb99cd05716af6800d78efd`**, selected through
`refs/remotes/origin/HEAD -> refs/remotes/origin/master`. The bare repository's
own `HEAD -> refs/heads/master` is stale at
`69b0269ab27bacd1f160af595d33f14563618daa`. Initial inspection used cached refs;
the lead subsequently reported a fresh fetch confirming the same remote head.
This package did not inspect any peer/reference session or worktree.

All source paths and line numbers below refer to the inspected revision. The
[exact source tree](https://github.com/vpsfreecz/syslog-exporter/tree/7c5a8e74e44a704cceb99cd05716af6800d78efd)
contains no `AGENTS.md`. Read scope: complete `lib/`, `spec/`, README, sample
config, Rack entry point and existing build/hook/CI manifests. One follow-up
pass checked parser/flare details, baseline differences and the entry point.
No external library implementation was inspected.

Compared with stale local master, the remote source adds WebUI metrics,
`hosts.*.collectors`, RSpec coverage and Ruby/dependency updates. `kernel[]`
recognition already exists on stale local master; the parser delta is an
iterator-variable rename. This corrects the preliminary peer message that
included kernel recognition among the newer changes.

## Transport, framing and configuration

`README.md:2` describes a named-pipe reader. `processor.rb:64–68` opens
`syslog_pipe` for reading and requests Linux `F_SETPIPE_SZ` (numeric command
1031) with `pipe_size`. It neither creates nor verifies a FIFO. There is no
TCP/UDP/Unix socket listener or producer configuration in this repository.
The exact rsyslog module, action, queue, template, escaping, producer permissions
and failure policy require the configuration-consumer evidence owned by
implementer1; they cannot be established from this source.

`parser.rb:11–24,29–94` consumes newline-delimited records through `each_line`.
The nominal record is:

```text
ISO8601_TIMESTAMP HOST PROGRAM[PID] MESSAGE\n
```

Fields split at one literal ASCII space. There is no RFC 5424 header parser,
priority/facility/severity field, length prefix, multiline reassembly, escape
decoding or line-size limit. The remaining message retains its trailing newline
when read from the pipe; parser unit examples without newlines bypass this.
Every new Parser **unconditionally discards the first line**, complete or
incomplete. After normal EOF, `processor.rb:29–35` warns, sleeps one second and
opens again. The opened file is not explicitly closed. There is no ack, replay,
durable cursor, checkpoint or persisted metric state.

`config.ru:3` selects JSON via `SYSLOG_EXPORTER_CONFIG`, defaulting to
`config-sample.json`. There is no exporter-owned CLI or `bin/` executable.
HTTP/process options come from the external Rack/Puma launcher and consumer
configuration. `rackup.rb:7–29` sets `Thread.abort_on_exception = true`, starts
three processor threads, wraps the app in Rack Deflater and Prometheus exporter
middleware, and provides a fallback HTTP 200 `text/html` body `OK`.
The middleware's default metrics path, exact exposition rendering, compression
and HTTP details are delegated to dependencies, not defined/tested here.

`config.rb:40–54` reads these keys without explicit schema validation:

| Key | Behavior |
| --- | --- |
| `syslog_pipe` | Read directly; sample `/var/log/rsyslog.pipe`. |
| `pipe_size` | Default `1048576` bytes; used as provided. |
| `hosts` | Object keyed by the incoming host name; converted to host objects. |
| `hosts.*.alias` | Value for metric label `alias`. |
| `hosts.*.fqdn` | Alternative incoming host identity and label `fqdn`. |
| `hosts.*.os` | Exact string `vpsadminos` enables three OS-specific collectors. |
| `hosts.*.collectors` | Defaults to `[]`; membership of `vpsadmin_webui` enables that collector. |

Unknown keys are ignored. Missing/type-invalid fields generally surface only
through later Ruby operations. No reload exists. `processor.rb:43–50` scans
hosts in config order for the first `name == msg.host || fqdn == msg.host`;
alias is not accepted for routing. Duplicate/colliding names/FQDNs have no
validation. Unknown hosts are silently discarded after parsing and queueing.

## Parsing and host/collector selection

`parser.rb:33` parses the outer timestamp with `Time.iso8601`. Generic programs
ending in `[digits]` yield the captured program and integer PID. Exact `kernel`
or `kernel[]` creates `KernelMessage` and normalizes program to `kernel`.
There is no colon stripping: `osctld:` stays `osctld:`. PID and timestamp do not
become metric labels.

For `HOST == localhost` and the special `svlogd -tt` prefix matching
`^\d+-\d+-\d+_\d+ \d+:\d+\.\d+ `, the parser discards the inner date/time,
extracts the inner host and program, and uses the outer timestamp. The inner
program is kept verbatim: no PID parsing or KernelMessage conversion occurs
(`parser.rb:44–61`). `kernel_message.rb:18–21` extracts a namespace only from
a leading bracketed tag with the source's required spaces (`[ TAG ] body`);
absence yields nil. It does not remove the prefix from the message.

All classes register metric families globally before host selection
(`processor.rb:9–17`, `collector.rb:15–22`). Every host gets Kernel, MessageCount,
Test and Zfs collectors. LxcStart, Nodectld and Osctld require
`host.os == 'vpsadminos'`. VpsadminWebui requires
`host.collectors.include?('vpsadmin_webui')`, regardless of OS. The collectors
list is an additional opt-in, not an allowlist that disables base collectors.
Source: each collector's `use_host?` and `collector.rb:29–30`.

## Metric families

There are **18 registered families: 5 counters and 13 gauges**. Every family
adds labels `alias,fqdn`; the table lists additional labels in declaration
order. HELP text is copied exactly from `collectors/*.rb`. Names are exact
registration names, including existing `_count` suffixes. No actual middleware
scrape was run, so dependency-driven rendering, empty-series behavior and nil
label serialization remain unverified. “No initial set” means this application
makes no zero-setting call; it does not assert a dependency's wire behavior.

| Name | Type | Additional labels | HELP | Initial application state / expiry |
| --- | --- | --- | --- | --- |
| `syslog_kernel_message_count` | counter | `syslogns` | Number of kernel log messages per syslog namespace | No initial set; increment each kernel message. |
| `syslog_kernel_bug` | gauge | `type` | 1 if kernel bug has occurred, 0 otherwise | `type=nullptr` set 0; 240 s. |
| `syslog_kernel_gpf` | gauge | — | 1 if kernel general protection fault has occurred, 0 otherwise | No initial set; 240 s. |
| `syslog_kernel_emergency` | gauge | `type` | 1 if kernel emergency message has been detected, 0 otherwise | `type=unregister_netdevice` set 0; 240 s. |
| `syslog_kernel_nf_conntrack_table_full` | gauge | — | 1 if kernel nf_conntrack table full message has been detected, 0 otherwise | No initial set; 240 s. |
| `syslog_kernel_oom_count` | counter | — | Number of out-of-memory situations reported by the kernel | No initial set. |
| `syslog_lxc_start_failed` | gauge | `id` | 1 if a container has failed to start, 0 otherwise | No initial set; 240 s. |
| `syslog_lxc_start_netns_limit` | gauge | `id` | 1 if a container has hit netns limit and failed to start, 0 otherwise | No initial set; 240 s. |
| `syslog_message_count` | counter | `program` | Number of syslog messages sent by a host | No initial set; nil program maps to `other`. |
| `syslog_nodectld_crash` | gauge | — | 1 if nodectld has crashed, 0 otherwise | Set 0; 180 s. |
| `syslog_nodectld_segfault` | gauge | — | 1 if nodectld has segfaulted, 0 otherwise | Set 0; 180 s. |
| `syslog_nodectld_zfs_stream_receive_error` | gauge | — | 1 if zfs recv in nodectld has reported an error, 0 otherwise | Set 0; 180 s. |
| `syslog_osctld_command_count` | counter | `command` | Number of executed management commands | No initial set. |
| `syslog_osctld_internal_error` | gauge | — | 1 if osctld internal error has occurred, 0 otherwise | Set 0; 180 s. |
| `syslog_flare_test` | gauge | — | 1 if flare is on, 0 otherwise | Set 0; 15 s. |
| `syslog_vpsadmin_webui_fatal_error_count` | counter | `error_type` | Number of fatal vpsAdmin WebUI PHP errors reported by nginx | No initial set. |
| `syslog_vpsadmin_webui_fatal_error` | gauge | `error_type` | 1 if a fatal vpsAdmin WebUI PHP error has occurred, 0 otherwise | `fatal,parse,recoverable_fatal` each set 0; 180 s. |
| `syslog_zfs_panic` | gauge | — | 1 if ZFS panic has occurred, 0 otherwise | Set 0; 240 s. |

Declarations: `collectors/kernel.rb:9–49`, `lxc_start.rb:5–20`,
`message_count.rb:5–13`, `nodectld.rb:5–24`, `osctld.rb:5–19`,
`test.rb:5–11`, `vpsadmin_webui.rb:11–26`, `zfs.rb:5–11`.

## Detection and state semantics

Collectors receive each routed message serially in registration order
Kernel → LxcStart → MessageCount → Nodectld → Osctld → Test → VpsadminWebui → Zfs
(`lib/syslog-exporter.rb`, `processor.rb:50`). Distinct collectors may match the
same record. Inside Kernel/LxcStart/Nodectld/Osctld, ordered `if/elsif` means
only the first matching branch executes.

| Collector / source | Program and exact matching behavior |
| --- | --- |
| Kernel `kernel.rb:61–87` | Exact `kernel`; increments namespace counter first. Ordered substring branches: `BUG: kernel NULL pointer dereference`; `unregister_netdevice: waiting for`; `general protection fault` unless also `traps: `; `nf_conntrack: nf_conntrack: table full, dropping packet`; ` invoked oom-killer: ` (counter only). |
| LxcStart `lxc_start.rb:26–56` | Program `lxc` or `lxc-start`; first substring `No space left on device - Failed to unshare CLONE_NEWNET`, else regex `Failed to spawn container "[^"]+"`. `id` is stripped message prefix before the first colon, or empty string without a colon; it does not use the quoted ID. |
| MessageCount `message_count.rb:15–18` | Every routed message, program or `other`. |
| Nodectld `nodectld.rb:36–44` | Exact `nodectld`; ordered substrings `Daemon crashed`, `[BUG] Segmentation fault`, `cannot receive incremental stream`. |
| Osctld `osctld.rb:29–35` | Exact `osctld`; regex `Received command '([^']+)'$` increments captured command, else substring `Error: internal error`. Ruby `$` permits a final newline. |
| Test `test.rb:18–21` | Any program, substring `flare test`. This is an enabled production collector, separate from RSpec. |
| WebUI `vpsadmin_webui.rb:38–54` | Exact `nginx`, plus `FastCGI sent in stderr`; first matching substring of `PHP message: PHP Fatal error:`, `PHP message: PHP Parse error:`, `PHP message: PHP Recoverable fatal error:` maps to `fatal`, `parse`, `recoverable_fatal`. Increments once per message and raises corresponding gauge; does not count each occurrence. |
| Zfs `zfs.rb:18–23` | Exact `kernel`, substring `PANIC: zfs:` or `spl_panic+0x`. |

Flares are keyed by collector instance (therefore host), family name and the
additional labels. `collector.rb:85–100` sets the gauge to 1 immediately and
renews an existing expiry to **processing wall clock now + duration**; repeated
messages do not accumulate a count for gauge-only families. There is no
cross-line, PID or request correlation. Message timestamps do not affect expiry,
so old/backlogged messages still raise a full-duration flare.

`collector.rb:52–72`, `flare.rb` and `processor.rb:54–61` clear a flare to 0
only when `Time.now > ends_at`, in a polling pass followed by a five-second
sleep. The effective duration includes scheduling and scan delay. Zero series
remain in the metric registry; no series eviction exists. Registry state,
counters, flares and queues are memory-only; restart resets them. No schema,
database or disk migration is present.

## Concrete risks and bug-compatibility decisions for the architect

These are source-derived risks, not measured throughput results. Preserve
supported metrics/config/detectors unless design explicitly changes them;
do not silently freeze the following accidents as required compatibility.

1. **Certain first-record loss:** every pipe open discards one record even when
   valid (`parser.rb:13`). A replacement should process complete first records
   and define recovery for partial records. A test explicitly encodes the old
   discard (`parser_spec.rb:35–50`), so changing it is intentional behavior change.
2. **Malformed input can terminate ingestion/process:** invalid ISO timestamps
   raise before nil-return handling; exceptions have no per-record rescue and
   Rack sets abort-on-thread-exception. Some missing fields instead yield generic
   Message objects and misleading `program=other`. Empty input raises
   `StopIteration` at the initial `next`; the outer Ruby `loop` may consume this
   and stop the parser thread instead of reopening. This last effect is inferred,
   not runtime-tested. Define reject-and-continue behavior with observability.
3. **Kernel class mismatch:** `kernel[123]` becomes generic Message with program
   `kernel`, as does svlogd-forwarded `kernel`; Kernel collector calls
   `message.syslogns_tag` unconditionally and can raise `NoMethodError`
   (`parser.rb:60–73`, `kernel.rb:62–65`). Normalize kernel records deliberately.
4. **Unbounded memory and work:** parsed messages enter an unbounded `Queue`
   (`processor.rb:6,32`), one consumer linearly scans every configured host and
   invokes every selected collector. Parsing allocates timestamps/strings per
   message. Flare lookup and settling scan arrays. Registry series for dynamic
   program/command/id/syslogns values never expire. Sustained backlog/cardinality
   growth can exhaust memory; no loss/backlog/parse-error metrics quantify it.
5. **Expiry race:** `set_flare` writes 1 before acquiring the flare mutex, while
   settling removes expired flares under the mutex and writes 0 afterwards.
   A concurrent fresh event can be overwritten with 0 although its renewed/new
   flare remains scheduled (`collector.rb:55–71,85–99`). Make update/reset ordering
   atomic in the replacement instead of reproducing this race.
6. **Unrecoverable I/O/startup errors:** FIFO open and pipe-capacity errors are
   unhandled; the reader requests a full configured capacity without fallback.
   Blocking FIFO open, EOF/reopen delay, discarded first records and lack of
   explicit descriptor close complicate writer reconnects. Actual writer
   backpressure/drop policy remains the configuration owner's evidence.
7. **Liveness is weakly reported:** fallback HTTP always returns OK independently
   of parser progress; unknown hosts disappear silently; malformed nil parses
   warn with the complete input line. A per-record warning flood also costs
   throughput. The source has no ingestion health/error/drop metrics.
8. **Dormant helper defect:** `unset_flare` indexes the array with nil when no
   matching flare exists and can raise (`collector.rb:103–109`). No current
   collector calls it. Removing this unused helper does not require preserving
   its failure behavior.

Wall-clock expiry vs a monotonic clock, startup zero-series choices, unknown
collector/config-key handling, duplicate host routing and bounded queue/record
limits are design choices with observable compatibility consequences. This
inventory does not select them. A bound requires an explicit overload policy;
it cannot establish losslessness by itself. No throughput number, burst target,
acceptable-loss threshold or production traffic distribution is established.

## Ruby/build/hook artifacts for a future rewrite

Removal/replacement inventory, not authorization to edit:

- Runtime/gem surface: all `lib/**/*.rb` (including enabled Test collector),
  `config.ru`, `Gemfile`, `syslog-exporter.gemspec`, `Rakefile` and Ruby version
  module. There is no checked-in `bin/`, lockfile or generated binary.
- Ruby tooling: `.overcommit.yml` (RuboCop PreCommit enabled), `.rubocop.yml`,
  `.rubocop_todo.yml`, `.rspec`, `spec/**/*.rb`; translate useful behavioral
  fixtures before removing RSpec. Retain changed first-record behavior as an
  explicit test decision.
- Replace `shell.nix`'s Ruby 3.4/bundix/rubocop environment and shell hook that
  installs bundler/geminabox/overcommit and executes bundle install. Do not run
  this hook during planning. Replace `.github/workflows/rspec.yml` (Ruby 3.4,
  `bundle exec rspec`) with the selected Rust checks when implementation is
  authorized.
- `.gitignore` currently lists `.gems`, `Gemfile.lock`, `pkg`: obsolete Ruby
  entries can go; future Cargo lock/build-output policy must be deliberate.
  Preserve project metadata/license/editor settings unless separately justified.
- Retain/extend JSON sample and README for supported interfaces. Consumer
  packaging/service changes belong to implementer1's evidence and architect's
  cross-project plan, not this source-only package.

Current gem constraints: Ruby `>=3.4.0`, `prometheus-client ~>4.2.5`,
`puma ~>8.0, >=8.0.2`, `rack ~>3.2`; development rackup/rake/rspec
(`syslog-exporter.gemspec:18–22`, `Gemfile:4–8`). No exact dependency lock is
tracked, so dependency behavior is not fixed by this source head alone.

## Existing evidence and remaining unknowns

`spec/syslog_exporter/parser_spec.rb` covers normal PID, kernel namespace,
svlogd, first-line discard and one no-space malformed record.
`config_spec.rb` covers defaults, pipe size and collector list.
`collectors_spec.rb` covers message count, nodectld crash, osctld command/error,
LXC ID, kernel OOM, manual flare expiry and WebUI classification/gating.
`spec_helper.rb:9–50` uses a fake metric registry. It does not verify actual
Prometheus exposition. There are no transport/process/HTTP/throughput tests,
concurrency tests, reconnect tests, invalid-timestamp tests or actual expiry
timing tests. The package read these tests; it did not run them.

Unknowns for the proposed plan: producer template/escaping and loss behavior;
service CLI/listen endpoint and deployed package source; actual scrape output
(counter naming, HELP, label escaping/nil values, empty series); traffic/burst
and memory budgets; intended empty/invalid-record policy; whether any consumer
depends on current bugs. Consumer evidence and architect decisions are the
next dependencies. Source evidence is sufficient to design regression fixtures
and to mark deliberate bug fixes without claiming live operational validation.

Artifact is ready for architect input and lead acceptance. Package R has no
remaining source pass planned and implementer0 has capacity after delivery;
no next package is implicitly accepted. Lead owns state/portal linkage and
acceptance. No substantive deliverable review is triggered by this bounded
investigation-only record.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/
