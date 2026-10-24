#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = d617ef3968280e9955da85e2d7464a47030e7087
test -z "$(git status --porcelain)"
exec nix build --impure --no-link --print-build-logs --expr 'let f = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace"; p = import f.inputs.nixpkgs { system = "x86_64-linux"; }; in p.xvfb-run'
