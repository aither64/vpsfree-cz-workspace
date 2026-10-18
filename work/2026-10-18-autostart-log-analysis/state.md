---
lifecycle: active
---

# osctld autostart fix

## Current phase

Implementation preparation. User approved the osctld-only plan and asked to implement it; endpoint is reviewed published branch, no merge/deployment. Swap and histfile are deferred.

## Phase checklist

- [x] Verify session identity and same-session roster (ready retained members, workspace-write implementers).
- [x] Collect logs and correlate EMFILE -> EOF with deployed source.
- [x] Agree osctld-only plan and reviewed-branch endpoint.
- [ ] Update architect-owned implementation brief.
- [ ] Implement handshake and deterministic unit regressions.
- [ ] Add focused packaged-osctld VM regression.
- [ ] Complete quick checks and commits.
- [ ] Independent final branch review.
- [ ] Focused VM verification and publication.

## Backlog and owners

| Owner | Expected result / acceptance | Dependencies and checks |
| --- | --- | --- |
| architect0 | Accepted osctld-only design.md with boundaries/compatibility/verification | Before substantive source edits; preserve evidence |
| implementer0 | Handshake source, deterministic specs, comments, commits and fixes | Design; Nix shell/hooks; preserve FD/socket invariants |
| implementer1 | One focused VM regression and registration, commit and fixes | Design; no production overlap; watcher launches long run after review |
| reviewer0 | Independent exact-head final review, history and no-migration conclusion | All intended changes committed and quick checks passed |
| lead | Identity, tracking, Git serialization, acceptance, review/watcher coordination and handoff | No application edits; session remains open |

## Repository

- vpsadminos worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-autostart-log-analysis/vpsadminos
- Branch: 2026-10-18-autostart-log-analysis
- Fetched base: origin/staging d531fc90888e3eabf17889b0dff94c648866cea4; origin/HEAD is staging. Stale origin/master is not the base.
- Worktree checkout exists but dev-session registration command failed at Overcommit signature validation; implementer0 owns hook preflight, then lead retries validated registration.

## Evidence and limitations

- Logs: node1-runit-since-1014.log; node1-host-since-1014.log (bounded); node1-host-since-102109.log (complete capture to 10:29:14).
- Shutdown began 10:15; new boot 10:21. 48 attempts, 25 success markers, 23 child EMFILE and parent EOF failures. Deployed OS eb5c39c0789401117c48cd124e47b7a401fb91b6; relevant source unchanged at staging baseline.
- Parent applies target prlimits before child acknowledges inherited descriptor cleanup. Daemon source limit131072, container default soft1024; actual node FD occupancy/limits not collected because direct node SSH denied. Deterministic regression will test causal ordering; no leak claim.
- Architect/implementer runtimes previously lacked remote network/SSH access; lead log transport succeeded. Do not take over application edits for access problems; resolve/report them.
- No application edits/checks/commits yet. No node mutation or deployment performed.

## Documentation and next action

- Architect updates design.md; implementer0 resolves hook signature and reports readiness; lead commits initial plan/state before project commits/external mutations.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-autostart-log-analysis/
- Initial tracking checkpoint pending. Preserve unrelated shared working tree/index changes. Retain session/branches; no lifecycle cleanup requested.
