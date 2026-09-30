# Aitherdev automatic-history rollout

Status: executed successfully. User-profile generation 74 selects the reviewed
package and the deployed long-conversation smoke passes.

## Exact inputs

- Generic dev-workspace feature:
  `7c133c562ac51076c1f45af46e180f8bfbabe836`
- Generic base and current remote `master`:
  `d20bb64c45db1d803fc3b7a8c2956049860d72dd`
- Current workspace composition revision:
  `e67da9920f3546522aa1301ff20dff009f6a877a`
- Previous selected package:
  `/nix/store/5dzn1p13lcqfgp6lqdii20swa0v3346g-dev-workspace-0.2.0`
- Candidate package:
  `/nix/store/8s0kg785hmz72law9psk19y8a2rig7gb-dev-workspace-0.2.0`
- Previous profile generation: 73

The candidate uses the committed workspace composition and its existing
vpsFree.cz extension inputs, overriding only the transitive generic
`dev-workspace` input with the exact clean reviewed feature worktree. No
`vpsfree-cz-configuration` or persisted configuration input is changed.

## Gates

- Focused JavaScript checks and live Chromium paging regression passed.
- Mandatory all-lane review rerun has no Blocking or Important findings.
- `nix flake check --print-build-logs` passed, including package and VM checks.
- GitHub Actions run `36693337955` passed at the exact feature head.
- The complete composed candidate package built successfully.
- Pre-switch router, portal, Codex, and tmux services are active.
- Candidate extension metadata retains both registered development-cluster
  providers.

## Switch and acceptance

Run the installed forward-transition entry point against the already built
candidate:

```sh
workspace-host switch --source \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-09-30-portal-auto-history/candidate-workspace-package
```

After the switch, confirm the selected package and new profile generation,
router/portal/Codex/tmux service health, current session and team access, then
run `deployed-history-smoke.cjs` against
`2026-09-27-newadmin-integration`. The smoke must prove the persistent control
is absent and one upward wheel crossing the 200-pixel threshold performs one
successful cursor read without a cascade.

## Recovery

Package generations are forward-only because team registration state can be
advanced by activation. Do not use `workspace-host rollback`, retarget profile
links, or edit generation/state markers. If acceptance fails after selection,
prepare, review, build, and switch to a newer package revision that restores
the previous browser behavior while retaining current state readers. No data
conversion or cleanup is required because this feature writes no persistent
state.

## Execution

- `workspace-host switch --source candidate-workspace-package` completed and
  selected
  `/nix/store/8s0kg785hmz72law9psk19y8a2rig7gb-dev-workspace-0.2.0` as
  user-profile generation 74.
- The transition retained Codex 0.155.0 compatibility, restarted disconnected
  terminal clients, restored the automatic-archive timer, and completed despite
  informational warnings about unrelated legacy unproven worktrees.
- Router, portal, Codex, tmux, and automatic-archive timer units are active.
- The current session and retained team roster resolve after the App Server
  restart.
- The deployed smoke on `2026-09-27-newadmin-integration` reports
  `passed: true`, zero persistent controls, one cursor read, and no automatic
  cascade. It increased the filtered visible transcript from 11 to 21 messages.
- An initial harness assertion checked `scrollTop <= 200` after the prepend;
  this was invalid because anchor compensation intentionally raises the final
  scroll position. The corrected harness retains the 260-pixel start, native
  upward wheel, successful cursor-response, and single-read assertions.
