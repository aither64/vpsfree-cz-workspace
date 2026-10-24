#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = 06126cd3fedf3df2b10f4173285b5af9038bdce6
test -z "$(git status --porcelain)"
exec nix build --impure --no-link --print-build-logs --expr 'let f = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace"; p = import f.inputs.nixpkgs { system = "x86_64-linux"; }; in p.xvfb-run'
