# V: local matched verification

Owner implementer0. Evidence-only package, dispatched after I/C2 acceptance.
No production access, deployment, dry activation, copy to production, machine or
merge claim, default integration or new shipped source is authorized.

## Phase and measurement gate

**V complete and accepted for measured-envelope preparation on final faf/3hk.**
The corrected two-consumer gate passed:42/42responses200,1.04Mrecords,gap0.
All final comparison, transport and lifecycle cases have ended; evidence is
accepted by the lead with explicit limits below. Final receipts live in
`measurements/final`.
No shipped source changes are part of V. Historical8ef/4gb results below retain
their original scope and do not certify the corrected artifact. Current build
and source identities are in the final-gate section and
`c2-artifacts/i2-build-verification-summary.json` (19tests, corrected host653paths).
Earlier187.714s package/127.576s host and rollback-transfer results belong to
75b/4gb and remain in `c2-artifacts/retained-build-recovery-summary.json`.

The goal is a bounded local measured envelope, not an all-load losslessness or
exclusive-hardware claim. Unexpected failures stop the current batch for diagnosis.
Deliberate saturation loss is retained as evidence and cannot be relabeled a pass.

## Historical8ef measurement identities

| Input | Identity |
| --- | --- |
| Exporter source / reviewed driver | `8ef8241c60f3b99976191b92f0467c945e36b1c8` |
| Configuration | `75b0af0323db1412de457cb73362fd741941eef4` |
| Rust release executable | `/nix/store/4gbgng817gz6gfvaxwh76gvzh8yvp478-syslog-exporter-0.14.0/bin/syslog-exporter` |
| Rust executable SHA256 | `06e40f591a64bb23f678eb1533c401256e5c529452159b6620bb005c0e2d195c` |
| Rust package derivation | `/nix/store/63q2mdnravm3cb9920mc1hcp0mcinfas-syslog-exporter-0.14.0.drv` |
| Rust output NAR | `sha256-+T5cM6etY80HtKvvVIShfuiHcZJxAdv3iQgPG1DmqHQ=` |
| Toolchain / profile | Rust/Cargo 1.95.0, Nix cargo build/check release, strip=true, all 14 tests passed |
| Ruby package | `/nix/store/w7g32wplgls6x79608h6nij02a4vvq9y-syslog-exporter` |
| Ruby source / libraries | `7c5a8e74e44a704cceb99cd05716af6800d78efd`; Ruby3.4.9, Puma8.0.2, Rack3.2.7, prometheus-client4.2.5 |
| Producer executable | `/nix/store/g0g8nvq928bgl2dwvvddh99l0543s9cx-rsyslog-8.2610.0/bin/rsyslogd` |
| Actual generated 67-host config | `/nix/store/k5a6bd0ilb1m6k1px7a4hpxrhp2r8s6p-syslog-exporter.json` |
| Config SHA256 | `1bbd6ae370b21067145c78cf68b21b0e7257549327cf7beb280f671c618426f9` |
| Reviewed driver SHA256 | `f7def4b0644dda40b9810b2905ce25e29f68ccfe3c089f24816eb9833f60a2c0` |
| Restored exact baseline config.ru SHA256 | `fe8b3a559bbca732befe0ef70fd75ac6bb916c46ba3d75e0f15d6bf6382baba6` |

The full source/input/profile/closure and old-system retention receipts are
C2-owned: `package-verification.json`, `host-verification.json`,
`final-flake-metadata.json`, `normal-confctl-host-derivation.json` and
`rollback-retention-verification.json`. No duplicate Cargo release build occurs.
The original independent reviews remain unchanged in
[exporter review](exporter-final-review.md) and [consumer review](c2-final-review.md),
with accepted narrow exporter fixes documented in [I evidence](exporter-review.md).

## Matched conditions and recipes

Shared KVM guest, Linux 6.18.57, x86_64, AMD EPYC7551, 64 vCPUs exposed as two
32-core sockets and one thread/core. Allowed affinity was 0–63. Candidate
affinity is 60,61 for both implementations; generator CPU62; producer CPU63.
These are affinity assignments, not exclusive reservations. Other sessions and
the hypervisor can contend. Initial shared load averages were about 15.

An owned disposable FIFO preflight accepted `F_SETPIPE_SZ=1048576` and returned
exactly 1048576; smaller tested capacities 262144/65536 also worked. Both candidates
request 1 MiB, with the same 67-host map, seed20261110, profile, record count,
offered rate, scrape schedule and finite deadline. Rust reports actual capacity.
Ruby's healthy ingestion requires its unrescued F_SETPIPE_SZ to succeed; a Ruby
capacity/startup failure stops the batch rather than silently changing capacity.

