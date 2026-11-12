---
lifecycle: archived
---

# 2026-11-10-rust-syslog-exporter

## Current status

**Current user direction C — merged and verified; session remains open.**
The simple custom updater is complete on published, clean source
`b9b9cfea4331ff28bd883f1ed7415af6f27cd5f7`, tree
`a1d826ecdbf019600ee63f74e74c385b00902a7c`. It follows the existing vpsf-status
pattern: one weekly/manual job, compatible Cargo.lock update, fresh audit,
sandboxed shared release checks, official github-actions bot commit and ordinary
push. No Dependabot/PR/ruleset/PAT, consumer pin or deployment changes.

[Independent RC review](custom-updater-final-review.md) and both precise lead
bindings close the only Important finding and the first hosted packaging error.
Exact-head [Rust CI43216044595](https://github.com/vpsfreecz/syslog-exporter/actions/runs/43216044595)
passed with effective sandbox=true/fallback=false, actual9workflow/Git fixtures,
fmt/Clippy and25release Rust tests. Final raw/compact evidence is in
logs/c-hosted-validation.json and c-final-effects.json. All current effects are
joined; the unused owned debug target was removed (391,041,024allocated bytes),
without store/peer/required-root cleanup. The observer's enclosing-shell logout
error is disclosed separately from the actual successful watch/run.

Complete891..b9 is useful F99ff plus one coherent custom-updater C commit.
Rejected unmerged B is consolidated out, with original keeprefs/reviews/CI kept
as history. Runtime, Cargo.lock/toolchain/flake.lock/developer-hook inputs and
current deployment remain unchanged; no migrations. All18recovery roots and
branches/worktrees/confctl generations remain retained. Old B activation payloads
are explicitly superseded and must not be executed.

User approved initial `syslog-exporter/master` integration with "ok, merge it".
The declared-shell fast-forward and ordinary SSH push completed at 2026-11-12
14:34 UTC: remote master and retained feature both equal exact b9b9cfea. Short
repository claim `5d6cf0ad-cd34-4c27-a349-ce77a47891e3` was released and verified
before CI or further records. The shell session4340 exited0. Exact commands,
remote refs and effects are in logs/c-integration-result.json. No hooks were
bypassed; this FF creates no commit and invokes no precommit hook.

Master Rust CI43238628054 and manual updater dry-run43238754813 both passed
(attempt1, exact b9). The updater actually resolved errno0.3.14→0.3.15, audited
candidate lock c417e3ec against fresh RustSec af7b3ec3 and ran mandatory
sandbox=true/fallback=false release checks:9shell/Git fixtures,25Rust tests,
fmt/Clippy. Its explicit DRY_RUN=true log ends “Validation complete; no commit
or push.” Push was skipped; remote master/feature remain b9. No dependency
update was published. The weekly job is active (Monday04:23UTC), with manual
invocation available. Actual authenticated bot push is not tested by dry-run.

Evidence: logs/c-master-validation-summary.json, complete c-master-{dry-run,rust}
logs/metadata and c-integration-result.json. Watcher transport failed to save
its report despite completed observations; lead independently verified GitHub,
raw logs and native transcript. Both watcher sessions11219/29480 exited0, every
call returned, native turn completed, and exact external-effects resolution
was accepted. No rerun or lifecycle action. No known remaining work/effects or
merge blockers. All existing recovery roots, branches and worktrees remain;
production891/79kk is unchanged. Session lifecycle remains active/open.

### Historical F preparation (integrated by C above)

**Current follow-up F:** user requests replacing exporter shell.nix with a
flake.nix development shell and nix develop commands. I0 delivered the bounded tooling migration as new commit
`99ffea73005685fc9f198dda3402fe24660ee944`, tree
`3dd3e3330c1b2fcaf9585d77c6a2fb04314c9c1c`, parent merged891. It preserves
nixpkgs718f/Rust1.95/tools, adds a generated two-node lock and README nix develop
commands, and removes shell.nix. Both Linux shells evaluated; the local shell
and full25tests/fmt/Clippy/active hook passed. Exact-head CI43180133253 succeeded.
RF independent affected review is accepted with no findings; all four lanes,
whole one-commit history/no migrations and documentation conclusions are in
[flake final review](flake-final-review.md). I0 removed only the owned target after exact owner/reference/quiescence proof:
391,110,656allocated bytes/384,495,938apparent bytes; absence verified. Accessible
references were0; protected unrelated metadata was unavailable, with no universal
process-visibility claim or repeated sudo attempt. Ready, awaiting merge approval
for this new follow-up; no deployment/consumer pin is required. No runtime,
configuration consumer, production probe/deployment or current recovery changes.
Committed quick-pass F passed retained reviewer0 affected final review.
Fresh default integration is not yet authorized for this new follow-up.

Prior delivery below is complete and remains historical deployment evidence;
F reopens development-tooling work only. The session remains active/open.

The compatibility fixes are implemented, reviewed, tested, deployed and merged.
The essential exporter is running and consuming records on log.int. No prior implementation, integration, deployment or verification package remains;
F+B tooling/automation is ready and awaits initial integration/settings approval.
The session remains open; no archive/delete/stop/hold or lifecycle command was
requested or run. The anchored lifecycle remains active for follow-up.

Exact remote master and retained feature heads:

- syslog-exporter: `891db6b82ccd37e985507c654050143e165041a7`, tree `4b28b6924e042ebf7582b9a0a91eea0bbbddc429`.
- vpsfree-cz-configuration: `dda57166bd8bb6d85a74decdd05a8810933bdecc`, tree `f56d93d060cc9e0e44917a32452d8a9c3bccbab9`.

Actual deployed system is `/nix/store/79kkfqwr8mc82g5si9ifzkl9ygaqys5r-nixos-system-log-26.05.20261026.718f670`,
profile `system-145-link`, clean source dda; normal confctl NAME
`2026-11-12--00-30-03`. Rust PID69580 runs exact gv3 package, binary SHA256
`14b542eb040024f0245a645d4ec338c5bdb52b502eb8f520669f410737500bd4`.
Rsyslog PID63415/startNov10 did not change. Only the exporter restarted;
copy/dry/switch and four health checks passed. All lead source sessions and
managed observers joined. [Rollout](rollout.md) owns exact identities/commands,
source/input/closure/NAR graphs and retained recovery paths.

D4 verified five snapshots over240s: HTTP5/5=200, no503/retry; natural intake
+57,467records/+11,786,607bytes, knownmessages+42,758 and kernel+35,582.
Rejected/reconnect/body-decoded counters stayed0; capacity1MiB. RSS4.80–5.49MB,
CPU+3.18s, one stable Rust process, same settings/FIFO/account/policy and four
known archive files advanced by metadata. Node2 nullptr0 is not a trigger test;
no production synthetic messages were injected. Monitor APIs remain unverified
because prior access was refused; no credential/key workaround or retry occurred.
Full evidence: [deployment verification](deployment-verification.md),
`deployment/d4-verification-summary.json`.

D7 restores Ruby ASCII/strip/colon semantics and allows invalid UTF8 bodies to
retain intact ASCII alert signatures while validating actual headers strictly.
Standard U+FFFD replacement does not join interrupted signatures; body-label
coalescence is documented. All25 local and Nix release tests, fmt/Clippy/hooks
passed. [R3 final independent review](r3-final-review.md) found no findings across
all four lanes and independently assessed complete single-commit history/no
migrations. Current feature CI43116296064 passed; fresh post-merge master
CI43124385181 also completed SUCCESS on exact891. The old6ec provider queue/
cancellation contradiction remains historical evidence, not a final-head failure
or active wait.

V3 on the exact final Nix binary passed17paired Ruby/Rust cases plus the explicit
replacement-label policy case;12matched100k replays all counted exactly.
Ordinary medians Ruby8502/Rust66435records/s (7.81x); OOM3963/32313 (8.15x).
RSS Ruby36.96–38.20MB/Rust7.53–8.18MB. A65s16k/s run counted1.04M exactly and
all42two-consumer requests returned200, maximum6.627ms. These are finite shared-
host/generator-limited results, not peak production capacity or causal<=10%
normal-scrape certification. [Verification](verification.md) retains bounds,
original transport-loss observations and exact result/effect receipts.

Both approved FF integrations used separate short repository claims, prepared
Nix environments and active required hooks. Fresh remote refs/ancestry equal
both final deployed heads. Each repo claim was released before records/CI.
Machine6fda was released at00:09:39Z after D4 and complete integrated deployed
lineage proof, then authoritative released/revision2 state was verified. No
resource remains held by these deliveries. A later deployment needs fresh
ownership. See `deployment/{exporter-integration,configuration-integration,
final-deployed-lineage,machine-release}.json`.

Current79kk/gv3 sources and immediate prior Rustgsw/3hk plus original Rubykgr/w7
recovery remain protected under18owned roots. Branches/worktrees and all confctl
generations remain retained. All disposable Cargo targets were removed after
quiescence/reference checks; C6 removed only the unused two C5 env-profile
symlinks (74textbytes/0allocateddata), preserving all18valid targets. No store
paths, peer data, globalGC or lifecycle state were removed. Current proof in
`c2-artifacts/c5-integration-preparation.json` and C2 evidence.

The user explicitly approved both master merges ("okay then, merge it") and
then authorized the fixes and essential-service continuity. Earlier keep-unmerged
instruction is superseded for these actions. Original deployed6ec/ebe ranges,
protected refs, reviews and recovery are preserved; they are sibling predecessors,
not claimed literal ancestors of the substantively corrected and actually
redeployed891/dda heads. No migrations or persisted exporter-state conversion.

Stable portal: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/>.

B rule inspection clarification accepted: legacy branch-protection GET requires
Administration(read), unavailable to GITHUB_TOKEN. Bootstrap one active master
repository ruleset; runtime uses Metadata(read) effective-rule/ruleset APIs for
strict app-bound aggregate and linear history. Lead sets/verifies no bypass actors
with administrative authority. Runtime omission of bypass_actors is documented
redaction, not proof of an empty list; visible nonempty actors are refused.
No new credential or settings mutation occurred.

## Current package table

| Package | Owner | Status | Next |
| --- | --- | --- | --- |
| C design | architect0 | Accepted; reference-based single job and trusted setup/sandbox boundary | Retains clarification ownership |
| F+C source/checks | implementer0 | Accepted b9b9cfea; clean/published, local hooks and final hosted release passed | Retains findings; no new package |
| C final review | reviewer0 | Complete on0b313; RC-I1 closed on a455, exact entry fix bound on b9 | Original report and both narrow receipts retained |
| Owned target cleanup | implementer0 | Accepted; absence verified and all effects ended | No further cleanup queued |
| Initial integration | lead | Clean891 target/FF/hooks/shell/commands prepared; user approval pending | Approve source merge into syslog-exporter/master |
| Live updater dry run | lead | Not started; depends on approved initial integration | Exact master dry_run, no publication |

Earlier A/B packages and their retired preparation remain historical below and
in linked reports. No rejected B source/settings action is pending.

## Phases

- [x] B sufficient revised design accepted; I0 source package released.
- [x] B1 locally committed5e3a5f38 and quick/mandatory-hook checks passed.
- [x] B independent final review complete; no Blocking/Important, one accepted narrow Advisory.
- [x] B exact-final-head feature full validation and owned target cleanup accepted.
- [x] Rejected B initial integration/settings plan superseded without execution.
- [x] C concise reference-based design accepted and I0 source release.
- [x] C committed quick-pass replacement0b3131ff, no publication before review.
- [x] C affected final review/precise fixes and exact-head sandboxed release CI passed.
- [x] C final evidence and owned target cleanup accepted; all current effects ended.
- [ ] Initial F+C master integration approval, then actual updater dry run.
- [ ] Initial F+C integration approval/readiness.

- [x] F flake development shell, committed quick checks/CI, affected final review.
- [x] F owned debug-target cleanup; all known source/check effects ended.
- [ ] Separate merge approval for follow-up F (ready99ffea73; master still891).
- [x] Contracts and architect-owned [design](design.md), including D2.
- [x] Complete Rust replacement and scoped Ruby/Overcommit removal.
- [x] Consumer package/service, operations guide and regression check.
- [x] Independent final reviews, direct narrow fixes and mechanical pin proof.
- [x] Corrected package release build, all 19 tests, closure/config checks.
- [x] Corrected normal confctl host build and realized closure verification.
- [x] Final release paired/periodic scrape and affected performance verification.
- [x] Remaining pinned producer/size/overflow/restart/backlog observations.
- [x] Stable retention roots and owned disposable-data cleanup; final handoff recorded.
- [x] Measured comparison in commit message, successor pin/provenance and manual-test instructions.
- [x] Corrected-head CI43116296064 succeeded on891db6b8; predecessor cancellation provider contradiction retained.
- [x] User-approved log.int switch and initial running-binary verification.
- [x] D3 live241s ingestion/scrape verification, with inaccessible monitor APIs explicit.
- [x] D7/I3 encoding and ASCII-compatibility corrections, quick checks/CI and R3 affected final review.
- [x] C4 final pin/rebase and exact package/host build with25release checks.
- [x] V3 focused corrected-release parity/performance/two-consumer verification.
- [x] Corrected log.int activation and D4 essential-service/live-file verification.
- [x] Approved exact-final-head integration of both projects and verified machine release.
- [x] Owned auxiliary-profile cleanup; all18 required roots valid, session left open.

## Repositories and exact current heads

| Repository | Base / current final feature head |
| --- | --- |
| syslog-exporter | `7c5a8e74e44a704cceb99cd05716af6800d78efd` / `891db6b82ccd37e985507c654050143e165041a7` |
| vpsfree-cz-configuration | `e91c8d21055b7110182fd4c531389947f180e359` / `dda57166bd8bb6d85a74decdd05a8810933bdecc` (deployed predecessor `ebe9248d7f57f1cec22089d40432aa95b3b93f60`) |

Both retained feature branches are `2026-11-10-rust-syslog-exporter`, each one
coherent commit with no migrations; exact final heads are now remote master too.
Feature worktrees remain under the dated worktree group. Canonical remotes use
SSH. Exporter base7c5 and final config basee91 are independently reviewed/bound;
original config base3c, old deployedebe/6ec and all intermediate review ranges
remain provenance. No merged/default history was rewritten. Final deployed
79kk/profile145 selects exactly891/dda. Machine and repo claims are released.

## Packages and meaningful transitions

Initial package times below are approximate Nov10UTC; M/C3/D3 are Nov11UTC.
They are dispatch milestones, not active-time totals.
Do not sum overlapping packages or count dependency waits as implementation churn.

| Package / deliverable | Owner | Dependencies and status |
| --- | --- | --- |
| A: custom bot lock-update design | architect0 | Executing bounded design: monthly no-PR verified lock-only bot commits; sufficient brief before implementation. |
| F: flake development shell | implementer0 | Accepted/ready for merge approval: published99ffea73,4paths54+/7-, both Linux shells evaluated, native nix develop and25tests/hooks/CI passed; RF no findings; own target391MB removed and known effects ended. |
| RF: affected tooling/docs final review | reviewer0 | Accepted/no findings891..99ffea73, saved Sol/xhigh/read_only; all4lanes/history/no migrations; flake-final-review.md. |
| D7: bounded compatibility correction brief | architect0 | Accepted about22:44Z; strict headers, borrowed/replacement-decoded body, ASCII/LXC parity, continuity/recovery settled |
| I3: provider encoding/ASCII parity correction | implementer0 | Ready for acceptance: published891db6b8/tree4b28, six focused+full25tests/fmt/Clippy/active hook pass. Main prose pass complete; finding ownership retained. |
| R3: affected independent final review | reviewer0 | Accepted/no findings, full7c5..891db6b8 / affected6ec..891db6b8, high risk/all4lanes; full report r3-final-review.md. |
| C4: dependent configuration/readiness | implementer1 | Accepted; package gv3 all25release tests172.706s and host79kk120.117s passed; NAME2026-11-12--00-30-03; full source/input/NAR/closure/unit/policy/18root/effect proofs c4-prepared-summary.json. |
| V3: focused corrected-release evidence | implementer0 | Accepted;17paired+policy,12exact matchedcases,1.04M/42HTTP200; finite medians7.81x/8.15x, all20unitsMainPID0/emptycgroup. PATH pre-app failure/correction retained. |
| C5/D4: integration readiness and live verification | implementer1 | Accepted; clean env/target preparation and five healthy live snapshots00:02:39–00:06:39Z, source60837/watchers/SSH ended. |
| M4: final exporter merge readiness | implementer0 | Accepted/used; exact891 target, active scoped hooks and Nix1.95 env; source FF/push/proof and claim release complete. |
| C6: unused auxiliary env cleanup | implementer1 | Accepted; only two own C5 profile symlinks removed; all18 required roots valid; no known effects. |
| D: [design](design.md) | architect0 | Assigned21:00, accepted21:14; bounded R/C evidence settled interfaces, recovery and verification |
| R: [Ruby contract](ruby-contract.md) | implementer0 | Assigned21:01, accepted21:06; all18families/input/expiry/removal inventory |
| C: [consumer investigation](configuration-integration.md) | implementer1 | Assigned21:01, accepted21:08; package/service/producer graph |
| I: Rust source, fixtures, driver, checks, docs, Ruby removal | implementer0 | Assigned21:21; delivered21:52; original review and narrow fixes accepted22:05 |
| C2: consumer package/service/check/docs | implementer1 | Assigned21:21; independent work21:32, dependency wait, final75b review22:17–22:24; original builds/recovery accepted22:44 |
| V: matched release/transport evidence | implementer0 | Assigned22:39, old-artifact runs22:44; parked23:06 on real two-monitor gap; final V resumed about23:52; accepted about00:12 with explicit performance limits |
| D2: actual two-consumer HTTP boundary | architect0 | Assigned23:00, accepted23:03; max2handlers/1encoder/1s waiter |
| I2: narrow HTTP correction/tests/docs | implementer0 | Assigned23:07, delivered23:16, affected review accepted23:24 |
| C2 final pin/build refresh | implementer1 | Mechanical pin accepted23:39; package passed159.576s/19tests; normal host passed120.315s; stable retention/cleanup accepted about00:17 |
| M: measured comparison in exporter commit message | implementer0 | User follow-up Nov11; message-only amend, complete-tree identity, scoped hook/CI |
| C3: dependent mechanical pin/provenance refresh | implementer1 | M published head; exact source/package reuse proof, updated normal-host metadata; no production test |

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

## Historical pre-I3 artifact evidence

Prior provider faf uses source hash
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

CI resource wait checkpoint: exact run43096574664/attempt1/head6ec remained
queued after about60min, jobs0/no conclusion. Existing readonlyobserver83998 is
retained, no retry/cancel/quiettimeout. Local work/cleanup is accepted. Lead
requested further reports only on actual scheduling/outcome/effect changes,
not unchanged periodic checkpoints. This does not stop any session or utility.

## Next

The user can run the supplied node2 alert command. Both branches stay unmerged
for bug fixes as requested. M's exact metadata-head CI remains queued externally,
with read-only watcher83998 owned byI0; no new green run is claimed. All local
checks, immutable release inputs, host builds, activation and D3 bounded live
verification are accepted. D3 could not access either monitor API (strictSSH
mon1 authentication refusal, mon2 unknown host key); no credentials/trust setup
or further probe is authorized. The node2nullptr gauge was0 in the sampled
window; no trigger/expiry was observed and none was injected by this session.

All known deployment/D3 commands and observers are joined; M's remote CI observer
is the sole continuing read-only operation. M target cleanup is complete: actual
390914048allocated/384313103apparent bytes removed, no path remains, no active
references in its bounded owned-UID check. Machine claim6fda remainsheld because
user explicitly keeps deployed lineage unmerged; no release or merge action.
Preserve exact old143/kgr rollback closure and currentgsw/source inputs. Do not
archive/delete/stop the session. Any finding returns to its owner and applicable
checks/review. Current records remain in the working tree under normal tracking
cadence; prior Nov11 checkpoint2050b47b0 is not rewritten.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/).

