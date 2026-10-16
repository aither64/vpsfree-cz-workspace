#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
product=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos
cd "$product" || exit 1
run_check() {
  name=$1
  shift
  "$@" > "$record/$name.log" 2>&1
  status=$?
  printf '%s\n' "$status" > "$record/$name.status"
  [ "$status" -eq 0 ] || return "$status"
}
run_check compatibility-selector-rerun1 nix develop --profile result/config-imports-dev-shell --command bash tests/nixos-container-eval.sh || exit $?
run_check compatibility-discovery ./test-runner.sh ls 'dist-config/nixos-persistence-upgrade*' || exit $?
run_check compatibility-kb nix develop --profile result/config-imports-dev-shell --command nix eval --impure --json --file "$record/kb-consumer-eval/evaluate.nix" || exit $?
run_check compatibility-hooks nix develop --profile result/config-imports-dev-shell --command overcommit --run || exit $?
run_check compatibility-docs nix develop --profile result/config-imports-dev-shell --command make doc || exit $?
run_check compatibility-evidence cp /nix/store/ikiimvhsi38s8jvm4y200kh0iinmrnim-persistence-evaluation.json "$record/compatibility-evidence.json" || exit $?
