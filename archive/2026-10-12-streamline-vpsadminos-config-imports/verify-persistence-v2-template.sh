#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos || exit 1
[ "$(git rev-parse HEAD)" = 29e26835047071022227968db964fdf2736b4bc0 ] || exit 1
[ -z "$(git status --porcelain)" ] || exit 1
nix develop --profile result/config-imports-dev-shell --command nix eval --impure --json --file tests/nixos-container-templates-eval.nix > "$record/persistence-v2-template.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/persistence-v2-template.status"
exit "$status"
