# Read-only deployment verification

Current D4: **bounded live window passed, five snapshots complete; all known
verifier effects quiescent**. Actual79kk/system-145-link/cleandda/gv3 remained
healthy with exporterPID69580 and unchangedsyslog63415. All5HTTP200; natural
ingestion/filelogging continued, rejected/reconnect/body_decoded remained0.
See final D4 results below. D3 evidence remains historical for prior3hk/gsw.


## Accepted D3 window (historical)

Owner: implementer1. Status: **bounded runtime verification accepted by lead for
its demonstrated scope**. Five serial snapshots passed over241.078s, from
2026-11-11T21:08:52.774134+00:00 to 2026-11-11T21:12:53.852307+00:00. All5 HTTP requests returned200; no503
retry was needed. No synthetic messages were sent. Both optional monitor checks
were refused, and no node2 trigger was observed.

## Deployed identity and invariants

Every snapshot resolves current-system and system profile to
`/nix/store/gsw7sx6vmin2ndvz1m6rwynbssd1mjc5-nixos-system-log-26.05.20261026.718f670`.
Observed profile link: `system-144-link`. Configuration metadata is schema1, clean
`ebe9248d7f57f1cec22089d40432aa95b3b93f60`; provider is
`6ecada0a9d2f6457a11031a3a4ffc341584fb29c` under the accepted source proof.
Both feature branches remain unmerged as explicitly requested.

Exporter PID68364 remained active/running; its exact service cgroup contained
one process, the3hk Rust executable, throughout. Initial binary SHA256 matches
`f1ad1b4f65be4e4315224b8e3426603f67eb8e99a42593e8f7cfe40ddbc4062c`.
No old Puma process was present in that cgroup. Rsyslog remained active/running
with PID63415 and its original start metadata/command. Known JSONK5 has67hosts;
JSON/rsyslog/logrotate immutable identities and store hashes match the fresh
preflight at every sample. FIFO remained0640 root:syslog-exporter; stateDir
remained0750 syslog-exporter:syslog-exporter with0children.

Remote system-143-link still resolves to exactoldkgr, whose store path remains
available. Local exactkgr/clean959e/662-path recovery roots/proofs are unchanged.
Profile143 is not a local confctl NAME. The verifier did not claim or release a
machine. Lead retains claim6fda89a5-8d08-4e52-acb4-a18e4204d331 and owns any
follow-up operation.

## Observed progress

All18 legacy families/types and observed label-key contracts passed each sample.
Payload-derived program/command/container/namespace label values were filtered
in remote memory and never retained.

| Offset(s) | HTTP | Records | Known-host messages | Kernel messages | Unknown host records | Rejected |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 200 | 83,287 | 61,536 | 51,518 | 21,751 | 0 |
| 60 | 200 | 101,865 | 72,002 | 60,425 | 29,863 | 0 |
| 120 | 200 | 124,161 | 87,795 | 73,524 | 36,366 | 0 |
| 180 | 200 | 141,801 | 100,522 | 84,012 | 41,279 | 0 |
| 240 | 200 | 158,785 | 112,583 | 94,331 | 46,202 | 0 |

Over the window, bytes increased15,560,315; records75,498; known-host messages
51,047; kernel messages42,813; unknown-host records24,451. Rejections and FIFO
reconnects stayed0, capacity stayed1,048,576bytes. Unknown hosts began21,751
and ended46,202. Their origin remains unresolved; a nonzero baseline/increase
alone does not establish a new regression. No cause or missing-host identity
was inferred, and no extra production diagnostics were run.

Sampled RSS ranged6,074,368–6,991,872bytes and ended6,152,192bytes. Process CPU
advanced3.24s across the observed interval, about1.35% of one core on average.
These are sparse steady-workload observations, not a peak memory/throughput
measurement. All4 exact known archive files kept their inode and advanced size
and mtime: /var/log/messages +8,956bytes; remote/localhost/log +415,133bytes;
remote/cz.vpsfree/nodes/prg/node19/log +1,086,364bytes;
remote/cz.vpsfree/nodes/stg/node2/log +281,109bytes. Only metadata was read; no
log contents or broad log-tree scan occurred.

## Consumer and manual-alert limits

One normal strict SSH attempt to each configured monitor was refused. Mon1
refused authentication; mon2 had no known ED25519 host key under strict checking.
Both exited255. No credential discovery, host-key enrollment, setup, retry or
access workaround occurred. Both consumers' local9090 target/up API health
therefore remains unverified by D3. Existing source/two-consumer design proof
and earlier checks are not relabeled as a live two-monitor success.

Allowed node2.stg/nullptr gauge was0 at all5 samples. No trigger or expiry was
observed; no synthetic/manual alert was executed by this owner. This does not
certify a production detector event.

## Exact recipe, results and effects

