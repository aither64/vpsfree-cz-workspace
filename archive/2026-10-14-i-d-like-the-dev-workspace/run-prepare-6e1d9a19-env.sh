#!/usr/bin/env bash
# Lead-owned corrected-environment build/copy preparation; no activation.
set -eo pipefail
umask 077
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
config=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/vpsfree-cz-configuration
cd "$record"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace || exit 2
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  test "${DEV_SESSION_SLUG-}" = 2026-10-14-i-d-like-the-dev-workspace || exit 2
  test "${DEV_SESSION_WORKSPACE-}" = /home/aither/workspace/ai/vpsfree.cz || exit 2
fi
test ! -e "$record/machine-prepared-6e1d9a19-env.json" || exit 2
test ! -e "$record/profile-prepared-6e1d9a19.json" || exit 2
test ! -e "$record/preparation-6e1d9a19-env-preflight.log" || exit 2
cd "$config"
source "$record/config-dev-env.sh" > "$record/preparation-6e1d9a19-env-preflight.log" 2>&1
bundle check >> "$record/preparation-6e1d9a19-env-preflight.log" 2>&1
cd "$record"
for mode in machine profile; do
  suffix=6e1d9a19
  if [[ "$mode" = machine ]]; then suffix=6e1d9a19-env; fi
  started=$(date --iso-8601=seconds)
  set +e
  dev-session coordination prepare 2026-10-14-i-d-like-the-dev-workspace --as-is --request "$record/$mode-prepare-$suffix-request.json" --json > "$record/$mode-prepared-$suffix.json" 2> "$record/$mode-prepare-$suffix.log"
  result=$?
  set -e
  finished=$(date --iso-8601=seconds)
  printf 'started=%s\nfinished=%s\nexit_status=%s\n' "$started" "$finished" "$result" > "$record/$mode-prepare-$suffix.status"
  test "$result" = 0 || exit "$result"
done
