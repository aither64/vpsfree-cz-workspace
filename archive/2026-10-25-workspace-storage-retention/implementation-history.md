---
lifecycle: active
---

# Workspace storage retention

Phase: independent review complete; narrow remediation and packaged verification. User said "Implement the plan" and authorized
tracking plus aitherdev deployment, without default-branch integration.

- [x] Read approved plan and applicable workspace procedures.
- [x] Create this initiative through installed dev-session (threadless tracking).
- [x] Record design, create owned worktrees and implement changes.
- [x] Commit intended deliverable and pass quick checks.
- [x] Independent whole-branch review and remediation.
- [ ] Packaged/native checks and exact host build/dry activation.
- [ ] Publish feature branches, deploy matching host/application, verify and clean.

Created by this conversation using `dev-session start ... --no-codex --no-attach`;
receipt binds slug and portal URL. No pre-existing bound initiative was adopted.
Team list reports no valid lead thread; no roster was created or changed. Lead
owns implementation; final review uses installed catalog standalone fallback.
Initial root disk: 984 GiB, 839 GiB used, 96 GiB available (90%). Shared workspace
has 203 unrelated modified tracked paths; preserve all unrelated files/index.
Initial records and design belong only to this directory.

## Implementation checkpoint

Owned worktrees exist for all three repositories. Baselines: runtime10bb0475,
workspaceb1b86b2b8 (ordinary registration keeps unknown historical base), and
configurationd12a7737. Configuration hooks installed/signed through its Nix shell.
The default post-checkout hook initially lacked its Gem environment; no hook was
bypassed. Registration retries preserve existing exact owned checkouts.

Implemented compact committed archive inventory schema3/policy3; predecessor
file/index readers remain. Fresh archive tracking retains Markdown/portal.yml.
New workspace feature/retained/scratch checkouts omit tracking. Nix export-ignore
is set in the workspace. Coordinator TTL24h, explicit expire-unused, optional
allocated sizes and deadline reporting, independent completed scratch cleanup.
Busy legacy drivers conservatively retain shared source checkouts because they
can reuse a head before recording it; unrelated completed scratch still collects.

Focused checks passed: new archive/summary/sparse tests3 runs54assertions;
legacy compatibility selected4 runs139assertions; compaction/advanced-branch/
negative ownership selected4 runs85assertions; coordinator selected5 runs28assertions;
maintenance preview/apply/skip2 runs10assertions. Syntax checks pass. These are
unit/fixture checks; packaged/native/integration/host checks have not started.

Workspace stages66320 historical artifact removals, preserving Markdown/portal.yml;
shared historical records remain untouched pending integration approval.
A git-rm invocation over66320 pathspecs was terminated after slow quadratic work;
it made no index publication or file changes. Retried using update-index --stdin.
The sparse helper must initialize the no-checkout index via read-tree; verified
with a disposable fixture after discovering the empty-index behavior during setup.

Remaining: finish documentation and verification, commits, review, exact consumer
pins, full checks, authorized deployment, completed recovery compaction and GC.
No shared default branches integrated; no other session's active files removed.


## Final verification preparation

Runtime committed series at this checkpoint: 07311cf3 (archive), 99ea9a34
(sparse checkout), bec074e8 (coordination). Two final archive fixture corrections
remain uncommitted pending the corrected unit batch. Prior direct invocation of
archive_cleanup_test.rb omitted the aggregate fixture loader and produced 42
NullTmux NameErrors; this was a harness failure. The corrected batch selects those
42 cases through dev_session_test.rb, plus GC, collection admission and package
capability checks. A fresh Luna/low watcher owns that single batch.

CI run 40178922312 failed on the uncommitted fixture expectation now being
corrected: test_completed_restore_never_overwrites_later_edits_after_interruption
read an uncommitted sentinel that new archives correctly discard. Its sentinel
must be committed. The legacy symlink full-copy scenario explicitly selects the
predecessor capture policy. Complete failed logs: ci-bec074e8-failed.log.

No deployment or storage cleanup has occurred. Installed coordination policy
requires verified deployment AND integrated deployed feature lineage before
machine release. Because integration is not authorized, a deployment claim will
remain held after successful verification until that condition is satisfied.
Historical tracked archive removals remain confined to the workspace feature
branch; recovery-only compaction is independently authorized after deployment.


## Final committed checkpoint

## dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-workspace-storage-retention/dev-workspace

Base: 10bb047513c82d1310e8fcaa797e8772f948dd8a
Head: 98466eaf48ab68f09a2261cd472f88b26bcebff0

