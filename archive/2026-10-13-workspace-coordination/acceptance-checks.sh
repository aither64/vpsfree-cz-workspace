#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination

test "$(git -C "$group/dev-workspace" rev-parse HEAD)" = a0be88432ead4df93eb950f51d08b748ebde2e37
test "$(git -C "$group/vpsfree-dev-workspace" rev-parse HEAD)" = 78589f37cc475d36ecc710eabba6c4a443335f9d
test "$(git -C "$group/workspace" rev-parse HEAD)" = 3d75b49635f38fdc62885252a6b6a3f09df2a773
cd "$group/dev-workspace"
nix flake check --print-build-logs
nix develop --command ruby test/workspace_coordination_systemd_test.rb -n /systemd/

cd "$group/vpsfree-dev-workspace"
nix flake check --print-build-logs

cd "$group/workspace"
nix flake check --print-build-logs
nix build --no-link --print-out-paths .#default > "$tracking/candidate-package.path"

cd "$group/dev-workspace"
nix develop --command "$tracking/native-notification-fixture" "$(cat "$tracking/candidate-package.path")"

gh run watch 38413102850 --repo aither64/dev-workspace --exit-status
gh run watch 38413426762 --repo vpsfreecz/dev-workspace --exit-status
