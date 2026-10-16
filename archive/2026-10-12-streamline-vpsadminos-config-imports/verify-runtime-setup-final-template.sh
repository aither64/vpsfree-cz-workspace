#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
product=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos
expected_head=$(cat "$record/compatibility-final-head") || exit 1
cd "$product" || exit 1
[ "$(git rev-parse HEAD)" = "$expected_head" ] || exit 1
[ -z "$(git status --porcelain)" ] || exit 1
nix develop --profile result/config-imports-dev-shell --command nix eval --impure --json --file tests/nixos-container-templates-eval.nix > "$record/runtime-setup-final-template.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/runtime-setup-final-template.status"
[ "$status" -eq 0 ] || exit "$status"

./test-runner.sh ls -t ci 'dist-config/nixos-persistence-upgrade*' > "$record/runtime-setup-ci-discovery.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/runtime-setup-ci-discovery.status"
exit "$status"