Corpus identity is the tuple of reviewed-driver hash, actual-config hash, seed,
profile, record count and cardinality. The driver uses a local seeded RNG and
fixed record timestamps, so matched cases generate identical record bytes by
construction; no raw corpus stream hash is claimed. Synthetic host distribution
comes from the actual map and is not an observed production traffic distribution.

Baseline `config.ru` was restored from the exact canonical Git revision to
`/tmp/2026-11-10-rust-syslog-exporter-v/config.ru`. Ruby launch is:

```text
taskset -c 60,61 env -u WEB_CONCURRENCY RACK_ENV=production SYSLOG_EXPORTER_CONFIG={config} /nix/store/w7g32wplgls6x79608h6nij02a4vvq9y-syslog-exporter/bin/puma --bind tcp://{listen} /tmp/2026-11-10-rust-syslog-exporter-v/config.ru
```

Rust uses the Nix executable with `--config {config} --listen {listen}` under the
same affinity. The reviewed driver runs on CPU62 and substitutes its private
FIFO/config/loopback listener. Transport mode uses an evidence-only three-line
wrapper that execs the exact pinned rsyslog executable on CPU63.

Each case has a fresh explicit dev-session service registration and stable UUID,
recorded with exact argv before launch. An evidence-only operational recipe
registers the reviewed driver and samples only that exact unit's cgroup PIDs
every 0.2s, collecting RSS/CPU and shared load. It neither changes the corpus nor
reads another session's processes. It records no remaining cgroup PIDs at finish.
The native watcher owns the finite related batch and reconciles all tool sessions.
Per driver deadline is 90s, plus bounded cleanup allowance; an outer 115s overrun
terminates only the exact owned unit and stops the batch as a failure.

Recipe provenance: `/tmp/2026-11-10-rust-syslog-exporter-v/run-case.py`, SHA256
`55df6300e35f8b008e9565cfb3caf60f19ba4ad7626cc6bf1673825d83b0cd8c`;
rsyslog affinity wrapper SHA256
`80e5cf9903da6f648d350e0cd8ce2054bcf750445b1de09c221c3b1c3251a04a`.
These are bounded operational collection recipes, not new shipped test/driver
source or a new framework. Exact commands/stable IDs/outcomes and samples live
under `measurements/`; only compact receipts and useful failure evidence are kept.

## Planned matrix and decisions

1. First ordinary direct-FIFO pair, 100k records at maximum producer speed,
   one-second stress scrapes, to identify generator/reader bottlenecks and select
   meaningful rates. Warm-up records are excluded by the reviewed marker logic.
2. At least three alternating matched ordinary and OOM fixed-cardinality pairs,
   normally 100–200k records, same conditions. Distinguish finite drain capacity,
   repeatable controlled offered rates and producer-limited lower bounds.
3. Controlled sustained/burst cases around Ruby's observed repeatable boundary,
   Rust at twice that boundary, with/without scrapes, one bounded high-cardinality
   case, RSS trend after initial host/series warm-up. One-second or faster scraping
   is stress, not the production 60-second schedule. State honest finite sample
   counts/latency limits; do not invent a p99 from no observations.
4. Pinned TCP/UDP/private-local below-saturation and deliberate-overload/pause
   cases; then bounded one-off size, positive-partial-write exposure, reader/
   producer restart and SIGTERM-backlog recipes. Never add a competing FIFO reader
   or alter producer transport/queue policy. Distinguish submitted sequence IDs,
   archived unique IDs/duplicates, unavailable producer/FIFO/exporter unique-ID
   stages and count gaps. Whole-process SIGSTOP also freezes HTTP/expiry.
5. Promtool only from the pinned cache without a local tool build. Separate parse
   errors from the inherited literal-counter naming lint.

Reassess after about 10–15 measured minutes using achieved results and missing
gates; an unexplained failure gets focused diagnosis before another batch.

## Storage and effects

Initial headroom was 96–97 GiB during prep. After I acceptance, C2's full Nix
14-test pass and explicit confirmation no rerun needed it, checked owned process
references (only the inspection shell matched), then removed exactly the proven
owned 403 MiB `work/<slug>/cargo-target`. No store path, C2 recovery root, peer data,
global GC or session lifecycle state was touched. Raw driver temp corpora/archives
are discarded only after compact counts/seed/receipts and failure diagnostics.

## Preliminary calibration