Complete series:

```text
adc2f21ff3837c52889425c049acb527fb12200c
archive: retain committed heads without checkout backups

Keep explicit archive recovery in compact schema-3 records and recreate
clean committed checkouts on revival. Discard uncommitted files and retain
Markdown tracking summaries, while preserving predecessor recovery readers
and partial-capture behavior. Require policy 3 for compact archive records.

73683cf2fd95a57907029303ca1250c002ee91e4
workspace: omit tracking from additional source checkouts

Initialize workspace feature, retained-source and integration scratch
checkouts with per-worktree sparse configuration. Exclude work and archive
tracking before materialization so historical evidence is not copied into
every source snapshot. Keep the shared checkout and other projects whole.

98466eaf48ab68f09a2261cd472f88b26bcebff0
coordination: expire unused payloads after one day

Shorten unused preparation and orphan retention to 24 hours and provide
explicit legacy expiration plus optional allocated-size reports. Continue
collecting completed integration scratch while busy drivers keep shared
sources and their required dependencies. Preserve live work and recovery.

```

Final diff: dev-workspace-final.diff

## workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-workspace-storage-retention/workspace

Base: 00fe575aff47eff8174c77281846f628aafd326e
Head: 0b5fe0dea7c2fee9bd9e37dea949c16c8a005fec

Complete series:

```text
94a49be34930090ae5f5f5660ae504518843ba7f
archive: remove disposable historical verification artifacts

Retain Markdown explanations and portal manifests while removing raw logs,
bundled repositories, downloaded artifacts and generated build output from
the current archive tree. These records accounted for about 4.1 GiB and
were copied repeatedly into worktrees and package source snapshots.

Keep committed history and repository branches unchanged. Historical raw
artifacts remain in prior commits; no history rewrite or artifact migration
is introduced. Shared tracking files change only after approved integration.

38e4c20ae73e705491e672c71f9e7344800bfcb3
workspace: keep compact tracking and provide storage maintenance

Keep Markdown explanations and portal manifests in tracking, and exclude
tracking directories from exported package sources. Document committed-only
archives and the 24-hour coordinator retention policy.

Provide explicit preview/apply maintenance for completed archived records
and private recovery payloads. Preserve active tracking, unfinished
operations, committed heads and the selected package transition boundary.

0b5fe0dea7c2fee9bd9e37dea949c16c8a005fec
deps: select compact archive and one-day retention runtime

Select the reviewed storage policy runtime through the existing nested
input while retaining the independent vpsFree extension and sibling pins.
The matching host contract is selected in the configuration repository.

```

Final diff: workspace-final.diff

## vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-workspace-storage-retention/vpsfree-cz-configuration

Base: d12a77374b18e15fe7600f95307114e2e1882828
Head: 0eebce77abbc3bafdb688e80b243b8cf64c74160

Complete series:

```text
f5d5555785b8d179657c4766b44bdba916727576
docs: describe workspace archive and coordinator retention

Explain the user-profile runtime's 24-hour preparation retention and
explicit completed-archive compaction procedure for aitherdev. Keep the
host GC policy and application ownership distinct so operators use each
tool's preserved recovery and locking contracts.

0eebce77abbc3bafdb688e80b243b8cf64c74160
inputs: set devWorkspace to 98466eaf

devWorkspace: 10bb0475 -> 98466eaf
git log for 10bb047513c82d1310e8fcaa797e8772f948dd8a..98466eaf48ab68f09a2261cd472f88b26bcebff0
> 98466ea coordination: expire unused payloads after one day
> 73683cf workspace: omit tracking from additional source checkouts
> adc2f21 archive: retain committed heads without checkout backups

```

Final diff: vpsfree-cz-configuration-final.diff

Quick unit batch passed (correct-unit-batch.log): archive42/1727, GC39/207,
collection concurrency2/12, capabilities3/9; no failures/errors/skips. Workspace
maintenance2/10 and final runtime composition passed. All intended files committed,
all owned worktrees clean. Independent final packet: final-review-packet.md.


CI run40180103947 reached package Go tests. Archive job121129149095 failed
on TestTrackingFilesArchiveRevive expecting raw tracking artifacts after normal
archive/revive. The approved policy removes those files; the fixture now checks
they are absent in archived and revived listings while Markdown download/preview
checks remain. Full job log: ci-98466eaf-archive.log. This is a narrow fixture
correction, not a product behavior change. Final reviewer is still inspecting
maintenance compatibility; no activation or cleanup has begun.


