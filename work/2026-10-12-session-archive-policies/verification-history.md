# Verification history

Historical checkpoints and superseded candidates, retained as execution evidence.
The current selected revisions and readiness are in [state.md](state.md).



Initiative 2026-10-12-session-archive-policies was created with dev-session start
--no-codex --no-attach. Complete environment binding agrees with dev-session
current. It has an owned terminal and no retained root/roster; ordinary lead owns
implementation. No other session was adopted.

All branches use this slug and worktrees are under its matching group:

- Runtime dev-workspace: base 60c679c52c263a0fc7a4b08c5f83a291cfd89191,
  final head ebe612f8c890bfc5325c0e5f8e86490ffa2534e3. Three logical commits:
  target-specific strict merge proofs, explicit archive/recovery, and artifact prevention.
- Workspace: shared master baseline 93e478b00c51fe6ef03610c46866a88509646fdb,
  head 7f932c7d44464c0de070e88ad17f9e903fe7ff78. Three owned commits:
  archive guidance, one final runtime composition pin, and artifact guidance. Six inherited tracking
  commits from remote master 7ac561bc are unchanged.
- Configuration: current upstream base b17dbea2cb1b9bf93714c929da776a4d4a6618f8,
  head edeb94c1a810f17a148de3edc59209e0f580a967. One generated confctl pin
  dev-workspace/devWorkspace to the same runtime. Declared Overcommit hooks pass;
  generated message-width warning is permitted and retained.

All feature heads are published over SSH. Repeated pins and follow-up corrections
were folded into their logical commits. No migrations. The extension remains
7157c8098dcf60127aa4df823fab82b4185ad22a; codex-web and native Codex 0.160.0 stay
unchanged. Final cross-consumer deployment contract passed at runtime 97ce087.
Application comes from the user profile; configuration supplies the host module.

## Independent review

Installed catalog 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd
selected standalone /root/archive_policy_review, reviewer role, gpt-6-astra/xhigh,
read-only. Fallback reason: threadless initiative has no retained roster.
Risk high: destructive removal, persisted recovery and lifecycle formats,
App Server protocol and host/application transitions.

General, Architecture/Repetition, Scope/Proportionality and Risk/Compatibility
initial review completed. All findings accepted and corrected: stop parents
before discovery and repeat discovery through shutdown; retire descendants first;
make restore completion irreversible and reconcile lingering intent only while
contents match; preserve threadless negative ownership proof.

The threadless-terminal boundary required General/Risk follow-ups with the same
reviewer/settings. Corrections retain the exact shell through capture/tracking,
seal fresh operation evidence before the full conversation absence check, make
the real Go observer accept only the proven explicit threadless terminal, and
scope hangup/output handling to the exact retiring caller terminal through
journal completion. Automatic policy still requires runtime absence.

Final General/Risk and whole-branch review passed at runtime 93c92dc, workspace
0f993e47 and config 6fa2e584, with no remaining findings. Unaffected lane
conclusions remain applicable. Explicit history conclusion: no obsolete branch
iterations, one final pin per consumer, no migrations. Later 73eb11f adds only
a one-line stale browser asset test expectation correction, verified by the
parent's focused test and complete range-diff under skill step 9; consumer pins
were regenerated and consolidated. No design or behavior boundary changed.

## Verification evidence

Focused checks passed for syntax/whitespace, Ruby explicit dirty/detached/locked
cleanup and exact restoration (including git gc --prune=now), strict unmerged
refusal, multiple target branches and journal retries. Initial 4 Ruby runs/104
assertions; review remediation 4 runs/115 assertions; terminal/absence aggregate
3 runs/52 assertions, including real tmux phase advancement after hangup.

Focused Go checks passed for full queue preservation before deletion, lost reply
reconciliation, goal/turn interruption, repeated native descendant shutdown,
retained-team identities, shared manifest fixtures, actual threadless observer
RPC (8 ownership/absence/context cases), browser receipts and CLI policy args.
Generated native goal/set schema agrees with selected 0.160.0. Host package-layout
fixture and final browser asset test pass. Corrected Ruby fixture checks pass
with global/system Git config disabled (3 runs/59 assertions).

Failures were investigated before new attempts:

- First packaged attempt da2a15d: 410 Ruby runs/5582 assertions, 3 failures
  (two old explicit CLI kwargs expectations and one release fixture lacking
  author identity). NixOS VM passed. Tests corrected; no product workaround.
