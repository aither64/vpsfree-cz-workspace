# Exporter implementation evidence and review packet

## Current C1 delivery

**Published `b9b9cfea4331ff28bd883f1ed7415af6f27cd5f7`, tree
`a1d826ecdbf019600ee63f74e74c385b00902a7c`; checks complete, ready for lead
acceptance and awaiting initial merge approval.** Root accepted the original
RC review and both narrow corrections. Exact-head Rust run
[43216044595/attempt 1](https://github.com/vpsfreecz/syslog-exporter/actions/runs/43216044595)
succeeded, including actual sandboxed release compilation and the shared
9 shell/Git fixtures, 25 Rust tests, rustfmt and Clippy. Effective configuration
was `sandbox=true` and `sandbox-fallback=false`.

The worktree is clean. Complete `891..b9b9` contains F99ff and one coherent C
commit; there are no migrations, application runtime or Cargo.lock changes. The failed a455
run and original reviews remain intact. All known command and watcher effects
have joined. The dedicated Cargo target was removed after exact ownership and
accessible-reference checks; 391,041,024 allocated bytes were removed and absence
verified. Protected unrelated process metadata remained unavailable; this is
not a claim of universal process visibility.

Compact final receipts: [hosted validation](logs/c-hosted-validation.json),
[effects and cleanup](logs/c-final-effects.json), and
[source provenance](logs/c-source-provenance.json). This validates read-only
feature CI, not an actual weekly update, fresh audit, bot commit or authenticated
updater push. Initial integration and a subsequent default-branch updater dry
run remain lead-owned future gates. No default, settings, consumer, production,
recovery-root or lifecycle mutation occurred. Earlier held/running statements
below are historical checkpoints.

## Current C1 check-entry packaging correction

**Local b9b9cfea/tree a1d826ec; publication held for root narrow binding.**
First actual a455 Nix run failed at scripts/check shebang after release compile,
before9/25 ran; exactfailure retained, no green/leak claim. One-word package fix
invokes existing stdenvBash explicitly. Other code/message/modes/Fparent identical.
Focused Bash syntax/declaredcheckPhase proof and mandatoryhook9+25 passed; all
effectsjoined. New helper entrypoints statically use sys.executable or resolved
Bash, not /usr/bin/env. Details c-shebang-proof.json and final section.

## Current C1 hosted validation

**Final a455/tree f819 published; actual read-only Nix feature CI is running.**
Root closedRC-I1 by direct narrowbinding (c-lead-narrow-fix.json). Exact-lease
SSH feature push replaced oldBf382, defaultmaster891 unchanged; comparison
891..a455 captured. Rust43214738861/attempt1 exacta455 singlejobcheck is
observed by fresh Luna/low c_hosted_release with fullraw/effect capture.
No success claim until actual sandboxtrue/fallbackfalse and full sharedNix
checks succeed. No oldBperformance/localrelease/realCargo.lockupdate or
authenticatedupdaterpush was run. Updaterdefaultdryrun requires later
initialintegration. Currentrun/observer are accountedfor; source remainsfixed.
Older unpublished-phase statements below are chronological receipts.

## Current C1 RC-I1 remediation

**Local final `a4554a93723abd65007a5dff174db63cbecc1245`, tree `f81944cebcb80c1d1d524b7fcb29534e6e736564`;
publication held for root's direct narrow binding.** RC accepted all original
0b313 lanes/history/docs/no migrations subject only to fail-closed sandbox
fallback. Exact4-path fix and tests are logs/c-rc-i1-proof.json plus exactpatch/
range-diff. Both installers set sandboxtrue/fallbackfalse, onlytwo nonsecret
settings are checked/reported, and all primary/CIhook builds explicitly disable
fallback. Nine finite fixtures+25Rust passed finalactivehook. No actualhosted
leak/failure or unsupported-kernel experiment is claimed. Older C/B receipts
below remain historical; original0b313 reviewedsource/report retained.

## Current C1 disposition

**C1 locally committed and ready for lead-invoked R0 review; NOT PUBLISHED.**
Current source `0b3131ffa6a2855cfa15c42de778d4bf794b4510`, tree
`f5d1659fdd8a31b44a80a1a06ed1657b9d7f16f3`, exact F99ff parent. C replaces the rejected
unmerged B approach; complete891..C is useful F plus one coherent C commit.
B keeprefs/reports/rawCI evidence remain historical and intact. Developer
quick checks and final mandatory hook passed8actualshell/Git fixtures+25Rust.
Actual sandboxed release and new feature validation await review; no pre-review
release build/audit/update or publication/default/settings/production action.
Full current receipt logs/c-source-provenance.json and C section at the end.

## Superseded B disposition and previous evidence

## Current B1 disposition

**B1 full reviewed feature validation complete; ready for lead acceptance.**
Published source`f38277bb96ee2814b6fd7179fdc5facf0e609e5b`, tree
`096e00e6c79956660e1a5c43874cd9909614f90b`; complete891..head is F99ff+B.
RB/RB-A1 binding accepted, focused/full/mandatory hooks passed. Exact hosted
Rust43200250554/attempt1 has all four selected jobs successful, including actual
maintenance and Rust required. Final results and limits are at the end; exact
logs/b-hosted-validation.json and b-final-validation-effects.json are the
compact receipts. No source/check/finding or active command remains. The own
Cargo target was removed at the approved no-rerun boundary. Settings bootstrap,
any live Dependabot auto-merge and initial default integration remain lead-owned
and have not been performed by I0. The session remains open.

## Historical implementation and previous phases

Packages I/I2 accepted; M message-only successor, implementer0.
Exact current-head CI/effect receipt follows below;
M authorizes no production action by implementer0. Deployment approval and
execution are lead-owned. The user later approved integration of exporter and
configuration into remote master; the current I0 package prepares only, with
merge/claim/push/release owned by lead.
Scope authority: accepted [design](design.md), [Ruby contract](ruby-contract.md),
[consumer integration evidence](configuration-integration.md), and lead's I
assignment. Original I/I2 authorization stopped before deployment; the later
user approval for log.int activation is lead-owned and does not permit merging.

## Exact source and series

Current I3 committed/published head: `891db6b82ccd37e985507c654050143e165041a7`;
tree `4b28b6924e042ebf7582b9a0a91eea0bbbddc429`. Local25tests/fmt/Clippy/
activehook and currentCI43116296064/attempt1 passed. R3 disposition pending;
no Nix release build, long replay or production action for this successor.

- Repository: `repos/syslog-exporter.git`, target `origin/master`.
- Worktree: `worktrees/2026-11-10-rust-syslog-exporter/syslog-exporter`.
- Feature branch: `2026-11-10-rust-syslog-exporter`.
- Fresh base: `7c5a8e74e44a704cceb99cd05716af6800d78efd`.
- Prior deployed/message-only head: `6ecada0a9d2f6457a11031a3a4ffc341584fb29c` (retained; substantive I3 successor below).
- Prior I2 reviewed/measured head: `faf06c1185ad2f6d39286d2e33896a6455b7bea6` (complete tree identical).
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


## M: measured comparison in commit message

Lead dispatched a user-requested message-only amendment after V acceptance.
Capacity was confirmed with V quiescent. Preserve the complete original commit
body and append the lead-written two-paragraph measurement summary verbatim,
wrapped within80columns. No exporter source, docs, tests, fixture, driver,
dependency, profile or hook edit is authorized. This record and compact logs
are evidence only. Base7c5 and full tree5d3e must remain exact; one replacement
commit/no migrations. Source stillfaf pending active hook and amendment.

`logs/m-before.json`, `m-old-message.txt`, `m-old-commit.txt` and
`m-old-series.txt` preserve old identities/message/complete range. The single
owned debug target was absent after V, so the mandatory declared pre-commit
fullcheck requires one disposable debug rebuild. Fresh Luna/low native watcher
`m_hook_preflight` owns that Nix-shell fmt/Clippy/19test preflight, with reduced
debug and no incremental output. Parent will amend with the same active
command-scoped hook after the cache is warm, publish with exact old-head lease,
prove full tree/range equivalence and notify C2 for mechanical pin handling.
No duplicate Rust release/Nix application build or benchmark is part of M.


M publication: `6ecada0a9d2f6457a11031a3a4ffc341584fb29c`, complete tree
`5d3e6ed8aba81c5b43c34f92b13a5b604d24c478`, exactly equal to priorfaf.
Base remains7c5, one commit, no migrations. `m-old-new.patch` is empty;
`m-range-diff.log` shows only the appended approved message. Raw prior/new commit
objects/messages and complete old/new ranges are preserved. Every original
message byte is a prefix, followed only by the lead's verbatim measurement
paragraphs; line lengths<=80. Manifest/lock/toolchain/shell/driver/source hashes
remain exact. No source/docs/tests/dependency/profile/hook changed.

Fresh hook preflight passed in about215s using one owned reduced-debug target;
actual command-scoped active amend hook passed in7.85s with fmt, Clippy and all19
tests. Logs are `m-hook-preflight.log` and `m-amend.log`. Common hooks/config
were preserved. SSH push used exact oldfaf lease; fresh remote proof shows
feature6ecada0 and unchanged master7c5, in `m-remote-heads.txt`. I1 received the
exact published head/tree for mechanical source pin handling; no source hash was
guessed and no release/Nix application rebuild was performed here.

Lead independently reconstructed the complete old tree in an isolated native
index, proving current-tree equality/base/single-commit/clean state and review
reuse without another whole review: `logs/m-lead-reconstruction.json`. Original
independent reports remain untouched. Prior3hk binary/V evidence applies to the
identical complete source/dependency/profile tree, with its original exact Nix
source/output identities preserved; C2 owns successor pin/input/output provenance.
Current exact-head Rust CI is43096574664/attempt1, owned by fresh native watcher
`m_current_ci`; final result/effects will be appended here. No superseded run was
queued or running; all earlier branch runs had already completed successfully.


M cleanup boundary was explicitly revised by lead: a queued remote CI run does
not require the local Cargo cache. After owner/realpath/non-symlink/Cargo-marker
checks and an exact process-reference scan (615 owned-UID processes; zero
references or unreadable owned processes), removed only the session-owned target:
390,914,048 allocated bytes / 384,313,103 apparent bytes; absence verified.
`logs/m-target-cleanup.json` and `m-equivalence.json` preserve actual values.
The first short report misstated counts/bytes before inspecting tool output; a
prompt correction supplied the actual receipt values. No other cleanup occurred.
Current exact-head CI remains pending; observer83998 is uninterrupted, with no
new run, timeout or cancellation. No local build/test/candidate remains.


## Approved exporter integration preparation

M source execution is explicitly parked on external CI; observer83998 and
finding ownership are retained. Capacity was confirmed before this bounded
preparation package. Lead relays user approval “okay then, merge it” for exporter
and configuration remote master, superseding the preceding keep-unmerged period.
No source fix/refresh was requested or made. This package acquired no claim and
performed no merge, default push, deployment or machine release.

Fresh origin fetch still gives master7c5 and feature6ecada0. Source is clean,
one commit with parent7c5, complete tree5d3e. Original whole-series/no-migration
reviews, accepted I2 review, M independent reconstruction and unchanged input/
profile/lock/source proofs apply. Active M hook already passed all19 tests,
fmt and Clippy; Nix19 release checks and exact3hk evidence are retained. No
unnecessary Cargo/application/release compile was run for preparation.

Prepared clean detached target:
`worktrees/2026-11-10-rust-syslog-exporter/syslog-exporter-merge-target`, HEAD7c5
from fresh origin/master; ff to6ecada0 is possible. Creation used the active
command-scoped approved source `.githooks` path, not a shared config edit. The
common Overcommit hook/config remain unchanged. Every critical Git invocation
must use `-c core.hooksPath=/absolute/source/.githooks`. Git fast-forward creates
no commit, so the declared pre-commit hook is active but Git does not invoke it;
the exact accepted M full-hook result is reused without bypass flags.

Current source `shell.nix`/pinned Nixpkgs env was realized and verified: Rust/Cargo
1.95.0, command-line hook origin/path correct, execsession90068 exited0 and joined.
Nine toolchain cache paths were fetched (11.4MiB download/2.2GiB unpacked), with
no source compile or explicit GC root. Enter this shell **before** acquiring the
claim and keep it alive across lead's critical Git section. Exact source/target/
remote refs, selected hook hash, input reuse and lead-only commands are in
`logs/exporter-integration-preparation.json`; complete series in
`exporter-integration-series.txt`. Portal comparison captured7c5..6ecada0.

CI snapshot from its existing owner for this preparation packet: Rust43096574664,
attempt1, exact6ecada0 stillqueued at about90min, jobs0/no conclusion; no green
claim. Observer83998 is unchanged. Preparation command sessions all ended; no
local build/test/candidate remains, and the Cargo target remains absent. Disk
100GiB available. Lead must fresh-check exact feature/default/cleanliness under
its one repository claim, ff/push normally overSSH, prove remote head and release
before CI/records/cleanup. If target moved or hook intervention is needed, stop
and release before reconciliation outside the claim.


M external observation terminal effect: existingghwatch session83998 exited1
after GitHub returnedHTTP502 “failed to get run”; this is an **incomplete
observation**, not a CI/test conclusion. Parent inspected the saved status:
run43096574664, attempt1, exact6ecada0 stillqueued, jobs[], conclusionempty.
Failed-log retrieval reports run stillinprogress/logs unavailable until complete.
Raw evidence is `logs/m-ci-43096574664.log`, `.json` and `-failed.log`;
`m-equivalence.json` separates observerexit from workflowstatus. All native
watcher cells/sessions joined; no observer process remains. No retry, restart,
new run, timeout or cancel was performed. M retains external-CI ownership parked
with outcome pending; no green claim. Local work/cleanup is accepted and target
absence previously verified. Prepared integration target/current6ec preserved;
integration is paused before any claim pending lead's product/scope decision.
No additional source/check/production/lifecycle action occurred.


Integration preparation is PARKED before any default mutation. User authorized
compatibility corrections; architect D7 brief and explicit lead source release
are pending. Prior6ec and the clean detached7c5 merge target are preserved, but
its prepared commands are historical and must not integrate stale6ec as final.
`exporter-integration-preparation.json` now explicitly marks not-ready/parked.
I0 confirmed capacity for I3 after source release; no app edits or new checks
were started. M external CI remains parked with no active observer.


## I3: D7 committed correction, R3 packet

Current I3 head `891db6b82ccd37e985507c654050143e165041a7`, tree `4b28b6924e042ebf7582b9a0a91eea0bbbddc429`; base remains7c5 and
complete series is one coherent replacement commit, no migrations. Original
reviewed/deployed7c5..6ec remains preserved, including local keep-ref
`refs/dev-sessions/2026-11-10-rust-syslog-exporter/deployed-pre-i3`, original
reviews and prior physical3hk/gsw receipts. This successor is substantive and
**not tree-equivalent** to the deployed code. No old-binary performance is
attributed to it; unchanged measurement paragraphs now explicitly identify
prior faf/6ec-equivalent/Nix3hk provenance. Actual3hk stays untouched.

D7 source hashc63269b is verified in `i3-before.json`. Byte-delimited actual
headers remain strict UTF8, including recognized ASCII svlogd inner headers;
body alone uses standard Cow replacement decoding, borrowed when valid. One
fixed unlabeled diagnostic counts repaired parsed records before host routing.
ASCII PID/svlogd/namespace classes and exact Ruby ASCII+NUL LXC strip/colon-zero
semantics are restored. Raw framing/LF/EOF/limits, malformed/first-record/
monotonic behavior and D2HTTP are preserved. Only the ten intended files in
`i3-changed-files.txt` changed; no deps/options/driver/transport/framework.

Six focused parser/collector/exposition cases passed129s; all test targets type
compiled. Full quick check passed68s: fmt, Clippy,8lib+11contract+6runtime=25tests.
Actual active command-scoped amend hook passed again8.38s/25tests, no bypass or
shared config edit. Fresh installed-policy Luna/low watchers owned uncertain
checks and joined every cell/session. One owned target is retained for review/
fixes; no release/Nix app build or long replay occurred. Lead's prose/HELP/
commit-message pass is complete. Manifest/lock/toolchain/shell/check script/
driver/HTTP/main/config hashes are exact unchanged; legacy metric definitions
and encoder are byte-for-byte unchanged.

Complete old/new ranges and substantive patch: `logs/i3-range-diff.log`,
`i3-old-new.patch`, `i3-full-series.txt`, `i3-full-branch.patch`,
`i3-source-provenance.json`; raw check/hook logs linked there. R3 must review
committed affected source/general architecture/compatibility/diagnostic/
bounds/tests/docs and whole-series/deployed lineage/no-migration conclusion.
No final pin/build/long replay before lead's review disposition. Publication/
current CI are recorded next; provider queue/outage does not become a green
claim or block this independent-review packet. Stale merge target stays parked.


I3 publication/CI complete: SSH exact6ec lease push published891db6b; fresh
remote proof remains feature891/master7c5, source clean. CI Rust43116296064,
attempt1, exact891, checkjob130845060200 and all steps **success**. Metadata
with actual timestamps/jobs and full raw log are `logs/i3-ci-43116296064.json`
and `.log`. It completed before waiting was necessary; known-quick terminal
receipt only, no new long observer or rerun. R3-ready packet was delivered
immediately after publication, independently of provider scheduling. I1 has
exact head/lock information but must await lead's R3 release before final pin.

Superseded same-branch6ec run43096574664 reconciliation is explicitly unresolved
on the provider: fresh list/view/API report queued/jobs0, but ordinary CLI
cancel refused “completed”; one direct cancellation POST after this focused
diagnosis refusedHTTP409 “not been queued yet”. Both requests were refused;
no cancellation achievement or current-run cancellation is claimed. No force
cancel/retry loop, infrastructure work or observer restart followed. Exact
responses/identities are `logs/i3-superseded-ci-cleanup.json`; original M502
raw log/snapshot/unavailable-log response remain unchanged. This is not an I3
source/check failure and does not hold the affected-review packet. Lead owns
any later provider reconciliation. All known local cells/sessions ended; no
background operation remains. One owned Cargo target is retained for review
fixes. Prepared merge target remains parked and production3hk stays untouched.


## F: flake development shell follow-up

Package F is a small tooling-only follow-up on merged/deployed
`891db6b82ccd37e985507c654050143e165041a7`; it never amends that history.
Current scope is README.md, removal of shell.nix, new flake.nix and generated
flake.lock. Sole input is nixpkgs718f670e845328e9c2cecdd832835712b2cbd065,
NAR `sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=`. Two Linux default
devShells preserve cargo/rustc/rustfmt/clippy/git/python3 and have no shell hook,
package or app output. Runtime source/Cargo.lock/driver/workflow are unchanged.
README retains command-scoped linked-worktree hooks; lead's direct wording pass
is complete. No reference/verification/scripts legacy shell mentions required
changes; historical workspace receipts remain historical.

Fresh SSH fetch proved origin/master and feature891 before edits. Generated
lock has exactly root+nixpkgs nodes; no helper input. Uncertain eval/tool/fullcheck
batch is owned by fresh installed-policy Luna/low watcher `/root/f_flake_quick`.
One explicitly owned Cargo target was recreated for debug quickcheck/mandatory
hook only; no release build or extra target. Local disk began101GiB available.
No runtime change, state format/migration, consumer pin, host build, production
probe/deployment, merge claim or default push is authorized by F. The new
follow-up awaits actual checks, scoped active hook, commit/publication and
lead-invoked affected final review; prior rewrite/R3/V3/deployment evidence is
preserved for its actual891 lineage, not claimed as new-head CI.


F committed/published review packet: head `99ffea73005685fc9f198dda3402fe24660ee944`, tree
`3dd3e3330c1b2fcaf9585d77c6a2fb04314c9c1c`, exact parent/base891db6b8, one new
follow-up commit (not an amended replacement). Source clean, SSH published on
registered feature; fresh remote master remains891 and feature matches final F.
Only README.md, flake.nix, generated flake.lock and removed shell.nix changed,
54 insertions/7 deletions. No migrations, runtime/manifest/Cargo.lock/driver/CI
workflow change, consumer pin, package build, production action or default merge.
Prior7c5..891 whole-rewrite/deployed lineage/reviews remain preserved intact.

Both Linux shell drv evaluations and flake show passed. Actual tools are
Rust/Cargo1.95.0, rustfmt1.9.0, Clippy0.1.95, Git2.54.0, Python3.13.15. Exact
shell drv paths are `6cal05wj5s9677f46xfd2jjgbba79awf-syslog-exporter.drv`
(x86_64) and `p6qilcb921g0g8jc8nb5chmvbnwdy730-syslog-exporter.drv`
(aarch64); only local x86_64 shell executed, aarch64 was evaluated.
Initial watcher `nix develop -c scripts/check` passed8lib+11contracts+6runtime
(25total), formatting/Clippy too. Its raw output retention was incomplete and
that limitation is explicit in f-quick-results.json/excerpt logs; no missing
stdout or exact wall duration is invented. Complete committed-head show/eval/
version output was recovered in7.67s of cached metadata checks, without another
full suite. More importantly the actual mandatory command-scoped precommit hook
ran the complete unchanged scripts/check under nix develop, passing all25 again
in4.84s; its full raw stream and exact argv/exit/timing are f-hook-commit.log/json.
No hook bypass or sharedconfig edit. Original common hook SHAa81910 remains
unchanged. README's direct lead writing pass is reconciled and included.

Complete follow-up series/diff/changed paths and exact unchanged inputs are
logs/f-series.txt, f-final.patch, f-changed-files.txt and f-source-provenance.json.
Current exact-head CI Rust43180133253/attempt1 is recorded in
f-ci-43180133253.json; last status at packet capture was completed/success.
Prior891 success is historical, not new-head green. No current run was canceled;
the accepted old6ec provider cancellation contradiction remains a recorded
external limit without another retry loop. Independent affected review is
lead-invoked now; the CI wait does not hold this committed quick-pass packet.
One373MiB target is retained through review/no-rerun proof; no release target,
root/peer/globalGC cleanup. All local quick/hook/push/eval command sessions joined;
current-head CI monitoring, if still needed, is the sole remaining check.


F CI terminal clarification: exact-head Rust43180133253/attempt1 completed
**success** before a long wait was needed. The packet's CI JSON/provenance
already captured success; the immediately sent lead message used the earlier
in-progress snapshot and is superseded by this terminal result. Full job log
is logs/f-ci-43180133253.log. No CI watcher or rerun was launched, and all local
command sessions are joined. The retained373MiB owned debug target awaits
review/no-rerun boundary; no ongoing process needs it currently.


F final cleanup complete after lead resolved the proof boundary: all known
session-owned F commands/watchers/tests/hooks were joined, RF needed no target,
and no other package uses this exact target. Recorded uid/device/inode/path
matched and was rechecked immediately before deletion. Accessible process
references were zero; protected unrelated metadata remained unavailable. This
is not a universal process inventory. The failed read-only sudo attempt and
visibility limit remain preserved in the existing F receipt. No further sudo
or protected-process inspection occurred.

Removed only the owned Cargo target: 391,110,656 allocated bytes /
384,495,938 apparent bytes; absence asserted. Exact result and prior limitation
are in logs/f-source-provenance.json cleanup. Source remains clean
99ffea73005685fc9f198dda3402fe24660ee944, published; all known effects are
quiescent. No other path, store/recovery root, peer data, session lifecycle or
production action. F awaits separate merge approval; no default merge occurred.


## B1: locally committed Dependabot verification and merge policy

**Ready for lead-invoked final affected review; NOT PUBLISHED.** Exact complete
range891db6b82ccd37e985507c654050143e165041a7..5e3a5f38f7d396e957d20afcb6448704a21b4c9d
contains retained F99ff plus one coherent B commit. Affected range99ff..B is
one commit, tree`f86bdb469eb533e28cc323a017594bc2732fbc41`. Merged891 is untouched,
no migrations or deployed consumer/source changes. Source clean; fresh SSH refs
remain master891 and feature99ff. Publication is deliberately held until R0
acceptance because it starts the full read-only feature validation. Prior full
rewrite/R3/F/RF/deployed lineage and old-provider limits are preserved.

B owns monthly grouped Cargo lock-only Dependabot configuration; read-only
scope/quick/maintenance jobs and always-run Rust required aggregate; trusted
default workflow_run inline metadata-only native squash-auto-merge guard; one
locked-input cargoLock.lockFile release package; minimal two-consumer extension
to the existing driver; actual-policy tests and maintenance documentation. No A
prepare/artifact/publisher framework, runtime source, Cargo.lock, manifest, MSRV,
flake lock, consumer pin, production, setting, PR or default mutation.

Focused static batch passed23.15s: actionlint, helper syntax,3 Python tests,
2 eligible+40 refusal cases against actual inline privileged code, package drv
evaluation and audit-tool help only. Full shared quick batch passed103s: workflow
lint, policy, fmt/Clippy and8lib+11contract+6runtime=25Rust tests. Complete direct
raw logs/provenance are b-focused.log/json and b-full-quick.log/json.

The actual first hook found a fixture isolation error: inherited Git hook
environment pointed the synthetic repo's staging operation at this owned source
index and propagated its scoped hook. No source commit/push occurred, HEAD stayed
F; every source file remained intact. Exact failed index/log preserved. Recovery
proved30 unowned files byte-identical to F and rebuilt an isolated native index
from exact F plus14 explicit owned B paths, validated the tree/change set, then
replaced only the owned index. No reset/clean/stash or unrelated edit. Synthetic
fixtures now clear inherited GIT_* only within their disposable context.

Focused actual inherited-hook/index regression passed7.87s with source and
sentinel logical index entries/flags unchanged. A first bookkeeping wrapper had
overly compared raw index bytes; its test output was OK and only Git/Nix stat/
cache metadata changed. Logical-tree proof and that limitation are preserved,
without inventing a second source mutation. Finally the real mandatory scoped
hook passed the complete shared suite again8.35s and created B. No bypass or
shared config/hook edit; common precommit remains SHAa81910 and common bare=true,
hooksPath/worktreeConfig absent. Detailed incident/recovery/finaltree proof is
logs/b-hook-index-incident.json; complete final stream b-hook-commit.log/json.

README, maintenance and verification prose and commit message received direct
lead writing/fidelity pass; new argparse help was inspected/accepted. Owning
maintenance page distinguishes ordinary/version/security PR scope, selected
checks, coarse75% hosted gate, immutable source/lock baselines, bootstrap and
revert/recovery. It documents the accepted hidden-bypass evidence split: runtime
Metadata-read APIs verify effective same named Repository ruleset/strict
aggregate App15368/linear history and reject visible bypass, while a maintainer
admin receipt establishes an empty hidden bypass list at initial activation.
No admin-only branch-protection endpoint or PAT fallback.

Latest official full action SHAs verified via release/ref APIs: checkoutv7.0.1
3d3c42..., github-scriptv9.0.0 3a2844..., install-nixv31.11.5 3dc140... .
Exact identities/URLs and observed Actions App15368/Dependabot Bot49699333 are
in b-upstream-identities.json. Complete range, diff, affected diff and changed
paths: b-complete-series.txt, b-complete.patch, b-affected.patch, b-changed-files.txt.
Exact source/input/hash/check/config/tree/currentremote/effect evidence is
b-source-provenance.json. The package was evaluated on final committed content
only; NO Nix app release build, fresh audit or replay has run before review.

All native/parent command cells/sessions are joined; no watcher/check or queued
cleanup is running. One explicitly owned debug Cargo target remains for review
findings/no-rerun boundary; no local release duplicate or global/store/root/peer
cleanup. Next dependency is lead's R0 review disposition, then explicit
publication and full no-write release/audit/regression validation under fresh
watchers. Existing99ff CI is historical and not a B-head green claim.


### RB-A1 narrow remediation, locally amended final source

RB final review on5e3 accepted all four affected lanes/history/no migrations/docs,
with only Advisory RB-A1: duplicate Dependabot branch-push and PR maintenance.
Direct lead release/fidelity pass allowed exactly this reduction. New local head
`f38277bb96ee2814b6fd7179fdc5facf0e609e5b`, tree`096e00e6c79956660e1a5c43874cd9909614f90b`, parentF99ff
unchanged. Only old5e3..new changes are rust.yml push.branches-ignore
`dependabot/**` and one accepted owning-page sentence. PR/manual/own-feature
paths and required aggregate remain intact. All other tree entries, runtime,
package/lock/toolchain/driver/policy tests and commit message are identical.
This is a narrow source delta, not whole-tree equivalence; no migrations.

Focused actionlint/actual Python Git+aggregate and Node policy tests passed
18.94s. Mandatory command-scoped hook passed all shared lint/policy/fmt/Clippy/
25Rust tests and amended B in17.71s, no bypass/sharedconfig edit. These individual
windows overlapped and are not added as wall time. Both parent command sessions
81858/76494 joined exit0; no effects remain. No cold standalone full suite,
release build, audit or replay was repeated. Existing single debug target is
retained; no cleanup/store/root/peer/settings/PR/production/default action.

Original RB report and5e3 kept intact, with local keepref and previous provenance.
Exact patch/range-diff/check/hash/remote proof: logs/b-rb-a1-proof.json,
b-rb-a1-exact.patch, b-rb-a1-range-diff.log, b-rb-a1-focused.log and
b-rb-a1-hook.log. Complete891..new (F+B) and affected99ff..new packets refreshed.
Fresh SSH refs remain master891/feature99ff. Publication stays held for root's
direct narrow-fix binding; there is deliberately no new-head CI yet.


### B1 reviewed publication and hosted full validation

Root accepted RB and independently reconstructed final f382/tree096e from
reviewed5e3 plus the exact two-path RB-A1 reduction (b-lead-narrow-fix.json).
Dependent publication/full no-write CI phase explicitly released. Fresh SSH
master891/feature99ff checked; ordinary scoped-hook SSH feature push completed0
in11.34s, fresh remote featuref382/master891 exact. Final comparison891..f382
captured. Source clean, no default/settings/PR/production/claim action.

Current exact-head Rust43200250554/attempt1 began on feature push: scope succeeded,
quick was in progress at first snapshot. Fresh installed-policy Luna/low native
watcher /root/b_hosted_full owns the single readonly observer and full direct
log/status capture. All four selected gates must actually succeed; required
aggregate alone or skipped maintenance cannot satisfy this phase. Initial old/new
locks are identical on the same frozen f382 source: this validates the complete
harness, not a real dependency update or live auto-merge. New workflow_run writer
is not on trusted default and feature events never authorize it.

Publication/local commands joined; current hosted run/observer remain accounted
for. No local release/audit/performance duplicate, extra Nix fetch campaign,
Ruby/transport/production matrix or target cleanup. Final current-head results
will be added after authoritative terminal evidence and joined observer effects.


### B1 full hosted validation and final quiescence

Exact run43200250554/attempt1 on f382/tree096e completed SUCCESS; every selected
job actually succeeded: Rust scope131121473558, Rust checks131121548932,
Lockfile release audit and replay131122377577, Rust required131124068531.
The aggregate log records full=true and scope/check/maintenance all success.
Readonly watcher /root/b_hosted_full exited0 after225s of observation and joined
its exec81746/all cells/sessions. No source/check/provider failure or rerun.
Full raw status/watch/job logs are b-ci-43200250554.json, -watch.log and .log.

This was a feature-push harness validation, not a real dependency update or live
PR merge. Frozen base/head/tested source all f382; lock SHA256 for both labels
is031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e,
flake.lock54143f88..., Rust1.95.0. Baseline/candidate therefore produced the SAME
release derivation `/nix/store/wlrzbyfvphabk0fg9dkdjyii4zls425q-syslog-exporter-0.14.0.drv`
and output `/nix/store/k4gycczcp70s538n37c9ww372qgyb96v-syslog-exporter-0.14.0`.
The log records an actual fresh build of that package; the identical second label
reuses the output. Effective sandbox=true was captured and each build command
explicitly requested sandbox=true. The owning checked definition enables doCheck
and release build/check, with the unchanged25-test Rust suite. Nix phase logs
were not requested by the build command, so individual release test-count lines
were not streamed; successful checked derivation execution is the release-check
evidence. The separate quick job directly logs all25 tests. No package/test-count
stream is invented, no second duplicate build or follow-up rerun was launched.

Fresh RustSec clone revision5fe96cf51fde2fd4e749d51ac8bdc59edbdce77b,
audit exit0 without ignore flags. Pinned nixpkgs718f and full source/tree/lock/
flake/toolchain/fixture/driver hashes, CPU allocation and Nix identities are in
b-hosted-maintenance-summary.json and b-hosted-validation.json. Runner affinity
was0–3,4CPUs; these are hosted resources, not exclusive production hardware.

All12 prescribed alternating baseline/candidate100,000-record runs completed
exactly, zero gaps, no scrape errors/unexpected exit/forced cleanup. Each used
seed20261110, fixed three-host fixture/cardinality1, effective1MiB FIFO and
periodic scrapes disabled. Ordinary medians baseline178,471/s vs candidate190,220/s
(106.58%); OOM65,379/s vs63,901/s (97.74%), both above75%. Individual rates/RSS/CPU
are retained in b-hosted-cases.json and compact validation receipt. Sampled peak
RSS ranged6.910–7.279MB. Since both labels use the same output, differences show
runner/generator noise, not a dependency performance change. This remains a
coarse finite regression gate, not production peak or a causal capacity claim.

The65s smoke derived16,344records/s (floor25% of slower baseline median), sent
and accepted1,062,360 records, zero gap, drain65.0010s. One real simultaneous
60s pair returned both HTTP200 through the driver's strict status check, latencies
1.068ms and1.098ms; no third marker caller overlapped the pair. All markers/counts
agreed, process exit0/no forced cleanup, CPU3.74s and sampled peakRSS7,041,024bytes.
Two latency samples are not a tail guarantee and this sparse RSS sample is not a
plateau/leak proof. Unique FIFO/exporter sequence stages remain unavailable;
zero count gaps do not establish all-path losslessness. No production/Ruby/
rsyslog matrix or local release/performance duplicate was run.

Final exact source remains clean/published f382, no source change since narrow
binding, no default/settings/PR/consumer/production/claim mutation. GitHub job
terminal receipts establish hosted completion; no independent hosted PID/cgroup
inspection is claimed. All local native/parent/API sessions are joined, no
queued cleanup or check remains. Old6ec provider cancellation contradiction is
only the preserved historical external limit, not a current-head failure.

Lead explicitly released B target cleanup after accepted review/terminal checks
and I1's no-target-use confirmation. Rechecked exact b-target-owner.json UID/
device/inode/path plus debug/.rustc_info.json/no-release markers; accessible
references were zero. Removed391,102,464 allocated /384,495,937 apparent bytes;
absence asserted. Protected unrelated metadata remained unavailable, with no
universal process-visibility claim or sudo attempt. Free space afterward was
102,154,268,672bytes (~95.1GiB), without attributing shared-space changes. No
other path/store/recovery root/peer/worktree/lifecycle action; all18 recovery
roots and branches/worktrees/raw evidence remain retained. Full cleanup identity,
visibility limit, terminal effects and exact head are b-final-validation-effects.json.

B1 source+review+validation work is complete for acceptance; lead owns initial
integration/settings bootstrap and any live auto-merge activation proof. No
implicit next package. Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/>.


## C1: conventional weekly/manual updater, committed review packet

Complete891..0b3131ffa6a2855cfa15c42de778d4bf794b4510 contains F99ff plus one coherent C replacement.
Affected99ff..C is one commit, parentF untouched; merged891 unchanged. Rejected
Bf382/5e3 sources/raw messages/reviews/CI remain in exact local keeprefs and
receipts before rewriting. B was never deployed/consumer-pinned and introduces
no migration boundary; no migrations. Current local source is clean; fresh SSH
master remains891 and featuref382, publication intentionally held for finalR0.

One weeklyMonday04:23UTC/manual job updates compatibleCargo.lock, checks whole
tracked lock-only regular/mode scope, fresh RustSec audit, ordinary sandboxtrue
checked package, then fixed botcommit/single-child/nonforcepush with freshbase
guard. No-change regular runs exitwithoutcommit; dryrun/featuremanual validate
withoutwriting. Finalpush is sole explicit shell-tokenenv. Trusted checkout/
installer may consume token and hostNixconfig staysoutside candidate; no actual
credential/config enters candidate source/env/mount. Nixeval confirms token
envkeys absent/no sandbox bypass; only selected proof fields recorded, never
full config/environment. CIprecommit wrapper invokes the SAME cachedsandbox
check with tokenunset; ordinary source developer hook byte-identical. No
artifact/authorizer/publisher framework.

B Dependabot/metadata guards/helpers/policy suite removed; pre-B benchmark exact
F bytes restored, special recurring12x100k/65s campaign and Node/actionlint env
deps removed. One owning cargoLock.lockFile package runs sharedcheck --release
with native fmt/Clippy/Python/Git and fixedCargo target; all updatedcrate/build/
proceduralmacro/test and hook validation remainsinside Nix. Normal RustCI is one
readonly Nix release/check job. Runtime/Cargo.toml/Cargo.lock/toolchain/flake.lock
and ordinary .githooks unchanged. No consumer/runtime/production/settings/PR
action, additional credential or initial default integration.

Focused8 tests of ACTUAL updater shell passed in disposable realGit repositories
(no fakeGit engine): nochange, failedcheck, onlytestedlock+officialauthor/committer,
extra tracked/mode rejection, dryrun, stale default, real competingpush rejection.
Only trustedNix tooling is substituted in these fast fixtures; actualNix sandbox
validation is later. Inherited Git context is cleared solely inside fixtures,
controlled Gitconfig redirects audit clone to a local fixture. No HOME rewrite
or sourceindex mutation. Fresh Luna quickbatch passed workflowlint9.55s, package
eval3.52s, fullsharedcheck121.88s with8shellfixtures+25Rust/fmt/Clippy. Full raw
streams c-workflow-lint/package-eval/full-quick.log and c-quick.json retain exact
source/commands/effects.

One staging command named already-staged removed B paths and returned128; a
subsequent local amend ran despite that result and therefore left3prose paths
unstaged. It was never published/reviewed; full hook passed actualcompletecode.
Preserved interim rawlogs/receipt, explicitly staged the existing ownedC paths
and finalamendedwithmandatoryhook; final intendedindex tree exactlymatches
commit tree. No standalone cold suite repeated. Final actual command-scoped
hook passed8shell+25Rust/allsharedchecks13.50s; fullraw c-hook-commit.log/json,
c-before-commit.json and c-staging-reconciliation.json. Sharedconfig/commonhook
unchanged, no bypass/reset/clean/stash. Allcells/sessions6686/84468/49604 and other
knownparentcommands joined; no ongoingcheck orqueuedcleanup.

Mainlead prose/fidelity pass complete for shortmaintenance README/verification/
message and descriptions. Latest official checkoutv7.0.1/3d3c42... and Nixinstaller
v31.11.5/3dc140... refs verified in c-upstream-actions.json; existingexamples read
fromexact publishedsource, no peerworktree/session access. Complete891..C,
affected99ff..C, B->C removaldiff/range and input/hash/history/check proofs are
c-complete-series.txt, c-complete.patch, c-affected.patch, c-from-b.patch,
c-range-diff.log and c-source-provenance.json. Final package derivation eval only
is c-final-package-eval.json; no actual release/update/audit before review.

One owned debugtarget remainsfindings-only; no localrelease duplicate orstore/
root/peer/lifecycle cleanup. R0 throughlead is next; then publication/longactual
Nix/featurevalidation, never oldB performancecampaign. Initialsourceintegration
remainsseparateapproval, and source is not a new-head CIgreenclaim yet.


### RC-I1 fail-closed sandbox fallback, committed narrow successor

RC final report accepted all four lanes/history/no migrations/docs with only
Important RC-I1. Default sandboxfallback could permit an unsandboxed build when
namespaces are unavailable despite sandbox=true. Source now sets fallback=false
in BOTH installer configs and explicitly on all main/CIhook build invocations.
Before candidate build, it asserts sandboxtrue/fallbackfalse and prints only
those two nonsecret values, never full token-bearing config/environment. Existing
fixture returns both fields, checks explicitfalse flags, and adds exactly one
negative case proving fallbacktrue fails before build/commit/push. Lead's exact
maintenance clause is included; no other prose/message change.

Reviewed0b313 keepref/rawmessage/packet retained; successor `a4554a93723abd65007a5dff174db63cbecc1245`,
tree`f81944cebcb80c1d1d524b7fcb29534e6e736564`, exactF99ffparent. Only4paths differ from0b313
(two workflows, fixture, owningdocs); all other blobs/modes/message identical.
No migration or other design change; merged891/F preserved and B historical
keeprefs intact. Exactpatch/range/log/hash/sourceproof in c-rc-i1-proof.json,
c-rc-i1-exact.patch, c-rc-i1-range-diff.log. Original RC report remains separate.

Focusedlint+9 actualshell/Git tests passed15.22s; final command-scoped activehook
passed9fixtures+25Rust/fmt/Clippy24.25s and amended intendedtree exactly. Complete
raw c-rc-i1-focused.log/json and c-rc-i1-hook.log/json; no bypass/sharedGitconfig
edit. All sessions65514/11959/parentcells joined, no known effects. No cold full
suite, Nix app release, hosted/kernel/leak experiment or sourcepublication before
binding. Actualhosted leak/failure is not established. One owneddebugtarget
retainedfindings-only, no cleanup/default/settings/PR/prod/claim action.


### First actual C hosted failure and minimal entrypoint correction

Run43214738861/attempt1 exacta455 failedafter50.48s successful releasecompile.
Filtered config proved sandboxtrue/fallbackfalse. IncheckPhase, directscript
shebang `/usr/bin/env` was unavailable and builderexited126;9fixtures/25Rust
checks did NOT run inthisrelease. Fullrawstatus/watch/log preserved; no source
consumer/default/productionwrite or hostedleak established. Observerallcells/
sessionsjoined. Actualfailureexcerpt/diagnosis c-first-hosted-failure.json.

Root accepted diagnosis and released exactstandardfix: package checkPhase
`bash scripts/check --release`, using existingstdenvBash. No new dependency,
shebangframework, kernelexperiment, installer/scrub, assertion/sandbox weakening.
Local successor`b9b9cfea4331ff28bd883f1ed7415af6f27cd5f7`, tree`a1d826ecdbf019600ee63f74e74c385b00902a7c`, parentF99ff.
Onlypackage.nix one-worddiff fromrevieweda455; allotherblobs/modes/message match.
Failedpublisheda455 keepref/rawmessage/CI retained, merged891/F untouched.

Focused `bash -n scripts/check` and declaredNixcheckPhase evaluation passed.
Additional requested STATIC inspection of only NEW temporary helpers confirms:
fakeNix andraceGit hook use sys.executable absolutePython shebang; CIprecommit
uses command-v-Bash shebang; shellfixture invokes Bash explicitly. No /usr/bin/env
assumption inthosehelper sources. No broadfixtureinventory/rebuild. Actualsandbox
execution of9 remains pending nexthostedrun. Realcommand-scoped hook9fixtures+
25Rust/fmt/Clippy passed14.95s, intendedindex tree==committree, no bypass.

Exactpatch/range/hash/entrypoint/effect proof c-shebang-proof.json,
c-shebang-exact.patch, c-shebang-range-diff.log, focused/hookraw logs. Complete
891..successor/affectedF..successor/removalpackets refreshed. Allknownparent
cells/session21595 andpriorobservercommandsjoined; no ongoingeffects.
Publication held untilrootdirectbinding; no duplicate localrelease or
unmodifiedCIrerun/app/performance/kernelcampaign/default/settings/prod/claim/
cleanupaction. Target retainedfindings-only.

### Final C1 hosted checked-release result and quiescence

Final source is `b9b9cfea4331ff28bd883f1ed7415af6f27cd5f7`, tree
`a1d826ecdbf019600ee63f74e74c385b00902a7c`, with exact parent F99ff. The SSH
feature publication and captured comparison preserve master891. Complete
891..head has two commits (F+C); affected99ff..head has one coherent C. The
original RC report, reviewed0b313, corrected a455, rejected B history, and failed
43214738861/attempt1 are retained. Root narrow bindings are
`logs/c-lead-narrow-fix.json` and `logs/c-lead-entry-fix.json`. No migrations,
updated source Cargo.lock, runtime changes or consumer pin exist in C.

Exact Rust run43216044595/attempt1, job131175436008 (`check`), completed SUCCESS.
Full raw log records only the two nonsecret configuration values:
`sandbox=true`, `sandbox-fallback=false`. Actual release compilation took1m09s;
actual checkPhase took50s and ran9 shell/Git fixtures plus25 Rust tests
(8+11+6), rustfmt and Clippy. Installation/fixup/strip also succeeded. The checked
derivation was
`/nix/store/n1kw1wbmgqfgn5mfz6qx848apar1pgc6-syslog-exporter-0.14.0.drv`;
output was
`/nix/store/1gxpkcpw92jkrnxxndayjcir891xj7cj-syslog-exporter-0.14.0`.
The pinned nixpkgs718f Rust/Cargo1.95 paths are present in the raw job log.
Cargo.lock SHA256 remains031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e;
flake.lock remains54143f880b4fbb768ed2fc315752efe3dcab52a7cc7f22af16e72c9dafe783ce.
Exact current manifest/profile/script hashes and raw-log hash are in
`logs/c-hosted-validation.json`.

Fresh installed-policy Luna/low watcher `c_hosted_entryfix` completed. Its
`gh run watch --exit-status` returned0 in66s. The enclosing login shell/session
43159 subsequently returned1 during bash_logout because set-u encountered
unset `__ETC_BASHLOGOUT_SOURCED`; this observation-wrapper limit is preserved
separately from the successful CI result. All known cells/native watchers/tool
sessions are joined; no background operation or queued cleanup remains.

At the accepted review/terminal-CI/no-rerun boundary, the exact owned target
(device64769/inode43926827/uid1000 and owner receipt unchanged) had no accessible
cwd/exe/fd reference and no known C operation consumer. Its debug markers were
present, no release target existed, and ownership was rechecked immediately
before removal. Removed391,041,024 allocated /384,495,938 apparent bytes; exact
path absence was asserted. Free space afterward was112,309,911,552 bytes, without
attributing other shared-space changes. Protected unrelated metadata was
unavailable; no sudo attempt or universal visibility claim. No other target,
store path, recovery root, peer data, worktree, branch or session lifecycle was
changed. Details are `logs/c-final-effects.json` and the retained owner proof.

This is actual checked-package/shared-check validation on a feature push. It
does not establish that the weekly updater, real Cargo update, fresh RustSec
audit, bot commit or authenticated push has run. Those updater-path operations
remain the explicitly separate post-integration default-branch dry-run gate.
No new campaign, default/settings/PR/production action or next package started.


### C initial integration — 2026-11-12 14:34 UTC

User approved the exact repository/target with “ok, merge it”. The declared-shell
FF and nonforce SSH push placed F99ff+C b9b9cfea on remote master, with exact
remote feature retained. Claim5d6cf0ad was released and verified before CI or
records; shell4340 exited0. No new hook execution was required for this FF.
See logs/c-integration-result.json. Actual master updater dry-run43238754813
(attempt1, b9) now checks resolution/audit/sandbox without a commit/push; ordinary
master Rust43238628054 is observed alongside it. Production is unchanged.


### C master verification — accepted

Master Rust43238628054 and updater dry-run43238754813 passed on exact b9.
The dry-run resolved errno0.3.14→0.3.15, freshly audited candidate lock c417e3ec
against RustSec af7b3ec3 and passed actual strict-sandbox9fixtures+25Rust
release tests/fmt/Clippy. DRY_RUN=true and explicit no-commit/no-push are logged;
push step skipped and remote master/feature remain b9. Bot write permission is
not exercised by this dry-run. Compact receipts: logs/c-master-validation-summary.json.
Watcher report transport ended incomplete; lead reconciled authoritative jobs,
logs, original joined11219/29480 sessions and completed native turn, then resolved
external effects without a rerun. All known effects ended; session left open.
