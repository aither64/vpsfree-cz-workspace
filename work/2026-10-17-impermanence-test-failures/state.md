---
lifecycle: active
---

# 2026-10-17-impermanence-test-failures

## Status

The user authorized merging the corrected product feature into staging.
Clean premerge rebase is checked, independently reviewed and published at
49636f902704ce6019a7a8ae47ec0b3ca6902f68. Coordinated background integration
c79bd2d9-b991-47e6-85f3-6740b7884214 is admitted in prepare; no merge job or
default-branch success is claimed yet. Native continuation will report results.
It restores oversized tests running alone, retaining normal concurrent budgets.
The requested full-native execution-time comparison is now measured: all 335
scripts across 127 tests passed in both legs on the same product and runner.
Without prebuild took 12297.60 seconds; with prebuild took 12515.11 seconds,
an observed increase of 217.50 seconds (1.77%). This is a qualified exploratory
warm pair: initial usable memory was 89.4 versus 90.4 GiB, so the harness
correctly declined a clean comparability result. See
[benchmark-results-analysis.md](benchmark-results-analysis.md). The
historical benchmark product was `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`;
the corrected feature head is `e32d5382910501b0c8fe80bc6b9e6044e56ead8e`.
All 12 original impermanence scripts plus defaults passed; cached defaults also
passed with a smaller configured memory ceiling. Native GitHub CI finished with
126 passing test groups and one failure in upgrade/from-6.18-guests. Diagnosis
found a capability-denied NixOS22.11 guest service on the pinned predecessor,
before any upgrade; no evidence warrants a resource implementation change.
User explicitly authorized merging the corrected vpsAdminOS feature into staging
(20 October: "this is good enough then, let's merge it"). The authorization
excludes the temporary benchmark workflow and grants no deployment or session
lifecycle action. Premerge refresh/checks and coordinated integration are pending.
The session remains open.

User accepts the observed performance overhead if it helps with OOMs (20 October).
This accepts the tradeoff, not an arbitrary-build OOM guarantee or merge approval.
User subsequently rejects strict memory admission: oversized tests should be
attempted, running alone as before; actual OOM failures should expose tests
requiring repair. Implementer0 owns this bounded scope correction, quick checks,
and coherent product history; architect0 reconciles design.md. Historical a2
benchmark receipts stay intact. New final source review and publication remain.

## Phase checklist

- [x] Verify the exact session identity and saved same-session team.
- [x] Investigate the original shared fixture build failure and test purpose.
- [x] User confirms OOM; compare proposals with actual runner defaults.
- [x] Accept opt-in staged preparation and architect-owned design brief.
- [x] Implement, pass quick checks/hooks and commit logical owners.
- [x] Independent final review, history/migration inventory and R1 repair.
- [x] Build selected images and pass all 13 selected scripts.
- [x] Pass cached representative test at the smaller configured ceiling.
- [x] Publish exact final source head and capture native comparison.
- [x] Native GitHub CI completes; OS build passed, native suite has one failure.
- [x] Diagnose upgrade/from-6.18-guests failure and record its separate scope.
- [x] Full-native timing comparison: both full suites pass; observed +1.77%, qualified by initial memory drift and one randomized warm pair.
- [x] Restore oversized-test run-alone fallback per user decision; 155 focused checks, independent review and corrected feature publication complete.
- [ ] Overall CI remains red; six livepatch profiles also lack executed coverage.
- [x] Explicit user direction to merge corrected vpsAdminOS feature into staging.
- [x] Refresh against staging; focused/hooks/current-input Nix checks and final independent review pass.
- [ ] Coordinated staging fast-forward: background run c79bd2d9-b991-47e6-85f3-6740b7884214 admitted in prepare.

## Next action