Two matched ordinary100k maximum-speed direct-FIFO cases passed, with exact
100000 exporter-count deltas and no gap. Ruby: write11.588s, drain11.965s,
8358records/s, CPU11.85s, peakRSS37.52MB; Rust: write1.517s, drain1.520s,
65769records/s, CPU0.56s, peakRSS7.58MB. Both used1MiB/67hosts/seed/affinity
and1s scrapes. Ruby had11 periodic samples, maximum observed latency26.2ms;
Rust had1 sample,3.18ms. These are finite-sample observations, not statistically
established p99 tails or repeatability/capacity acceptance. Rust's short run is
likely bounded by the Python generator.

Calibration services `6fab278b-0497-4dff-818d-0bbc54cb7f39` (Ruby) and
`171f61bf-e0d7-493d-a061-330341655a10` (Rust) completed with no cgroup PIDs.
The fresh watcher completed17.3s batch, exit0 and joined its tool sessions.
Ruby final status-15 is expected graceful TERM disposition, not an earlier
measurement failure: log records graceful stop after complete counts; pinned
Puma launcher.rb448–452 calls do_graceful_stop then raises SignalException when
configuration.rb167 default raise_exception_on_sigterm=true. It was reaped in
32ms without forced kill. Rust exited0 in16ms. Shutdown statuses stay distinct.
The Ruby candidate RSS medians by elapsed thirds were37.39/37.47/37.52MB,
showing no large growing queue in this small fixed-cardinality run; longer and
repeated trend evidence remains necessary.

Measured results and final no-running-effects proof will be added here.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/


## Three matched repeats, finite direct FIFO

All three ordinary pairs and three OOM pairs completed100000 records per case,
with exact count deltas and zero gaps:1.2million measured records total. Ordinary
rates Ruby8358/8649/8465 versus Rust65769/63423/67476records/s; OOM Ruby4248/3828/3997
versus Rust38923/35873/35138records/s. Median finite drain ratios are7.77x ordinary
and8.98x OOM. These exceed2x as observed reader-stage lower bounds; the Rust
ordinary input is likely Python-generator limited, and this is not an absolute
maximum or exclusive-host result.

Ruby peaks37.5–37.7MB ordinary and38.2–39.2MB OOM; Rust7.6–7.8MB ordinary and
7.9–8.1MB OOM. Fixed-cardinality RSS medians in later elapsed thirds were near a
plateau (Ruby about37.4–39.0MB, Rust about7.6–8.1MB); no large accumulating queue
was observed. Source still retains dynamic series, and no total-memory cap is
claimed. Ruby ordinary CPU11.76–11.85s, OOM24.08–26.02s per100k; Rust ordinary
0.54–0.58s, OOM1.97–2.02s. These CPU counters include candidate startup overhead.

Stress1s scraping produced33 ordinary/72 OOM samples for Ruby and3 ordinary/6
OOM samples for Rust. Maximum observed sample latency was26.2/32.8ms Ruby and
3.52/5.38ms Rust. Short runs provide few samples, so these are honest finite
observations; production tail latency is not statistically certified.

`measurements/repeats.log` and per-case JSON/invocations/samples retain exact
commands/UUIDs and shared loads. Fresh watcher ran146s, exit0. All ten repeat
service IDs were independently checked in authoritative registry as exited,
cgroups empty and native tool sessions joined. Immediate registration snapshots
show startup state running; they are not terminal-state proof.


## Controlled rates, scrape diagnostics and V park

All12 control commands completed with exact counts and empty cgroups; parent
also checked their exact UUIDs in `controls-services-final.json` as exited.
Ruby ordinary100k@8000 achieved7994/s; Rust@16000 achieved15988/s. Ruby OOM100k@3800
achieved3798/s; Rust@7600 achieved7598/s. These are controlled finite lower bounds
and do not establish the absolute highest sustainable rate.

Three Rust no-scrape ordinary rates64931/60094/62417 (median62417) and OOM
34388/20507/26526 (median26526) were lower than the three1s-scrape medians65769
and35873. No scrape-induced throughput loss is observed, but the shared-host/
generator variance is substantial, especially OOM. These observations cannot
causally certify a universal10% degradation bound at maximum capacity.

The30k-record/30k-program high-cardinality case completed in0.571s with exact
counts. The driver's1s sampler missed RSS and returned null; independent0.2s
cgroup samples recorded five candidate observations, sampled maximum54.3MB and
elapsed-third medians16.0/46.3/51.5MB. Dynamic series remain retained and memory
grows; this is explicit evidence against a total-memory-cap claim. All quoted
RSS maxima are sampled observations, not an exhaustive kernel high-water mark.

