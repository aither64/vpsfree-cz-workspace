# Exporter implementation evidence and review packet

Packages I/I2, implementer0. I2 ready for affected independent final review;
no deployment, dry activation or default-branch integration is authorized.
Scope authority: accepted [design](design.md), [Ruby contract](ruby-contract.md),
[consumer integration evidence](configuration-integration.md), and lead's I
assignment. The user explicitly requires stopping before deployment.

## Exact source and series

- Repository: `repos/syslog-exporter.git`, target `origin/master`.
- Worktree: `worktrees/2026-11-10-rust-syslog-exporter/syslog-exporter`.
- Feature branch: `2026-11-10-rust-syslog-exporter`.
- Fresh base: `7c5a8e74e44a704cceb99cd05716af6800d78efd`.
- Current I2 final head: `faf06c1185ad2f6d39286d2e33896a6455b7bea6`.
- Prior fixed and locally verified I head: `8ef8241c60f3b99976191b92f0467c945e36b1c8` (historical V/Nix artifact only).
- Original independently reviewed range: `7c5a8e74e44a704cceb99cd05716af6800d78efd..9a5b3d1c5a970d7bdc8c4771f0c24f3d9ec2b052`; preserve [review report](exporter-final-review.md) unchanged.
- Complete series: that one commit, “Replace Ruby exporter with ordered Rust
  FIFO processing.” Inspect `git log BASE..HEAD` and `git diff BASE HEAD`.
- Cargo version `0.14.0`, Rust `1.95.0`, edition 2024. Cargo.lock SHA256:
  `031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e`.

The first published candidate `3372f218f5d6ced94bfa5e732c5b8ede320b19c4`
was amended before review solely to distinguish requested records from completed
unique sequence submissions in driver receipts. `git range-diff` proves the
change is two receipt bookkeeping lines; runtime and fixture bytes are identical.
No C2 pin, independent review, deployment or supported consumer used that old
candidate. It is superseded by the one final functional commit above; this is
not a claim that the two complete trees are equal.

There are **no migrations**, no persisted application format, no schema and no
intermediate feature version merged, released, deployed or externally consumed.
The branch directly introduces the final replacement; there are no superseded
approaches, fixup commits, compatibility shims or repeated pin-update streams.
Cargo.lock is the one final dependency graph, not repeated dependency bumps.
Ruby source/tooling removal, runtime, Cargo/toolchain, supporting tests/fixtures,
hooks/CI and explanatory docs are bundled because the replacement must build,
preserve its wire contract and pass the newly active checks as one change.
The finite driver is included before review so V will not add unreviewed test
infrastructure after the final review. No configuration-consumer edits are in
this branch; C2 owns its independently reviewable package and exact source pin.

## I2: supported two-consumer HTTP admission

Lead accepted architect D2 after canonical config proved two independently
scheduled Prometheus consumers, mon1 and mon2, and V observed7 HTTP503 responses
among40 normal overlapping requests on8ef. V is parked; old throughput evidence
is scoped to that old artifact and does not certify this successor binary.

Current complete series is one coherent amended replacement commit:
`7c5a8e74e44a704cceb99cd05716af6800d78efd..faf06c1185ad2f6d39286d2e33896a6455b7bea6`.
Preserve the unchanged original reviewed7c5..9a5 report and the prior8ef fix
history above. C2's published75b/old4gb package were local development/verification
only; no supported production deployment consumed these feature candidates.
The future consumer pin is C2-owned and will be consolidated to this reviewed
successor; no source lineage is claimed literally merged.

Only `src/http.rs`, `docs/reference.md`, and `docs/verification.md` differ from8ef.
The private production state constructor admits at most two metrics handlers,
including separate HTTP/2 streams. One encoder remains active; the other request
waits asynchronously up to one second. Excess admission or wait expiry receives
503. Both owned permits move into blocking encoding and survive HTTP future
cancellation until the actual job ends; they release before response writes.
The32-connection/30s lifetime, gzip/fallback, metric names/labels/timers, FIFO,
parser/collector/config/routing and benchmark behavior are unchanged. No cache,
new worker pool, dependency, public test hook, config knob or persistence.

Five deterministic private HTTP tests hold/release a real registry collector:

- Both admitted overlapping requests return valid200 exposition, third gets503,
  and peak concurrent encodes is one.
- Second response completes while the first response body remains unread,
  proving permits release before body consumption/network writes.
- A blocked encoder causes the waiter to expire after one second; admission
  recovers and a later request succeeds.
- Cancelling a waiter returns admission; cancelling a running HTTP future keeps
  both limits owned by the continuing blocking encode, then recovers after exit.
- Dropping the sole test-gate sender unblocks the collector and returns permits;
  assertion unwind uses that same drop path, so failed tests do not strand a
  blocking worker/runtime. The fixture is test-private, not a production hook.

Initial fresh-target full checks passed18tests in94s. A small private constructor
then removed duplicated production/test limit construction, and an explicit
fixture-failure cleanup assertion was added. Focused final HTTP tests5/5 passed
in1.01s; complete scoped active commit hook passed fmt, Clippy and **19 tests**
(6library,7contracts,6runtime). No failure/rerun loop occurred. Toolchain paths
had been reclaimed since earlier work; the formatter shell re-substituted exact
1.95 toolchain from cache before checks, with no local release build.
Logs: `logs/i2-quick.log`, `i2-focused.log`, `i2-commit-hook.log`.

Whole old-to-new evidence: `logs/i2-from-8ef.patch`, `i2-range-diff.log`.
Exact byte/blob/SHA proofs are `logs/i2-equivalence.json`. Old overall src tree
`1362270280553d1978986649adc54e4231c9666e` becomes
`f563642a228e19e368b7f3b7ad638ef866f0bc89` solely because HTTP changed; do not call
complete source trees equivalent. Unchanged source blob identities:

| File | Unchanged blob |
| --- | --- |
| parser.rs | `749949e1dcec0e81c48bea63a14f10dff6dc908a` |
| input.rs | `d081792839990b7dfe4f96f063e079c76405475b` |
| collectors.rs | `452c53b14ed5e59acf3977b9c77ab4992bea5bad` |
| metrics.rs | `76d0f7fadc921e3b35930e721c2f94f91565ad0d` |
| main.rs | `7b2c052555ed8e2785a5d82788af31b5d908a6a2` |
| config.rs | `554910324c958ff9f2d571a5fa9e6b8eb7c8c886` |
| lib.rs | `4866e2609c8fd350c6732355242315d39235aa7f` |

Manifest SHA256 remains `790f0f4925d8de2f682f007330788cf1361c6f22fe425b28cb013c2aabac003f`;
lock `031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e`;
toolchain `7d21c66a15f41bad66b82ed06a289f5dc8a6e3751951d2696bbf20ce296f2b0f`;
shell `3b7c05358de0992b3783d1b6732efc14a902db4a0752a2049aed5358339b7540`.
Benchmark and all existing contracts/runtime fixture tests are byte-identical;
all117 audited package versions and release-profile inputs remain unchanged.
New HTTP blob `caccd3419f676b528cb88971c7dcf04df01b3ded`, SHA256
`65fe9a455a096d5dad249eeebb0031241092fb40058d8afd0864dcb57c9cd7c9`.

The main lead directly reviewed the new HTTP paragraphs/error strings before
commit. Reference owns admission/cancellation/HTTP2 behavior; verification page
owns deterministic-check guidance. Existing prose/commands/pins/data-loss and
rollback caveats remain preserved. No migration, transitional schema, obsolete
feature commit, repeated dependency stream or merged-history rewrite is added.

Affected final review requested through lead: same reviewer0, general,
architecture/repetition and risk/compatibility lanes, with whole-series/history
and documentation conclusions; overall scope remains the accepted replacement.
C2 pin/build and final focused V remain blocked on that review and explicit
release. No long V/Nix package build, production access, deployment, dry
activation, default integration, claim or lifecycle action ran in I2.
One373MiB debug target was recreated only for necessary checks/review; latest
filesystem95GiB free. No duplicate Cargo release target. Keep it while current
review/reruns need it, then remove only the owned target under the existing rule.

## Current I2 publication and CI

