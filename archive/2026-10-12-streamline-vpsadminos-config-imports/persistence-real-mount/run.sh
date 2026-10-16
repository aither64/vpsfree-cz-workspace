#!/usr/bin/env bash
set -euo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
here=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
[ "$here" = "$record/persistence-real-mount" ]
[ "$#" -eq 1 ] || { printf 'Usage: bash run.sh EVALUATED_SNIPPET\n' >&2; exit 2; }
snippet=$(realpath -- "$1")
[ -r "$snippet" ]
run_dir=$(mktemp -d "$here/run.XXXXXXXX")
cp -- "$snippet" "$run_dir/input-snippet.sh"
cmp -- "$snippet" "$run_dir/input-snippet.sh"
sha256sum -- "$snippet" "$run_dir/input-snippet.sh" > "$run_dir/input.sha256"
git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos rev-parse HEAD > "$run_dir/source-head"
parent_mount=$(readlink /proc/self/ns/mnt)
parent_user=$(readlink /proc/self/ns/user)
printf 'Evidence directory: %s\n' "$run_dir"
set +e
unshare --user --map-root-user --mount --propagation private \
  bash "$here/inside.sh" "$run_dir" "$parent_mount" "$parent_user" > "$run_dir/run.log" 2>&1
status=$?
set -e
printf '%s\n' "$status" > "$run_dir/status"
cat "$run_dir/run.log"
exit "$status"
