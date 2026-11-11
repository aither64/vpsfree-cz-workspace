# Rust syslog-exporter proposal

Owner: architect0. Status: proposed design, 2026-11-10; investigation and planning
only. No application edits, builds, tests, integration or deployment occurred in
this package. Implementation requires a later assignment accepted by the lead.

## Scope and evidence

Replace the exporter entirely with one Rust executable, retaining rsyslog FIFO
input and the existing Prometheus contract. Replace Ruby development tools and
Overcommit, add Rust CI, and update the single configuration consumer
`log.int.prg.vpsfree.cz`. No crates.io publication, node rollout, new transport,
durable message broker, plugin system or persisted metric database is needed.

The lead freshly confirmed these remote defaults:

- `syslog-exporter`: `7c5a8e74e44a704cceb99cd05716af6800d78efd`.
- `vpsfree-cz-configuration`: `3c088a4b71881b3649441ce3c4e92c71757708e6`.

[Ruby contract](ruby-contract.md), accepted package R, is the authoritative
inventory of all 18 families, exact HELP strings, labels, detector order,
initialization and expiry. [Configuration integration](configuration-integration.md),
accepted package C, records exact package/input identities, service, producer,
scrape and alert contracts. This design selects behavior and execution boundaries
from those inventories. Bare exporter local master is stale; do not use it as
the implementation baseline. No reference-session files or transcripts were read.

Source proves an unbounded Ruby message queue, linear host lookup, per-message
allocation, unconditional first-line loss and a flare renewal/reset race. The
user reports missed messages during OOM floods. Their relative performance cost
and the location of production loss have **not** been measured. Faster Rust
ingestion is a plausible remedy, not evidence of end-to-end losslessness.

## Proposed runtime and interfaces

Use a single Cargo package, `publish = false`, with a binary and a small library
for deterministic tests. Suggested files are `src/{main,config,input,parser,
collectors,metrics,http}.rs`; split collectors only if it aids navigation.
Use ordinary enums/structs and functions, borrowed message fields, standard hash
maps and cached metric handles. Avoid an extensible collector trait hierarchy,
per-message task spawning, generic event bus or parallel parser pipeline.

```text
rsyslog -> existing FIFO -> poll/read + frame + parse + route + collectors
                                                   | one ordered state owner
                                                   v
                                      cached atomic metric handles
                                                   |
                                  independent HTTP gather/encode -> /metrics
```

**Ingestion:** a dedicated OS thread owns the FIFO descriptor, framing buffer,
host index, collector dispatch and flare deadlines. Read nonblocking in reusable
chunks (initial implementation: 64 KiB), scan delimiters in bytes, and process
records in their FIFO order. There is no application message queue. The kernel
pipe and bounded framing buffer provide limited burst storage. Check timers and
shutdown between bounded batches, including while continuously readable; begin
with at most 256 records or 2 ms of work per batch and validate under load.

**Routing:** build an incoming-name/FQDN-to-host-ID map once; do not route by
alias. Preserve the Ruby first-in-config match if identities collide by inserting
in JSON order and keeping the first mapping; warn once on ambiguity. This needs
ordered JSON map deserialization, not accidental sorted-key order. Fixed host
labels and eligible collectors are computed at startup. MessageCount and Test
still see every accepted known-host record; program-specific dispatch skips
irrelevant collectors while preserving detector and cross-collector semantics.

**Config/CLI:** preserve JSON `syslog_pipe`, `pipe_size` (default 1048576),
`hosts.*.{alias,fqdn,os,collectors}` and additive WebUI opt-in. Preserve ignored
unknown keys/collector names, warning once for unknown collector names. Validate
required types/paths at startup with a useful error. Introduce
`syslog-exporter --config PATH --listen ADDRESS:PORT`; accept
`SYSLOG_EXPORTER_CONFIG` as the config default and retain `config-sample.json`
as its fallback. Configuration passes both arguments explicitly. Include
`--help`, `--version` and `--check-config` (no FIFO/HTTP side effects). No live
reload, daemonization or Puma-compatible CLI is required.

## Framing, errors and delivery limits

Preserve the actual line protocol: outer ISO8601 timestamp, incoming host,
program/PID and message separated by literal spaces, with the existing svlogd
localhost form. It is not a general RFC 3164/5424 parser. Preserve colon handling,
namespace extraction, substring/regex precedence, and the final-newline behavior
of anchored command detection. PID and timestamp never become metric labels.

