# Current plan decision deployment

Deployed to aitherdev on 2026-09-13. Switching to Plan mode after an ordinary
reply keeps the composer visible. A decision is offered only for a nonempty
native plan in the newest completed turn. During that decision the entire
composer and waiting strip are hidden; drafts, files and uploads are preserved.
Keep planning restores focus. Queue and receipt UI remain available, and
canceling the new-session dialog keeps the decision open.

- User profile generation 35:
  /nix/store/cgllc6zfnab06ah8w17izn4hmj80mhia-dev-workspace-0.2.0.
- System generation 2026-09-13--11-33-55:
  /nix/store/jvi5n2bbp0li9w2xikh5kgwqnnzgy7g7-nixos-system-aitherdev-26.05.20260911.21a67dc.
- Profile 34 and system 2026-09-13--10-05-18 remain available for rollback.
  Codex stays 0.154.0 with MainPID 1090021; ledger formats are unchanged.
- Workspace/configuration pin contract, package/system builds, dry activation,
  normal workspace-host switch and confctl switch passed. Both deployment health
  checks passed. Portal, router, Codex, tmux and nginx are active. No kernel build.
- Live authenticated health, index, initiative, JS/CSS and thread returned 200.
  Unauthenticated health returned 401. The real thread reports latestTurnId and
  the current portal assets use no-store. Details: plan-decision-live-results.json.
- All 10 Firefox checks passed at 1280x900 and 390x844. The fixture transcript
  gains about 193px on desktop and 200px on narrow screens during a decision.
  The tests include upload completion while hidden, exact draft/focus restoration,
  queue/dialog behavior, fresh-plan eligibility, pure legacy recovery, delayed
  receipt acknowledgement and distinct implementation of a later identical plan.
- Required review completed in all four lanes at sol xhigh. All Blocking and
  Important findings were fixed; details are in plan-decision-review-reconciliation.md.
  Provider and workspace flake checks passed; package Go tests and Ruby suites
  passed (297/2989 and 73/438 runs/assertions, no failures or errors).
- All configured CI passed at the exact current provider/runtime/organization
  heads, including the organization devcluster-check. Workspace/configuration
  have no feature-branch workflow. Results: plan-decision-ci-results.json.

Temporary fixture servers, test copies and input files were removed. Project
tracked worktrees are clean; existing configuration tool caches remain. Exact
pushed feature heads are in plan-decision-revisions.json. All branches remain
unmerged and this initiative stays active for follow-up. No archival or stop.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-12-portal-file-uploads/