- CI 38269656485: old strict CLI expectation omitted --require-merged; corrected.
- CI 38274754897: all 411 session Ruby runs/5638 assertions passed; host fixture
  omitted new recovery helper in its hand-built package. Added both fixture
  entries; production packaging was already correct.
- Final packaged attempt at 93c92dc and CI 38277704899: stale automatic-page
  expectation v29 versus coordinated template v36. One-line test corrected.
  Full local log runtime-final-packaged.log and downloaded CI evidence
  /tmp/session-archive-93-ci.log. No remaining process from failed batch.
- Cancellation of superseded CI 38271839622 received HTTP 403; run stayed owned
  by GitHub and subsequently finished. No current superseded live run found.

Previous candidate CI: https://github.com/aither64/dev-workspace/actions/runs/38279110178
at 73eb11f passed. Local final runtime flake check passed: 412 Ruby runs/5638
assertions, zero failures/errors, 13 skips; host-idempotency VM 274 seconds and
session-recovery-boot VM 302 seconds. Full Nix build logs for the package and both VMs were subsequently recovered;
all later commands have complete launch-time logs. Final utility logs/status: runtime-release-packaged,
workspace-release-packaged, application-build, aitherdev-build, playwright-build,
release-ci alongside this record. Do not commit bulky logs.

Configuration registration initially returned exit 78 outside its Nix shell due
to missing Bundler. Registration inside nix develop succeeded without recreating
or resetting the worktree. Existing lesson:
notes/vpsfree-cz-configuration/2026-10-11-worktree-hooks-in-nix-shell.md.

## Deployment and recovery

Prepared rollout: [rollout.md](rollout.md). No new-format production archive or
revival written yet. Existing profile is recorded there. Live native/tmux PID
and socket generation are saved in live-before.json for continuity checks.
All pending lifecycle journal scans were empty. Recheck before switching.

Original requested session has ten clean checkouts, five registrations and two
HaveAPI targets. [requested-archive-before.json](requested-archive-before.json)
records exact paths/heads. Private snapshot capture precedes all forced removal;
branches remain. Retry ordinary archive on interruption; never delete receipts
or downgrade the executor after writing new formats. Own initiative remains open.

The storage-redesign FYI was investigated read-only: retained lead and members
verify idle, but eight historical loaded native utility descendants outside its
roster trigger loaded_conversation_residue in the existing recovery check.
This predates deployment; that session was not mutated.

The network-ipv4-left-counter FYI was also checked read-only. Three new
uncommitted artifact entries use name instead of the existing label field.
Artifact field validation is unchanged in this branch; the live profile remains
the predecessor. After explicit user direction, only those three caption keys were repaired;
all unrelated edits remain with that session owner. Live GET returned 200.

## Documentation and portal

[Plan](plan.md), [design brief](design.md), [review packet](review-packet.md).
Owning project explanations: runtime docs/dev-sessions.md and
session-archive-recovery.md; workspace docs/agent-instructions/lifecycle.md and
sessions.md. Existing README links reach runtime contracts. Main agent applied
English writing guidance directly. Individual execution evidence stays here.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-12-session-archive-policies/

Artifact prevention: runtime adf7b83 adds shared Go/Ruby caption aliases,
canonical atomic artifact registration, operation/generation exclusions and
concurrent-edit detection. Four new Ruby registration tests pass (42 assertions);
shared valid/invalid fixture checks and full Go session package pass. All older
candidate runtime/workspace/config builds and exact CI passed; affected review is complete and the corrected final candidate is under
packaged/browser/build/CI verification before deployment. Old built
application remains rooted for comparison; it has never been selected.


## Artifact review completion

Same independent reviewer /root/archive_policy_review, Astra/xhigh/read-only,
completed all four affected lanes at adf7b83/3bfdb694/024196c3. Two Important
findings: Unicode-only blank captions diverged between Ruby and Go; and valid
ready creation manifests may omit the artifact list. Both corrected in the
owning artifact commit 97ce087 with one shared Ruby Unicode-space predicate and
initialization only after existing readiness validation. Creation-less explicit
scope requirements remain unchanged. Shared valid/invalid Unicode fixtures and
ready-predecessor registration coverage were added. Parent focused verification:
5 registration runs/46 assertions, shared fixture 3 runs/56 assertions, full Go
session package, syntax and whitespace all pass. Direct remediation satisfies
skill step 9; no new design/interface boundary and no reviewer rerun required.
Whole-branch conclusion: no obsolete unmerged iterations, three runtime logical
commits, three owned workspace commits, one final pin per consumer, no migrations.
Previous archive review remains valid.