Wait for native coordinator continuation for run
c79bd2d9-b991-47e6-85f3-6740b7884214. On completion/action notification, read its
authoritative status, acknowledge exact handoff event/generation and verify the
remote staging result. No direct Git bypass, deployment or lifecycle action.
Current rebased head passes155focused specs/hooks/current-input Nix fixtures and
final independent review; exact user authorization and request are retained.
Retain the measured totals and limits. Benchmark
39305352549 is complete; both CLI commands exited zero and no owned processes
remain according to its receipts. The CI job is red solely because its two
initial memory ceilings differed. No further full-suite run is launched.
Benchmark head is 295b814ad; exact product a2 for both legs. Product implementation
is independently reviewed and checked, with a qualified performance comparison
now available. No merge/deploy/lifecycle authorization exists.

## Historical measured source and history (a2)

- Repository: `vpsadminos`, canonical remote `git@github.com:vpsfreecz/vpsadminos.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-17-impermanence-test-failures/vpsadminos`.
- Branch: `2026-10-17-impermanence-test-failures`, published to the same remote branch.
- Initial/review base and current origin/staging: `0081fc01f13236a098380094ddbd00539a9c8dae`.
- Final head: `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`.
- Exact tested final tree: `98fab6887104cc1aa6f05941825047b031c7c662`.
- Worktree/index clean; remote feature head matches. Final fetch confirmed staging
  remains at the reviewed base. Native comparison was captured after amendment.

Complete base-to-head series, oldest first:

1. `5acb08db650a0c72d3b00ab66cbdd9da6b50eb46` — test-image SquashFS cache option.
2. `09fb4131d65926e7490829d5a278b3d162fac44d` — strict RAM/shm admission.
3. `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1` — opt-in preparation and supporting
   exact-config/root/selection/CI/docs/tests, including the narrow R1 repair.

Three coherent owners; no obsolete approaches, fixup/repair residue, migrations,
transitional state formats, dependency/pin streams or generated update streams.
First two owners remained unchanged through R1. The amended final tree exactly
matches the frozen fully tested repair tree. No migration was merged, released,
deployed or externally consumed because there are no migrations.

## Behavior at measured a2 and upcoming correction

`test --prebuild` is opt-in; `--no-prebuild` disables staging. Native CI enables it
and its manual boolean can explicitly disable it. All selected config/image
closures finish before any selected VM; runtime and retries consume exact rooted
configs without Nix. The pre-preparation ResourcePool is retained for runtime.

Preparation jobs scale with detected available/assigned memory, configured maximum
and the existing 8192 MiB reserve, divided by the overridable positive 8192 MiB/job
estimate and capped at inherited Nix max-jobs. Zero remains remote-only. Runtime
`--jobs auto`, CPU factor 1.5 and build cores/processor parallelism are unchanged.
Test-image compressor cache defaults to 2048 MiB; production defaults to null.
At historical a2, RAM/shm oversize requests failed finitely. The user rejected
that policy: the corrected series restores the baseline fallback for RAM/shm/CPU
when no test fits and none is running. Requests stay unchanged and the runner
warns. Normal concurrent budgeting remains. Both prebuild settings use the same
runtime scheduling.

No guest-state/schema/protocol migration or coordinated node update. Existing
metadata, legacy/debug behavior and external tests/testsMeta-only exports remain
supported. Representative vpsAdmin HEAD `b4ef8535a629ee8c9cd753afecdb05e0895d0eea`
pins vpsadminos `8e44a5124439b1f3048ffc56b1717614a5360358`; it does not re-export
lib.testFramework. Consumer/pin code changes were unnecessary.

## Verification

See [verification.md](verification.md) for commands, timing, capacities, exact
store-path reuse, phase boundary, root lifetime, measurements and limitations.

- Full runner: 373 examples, 0 failures (88 seconds).
- Full OSVM: 184 examples, 0 failures (62 seconds).
- Pure SquashFS flags/module wiring and declared Nixfmt/RuboCop hooks pass.
- Enabled hooks ran for every commit/amendment; no bypass.
- 32 GiB configured ceiling: 3 prep jobs, unchanged 96-vCPU runtime budget;
  both new images compressed with 64 processors, zstd10 and explicit `-mem 2048M`.
  All 12 unique impermanence scripts plus defaults passed, exit 0. Runtime
  5955.47 seconds. No VM began before both configurations were prepared.
