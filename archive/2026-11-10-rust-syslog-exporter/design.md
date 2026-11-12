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

## D6: compatibility boundaries and open comparison (2026-11-11)

This is an inventory of accepted decisions, not certification that arbitrary
Ruby-accepted text has identical Rust behavior. Baseline is Ruby
`7c5a8e74e44a704cceb99cd05716af6800d78efd`; final provider is
`6ecada0a9d2f6457a11031a3a4ffc341584fb29c`. The deployed `3hk` binary/`gsw`
system identity is retained in [rollout.md](rollout.md), with source equivalence
evidence there and in [exporter-review.md](exporter-review.md). This clarification
does not change production, interfaces, source, or release authority.

Evidence: [R's exact Ruby contract](ruby-contract.md), original D and D2 above,
[final runtime reference](https://github.com/vpsfreecz/syslog-exporter/blob/6ecada0a9d2f6457a11031a3a4ffc341584fb29c/docs/reference.md),
final `src/{parser,config,input}.rs` for the boundaries below, captured fixture
inventory in exporter-review, and [I2's affected review](i2-final-review.md).
Reviewer0 owns R2's independent parser/collector comparison; implementer1 owns
P2's small executable differential replay. Architect did not repeat that audit
or run tests. Results from those packages remain a dependency, not an assumed
outcome of this classification.

| Area | Intended difference and reason | Impact / correction boundary |
| --- | --- | --- |
| First record | Rust processes the first complete line; Ruby always discarded it on each open. Fixes certain event loss. | A replay must isolate this known difference so it does not masquerade as a detector mismatch. Rust still must process subsequent valid records exactly once. |
| Invalid/missing fields and timestamps | Rust rejects malformed required headers/timestamps per record and keeps running; Ruby sometimes admitted missing fields and sometimes terminated a thread/process on error. Rust currently validates RFC3339, the pinned producer's timestamp subset, rather than all Ruby `Time.iso8601` forms. | Changes malformed-record counts and liveness. Broad ISO8601 parity was not established. A valid required producer timestamp rejected by Rust is a compatibility gap; it cannot be excused merely by calling the parser stricter. |
| Encoding and record limit | Rust rejects invalid UTF-8 and records over the configured limit (default 1 MiB including LF), discarding through LF. Ruby had no explicit line bound; encoding-sensitive operations could fail. | These are documented policies, not proof that all producer output is UTF-8 or within bounds. Pinned rsyslog preserves high bytes. Captured valid UTF-8 controls do not establish invalid-byte equivalence. If required producer content crosses either boundary, lead must resolve the compatibility gap explicitly. |
| Program normalization | Rust safely handles ordinary `kernel[digits]` and forwarded kernel variants; Ruby's generic/kernel class mismatch could crash, and some forwarded variants missed the kernel collector. Other forwarded programs remain verbatim. | This expansion is deliberate. No general colon stripping, nested-header parsing, case folding or arbitrary tag normalization is authorized. A program `1` remains program `1`; an embedded `kernel` later in its body is not the kernel program field. |
| Host/config behavior | Exact host-key or FQDN routing and first-config-match collision selection remain. Unknown hosts are now counted rather than silently discarded. Startup requires valid types/nonempty required strings/positive sizes and an actual FIFO; unknown config keys remain ignored. | Stronger validation can reject old malformed configs earlier. Alias remains output-only. Any changed routing for valid generated config or an intended allowlisted host requires correction; do not auto-add unknown hosts. The unknown-host counter alone does not prove a new discard. |
| EOF, shutdown and buffering | Rust drops/counts an incomplete EOF/shutdown tail, closes before a short interruptible reopen delay, finishes already-read complete records on orderly stop, and has no unbounded parsed-message queue. Pipe-enlargement refusal falls back to actual capacity. | Ruby could pass a final unterminated line to parsing and used a one-second reopen delay. Restart buffering/timing are intentionally different; neither implementation guarantees cross-restart delivery. A lost complete record already handed to the new framer is not justified by this policy. |
| Flare timing/order | Rust uses monotonic processing time and one state owner; duration/renewal keys, strict expiry, five-second sweep and retained zero series remain. Fixes clock-jump sensitivity and concurrent reset-over-renewal race. | Wall-clock jumps and overload backlog can change observed timing; message timestamps never determine expiry. Changes to detector precedence, host/label isolation, configured TTLs, metric increments or ordinary renewal/expiry semantics remain defects. |
| HTTP and diagnostics | Separate HTTP runtime, bounded two-request admission after D2, one-second encoder wait, 32 connections/30-second lifetime; additional fixed diagnostic families. Small fallback compression headers can differ. | Normal two-monitor overlap must succeed within the tested envelope. Overload/timeout may return 503. Legacy names/types/HELP/labels/initial presence/zero retention and decoded exposition remain compatibility requirements; bounds do not authorize ordinary scrape failures or changing alert semantics. |

The positive kernel-buffer alert reported by the user proves that one current
kernel-input/forwarding/detector/alert path worked. It does not establish how
either exporter treats the separately supplied nested-header record. For that
exact archived shape, source predicts outer program `1` in both parsers and no
kernel-bug trigger. Treat that as a hypothesis pending P2's executable replay,
with first-record handling controlled and positive controls included; do not
accept or dismiss the user's broader inference solely from recollection.

**Fix boundary:** a concrete difference in required valid FIFO input, routing,
collector gate/detector precedence, count/labels or pulse semantics outside the
enumerated intentional decisions is a correction candidate. Preserve the tiny
input/result vector, determine affected scope, and route the fix decision through
the lead. Accepted design intent cannot retroactively excuse an implementation
mismatch. R2 may find regex/whitespace/anchor/encoding differences that existing
goldens did not exercise; this inventory neither asserts nor rules them out.
Conversely, a transport changing the outer program before the exporter receives
the record is not by itself a Rust parser regression. No collector rewrite,
parser widening or source fix is authorized by this addendum.

Existing wire goldens, quick checks and measured/live evidence cover their stated
fixtures and envelopes, not all arbitrary message bytes, Ruby's full timestamp
grammar or every irregular delimiter/body combination. R2/P2 findings and their
lead disposition must be reported before an unqualified compatibility assurance.
No new broad test campaign is requested here.

## D7: bounded compatibility corrections and essential-service continuity

2026-11-11, architect0. Sufficient brief for lead release of I3; user authorized
the fixes and requires the exporter to remain running and working on log.int.
R2/P2 established concrete mismatches, not a production outage. Healthy deployed
`3hk`/`gsw` remains serving throughout preparation. This section supersedes D/D6's
whole-record rejection of invalid UTF-8 bodies and permits only the corrections
below. Other parser, metric, HTTP and transport interfaces remain frozen.

### Source contract

1. Restore Ruby's ASCII shorthand matching: PID and svlogd date/time recognizer
   digits are `[0-9]`; namespace whitespace is exactly ASCII space, tab, LF, VT,
   FF and CR. Unicode whitespace/digits remain ordinary literal input, without
   normalization. Preserve all other regex anchoring, captures and precedence.
   Thus U+0661 in a PID does not turn its program into `kernel`, and NBSP remains
   in a namespace label. Ordinary ASCII PID/kernel forms and supported forwarded
   kernel normalization retain their accepted behavior.
2. Restore Ruby `String#strip` semantics for LXC IDs: trim only NUL and those six
   ASCII whitespace characters, not NBSP or other Unicode whitespace. Preserve
   the legacy first-colon rule exactly: no colon gives an empty ID; a colon at
   positive offset selects its preceding prefix; colon at offset zero selects
   the whole body (Ruby's `0..-1` slice). Apply the same strip rule to the selected
   string. This includes the verified odd colon-zero case; no new ID validation.
3. Parse framing/header boundaries from the raw bytes using the existing literal
   ASCII spaces, then validate every actual header field as UTF-8. Outer timestamp
   remains RFC3339. Host/program are borrowed valid strings; invalid bytes in
   them are rejected with the existing `utf8` rejection reason, never repaired
   into routing identities or labels. Recognize the supported localhost/svlogd
   prefix with the restored ASCII grammar; once that branch is selected, its
   inner host/program are headers and require valid UTF-8 too. Recognition must
   not validate the whole remaining message just to inspect the prefix, or
   accidentally promote an ordinary localhost message body into a header. A
   prefix that does not match retains the existing ordinary-message fallback;
   no broadened date/header grammar or nested RFC5424 decoding is introduced.
4. Represent **only the body** as `Cow<'a, str>` (or the equivalent conventional
   borrowed/owned representation). Use borrowed valid UTF-8 without a new
   per-message allocation; decode invalid body bytes once with standard
   `String::from_utf8_lossy`. Invalid sequences become U+FFFD, never deletion,
   so bytes inside an ASCII signature cannot join its halves into a false match.
   Existing contiguous ASCII signatures before/after invalid bytes must still
   work, including nodectld's raw-FF crash vector. All collectors and body-label
   extraction see the same decoded body; do not decode independently per collector.
5. Valid UTF-8 bodies remain byte-for-byte unchanged except the explicit matching/
   trim corrections above. Body-derived `syslogns`, LXC `id` and osctld `command`
   labels use that same text, including U+FFFD where necessary; the established
   Prometheus encoder handles escaping. Different invalid sequences, or a literal
   U+FFFD, can consequently share a label value. This is the explicit policy for
   previously rejected bodies, not lossless byte-label equivalence with Ruby.
   No invalid UTF-8 label bytes, surrogate escaping scheme, hashing, extra dynamic
   labels or new codec is introduced.
6. Add one fixed, unlabeled diagnostic counter,
   `syslog_exporter_body_decoded_records_total`, counting each successfully parsed
   record whose body required replacement decoding once, before known-host routing.
   Invalid-header records do not increment it; unknown-host records can. This
   counter overlaps ordinary intake counts and must not be added to them. Existing
   `rejected_records_total{reason="utf8"}` now means a header UTF-8 rejection;
   accepted repaired bodies are not rejected records. Byte/record counters continue
   to describe the raw FIFO input. Do not log payloads or individual replacements.

Framing limits remain measured in original bytes including LF and enforced before
decoding. Retain LF exactly in the body, oversized discard-through-LF and incomplete
EOF/shutdown rejection. Standard replacement decoding allocates only on the rare
invalid-body path, at most three output bytes per input body byte, still bounded
by the existing one-record limit. No message queue, worker, new dependency,
configuration option or cross-record state is needed. Preserve deliberate
first-record processing, malformed-header rejection, monotonic flare ownership
and D2 HTTP admission. Original `program=1` records remain program `1`.

### Packages and required evidence

| Package / owner | Files and dependency | Acceptance and evidence |
| --- | --- | --- |
| I3 / implementer0 | `src/parser.rs`, LXC extraction in `src/collectors.rs`, minimal decode diagnostic wiring in `src/{input,metrics}.rs`, focused existing tests/fixtures and existing reference/verification docs; manifests/dependencies/HTTP unchanged | Lead accepts D7 before edits. Correct concrete R2/P2 vectors, full existing quick suite, formatter/Clippy/hooks, exact committed/published head, changed-file inventory and reviewed history. Owner retains fixes. |
| R3 / reviewer0 | Read-only affected independent review of final I3 commit and complete branch history | After I3 quick checks, before long package builds/replay. Cover UTF-8 header/body separation, delimiter preservation, ASCII matching/labels, bounded rare path, diagnostics and tests. No migrations; preserve earlier review for unchanged scope. |
| C4 / implementer1 | Dependent configuration package pin/hash and existing receipts/docs only | Prepare in parallel without activating. Final pin requires reviewed I3 head; applicable configuration checks/review precede long Nix work. Build exact package/host, retain full source/input/closure proofs and healthy-current rollback paths. No unrelated input/module change. |
| V3 / existing verification owners through lead | Execute committed fixtures/driver against the final Nix binary, using the required watcher for long checks | Focused parity and ordinary/OOM rate plus two-consumer scrape smoke below. No new driver/framework or complete matrix repeat. Lead accepts result and controls any rollout/integration. |

Meaningful quick regressions must assert parser/collector/exposition outcomes:

- P2's two exact user records still count as program `1` without a kernel flare;
  direct kernel/FQDN positive, `kernel[]`, valid ASCII PID, normal MSG-leading space
  and fresh isolated svlogd controls retain their expected results.
- U+0661 PID, ASCII-versus-Unicode svlogd recognition, NBSP namespace/LXC ID,
  ASCII/NUL trimming and colon-zero/no-colon/ordinary-colon cases match the agreed
  Ruby outcomes. Use concrete P2 vectors, not a newly generated combinatorial suite.
- Raw FF before/after an intact nodectld crash signature yields message count and
  flare; invalid bytes inserted **inside** a signature do not synthesize a match.
  Cover invalid bytes at body start/end, a truncated UTF-8 sequence, a valid
  literal U+FFFD and body-derived replacement labels. Verify the one-per-record
  diagnostic and unchanged legacy labels/counters on valid input.
- Reject invalid UTF-8 in outer timestamp/host/program and in recognized svlogd
  inner host/program. Ordinary and recognized-forwarded invalid bodies must be
  accepted without relaxing header grammar. Verify the valid-body representation
  stays borrowed; no bespoke allocation-counting framework is needed.
- Existing real framing tests must still prove split reads, exact LF/size
  boundary, oversized recovery, incomplete EOF and clean shutdown. Decoding must
  not change which bytes form a record. Run the full existing suite as well as
  these focused regressions, rather than mirror helper implementation in tests.

After R3 and the dependent final pin are ready, run the committed parity cases
against the exact final Nix binary and known Ruby baseline, allowing only the
documented deliberate changes. Reuse HTTP/transport/lifecycle evidence solely for
unchanged code/input scope; it does not prove the new binary identity or newly
accepted body behavior. A small fresh performance batch is sufficient: three
matched Ruby/candidate 100,000-record pairs for each existing ordinary and OOM
profile, same host/resources/corpus/settings, followed by one existing normal
65-second/~16k-per-second two-consumer scrape smoke on the final binary. Preserve
counts, medians/ranges, RSS/CPU and scrape results; no new cardinality, overload,
1 Hz stress or transport matrix is required without a relevant new failure.
Retain the established measured-envelope interpretation: finite rate lower bounds
are not production-peak or isolated causal-10% certification. If noise prevents a
conclusion, report it rather than repeatedly sweeping rates.

Keep the source commit's measured-performance prose accurate: label previous
numbers with their original measured binary/source, and label V3 results with
the final candidate identity. A later message-only amendment requires exact tree/
binary equivalence and updated pin receipts under the existing rules; it is not
a reason to silently attribute an old benchmark to changed code. Reuse one owned
target, respect disk headroom and remove only proven disposable owned outputs.
Report current CI honestly; a GitHub outage does not authorize an infrastructure
project or pretending current-head CI passed. Lead decides readiness from required
local exact-build/check evidence and the actual CI state.

### Essential-service cutover and recovery

No rollout or restart occurs during I3/R3/C4/V3. The existing `3hk`/`gsw` service
must remain serving; never attach a second reader to its FIFO. Preserve held
machine ownership `6fda` and the exact current/prior recovery receipts. Retain the
healthy current Rust closure as the immediate fallback and keep the original
Ruby recovery closure/contract intact. No metric state migration is introduced.

Before lead-owned activation under the recorded user authority, finish review,
checks, final source/pin/closure proof, copy and disposable preflight. Confirm
current service identity/health, FIFO ownership and package/config/CLI agreement.
Missing evidence, unsuccessful preflight, insufficient disk/recovery closure or
uncertain command effects stops the cutover while the current service keeps
running. No merge before correction review and readiness.

Switch exactly one live reader with the unchanged unit/port/FIFO/settings. A
brief restart gap is unavoidable; do not promise zero interruption or replay.
Check active service and HTTP immediately: an explicit startup failure, crash
loop or lack of a healthy response within 30 seconds requires prompt rollback
to the retained healthy current closure, not waiting through repeated restart
cycles or the 240-second flare window. Then verify ongoing FIFO intake alongside
normal file logging and expected host metrics; distinguish genuinely idle input
from a stalled reader using existing permitted evidence, without injecting tests
or reading payloads on the architect's authority. Unexpected parser rejection,
missing known-active intake or service degradation requires lead reconciliation
and rollback if the candidate cannot promptly be established healthy.

Once startup is healthy, complete the existing bounded live observation/expiry
checks and record exact effects. Counters reset on replacement/rollback; neither
recovers already-lost FIFO events. Integrate only after correction readiness
under the user's named-repository approval, then establish final remote lineage
before releasing machine ownership per the installed procedure. Do not release
an uncertain deployment or reinterpret successful cutover as session lifecycle
permission. Architect performs no application edit, build, activation or merge.

All D7 choices above are settled for source release; no further investigation is
needed. Lead accepts this sufficient boundary and assigns I3. Any wider grammar,
transport, label encoding or HTTP change returns to the lead for scope decision.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/>.

## A: automated compatible Cargo.lock maintenance (2026-11-12)

Sufficient brief for lead acceptance and I0 release. The user authorizes future
routine verified lockfile commits to exporter `master` as `github-actions[bot]`,
without PRs or routine human review. Initial workflow integration/activation
remains lead-owned after committed review and verification. This package changes
only the exporter repository; configuration pins, production, manifests/MSRV and
flake-input upgrades are outside automated update scope. Preserve merged
`891db6b82ccd37e985507c654050143e165041a7`; independently useful flake commit
`99ffea73005685fc9f198dda3402fe24660ee944` may remain its own logical commit.

The bounded source pass inspected F's Cargo/flake, existing CI/check hook,
benchmark driver and test coverage. F provides a shell, not a package build.
`Cargo.toml` requires Rust 1.95; the unchanged nixpkgs pin supplies that toolchain.
The existing lock is approximately 27 KiB. No application edit, build, test or
external mutation was performed for this brief.

### Workflow and trust boundary

Add `.github/workflows/update-lockfile.yml` with a monthly off-hour schedule
(for example `23 4 1 * *`, UTC) and `workflow_dispatch`, whose `publish` boolean
defaults to false. A scheduled default-branch run may publish; manual publishing
requires `publish=true` on `refs/heads/master`. Relevant non-default branch
pushes validate the feature with publishing unconditionally disabled. Limit that
push trigger to this workflow, its helpers, benchmark, Cargo and flake files;
default-branch pushes do not repeat the long campaign. Use one workflow
concurrency group with `cancel-in-progress: false`, finite job timeouts, and
fresh GitHub-hosted Linux runners. Scheduling can be delayed; this is monthly
maintenance, not an advisory-response SLA.

Use three jobs, with no secrets other than their scoped `GITHUB_TOKEN`:

1. **Prepare, contents:read.** Checkout the trusted event `github.sha` with
   `persist-credentials: false`; never accept a source/base SHA from an artifact.
   For a publishing run require fresh remote master to equal that SHA. Run
   `cargo update` with the pinned Cargo 1.95 environment, without changing
   Cargo.toml or using incompatible/ignore-rust-version switches. Cargo's
   manifest constraints and subsequent Rust 1.95 compilation are both gates.
   Resolution must not run candidate builds/tests/binaries. Check the tracked
   diff permits only Cargo.lock; freeze it immediately into one immutable
   artifact **before any updated dependency code executes**. Export the original
   upload's artifact ID and lock SHA-256 from this job. Bind metadata to the
   event base and run/attempt. Only Cargo.lock (maximum 1 MiB) and small fixed
   metadata (maximum 4 KiB) belong in this artifact. No source archive, scripts,
   executables or arbitrary paths. A normal scheduled/publishing no-change run
   succeeds without a commit or expensive verification. Feature/manual dry runs
   still verify when resolution makes no change, so bootstrap can be exercised.
2. **Verify, contents:read.** Fresh checkout of that same event SHA, again with
   no persisted credentials. Download the **prepare artifact by its exact ID**
   into a separate directory and validate file type/path/size/hash/base before
   installing the lock. All candidate code runs here, never in prepare or
   publish. Baseline is the same source SHA with its original lock; candidate
   differs only in the frozen lock. Run all gates below. Verify cannot replace
   the publishing artifact or choose publishing metadata; its job success is
   the only release signal. Keep logs/results separate from the lock artifact.
3. **Publish, contents:write.** Require prepare/verify success, a changed lock,
   and the explicit default-branch event policy above. Fresh trusted checkout;
   no cache/target/source artifact from verify, Nix/Cargo invocation, candidate
   binary, dependency install, or candidate build script. Download the original
   prepare artifact by ID, not by mutable name or a verify-job output. Treat
   artifact contents as data: exact two regular files, bounded sizes, valid
   metadata, expected SHA-256 and event-base identity; reject symlinks/extras.
   Copy only Cargo.lock into the clean checkout. Confirm its only tree change is
   Cargo.lock and its parent is the tested event SHA. Freshly check remote master
   still equals that SHA, then make one ordinary nonforce fast-forward push.
   Advancement before either guard stops the run visibly; a push race is rejected
   by Git. Never force, rebase, merge or retry against a different source base.

All publisher logic comes from trusted checked-in workflow/helper code and uses
fixed paths and safely quoted data. Do not execute downloaded material or feed
metadata to a shell. After pushing, verify the committed lock/tree/parent and
remote ancestry; later legitimate advancement is acceptable if the bot commit
is its ancestor. An uncertain push is reconciled by that exact commit identity,
not repeated blindly. A failed gate leaves master unchanged; a failure after
an accepted push must report that distinction. No branch-protection changes,
ruleset bypass, PAT/App installation or auto-merge configuration is needed.

Set both author and committer to `github-actions[bot]` and
`41898282+github-actions[bot]@users.noreply.github.com`, using a fixed explanatory
commit message via a message file. Developer implementation commits retain the
existing mandatory hooks. The automated publisher does not install/run the
build/test hook: its same `scripts/check` gate has already run in the read-only
verifier, as required by the explicit no-candidate-execution write-job boundary.
Document this bot-specific separation, without adding a general hook bypass.

GitHub documents that a GITHUB_TOKEN push does not start push CI; therefore
publication cannot depend on a later Rust workflow. Official artifact docs
describe immutable IDs for v4+ and ID-specific download. Current upstream release
pages identify checkout v7.0.1, upload-artifact v7.0.2, download-artifact v8.0.2,
and install-nix-action v31.11.5. I0 must verify and pin their full upstream commit
SHAs when authoring the workflow; no floating action refs or invented hashes.
Artifact integrity prevents workspace substitution across jobs; it is not proof
that a dependency is benign.

### Required gates and proportional performance check

Keep one owning `rustPlatform.buildRustPackage` definition in `flake.nix` (or a
small `package.nix` called by it). Expose a default release package with
`cargoLock.lockFile = ./Cargo.lock`, `doCheck = true`, release-mode tests and
Python available for existing runtime checks. Preserve the release profile and
flake input; include all source/fixture files needed by tests. This avoids a
second auto-updated cargoHash file. Require an actual sandboxed Nix package
build/check of the candidate, with no skipped tests or sandbox disablement;
a development-shell invocation alone is insufficient. Build baseline and
candidate using this same definition and pinned inputs on x86_64-linux.
The consumer's separate package/pin/hash update remains separate future work.

For every changed lock, before publishing:

- Run the shared `scripts/check`: fmt, Clippy with warnings denied, and the full
  existing 25-test suite, including real Ruby wire goldens and byte/parser,
  flare, FIFO/reconnect, HTTP/gzip/cancellation regressions. Preserve that shared
  entry point for local checks and ordinary CI. Run RustSec `cargo audit` against
  the frozen lock with a successfully refreshed advisory database and record its
  revision. Use the pinned tool from the Nix environment; vulnerabilities or
  audit/network/tool failure block publication, with no automatic ignores.
- Complete the Nix release build and release tests above. Record base SHA,
  original/candidate lock hashes, toolchain, flake input and derivation/output
  identities. Never substitute an old-lock build result for candidate evidence.
- Run `scripts/benchmark.py` against the two Nix release binaries on the same
  runner, sequentially with alternating baseline/candidate order: three matched
  repetitions of 100,000 records for each of `ordinary` and `oom`, fixed seed,
  fixture host map, cardinality, effective pipe capacity and release resources,
  direct transport, unlimited input rate and periodic scraping disabled. Each
  run must finish within its finite deadline, preserve exact reader-stage counts
  and marker, and report no unexpected exit or forced cleanup. Require candidate
  median throughput **at least 75% of baseline separately for both profiles**.
  Record CPU/RSS and individual results; missing/invalid results fail closed.
- Run one bounded candidate socket-level two-consumer smoke during ingestion:
  65 seconds at a rate derived conservatively from this run's baseline (25% of
  its slower profile median), two concurrent scrapes at the normal 60-second
  interval, exact final count/marker, both HTTP 200 and each completing within
  one second, with no scrape error or unexpected shutdown. A small two-client
  option in the existing driver is sufficient. Join the periodic scrape pair
  before final-marker polling so the fixture does not introduce a third request.
  Require evidence of at least one completed pair; do not silently pass a run
  that finishes before the pair. Existing HTTP tests cover admission edge cases.

The 75% rule is an intentionally coarse dependency-regression gate, distinct
from the original controlled rewrite acceptance. Shared-runner noise or generator
limits can block a good update or hide smaller regressions; a green run certifies
only this measured envelope, not production peak, a causal 10% effect, or freedom
from all upstream/supply-chain defects. Update verification prose to distinguish
this conservative CI gate from controlled capacity measurements. Failures remain
visible and require diagnosis; do not rerun until green or relax thresholds
automatically. No Ruby closure download, rsyslog matrix, production probe or
additional benchmark framework is needed.

### Ownership, validation, activation and recovery

One implementation package **A1, implementer0** owns the workflow, owning Nix
package/check definition, small update/validation/publish helpers and focused
guard tests, the minimal benchmark extension, and README/verification maintenance
documentation. No application runtime edits, consumer files or production actions.
Dependency: lead accepts this brief; F is retained/reconciled under its accepted
history boundary. I0 may clarify routine contracts directly with architect0;
scope/permission changes return to lead. No independent I1 implementation package
is needed.

Quick acceptance covers workflow/static syntax, full existing checks, and tests
of the **actual publishing helper** against disposable local Git repositories:
unchanged lock creates no commit; changed verified lock creates exactly one
lock-only child with bot identity; stale base, disallowed path/hash and failed or
missing verification cannot update the target. Exercise actual nonforce push
rejection for an advanced local target, not a reimplementation of Git behavior.
Include guard tests and every intended helper/driver/doc change in the commit.

Sequence: I0 completes and locally commits A1 with quick checks, sends the full
891-to-final range (including F) and packet, then **R0 reviews before A1 is
published**. After affected final review acceptance, publish the feature and run
the read-only feature-push Nix/update/performance validation. This avoids a new
workflow_dispatch bootstrap dependency and prevents premature long checks.
Writer must be skipped even if a feature run supplies `publish=true`. Any fix
returns to I0 and its affected review/check lane. Retain exact run/commit/artifact
IDs, lock hashes and compact results; lead performs the prose pass, accepts the
deliverable and owns initial integration/activation. Do not rerun identical long
checks merely because the reviewed source was fast-forwarded to master.

Routine green scheduled updates subsequently need no human review. Monthly
no-change is successful/no commit. Failure is a visible failed workflow with
master left at its prior value unless the push already succeeded, as recorded
above. For a later discovered bad lock, revert its lock-only commit through the
normal maintained-source process and stop/restrict subsequent publication until
the cause is understood; do not force-reset history or change configuration pins.
Automation never deploys, so service continuity and deployed rollback closures
remain untouched. Disabling the schedule or changing checks is a separate
maintainer action, not an autonomous response that changes repository settings.

Use bounded artifact retention and session-owned disposable targets/temp data.
Monitor headroom, reuse one local Cargo target for checks, and remove proven
owned disposable measurement data when no longer needed; no broad cleanup or
Nix GC. No unresolved design choice blocks A1. Actual action SHA selection,
sandbox/package execution and guard/workflow evidence are implementation gates,
not claims established by this planning pass.

Primary references: [Cargo update](https://doc.rust-lang.org/cargo/commands/cargo-update.html),
[Nix Rust packaging](https://nixos.org/manual/nixpkgs/stable/#rust),
[RustSec](https://rustsec.org/),
[GITHUB_TOKEN event behavior](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow),
[checkout/bot identity](https://github.com/actions/checkout),
[immutable upload artifacts](https://github.com/actions/upload-artifact),
[download by artifact ID](https://github.com/actions/download-artifact),
[Nix installer releases](https://github.com/cachix/install-nix-action/releases).

## B: Dependabot PRs with verified automatic merge (2026-11-12)

**Current sufficient brief; supersedes A's custom updater before source release.**
The user now requests Dependabot with automatic merging when tests pass. A stays
above as decision history; do not implement its prepare/artifact/publish jobs,
direct bot commits or publisher tests. Retain F's independently useful flake
commit and the necessary verification below. Application runtime, configuration,
production and deployed recovery remain unchanged. Routine eligible green PRs
need no human review; initial workflow/configuration integration and repository
settings activation remain lead-owned after review and checks.

### Dependabot configuration and verification

Add `.github/dependabot.yml`: version 2, Cargo at `/`, monthly schedule,
`versioning-strategy: lockfile-only`, `allow: dependency-type: all`, and one
version-update group matching `*`; bound open version-update PRs to one. Keep
normal Dependabot rebasing enabled. Compatibility means existing Cargo.toml
constraints and successful Rust 1.95 compilation, not merely a title or SemVer
label. No manifest, MSRV, flake-input or other ecosystem upgrades. Do not change
security-alert/settings policy as part of this work; any independently generated
security PR must meet the same strict lock-only/test boundary to auto-merge.

Extend the existing read-only `Rust` workflow rather than adding an updater:
`contents: read`, checkout without persisted credentials, no repository secrets,
write permission or privileged event while executing PR/dependency code. Keep
`scripts/check` as the shared fmt/Clippy/full 25-test entry point. For Dependabot
PRs, all of these are required, including an actual exact-content lock-only check:

- Original and candidate differ only in the existing regular `Cargo.lock` file;
  no rename, deletion, mode change, extra file, manifest or workflow change.
  Bound lock size to 1 MiB; verify the complete diff, not a truncated API page.
- Rust 1.95 checks and a fresh RustSec audit, without automatic ignores; actual
  sandboxed Nix release build and full release tests using A's one owning
  `buildRustPackage`/`cargoLock.lockFile` definition and unchanged pinned input.
- A's three alternating matched 100k ordinary/OOM release repetitions, candidate
  median at least 75% of baseline in each profile, exact counts/markers and no
  unexpected exit; its one finite 65-second normal-interval two-client HTTP/count
  smoke. Keep the same conservative noise/performance limitations and bounded
  cleanup. No Ruby fetch, production/rsyslog matrix or new benchmark framework.

Baseline is the tested PR base with its original lock; candidate is that same
source plus the exact PR lock. Record base, PR head, tested merge/tree identity,
lock hashes and Nix outputs. Never benchmark against a moving master checkout or
resolve dependencies again during verification. Use the current PR merge result
for integration checks and verify that it represents this lock-only change.
Stale/conflicting or unidentifiable source fails closed until Dependabot refreshes
the PR and the checks run on the new exact content.

Expose one uniquely named required aggregate, e.g. `Rust required`. It runs with
`if: always()` and explicitly fails unless **every selected prerequisite has
result `success`**. Missing, skipped, neutral, cancelled, failed or timed-out
selected gates cannot satisfy it. Dependabot always selects the complete set
above, including eligibility. Ordinary non-Dependabot changes still require the
normal quick checks; a deliberate maintenance-validation path selects the full
set for feature/bootstrap testing. Required workflow/aggregate triggers must not
be path-filtered away. Keep job names unique, explicit dependencies and per-PR
concurrency; a new head cancels superseded verification without reusing its pass.
GitHub accepts skipped/neutral required checks, so the explicit aggregate logic
is necessary. A green workflow summary alone is not the eligibility assertion.

### Metadata-only merge authorization

Add one small workflow on `workflow_run` completion of the exact `Rust` workflow.
This event uses trusted default-branch code and can obtain write permissions
after an unprivileged PR workflow. It must **never** checkout PR code, download
PR artifacts/caches, install dependencies, run a build/test/binary, or interpolate
PR-controlled text into executable code. Use fixed inline metadata handling
with GitHub APIs/CLI; no custom publisher or artifact protocol. Permissions are
only `contents: write`, `pull-requests: write`, and the read permissions needed
for Actions/check metadata; no administration, secrets, PAT/App or bypass token.
Pin any imported action to an officially verified full upstream commit.

On completion, freshly query GitHub metadata and require all of the following:

- The triggering run belongs to this repository and expected workflow, was a
  `pull_request` verification, completed successfully, and is tied to the current
  PR head/tested base. Resolve its PR through GitHub API associations, not an
  artifact or branch-name convention. Require a unique open, non-draft PR into
  this repository's `master`, authored by GitHub's `dependabot[bot]` Bot identity,
  with its head repository also this repository. Titles/labels/commit author
  strings alone establish no trust. Human or fork PRs are never auto-enabled.
- Recheck the complete exact-head lock-only diff and current required aggregate
  from the expected GitHub Actions app. Require all selected checks to have
  actually succeeded for that content; pending/unknown or stale results stop.
  The read-only aggregate itself rejects expanded Dependabot diffs on every new
  head, so an earlier auto-merge enablement cannot authorize new extra files.
- Repository auto-merge is enabled and the **current effective master rule**
  requires the expected aggregate from GitHub Actions, strict up-to-date status
  checks and linear history, with no bot/admin bypass used. Inspect actual rule
  metadata through supported read APIs. Missing, ambiguous, inaccessible or
  weakened protection is a visible refusal, never a reason to merge directly.

Then invoke native auto-merge with `--auto --squash --match-head-commit <head>`
for the fixed repository and validated PR number; never `--admin`, `--merge`, a
direct push, branch deletion or automatic approval. Squash makes one linear
lockfile update and permits a simple revert; this bot policy does not change the
workspace's initial feature integration by lead-owned fast-forward. Dependabot
authorship and GitHub's native merge identity replace A's custom commit identity.

Strict required checks prevent merging when master advances. Let Dependabot
refresh/rebase and run fresh checks; do not transplant a tested lock onto changed
source or force a merge. A new head must pass the aggregate again. GitHub's
head-match guard and branch rules cover races after metadata inspection. Pending
requirements leave the PR unmerged; metadata/API/permission failures are visible
workflow failures. No polling broker, merge queue or extra credential is needed.

### Bootstrap, package and recovery

**B1 owner: implementer0.** Own `.github/dependabot.yml`, changes to
`.github/workflows/rust.yml`, the small metadata-only auto-merge workflow, owning
Nix package/check definition, minimal benchmark/check helpers and focused tests,
and maintenance/verification documentation linked from README. No runtime or
consumer edits. Dependencies: lead accepts B; retained F remains a useful
separate logical commit. The API guard's tests should exercise its actual policy
with finite metadata fixtures: wrong author/repository/head, extra or renamed
file, missing protection, failed/skipped/pending gate all refuse; authenticated
exact green lock-only case requests squash auto-merge. No A publisher tests.

I0 completes all intended source and quick checks, locally commits and supplies
the complete 891-to-final packet including F. R0 performs affected independent
final review **before publication that starts long feature validation**. Then
run the full read-only Nix/audit/performance validation on the reviewed feature
through the existing push/manual check path. Its metadata merge workflow must
ignore feature pushes/manual runs. Record the stable aggregate name/app and
exact successful source so lead can configure protection concretely.

Current repository facts supplied by lead: auto-merge is disabled and no branch
protection/ruleset currently exists. Before routine auto-merge can be active,
lead must verify the reviewed aggregate has been emitted, integrate the initial
workflow under the separate bootstrap authority, and set/verify master required
status protection (strict), linear history, expected GitHub Actions source and
allow-auto-merge with squash available. No routine review requirement or auto-
approval step is needed. Rules must apply to the automation without bypass;
existing human integration effects must be recorded. Keep automation fail-closed
through the bootstrap window: a PR created before protection is ready remains
unmerged. Once rules/settings are proven, re-run the relevant check workflow for
an eligible PR if needed; do not weaken rules to obtain a green bootstrap.

Lead owns concrete settings approval/action and final activation evidence from
actual GitHub metadata, including event/head/base and effective protection. No
architect setting change is performed here. Unexpected platform restrictions
are reported as an activation blocker, not solved by adding credentials. The
brief is sufficient for source release; external bootstrap is a later dependency.

Failed updates stay open and unmerged for diagnosis; routine green updates merge
without human intervention. A regression discovered after merge is recovered by
reverting the lockfile squash commit through the normal checked source process
and withholding further auto-merges until understood. No force-reset or deployed
configuration change occurs. Reuse only unchanged verification within its proven
scope; green checks do not prove absence of every upstream defect. Keep bounded
artifact/temp retention and the existing disk policy.

Official evidence: [Dependabot lockfile strategy/grouping](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference),
[Dependabot auto-merge and required protection](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/automate-dependabot-with-actions),
[auto-merge prerequisites](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-auto-merge-for-pull-requests-in-your-repository),
[strict checks, check source and linear history](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches),
[workflow_run trust boundary](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_run),
[CLI auto/squash/head-match options](https://cli.github.com/manual/gh_pr_merge).

### B correction: token-compatible rule inspection

Lead accepted this boundary after verifying GitHub's permission contract. Use
one **repository branch ruleset**, `syslog-exporter-verified-updates`, targeting
exactly `refs/heads/master` with no exclusions and `enforcement: active`.
Its required-status rule includes the exact aggregate context and observed
GitHub Actions `integration_id`, with
`strict_required_status_checks_policy: true`; its other required rule is
`required_linear_history`. Lead creates/verifies it under existing administrative
authority and records its actual ID. This replaces any implication that the bot
should inspect legacy branch protection, whose GET requires Administration(read).

The metadata-only job paginates
`GET /repos/vpsfreecz/syslog-exporter/rules/branches/master`. Require both rules
from the same `ruleset_id`, `ruleset_source_type: Repository` and
`ruleset_source: vpsfreecz/syslog-exporter`, with the parameters above. This API
returns applicable active rules, excluding evaluate/disabled rules, and needs
only Metadata(read). Fetch that ID using
`GET /repos/vpsfreecz/syslog-exporter/rulesets/{id}` (also Metadata(read)) to
confirm name, source, branch target, active enforcement, exact conditions and
matching parameters. Missing, malformed or mismatched visible policy refuses
auto-merge. Other applicable rules remain enforced by GitHub; never bypass them.
No admin-only endpoint, speculative fallback, extra token or permission is added.

GitHub documents that `bypass_actors` is visible only to callers with write access
to the **ruleset**. The workflow's contents:write does not grant that authority.
Lead must set and authoritatively verify `bypass_actors: []` during bootstrap and
retain the receipt. Runtime rejects a visible nonempty bypass list; an omitted
property is documented redaction, not proof of emptiness and not itself a
failure. All other visible-policy checks remain mandatory. The workflow never
requests bypass or `--admin`. This explicitly trusts administrators who already
control the workflow/settings; runtime does not claim universal proof of hidden
bypass configuration. No broader design investigation or package is needed.

I0's actual inline-policy tests cover missing/incorrect rule source, strictness,
check app, and visible nonempty versus redacted bypass metadata. Official
contracts: [active branch rules and ruleset GET](https://docs.github.com/en/rest/repos/rules),
[legacy protection GET permissions](https://docs.github.com/en/rest/branches/branch-protection).

## C: conventional weekly lockfile updater (2026-11-12)

**Current sufficient brief, superseding A and B.** User wants a weekly/manual
custom workflow: update dependencies, test, then commit/push as github-actions
bot. A/B remain decision history only. No Dependabot, PRs, auto-merge settings,
rulesets, extra credentials, consumer pins or deployment. Master
`891db6b82ccd37e985507c654050143e165041a7` stays untouched during preparation.
Retain useful F `99ffea73005685fc9f198dda3402fe24660ee944`; replace/consolidate
unmerged B `f38277b` rather than retaining its superseded implementation stream.

Published-default references inspected without fetching or accessing other
sessions:

- [vpsf-status update-dependencies.yml](https://github.com/vpsfreecz/vpsf-status/blob/8e17ccb9728bed308bbe7d67126eb84dfdf8a81c/.github/workflows/update-dependencies.yml)
  is the closest pattern: one job, schedule/manual, non-cancelling concurrency,
  recorded starting SHA, official bot identity, no-change handling, tests and Nix
  build before an ordinary push.
- [vpsadminos daily-update.yml](https://github.com/vpsfreecz/vpsadminos/blob/eedc1254d309cac861cb0f7af080ee8de8296506/.github/workflows/daily-update.yml)
  and [flake-update.yml](https://github.com/vpsfreecz/vpsadminos/blob/eedc1254d309cac861cb0f7af080ee8de8296506/.github/workflows/flake-update.yml)
  use the same short update/commit/push shape. These inspected schedules are
  daily; C deliberately uses the user's weekly cadence.

### Smallest implementation

One `.github/workflows/update-dependencies.yml`, one `update` job on a fresh
GitHub-hosted Linux runner, weekly cron (e.g. `23 4 * * 1`, UTC),
`workflow_dispatch`, a finite timeout, and fixed concurrency group with
`cancel-in-progress: false`. Use `contents: write`; no other write permission.
Checkout the exact triggering SHA with `persist-credentials: false`, record it
as the base, and restrict real publication to this repository's default branch
`master`. Manual feature-ref runs are validation-only. A manual `dry_run` input
also permits default-ref validation without writing; normal weekly/manual runs
publish on success. No push trigger is needed for this updater.

Use the unchanged pinned Rust 1.95 environment to run `cargo update`, changing
only Cargo.lock within existing manifest constraints. Check the entire tracked
diff permits only the existing regular lockfile with unchanged mode. If unchanged,
finish successfully without a commit; ordinary scheduled runs may skip expensive
checks in that case. Explicit dry-run validation still exercises checks. No
manifest, toolchain or flake-input update, silent incompatible resolver option,
or selective fallback after a failed check.

Keep one owning Nix package/check definition: build the locked release with
`cargoLock.lockFile`, and execute the shared fmt/Clippy/full 25-test checks within
the **Nix build sandbox**, including release tests and Python runtime fixtures.
A small release-mode option to `scripts/check` is sufficient if needed to reuse
it without duplicating commands. Ordinary developer checks/hooks remain usable.
Configure and require `sandbox = true`, not relaxed; do not disable tests,
network isolation or sandboxing to make CI pass. A shell entered by `nix develop`
is not this boundary. All candidate crate build scripts, compiler plugins,
exporter binaries and test processes stay inside the derivation; do not run the
candidate or benchmark driver on the outer runner.

Outside the sandbox, only trusted pinned tooling resolves dependencies, fetches
the current RustSec database and audits the lock, and handles Git. Require a
successful fresh audit with no automatic ignores. Fetching crate data uses Nix's
normal fixed-output fetchers; compiling/running it occurs in the ordinary isolated
build. Do not pass tokens as derivation/environment inputs or mount the checkout,
runner credential locations or daemon socket into the candidate sandbox.
The reviewed workflow/Nix definition and pinned tools are trusted infrastructure;
this is conventional process isolation, not a proof against every upstream flaw.

No workflow-global shell token environment and no persisted checkout credentials.
Trusted pinned checkout/Nix installation may consume the built-in token; the
installer's token-bearing host Nix configuration remains outside the ordinary
candidate sandbox. No token, credential/config file or host credential location
may be passed or mounted into the candidate derivation. Final static Git
authentication/push is the only explicit shell-token environment, with no candidate
execution there. Diagnostics print only the sandbox setting, never complete
configuration or environment. Lead accepted this clarification; no installer
replacement, credential scrubbing or extra mechanism is needed. CI's active
pre-commit hook can be a short wrapper
invoking the **same cached sandboxed Nix check**, so committing does not invoke
the existing host-Cargo hook outside isolation or bypass its checks. Do not add a
general hook framework or change ordinary developer hook behavior for this.

After checks, confirm only the tested Cargo.lock changed. Configure both Git
author/committer as `github-actions[bot]` with
`41898282+github-actions[bot]@users.noreply.github.com`; use a fixed explanatory
message file and stage only Cargo.lock. Immediately before publishing, require
fresh remote master to equal the recorded base. Commit as its single child and
push normally without force. A stale base or push race fails visibly and waits
for a later fresh run; never rebase/merge a tested lock onto new source. No-change,
audit/build/test failure or dry-run performs no default write. Reconcile an
uncertain push by its exact commit identity instead of blindly repeating it.
GITHUB_TOKEN pushes do not start ordinary push CI, so all gates finish here first.

### Package and delivery

**C1, implementer0:** own the updater, compact flake/package/check adjustments,
normal Rust CI simplification, and short README/maintenance documentation. Remove
B's Dependabot config, auto-merge workflow, scope/maintenance helpers and policy
test framework. Restore the pre-B benchmark driver; remove the recurring
12-run/65-second acceptance campaign and its special CI dependencies. Existing
real Rust FIFO/parser/HTTP/cancellation/gzip/legacy-golden tests remain the
functional regression gate. Fresh audit plus actual Nix release/check is
sufficient for routine compatible lock updates; no production/performance
certification is claimed. Keep F and the useful package definition, not an
artifact-transfer/publisher/authorization subsystem.

Quick checks: ordinary shared checks, workflow syntax, and focused verification
of actual update shell behavior in disposable local Git: unchanged creates no
commit, failed check stops before push, changed lock is the only committed file,
and a competing default update rejects the nonforce push. Keep these finite;
no mock Git engine or restored policy suite. I0 owns implementation, quick checks,
commits and fixes; R0 owns affected final review. Lead accepts scope/history and
the main prose pass. All source, including any tiny check fixture, is committed
with quick checks **before R0 review**, then long sandboxed Nix validation.

For bootstrap, the existing read-only Rust push/manual workflow may exercise the
Nix check after review; if publishing triggers that long check, publish only
after local committed review. A new updater's manual dispatch need not work
before it exists on default: use the same commands locally after review and the
existing workflow for feature validation. After initial authorized integration,
its explicit dry-run proves orchestration without writing master. Do not add a
temporary privileged trigger or extra workflow just for bootstrap.

Initial source integration remains a separate lead/user gate; future routine
bot commits are user-directed. No repository setting change is needed. Record
exact source/lock/Nix identities and concise results; retain original B reports
as historical evidence only. Failed updates leave default unchanged unless a
push already succeeded, which must be reported honestly. A later bad lock is
recovered by a checked revert, never a forced history reset; deployed configuration
is unaffected. Reuse one owned target/temp area and keep the existing disk policy.

No unresolved design choice blocks C1. Actual sandboxed check execution and
normal hook behavior are implementation evidence gates; if isolation cannot be
preserved, stop that path and report the concrete limitation before adding jobs
or credentials. Pin maintained action SHAs using official upstream verification.
References for the boundary: [Nix sandbox](https://nix.dev/manual/nix/2.28/command-ref/conf-file#conf-sandbox),
[Nix Rust packaging](https://nixos.org/manual/nixpkgs/stable/#rust),
[checkout credential/bot guidance](https://github.com/actions/checkout).