The960k@16k/s exactly60s case completed all counts but its periodic scrape got
503 when it collided with the driver's own final-marker polling. This result is
retained as a failed normal-scrape observation, despite driver outcome=complete.
The separated1M@16k/s62.5037s case produced one ordinary60s scrape200 in3.61ms,
no scrape errors and exact1M count; RSS medians7.54/7.67/7.67MB in the earlier
60s case showed a plateau. One sample is not a statistical production p99.
The separated case proves only the isolated schedule, not concurrent consumers.
Its service `d6d5d78d-4c79-46b3-9f4f-4fc2ce46987a` has no process or cgroup;
parent exact-unit state verification supersedes the watcher's inactive/dead wording. Watcher elapsed66s.

Pinned Prometheus3.12.0 server output lacks promtool; the correct CLI output
`/nix/store/h9qjpp5k20fifrsq1hdhj13y7psq6462-prometheus-3.12.0-cli` was obtained
from the official cache without a local build and retained by an owned temporary
root. Both actual Ruby and Rust calibration exposition parse checks returned3
solely for the same inherited literal-counter naming lints: `syslog_message_count`
should end `_total` and nonhistogram/nonsummary should not end `_count`. There
were no parser errors. Raw logs/statuses are `measurements/promtool-{ruby,rust}.*`.
Legacy names remain unchanged as required.

### Two-request overlap evidence

Canonical D2 establishes two legitimate independently scheduled60s Prometheus
consumers. The corrected bounded diagnostic ran20 barrier-synchronized request
pairs while160k@16k/s direct-FIFO ingestion ran. Of40 responses,33 were200 and7
were503; maximum observed request latency5.145ms. All160000 records counted
exactly with zero gap, driver/candidate exit0. This confirms an HTTP compatibility
gap for8ef's immediate encoder rejection, not ingestion loss.

The first diagnostic failed before candidate launch because a temporary recipe
was named `concurrent.py`, shadowing Python's standard package. Unit
`e13cc9e7-dddd-4605-a4a2-404ddcc6435a` failed with MainPID0/cgroup absent and no
traffic. Journal proved the import error. The owned recipe was renamed to
`metrics-overlap.py`; the single corrected attempt used unit
`62131138-b29d-43fa-9d8e-8061fc92e6c8` and completed with retained ActiveState=active/SubState=exited, MainPID0,
ExecMainStatus0, empty ControlGroup. Parent exact-UUID query supersedes the
watcher's incorrect inactive/dead wording; this is a retained exited service
record, not a running process. No retry of the broad matrix occurred.

Receipts: `measurements/concurrent.json`, `concurrent-driver.json`,
`concurrent-corrected.unit-final.txt` and `concurrent-corrected.journal.log`.
The native watcher failed to redirect the requested outer stdout log, so that
exact outer transcript is unavailable; the persisted full query receipt and
own-unit journal preserve the actual result. The watcher also attempted an
inapplicable registered-monitor status/report lookup, which was rejected;
this was a native utility, not a registered monitor operation. Its native exec
session88178 completed0 and no other operation-owned session/cell survived.
Parent independently rechecked exact unit state and persisted data; no rerun
was used to manufacture a log.

### Current park and remaining path

V is explicitly parked on lead-accepted D2: HTTP correction and affected review,
then C2's refreshed source/vendor pin and package/host output. implementer0 has
capacity for the separately dispatched I2 and retains V ownership; no next
package was accepted or silently queued before this park.

No old-artifact TCP/UDP/local transport, size/shortwrite or restart/backlog case
was launched. Their bounded operational recipes are prepared only. Once released
on the final binary, the shortest remaining measured path is about2–3minutes:
focused two-consumer/normal-scrape checks plus affected scrape comparison;
below-saturation/useful-burst and declared-overload transport cases (~90s), then
bounded size/positive-shortwrite, reader/producer restart, partial EOF and SIGTERM
backlog observations (~10–30s). Stop any unexpected correctness failure; expected
overload losses remain separately classified observations. The old8ef throughput
and unchanged parser/collector evidence may be reused only for its independently
proven unchanged scope, never as final successor-binary certification.

All launched measurement commands exited with no known surviving
candidate/driver/daemon/tool effects. Shipped exporter source/index remain clean
at8ef; no source edits, production access, deployment, dry activation, copy to
production, claim or integration occurred. C2 retains all Nix recovery/build
roots. Session remains open.