- 16 GiB configured ceiling: 1 prep job, same CPU settings, same cached defaults
  JSON/image, unchanged 8 GiB guest; passed, exit 0 (261.7 seconds).
- Owned preparation roots remained during runtime and disappeared after complete
  VM cleanup. Both owned command processes exited; no local verification remains.
- Final job cgroup max/oom/oom_kill event counts are zero.
- GitHub exact-head RSpec39068521789 and RuboCop39068521800 succeeded.
- Native CI39068521841 failed: OS build passed; native suite126 test groups passed/1 failed
  (upgrade/from-6.18-guests); four livepatch jobs passed and six jobs that never
  started were cancelled after24h. Original logs/artifacts downloaded; architect0 traced the failure to
  network-setup.service exit218/CAPABILITIES on NixOS22.11 before the upgrade.
  Its fixture and capability policy are unchanged by this branch:
  https://github.com/vpsfreecz/vpsadminos/actions/runs/39068521841

The local ceilings were admission settings on one 96 GiB/64-CPU builder, not
enforced cgroups. Native CI adds a second physical builder:100GiB/48CPUs,
11 adaptive prep jobs and unchanged72-vCPU runtime capacity; all12 persistence
scripts passed there too. Evaluator client high-water mark was about
20 GiB; no aggregate daemon peak was measured. The per-job estimate and cache size
are policies, not RSS caps or an arbitrary-build OOM guarantee. Dependency caches
were partially primed; both selected images were actually compressed. No fully
cold closure or same-full-fixture warm repeat is claimed. The smaller warm check
used defaults to avoid repeating the large fixture's evaluation and long scripts.

## Independent review

[review.md](review.md) records reviewer0's all-four-lane review and lead decisions;
[review-packet.md](review-packet.md) contains the complete history/consumer packet.
Retained reviewer0 used saved gpt-6.1-sol/xhigh/read_only, no override/fallback.
Risk high because of host resource/public framework behavior.

One Important R1: partial TestConfig validation could admit malformed later
machines and allow earlier fresh disk reset. Fixed by sharing canonical OSVM
parser/network rendering with MAC/port allocation disabled. Regressions prove
valid-first/invalid-later rejection before Executor, VM/disk/global allocation,
including expectFailure. Full suites and scoped hooks passed on the exact repair;
lead directly verified this narrow requested fix under review steps 9–10. No new
contract or scope expansion requiring unaffected-lane reruns. Repair was folded
into the preparation owner; first reviewed head `fac4fe226` and original diff
receipts remain recorded in the review artifacts.

## Original incident and setup evidence

User confirmed the original build was OOM killed. One shared fixture image failed
before any VM/assertions; 12 reported script failures followed that single build
failure. The tests protect UID/GID maps, account IDs, payload integrity/ownership,
machine-id and bind metadata through compatibility-module adoption, activation
and restart. They retain each scenario's NixOS release/stateVersion22.11; the old
pin `1150e37b1cc997b1728f2fda806a3433ef55b798` is compatibility source, not a release
upgrade. [source-investigation.md](source-investigation.md) preserves source lines
and original evidence. Runner SSH keys were refused and physical host key was
untrusted; no trust bypass or exact victim/aggregate peak claim.

A utility accidentally stopped the first long attempt on a systemd unit named
sys-kernel-debug after960seconds; parent confirmed no kernel compile. That TERM
attempt is invalid verification, not a product failure/OOM. Corrected retry used
visible parent monitoring because fresh utility invocation was unavailable.
Slow guest boot (~7m10) eventually reached userspace/shell within900seconds; no
boot fix/timeout change was made. No kernel was intentionally rebuilt.