SSH remote proof binds `faf06c1185ad2f6d39286d2e33896a6455b7bea6` to the
feature branch. Own worktree/index are clean. Current exact-head Rust CI
[42921690945](https://github.com/vpsfreecz/syslog-exporter/actions/runs/42921690945),
attempt1, completed **success** on `faf06c1185ad2f6d39286d2e33896a6455b7bea6`.
A fresh Luna/low watcher verified metadata/watch exit0 and joined all tool calls;
`logs/ci-42921690945.{log,json}` preserve the exact receipt. No known running
I2 command or utility cell/session remains. All superseded branch runs were already completed
successfully; no superseded queued/running workflow required cancellation.
Current run must be retained. No default-branch push occurred.

## Prior I publication and CI (historical)

SSH `git ls-remote origin refs/heads/2026-11-10-rust-syslog-exporter`
proved the historical I head `8ef8241c60f3b99976191b92f0467c945e36b1c8`.
Own worktree/index are clean; shared hooksPath override is absent.
The original candidate's Rust workflow
[42908282402](https://github.com/vpsfreecz/syslog-exporter/actions/runs/42908282402)
completed successfully, so no superseded queued/in-progress run required
cancellation. The independently reviewed head's Rust run was
[42908713683](https://github.com/vpsfreecz/syslog-exporter/actions/runs/42908713683),
attempt 1, **completed successfully** on reviewed head `9a5b3d1`. A fresh Luna/low
watcher verified run/head/attempt and joined all tool sessions; complete log is
`logs/ci-42908713683.log`. This CI run repeats quick checks, not post-review V.

Final fixed-head CI is
[42910934231](https://github.com/vpsfreecz/syslog-exporter/actions/runs/42910934231),
attempt 1, exact `8ef8241c60f3b99976191b92f0467c945e36b1c8`, **completed
successfully**. A fresh Luna/low watcher verified run/head/attempt/conclusion and
joined all tool sessions; log `logs/ci-42910934231.log`. Both superseded runs were
already completed successfully, so there was no eligible queued/in-progress
superseded run to cancel. The current run is retained.

## Narrow review fixes and direct verification

Reviewer0's unchanged original report found no Blocking/runtime defects, one
Important driver deadline defect (I1) and one Advisory HTTP-fixture coverage gap
(A1). Lead authorized these narrow fixes and direct verification without a new
whole-branch review; no new design or runtime contract was introduced.

- I1: cap rate-pacing sleep at remaining deadline and raise the existing timeout
  before another record is sent once exhausted. No scheduler/helper framework.
  Focused real regression runs two requested records at 0.001/s with a one-second
  deadline, submits exactly one, then exits through normal finally cleanup. It
  passed in 1.36s: candidate exit 0, no forced kill and closed listener; driver
  exit 1 reports the intentional timeout. A bounded test process-group cleanup
  protects failure cases from leaking fixture children.
- A1: small in-memory middleware assertions consume `http.json` for fallback
  status/content-type/body, ordinary metrics type and gzip negotiation/type/Vary.
  Decoded gzip bytes equal the plain metrics response. Test-only `flate2` and
  `tower` are now direct dev dependencies; both were already in the audited lock.
  No resolved crate version changed, and no runtime HTTP implementation changed.
  The reference explicitly excludes tiny fallback incidental compression/Vary
  header differences; lead applied the wording pass before commit.
- Full active scoped pre-commit hook passed formatting, Clippy and all 14 tests.
  Focused evidence: `logs/review-focused.log`; complete hook evidence:
  `logs/review-fixes-hook.log`.
- Full `git range-diff` between the reviewed and fixed ranges is retained in
  `logs/review-fixes-range-diff.log`, with exact old-to-new patch in
  `logs/review-fixes-diff.patch`. Only Cargo root dev-dependency entries,
  the driver pacing block, HTTP reference clarification and two regression
  tests differ. Both `9a5b3d1:src` and `8ef8241:src` equal
  `1362270280553d1978986649adc54e4231c9666e`. Runtime source trees are identical;
  the complete trees are intentionally different. The current feature history
  still consists of one final functional commit, with fixes folded into it and
  no migrations/transitional history.
- Previous Cargo.lock SHA256 at reviewed head was
  `e49e3f6163856a6c29d0fb6a7fca835d1d41539cbda0b58fe95b2417ff92f2a8`;
  final SHA256 is `031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e`.
  C2 must select the new exact source/vendor identity. No tracked consumer pin
  or deployment is claimed to have used the reviewed intermediate head.

## Delivered behavior and boundaries

All Ruby runtime/gem/RSpec/Overcommit/RuboCop artifacts are removed. The Rust
executable preserves all 18 legacy families (5 counters, 13 gauges), literal
names/HELP/types, aliases/FQDNs, dynamic labels, initial zeros, metadata-only
families, retained zero series, host gates and detector order. Real middleware
goldens cover all detectors and optional WebUI behavior, nil namespace, escaped
Unicode labels, startup, triggers and expiry. Counter names gain no `_total`.

One dedicated ingestion thread owns nonblocking FIFO framing, indexed host
routing, cached metric handles and monotonic flare deadlines. There is no
application message queue. Framing is bounded to configurable 1 MiB including LF;
dynamic series remain retained and can grow with cardinality. HTTP uses Axum/
Tokio/Hyper with one encoding job, 32 active connections and a 30-second complete
connection lifetime; response encoding/writes do not run on ingestion.

JSON/CLI: `--config PATH --listen ADDRESS:PORT`, env config fallback, sample
fallback, `--help`, `--version`, `--check-config`. No live reload, daemonization,
Puma compatibility CLI, systemd notify/watchdog or new persisted state.

Deliberate accepted fixes: process a complete first record; reject malformed
headers/timestamps/UTF-8 and continue; safely handle kernel PID/forwarded forms;
use monotonic ordered expiry; bound oversized records and reset partial framing
on EOF; tolerate refused pipe enlargement while exposing actual capacity.
Missing required program fields are rejected rather than manufacturing a generic
Ruby Message. Arbitrary broader Ruby ISO8601 variants are not claimed: pinned
producer RFC3339 forms define the required timestamp subset.

No producer queue/retry/buffer policy change, new protocol, durable broker,
pluggable collector framework, production traffic observation, deployment or
integration occurred. Rsyslog can lose or splice records before the reader; a
parseable truncated concatenation cannot be detected reliably by this protocol.
No throughput, production-envelope or end-to-end losslessness claim is made.

## Captured baselines and input identities

Before Ruby deletion, real `SyslogExporter::Rackup.app` middleware was invoked
with Rack::MockRequest. Processor.start was intercepted to retain startup state
without starting threads; actual parser/collectors/registry and expiry method ran.
No fake Prometheus registry was used. Inputs/outputs and exact provenance live
in `tests/fixtures/{config.json,events.log,startup.prom,triggered.prom,expired.prom,http.json,README.md}`.
The temporary capture script remains in
`/tmp/2026-11-10-rust-syslog-exporter-i/capture.rb` for review reproducibility,
and is not shipped with the Rust application.

- Ruby source: `7c5a8e74e44a704cceb99cd05716af6800d78efd`, version 0.13.4.
- Ruby baseline package:
  `/nix/store/w7g32wplgls6x79608h6nij02a4vvq9y-syslog-exporter`.
- Derivation:
  `/nix/store/hzv5vgrxq9iz7kl4brm8w8k0bbikwrbf-syslog-exporter.drv`.
- C2 proved it in the exact log-host baseline derivation graph
  `/nix/store/nwb1jw34jy539z5hgbx4cwr3v5pn10kp-nixos-system-log-26.05.20261026.718f670.drv`.
- Ruby 3.4.9, Puma 8.0.2, Rack 3.2.7, prometheus-client 4.2.5, Bundler 2.7.2.
- Consumer stable nixpkgs `718f670e845328e9c2cecdd832835712b2cbd065`, local
  source `/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source`.
- Pinned producer:
  `/nix/store/g0g8nvq928bgl2dwvvddh99l0543s9cx-rsyslog-8.2610.0/bin/rsyslogd`,
  upstream tarball hash `sha256-e9+V6B6mwO5dWGNC1X0qbjlbCJ+zxnMYoNxVWBbeQEs=`.

C2's later lead-authorized read-only inventory additionally confirmed the actual
running Ruby package and rsyslog paths are identical to these baseline closures;
stateDir is empty and normal FIFO/ownership are intact. Full deployed configuration
revision remains unknown; see c2-evidence.md. This package performed no production
access and did not infer activation authorization from that inventory.

The registered finite producer fixture captured actual TCP → file → ompipe bytes
in `producer-{input,output}.log`: RFC3339, host, normalized app/PID tag, body, LF;
tab became `#011`, Unicode high bytes survived. Small records establish framing,
not a maximum-size or overload guarantee. Local imuxsock is a distinct shape:
legacy local input retains a program colon and uses producer local time. The
driver deliberately preserves this rather than changing the exporter parser.

## Quick checks and corrections

All Rust commands used the pinned Nix shell with one explicit target:

```sh
nix-shell -I nixpkgs=/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source \
  --run 'export CARGO_TARGET_DIR=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-10-rust-syslog-exporter/cargo-target; scripts/check'
```

`scripts/check`: Python driver syntax/help, rustfmt check, Clippy all targets with
warnings denied, and locked tests. Final suite after review fixes: **14 tests pass** (one parser,
seven contract/timer tests, six runtime/CLI/HTTP/driver tests). The real FIFO test forces a
capacity-request refusal and proves fallback, split/coalesced first records,
oversize/malformed recovery, incomplete EOF, reopen and orderly shutdown. HTTP
test keeps slow incomplete-header clients open while ingestion updates counters.
The finite driver separately verifies real binary SIGTERM completion.

Initial compilation passed. The first lint run found two collapsible-if cases;
they were fixed before tests. The first runtime run found an EOF descriptor
lifetime defect: the reader retained its descriptor during backoff, permitting
a writer to enqueue bytes that were dropped on close. The descriptor now closes
before backoff; the focused regression and full suite passed. No timeout was
treated as proof of correctness or hidden by unmodified reruns.

Fresh Luna/low watchers launched uncertain dependency fetch, initial compilation,
first complete check batches and advisory auditing. Terminal tool sessions were
joined/reconciled. Later known-fast focused/full checks and the final active
pre-commit hook ran inline. Audit setup initially lacked Cargo; one corrected
shell fixed it. Final `cargo audit --file Cargo.lock` passed for 117 packages,
with no reported vulnerabilities. Metadata inspection found no unknown licenses
or declared MSRV above 1.95. This is current advisory evidence, not a security
guarantee. Upstream Actions checkout v7.0.1 was verified via official repository
refs and pinned to `3d3c42e5aac5ba805825da76410c181273ba90b1`.

Raw logs (local, disposable): `logs/{rust-fetch,initial-check,quick-tests-1,quick-tests-2,fifo-focused,quick-tests-final,quick-final-driver,commit-hook,final-amend-hook,ruby-capture,dependency-audit,dependency-audit-2}.log`,
plus `logs/cargo-metadata.json`. Retain compact evidence when raw output is removed.

## Driver smoke evidence and remaining performance work

`scripts/benchmark.py` is one finite stdlib driver, with the same seeded corpus,
host map and result model for direct FIFO, pinned-rsyslog TCP/UDP and private local
socket paths. It supports ordinary/OOM/mixed shapes, controlled rate/cardinality,
repeated bursts, optional whole-exporter SIGSTOP pause, independent archive unique
sequence/duplicate counts, final marker/count deltas, RSS/CPU/scrape sampling and
bounded owned-child shutdown. It exposes unavailable producer/FIFO/exporter unique
sequence stages explicitly and never installs a competing reader or tee.

Functional smoke results, **not performance measurements**:

| Mode | Submitted records | Exporter count delta | Unique archived sequences | Duplicates | Result |
| --- | --- | --- | --- | --- | --- |
| Direct OOM, burst/pause | 32 | 32 | Unavailable | Unavailable | Passed, exit 0 |
| TCP ordinary, burst/pause | 32 | 32 | 32 | 0 | Passed, both children exit 0 |
| UDP ordinary, rate 100/s | 16 | 16 | 16 | 0 | Passed, both children exit 0 |
| Local mixed, rate 100/s | 16 | 16 | 16 | 0 | Passed, both children exit 0 |

First local smoke used RFC5424 on imuxsock and timed out because the local parser
treated `1` as its program. Source/diagnostic evidence identified the fixture
mismatch; local mode now sends the local legacy shape and waits for colon-bearing
marker labels. The original failure/metrics and corrected receipt remain under
`logs/driver-local-{smoke,corrected-smoke}.*`. Other receipts are
`logs/driver-{tcp,udp,direct-final}-smoke.*`. JSON contains exact argv, capacities,
stage gaps and bounded archive previews. Raw throughput numbers from these tiny
debug runs must not be presented as capacity estimates.

All registered fixture commands finished: service registry distinguishes `exited`
for successful smokes and `failed` for the old local smoke; neither state is an
active process. The failed attempt reaped both children and retained diagnostics.
No lifecycle cleanup/retirement operation was invoked.

Post-review V remains required: matched release Ruby/Rust runs on isolated equal
resources, three matched repeats, baseline-boundary sustained/burst OOM/ordinary
traffic, high cardinality, scrape/RSS trends, pinned producer saturation, reader
and producer restart/partial-write scenarios and complete observed-stage loss
accounting. Promtool was not available in ambient/store tools during this package;
actual golden parity passed, but separate promtool validation remains a gap.
Neither C2's package/system build nor live generation/stateDir inspection is
claimed here. No production machine reservation exists.

## Hook safety and storage

Own commits use an explicit active command-scoped hook path:

```sh
git -c core.hooksPath=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-10-rust-syslog-exporter/syslog-exporter/.githooks commit -F /path/to/message
```

Both the initial commit hook and final amended-commit hook ran all quick checks and passed. An early `git config --local
core.hooksPath .githooks` mistakenly affected the bare repository's shared config.
It was promptly corrected by verifying/removing only that introduced value;
canonical effective hooksPath is now absent, `core.bare=true` and no worktreeConfig
extension was added. Existing common Overcommit pre-commit remained unchanged:
SHA256 `a81910ebf3fd7a535b81cc3497d14bbed38190d6e2a6473ee71f04634c516cc5`.
The initial pre-set key was not captured, so absence of an overwritten older
custom value cannot be independently certified. This uncertainty was reported
to the lead; no peer worktree was accessed. README now distinguishes standalone
clone setup from command-scoped linked-worktree hooks. No hooks were bypassed.

Filesystem headroom: 100 GiB before this package; latest 99 GiB (shared activity
also affects this value). One owned Cargo target is 403 MiB, reduced-debug and
nonincremental. It remains needed for review/reruns and later compatible checks;
remove obsolete owned build profiles once those dependencies end. Temporary driver
roots were removed by finite fixtures after reaping their owned processes and
preserving result receipts. No broad cleanup, Nix GC or peer-data deletion ran.

## Review scope, docs and next dependency

Risk is high because FIFO parsing/loss behavior, metric public contracts,
cross-project packaging/service replacement, restart and rollback matter.
Recommended lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Lead owns reviewer eligibility/settings, packet acceptance
and invocation; retained reviewer0 is configured Sol/xhigh, to be reverified by
the lead. Require explicit complete-series, no-migration and documentation
placement/fidelity conclusions. This record is evidence, not self-review approval.

| Topic | Reader / class | Authoritative location | Evidence / limit |
| --- | --- | --- | --- |
| Build/start/hooks | Maintainer, how-to entry point | Exporter README.md | CLI/config tests, pinned Nix checks, hook log |
| JSON/protocol/metrics/timers/delivery | Developer/operator, reference | Exporter docs/reference.md | Captured goldens, deterministic and FIFO/HTTP tests; upstream loss remains bounded only by future measurements |
| Test/performance procedure | Maintainer, how-to | Exporter docs/verification.md | Four transport smoke modes; long acceptance still V |
| Oracle provenance | Developer, fixture reference | Exporter tests/fixtures/README.md | Exact pinned baseline and real captured data |
| Concrete site deployment/rollback | Operator, reusable operations | C2-owned configuration documentation | C2 final pin/build/review pending; no activation authorization |
| Exact current heads/results | Lead/reviewer, individual execution | This record and existing plan/state | No live-deployment claims |

The lead directly applied the user-facing writing skill to the settled prose,
CLI help and errors, then to the linked-worktree and transport/pause additions.
No required recovery instruction or existing public anchor was removed: the old
README only described named-pipe input. Relevant links are local repository paths.

Next: lead accepts I and invokes independent final exporter review. C2 must pin
the exact **reviewed** published exporter head before its own final review/build.
V starts only after I/C2 checks and required final reviews. I retains ownership
of review findings; no new independent package has been accepted implicitly.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/