Parent final effect-proof correction: exact normal/overlap unit queries show
retained active/exited records (RemainAfterExit), MainPID0 and empty ControlGroup.
The utility's inactive/dead wording is not authoritative and was corrected here
and to the lead. No registered service was stopped/retired to make state look
inactive. Current filesystem headroom97GiB; compact measurement artifacts4.5MiB.


## Historical final-artifact preparation checkpoint (superseded by results below)

I2 affected review found no findings and the lead accepted the corrected C2
mechanical pin at `a839ccf7e7ff07ac616ad7994af33f07975bd1b5`. C2 reported the
corrected package passed all19 release tests, version/config67 and runtime
Ruby/Python exclusion. Actual binary is expected/confirmed by C2 as
`/nix/store/3hk34i2k760dirn1xrarxqsrwrcryaj5-syslog-exporter-0.14.0/bin/syslog-exporter`,
SHA256 `f1ad1b4f65be4e4315224b8e3426603f67eb8e99a42593e8f7cfe40ddbc4062c`,
package NAR `sha256-Y+H0duMpY5PGDsNk9DYyO7YJXG3u8u4kwV9Y9X0md28=`.
The normal host build is still active; these are not permission to launch.
No final-artifact candidate has been run. A separate released-build manifest is
intentionally absent until explicit both-build quiescence/gate; prepared recipes
fail before launch without it. Current debug target remains373MiB pending that
quiescence/no-rerun check; it has not been deleted during active build preparation.

Prepared final-only recipes live under
`/tmp/2026-11-10-rust-syslog-exporter-v-final/`, keeping old recipes/receipts intact.
They assert provider `faf06c1185ad2f6d39286d2e33896a6455b7bea6`, corrected package
path and binary hash; preflight will recompute the exact package NAR, local
source/driver identities and bind the actual C2 release receipt before measuring.
Results go to `measurements/final/`, never overwriting old8ef evidence.

The first normal two-consumer fixture is65s/1.04M records@16k/s. Driver periodic
scrapes are disabled; after initial warm-up completes,20barrier pairs make only
two requests at a time during ingestion. Then two separately scheduled60s
consumers both request once around60s, still about5s before final-marker polling.
There is no third driver HTTP poll in either normal phase. All42 must be200;
excess/timeout503 remains separate overload, not a normal pass. The receipt will
record actual statuses/latencies/ingestion progress and a final exact counter
check, plus direct-child RSS/VMHWM/CPU samples without extra HTTP traffic.
One sample per periodic consumer is finite evidence, not a statistical tail SLA.

A short final-only comparison is prepared: two new Rust ordinary/OOM repeats
with1s stress scrapes, two without scrapes, and one fresh matched Ruby control
per profile for changed shared-host load. It reuses exact seed/67-host map/
1MiB/affinities and the reviewed driver. It does not repeat the full old matrix.
Previously unfulfilled transport, size/positive-shortwrite, reader/producer
restart and backlogTERM recipes are adapted to the corrected output but remain
unlaunched. Expected remaining measured work is about4–5minutes including65s
normal overlap, fast comparisons and the prior2–3minute transport/lifecycle path;
stop at the first unexpected correctness failure. No tool/cache fetch is planned
during measured batches. No source edit, production access or deployment.


## Final measured gate released

Both C2 and lead explicitly released the corrected measured gate after package
159.576s/host120.315s builds and all receipt checks ended. Source is
`faf06c1185ad2f6d39286d2e33896a6455b7bea6`, configuration
`a839ccf7e7ff07ac616ad7994af33f07975bd1b5`. Corrected package3hk/SHAf1ad/NARY+H0
above are the only final candidate. Corrected host is
`/nix/store/nw3d0j9hb1mrwf7hd0daxm6gk1vcfabc-nixos-system-log-26.05.20261026.718f670`,
NAME`2026-11-11--00-46-58`, NAR
`sha256-KknCgMIpbg2EJqGIijH1rFdiAWjtdt33n+Saj2HLemU=`,653-path closure.
The complete authoritative receipt is
`c2-artifacts/i2-build-verification-summary.json`; source/input/profile/closure
proofs are linked there and I2/C2 mechanical reviews remain retained.

Vendor layers are deliberately typed: cargoHash`sha256-dvnEEbDRJoHlHLj/EDXp21PYrnvx5+J1+BGYQkmN7yI=`
is the recursive fixed-output **staging** vendor hash, not the processed vendor
NAR. The normal processed vendor pathdfpq has NAR
`sha256-+zkoIofB1/aV2+6AH86P1thpT3Rpt2UpLSxDGQuIDuY=`. C2 owns the exact layer
receipts and retention roots; V does not rename them or conflate their hashes.