Fresh worktree hooks needed install/sign; native Ruby specs needed the existing
CI libosctl extension recipe and -Itest-runner/spec. Incorrect initial harness
commands ran zero examples. Nix fixture context-parsing errors were test-only
and fixed while retaining production references. Hook signature during ambient
push required signing/pushing in the declared Nix environment, without bypass.
Known lessons already live in notes/vpsadminos/2026-07-04-test-runner-rspec-local.md
and 2026-06-03-overcommit-nix-env.md. Official action versions were verified;
compatible existing @v7 refs retained (checkout7.0.1/upload-artifact7.0.2).

## Artifacts and ownership

- [plan.md](plan.md), architect-owned [design.md](design.md), [verification.md](verification.md).
- [native-ci-follow-up.md](native-ci-follow-up.md): exact CI failure and scope.
- Original job.log/native-logs.zip/ci-logs; review diffs and frozen quick receipts.
- r1-runner/r1-osvm/ready-cache logs/status; integration-retry-32g and integration-16g
  logs/status; image-preparation.log, warm-preparation.log, compressor-sample.txt,
  compact expected_success results and final-job-memory-events.txt.
- Transient whitelisted runner-nix-env.sh/hooks-nix-env.sh are local environment
  receipts only; do not publish/commit them. No credentials were captured.
- Native test-state directories: /tmp/os-test-2026-10-17-impermanence-test-failures-32g
  and -16g. Managed VM disks were removed by normal runner cleanup. Logs retained;
  no manual session/worktree/branch deletion, archival or stop requested/performed.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-17-impermanence-test-failures/

## Performance comparison ownership

- Benchmark-only worktree: worktrees/2026-10-17-impermanence-test-failures/vpsadminos-benchmark.
- Benchmark-only ref: 2026-10-17-impermanence-test-failures-benchmark, initiallya2ccd72d0.
- This ref is not part of the product integration request. Product branch stays unchanged.
- Hooks installed/signed in declared Nix environment; retry registered the worktree
  after the known inherited post-checkout signature refusal. No hook bypass.
- Architect brief is written/accepted and registered. Implementer0 committed the temporary workflow/harness and focused specs as
  4a3e43347ffe9913b330a97fd297d7e64db51d50 (treeb153c396a52f1bd7e9e72317de7dc67e8eeda2fa).
  11 focused examples, YAML/bash syntax and hooks passed; source/index clean.
  Lead final prose pass and actual admission-ceiling comparison are included.
  Retained reviewer0 completed all-four-lane final review; benchmark-review.md
  records two Important measurement findings (guest builds misclassified as host
  builds; transient runtime capacity changes ignored). Both accepted and assigned
  to implementer0 for narrow fixes/regressions/amendment. Lead directly verified both narrow fixes and meaningful regressions under
  review steps9–10. Final amended benchmark06915925a7a63a2fac7135a752101228b5b699e0,
  tree771895324cfc498413a8eb801ac0b0b9bac5fb4b;13 examples0failures, hooks pass,
  clean worktree. Review gate satisfied; publication/dispatch next.

## Active matched timing run

Benchmark-only head06915925a7a63a2fac7135a752101228b5b699e0 was published over
SSH after independent review and direct R1/R2 verification. No rebase onto a
new product revision: exact producta2 is the deliberate benchmark boundary.
Native comparison captured full inherited range from0081fc01 to06915925a.

Dispatched manual CI39276852536 at2026-10-19T15:18:40Z:
https://github.com/vpsfreecz/vpsadminos/actions/runs/39276852536
Initially queued; one job, exact producta2 for both CLI legs, full native335
scripts/127 groups, warm roots retained, A(no-prebuild) thenB(prebuild), auto jobs
and production CPU/memory settings. No timing result yet.

