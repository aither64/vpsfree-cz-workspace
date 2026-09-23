---
lifecycle: active
---

# Current status

Ready, awaiting merge approval. The policy and tests are committed in both
feature worktrees; focused checks, independent review, both flake checks,
extension CI, and the aitherdev user-profile package switch passed. No merge
approval has been given for this initiative. Keep both feature heads out of
their `master` branches until the user explicitly directs integration of the
workspace and `vpsfree-dev-workspace` repository/target set.

## Ownership

- Coordination workspace: feature branch `2026-09-23-review-merge-approval-policy`,
  worktree `worktrees/2026-09-23-review-merge-approval-policy/workspace`,
  current head `1a305fbafd918793bea633bbbb3a37c321f1c05c` (base
  `bfe7b87e`). Pushed to its feature ref.
- `vpsfree-dev-workspace`: same-name feature branch, worktree
  `worktrees/2026-09-23-review-merge-approval-policy/vpsfree-dev-workspace`,
  current head `ad13e7fc2a1874a54921bb91d743e4a4851d3c4a` (base
  `ecd56fb`). Pushed to its feature ref.

## Verification and review

- Workspace: `ruby test/agent_instructions_test.rb` passed (4 runs, 48
  assertions); `git diff --check` clean.
- Extension: `ruby test/skill_policy_test.rb` passed (2 runs, 16 assertions);
  `git diff --check` clean.
- Overall risk: high because these instructions govern default-branch
  integration authority. Mandatory review covered General, Architecture,
  Scope, and Risk lanes on workspace `1a305fba` and extension `ad13e7f` with
  one standalone Sol/xhigh reviewer. The session has no retained roster; the
  installed catalog's default development reviewer is Sol/xhigh. The reviewer
  reported no findings. The gate is procedural rather than branch protection;
  the installed package now supplies the updated skill text.
- Extension `nix flake check --print-build-logs` passed at `ad13e7f`; full
  output in `extension-flake-check.log`.
- Workspace `nix flake check --print-build-logs` passed at `1a305fba`; full
  output in `workspace-flake-check.log`.
- Extension GitHub Actions `Check` run `35868253569` passed at exact head
  `ad13e7f`; watch output is in `extension-ci.log`. The workspace repository
  has no configured GitHub workflow for this feature branch.
- The `workspace-host switch` of the workspace feature worktree completed
  successfully. `workspace-host status` reports package
  `/nix/store/jxhdykqrvlxh9pyzip3b19n27jpcq35h-dev-workspace-0.2.0`;
  installed review and handoff skills contain the new policy. The switch log
  is `workspace-switch.log`. It warned about two unrelated unproven portal
  worktrees but did not refuse or fail the switch.

## Documentation and compatibility

The durable policy is in the workspace `AGENTS.md` and Git, session,
verification, and deployment procedures; review and handoff routing lives in
the extension skills. No runtime API, schema, state format, or migration changed.
The workspace feature pin selects the extension feature commit. The user-profile
package now supplies the updated skills. Existing agents that already loaded
older instructions may need to reread the changed files; the root workspace
integration rule remains authoritative after it is integrated. The gate is
procedural, not a GitHub branch-protection rule.

Stable portal URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-23-review-merge-approval-policy/

## Next

Await the user's explicit direction to merge the workspace and extension
feature branches into their respective `master` branches. Before that future
integration, refresh target refs, rebase cleanly if needed, verify patch
equivalence and re-run relevant checks/CI on changed heads, capture comparisons,
then fast-forward only. A material patch or target-set change requires renewed
approval. Do not mark the initiative complete or archive it now.