## Independent review

See final-review.md for full findings, reviewer settings, history/migration
conclusions and direct fixes. Blocking receipt/automatic-eligibility fixes pass
2 regression cases63assertions; Important transition-admission fix passes
workspace3 cases14assertions. No activation/cleanup has occurred.


## Post-review committed heads

Final series and exact heads: final-remediation-heads.json. Narrow requested
fixes and the CI fixture correction were folded into their owning commits.
Both consumer streams regenerated once to ec53874b; extension/siblings unchanged.
Runtime review remediations: runtime-review-remediation.diff. Direct focused checks
pass; no new design, public capability or migration boundary was introduced.
Review is accepted with all Blocking/Important findings fixed.
Exact-head CI40181077743 is running. Local composed package and scoped host build
are running; complete logs/status: composed-build.*, aitherdev-build.*.
No deployment or cleanup yet.


Deployment preparation: first confctl build stopped at its interactive confirmation
without performing a build (aitherdev-build.exit1). Repository CLI declares
--yes for pre-authorized noninteractive builds; rerun aitherdev-build-confirmed
uses it. No deployment effects occurred. Root SSH uses the task's verified
ssh-known-hosts and ssh-config through CONFCTL_SSH_CONFIG/NIX_SSHOPTS; host-key
checking remains strict. System/application selection are still unchanged.


Scoped system build and copy passed: aitherdev-build-confirmed.exit0 (140.8s),
aitherdev-copy.exit0 (92.4s). Built generation2026-10-25--10-35-36 selects
/nix/store/1bnl145ln79094l10j60cp4631a69vww-nixos-system-aitherdev-26.05.20261021.da6dc0e
and runtimeec53874b. No local kernel build. No machine claim acquired yet.
Composed application Ruby checks passed; Go checks and exact native CI pending.


Runtime CI40181077743 passed fast, archive and creation jobs at exactec53874b;
host workflow is deliberately skipped on feature pushes. Composed package passed
(534.6s) and subsequent same-runtime site refresh passed (178.8s). Workspace four
original Nix checks passed. Recovery preview fixed a File::Stat#symlink? argument
error before mutation; real-Git command fixture now proves preview/apply, external
symlink preservation, committed ref retention and repeat application (4/23 pass).
Eligible private recovery:137306112 allocated bytes;84 unfinished bookkeeping and
8 nonterminal tracking records skipped. No cleanup has occurred.

Pure Git fetch validation exposed that .gitattributes needs exportIgnore=1. Added
explicit cleanSourceWith filtering for all workspace package/check source refs and
a tracking-source check; pure committed Git check passed. This source-retention
mechanism is receiving an affected-lane independent review before its long build.
Original native delegation tools became unavailable; replacement standalone CLI
reviewer is native01a1727d-11a8-7f03-8ba0-ae0bb774a578, gpt-6.1-sol/xhigh,
provider codex-lb, approvals never, danger-full-access with read-only role. Actual
launch policy verified in followup-review-execution.log. Reports to
followup-review-report.md. No roster was created or modified.

Historical tracked deletions remain unintegrated. Before applying them to shared
master, reconcile any pending lifecycle/tracking receipts whose exact tracking
bytes they would change. Do not bypass pending digests or alter unfinished data.


Focused final follow-up review passed with no findings at workspaceb94ca3e2;
full report: followup-review-report.md. Reviewer proved pure Git and sparse
evaluation have identical filtered sources/package derivations, preserve all619
non-tracking files and omit unfiltered workspace inputs from every package/check.
No migrations, obsolete history or redundant pins; other reviewed boundaries
unchanged. Final candidate package build running; after it, final five workspace
checks, machine claim and dry activation precede deployment.


A fresh installed-policy CLI verification watcher now observes the existing final
application build (no relaunch): native01a17284-5aac-78b1-ae82-4be072282208,
gpt-6-luna/low, full access/approval never verified from its launch log.
Parent is not polling its build logs. Exact feature publication proof is recorded.


Historical preflight found49116 proposed raw deletions/3526176691 logical bytes
overlap84 archives with unfinished lifecycle/tracking bookkeeping. Before calling
the branch merge-ready, narrow its mechanical deletion to settled archives. This
reduces destructive scope under the accepted never-alter-unfinished-operations
constraint. Changes are confined to archive/ and cannot affect the independently
reviewed filtered Nix source. Preserve exact derivation/input identity proof after
the narrowing before reusing build verification.
