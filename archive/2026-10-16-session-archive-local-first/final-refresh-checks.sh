#!/usr/bin/env bash
set -uo pipefail
archive_record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-session-archive-local-first
archive_trees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-session-archive-local-first
runtime_checks() (
  set -e
  cd "$archive_trees/dev-workspace"
  test "$(git rev-parse HEAD)" = 598336522fbb490e7606670d5fdb504e66c607ec
  test -z "$(git status --porcelain)"
  nix flake check --print-build-logs > "$archive_record/final-refresh-runtime-checks.log" 2>&1
)
workspace_checks() (
  set -e
  cd "$archive_trees/workspace"
  test "$(git rev-parse HEAD)" = abdeefc472bb96da2ca15f3aee2599987d10ab6e
  test -z "$(git status --porcelain)"
  nix flake check --print-build-logs > "$archive_record/final-refresh-workspace-checks.log" 2>&1
  nix build --json --out-link "$archive_record/final-refresh-application-result" .#default > "$archive_record/final-refresh-application-build.json" 2> "$archive_record/final-refresh-application-build.log"
)
system_build() (
  set -e
  cd "$archive_trees/vpsfree-cz-configuration"
  test "$(git rev-parse HEAD)" = 62287e040638c9f66663a2ad4458836be1585718
  test -z "$(git status --porcelain)"
  nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev > "$archive_record/final-refresh-system-build.log" 2>&1
)
runtime_checks & archive_runtime_pid=$!
workspace_checks & archive_workspace_pid=$!
system_build & archive_system_pid=$!
archive_result=0
for archive_item in "runtime:$archive_runtime_pid" "workspace:$archive_workspace_pid" "system:$archive_system_pid"; do
  archive_name=${archive_item%%:*}
  archive_pid=${archive_item#*:}
  wait "$archive_pid"; archive_status=$?
  printf '%s\n' "$archive_status" > "$archive_record/final-refresh-$archive_name.exit"
  if [ "$archive_status" != 0 ]; then archive_result=1; fi
done
printf '%s\n' "$archive_result" > "$archive_record/final-refresh.exit"
exit "$archive_result"
