#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos || exit 1
nix develop --profile result/config-imports-dev-shell --command bash -c 'nix eval --impure --json --file "$1" > "$2"' bash "$record/implementer-activation-option-probe/evaluate.nix" "$record/activation-option-probe-rerun.json" > "$record/activation-option-probe-rerun.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/activation-option-probe-rerun.status"
exit "$status"
