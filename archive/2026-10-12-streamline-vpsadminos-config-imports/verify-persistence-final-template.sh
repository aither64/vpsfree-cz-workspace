#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos || exit 1
[ "$(git rev-parse HEAD)" = 809799be12da1d35eacd180dd936579ab55e5bbe ] || exit 1
[ -z "$(git status --porcelain)" ] || exit 1
nix develop --profile result/config-imports-dev-shell --command nix eval --impure --json --file tests/nixos-container-templates-eval.nix > "$record/persistence-final-template.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/persistence-final-template.status"
exit "$status"
