---
lifecycle: active
---

# Portal message delivery recovery

Phase: setup and implementation. User authorized implementation and aitherdev
deployment; no default-branch integration authorization.

- [x] Investigate original failure and approve portal-level recovery plan.
- [x] Create a separate tracked initiative without starting a new Codex task.
- [ ] Implement client/HTTP delivery handling and focused regressions.
- [ ] Implement portal recovery and current composer feedback.
- [ ] Commit source, quick checks and independent final review.
- [ ] Complete packaged/native/browser checks and publish feature heads.
- [ ] Compose matching runtime/configuration and deploy aitherdev.
- [ ] Verify live continuity/recovery and report remaining integration gate.

The original confctl message was absent from native history, rollout and queue.
Its submission record remained `submitting`; retries only reconciled history.
The banner additionally cleared only for the same attempt ID, so a successful
reworded message left the earlier composer error visible.

Baseline: installed application
`/nix/store/l9sc1ksacdkm7iij99ggyg87bqsp9n15-dev-workspace-0.2.0`;
codex-web `11ec57d2203fc735696fe75a837d47da55a5c6af`, native Codex 0.163.0.
Recheck published defaults and current deployment before composition. Retain
existing caller-cancellation isolation and the deployed retry/UI improvements.

This initiative has no retained team roster. The external lead owns development;
use the installed default review and verification utility policies for final
review and long checks. Preserve unrelated dirty shared-workspace files.

Next: create isolated project worktrees from current published defaults, inspect
their instructions and delivery paths, implement the approved design.