Process every complete first record; do not copy Ruby's unconditional discard.
Normalize ordinary `kernel`, `kernel[]`, `kernel[digits]` and forwarded kernel
records into a representation with optional namespace access, removing the
Ruby class-mismatch crash. Preserve forwarded program parsing otherwise. Parse
the outer timestamp with a maintained date parser, initially preserving valid
fixture forms; do not retain a parsed timestamp after validation because current
collectors do not use it. Broader Ruby ISO8601 forms need explicit fixtures before
claiming compatibility; use the captured producer format as the required subset.

Add `max_line_bytes`, provisional default **1 MiB including LF**, independent of
pipe capacity. Reject an over-limit record once, discard until LF, then resume;
never let a delimiter-free stream grow memory without bound. This is an explicit
new limit and must exceed every required producer record after framing/escaping
is measured. Tests cover the boundary, split reads and long lines spanning chunks.
Reject invalid UTF-8 or malformed required headers, increment a bounded-reason
diagnostic counter, and continue. Unknown hosts are counted separately and ignored.
Do not log every bad line or entire potentially sensitive payloads; rate-limit
summary diagnostics. Preserve accepted missing-program behavior only where the
contract fixtures establish it; no collector may panic on a missing body.

Verify the configured path is a FIFO; never create or replace it in the binary.
Request `F_SETPIPE_SZ` once per open and expose the effective size. If the kernel
refuses enlargement, continue with the actual capacity and one warning, recording
this in performance results. Fail on an invalid path/type/permission instead of
silently reading another file. EOF closes the descriptor and resets framing;
count/drop an incomplete tail and reopen with bounded interruptible backoff.
Avoid a busy HUP loop and keep timers/HTTP responsive while no writer exists.
Do not hold a dummy writer open, which would hide writer disconnects.

On SIGTERM/SIGINT, stop intake, finish complete records already in the local
bounded buffer, discard/count its incomplete tail, close the FIFO and stop HTTP
within a tested shutdown deadline. Do not claim to drain an indefinitely active
producer. Fatal ingestion failure must terminate the process so systemd restarts
it; it must not leave a permanently healthy HTTP-only process.

There is no acknowledgement, durable cursor, retry journal or persisted counter
state. A full FIFO may block or lose producer output depending on the actual
rsyslog action/error/queue behavior, which the present configuration does not
specify. EOF/restart/partial writes can lose a record; attaching mid-record cannot
always distinguish a plausible partial header. Existing remote file output is
not an automatic replay source. Node TCP queues do not prove central FIFO
reliability, and UDP before the central reader has separate loss risk. A second
reader on the same FIFO steals records; use separate replay FIFOs for comparison.

Do not add a disk queue, enlarge host buffers, or change rsyslog retry policy as a
speculative fix. If the pinned-rsyslog experiment shows transport loss remains
unacceptable at the agreed burst, report it through the lead as a separate design
decision; a queue alone may not repair an action that reports discarded output as
success. A bounded byte queue is a later option only if measured ingestion stalls
justify its complexity and explicit overflow policy.

## Metric and state compatibility

Preserve the **18 existing metric families (5 counters, 13 gauges)** in R's exact
table. All have `alias,fqdn`. Counter names are literally
`syslog_message_count`, `syslog_kernel_message_count`, `syslog_kernel_oom_count`,
`syslog_osctld_command_count`, `syslog_vpsadmin_webui_fatal_error_count`;
do not append `_total` or rename the existing families to modern conventions.
Keep HELP, TYPE, label sets/values, conditional series creation, startup zeros,
renewals and retained-zero series. Never introduce program/PID/host labels on
families that did not have them. An absent namespace's exact serialization,
empty-family exposition and HTTP defaults require a real pinned Ruby scrape;
the fake registry tests are insufficient.

All hosts retain Kernel/MessageCount/Test/Zfs; LxcStart/Nodectld/Osctld require
`os == vpsadminos`; WebUI requires the additive opt-in. Keep every detector in R,
including exclusions, branch precedence and the production `flare test` metric.
One line can affect multiple collectors; WebUI counts once per matching message.
LXC ID comes from the prefix before the first colon, not the quoted container ID.