### B1 first milestone

I0 reports focused actionlint/Python/actual inline metadata-policy tests and Nix
package derivation evaluation passed in23.15s. Python3 tests and Node2eligible+
40refusal cases cover actual policy rather than only a duplicate model. Official
upstream action refs and observed GitHub Actions15368/Dependabot49699333 identities
are captured in owner evidence. No long release/audit/performance run, feature
publication or setting/default/production mutation. All focused cells joined.

### B1 mandatory-hook fixture failure and owned recovery

Standalone full quick suite passed103s. The actual commit hook then exposed Git
environment leakage into a disposable Git fixture: inherited GIT_* settings let
fixture git add touch the own source index and run its hook from the temporary
cwd. Source files/HEAD99ff remained intact; no commit/push occurred and all
commands ended. I0 owns clearing Git environment only for disposable fixtures,
reconstructing the explicit intended B index from saved clean99ff/native isolated
index, then focused actual-hook-context verification and the real mandatory hook.
This is a diagnosed fixture correction, not a product failure or hook bypass.
No broad reset/clean/stash, publication, setting/default or production action.

### RB final independent review dispatched

Complete891..5e3a5f38 is F99ff plus coherent B; treef86bdb46,16paths866+/22-.
B is locally committed and clean, unpublished by design until final review.
Final mandatory hook passed25Rust+policy/fmt/Clippy/workflow lint in8.35s after
focused inherited-Git recovery proof7.87s. Full standalone quick suite103s and
focused23.15s evidence retained; runtime/manifest/lock/toolchain/flakelock same.
RB assigned retained reviewer0 (Sol/xhigh/read_only), HIGH authority/credential
risk, all four lanes; exact complete/affected series, no migrations, useful F
split, docs routing and Git incident included. Long Nix/audit/replay remains
held; no external settings/default/production mutation. Bootstrap approval still
separate from requested future routine Dependabot PR merge authority.

