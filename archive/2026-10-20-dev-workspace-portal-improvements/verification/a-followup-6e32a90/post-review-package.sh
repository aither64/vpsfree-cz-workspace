#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/codex-web
expected=6e32a9043ee6367d92bfaf8d3ebdf48036e275f9
[[ $(git rev-parse HEAD) == "$expected" ]]
[[ -z $(git status --porcelain=v1) ]]
receipt=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/a-followup-6e32a90
[[ ! -e "$receipt/package-results.json" && ! -e "$receipt/package.log" ]]
# The parent launches only after independent review under its fresh utility.
timeout 1200 nix build --json --print-build-logs --out-link "$receipt/package-result" \
  .#checks.x86_64-linux.default .#checks.x86_64-linux.generic-source \
  > "$receipt/package-results.json" 2> "$receipt/package.log"