Fresh utility /root/prebuild_benchmark_ci_watch owns monitoring this exact run
and head, resolved from retained verification_watcher gpt-6-luna/low and utility
identitydw_024841fba072af1d79bd78026612eaeca055acfa31ecc89f; current installed
execution_access=full_access. No retained-member reconfiguration. Follow monitor
skill; original product branch unchanged. Root will interpret artifacts and
report totals/deltas after completion, not infer performance from correctness.

## Benchmark attempt1 failed before measurement

User reported CI39276852536 failed. Lead retrieved original job118143302393
logs and artifact12201105726 to benchmark-ci-failed-job.log and
benchmark-ci-failed-artifacts. timings.json contains legs=[] and preflight error
NoMethodError: undefined method fetch for Integer; warmup bookkeeping elapsed
1681.965s. No A/B time exists, and no performance conclusion is possible.

Implementer0 is assigned bounded parser diagnosis/repair with pinned-Nix
contract coverage and hooks, retaining the published06915925a receipt and
folding the caused fix into the sole benchmark owner. No rerun until diagnosis
and verification. Producta2 remains unchanged. Active monitoring of attempt1
must be treated as terminal failure, not a running benchmark.

## Corrected benchmark attempt2

Root cause confirmed: CI Nix2.34.8 emits version4 JSON envelope; helper assumed
flat derivations and called fetch on Integer4. Exact pinned binary reproduced it.
No aggregate warmup or A/B leg started.15 focused examples including actual
Nix inspection (no realization) pass; hooks pass. Lead directly verified this
narrow repair and wording, retaining independent review under steps9–10.

Benchmarkd3474e5fc634a387c7c2f2ecb28efefe476c434b/tree
7ccf6b85573a7ce631809dfd5b26f9d8a7f05e2b is published by exact lease over069;
producta2 and measurement settings unchanged. One owner, no fixup residue,
migrations or dependency streams. Original published head/diff and failed logs
retained. No superseded active CI run to cancel. Native comparison recaptured.

New CI39296042103, dispatched17:39:49Z19October, is in progress:
https://github.com/vpsfreecz/vpsadminos/actions/runs/39296042103
Same-head RSpec39296020214 and RuboCop39296020233 also started. Fresh Luna/low
utility must monitor this new operation (do not reuse attempt1 watcher) and
send terminal report through supported same-session lead reporting if available,
as well as normal collaboration report, so failure is acted on promptly.
No A/B times exist yet. Remaining acceptance is still real measured comparison.

## Attempt2 outcome / status request

CI39296042103 failed18:33:45Z19October. Warmup completed3174.64s;
A(--no-prebuild) immediately failed0.5439s with Bundler::GemNotFound(geminabox),
zero tests/phase markers; B was skipped. No valid A/B comparison. Original
artifact saved benchmark-attempt2-results and full job benchmark-attempt2-job.log.
Lead assigned implementer0 narrow subprocess environment diagnosis/repair and
an actual packaged-CLI smoke test before another expensive warmup. No rerun yet.
Producta2 and resource settings unchanged. Root cause beyond the observed
Bundler failure is being established; do not describe this as test/OOM failure.

## User directs persistence to measured results

User: “well proceed, fix it until we get the results”. Continue autonomously
through benchmark repair, actual CLI smoke and measured A/B completion; do not
stop at a queued run or setup success. No merge/deployment/lifecycle approval.

Attempt2 causal diagnosis: bundle exec exports BUNDLER_SETUP, consumed directly
by Ruby3.4.9 rubygems.rb1482. Manual child cleanup removed BUNDLE_GEMFILE but left
BUNDLER_SETUP/BUNDLER_ORIG_*; forced setup then selected product root Gemfile and
failed on geminabox. Implementer0 is using Bundler's own unbundled environment
with unsetenv_others and adding the actual wrapper --help smoke before expensive
warmup. Existing package availability is being checked; no gem-install shortcut.

## Attempt2 child environment repair and attempt3

