#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
checkout=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos
cd "$checkout" || exit 1
export VPSADMINOS_PERSISTENCE_BASELINE="$record/persistence-v2-raw-baseline/os/lib/nixos-container"
nix develop --profile result/config-imports-dev-shell --command bash tests/nixos-container-eval.sh > "$record/persistence-quick-eval.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/persistence-quick-eval.status"
[ "$status" -eq 0 ] || exit "$status"
nix develop --profile result/config-imports-dev-shell --command overcommit --run > "$record/persistence-quick-hooks.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/persistence-quick-hooks.status"
[ "$status" -eq 0 ] || exit "$status"
doc_dir=$(mktemp -d /tmp/config-imports-persistence-doc.XXXXXX) || exit 1
printf '%s\n' "$doc_dir" > "$record/persistence-doc-preview-path"
nix develop --profile result/config-imports-dev-shell --command mkdocs build --site-dir "$doc_dir" > "$record/persistence-quick-docs.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record/persistence-quick-docs.status"
exit "$status"