Before the first measured case, removed only the373MiB owned Cargo target after
checking no nonancestor process command references it, with accepted I2 review,
all19 Nix release tests and both-build/no-rerun quiescence. No store path, peer
file or C2 root was touched. Headroom91GiB. No Cargo release duplication, build
or cache fetch is permitted during final measured batches.


Final recipe provenance is `measurements/final/recipe-identities.json` and the
released identity/preflight receipt will be retained next to results. The first
final normal fixture is registered as7210bbf6-46dd-4b9b-aa98-57903c6e3394. Its
65s run is held to the same1MiB/67hosts/seed/CPU partition; no cache fetch or other
candidate runs concurrently. Old reference records remain untouched.


## Final corrected two-consumer result

Registered unit7210bbf6-46dd-4b9b-aa98-57903c6e3394 completed on the corrected
faf/3hk artifact. All42 requests returned200:20 intentionally overlapping pairs
and two independently scheduled60s consumers during sustained ingestion. There
was no third diagnostic request in those phases. The final marker was sent
after65.000s, separately from the60s pair. All1,040,000 records were accepted,
reader-stage count gap0, achieved15,999.25records/s over65.003s. The maximum
HTTP latency was6.76ms across42samples; this is a finite sample on a shared host,
not a population p99 or isolated-hardware result. No scrape errors or503s occurred.

CPU11.72s; observed RSS maximum8.18MB; elapsed-third RSS medians
8.05/8.18/8.18MB. Fixed-cardinality memory plateaued
after initialization. Graceful shutdown took15.54ms, exit0, no forced kill.
The parent independently queried the exact unit after the watcher ended:
active/exited with RemainAfterExit=yes, MainPID0, emptyControlGroup and
ExecMainStatus0. The watcher's inactive/dead wording was inaccurate; it does
not affect the zero-process proof. All watcher cells were joined. Full receipts
are `measurements/final/two-consumers-summary.json`, `two-consumers.json`,
`two-consumers-driver.json`, `two-consumers.samples.csv` and `normal.log`.
The previous8ef 503 collision and paired-consumer failure remain retained.


## Final short comparisons and limits

The final comparison command completed exit0 in about93.5s; its ten registered
cases each counted exactly100,000records, gap0, no scrape errors, no forced
shutdown. `measurements/final/comparison-summary.json` retains exact source/input
links, rates, CPU/RSS, elapsed thirds, load and service UUIDs;
`comparison-units-final.json` independently proves all ten MainPID0, empty cgroup
and ExecMainStatus0. Ruby process return-15 is the pinned Puma normal TERM
disposition already diagnosed above, distinct from successful pre-stop counts.

| Final profile / scrape schedule | Achieved records/s | CPU seconds | Observed RSS maximum MB |
| --- | --- | --- | --- |
| ruby-ordinary | 16022 | 6.58 | 38.17 |
| rust-ordinary-r1 | 70365 | 0.62 | 7.68 |
| rust-oom-r1 | 36067 | 2.03 | 8.14 |
| ruby-oom | 4107 | 24.41 | 39.09 |
| rust-ordinary-r2 | 49850 | 0.51 | 7.68 |
| rust-oom-r2 | 35602 | 2.02 | 7.94 |
| rust-ordinary-noscrape-1 | 68059 | 0.82 | 7.75 |
| rust-oom-noscrape-1 | 38867 | 2.40 | 7.91 |
| rust-ordinary-noscrape-2 | 69826 | 0.82 | 7.62 |
| rust-oom-noscrape-2 | 34693 | 2.83 | 8.17 |

Final Rust ordinary repeats exceeded2× the fresh Ruby ordinary control; both
OOM repeats exceeded2× the fresh Ruby OOM control. These are finite drain-rate
lower bounds; they do not identify the Rust saturation point. Fresh Ruby ordinary
was16,022records/s, substantially higher than the earlier8k results, illustrating
shared-host/generator variation. Old three-pair results remain valid only for
their original artifact/input timing; the short final runs supplement them.

One-second scrape stress is more frequent than the production60s schedule.
Final ordinary scrape/no-scrape medians were60,108/68,942records/s (12.8% lower),
while OOM medians were35,834/36,780 (2.6% lower). This does **not establish** a
universal <=10% throughput impact: only two samples per condition, one ordinary
scrape run49,850 with0.51candidate CPU seconds, and shared load16–18. Lower CPU
work with slower wall time is consistent with producer/scheduling contention;
it does not prove HTTP caused the difference. No causal isolation is claimed.
The normal60s paired-consumer run independently sustained15,999records/s with
exact counts and all42responses200. No optional full-matrix rerun was added.