The fresh installed-policy Luna/low native watcher ran once:
`python3 deployment/d3-window.py --gate-released`. The
[recipe](deployment/d3-window.py) contains exact strict SSH argv, remote stdin,
serial0/60/120/180/240schedule,30s remote/45s local snapshot bounds and the
optional exact-target monitor API calls. Initial binary hash and live HTTP
checks were read-only; the only labels retained from input metrics are the
explicitly allowed node2 alias/fqdn/type values and fixed rejection reasons.

Evidence: [filtered window](deployment/d3-window-result.json),
[compact interpretation](deployment/d3-verification-summary.json),
[watcher output](deployment/d3-watch.log),
[watcher terminal receipt](deployment/d3-watch-result.json).
Native execsession76203 is terminal; watcher cells3–6 completed, every known
SSH/sampler/child command joined, stillRunning is empty. Parent interpretation
and evidence writes are complete. No operation or uncertain effect remains
owned by D3.

The window supports sampled steady usability of the deployed exporter and file
logging. It does not establish peak performance, central FIFO losslessness or
health of inaccessible monitoring APIs. No source/docs/driver edit, commit,
build/fetch/benchmark, copy/activation/restart, GC/root/claim/merge or lifecycle
action was performed by this verifier. Existing19tests/measured3hk/input proof
is reused; queued metadata-only CI is not claimed green. Lead owns state/rollout/
review records and any recovery or follow-up. Session stays open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/>.

## C5/D4 preparation (historical gated stage)

Owner implementer1. The read-only [D4 recipe](deployment/d4-window.py) reuses
D3's five serial offsets0/60/120/180/240 and strict bounded log.int SSH. Outer
and embedded remote Python parse checks passed; no recipe command was executed.
[Gate](deployment/d4-gate.json) is FALSE and exporterPID/profile are unset.
Explicit lead SWITCH-COMPLETE supplies those values; profile number is never
inferred from local confctl NAME2026-11-12--00-30-03. Lead owns near-activation
health and every mutation; claim6fda remains lead-owned. A fresh installed-policy
Luna/low watcher will own the one bounded window only after release.

Expected system79kk/config cleandda/provider891/tree4b28 and gv3 binary SHA256
14b542eb040024f0245a645d4ec338c5bdb52b502eb8f520669f410737500bd4
are bound to accepted C4. Check one Rust cgroup process, strict current/profile,
syslog63415/start identity, immutable JSON/policy, FIFO/state/account and both
Rust144gsw and Ruby143kgr recovery metadata. Natural aggregate intake,18legacy
families/types/observed label keys, fixed diagnostics, RSS/CPU and the same4
archive-file metadata paths are observed without payloads or synthetic input.
The new unlabeled body_decoded_records counter overlaps intake; never add it to
record totals. Zero is valid and does not prove a bad-byte alert was exercised.

Actual HTTP statuses/one allowed503jitter retry remain in evidence even on
failure. Unexpected service/input/HTTP failure stops the window and reports to
lead promptly; no recovery/restart by this owner. Both monitor retries have been
removed because prior access was refused; live monitoring API coverage remains
unverified. A natural node2 gauge can be recorded, but no trigger/expiry success
is claimed without observation. Every sampler/SSH/cell is joined before final
report. Exact instantiated remote stdin is saved only on gated launch.

C5 integration preparation is also text-only during measured V3. No Nix shell,
cache fetch, worktree target, fresh fetch, roots or cleanup has started. After
explicit V3-quiescence release, the bounded fresh-default/clean-target/hook-shell
preparation uses [the command plan](c2-artifacts/c5-integration-preparation.json).
Default drift or substantive conflict is reported before repair. FF post-merge
uses the active Overcommit entrypoint; no new commit/precommit suite is created
by FF. Lead alone merges/pushes/claims/deploys. All18 recovery roots/generations
remain unchanged. No source/index change or commit occurred.

Preparation receipt: [c5-d4-recipe-preparation.json](c2-artifacts/c5-d4-recipe-preparation.json).

C5 integration preparation released after V3 quiescence and completed. Fresh
SSH fetch leaves origin/mastere91; fixed featuredda/treef56 remains clean and
FF ancestry passes. Clean detached target:
`worktrees/2026-11-10-rust-syslog-exporter/configuration-merge-target` at e91.
Required PostCheckout passed, no hook bypass/shared-config/source change.
Declared tools/Overcommit0.73 environment retained at `retained/c5-dev-env`
(store y90v3dxkpg33x4ar6vn968cdflwn5wwi-nix-shell-env). Enter it from the feature
checkout to reuse that checkout's prepared absolute .gems/.bundle; lead runs
only the ordinary git FF/push under its later claim/fresh checks. PostMerge
framework remains active; no configured PostMerge jobs or commit hooks are
introduced by FF. Exact ready state/argv: c5-integration-ready.json and
c5-target-creation.json. No merge/default push/claim or production command by I1.
Existing18 roots and all confctl generations unchanged; auxiliary dev profile
added, no cleanup. Original watcher notification was premature; recovered original
command result0/20.6285s and full log prove success without rerun. Its unavailable
transport handle is retained in c5-watcher-reconciliation.json; source effects and
parent target session94739 are settled. D4 execution gate remains FALSE.

