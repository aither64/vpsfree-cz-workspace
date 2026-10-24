#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = 0ba320a5a7bba9234f4d713bf8e142fe10f000b4
test -z "$(git status --porcelain)"
exec nix build --impure --no-link --print-build-logs --expr 'let f = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace"; p = import f.inputs.nixpkgs { system = "x86_64-linux"; }; in p.xvfb-run'
