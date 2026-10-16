#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
source=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos
cd "$source" || exit
nix develop --profile "$source/result/config-imports-dev-shell" --command bash tests/nixos-container-eval.sh > "$record/quick-module-eval.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/quick-module-eval.status"
if [ "$status" -ne 0 ]; then exit "$status"; fi
nix develop --profile "$source/result/config-imports-dev-shell" --command nix eval --impure --json --file "$record/kb-consumer-eval/evaluate.nix" > "$record/quick-kb-eval.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/quick-kb-eval.status"
if [ "$status" -ne 0 ]; then exit "$status"; fi
nix develop --profile "$source/result/config-imports-dev-shell" --command overcommit --run > "$record/quick-hooks.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/quick-hooks.status"
exit "$status"