Rust fixed-cardinality RSS stayed7.6–8.2MB, lower than Ruby38.2–39.1MB. Later
thirds plateaued; short-run maxima are sampled RSS observations. The long normal
case additionally sampled kernel VMHWM. Old high-cardinality growth evidence
remains scoped to unchanged metrics code; it does not demonstrate a memory cap
or constitute a new final-binary high-cardinality measurement.


## Final pinned transport and deliberate loss

The sequential transport/lifecycle batch exited0 in about100s, with no source,
build, fetch or parallel candidate. Pinned rsyslog8.2610.0 used disposable
loopback TCP/UDP or a private Unix socket, existing file-plus-ompipe rules and
only required path/port substitutions. Local socket injection is a local-path
fixture, not journald end-to-end coverage. Each actual exporter used corrected
faf/3hk, the67-host map,1MiB effective pipe and fixed CPU partition.

| Case | Submitted unique IDs | Archived unique IDs | Archive duplicates | Exporter workload count / final total | Result |
| --- | --- | --- | --- | --- | --- |
| tcp-below | 10000 | 10000 | 0 | 10000 workload | zero reader count gap |
| udp-below | 5000 | 5000 | 0 | 5000 workload | zero reader count gap |
| local-below | 5000 | 5000 | 0 | 5000 workload | zero reader count gap |
| tcp-useful-burst | 30000 | 30000 | 0 | 30000 workload | zero reader count gap |
| tcp-overload | 30000 | 30000 | 0 | 4921 final total | expected final-marker deadline / loss |
| udp-overload | 30000 | 26030 | 0 | 7902 final total | expected final-marker deadline / loss |
| local-overload | 30000 | 30000 | 0 | 15372 final total | expected final-marker deadline / loss |

TCP ordinary10k@2,000/s, UDP ordinary5k@500/s and private-local mixed5k@500/s
all completed with exact archive/count totals. TCP OOM30k@7,600/s with3,000record
bursts and0.1s gaps completed in3.951s with exact counts. These are the measured
useful envelopes. The offered7,600/s is twice the previously observed3,800/s
controlled Ruby OOM rate; the separately measured fresh Ruby finite OOM result
was4,107/s. No claim that7,600 is twice every observed Ruby capacity is made.

All deliberate overloads submitted30k OOM records as fast as possible and paused
the entire exporter for1s midstream, exceeding pipe storage. SIGSTOP also froze
HTTP and expiry; this measures transport outage, not independent HTTP isolation.
Their final markers were absent at15s deadlines; each failed result/status1 is
retained as expected loss evidence. The shell's overall0 means the expected
outcomes were collected, not that overloaded delivery passed. Final exporter
totals include warm-up/auxiliary records and are not unique-ID counts. UDP had
3,970 fewer archive IDs than submissions; further archive-to-exporter gaps are
visible in counters, but exact lost unique identities are unavailable.

Producer-accepted, FIFO-observed and exporter-accepted **unique-ID** stages remain
null in these shared transport fixtures. TCP send completion or UDP submission
is not rsyslog acceptance. Equal counters cannot exclude compensating duplicates
and losses; archive duplicate counts are independently zero. No competing FIFO
reader or tee was used. Rejection counters cannot quantify upstream loss or all
parseable concatenation. All seven exporter/producer children exited0 without
forced kill; overloaded registered drivers exited1 as expected and were reaped.

The operation-recipe capacity receipt uses the retained final exposition on
expected deadline failures (the success-only JSON field is absent); before/after
hashes are in `transport-recipe-adjustment.json`. Workload and reviewed driver
were unchanged. `transport-summary.json`, exact invocation JSONs, generated
rsyslog configs/logs, final exposition and samples preserve the results. A watcher
redirection-precedence mistake left the flat `transport-lifecycle.log` containing
only lifecycle output. Transport stdout remains in its native exec result; all
per-case raw JSON/stderr/rsyslog logs remain local. No rerun manufactured a log.
The utility also queried unrelated host unit names; those were irrelevant and
are excluded from quiescence evidence. The parent queried the exact registered
UUIDs instead, in `transport-lifecycle-units-final.json`.

## Producer size and positive short write