Attempt2 image warmup completed3174.64s, but actual A CLI exited0.544s on
Bundler::GemNotFound(geminabox); no VM/test or B leg. Inherited BUNDLER_SETUP
survived manual BUNDLE_/RUBY/GEM cleanup and Ruby3.4.9 loaded the dev Bundler,
which resolved product root Gemfile after BUNDLE_GEMFILE removal. Original
attempt2 artifacts/stack and published d347 receipt preserved.

Implementer0 replaced manual environment logic with Bundler.unbundled_env and
unsetenv_others, shared by both measured children and a new exact wrapper --help
smoke before expensive selection/warmup. No product/resource settings changed.
Exactproducta2 package was built/rooted by a fresh Luna package-only watcher
(exit0,39s,noimages/kernels). Actual contaminated Ruby3.4.9/Bundler4.0.23 parent
reproduced old CLI exit1/geminabox and new CLI exit0/normalhelp. Receipts under
benchmark-child-env-smoke;16focused examples0failures2.65s and enabled hooks pass.
Lead inspected source/realreceipt and main-context wording; direct narrow-fix
verification under review steps9–10, no new public boundary or design.

Finalbenchmark295b814ad3aadca80ee10c043327c4676d71913c/tree
626b58c3fe84ecc53db322a7853b9e6240220266 clean; soleowneraboveexacta2.
Fixdiffb7533b9a946153182c6efe820839b13c3ae18794e77f848169fdfd2b7855458e;
fulldiff3896b3081c4e7f2cca5f845a1ca9eb26dcf27d5c08ab0942f1d4c966fd4c0902.
Published SSH with exact d347 force-with-lease afterfetch; comparisoncaptured.
No active superseded run to cancel. New manualbenchmark39305352549 is active:
https://github.com/vpsfreecz/vpsadminos/actions/runs/39305352549
SameheadRSpec39305340692/RuboCop39305340491. Fresh Luna/low standalone watcher
owns only this observationbatch, explicitfullaccess/never and boundenvpair;
parent keeps turn open until result/failure handling. Producta2 unchanged.
No valid timing result yet; user's explicit instruction is persist until results.

## Attempt3 completed: measured warm comparison, 20 October

Run 39305352549 finished at 02:37 UTC. Both complete CLI commands passed all
335 scripts/127 tests with identical selections, outcomes and intentional retry.
A (--no-prebuild) took 12297.601794 s; B (--prebuild) took 12515.105386 s.
Observed difference +217.503592 s (+1.768667%). B global preparation receipt
was 1571.263 s; executor intervals A12231.06 s and B10858.52 s include different
work because legacy preparation overlaps execution.

The automated comparison is correctly qualified, not a test failure: its only
failed predicate is initial memory ceiling equality (89.4 vs90.4 GiB). Other
conditions pass, including unchanged assigned resources, no recorded updates,
host image builds, kernel failures, OOM kills or remaining owned processes.
Architect0 independently verified the predicate and original receipts and accepts
reporting a qualified exploratory warm pair. No causal regression/equivalence,
cold-build or arbitrary-memory-safety claim. See benchmark-results-analysis.md
and verification.md. The watcher exited and returned its full artifacts; no
further run was launched. Session and both feature branches remain open.

## Oversized-test correction, 20 October

Implementer0 reconstructed the original a2 tree exactly in isolated
vpsadminos-admission before intentional edits. Dated backup
refs/backup/2026-10-20-impermanence-before-admission-correction and benchmark
ancestry retain a2 unchanged. Final topic head e32d5382910501b0c8fe80bc6b9e6044e56ead8e,
tree a57b700797c2396e148da18b6729cb49b2fc0d21, clean.
Shipping series from original0081 base now has two owners: unchanged5acb08db6
cache and e32d53829 prebuild. Rejected09fb4131d is removed rather than reverted
in shipping history. No migrations, pins or repeated generated streams.

