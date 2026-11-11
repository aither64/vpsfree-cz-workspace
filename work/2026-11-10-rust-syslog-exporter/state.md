---
lifecycle: active
---

# 2026-11-10-rust-syslog-exporter

## Current status

Ready, awaiting merge approval for both named repositories and separate approval
before deploying log.int. Source is published and independently reviewed; all19
release tests, CI, package/host builds and bounded final verification are accepted.
Candidate and rollback retention plus owned cleanup are complete. No code, check,
build or cleanup is running. This session has not deployed or merged anything;
it remains active and open. Performance acceptance is qualified below.

The user's boundary is: “you are not to deploy log.int without approval however.
prepare it all, but stop before deploy” and “otherwise you can implement it”.
No activation, dry activation, copy TO production or default-branch merge has run.
No machine or merge claim was acquired. No lifecycle action is authorized.

Identity was reverified after context restoration: `dev-session current`, both
DEV_SESSION markers and the thread binding agree on this slug and
`/home/aither/workspace/ai/vpsfree.cz`. Saved Full-team delegated_5 settings remain
unchanged; architect0 owns design, implementer0 exporter/V, implementer1 consumer.

## Phases

- [x] Contracts and architect-owned [design](design.md), including D2.
- [x] Complete Rust replacement and scoped Ruby/Overcommit removal.
- [x] Consumer package/service, operations guide and regression check.
- [x] Independent final reviews, direct narrow fixes and mechanical pin proof.
- [x] Corrected package release build, all 19 tests, closure/config checks.
- [x] Corrected normal confctl host build and realized closure verification.
- [x] Final release paired/periodic scrape and affected performance verification.
- [x] Remaining pinned producer/size/overflow/restart/backlog observations.
- [x] Stable retention roots and owned disposable-data cleanup; final handoff recorded.
- [ ] User-approved deployment and live verification.
- [ ] Separately approved exact-head default-branch integration.

## Repositories and exact current heads

| Repository | Base / current final feature head |
| --- | --- |
| syslog-exporter | `7c5a8e74e44a704cceb99cd05716af6800d78efd` / `faf06c1185ad2f6d39286d2e33896a6455b7bea6` |
| vpsfree-cz-configuration | `3c088a4b71881b3649441ce3c4e92c71757708e6` / `a839ccf7e7ff07ac616ad7994af33f07975bd1b5` |