A standalone Ruby module invocation failed because NullTmux is supplied by the
main test harness; the corrected focused command uses test/dev_session_test.rb
with --name. No application change was made for that invocation error. Superseded
CI cancellation is unavailable under the current GitHub token (HTTP 403); current
head checks are tracked by exact identity rather than old runs.


Final candidate watcher /root/archive_candidate_checks is fresh Luna/low from the
installed separate utility policy. It owns sequential runtime/workspace flake
checks, rooted application build, aitherdev build, Chromium/Firefox archive failure
and page lifecycle checks, and exact CI 38285693900. Complete launch-time logs and
actual statuses use candidate-* names beside this record. No deployment delegated.

Final candidate runtime flake check at 97ce087 passed, including package tests
and both VM scenarios. Complete candidate-runtime.log and actual status 0 retained.
Watcher continues the remaining release batch.

Final composed workspace flake check at bb9ba7e passed (status 0), including
deployment contract and provider/package checks. Final application and target
builds, browser checks and exact CI remain in the same watcher batch.

## Final browser correction

Final 97ce087/bb9ba7/f40eb8 packaged runtime/workspace checks, application
build and aitherdev build passed. Runtime tests: 417 runs, 5688 assertions,
zero failures/errors, 13 documented skips; both host/recovery VMs passed.
CI 38285693900 also passed. Archive browser regression initially failed on
read-only pending archival pages. Exception stacks identify the request/queue
refresh-notice callbacks: visibility events render notices even when their
controls are intentionally absent. The identical unsafe callbacks exist in
runtime base 60c679c, so this predates our work. Two local DOM guards fix it;
the regression now logs exception stacks and passes Chromium and Firefox
(12.78 seconds). Syntax and whitespace checks passed. Correction folded into
the archive behavior commit, retaining three logical runtime commits.
A bounded General/Architecture follow-up will assess this correction;
remaining lane conclusions stand. Final selected runtime is ebe612f8.
Deployment remains unstarted.

Final consumer lock inspection changed only the selected runtime nodes:
workspace ebe612f8 URL/hash in its existing nested input, configuration
only devWorkspace. Both retain extension/siblings; cross-consumer contract
passed. New exact CI is 38290319369; prior 97ce087 CI succeeded, no superseded
runs remain live. The next batch runs the remaining browser lifecycle check,
final application (including packaged tests) and aitherdev builds, and exact CI.
Previously passed VM scenarios need no duplicate local rerun for the two DOM
presence guards; CI independently covers its configured full checks.


## Pause, deployment and shutdown-context correction: historical checkpoints

The following checkpoints were recorded as work progressed. Their pending actions
and intermediate revisions are historical; state.md and rollout.md contain the
verified final outcome.



The user requested pause during final application verification. The parent
instructed /root/archive_final_builds to stop only its owned foreground local
batch, preserve logs and report actual cancellation. Remote CI is left alone.
No deployment, original-session archive or default-branch integration occurred.
Resume with the cancellation report and final-* logs/statuses, then run only
uncompleted required checks before the prepared rollout.

Cancellation confirmed: final application build interrupted through the owned
foreground handle after about six minutes. Exit 1 is user cancellation, with
`error: interrupted by the user` in final-application.log, not a product-test
failure. No owned batch process remains. Aitherdev build and CI watch never
started; remote GitHub workflow was not canceled. Browser lifecycle and archive
regressions already passed. Next on explicit resume: finish remaining checks,
then execute the prepared deployment and requested original-session archive.

User explicitly resumed. Published source heads remain unchanged and clean;
resume only uncompleted builds/CI with a fresh watcher and resumed-* evidence.
Completed review and browser checks remain applicable.

Predeployment baseline changed during the user pause: systemd reports native
Codex restarted at 20:37:07 CEST, before our deployment. The selected application
profile remains the predecessor and Codex remains 0.160.0; tmux PID is unchanged.
The cause of that external restart was not established. Initial evidence is
preserved in live-before.json; live-before-deployment.json records the verified
current process/socket for deployment continuity. No restart by this task is
claimed or hidden. Final live checks compare against the new explicit baseline.

