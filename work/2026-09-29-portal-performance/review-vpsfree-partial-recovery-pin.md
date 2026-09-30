# Focused review: vpsFree extension recovery pin

## Scope

- Repository: `vpsfree-dev-workspace`
- Worktree: `worktrees/2026-09-29-portal-performance/vpsfree-dev-workspace`
- Base: `9c9833579e148e108b5811d618c81ec497b809bf`
- Head: `dd09ec08dd2e6081fe82a4365af02113c9300189` (`Update dev-workspace`)
- Upstream reviewed and pushed dev-workspace head: `b9465ab61dfc4e9820e312b062cb7b96ed3f09b0`
- Expected files: `flake.nix`, `flake.lock`

Confirm that the direct input and canonical lock node identify the exact reviewed dev-workspace head, the transitive codex-web node remains `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`, unrelated lock nodes and follows relationships are unchanged, and no package/deployment behavior changes beyond selecting this dependency revision.

## Checks

- Canonical `nix flake lock --update-input dev-workspace` completed on the host.
- Nix parse, lock JSON assertions, exact dev-workspace and codex-web revisions, and `git diff --check` pass.
- The diff contains only `flake.nix` and `flake.lock`; only the dev-workspace lock node changed.

## Review

Use the mandatory change review workflow with General, Scope and proportionality, and Risk and compatibility lanes. This is a dependency-only incremental pre-push review. Inspect the committed diff directly, remain read-only, and report findings by severity or state explicitly that there are none. Full extension build/CI and final whole-chain readiness remain separate gates.
