#!/usr/bin/env bash
set -euo pipefail
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/final-coordinated-ea64ef57/guards.py
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = 0c0dd2d22ce4e03c22a7bd0c471267deb6ee3a2a
test -z "$(git status --porcelain)"
exec nix build --impure --no-link --print-build-logs --expr 'let f = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace"; p = import f.inputs.nixpkgs { system = "x86_64-linux"; }; in p.xvfb-run'
