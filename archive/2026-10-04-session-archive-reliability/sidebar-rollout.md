---
lifecycle: active
---

# 2026-10-04-session-archive-reliability

Current phase: deployed UI; remaining archival and prepared corrected deployment.

The previous reliability rollout is complete and merged; its result is preserved
in [completed checkpoint](completed-before-sidebar.md). The user approved the
[sidebar/archive plan](sidebar-archive-plan.md), including abandoned archival
when completion cannot be proved, while preserving unfinished work and refs.

Latest steering: deploy the UI for review, but do not merge any of these feature
branches automatically. Runtime, workspace and configuration remain on retained
feature refs until the user approves the UI. Do not wait for CI.

The cutoff is 2026-08-31 inclusive. Exactly 141 active records are selected,
excluding 2026-06-15-vpsadmin-events and 2026-07-24-ct-start-hang. The two dirty
checkouts are preserved in verified backups, and the three missing-ref records
have exact local refs restored. Main owns the
private loop, preservation, failures and deployment; retained implementer0 owns
this bounded UI edit and reviewer0 final review. No roster or settings changes.

Phase checklist:

- [x] Approved scope, preservation choice and merge hold recorded.
- [x] UI implementation and quick checks.
- [x] Independent review.
- [x] Matching deployment for UI review.
- [ ] All 141 requested archives, preserved work and live verification.
- [ ] User UI review and explicit feature integration approval.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-04-session-archive-reliability/

## Sidebar implementation and quick checks

Retained implementer0 committed the shared menu as `27f6c2686b46516d64d87e033161e22b197dd682`.
Main applied the writing skill to final navigation copy and accepted it unchanged.
Nix Node syntax checks and the two focused Go template tests passed. The fresh
Luna/low utility passed the real page-lifecycle browser scenario in Chromium and
Firefox, including keyboard access, dismissal and compact placement (20.62s).
Workspace/configuration locks select the exact runtime; the deployment contract
check passes and changes no sibling input. No migrations or persisted-format/API
changes. All new feature content remains unmerged.

The selected archive records included 85 existing plans without prior commits.
Tracking checkpoint `303c206fb180736d3b18f3178960f4a908b9965c` preserves their
content with active state before ordinary archival. The private 43-line shell
loop covers 141 selected rows (128 completed-mode attempts, 13 empty sessions
archived as abandoned), sequentially with per-row logs and a failure queue.

## Independent review

High-risk classification covers deployment ordering and the authorized archival
operation; the UI itself is bounded and reversible. Retained reviewer0
`01a10867-4791-78a1-995f-f81a027350c5`, actual gpt-6.1-sol/xhigh/read-only,
reviewed all four lanes in turn `01a11042-8ab8-72c0-8f8e-6da33dbf83a7`.
Reviewed source heads: runtime `27f6c2686b46516d64d87e033161e22b197dd682`,
workspace `1414fcbaa682fdc289ac1e00bf2dbe7c91112744`, configuration
`2ab105a5246bb3ba40e2bc2774e4e1db85ae5ead`. Complete new 1/1/1 commit
series is clean, with no obsolete approaches or migrations. Prior runtime
changes were merged/deployed/consumed and remain intact.

One Important operational recovery finding was resolved: the private loop now
skips a moved archive only when both native archive journal and cleanup sidecar
are absent. Reviewer checked the correction and reported no remaining Blocking,
Important or Advisory findings. Bash syntax and exact selection checks passed.

The initial package/host build and deployment passed as recorded below.
Feature merges remain withheld for UI review.

## Deployment, 2026-10-06