The a2-to-e32 delta is seven paths: scheduler/pool/spec, CLI help/spec and
testing docs/man. Generic baseline fallback/warning and worker loop restored;
prebuild root-lifetime cleanup remains. No cache/sizing/Nix-closure changes.
155focused examples pass in1.48s; enabled Nixfmt/RuboCop/commit hooks pass.
Lead accepted visible wording. Retained reviewer0 now performs all-four-lane
final review with explicit whole-series/history/migration conclusions; see
admission-correction-review-packet.md. No image/VM/OOM/full benchmark rerun is
needed for this baseline fallback restoration; measured pair retains exacta2.

Origin/staging has advanced to f4bac6b49. Current reconstruction deliberately
retains original0081 base for an exact change comparison; a premerge refresh
and applicable checks remain necessary before any later authorized merge.
No integration authorization exists. Feature publication follows final review.

Reviewer0 completed all four lanes on exacte32/treea57b with no findings and
explicit coherent-series/no-migrations/no-repeated-streams conclusions. Lead
recorded read-only report in admission-correction-review.md. Review accepts
user's actual-OOM boundary; no refusal gate restored. Source delta and docs match.
Original product worktree cleanly detached at backed-upa2, feature branch moved
to reviewede32 and reattached; SSH force-with-lease required exactremotea2.
Push succeeded, benchmark295 unchanged, native comparison recaptured.
New hosted checks RSpec39396698231 and RuboCop39396698224 are observed by a fresh
pinned Luna/low utility (fullaccess/never/boundenvpair); automatic native
CI39396698293 is recorded but no fullsuitewait/rebenchmark selected. No active
superseded runs were present. Defaultbranch and session lifecycle unchanged.

Hosted checks completed successfully on exacte32: RSpec39396698231 (3m56s),
RuboCop39396698224. Fresh utility exited0. Native CI39396698293 still in progress
at its final sample, not awaited. Utility first used ambient default repository
for one RSpecwatch (404), then corrected to explicitly requestedvpsfreecz/vpsadminos;
no test rerun. Raw /tmpwatchlogs copied into session-owned admission-correction-ci
for durable evidence, report admission-correction-ci-report.md. No source fixes
or follow-up run needed. Product source clean/published, review passed; unmerged,
not deployed, session open. Preparation/cache heuristics and accepted oversized
test OOM possibility remain explicit limitations.

## Authorized staging integration admission

User's "this is good enough then, let's merge it" authorizes only corrected
vpsAdminOS product into refs/heads/staging. Clean rebase preserves both patches;
reviewer0 independently assessed final49636f902/basef4bac6b49 and inherited
context with no findings. Final two-owner inventory2028283db/49636f902, no
obsolete strict-rejection history, migrations or feature pin streams. Report
staging-refresh-review.md and coordinator binding merge-review-receipt.json.

SSH feature push used exact e32 lease and succeeded. Superseded olde32 native
CI39396698293 cancellation requested; current-head runs untouched. Exact
benchmark295 and a2/e32 backups retained. User mergeapproval preserved by
reviewed patch-equivalent rebase. Current target remote wasf4bac6b49.

Selected runtimep4snvm49... catalog includes vpsadminos->staging. Read selected
coordination/operations guides plus integration guide from its exact derivation
source ih0j160... (the installed share omitted integration.md). Merge-only needs
no machine reservation; foreign aitherdev reservation untouched. CODEX thread
and session IDs both match retained leadc20e, so --background admission verified
managed recipient. Request merge-integration-request.json UUID
c79bd2d9-b991-47e6-85f3-6740b7884214 returned schema2/prepare/runnable, no jobs yet.
Only runtime preparation/queue/mutation remains; lead ends turn per background
continuation policy and resumes on native event. No defaultbranch effect yet.
No completion/reservation-finish/deploy/session-lifecycle request included.

## Integration c79bd2d9-b991-47e6-85f3-6740b7884214

Requested exact feature heads are integrated. See integration/c79bd2d9-b991-47e6-85f3-6740b7884214/summary.md
and integration/c79bd2d9-b991-47e6-85f3-6740b7884214/result.json for operation receipts. Feature refs and session retained.
