#!/usr/bin/env bash
set -eo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
cd "$record"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace
for repository in dev-workspace workspace vpsfree-cz-configuration; do
  output="$record/notification-compact-merge-$repository-prepared.json"
  test ! -e "$output"
  set +e
  dev-session coordination prepare 2026-10-14-i-d-like-the-dev-workspace --as-is --request "$record/notification-compact-merge-$repository-prepare-request.json" --json > "$output" 2> "$record/notification-compact-merge-$repository-prepare.log"
  result=$?
  set -e
  printf '%s\n' "$result" > "$record/notification-compact-merge-$repository-prepare.status"
  if [[ "$result" != 0 ]]; then exit "$result"; fi
done
