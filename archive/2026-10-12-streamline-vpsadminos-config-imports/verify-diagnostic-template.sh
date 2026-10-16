#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
source=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos
cd "$source" || exit 1
if [ "$(git rev-parse HEAD)" != 4a40154539bf6dc73d391c30326af255b4dc15b2 ] || [ -n "$(git status --porcelain)" ]; then
  printf 'Final diagnostic source changed; refusing verification\n' >&2
  exit 1
fi
nix develop --profile result/config-imports-dev-shell --command nix eval --impure --json --file tests/nixos-container-templates-eval.nix > "$record/final-diagnostic-template-eval.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/final-diagnostic-template-eval.status"
exit "$status"
