#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-04-upload-display-limits/workspace
test "$(git rev-parse HEAD)" = 88c0b957a1e870e4ce36a1743f72b529ba4825e1
test -z "$(git status --porcelain)"
nix flake check --print-build-logs > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits/packaged-workspace.log 2>&1
nix build --no-link --print-out-paths .#default > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits/candidate-package.txt 2> /home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits/candidate-package-build.log
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-04-upload-display-limits/vpsfree-cz-configuration
test "$(git rev-parse HEAD)" = e179a58ee3f7ceb4cf0b253d368c8ad94967b2d5
test -z "$(git status --porcelain)"
nix develop --command confctl build -y 'cz.vpsfree/machines/aitherdev' > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits/aitherdev-build.log 2>&1