The package build passed in 557.93s and the host build in 92.72s. Packaged
checks: 391/5118, 12/50 and 122/913 runs/assertions, zero failures/errors,
15 existing skips. The temporary /build helper-alias warning is unchanged and
did not affect the result. Application switch (80.71s), generation dry-activate
(17.74s), and host switch (26.86s) all passed. Host generation
`2026-10-06--10-28-46` selects runtime `27f6c2686b46516d64d87e033161e22b197dd682`.
Actual profile `/nix/store/gr9xh9gs6sxdimmrgy6blq222qpdlhzv-dev-workspace-0.2.0`
and system `/nix/store/qrvi288lar4x4ri4jdplxp1ncg0bpsfl-nixos-system-aitherdev-26.05.20261004.0d9e9b8`
match built outputs. Portal, Codex, router, tmux and hourly timer are active.
Live index serves app.js v25 and the shared menu, with no redundant Workspace
heading or main-page Automatic archival link. No source feature was merged.

The private sequential archive loop has started after successful deployment;
a fresh Luna/low utility observes its logs/counts and portal responsiveness.

## Archive recovery in progress

The first private loop inherited umask 077 into the archive child, producing
0600 state/manifest files instead of the sealed 0644 projection. Main restored
only those file modes after independently matching all five immutable journal
hashes; contents and journals were untouched. The loop now runs ordinary archive
children under umask 022, uses each saved journal mode, and falls back to the
approved abandoned mode only after a completed preflight refusal without an
accepted journal. The first moved record resumed successfully.

Two dirty checkouts have exact private file backups, binary/staged patches,
checksums and recovery instructions in their own state records. Only the saved
paths were moved/restored; branches and original heads are retained.

The github-event-verbosity record explicitly reported deletion of both feature
refs. Main restored its exact recorded historical bot head and independently
corroborated configuration head locally. Remote refs were intentionally deleted
by the original work. A bare-clone push hook required its worktree configuration
and refused; no hook was bypassed. Approved abandoned archival retains the exact
local refs without needing republished branches. No source/default was changed.

A pending shared-workspace/master archive exposed a genuine self-invalidation:
tracking commits advance master and fail feature-head equality. Retained
implementer0 completed the bounded correction: shared-default monotonic
ancestry with exact sealed final-head retention; all ordinary feature equality,
identity, journal and recovery checks remain. No new formats/migrations were
added. Independent final review passed before source-based native recovery. The
deployed sidebar remains available and all feature merges remain held.

## Shared-master correction and matching pins

Runtime `4c3ea2eb3b82b572e86f23ec7f9e53a0f1dc6a0c` fixes archival
self-invalidation when shared master advances. Seven focused Nix regressions
passed with 279 assertions, zero failures/errors/skips. Main applied the writing
skill and accepted the short invariant paragraph/error unchanged. Retained
reviewer0, saved gpt-6.1-sol/xhigh/read-only, reviewed all four lanes in turn
`01a11085-558e-7a41-9ac0-11f6772e3943`: no findings; exact sealed heads and
formats preserved. The private source entry retains the installed full host
invocation/generation/transition guards and changes only the reviewed executor.
Its read-only current-session smoke check passes.

Matching workspace `c650b86f83785e2c47ab827e2f0e37f7186e5712` and
configuration `676a73c0d7e1570f2e4c4ebfb0cc8bd0b02b8271` select that runtime.
Only the existing nested runtime URL/lock node and confctl devWorkspace node
change; sibling inputs, extension revision and follows paths remain. Normal
configuration hooks pass; generated width warnings are retained. Contract check
passes. Reviewer addendum turn `01a11095-1398-7121-aaa8-052456fa0a2b` confirms
the complete 2/2/2 histories are sound, with no obsolete approaches or migrations.
Earlier UI/pin commits stay intact because they were deployed and consumed.

The sequential shell was stopped only between native children and reaped. The
reviewed three-worker xargs loop resumed the same frozen selection, original
journal modes and native locks. At the first 40-row milestone, 20 calls succeeded,
20 finished records were skipped, and no failures remained. A fresh catalog
Luna/low utility observes the batch and owns the matching normal package/host
build. Package switching waits for all native journals to finish. No CI wait or
feature merge is authorized; the user still owns UI review.

## On-demand legacy-cluster recovery