Resumed application build passed (resumed-application.status 0). The same fresh
watcher continues aitherdev build and exact CI. Review and source heads unchanged.

Final resumed batch completed successfully: application/package and aitherdev
builds exit 0; exact CI 38290319369 success. Fresh Luna/low utility
/root/archive_resumed_builds retained complete resumed-* logs and statuses,
14m13s total, no remaining handles and no local kernel compilation.
Deployment is now authorized and starting under parent ownership.

Host and application deployed successfully. Both confctl health checks pass.
All five user units are active; native and tmux PID/socket match the explicit
predeployment baseline. Own and network session pages return 200 with v36 assets.
Installed artifact command and instructions verified; actual typed registrations
for owned verification history/live evidence succeeded. Live read-only Chromium
and Firefox probes verify one Archive submit, neutral archived mode and exact
target identity, zero page errors, and zero forwarded mutations. Logs deploy-*
and curated live-after.json record acceptance. Only requested archival remains
before final handoff; no default integration authorized.

### Shutdown-context correction

The real archive attempt exited1 before worktree removal or journal capture.
Cause: Ruby omitted --workspace and --user-state-root for Go quiesce-explicit;
Go correctly refused to preserve queued prompts without private storage. Fixed
by passing the already selected context, preserving every existing format and
policy. Focused Ruby regression passed1run/8assertions; real Go CLI private queue
fixture passed, syntax/whitespace/consumer deployment contract passed. Two test
harness setup errors (standalone module lacked shared NullTmux, missing fixture
manifest) were corrected; they were fixture setup errors, not product failures.
New helper regression runs through aggregate Ruby harness. Original logs/rollout
SHA remain retained. Do not discard recovery hold. No archive journal exists.

Published runtime1a27453c0b67c8c24cbe1474d5a05607eb698a9a, workspace
d1e5888a9f96e32833d56f5ae18da477df44472b, configuration
1697613eab00a4bb0642b79c355c0b673b758a41. Each input stream consolidated once;
fix folded into owning archive commit. Workspace rebased patch-equivalently onto
current shared mastere76c0c14; inherited new commits are tracking only. Exact CI
38297311907, all superseded runs completed. Same independent reviewer assigned
General/Architecture/Risk bounded follow-up before long corrected-package checks.
No new docs useful: private storage semantics already documented. No database
migrations; failed actual archive wrote no new archive journal/schema.

Correction review completed with no findings; prior unaffected lanes stand.
Fresh /root/archive_corrected_builds Luna/low now owns one foreground related
application/target/CI verification batch, corrected-* logs/status, no deployment.
Policy resolved from actually selected profile catalog437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd;
matching native utility dw_024841fba072af1d79bd78026612eaeca055acfa31ecc89f.

Corrected verification passed all three checks: app package418Ruby/5696assertions,
zero failures/errors,13skips; schema12/50; provider127/994,3skips; all Go packages.
Exact CI38297311907 success. Appyb4mamskfrlzaz71ncp3363bhl4jc6hg and new host
apsqp7fvi89kjc0fxp7gijq03sr4jm3n checked; new host differs in selected input
metadata, so scoped deployment repeats. No original archive journal exists.
Native restarted at21:18 before corrected deployment (NRestarts0, normal systemd
stop/start). Cause not established; native0.160.0 verified. Both previous baselines
and first postdeployment evidence retained; live-before-corrected-deployment.json
records new actual process/socket for continuity, not an unchanged-generation claim.
Parent owns corrected deployment; fresh observer watches corrected-deploy-* only.


## Final acceptance

Corrected application and aitherdev builds passed. Exact CI 38297311907 passed.
Parent deployed the corrected host and user-profile application, with both health
checks and all five user units active. Final live verification preserved native
Codex/tmux process and socket continuity against the explicit corrected baseline.

The normal explicit archive command completed with exit 0 and committed the
selected tracking transition as 8df4f006. A fresh Luna/low observer then ran the
read-only recovery verifier: exit 0, ten fully verified snapshots, every checkout
and Git registration absent, heads/branches retained, neutral archived lifecycle,
and no unfinished journals. Parent verified archived portal GET 200/read-only,
absent tmux session and absent runtime authority. No revival was performed.

The temporary application GC root was removed only after confirming that the
selected user profile retains the exact final application. All utility handles
are finished. The three published source worktrees remain clean and unmerged.