## D4 final bounded live verification

Explicit lead SWITCH-COMPLETE released D4 after normal switch/health4of4 passed.
Fresh installed-policy Luna/low ran the prepared recipe once, exit0. Five serial
snapshots0/60/120/180/240 span2026-11-12T00:02:39.895912Z to00:06:39.871794Z;
recipe elapsed241.251s, watcher wrapper241.377s. No replacement window or extra
production diagnostic was run. The parent's t0 milestone used the existing
filtered first snapshot while utility progress delivery lagged.

Every snapshot confirms exact current AND profile79kk, system-145-link, schema1
cleandda57166bd8bb6d85a74decdd05a8810933bdecc, provider891/tree4b28 under
accepted C4 proofs. Active RustPID69580/exactgv3/start identity/single service
cgroup/account/CLI/JSON remain unchanged; initial binary SHA256 is
14b542eb040024f0245a645d4ec338c5bdb52b502eb8f520669f410737500bd4.
SyslogPID63415/startTue2026-11-10 16:57:51CET is unchanged. FIFO remains0640
root:syslog-exporter; stateDir0750 exporter:exporter with0children. Immutable
JSONK5/67host, rsyslog and logrotate identities/hashes match all5samples.
Remote oldRust144gsw and original143kgr profile/system metadata remain available;
C4 local exact closure/root recovery proofs are reused, not freshly probed.

All18 legacy family types and observed label-key contracts pass. All5HTTP replies
are200 in65.96–85.71ms; no503/retry occurred. Payload-derived label values were
filtered remotely and never retained. Only fixed diagnostics and the allowed
node2 alias/fqdn/type are saved.

| Offset(s) | HTTP | Records | Known messages | Kernel messages | Unknown hosts | Body decoded |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 200 | 50,602 | 39,296 | 30,567 | 11,306 | 0 |
| 60 | 200 | 63,131 | 48,353 | 38,245 | 14,778 | 0 |
| 120 | 200 | 78,360 | 59,712 | 47,617 | 18,648 | 0 |
| 180 | 200 | 94,942 | 72,461 | 58,053 | 22,481 | 0 |
| 240 | 200 | 108,069 | 82,054 | 66,149 | 26,015 | 0 |

Natural deltas: bytes+11,786,607; records+57,467; known messages+42,758; kernel
messages+35,582; unknown-host records+14,709. Rejected and reconnect counters
stayed0; capacity stayed1,048,576bytes. Body-decoded stayed0 and is never added
to intake totals: no repaired-body event was observed, so this window does not
prove a bad-byte alert was detected or avoided. Unknown-host identities/cause
remain unresolved; policy is unchanged and no regression is inferred from the
baseline/trend. No host autodetection or additional diagnostic was attempted.

Sampled RSS4,800,512–5,492,736bytes, final4,800,512. CPU+3.18s over the sampled
interval is approximately1.325% of one core. These sparse steady observations
are not a production peak measurement. All4 exact archive files kept their inode
and advanced size/mtime: /var/log/messages+27,068bytes, localhost/log+414,416,
node19/log+1,114,379 and node2/log+189,560. Only metadata was read.

Node2nullptr gauge stayed0 all5samples. No synthetic event or user trigger/expiry
was observed, so no production detector-event claim is made. Monitor SSH/API
checks were not retried after prior refusals; live API health remains unverified.
This window demonstrates sampled usability/intake/filelogging, not losslessness
or performance beyond the observed workload.

Exact argv, remote stdin, gate/policy and results:
[d4-window.py](deployment/d4-window.py),
[d4-remote-stdin.py](deployment/d4-remote-stdin.py),
[d4-window-result.json](deployment/d4-window-result.json),
[d4-verification-summary.json](deployment/d4-verification-summary.json),
[d4-watch.log](deployment/d4-watch.log) and
[d4-watch-result.json](deployment/d4-watch-result.json).
Source execsession60837 joined0; watcher source/report/follow-up-read cells and
all5SSH/sampler/child commands are joined. Parent interpretation/evidence writes
are complete; stillRunning is empty. No further probe/timer/operation is queued.
No deployment/copy/restart/recovery/default push/claim/root cleanup or lifecycle
action by I1. Existing18 recovery/source/candidate roots and generations stay
held, with the accepted auxiliary C5 dev environment. Lead owns integrations,
source/target lineage, machineclaim6fda retention/release and state/rollout.
C4/C5/D4 finding ownership is retained; capacity is available after delivery.
Session stays open.