The July 2 haveapi-i18n archive reached quiesced phase but its cluster reset
found a legacy temporary directory. Inspection proved that cluster state was
absent, the directory was empty and owned by this user, and no processes
referenced it. Main removed only that empty directory with rmdir, then resumed
the accepted abandoned-mode native journal. Archival completed with exit 0;
no cluster files, socket identities, journal contents or processes were changed.
The original batch failure remains in the attempt log; its separate recovery
is successful.

There were no superseded queued/running workflows to cancel after the latest
feature pushes. CI was not awaited.

The matching corrected package and aitherdev host builds passed in 607.135s
and 96.428s. Generated host generation is 2026-10-06--11-54-16. Deployment
remains prepared while the three-worker archive batch finishes.

The July 10 kb-czech-fixes record had the same empty legacy temporary-directory
refusal, with absent cluster state and no process references. Main used the
same rmdir-only cleanup and native abandoned-journal retry; exit 0.

The already-finished runtime CI run 37443657837 failed in
TestArchiveJournalRetryRefusesASameKindReplacementWhileWaitingForTheLock.
The failing assertion expected immediate replacement reconciliation but observed
the preceding running receipt. The assertion and lifecycle implementation are
unchanged from the already-merged baseline. A concurrent display reconciliation
can change the receipt revision while the test's fresh proposal is being read;
acceptLifecycleReconciliation then preserves the newer revision and returns the
current receipt. This is the inferred timing explanation; the failure has not
been reproduced locally. The executor separately rereads and compares the native journal
after taking its mutation lock, so this assertion does not show execution against
the replaced journal. The local full package build passed this test. No CI rerun
or wait was used as validation; the failed result remains recorded.

The July 13 security-advisory-automation empty-directory retry succeeded.
The July 20 binary-cache-kernels attempt briefly met an ordinary per-session
mutation lock; after the holder had left, its unchanged approved native retry
succeeded. No lock was bypassed and no other command was stopped.

The July 20 kernel-boot-evidence-history and security-advisory-review records
also had absent cluster state and empty unreferenced legacy directories. Their
rmdir-only cleanups and same-mode native retries both passed. At 85 processed
rows, 59 batch calls succeeded, 20 records were already finished and skipped,
and all six originally failed calls had successful individual recovery. The
portal remains responsive.

After the matching builds finished and overlapping recovery commands left the
portal responsive, main increased only the verified running GNU xargs scheduler
from three to six workers with SIGUSR1. No native child was interrupted and
archive commands, modes, locks and the frozen reviewed source head are unchanged.
The watcher continues the same batch and reports unhealthy portal responses.

The Aug 6 node-kernel-history retry completed successfully in its accepted
complete mode. Seven initially failed rows now have successful native recovery;
all parent-owned recovery handles are reaped. Backups of both dirty checkouts
were rechecked byte-for-byte, with exact modes and retained branch heads, after
archival began.

## Completed old-session operation

All 141 selected records are now archived: 67 complete and 74 abandoned, under
the approved retain-work choice. All ten initial failures have successful native
recovery. The final three threadless records passed the unchanged absence check
after other retirements had finished. No native journal, cleanup sidecar or
selected worktree group remains. The only active records dated through August
are the two requested exceptions. Both dirty-file backups and exact retained
branch heads are verified. Matching deployment is now running; feature merges
remain held for UI review.

## Final matching deployment and live verification

Application switch, host dry-activate and host switch passed in 80.14s, 17.31s
and 26.22s. Host generation 2026-10-06--11-54-16, actual application profile
/nix/store/h73nvgmdlwq2ccsnr2499qdlxnj9qrdx-dev-workspace-0.2.0 and actual
system /nix/store/98s4gm1ifnvljbap8hgd6vvg7bb885an-nixos-system-aitherdev-26.05.20261004.0d9e9b8
match built outputs. Portal, Codex, router, tmux and hourly archive timer are active.
Live index, Automatic archival and this session return HTTP 200. The index shows
all 141 selected cards as archived, none active, and only the two exceptions
as active August-or-older sessions. Menu navigation and asset versions are correct.
The six completed one-time archive helpers have been removed from private
maintenance storage. Verified dirty-work backups and operation evidence remain.
No feature default branch was integrated.
