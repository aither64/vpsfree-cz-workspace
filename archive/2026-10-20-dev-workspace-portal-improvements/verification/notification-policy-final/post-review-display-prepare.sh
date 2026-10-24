#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = 133d23f5d341808559b08a533409e748d6a400aa
test -z "$(git status --porcelain)"
exec nix build --impure --no-link --print-build-logs --expr 'let f = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace"; p = import f.inputs.nixpkgs { system = "x86_64-linux"; }; in p.xvfb-run'
