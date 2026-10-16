#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos || exit 1
[ "$(git rev-parse HEAD)" = 29e26835047071022227968db964fdf2736b4bc0 ] || exit 1
[ -z "$(git status --porcelain)" ] || exit 1
nix develop --profile result/config-imports-dev-shell --command bash -c 'nix eval --impure --raw --file tests/nixos-container-persistence-eval.nix --apply "checks: checks.shellFixture" > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-real-mount/final-head-snippet.sh' > "$record/persistence-real-mount-eval.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/persistence-real-mount-eval.status"
[ "$status" -eq 0 ] || exit "$status"
cmp -- "$record/persistence-activation-snippet.sh" "$record/persistence-real-mount/final-head-snippet.sh" || exit 1
nix develop --profile result/config-imports-dev-shell --command bash "$record/persistence-real-mount/run.sh" "$record/persistence-real-mount/final-head-snippet.sh" > "$record/persistence-real-mount.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/persistence-real-mount.status"
exit "$status"