RB assignment first twice refused with the public session-command-lock error;
no submission was claimed. Same exact message/UUID was retried after the lock
cleared and accepted as native turn01a1cf37-d1c7-7e32-aabf-7c1f4f8083e6.
No lock/private helper/lifecycle intervention. Public status is unavailable
(unknown subcommand); normal list and exact same-session process check were
read-only. Review is now executing; no duplicate review thread was created.

### RB accepted; narrow Advisory reduction

[Original RB report](dependabot-final-review.md) is persisted verbatim with
complete891..5e3/affected99ff..5e3, reviewer0 Sol/xhigh/read_only, HIGH risk/all
four lanes. No Blocking or Important findings; independently complete useful
F+B history/no migrations/no redundant input stream and sound docs preservation.
Actual public Dependabot run/check/head/suite/App shape and official CLI expected
head semantics were checked. No live token/bootstrap or long-check certification.

RB-A1 duplicates full expensive maintenance on Dependabot branch push and PR;
lead accepted exact reduction and released I0: push.branches-ignore dependabot/**
plus one owning-page factual sentence, preserve every PR/aggregate/manual/own
feature bootstrap. Main prose/fidelity pass accepted unchanged. Source amendment
and focused mandatory-hook proof precede lead's direct narrow-fix binding; no
new design or unaffected review rerun. Publication/long CI still held. Initial
integration/settings remains unapproved and unexecuted; current production
runtime891/configdda is unchanged.

### RB-A1 bound and long feature validation released

Final B f38277bb96ee2814b6fd7179fdc5facf0e609e5b, tree096e00e6c79956660e1a5c43874cd9909614f90b,
retains F99ff parent/message and all other blobs. Lead independently rebuilt
whole tree from reviewed5e3 plus only accepted YAML trigger/doc sentence in a
native isolated index; source logical state clean, no migrations. Focused
18.94s and final active hook17.71s pass full25Rust+policy/lint; actual sessions
joined. Original review binds5e3, exact narrow-fix receipt bindsf382; no scope/
design expansion or unaffected review rerun. logs/b-lead-narrow-fix.json.

I0 released one complete dependent feature SSH publication + exact-head full
read-only CI phase, fresh Luna watcher, no extra local release duplicate. Must
verify full selected jobs, actual Nix sandbox/releases/tests, fresh RustSec and
12matched cases/75% medians/65s pairedHTTP; disclose identical initial locks as
harness validation rather than real update proof. First failure requires logs/
bounded diagnosis, no blind rerun. No initial default/settings/PR/deployment or
claim action is authorized by this phase. Runtime and recovery unchanged.

### B feature publication and hosted validation

Exact finalf38277bb96ee2814b6fd7179fdc5facf0e609e5b/tree096e00e6 published by
ordinary SSH feature push0 (11.34s), fresh remote featuref382/master891 and
891..f382 portal comparison proven. Rust43200250554 attempt1 exactf382 began:
scope success, quick in progress at owner report. Fresh Luna/low b_hosted_full
owns one read-only CI observation; no root duplicate polling/local release.
Feature source/base/head and original/candidate locks are identical, so this
is harness validation, not a real dependency-update/live-auto-merge claim.

Exact initial ruleset/settings payloads and approval-bound plan prepared at
logs/b-bootstrap-{ruleset,settings,plan}.json, not executed. Required aggregate
Rust required/App15368, strict master-only named repository ruleset, linear and
no admin bypass; enabling only allow_auto_merge after squash availability check.
All external settings/default/PR actions remain unexecuted; no repository or
machine claim acquired. Current runtime/configuration/recovery unchanged.

### B hosted terminal success and independent preparation

I0 terminal checkpoint: Rust43200250554/attempt1/exactf382 SUCCESS; actual jobs
scope131121473558, quick131121548932, maintenance131122377577 and aggregate
131124068531 allsuccess, scope full=true. Watcher exit0/225s, every owned cell/
session joined. Exact audit/Nix/replay receipts are being reconciled from full
completed raw logs, no rerun or duplicate local release. Initial normal receipt
shows1,062,360 exact records/two successfulscrapes/noerror, final details pending.

I1 capacity reconfirmed after acceptedC6 and released B-M independently: same
session exact detached exporter merge target/fresh SSH default891+featuref382,
declared nix develop env/hooks/FF command preparation only. No source/index/
feature ref mutation; source heldfixed until short common-Git setup ends. Hosted
CI is independent of local env realization. No claim/merge/settings/production
or cleanup authorized by preparation. Initial approval still pending final
concrete result; all18 recovery roots/generations preserved.

### B1 final acceptance

Final I0 delivery accepted: sourcef382/tree096, full4job CI43200250554 success,
all effects joined. Fresh RustSec5fe96cf51fde2fd4e749d51ac8bdc59edbdce77b audit0;
sandbox true and fresh checked release drvwlrzbyfvphabk0fg9dkdjyii4zls425q ->
outputk4gycczcp70s538n37c9ww372qgyb96v. Both labels same source/lock/output:
harness validation only. doCheck/release/known25suite contract enforced by fresh
successful build; individual release-test count lines were not streamed. Quick
job directly records25tests; no duplicate build/rerun to repair log retention.

12alternating100k cases exact/gap0/exit0/no forced/error; ordinary median ratio
106.58%, OOM97.74%, above75% coarse gate. Samebinary variation is shared host/
generator noise. Fixture3hosts/cardinality1/seed20261110/1MiB, no periodic stress.
65.001s at16,344/s:1,062,360 exact/gap0, pair200 at1.068/1.098ms, no third-marker
request overlap, CPU3.74s/RSS7.041MB. Not production capacity/tail/unique-delivery
proof or actual dependency update/live merge. logs/b-hosted-validation.json,
b-hosted-maintenance-summary.json, b-hosted-cases.json and full raw CI retained.

Owned debugtarget removed after exact UID/device/inode/path/marker and scoped
reference/quiescence proof:391,102,464allocated/384,495,937apparent bytes,
absence verified; protected unrelated metadata unavailable, disclosed/no sudo.
Free102,154,268,672bytes, no shared-space attribution. All18roots, branches,
worktrees/source/evidence/recovery preserved. I0 accepted/quiescent, no newpackage
queued; only initial integration/settings activation and first-live-PR proof
remain unexecuted/approval-bound. Session staysopen/active.

### B-M final acceptance and current handoff

I1 preparation accepted: exact freshSSHmaster891/featuref382/tree096, clean owned
detached target891, native FF proof and measured source/target index identities,
common config/hooks unchanged. CompleteF+B history and no-migration binding
included. Declared718f/Ee5 environment resolves9tools; six toolversioncommands0.
Utility extra Node24.14 assertion caused original outerexit1; actual24.21 meets
nodejs_24, originalresults/69782 join3.6s and missingliteralCODE limit retained.
No rerun/greenouterclaim/newprofile or root. B1 independent fullactual-shell
checks provide separate passing evidence; metadata-only preparation adds no test
campaign. logs/b-integration-preparation.json has exact future source-shell/
freshcheck/FF/nonforceSSHpush/proof/release argv and active hooks.

All I1 parent/utility/tool/peer-message sessions joined, stillRunning[]. Short
source/commonGitsetup window released; I0 informed. Both implementers accepted
and quiescent, no further checks/actions queued. No repository or machine claim,
initial default/settings/PR/prod/lifecycle mutation. All18recoveryroots and
source/branches/worktrees/confctlgenerations retained. Initial user approval is
now the remaining gate: merge both F+B commits into syslog-exporter/master and
activate prepared strict/app-bound Rust required/linear/no-bypass ruleset plus
native allow-auto-merge. Requested future routine eligible Dependabot merges
need no per-update approval; this gate concerns only initial bootstrap.

### C reference direction settled

Architect bounded published-source pass found closest vpsf-status@8e17ccb9728bed308bbe7d67126eb84dfdf8a81c
.github/workflows/update-dependencies.yml: single schedule/manual contents-write
job, cancel=false concurrency, numeric official bot email, startingSHA/no-change,
tests+Nix before ordinarypush. vpsadminos@eedc1254d309cac861cb0f7af080ee8de8296506
.github/workflows/daily-update.yml andflake-update.yml corroborate pattern;
reference daily schedules must become requestedweekly. No reference repo mutation.

Settled C shape: one weekly/manual job, checkoutpersistfalse, trusted pinned
cargo update/audit; all updated dependency/build/test code in Nix sandbox before
static botpush. Retain actual25/fmt/Clippy/release/audit, remove B authorization/
scope/benchmark automation and restore baseline driver. No12case/65scampaign
required for routine lock maintenance; those were internal design choices.
ExactCargo.lock-only/no-change/stale-nonforce invariants; no artifact/publisher
engine/PR/ruleset. Architect writes concise sufficient brief incl sandboxed CI
hook/check reuse; I0 confirmedcapacity awaiting release, no sourceedit yet.

### C1 released

One complete I0 package from sufficient C brief (80612733), normal weekly/manual
updater matching published references; no artifacts/policy engine. One-job
sandboxedNix dependency execution/shared25+fmt/Clippy/release with freshaudit,
minimalCIhookreuse, plainbotcommit/nonforcepush and nochange/stale/failureguards.
Remove rejectedB machinery/performance campaign and restore preBdriver; preserve
F99ff, merged891 and exacthistoricalBrefs/evidence before coherent replacement.
Current initialintegration/settings has neverexecuted. Mainprosepass after facts,
localcommittedquickpass before retainedR0review, then actualNix/featurevalidation.
No Dependabot/PR/ruleset/PAT/deployment/currentrecovery/lifecycle work. I1 setup
window ended and oldf382preparation is parked. Current source mutation solely I0.

### C1 installer boundary clarified

I0 found that the pinned trusted cachix installer consumes github.token and
writes host Nix access-token configuration even when its token input is omitted.
Architect/lead accepted the smallest accurate trust split: trusted checkout/
installer consumption is allowed; persist-credentials:false and no token/config
in candidate derivation/env/source/mounts, with every updated crate/build/test/
hook process in ordinary sandbox=true. Host installer config is outside that
sandbox. Final push is only the explicitly configured shell-token environment,
not a claim of zero token consumption during trusted setup. No new installer,
scrub mechanism, credential or permission expansion; diagnostics expose only
sandbox field, never full token-bearing config/env. Consequential wording is
settled and source work continues without another permission gate.

### C1 source/focused milestone

One weekly/manual update job implemented, read-only Rust CI reduced to one
checked Nix release, B's six config/guard/helper/policy-test files removed,
benchmark restored byte-for-byte to F99ff. Node/actionlint CI dependencies
removed; one package checkPhase calls shared --release/offline fmt/Clippy/full25
plus small actual-shell fixture. Eight finite tests passed6.397s with real local
Git remotes: nochange, failedcheck, lock-only officialbotcommit, extra tracked
path/mode refusal, dryrun, stale default and real competing nonforce rejection.
Only trusted Nix tooling is substituted in quick fixtures; actual sandbox build
remains post-review. No fake Git engine, artifact/policy framework or production
activity. Source still uncommitted/unpublished; next lint/eval/fullquick/prose/
local commit before R0 affected final review. All historical B evidence retained.

### C1 local committed delivery / RC dispatched

Exact0b3131ffa6a2855cfa15c42de778d4bf794b4510/treef5d1659fdd8a31b44a80a1a06ed1657b9d7f16f3,
parentF99ff, complete891..C two useful followups and affected99ff..C one coherent
replacement. Complete11paths392+/16-; C-overF9paths339+/10-. SupersededB5e3/f382
keeprefs/rawmessages/reviews/CI retained before rewriting; B never integrated/
pinned/deployed and has no migrationboundary. No obsolete B source/framework/
benchmark campaign remains; driver exactF, runtime/Cargo.toml/lock/toolchain/
flake.lock/developerhook unchanged. CleanlocalC unpublished, remote master891/
featuref382. No migrations.

Quick8real shell/Git fixtures pass6.397s; actionlint9.55s, Nixpackageeval3.52s,
fullordinaryshared121.88s and finalactualhook13.50s (8fixtures+25Rust/fmt/Clippy).
Staging128 for removed B paths and interim3prose unstaged are preserved; final
explicit owned-stage/amend/fullhook yields intendedtree=head andclean. No broad
reset/clean/stash/bypass or coldrepeat. All6686/84468/49604,parent/API sessions
joined; debugtarget findings-only. No actualrelease/update/audit before review.

RC assigned retainedreviewer0, verified savedSol/xhigh/read_only, HIGH authority/
credential risk, all4lanes. User simplicity correction/references primary;
complete/affected/removal/history/no-migration/input/incident/prose evidence in
exporter-review.md C1 and logs/c-*. Mainwording pass done, superseded B process
removed from finalmessage. Long Nix/featurevalidation held until review; no
initial default/settings/PR/production/claim/lifecycle mutation.

### RC Important finding: fail-closed sandbox fallback

RC-I1 (risk/general), reviewed0b313: pinned installer Nix2.35.6 defaults
sandbox-fallback=true. Exact upstream local-settings.hh418-419 and derivation-
builder.cc1759-1806 confirm mount/PID namespace support can flip useSandbox=false
even with smEnabled/sandbox=true. The existing config assertion alone cannot
establish isolation; trusted setup left a write token in host Nix config. No
actual hosted fallback/leak is asserted. Lead accepts required narrow correction:
set sandbox-fallback=false with sandbox=true in BOTH installer configs, assert
both nonsecret values, same hook/main-build setting, focused existing fixture
update only. No new framework/installer/scrub/kernel experiment. Source0b313
held fixed until complete RC report; I0 owns amendment, root direct inspection/
focused proof under narrow-fix rule. Long validation remains held.

### RC final report and precise remediation release

[Original RC final report](custom-updater-final-review.md) retained verbatim.
Reviewed891..0b313/affected99ff..0b313, retained reviewer0 Sol/xhigh/read_only,
HIGH/all four lanes. One Important RC-I1, no Blocking/other Important/Advisory.
Independent scope/history confirms conventional reference-based updater, useful
F+C split, no obsolete B/A source or redundant input stream, no migrations and
sound documentation preservation apart from required isolation correction.

I0 released precise RC-I1 amendment only: both installer configs set fallback
false, nonsecret assertions check true/false, main/hook builds keep same setting,
existing fixture adds refusal as needed. Original0b313/report kept before amend;
no new framework/installer/scrub/kernel experiment. Lead directly edited owning
maintenance paragraph: unavailable isolation fails build; factual/prose pass done,
source/index window released back to I0. Focused+real hook proof and final narrow
patch/head/history bind precede any publication or long build. No full reviewer
restart for this exact enforcement of the already reviewed contract.

### RC-I1 closed; C feature validation released

Final a4554a93723abd65007a5dff174db63cbecc1245/tree
f81944cebcb80c1d1d524b7fcb29534e6e736564, parentF99ff. Root inspected the exact
four-path patch and independently checked both installer settings, filtered
sandbox=true/fallback=false assertions, all3 build invocations explicit false,
focused refusal before any build and main prose clause. All modes/other blobs/
message/F parent unchanged, source logical state clean/no migrations. Focused
15.22s + actual active hook24.25s pass9fixtures+25Rust/fmt/Clippy, effects joined.
Original RC binds0b313; logs/c-lead-narrow-fix.json closes RC-I1 on a455 under
step9. No scope/design expansion or full-review restart. No hosted leak claimed.

I0 released complete dependent fresh SSH feature publication with exact Bf382
lease, remote/comparison proof and exact-head hosted read-only Rust CI under
fresh Luna watcher. Require actual strict sandbox/release/sharedchecks/full logs;
no retired performance campaign or duplicate local release. Actual updater
master dry_run/authenticated push remains post-integration and unexecuted;
initial default integration still separately unapproved. No settings/PR/PAT/
consumer/production/claim/lifecycle change. Local target retained until final
CI/no-rerun proof, then only scoped own cleanup; all18 recovery roots retained.

### C first hosted failure: sandbox script entry

Finala455 published via exact SSH lease over Bf382, push0/4.84s; fresh remote
featurea455/master891 and891..a455 comparison saved. Rust43214738861 attempt1
singlecheck131170976168 failed in checkPhase entry after50.48s releasecompile:
scripts/check has /usr/bin/env Bash shebang, /usr/bin/env absent in sandbox,
exit126. Effective config logged sandbox=True/fallback=False; shared9/25 checks
DID NOT run in this failed release. No current fallback/leak is asserted.
logs/c-first-hosted-failure.json/raw failed log/status/watch preserve evidence;
watcher all cells joined, no ongoing effects or default/prod mutation.

Lead accepts I0 exact one-word package checkPhase correction: invoke
`bash scripts/check --release` with already-present stdenv Bash. Source owner
preservesa455/failure evidence, does focused invocation/static + mandatoryhook,
amends same C(parentF) and supplies exact narrow proof before publication/root
binding. No new framework/dependency/sandbox relaxation, unmodified CI rerun,
duplicate local release, performance/kernel experiment or full review restart.
No C integration-prep mutation had started; source/index window remains I0.

### C packaging entry correction bound / changed-head validation released

Final b9b9cfea4331ff28bd883f1ed7415af6f27cd5f7/tree
 a1d826ecdbf019600ee63f74e74c385b00902a7c, parentF99ff. Root independently
compared exact bytes: ONLY package.nix adds Bash before the same release check;
all other blobs/modes/message/parent unchanged, clean/no migrations. RC-I1 strict
configs/options untouched. Existing stdenv provides Bash; new directly executed
fixture helpers use absolute sys.executable and CI hook command-v-Bash, no other
/usr/bin/env assumption in new helpers. Syntax/phase eval and final actual hook
9fixtures+25Rust/fmt/Clippy14.95s pass; all known21595/local/prior watcher effects
joined. Original faileda455/43214738861 and rawmessage retained before amend.
logs/c-lead-entry-fix.json binds this precise packaging correction; no new design
or full reviewer restart, source no broader changes.

I0 released exact feature lease over a455 and a new changed-head hosted Rust
validation under fresh Luna watcher, not an unmodified failed-run rerun. Require
actual release checkPhase9+25, fmt/Clippy and effective true/false config; no old
benchmark campaign, duplicate local release or updater/audit/default mutation.
First new failure needs concrete diagnosis before another expensive run; no
weakened isolation/assertions. Target kept until final CI/no-rerun, all18 roots
and current production unaffected. Initial integration/master dryrun pending.

### C corrected hosted success

Rust43216044595 attempt1/exactb9, check131175436008 SUCCESS. Full raw log proves
filtered sandbox=True/fallback=False, fresh release compile1m09s, actual checkPhase
9shell fixturesOK1.995s, fmt/Clippy and release8+11+6=25 Rust tests passed;
checkPhase50s/install success. Drvn1kw1wbmgqfgn5mfz6qx848apar1pgc6 ->
output1gxpkcpw92jkrnxxndayjcir891xj7cj. Prior43214738861/a455 failure retained.
No actual updater/dependency update/audit/auth push or retired benchmark claim.

Observer ghwatch0/66s and43159/all cells joined. Its enclosing local login shell
returned1 AFTER ghwatch0 due bash_logout reading unset __ETC_BASHLOGOUT_SOURCED
under set-u; authoritative job/run and actual test log establish hosted SUCCESS.
No rerun/infrastructure loop or unknown effect. I0 final compact evidence and
scoped unused target cleanup follow at accepted no-rerun boundary; no local
measurement/consumer. Source fixedb9; default/production/settings unchanged.

Lead prepared source/target/FF/hooks/devShell identities and exact future merge
steps in logs/c-integration-preparation.json (2.6s read-only eval/Git checks).
Existing owned detached target891 remains clean and FF-compatible; declared
shell3g7315i0q8w0z8myr5cqdqidfg0n41a5, no new profile/root/build. Initial approval
still pending; no repository claim or merge occurred. Actual master dry_run is
a post-approved-integration gate, not claimed by feature CI.

### C final acceptance / approval boundary

Lead accepted final I0 source/CI/effect packet after direct compact inspection.
Actual release drv n1kw1wbmgqfgn5mfz6qx848apar1pgc6 -> output
1gxpkcpw92jkrnxxndayjcir891xj7cj; stricttrue/false,9fixtures+25Rust/fmt/Clippy.
Watch0/66s, enclosing logout1 documented, all known effects terminal. Removed only
owned target391,041,024allocated/384,495,938apparent bytes after exact device64769/
inode43926827/uid1000 and scoped reference/quiescence proof; absence independently
checked, protected unrelated metadata unavailable/no sudo/universal claim.
Free112,309,911,552bytes reported, no shared-space attribution. No new package.

Selected coordination guide9hr3ppqzzwb12x51vwjasw8hq0ka7dab, catalog7376b5c9,
read fully (727lines) and retained as raw c-selected-coordination-guide.txt.
Prepare/recheck source shell before a short approved repository claim; fresh
check/FF/SSH push/remote proof/release only inside it, before CI/records. No claim
or initial default/settings/PR/prod/lifecycle mutation occurred. Initial source
approval is now the remaining external gate; actual master dry_run follows it.

### Initial F+C merge approval and fresh preparation

User: "ok, merge it", direct reply to request to merge the flake and updater into
syslog-exporter/master. Scope covers F99ff+C finalb9; no settings/deployment or
lifecycle operation. Future routine bot writes were already requested; after FF,
run actual updater master dry_run without publishing. Current binding and both
environment markers match, source b9/treea1d826 and target detached891 clean,
fresh SSH master891/featureb9 unchanged. Selected coordination guide byte-identical
to fully read9hr guide. Reviewed RC/narrow bindings/fullCI still apply.

Initial nix develop --dry-run was unsupported and exited before realization;
corrected read-only nix build --dry-run devShell succeeds. It plans one mkShell
and10 cache paths18.7MiB compressed/2.2GiB unpacked (Cargo/Rust/audit tools), no
application or kernel compile. Restore declared environment before any claim;
never hold repository ownership during this resource work.
