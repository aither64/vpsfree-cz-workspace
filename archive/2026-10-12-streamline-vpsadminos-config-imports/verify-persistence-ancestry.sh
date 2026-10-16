#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos
cd "$repo" || exit 1
[ "$(git rev-parse HEAD)" = 809799be12da1d35eacd180dd936579ab55e5bbe ] || exit 1
[ "$(git diff --name-only)" = tests/nixos-container-persistence-eval.nix ] || exit 1
[ -z "$(git diff --cached --name-only)" ] || exit 1
printf '%s\n' 'ed5bf122faf20da4af47509092bb3dcb406e143fe39e39ef8f0ff5331af44b3d  tests/nixos-container-persistence-eval.nix' | sha256sum --check --status || exit 1
export VPSADMINOS_PERSISTENCE_BASELINE="$record/persistence-v2-raw-baseline/os/lib/nixos-container"
nix develop --profile result/config-imports-dev-shell --command nix eval --impure --json --file tests/nixos-container-persistence-eval.nix > "$record/persistence-ancestry-eval.json" 2> "$record/persistence-ancestry-eval.log"
status=$?
printf '%s\n' "$status" > "$record/persistence-ancestry-eval.status"
[ "$status" -eq 0 ] || exit "$status"
nix develop --profile result/config-imports-dev-shell --command overcommit --run > "$record/persistence-ancestry-hooks.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/persistence-ancestry-hooks.status"
[ "$status" -eq 0 ] || exit "$status"
nix develop --profile result/config-imports-dev-shell --command git fetch origin staging > "$record/persistence-final-fetch.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/persistence-final-fetch.status"
exit "$status"
