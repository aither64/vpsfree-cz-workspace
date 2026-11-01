# 2026-10-25-archive-unmanaged-files-investigation

## Goal

Implement the accepted archive preflight and lead-assisted cleanup plan. First
repair and retry the original `2026-10-22-haveapi-release` archive, then add a
read-only readiness command and durable portal preparation before agent shutdown.
The user explicitly requested implementation after accepting preflight-only repair
and progress-based retries (stop after three completed cycles without progress).

## Affected repositories

- `dev-workspace`: archive discovery, journaled cleanup and portal feedback.
- Coordination workspace: this initiative's tracking and evidence.
- `vpsfree-cz-configuration`: starting location; no configuration changes needed.

## Approach

Preserve the investigation in findings.md. Move the verified hook cache inside
its canonical checkout and retry the retained portal operation. Implement on the
registered dev-workspace feature branch, with design in design.md. Complete quick
checks and commits, independent review, then packaged integration tests. Preserve
master branches; implementation does not authorize their integration.

## Decisions

The approved plan supersedes the earlier investigation-only scope. Repair is
limited to the reported session and its original archive intent. No generic
auxiliary-file deletion and no lead revival after partial destructive archival.
The existing threadless initiative has no retained team; implementation stays
with the lead, with catalog-resolved independent review and verification watchers.

## Compatibility and deployment

Keep archive journal formats and strict automatic archive policy unchanged.
Preparation is private portal state, never a lifecycle reservation. Package
transitions park preparation as retryable failure; supported packages must never
leave an old portal receipt permanently running because of unknown preparation.
Recheck generation, session target and native message identity at each boundary.

## Documentation

Readers: the operator deciding on repair and developers implementing prevention.
Keep the original incident findings and proposal in [findings.md](findings.md).
Supported behavior is documented in the runtime's archive and session guides;
its README describes the native lifecycle verification path.

## Testing plan

Cover structural blockers without agent shutdown or journals, lead repair
progress and no progress, uncertain delivery, restart/browser closure,
cancellation and stale identity. Verify unrelated operations remain available.
Run focused checks before independent review and packaged lifecycle tests after
review. Retain all live-recovery results in state.md and recovery.md.

## Authorized creation-race follow-up

The user's instruction “if you found a problem, then you must find the root cause
and fix it” extends this initiative to both creation CI lock failures. Reproduce
with identified application lock holders, fix collision selection and plan-source
lock ordering, add meaningful regressions, review, then verify packaged creation
and archive workflows. The existing feature review and passing checks remain
historical evidence; final readiness requires the extended work to pass too.

## Authorized aitherdev rollout (2026-10-25)

User direction: "deploy aitherdev using vpsfree-cz-configuration". Deploy the
reviewed/published runtime b974f2f3f83792a494610d1ea03f3d69e97bc1a4 without
integrating any feature into master. Extend scope to initiative-owned configuration
and workspace-composition worktrees. Preserve shared master checkouts and all
unrelated files. Exact runtime selection uses configuration channel dev-workspace /
role devWorkspace and the workspace direct nested override; retain extension and
other inputs. Build final committed artifacts before ownership, then acquire
vpsfree:aitherdev and dry-activate/switch system before the ordinary workspace-host
profile switch with the held claim and exact session identity. Use the installed claims workflow and the current configuration site guide
docs/operations/codex-providers-aitherdev.md for ordinary confctl deployment.

Verify exact system/profile identities, contract, portal/router health,
conversation continuity and a disposable creation/archive acceptance. Use normal
forward profile recovery for interruptions, retain original journals, never
reboot or force release. Keep the machine claim while deployed feature lineage
remains unintegrated. No new database/state migrations are introduced by pinning.
Individual rollout evidence lives in rollout.md; source behavior remains in
runtime docs. Readers: operator continuing deployment/recovery and merge reviewer.

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
