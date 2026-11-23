---
lifecycle: active
---

# 2026-11-23-pi-goal-completion

## Status

Implementation requested. Offline SDK and worker fixtures confirmed the continuation seam and exposed a queued-input receipt race. The first feature package will preserve the existing receipt rules and prove the fence before exposing any behavior.

- [x] Verify session identity, scope and roster.
- [x] Inspect Pi turn handling and the existing portal goal workflow.
- [x] Accept a proposed approach and identify its first verification gate.
- [x] Compare published Pi goal extensions and check whether the managed worker can load them.
- [x] Specify how the agent maintains a goal from chat and how users see, correct or pause it.
- [x] Limit the composer to one non-wrapping, width-truncated goal row (zero when empty); put details and controls in an overlay.
- [x] Verify continuation and abort in the installed SDK with an offline fixture.
- [ ] Verify the managed worker preserves queued-input receipts, rejects stale goal reports, and preserves limits on edits before exposing the feature.

| Package | Owner | Acceptance | Status / evidence |
| --- | --- | --- | --- |
| Current behavior and proposed design | `architect0` | Source-backed gap analysis, bounded design and focused verification cases; no application changes | Assigned 21:40 UTC via native turn `2f7d3781`; hook finding 21:43, [design](design.md) accepted for recommendation 21:48. No implementation package released. |
| Published extension comparison | `architect0` | Confirm actual continuation, constraints and portal loading from published artifacts; read-only | Report accepted; see below. |
| Editable goal design | `architect0` | One visible strip and revision handoff; reject old reports and let Stop/queue take precedence | Updated [design.md](design.md) and reported at 22:26 UTC. |
| A0: disposable pinned-SDK check | `implementer0` | Exact request counts for ordinary answer continuation and Stop during hook; no product edits or network | Assigned 22:26 UTC via native turn `9f4a776a`; accepted at 22:29. 2 cases passed; see results below. |
| Chat-first goal design | `architect0` | Clear user requests can create or revise a goal; preserve correction, Stop, input and budget fences; one-row composer UI | [Updated design](design.md) accepted at 22:34 UTC; one-row requirement added at 22:36 with narrow/mobile and keyboard checks. |
| A1: focused queued-input experiment | `implementer0` | Check overlap between a natural Follow Up and a goal reminder; identify receipt or hook ordering constraints | Accepted at 22:40 UTC; 3 offline cases passed with the baseline failure reproduced. |
| Worker fence package | `implementer0` | Preserve exact receipt checks; suppress unattended work on pending user input and Stop | Awaiting settled brief and registered worktree. |

## Published extension follow-up

- [`@narumitw/pi-goal`](https://github.com/narumiruna/pi-extensions/tree/f52e4cb005ccb710383e14883b68f156a9e47f0d/packages/pi-goal) 0.55.4 is the closest behavior reference: one durable objective, automatic continuation, completion/blocker/wait reporting and configurable limits. It dispatches a new message after settlement and documents the idle-send race.
- [`pi-goal-x`](https://github.com/tmonk/pi-goal-x/tree/b0fc15ebb658a1e9ea60ae65496717a780080f37) 0.34.1 adds task plans and an optional auditor. Its published SDK and Node ranges include the selected worker versions; automatic continuation is uncapped by default unless configured. Compatibility was not run.
- [`pi-codex-goal`](https://github.com/fitchmultz/pi-codex-goal/blob/e8dcea2e0121ec780ae8988b656934d2fa0b42d1/docs/reference.md#installation-options) 0.7.11 has a Codex-style persistent goal but its documented Pi and published Node requirements exceed the selected portal worker's Pi 1.5.2 / Node 22.23.2.
- The [managed Pi loader](https://github.com/aither64/dev-workspace/blob/0abe5fe48955/pi-runtime/src/session.mjs#L405-L415) disables third-party discovery and wires its own extension factories. None is a drop-in portal installation. Use the first package as a reference and keep continuation and Stop ownership in the managed worker. No extension installed or executed.

## Next action

Register the feature worktree and dispatch the worker gate. Test exact human-input provenance and goal revision behavior before exposing the shared goal UI. The user's instruction authorizes implementation, not merging or deployment. An agent's report of completion is not independent evidence or permission to merge or deploy.

## Repositories and checks

No registered branches or worktrees. Used user-profile `dev-session current`, `team list` and `url`; the minimal Pi shell required adding `$HOME/.local/state/dev-workspaces/profile/bin` to `PATH` ([note](../../notes/dev-workspace/2026-11-23-pi-tool-shell-profile-path.md)). See [design.md](design.md) for source pins and proposed checks. No product tests run and no released documentation changed.

A0 used the selected Pi 1.5.2 SDK and Node 22.23.2 with a scripted offline provider, no discovered extensions, and one managed-style factory, in disposable HOME/XDG state (`node --test a0.test.mjs`; 2 passed, 0 failed, 3.953 seconds). Clean plain reply: 2 provider requests, one extension-authored reminder in the second, one original user entry. Abort while the hook waited: 1 provider request; the reminder entry still persisted but no continuation ran. This does not establish managed-worker queue/steer, receipt provenance, revision fencing or portal Stop behavior. The fixture directory was removed.

## Cleanup

The A1 fixture was cleaned up. With no reminder, Follow Up at the awaited settle hook produced one natural request, an exact Accepted receipt and successful verification. A persisted reminder caused another goal request before the human request, invalidating the expected receipt lineage and holding the worker. Do not broaden the existing ancestry allowlist to make it pass. No services or temporary checkouts created.