There is **no cross-line/PID correlation** to recreate. Preserve sequential
global FIFO processing and separate state per configured host and metric label
set. On a trigger, set 1 and replace that key's deadline with processing-now plus
15/180/240 seconds as specified in R. Use monotonic time; message timestamp and
wall-clock changes must not shorten or prolong the intended duration. This
deliberately fixes wall-clock sensitivity. Retain a five-second expiry sweep and
strict expired comparison; fake-clock tests cover just-before/equal/after, idle
input, repeated renewals and interleaved hosts. Only ingestion mutates deadlines
and resets, eliminating the old race.

Start with one map of active flare keys/deadlines scanned every five seconds,
not a heap that accumulates obsolete entries on renewal. Remove expired deadline
entries but retain their metric series at zero. Cache metric handles per series
so the common update is an atomic increment/store without repeated vector lookup.
Dynamic programs/commands/container IDs/namespaces still create retained series:
**bounded framing does not imply bounded total memory**. Measure realistic and
high-cardinality cases. Do not silently cap/evict/relabel legacy series; any such
policy changes metric semantics and needs a separate accepted decision.

Add only a small `syslog_exporter_*` diagnostic namespace: bytes/complete records
read, rejected records by fixed reason, unknown-host records, FIFO reconnects and
effective capacity. The exact diagnostic list may be narrowed during implementation;
it cannot substitute for producer-side loss measurements. No payload-derived
diagnostic labels. Do not enable a large default process-metric bundle accidentally.

## HTTP isolation and dependency choices

Use `prometheus` 0.14.x with an explicit registry, integer counters/gauges and
`TextEncoder`. Its encoder uses the registered counter name unchanged;
`prometheus-client`'s normal OpenMetrics counter encoding adds `_total`, so it is
not the default for this compatibility rewrite. Exact emitted samples/escaping
must still pass golden fixtures. Use `serde`/`serde_json` for config, `clap` 4.x
for CLI, `nix` 0.31.x for safe Linux FIFO/poll/fcntl wrappers, a maintained time
parser, and `regex` only for matching that benefits from preserving the existing
pattern. Compile regexes once. Avoid custom unsafe code, date parsing or HTTP.

Serve HTTP using Tokio 1.x and Axum 0.8.x on an independent runtime thread;
ingestion never runs on an HTTP executor. Preserve `/metrics` and the existing
plain `OK` fallback, address and port. Use a library text encoder and existing
compression middleware if wire fixtures confirm clients need it. Gather/encode
off ingestion with one concurrent encoding job and bounded admission. D2 below
revises the initial immediate-overlap rejection: support the two configured
Prometheus consumers with one active encoding and one bounded waiter; reject
excess demand or an expired wait with 503. Response bytes are independent of
collector state before writing to the client. Configure standard connection/
request timeouts so slow clients cannot accumulate indefinitely. Cached atomic
updates avoid HTTP backpressure; first-time series creation can briefly contend
with registry gathering and must be measured in the cardinality benchmark.
Do not promise transactional cross-family scrapes; Ruby provides none either.

Official current references checked on 2026-11-10:

- [prometheus 0.14.0 API](https://docs.rs/prometheus/0.14.0/prometheus/)
  and [literal-name encoder source](https://github.com/tikv/rust-prometheus/blob/v0.14.0/src/encoder/text.rs).
- [prometheus-client comparison](https://docs.rs/prometheus-client/0.25.2/prometheus_client/).
- [Tokio API](https://docs.rs/tokio/latest/tokio/), [Axum API](https://docs.rs/axum/latest/axum/),
  [nix fcntl](https://docs.rs/nix/latest/nix/fcntl/enum.FcntlArg.html),
  [Serde JSON](https://docs.rs/serde_json/latest/serde_json/),
  [Clap](https://docs.rs/clap/latest/clap/), [regex](https://docs.rs/regex/latest/regex/),
  [time](https://docs.rs/time/latest/time/).
- [rsyslog ompipe reference](https://docs.rsyslog.com/doc/configuration/modules/ompipe.html):
  confirms FIFO actions and resume/reopen configuration; it does not establish
  the deployed queue, template or delivery guarantee.

These have current published APIs and established upstream projects; this is
dependency-selection evidence, not a security audit or a guarantee of future
maintenance. Pin exact compatible releases in Cargo.lock, inspect their MSRV,
licenses and current advisories during implementation. Consumer default
rustPlatform is Rust **1.95.0**, established by C; choose that toolchain and an
edition it supports. Do not upgrade configuration channels solely to compile a
gratuitously newer dependency. Verify imported CI action refs from official
repositories at implementation time, not from remembered version numbers.

## Cargo, Nix, hooks and complete Ruby removal

Commit Cargo.toml/Cargo.lock and pin Rust 1.95.0 in rust-toolchain.toml, matching
the consumer build. Keep shell.nix but replace its Ruby installer hook with a
Rust/Cargo/rustfmt/Clippy environment; no network package installs on shell entry.
Document the tested pinned nixpkgs invocation so development and CI can reproduce
the consumer toolchain. Do not add an exporter flake input/channel to the site.
Use the existing configuration-local `packages/syslog-exporter/default.nix` as
the single production `rustPlatform.buildRustPackage` recipe, with exact source
revision/hash and Cargo dependency hash; derive runtime version from Cargo.

Replace Overcommit with checked-in `.githooks/pre-commit` calling
`scripts/check` and a documented one-time `git config --local core.hooksPath
.githooks`. The shared check entry point runs `cargo fmt --all -- --check`,
`cargo clippy --locked --all-targets -- -D warnings` and the fast Rust tests.
Hooks never stage, autoformat or modify unrelated changes. Replace the RSpec
workflow with GitHub push/PR/manual checks using the same commands, locked
dependencies, read-only permissions, timeout and branch concurrency cancellation.
Run Linux FIFO/HTTP regression tests in CI; keep performance thresholds out of
noisy hosted-runner timing gates. A manual benchmark target uses the documented
same-host baseline procedure. Long local checks use the required watcher.

After translating fixtures, remove all Ruby `lib/`, `spec/`, config.ru, Gemfile,
gemspec, Rakefile, `.rspec`, Overcommit/RuboCop configuration and obsolete ignore
entries/workflow. Retain the Test collector's behavior in Rust. Update README,
sample JSON and ignore `/target`; preserve license/editor metadata. No legacy
Ruby runtime path or optional dual implementation remains in the final exporter.
The baseline Ruby checkout/closure is verification/recovery material, not shipped
fallback code.

In configuration, replace Rackup/Puma-generated launch files with the Rust CLI;
retain unit/options/settings/FIFO/user/group/stateDir/listen/firewall/scrape names.
Use `Type=simple`, remove Puma's notify/watchdog settings and RACK_ENV, retain
Restart=on-failure/RestartSec=30. Implemented input failures exit the process;
HTTP remains independent. Adding systemd readiness/watchdog support is unnecessary
for this first replacement and would need an ingestion-aware definition.
Remove only `packages/syslog-exporter/{Gemfile,Gemfile.lock,gemset.nix}` and its
entry in `.github/workflows/daily-update.yml`'s Ruby update loop. Do not remove
Ruby from confctl, unrelated packages or nodes. Preserve new log-reader ownership,
rotation and all normal file logging; no rsyslog change is proposed initially.

## Verification and performance acceptance

Before Ruby removal, generate versioned language-neutral input/expected fixtures
with the **configuration-pinned Ruby closure**, including actual middleware
scrapes. Record source/dependency identities. Store fixtures and expected results,
not a permanent Ruby oracle in normal Rust CI. Normalize only sample/label order
and equivalent numeric rendering; compare family names, TYPE/HELP, escaping,
label omission/empty values, startup presence and zero-after-expiry exactly.
Mark deliberate differences (first line, robust malformed/kernel handling,
monotonic expiry, renewal race, frame bound, effective-capacity fallback).

Quick tests cover all R detectors and negative matches, gates, name/FQDN routing,
host collisions, literal-space/svlogd/PID parsing, Unicode/escaped labels, newline
anchor behavior, fake-clock renewal/expiry and interleaved hosts. Include every
alert-consumed metric. Test real HTTP exposition with promtool where available.
Linux integration tests cover FIFO startup without a writer, split/coalesced
writes, first complete line, empty EOF, reopen, malformed/oversized recovery,
slow concurrent scrape and orderly shutdown. No test waits 240 seconds when a
fake clock resolves the same contract.

I includes all intended test and benchmark-driver source. Commit I, pass its
quick checks and independently review the exporter under mandatory-change-review,
including whole-branch history and "no migrations" provenance. C2 then selects
that exact reviewed exporter head, commits the final pin and configuration,
passes configuration quick checks and receives its independent final review.
Neither exporter review nor its source head depends on a completed C2 build.
Only then does V run longer pinned-rsyslog/system/performance checks with a fresh
verification watcher, using the already reviewed driver and writing evidence
only. Findings requiring source changes return to the owning implementer and
affected review/check lane; changed exporter heads also refresh C2's exact pin.
This planning record itself requires no automatic review.

For the performance gate, use the same isolated machine, CPU allocation, kernel
pipe size, host map, input bytes, scrape schedule and run duration for old and
new. Record exact release binary/store paths, source/input identities, compiler
profile, CPU/RSS and filesystem headroom. Generate a seeded corpus from sanitized
real shapes: ordinary messages, OOM start plus long stack traces, namespaces,
osctld/nodectld/LXC/WebUI events, unknown hosts, and mixed record lengths. Derive
host/label distribution from configuration and permitted observations. Fixed
cardinality and high-cardinality profiles are separate. No production rate is
assumed; a synthetic stress profile must be labelled synthetic.

1. Measure Ruby's largest repeatably sustainable rate for that corpus without
   growing pending work, loss or scrape timeout. Use finite sequence-marked
   inputs, a final marker and at least three matched runs; warm up separately.
2. Replay sustained traffic and repeated finite bursts around that measured
   boundary through the actual pinned central rsyslog 8.2610.0 configuration in
   a disposable fixture. Inspect TCP, UDP and local paths separately. Count
   submitted/accepted, archived, FIFO-observed and exporter-accepted records
   independently wherever observable; inability to observe a stage is a gap,
   not proof of delivery. Do not run two readers on one pipe.
3. Proposed acceptance: all supported events that reach the reader are reflected
   exactly; Rust's sustainable rate is at least **2× the measured Ruby baseline**
   on both ordinary and OOM-heavy fixed-cardinality profiles; at that offered
   rate finite bursts drain before the next burst, with no observed loss in the
   supported transport fixture. This is a target to verify, not a forecast.
   Report achieved capacity even on failure and revisit design before rollout.
4. Concurrent ordinary 60s scrapes must complete inside the configured scrape
   timeout with margin; require p99 at most 1s in the isolated test and no more
   than 10% ingestion throughput degradation from normal scrape activity.
   Stress slow/concurrent clients separately. Compare maximum RSS with Ruby at
   the same finite workload; require no ongoing growth after fixed-cardinality
   warm-up and no worse peak RSS than Ruby. Report dynamic-series memory growth
   honestly instead of claiming a total cap.
5. Saturate/pause the reader past FIFO capacity, stop/restart both sides and
   terminate during backlog. Record actual lost/delayed/truncated records,
   reopen time and recovery; no all-load or cross-restart zero-loss criterion is
   asserted. If the useful burst fails due to transport, resolve that contract
   before production acceptance rather than presenting parser speed alone.

Keep one compact benchmark driver/fixture recipe with exported results; do not
build a benchmarking framework. Production burst distribution and acceptable
maintenance gap remain operational inputs. Performance evidence can release a
candidate only for its measured envelope.

## Packages, ownership and release boundaries

These are proposed later assignments; the lead owns allocation/acceptance and
checks member capacity/settings. Do not fill retained slots merely to parallelize.

| Package | Owner and files | Dependencies, acceptance/checks and evidence |
| --- | --- | --- |
| D: this proposal | architect0; this file only | R/C accepted; settled design and explicit gates. Lead accepts proposal; no application changes. |
| I: Rust replacement | implementer0; exporter source, tests/fixtures and small benchmark driver, Cargo, shell, hooks, CI, docs and Ruby removal | Accepted D and implementation authorization. First capture pinned Ruby wire fixtures and validate producer framing; then implement, passing parity/quick checks. Deliver exact base/head, file inventory, command results, intentional deviations, complete series/no-migration provenance. |
| C2: consumer integration | implementer1; configuration package, exporter service module, daily-update loop and reusable operations docs | Can prepare against settled CLI/JSON/service contract; final pin/hash needs I's reviewed published head. Evaluate log-host JSON/unit/FIFO/ownership; build package then host; preserve input graph. Deliver exact source/hash/closure evidence and rollback instructions. No activation authority. |
| V: end-to-end/performance evidence | implementer0 after I is reported/accepted; session evidence using I's committed test/benchmark driver | I/C2 quick checks and final review, exact pinned Ruby/Rust/rsyslog inputs. Watcher runs long checks; implementer diagnoses. Deliver measured envelope, loss accounting, RSS/scrape results and residual limits. Relevant fixes return to owned packages/review. |
| Release coordination | lead; session rollout/review records | Final evidence, explicit integration/deployment directions and installed coordination procedure. Reviewer remains independent/read-only; no automatic planning review. |

I's collector/parser unit design is settled. Actual wire escaping/nil/empty-series
goldens, producer format/maximum record size, dependency compilation and loss
behavior must settle before claiming implementation parity/release. These need
bounded fixture work, not more exploratory design. C2's option/ownership and
CLI contract is settled independently; source hash and rollout await I/V.
Implementers own application edits; architect resolves routine contract questions;
scope/ownership/transport changes go through the lead. Sequence overlapping index,
Cargo.lock, commits and source-pin changes within explicit owner windows.

## Integration, rollout and recovery

1. Prepare/publish exporter and configuration feature branches in this session's
   worktrees; pin the exact exporter revision in the local package recipe.
   Avoid unrelated configuration/channel changes. Complete quick checks, final
   review, CI and longer verification. Evaluate/build only the log host first;
   no coordinated running-node update is required.
2. Before activation, confirm the actual deployed generation and retain its exact
   Ruby system closure plus old/new package/system store paths and complete input
   graph in the rollout receipt. Inventory stateDir before assuming it is empty;
   exporter source has no persistence, and Rust adds none. Keep log files,
   permissions, stateDir and ordinary rotation/recovery contracts intact.
3. On explicit deployment direction, read selected runtime coordination guides,
   prepare build/copy before acquiring machine ownership, dry-activate and switch
   only `log.int.prg.vpsfree.cz`. One live FIFO reader: stop old, start new. Minimize
   the gap and avoid rsyslog restart unless activation actually requires it.
   Do not inject fake production OOM/fatal events for testing.
4. Verify exporter and syslog units, continuing file logging, FIFO consumption,
   `/metrics`, unchanged labels/alerts and multiple 60s scrapes plus a full 240s
   flare window. Compare runtime behavior with the measured envelope; an HTTP
   `up` check alone is insufficient. Record restart counter reset and any gap.
5. On regression, stop Rust and reactivate the retained Ruby system closure,
   then verify the same services, logging and metrics. No state conversion or
   data deletion is required. In-memory counters/gauges reset in either direction;
   rollback cannot recover FIFO events already lost.
6. Integration needs separate explicit direction for each repository/master.
   Prefer integrating the verified exporter before the configuration pin when
   both are approved. Refresh targets and reviewed history outside claims; use
   short merge claims only for fresh check/required hooks/fast-forward push/remote
   proof, releasing before CI or records. Preserve exact final-head rules. If
   history changes, retain old/new ranges and independently justified equivalence;
   a substantively different successor requires verified deployment.
7. Once deployment and its complete feature lineage are verified in approved
   remote defaults, inspect authoritative machine ownership, reconcile unfinished
   effects, release this session's exact machine claim and verify release. Do not
   retain a successfully integrated machine for separate UI acceptance. Uncertain
   deployment or missing lineage proof keeps it held. This never authorizes
   closing, archiving, deleting or otherwise cleaning the session.

## Disk discipline and remaining gates

The user's disk constraint applies throughout implementation. Lead reports 91 GiB
available with 91% usage at planning time; this is not reserved capacity. Check
filesystem headroom and owned directory sizes before/after build batches. Reuse
one explicit session-owned `CARGO_TARGET_DIR` for compatible checks; avoid per-
worktree duplicates. Use nonincremental/reduced-debug disposable check profiles
where useful; preserve recorded release settings for comparable benchmarks.
Do not duplicate Nix closures into worktrees or retain full raw logs unnecessarily.

Remove proven session-owned disposable target/temp/benchmark data promptly once
no active process, rerun, review evidence or recovery depends on it. Retain compact
results, fixture seeds/hashes and necessary rollback closures. Never run broad
workspace cleanup/Nix GC, delete peer data, or infer lifecycle permission from
this instruction. This phase created only small records and had no build data to
delete. Disk exhaustion is a reason to stop the next build and reassess owned
outputs, not to broaden cleanup authority.

Remaining gates are operational: real Ruby exposition, pinned rsyslog bytes and
overflow/reconnect behavior, dependencies on Rust 1.95, measured capacity and
production envelope, actual deployed generation/stateDir, and explicit later
implementation/integration/deployment directions. No further source investigation
is planned for package D. Durable feature/protocol/failure documentation belongs
in exporter README plus linked reference/how-to pages; reusable site rollout/
rollback guidance belongs in configuration operations docs. This rollout's exact
revisions, results and receipts stay here in session records.

## D2: two normal scrape consumers (2026-11-11)

Bounded design clarification requested by the lead; recommendation ready for
lead acceptance/release, not an application edit or deployment authorization.
The observed V 503 coincided with final-marker polling and the periodic scrape;
the reported 960,000 input count was exact. That fixture collision does not
establish ingestion failure. It does expose a supported concurrency gap.

At final configuration `75b0af0323db1412de457cb73362fd741941eef4`:

- `cluster/cz.vpsfree/containers/prg/int.mon{1,2}/module.nix:33` declares both
  machines monitors. Their `config.nix:14`/`:16` enables independent Prometheus
  instances without a `monitorMachines` restriction: **two configured consumers**,
  `mon1.int.prg.vpsfree.cz` and `mon2.int.prg.vpsfree.cz`.
- `modules/clusterconf/monitor/default.nix:52`, `:128`, `:737` selects monitored
  loggers for both and gives each the same `log` scrape job every 60 seconds.
  Neither source coordinates the two scrape schedules or forbids overlap.
- Logger `config.nix:46` and `:82` permits both monitors to access port 9102.
  Logger `module.nix:32` checks unit state only; `health-checks/monitoring.nix`
  checks Prometheus's own `localhost:9090/-/healthy`, not exporter metrics.
  No additional exporter HTTP health caller was found in these scoped references.

This establishes intended configuration, not live deployment state or measured
scrape phases. At exporter `8ef8241c60f3b99976191b92f0467c945e36b1c8`,
`src/http.rs` uses `try_acquire_owned()` on one encoder permit and rejects the
other request immediately. Both legitimate monitor requests must be serviceable
when their finite encodes overlap. The original 503-on-any-overlap decision is
therefore revised; excluding the benchmark collision alone is insufficient.

**Minimal implementation brief, owner implementer0:** retain one encoding worker,
32 connection limit and existing connection lifetime. Admit at most two metrics
handlers total with a nonwaiting admission permit, then wait asynchronously for
the existing single encoder permit for at most one second. This admits one
active encode and one waiter, including across HTTP/2 streams; a connection cap
alone is not a request cap. Excess admission or wait expiry returns 503. Move
both owned permits into the blocking encode so client cancellation cannot free
capacity while encoding continues; release them when encoding finishes, before
slow network writes. No shared-response cache, new worker pool, broker or metric
semantics change. Adjust `src/http.rs`, focused HTTP regression tests and the
existing HTTP contract documentation only. Lead owns release of this work.

Tests must force overlap deterministically (hold/release the encoder), assert
that the two admitted requests return valid 200 exposition after release, and
cover a third request, wait timeout and permit recovery/cancellation. Keep FIFO
ingestion independent. Existing normal-load latency and throughput criteria
still apply to both consumers; pathological encoding exceeding the deadline
may yield 503, and more than two concurrent scrapes remains explicit overload.

Commit and quick-check the narrow change, obtain affected independent HTTP/review
coverage, then refresh C2's exact exporter pin and package/host receipts through
its owner. Reuse unchanged Ruby wire/parser/collector/transport evidence only for
that unchanged scope; it does not certify the new HTTP behavior or final package
identity. Rerun focused two-consumer scrapes during ingestion, normal-scrape V and
the relevant scrape/no-scrape performance comparison on the final binary. Do not
repeat unrelated transport campaigns solely because HTTP admission changed;
revisit them only if relevant code or inputs change. Preserve the original
selfcollision result and distinguish the separated-poll diagnostic from the new
two-consumer acceptance check. No further D2 investigation is needed.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/>.
