---
lifecycle: complete
---

# 2026-10-25-archive-unmanaged-files-investigation

## Status


**Complete: merged, deployed, verified, and released.** Remote masters contain
runtime `960dd816`, configuration `270d348a`, and workspace `3e72f394`. Final
feature CI and all four post-merge master CI jobs passed, including host tests.
Aitherdev runs system `w1m7vv5c` and workspace package `fqajxhsm`. Live portal,
models, naming, process continuity and the disposable archive acceptance passed.
All three repository claims and machine claim `41f1b026-5b5f-400c-8148-99a6df008c20`
are confirmed released. No work or blocker remains. The actual initiative stays
open, with its worktrees/branches retained; it was not an archive test target.

- [x] Recover the blocked HaveAPI archive on attempt 2.
- [x] Implement/review archive preparation and both creation lock fixes.
- [x] Pass final-head full feature CI and final artifact builds.
- [x] Deploy system then profile; pass health/naming/continuity/archive acceptance.
- [x] Obtain explicit "merge and release" direction for the three master targets.
- [x] Reconstruct and certify the clean workspace rebase over tracking/notes.
- [x] Fast-forward/push all three masters; release each short repository claim.
- [x] Prove deployed runtime, extension/client dependencies and equivalent workspace
      lineage integrated; recheck live effects and release owned machine claim.
- [x] Preserve unrelated shared changes/index and remove only temporary merge targets.
- [x] Diagnose failed post-merge archive job with a deterministic known-reader reproduction.
- [x] Review/verify the archive/worktree/startup/recovery follow-ups and deploy them.
- [x] Finish post-merge master CI, including the host job.

## Integrated heads and live deployment

- dev-workspace/master: b974f2f3f83792a494610d1ea03f3d69e97bc1a4.
- vpsfree-cz-configuration/master: 6428e280f06bffabef829a1335b36bac6cad5b9d.
- workspace/master: 9c4c97cd1d49232cb930ff5037ae124295f04f0f.

Original deployed workspace source ffadbf5b is preserved under a retained local
refs/dev-session-deployments/ initiative ref. The installed certification engine
reconstructed the exact final 9c4c97cd tree from its reviewed pin over only
tracking/notes changes. Original independent review and migration inventory,
range-diff, reconstruction and quick verification are retained in
workspace-review-reuse.json and adjacent evidence. No application behavior or
runtime/client/extension selection changed; no additional deployment was needed.
No claim of literal old-ffadbf5b ancestry or identical package derivation is made.

[Rollout](rollout.md), [lineage](integrated-deployed-lineage.json),
[downstream review](deployment-review.md), [archive acceptance](deployment-archive-watcher.md).
Both system links select g4kzll8p; the user profile still selects bhi44p5i.
Fresh health check returned 200 and all conversation/portal/router services are
active. Native Codex 0.163.0 and its running processes were preserved during the
rollout. Extension 767dfd58 and codex-web 8b60554b are freshly proven ancestors
of their own remote master branches. All owned jobs/legacy integrations are settled.

Machine release was verified through ordinary claim-status after release, with
owner d9056db0-2d6a-463d-ba75-ef6622366976; all three repository claims were
released immediately after each verified push. No receipt or journal was edited.
Unrelated shared staged/unstaged changes and untracked names were compared before
and after workspace integration under the short tracking lock and preserved.
Original configuration checkout was not switched or cleaned. Feature refs and
registered worktrees remain; no archive, deletion or stop was requested.