Both branches are `2026-11-10-rust-syslog-exporter`, published, one coherent
replacement commit each. Worktrees are
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-10-rust-syslog-exporter/{syslog-exporter,vpsfree-cz-configuration}`.
Canonical remotes use SSH. Bare exporter local master69b0269 is stale; use the
recorded fresh origin/master7c5 baseline. Neither feature is merged or deployed.
No migrations or persistent exporter state formats are introduced. Final fresh
SSH refs confirm both exact feature heads and unchanged defaults; both trees/indexes
are clean, one commit each, full-range whitespace checks pass. Portal comparisons
were captured at these exact final heads after fetching; no integration occurred.

## Packages and meaningful transitions

Times below are approximate Nov10 UTC dispatch milestones, not active-time totals.
Do not sum overlapping packages or count dependency waits as implementation churn.

| Package / deliverable | Owner | Dependencies and status |
| --- | --- | --- |
| D: [design](design.md) | architect0 | Assigned21:00, accepted21:14; bounded R/C evidence settled interfaces, recovery and verification |
| R: [Ruby contract](ruby-contract.md) | implementer0 | Assigned21:01, accepted21:06; all18families/input/expiry/removal inventory |
| C: [consumer investigation](configuration-integration.md) | implementer1 | Assigned21:01, accepted21:08; package/service/producer graph |
| I: Rust source, fixtures, driver, checks, docs, Ruby removal | implementer0 | Assigned21:21; delivered21:52; original review and narrow fixes accepted22:05 |
| C2: consumer package/service/check/docs | implementer1 | Assigned21:21; independent work21:32, dependency wait, final75b review22:17–22:24; original builds/recovery accepted22:44 |
| V: matched release/transport evidence | implementer0 | Assigned22:39, old-artifact runs22:44; parked23:06 on real two-monitor gap; final V resumed about23:52; accepted about00:12 with explicit performance limits |
| D2: actual two-consumer HTTP boundary | architect0 | Assigned23:00, accepted23:03; max2handlers/1encoder/1s waiter |
| I2: narrow HTTP correction/tests/docs | implementer0 | Assigned23:07, delivered23:16, affected review accepted23:24 |
| C2 final pin/build refresh | implementer1 | Mechanical pin accepted23:39; package passed159.576s/19tests; normal host passed120.315s; stable retention/cleanup accepted about00:17 |

Implementers retain finding ownership. No extra package is implicitly queued.
Others have no execution package. Routine peer clarification is allowed within
these boundaries; scope, approval, acceptance and tracking stay with the lead.

## Accepted review and quick evidence

[Review record](review-packet.md) binds all exact ranges and documentation routing.
Full verbatim reports remain in [original exporter review](exporter-final-review.md),
[original consumer review](c2-final-review.md) and [current I2 review](i2-final-review.md).
Reviewer0 retained Sol/xhigh/read_only; original all-four-lane and I2 affected
lane reviews include complete-history/no-migration/consolidation conclusions.

Original Important I1 driver pacing deadline and Advisory A1 HTTP fixture coverage
were fixed in8ef and directly verified under the narrow-fix rule. I2 subsequently
changed only http.rs and two existing HTTP docs to support two actual configured
Prometheus consumers. All other tracked files and dependency/profile/driver inputs
are identical. Current19tests, rustfmt, Clippy and exact-head CI42921690945 attempt1
pass. All superseded CI runs were already terminal success; none needed cancelling.

Final C2 differs from independently reviewed75b only by provider revision/source
hash. Lead independently reconstructed the entire final tree
`514c410ea4de2e24fc4cef288eac22a359ff2465`; schema-1 proof
`c2-artifacts/lead-i2-pin-reconstruction.json` binds original/current ranges,
reviewer, source hash and no migrations. Independent I2 review explicitly permits
this mechanical consumer boundary; no redundant whole-C2 review was required.

## Final artifact evidence

Current provider faf uses source hash
`sha256-2ChtOI8cW7zKer4jbaD5b77Eut+Mf/NzsLc/Hwhy2TE=` and unchanged lock SHA256
`031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e`.
Cargo vendor staging hash is `sha256-dvnEEbDRJoHlHLj/EDXp21PYrnvx5+J1+BGYQkmN7yI=`.
Processed cargoDeps has a distinct NAR `sha256-+zkoIofB1/aV2+6AH86P1thpT3Rpt2UpLSxDGQuIDuY=`;
these are different layers, not a checksum disagreement. See
[C2 evidence](c2-evidence.md), typed identity receipt and the reusable vendor note.

Corrected package drv21lm6pl39ly86srnk28417pmdqd4invk built successfully in159.576s:
`/nix/store/3hk34i2k760dirn1xrarxqsrwrcryaj5-syslog-exporter-0.14.0`.
All19 release tests passed; version0.14.0 and --check-config on actual67hostJSON
passed. Its7path runtime closure contains no Ruby/Python. Binary SHA256
`f1ad1b4f65be4e4315224b8e3426603f67eb8e99a42593e8f7cfe40ddbc4062c`, package NAR
`sha256-Y+H0duMpY5PGDsNk9DYyO7YJXG3u8u4kwV9Y9X0md28=`.
Normal-host nc86→nw3 build passed120.315s, NAME2026-11-11--00-46-58, exact system
`/nix/store/nw3d0j9hb1mrwf7hd0daxm6gk1vcfabc-nixos-system-log-26.05.20261026.718f670`.
NAR `sha256-KknCgMIpbg2EJqGIijH1rFdiAWjtdt33n+Saj2HLemU=`. Its653path closure
contains corrected3hk, excludes Ruby exporter/gem and superseded4gb, and retains
unrelated Ruby/Python. Unit/settings/modes pass, rsyslog/logrotate paths match
production and installed revision is clean a839. All build effects ended;
`c2-artifacts/i2-build-verification-summary.json` binds outputs and checks.
Lead explicitly released final V after these receipts; no new production access.

## Verification boundary and observed learning

[Verification](verification.md) owns exact recipes/results and old/new scope.
Historical8ef/75b package4gb and host3vv are superseded and not deployable final
identities. Three ordinary and three OOM matched100k pairs preserved1.2Mcounts;
median rates were Ruby8465/Rust65769 per second ordinary and3997/35873 OOM
(7.77x/8.98x). Shared AMD7551 host and Python generator limit inference; these
numbers describe8ef, not the corrected full binary or production peak capacity.
Fixed-cardinality RSS plateaued about37–39MB Ruby and7.6–8.1MB Rust. High-cardinality
labels grew RSS, confirming no total-memory cap. Promtool found only inherited
legacy naming lints in both applications, no exposition parse errors.

Observer concern `normal-scrape-evidence-gap` CLOSED by final faf/3hk release
measurement:1,040,000 accepted records,42 paired and periodic HTTP responses200,
zero503/errors, max6.76ms and reader-stage gap0. Exact registered unit
7210bbf6-46dd-4b9b-aa98-57903c6e3394 exited0, MainPID0/empty cgroup; all watcher
command effects ended. Original old60s collision, isolated62.5s result and
7/40paired503 evidence remain retained. Source tests/review alone did not close it.
Final comparison batch passed all10x100k ordinary/OOM scrape/no-scrape/freshRuby
control cases with countgap0 in about93.5s; all command/native effects ended.
Final finite ordinary rates70365/49850 per second versus freshRuby16022; OOM
36067/35602 versusRuby4107. RSS about7.6–8.2MB versus38–39MB. These are100k burst
observations, distinct from the demonstrated sustained16k/s/65s envelope.
One-Hz stress comparison ordinary60108 vs68942(no scrape),12.8% difference, and
OOM35834 vs36780,2.6%; shared-host/generator noise and two samples do not establish
causality. Architect clarified criterion4 applies NORMAL60s activity. Lead accepts
measured-envelope preparation, conditional on remaining transport gates: normal
service/latency demonstrated, isolated causal<=10%capacity-impact subclaim and
production-peak capacity UNESTABLISHED. No unqualified full-design certification
or retroactive threshold change is claimed, and no additional matrix is needed. Remaining pinned transport/size/short-write/restart/backlog observations completed.
Four useful fixtures had exact archive/reader counts:TCP10k@2k/s,UDP5k@500/s,
private-local mixed5k@500/s,TCP30k OOM@7600/s with3kbursts/0.1sgaps. Deliberate
30k/pause1s overloads lost final markers and hit15s deadlines; archiveunique totals
TCP30000/UDP26030/local30000, exporter totals4921/7902/15372 include warmups.
These are retained LOSS observations, not passing no-loss tests. Stages not
individually observable remain unknown. Pinned ompipe reproduced7053→4096 then
51→51 writes:2sequenceIDs but1LF in joined wire. Size16450input split to7wire lines,
max8141bytes, supporting the sampled framing bound without a universal claim.
Reconnect/reset/partialEOF/backlogTERM cases passed (TERM15.87ms; reconnect within5s, exact latency unmeasured); post-exit
backlog drain is unobservable. All54registeredunit MainPIDs/cgroups are empty,
expected overloadexit1 preserved, other caseexit0, all3nativewatchers joined.
Final V packet accepted about00:12UTC after complete report/receipt reconciliation;
no new check or background measurement is pending.

Pinned rsyslog source proves nonblocking ompipe, EAGAIN suspension and unchecked
positive short writes. Faster parsing cannot recover upstream loss or restart
gaps. Metric series/caches remain retained without a total-cardinality bound.
No source review or finite replay establishes production losslessness.

## Recovery and operations

[Rollout](rollout.md) records the exact final candidate and later approval boundary;
[C2 evidence](c2-evidence.md) retains full source/input/build/closure history.
Actual production is clean config959e1d54cabc7ac5530dac6179acacb077a57754,
profile143, system
`/nix/store/kgrfplplhrhhj4idvzx172lqh4hiyimq-nixos-system-log-26.05.20261026.718f670`.
Its complete662path closure, clean source and locked graph are locally retained.
Seven missing paths156824bytes were pulled read-only FROM production; exact NAR
and path-set checks passed. No candidate was sent TO production. Profile143 is
not a confctl local build NAME; recovery uses the exact retained store closure.
No further production query or pull is required for current preparation.

The67host JSON/FIFO/account/9102/alerts remain unchanged. Production rsyslog and
logrotate output paths were identical to the historical candidate; final build
corroborated its own identities. Intervening DNS/status commits do not select
unrelated logger inputs. Retain one FIFO reader, replace package+launcher together,
and preserve reset/loss/rollback limits in the reusable configuration operations
guide. Live usability verification waits for separately approved deployment.

## Resource retention and cleanup

User requested disk monitoring and own disposable-data cleanup. Latest corrected
build start:92GiB free,91% used. No duplicate Cargo release build. First owned403MiB
debug target was removed after proven quiescence; I2 target373MiB was also removed after final19test/review/C2 quiescence and an
owned process-reference check, before final measurement. V must not overlap cleanup or new fetch/build IO.
V and C2 are quiescent. All10 stable ordinary indirect roots are under
`retained/`; root targets and local validity were proved before removing20
redundant OWN temporary root symlinks. Candidate653/rollback662 sets match saved
receipts and every path is locally valid, normal4075path derivation graph valid.
Final confctl NAME/links are unchanged. Removed12 owned unused drafts/tar/extracts,
12468223logical/12496896allocated bytes; own C2tmp now344064allocated bytes.
Final free space99495776256bytes (91%used); shared free-space movement is not
attributed to this session. Raw measurements6MiB and Vrecipes256KiB retained.
Stable root map is in [rollout](rollout.md); compact receipt
`c2-artifacts/stable-retention-cleanup.json` records exact targets/effects. Optional
same-UID /proc scan stopped on unreadable cwd; authoritative prior exact-unit and
watcher quiescence proofs were reused, no complete process scan is claimed. No global
GC, store-path deletion, peer cleanup or session lifecycle action is permitted.

A shared hooksPath mistake was corrected by removing only I0's override; common
Overcommit hook remains unchanged. Its previous key value was not captured, so
no claim is made that an older custom setting could not have been overwritten.
Rust commits use an active command-scoped own hooksPath; no hook bypass occurred.

Initial substantive tracking commit12072e153 preceded project commits. Shared
workspace has unrelated dirty paths; preserve them/index and stage only owned
records under the normal consolidated checkpoint cadence.

## Next

User decides whether to approve integration of syslog-exporter/master and
vpsfree-cz-configuration/master, and separately deployment of the prepared logger
candidate. No further operation is authorized by this handoff. Recheck fresh
source/target/candidate/production identities and required coordination procedures
at any later approved integration or deployment; retain one FIFO reader and the
exact prior system. Live usability checks remain part of that future operation.
Do not archive, delete or stop the session.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/).
