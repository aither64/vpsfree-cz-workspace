#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
source=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos
cd "$source" || exit
for check in templates standalone; do
  nix develop --profile "$source/result/config-imports-dev-shell" --command nix eval --impure --json --file "tests/nixos-container-$check-eval.nix" > "$record/quick-$check-eval.log" 2>&1
  status=$?
  printf '%s\n' "$status" > "$record/quick-$check-eval.status"
  if [ "$status" -ne 0 ]; then exit "$status"; fi
done
nix develop --profile "$source/result/config-imports-dev-shell" --command bash -c 'eval "$(sed -n "/^error_log=/,\$p" tests/nixos-container-eval.sh)"' > "$record/quick-negative-eval.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/quick-negative-eval.status"
if [ "$status" -ne 0 ]; then exit "$status"; fi
nix develop --profile "$source/result/config-imports-dev-shell" --command nix eval --impure --json --file "$record/kb-consumer-eval/evaluate.nix" > "$record/quick-kb-eval.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/quick-kb-eval.status"
if [ "$status" -ne 0 ]; then exit "$status"; fi
nix develop --profile "$source/result/config-imports-dev-shell" --command overcommit --run > "$record/quick-hooks.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/quick-hooks.status"
exit "$status"
