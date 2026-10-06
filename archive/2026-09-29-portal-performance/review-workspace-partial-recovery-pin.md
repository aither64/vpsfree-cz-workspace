# Focused review: consuming workspace recovery pin

## Scope

- Repository: consuming vpsFree.cz workspace
- Worktree: `worktrees/2026-09-29-portal-performance/workspace`
- Base: `50c3dcf74f7eb816671caf4efd365f9c466e387a`
- Head: `4ba6ea9629b309f854e7790d37e2b3ad2d94a6aa` (`Update vpsFree dev workspace`)
- Reviewed/pushed extension: `dd09ec08dd2e6081fe82a4365af02113c9300189`
- Reviewed/pushed dev-workspace: `b9465ab61dfc4e9820e312b062cb7b96ed3f09b0`
- Reviewed/pushed codex-web: `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`
- Expected files: `flake.nix`, `flake.lock`

Confirm that the direct input and canonical lock graph resolve exactly through extension -> dev-workspace -> codex-web at those revisions, only the extension and dev-workspace lock nodes changed, and all unrelated nodes and follows relationships remain unchanged. No workspace package composition or deployment mechanism should change beyond selecting these reviewed inputs.

## Checks

- Canonical `nix flake lock --update-input vpsfree-dev-workspace` completed after the extension feature commit was pushed.
- Nix parse, exact three-revision lock assertions, and `git diff --check` pass.
- The diff contains only `flake.nix` and `flake.lock`; only the extension and dev-workspace lock nodes changed.

## Review

Use the mandatory change review workflow with General, Scope and proportionality, and Risk and compatibility lanes. This is a dependency-only incremental pre-push review. Inspect the committed diff directly, remain read-only, and report findings by severity or state explicitly that there are none. Exact consuming package build, deployment/live recovery, and final whole-chain readiness remain separate gates.