A separate producer-only FIFO had exactly one observer and no exporter reader.
Inputs164/4,065/8,165/16,450bytes produced seven wire lines, with lengths
152,4053,8085,103,8085,8141,291bytes. All four submitted sequence IDs appeared in the archive and exactly once
in the observed wire. Over-limit producer input was split into multiple output records;
this is not preservation of one original message per line. The observed largest
wire line was8141bytes, well below1MiB. This finite fixture supports the configured frame
limit for these producer shapes, not a universal maximum for arbitrary input,
escaping or a proof that every split fragment is a supported exporter message.
`size-frame-summary.json` records exact per-frame hashes/prefixes; `sizes.wire`
and its hash in `size-shortwrite.json` retain the concrete framing evidence.

With only4,096bytes free in the1MiB FIFO, strace recorded an ompipe write of
7,053bytes returning4,096; the next write returned51/51. The resulting4,147bytes
contained both sequence IDs but just one LF: the truncated first record was
joined to the next complete record. Both originals were archived independently.
This directly confirms the pinned source's unchecked positive-short-write risk.
A valid first header can leave the joined stream parseable; no complete
resynchronization/detection or upstream-loss-count claim is made. Exact write
records, wire hash/prefix/suffix and bounded strace are retained. Producer exits0,
no forced kill. No transport/queue policy was changed.

## Restart, EOF and backlog shutdown

The private TCP fixture observed initial101 records (100events plus marker),
producer stop/restart then202 total with FIFO reconnect counter2, and reader
restart resetting counters to0 before the next101. Reconnect/startup completed
within each finite5s observation deadline; exact reconnect latency was not
measured. Archive contained all300 unique event IDs. Closing a direct writer
with an incomplete tail produced exactly one incomplete rejection; reopening
then accepted the first complete record. No stale partial tail was reused.

While the exporter was SIGSTOPped, one nonblocking write queued1,048,576bytes:
6,393complete-record lower bound plus124partial-tail bytes. TERM was queued,
then CONT; process exited0 in15.87ms without forced kill. Accepted-after-signal
count is unobservable after exit. This proves prompt finite shutdown with kernel
backlog, not complete kernel/producer drain or cross-restart recovery. All
producer/reader stop dispositions were0; cleanup nulls mean the owned children
had already been joined, as the exact empty cgroups independently prove.
`restarts.json`, retained exposition and child logs preserve the result.

## Final disposition and remaining limits

V evidence collection is complete for the dispatched bounded matrix; lead owns
acceptance. Architect/lead clarified that criterion4's10% concerns normal60s
activity, not1Hz stress. Normal two-consumer service and latency at sustained
16k/s were demonstrated; isolated causal <=10% capacity impact and production
peak remain **unestablished**. The12.8% ordinary stress observation and shared
host variation are retained, not waived or labeled passed. Final finite burst
lower bounds exceeded2× fresh matched Ruby controls; sustained maximum capacity
and all-load/cross-restart losslessness were not established. High-cardinality
evidence is reused only for unchanged metric code and its original artifact.

Pinned promtool3.12.0 checked the final actual exposition after measurement:
exit3 solely for inherited literal `syslog_message_count` counter naming lint
(`_total`/`_count`), with no parse error. Baseline Ruby and old Rust had the same
lint. `promtool-final.json` preserves exact argv/output. No local tool build or
cache fetch occurred during measured batches.

Final source remains clean at`faf06c1185ad2f6d39286d2e33896a6455b7bea6`, tree
`5d3e6ed8aba81c5b43c34f92b13a5b604d24c478`; manifest/lock/driver/source hashes
are in `final-effects-and-source.json`. Original reviewed ranges, no-migration
lineage, accepted I2/C2 reviews and current exact-head CI remain unchanged in
`exporter-review.md`; V introduced no shipped change or history rewrite.

Parent independently queried all54 exact service registrations in the latest
same-session registration receipt: every MainPID0 and emptyControlGroup. Retained
active/exited and expected failed records are not running processes and were
not stopped/retired to change their display. All three final native watchers
accounted for/joined their command cells and sessions. No known candidate,
daemon, generator, sampler, timer or tool command remains. Full exact inventory
and source proof are in `final-effects-and-source.json`. The watcher's unrelated
host-unit query is not used as evidence.

Disk now93GiB available; all measurements6.0MiB, own temp recipes256KiB combined.
Driver and one-off TemporaryDirectory corpora/archives were automatically removed
after compact receipts; only small useful wire/trace/log evidence remains. The
373MiB debug target is absent. No store path, peer data, C2 retention root, global
GC or session lifecycle was touched. C2 stable retention cleanup remains the
lead's next dependency; V authorizes none. No production access, deployment,
dry activation, default integration or claim occurred. Session stays open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/>.
