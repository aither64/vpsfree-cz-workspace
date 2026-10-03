---
lifecycle: active
---

# Infra monitoring

## Current status

Phase: ready, awaiting merge approval. Implementation, focused verification,
independent whole-branch review and all four central system builds passed.
The feature branch is published, the project checkout/index are clean, and no
verification operation remains running. No default integration or production
deployment occurred. Session remains open; no lifecycle action/cleanup scheduled.

## Phase checklist

- [x] Investigate current disk/CPU rules, inventory and notification routing.
- [x] Settle machine_type, exact VPS SMS exception and pgnd CPU-only scope.
- [x] Delegate architect design and implementer application work.
- [x] Implement and commit two behavior changes with active declared hooks.
- [x] Pass focused and adjacent checks; keep disk/loadavg/pins unchanged.
- [x] Independent complete-branch review with explicit no-migrations/history conclusions.
- [x] Fix Advisory R1, run focused check and verify rewritten two-commit series.
- [x] Build both monitors and both alerters from exact final revision.
- [x] Publish feature branch, capture portal comparison and prepare handoff.
- [ ] Explicit integration direction for vpsfree-cz-configuration/master.
- [ ] Any separately requested production rollout and live verification.

## Repository and team

- Worktree: ../../worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration.
- Branch: 2026-10-03-infra-monitoring, local and origin refs match.
- Base / freshly fetched origin/master: b66c929bb7c202ad31bd8994a691ade14c40ebf0.
- First: e7b029165e3304e6f1ca4ec7e261d007ff4cab81 (metadata/labels/SMS).
- Final: f725dd3f407b0e5b82c9f9c1ad7720bbc7b14b68 (CPU usage).
- Final tree: 8978bc46c53107705a7dc587c0f036ff6d88a219.
- architect0: design, gpt-6-astra/xhigh, workspace_write.
- implementer0: implementation, gpt-6.1-sol/xhigh, workspace_write.
- reviewer0: independent review, gpt-6.1-sol/xhigh, read_only.
- Retained catalog: 4676433c6831fbaca91da8ffde84891aff6ce065a17c74c2f367f1acf1d15b17.
- Session/current and both lead environment markers matched the trusted binding.

## Verification, review and risks

[Final verification](verification.md) records actual commands/results, exact trees,
build generations, CI observation and remaining operational limits. Focused
metadata/labels/routing/CPU/filesystem and adjacent autostart/process-count checks
passed. Declared Nixfmt/RuboCop hooks ran on both final commits. Full builds
passed for mon1+mon2 (107 seconds) and alerts1+alerts2 (139 seconds).

Mandatory review was High risk because operational notification policy and new
label identities affect rollout, HA deduplication and rollback. Reviewer0 used
saved settings without override/fallback; all four lanes completed. No Blocking
or Important finding. Advisory R1's warning-boundary fixture was corrected and
verified on the final tree. Lead checked that the only change after review was
that fixture; CPU patch was unchanged, exactly two commits remain, no obsolete
history/migrations. Narrow direct verification closed the finding without rerun.

[Independent review](review.md), [branch inventory](branch-inventory.md) and
[implementation report](implementation-result.md) provide detailed evidence.

Material operational limits: no live reload/notification delivery verified.
Relabeling can reset pending alerts; mixed monitor versions may emit distinct
identities and old unlabeled VPS alerts may still SMS. The /run exception remains
accepted even though tmpfs is not dataset-auto-expanded. No migrations or
coordinated exporter/node update is needed.

## Setup and failure recovery

Initial substantive tracking commit: 4123553c; final records follow the
consolidated checkpoint cadence. Public preset replacement was refused; adding
architect/implementer/reviewer from the installed catalog preserved lead policy.
See ../../notes/dev-workspace/2026-10-03-add-members-to-retained-solo-roster.md.

Worktree checkout hook initially exited 78 because pinned gems were absent;
no hook was bypassed. Repeating public worktree add registered the checkout.
Fresh environment watcher installed the frozen bundle (40 gems, exit 0,
61 seconds); implementer installed/signed active Overcommit hooks.
Retained members could not reach the Nix daemon; functional operations ran
through the authorized watcher path. Realized pinned tool variables supported
local static checks/hooks without changing access. See
../../notes/vpsfree-cz-configuration/2026-10-03-retained-member-nix-checks.md.

First focused evaluation failed because synthetic service fixtures lacked
`monitor`. Complete address/port/monitor metadata corrected the fixture; the
subsequent focused run passed. This was not a production defect or design deviation.
Full logs remain local; curated structured results are linked in verification.md.

## Documentation and next action

- [Accepted plan](plan.md), [architect design](design.md), [architect report](architect-result.md).
- [Owning-project policy and recovery](../../worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration/docs/services/monitoring.md), linked from mkdocs Services.
- Next user-owned decision: explicit integration of vpsfree-cz-configuration into master.
  If rollout is requested, update both alerters before either monitor, then both
  monitors promptly and verify effective labels/reload health on each replica.
- No integration approval was inferred from "Implement the plan"; no deploy command ran.
- Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-infra-monitoring/.