[Master CI 40229910427](https://github.com/aither64/dev-workspace/actions/runs/40229910427)
checks exact b974f2f3 after merge; the earlier full feature run 40223710351 passed.
Fresh native Luna/low watcher owns only this new run's observation. No new push-triggered runs were created in
configuration/workspace; configuration has unrelated scheduled Daily update history. No machine claim is held during CI.

## Source and history

Runtime implementation is in `dev-workspace`; deployment additionally pins
`vpsfree-cz-configuration` and workspace composition. Runtime branch
`2026-10-25-archive-unmanaged-files-investigation` is published over SSH at
`b974f2f3f83792a494610d1ea03f3d69e97bc1a4`. Its clean worktree is
`worktrees/2026-10-25-archive-unmanaged-files-investigation/dev-workspace`.
Review base and pre-integration origin/master:
`9634151b9836311c331a58880fbb4c46133fd98f`. Current master includes the final head.

Final series:

1. `e4f6180fa7340335db0d0db8033d164639985e78` — archive readiness before shutdown.
2. `5e4e99dfecfda94da47c10cd154dfa98269a6533` — durable portal lead-assisted repair.
3. `a27fd38e` — reject occupied name candidates before requesting runtime EX.
4. `b974f2f3f83792a494610d1ea03f3d69e97bc1a4` — wait for accepted-plan source readers before destination/provider admission.

The independent review assessed the complete four-commit series and final diff:
no obsolete approaches, redundant fixup history, repeated input/dependency/update
streams or migrations. The final saved comparison and remote head proof bind the
exact base/head above. The user subsequently authorized integration; see current status.

## Outcome and root causes

Explicit Archive checks readiness while the lead remains available, asks it to
repair local blockers, and rechecks after each completed repair turn. It stops
after three cycles without progress or when operator input is required. Native
message identities survive retries, cancellation revokes continuation, and portal
restart resumes durable preparation. Other sessions remain usable. Automatic
archival and existing destructive-phase journal recovery retain their policies.

The creation failures were reproduced with a real portal queue/reconcile SH
lease. Naming tried to take an occupied session's runtime EX before recognizing
the collision; it now rejects/skips known occupied names before mutation locks
and still proves unused candidates under both locks. Plan initialization tried a
nonblocking source EX from inside destination/provider admission; it now waits
before that admission and revalidates the exact source after obtaining EX.
Cancellation, source replacement and journal-bound recovery remain covered.
The original CI holder PIDs are unavailable, but both causal mechanisms are
reproduced with identified application holders and corrected.

## Verification and independent review

[Verification](verification.md), [creation root causes](creation-contention-findings.md),
[creation final review](creation-contention-review.md), [initial archive review](review.md),
[archive follow-up](review-followup.md), [recovery](recovery.md), [design](design.md),
[earlier implementation history](implementation-history.md), [handoff](handoff.md).

[CI run 40223710351](https://github.com/aither64/dev-workspace/actions/runs/40223710351)
passed on final head b974f2f3, attempt 1: creation, archive and fast/package jobs
all successful. The standard master/manual-only host VM job was skipped.
The watcher observed completion in 1226.2s. New/related Go regressions and
9 Ruby tests / 117 assertions passed before final review; the reviewer reran the
new tests (web 3.091s) and the Ruby regressions independently.

Risk is high because this changes lifecycle/creation synchronization. All four
review lanes were applied. Initial archive reviewer /root/final_review used the
installed default gpt-6.1-sol/xhigh fallback for this tracking-only initiative.
Its identity was unavailable for the creation follow-up, so a fresh standalone
reviewer used the same installed policy: native thread
`01a17467-084f-7932-b2f0-cf4352265c1e`. Its own rollout verified model/effort,
approval never and danger-full-access execution; assignment stayed read-only.
It reported no findings and explicitly assessed full history/migration lineage.

Fresh verification utility thread `01a1746d-9592-7783-b2ff-ac4e8ba68de5` used the
installed gpt-6-luna/low policy, with actual settings verified from its rollout.
It owned only exact-run CI observation, with no retries, edits or diagnosis.
See creation-contention-watcher.md and the adjacent untracked launch/status/log
artifacts. Catalog digest:
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`.
Both native utility/review processes have finished; no owned runner or guest is
left active. Tracking updates remain in the working tree under the daily
checkpoint cadence; project-code commits are published.

## Documentation, compatibility and limits

The runtime archive guide, session guide, preparation guide and README describe
supported behavior and verification. The creation fixes document occupied-name
handling and source lock order in docs/session-preparations.md and
docs/dev-sessions.md. Session-local findings preserve the incident evidence.
Reusable lessons are in notes/dev-workspace/2026-10-25-creation-lock-order.md and
notes/dev-workspace/2026-10-25-ruby-package-layout-dependencies.md.

Archive preparation is private schema-1 state. Existing receipt/journal/native
protocol formats are unchanged. A predecessor-reader/continuation VM passed on
archive head 5e4e99df; the later creation fixes do not change that persistence
boundary. Final-head packaged creation/archive CI supplies current acceptance.
The reviewed package is now deployed; see rollout.md. Later I/O failures or external writers can still
require normal journal recovery after shutdown; lead revival in that phase is
outside the accepted design.

## Next action

Finish observing the exact post-merge master CI run and reconcile its result.
All approved integration and release work is complete. Keep the initiative and
feature refs; no lifecycle closure was requested.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-archive-unmanaged-files-investigation/

## Explicit integration and release direction

User now directs: "merge and release". This covers the three reviewed/published
initiative branches into dev-workspace/master, vpsfree-cz-configuration/master
and workspace/master, followed by releasing this initiative's aitherdev claim
after complete deployed-lineage and live-effect proof. Keep branch refs. No
archive, deletion or stop is requested. Fetch and prepare outside repository
claims, reconcile moved baselines with patch-equivalence and applicable checks,
then claim one repository at a time only for final checks, fast-forward merge,
hooks, push and exact remote proof. Workspace integration also uses the shared
tracking lock and preserves all unrelated dirty/index files. Machine claim stays
held until verified deployed dependencies are integrated and command effects settled.

### Integration preparation

Runtime b974f2f3 and configuration 6428e280 remain exactly reviewed, clean and
fast-forwardable from current origin/master. Workspace was cleanly rebased to
9c4c97cd1d49232cb930ff5037ae124295f04f0f over shared tracking master
fe4f9ff1bf0a6af24d83327018c053ef84148c8f. Incoming baseline paths are only
work/, archive/ and notes/; the sole outside-tracking note records the earlier
Ruby package-layout lesson. No application source or dependency changed.
Installed Certification.prove reconstructed the exact final tree from the
original reviewed patch; range-diff matches the one pin commit. Original review
receipt, full proof and review-reuse evidence are retained. No migrations or
repeated update streams. Exact original deployed workspace head is retained under
refs/dev-session-deployments/2026-10-25-archive-unmanaged-files-investigation/workspace.
Deployment contract and its 4 tests/19 assertions passed again on the final range.
Original live package remains selected; no claim is made that its derivation is
the new composition derivation. Integration uses the certified source-equivalence
boundary; no changed runtime behavior needs deployment.

## Post-merge archive CI follow-up: worktree registration

Master CI 40229910427 failed only archive (job 121279205759); creation, fast and
host passed. Exact b974f2f3. Failure is worktree add immediately after native
session start: "another dev-session command is changing ...". Earlier archive
run at the exact same head passed. Do not rerun unexplained failures. Historical
holder PIDs are not present in the retained VM log; diagnostics also show a
portal shutdown timeout, recorded separately without assuming it caused this lock.

The worktree command intentionally rejects competing exclusive session writers;
Ruby test_worktree_mutations_use_the_slug_lock asserts this. A blind wait:true
would change that contract. Reproduce with an identified actual portal
queue/reconcile SH admission on the same device/inode, then scope the fix to
worktree-add: on EX/NB contention, a successful SH/NB probe identifies compatible
readers and permits waiting for EX. A failed SH probe keeps writer refusal.
Use the existing host-lock helper with one optional internal flag, passed only
from worktree-add via with_slug_lock. Keep all actual validation after EX, retain
existing provider/lifecycle/generation locks and refusal behavior, and introduce
no new lock file, state format, restart, global lease or generic retry loop.
Other commands retain their current behavior.

Quick acceptance: deterministic Go/Ruby boundary regression with real Git
worktree creation and identified Go SH holder; prove no mutation before release,
unrelated slug worktree registration remains usable, and writer EX still refuses.
Run focused Ruby worktree/lock tests and related Go tests. Record pre-fix failure.
Commit one forward-only fix (b974f2f3 is already merged), run applicable independent
review before the archive VM/CI. Reconcile exact tested source, downstream pins,
deployment need and approved integration scope after the fix is concrete.
No machine or repository claim is held for this work. Earlier three merges and
machine release remain complete. Initiative stays active until follow-up settled.

### Post-merge follow-up quick verification

Master CI failed archive only; creation, fast and the master-only host VM passed.
The actual earlier VM holder PID is unavailable. A deterministic real Go portal
queue/reconcile SH admission on the same inode reproduces its exact Ruby busy
error at worktree_add; the pre-fix log retains that failure. The scoped shared
probe correction passes real Git registration after reader release, leaves the
checkout absent while waiting, permits unrelated slug registration and still
refuses an active EX writer. Go related creation/plan/new tests pass in 4.473s.
Ruby worktree/observation/writer regressions pass 9 tests/134 assertions.

A broader native Ruby selection also exposed an existing test fixture without
its required ordinary manifest. Exact already-merged b974f2f3 reproduces the same
failure (1 test/12 assertions/error). Initial baseline filter syntax selected no
tests; corrected slash-delimited filter executed the actual failure. The separate
test-only fix initializes explicit fixture tracking before startup; native tmux
verification now passes 1 test/44 assertions. The production refusal is unchanged.
This remains separate from the worktree-reader implementation commit.

All intended follow-up changes are committed; independent review is next, before
new long CI/VM checks. No deployed package, master ref or resource claim changed
while diagnosing. The prior three merges and machine release remain complete.

Current follow-up source head: b75a6a1065449743b6a3c2f859b44bc32fefdc40

2a58cf4937d035dd8688aaae92d9e997c3efdb63 worktree: wait for portal readers during registration
b75a6a1065449743b6a3c2f859b44bc32fefdc40 test: initialize explicit scope in native worktree fixture

### Follow-up review and final pins

Retained independent reviewer cleared b75a6a10 in all four lanes with no findings;
review includes exact two-commit unmerged range, known-reader reproduction,
exclusive-writer compatibility, two simultaneous shared upgraders, and independently
passed 10 Ruby tests /178 assertions plus Go boundary regression. Historical VM
holder and portal timeout remain outside what that reproduction proves.

Published final heads: source b75a6a1065449743b6a3c2f859b44bc32fefdc40,
configuration fc713f7cae75f91c4d4669ec4b405d035c2393e8,
workspace eb08828454e20acbed21dbcf5f42a9108bfe5242. Downstream changes are
mechanical pin-only updates (one new commit each over their already merged
previous heads), not new configuration logic. Parent semantic checks prove only
the runtime lock node/URL changed, with extension/native/siblings/follows preserved;
deployment contract passes. Generated configuration hooks passed. Exact comparisons
retained. No repeated unmerged update streams, migrations or obsolete history.
The earlier pin commits are protected merged history and remain intact.

This is a bounded compatible correction to the already authorized lock-contention
work in the same three approved repositories/master targets. Existing active-writer
refusal and state/API formats stay unchanged. Continue the user's deployment,
merge and release direction for this narrow remediation; no new repository, product
capability or unrelated infrastructure operation is introduced.

Fresh utility is building the final committed artifacts then observing source CI
40233127533, without retries or activation. All claims remain released during
preparation. Any later activation requires a fresh machine request/claim.

Initial follow-up verification utility 01a174de-37df-7e42-bd22-f2072a41fd55
stopped before any build/CI observation: its requested relative log/status files
made the source checkout unclean. Parent moved exactly those owned monitor files
to tracking, preserved evidence, improved the preflight diagnostic and verified
all three worktrees clean. Fresh utility launched with absolute tracking log paths;
no product check or workflow was retried. No package or claim changed.

## Retry race reproduction and correction

Follow-up exact CI 40233127533 passed registration/lead repair but failed retry
after checkout removal. Captured GETs with no POST match the deterministic
browser reproduction: release a background refresh of the same receipt while
Retry awaits its details preflight. Before correction, expected one mutation
remains zero (retry-race-before.log/status, 22 seconds). Preserve cancellation
on a changed receipt/target/options/state and page suspension; compare the
retry-relevant snapshot rather than decoded object identity. Diagnostic text
and timestamps do not confer retry authority. Regression adds same-receipt
success and changed-receipt cancellation. Source comment owns this invariant;
existing recovery docs remain applicable, with no new operator procedure.
No API, persistence, native Codex, or migration change. The historical portal shutdown
timeout lacked a stack; the same startup cancellation defect is now reproduced
and corrected independently, without claiming its exact historical ordering.

Retry guard commit 78077b0e: quick syntax/whitespace and deterministic Chromium/Firefox
regressions pass (retry-race-after.log/status, 28.30 seconds). Independent retained
reviewer01a17467 resumed for all affected lanes and complete b974..780 history.
Original three masters and live profile remain unchanged. No resource claim held.

Startup wait root cause reproduced: startup-cancel-baseline.log contains real
SIGTERM failure and Go stack in constructor reconciliation waiting for package
transition admission. Missing authority/metadata fixture failures were repaired
and are not root-cause evidence. Committed496ae1b4 passes quick real-signal,
existing shutdown, constructor/worker lifetime and preparation confirmation
checks. All affected lanes assigned to retained reviewer01a17467. Current780
CI/builds remain immutable intermediate evidence; not the final release.
Docs workspace-portal.md now describe cancelable startup admission and preserved
park-before-cancel worker shutdown. No migrations/public request/state changes.

Intermediate780 verification: both final local builds and archive/fast CI pass;
creation fails later with completed plan but a permanent runtime recovery busy
error. No rerun. Bounded typed-contention classification fix planned above.
Startup review Important finding reproduced: canceled attachment claim returned
nil and persisted failed. Narrow correction4fc8ba11 now propagates cancellation,
checks before worker launch, and preserves accepted bytes; focused checks pass
(startup-attachment-before/after logs). Source history remains four logical
commits after amending the unmerged startup fix; no state/API/migration change.

Recovery contention correction960dd816: real SH and EX ownership yield temporary
recovery without manifest/journal/authority/native effects; release restores
retained-root. Ruby4/82 and Go recovery retry policy0.116s pass. The initial
standalone Ruby command lacked shared NullTmux definitions, and the first Go
fixture socket exceeded Unix path length under the long Nix-shell TMPDIR; use
the aggregate Ruby runner and TMPDIR=/tmp inside the dev shell for these checks.
Those setup failures are not product regressions. Full source b974..960 under
retained independent related review, with startup Important finding fixed in4fc
and existing source content/consumer histories preserved.

Final published candidate heads: {"dev-workspace": "960dd816b7e56cbdd4af0da15bf0b26257775151", "vpsfree-cz-configuration": "270d348a29a832e552a798ba8bb467152a2d36d6", "workspace": "3e72f394a73c33be71fcdc1313d05cc74abb802f"}
Source related review clear, prior Important resolved. Mechanical consumers
consolidated to one pin each and semantic graph/contract passed; final independent
history assessment running. Fresh watcher owns final CI40238397116 and builds.
No follow-up integration, activation or resource acquisition yet.

Final consumer/source history assessment clear in startup-final-consumer-review.md.
All final heads clean; current full series/diff agrees with review, as saved in
startup-final-history-inventory.json. Each consumer has one final generated update,
no superseded source approach or migration remains. Retained independent reviewer
01a17467/gpt-6.1-sol/xhigh confirmed all affected lanes and final history.
Final builds/CI remain pending; no follow-up resource claim is held.

Final feature archive VM diagnostics reviewed: no portal stop timeout (exact
run40238397116/job121304766832). Machine and merge claims remain released; only
post-merge CI40239653867 remains. Stable portal URL is unchanged.

## Final completion evidence

- Source: `960dd816b7e56cbdd4af0da15bf0b26257775151`.
- Configuration: `270d348a29a832e552a798ba8bb467152a2d36d6`.
- Workspace: `3e72f394a73c33be71fcdc1313d05cc74abb802f`.
- Final source review: recovery-contention-review.md; consumer/history review:
  startup-final-consumer-review.md. All lanes covered; prior Important resolved.
- Feature CI: https://github.com/aither64/dev-workspace/actions/runs/40238397116.
- Master CI: https://github.com/aither64/dev-workspace/actions/runs/40239653867;
  fast/archive/creation/host all passed. No process remains running.
- Final heads remain clean and integrated, including any later tracking-only
  master advances. Exact proof and all four released claim IDs are retained in
  startup-final-completion.json; deployment/health/lineage evidence in rollout.md.
- Prepared detached merge checkouts and obsolete owned build links removed.
  Final package roots/profile generations, branches, deployment refs and journals
  preserved. Shared unrelated working/index changes were preserved across merge.
- Daily tracking checkpoint ceiling was already reached; current final records
  stay in the working tree under the normal cadence, without another routine
  same-day checkpoint. Project and workspace feature changes are committed.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-archive-unmanaged-files-investigation/
