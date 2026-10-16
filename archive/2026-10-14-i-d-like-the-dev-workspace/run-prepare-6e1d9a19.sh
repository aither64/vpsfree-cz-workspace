#!/usr/bin/env bash
# Lead-owned build/copy preparation only. No approvals, job refresh or activation.
set -eo pipefail
umask 077
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
cd "$record"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace || exit 2
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  test "${DEV_SESSION_SLUG-}" = 2026-10-14-i-d-like-the-dev-workspace || exit 2
  test "${DEV_SESSION_WORKSPACE-}" = /home/aither/workspace/ai/vpsfree.cz || exit 2
fi
for mode in machine profile; do
  test ! -e "$record/$mode-prepared-6e1d9a19.json" && test ! -e "$record/$mode-prepare-6e1d9a19.status" || exit 2
done
for mode in machine profile; do
  started=$(date --iso-8601=seconds)
  set +e
  dev-session coordination prepare 2026-10-14-i-d-like-the-dev-workspace --as-is --request "$record/$mode-prepare-6e1d9a19-request.json" --json > "$record/$mode-prepared-6e1d9a19.json" 2> "$record/$mode-prepare-6e1d9a19.log"
  result=$?
  set -e
  finished=$(date --iso-8601=seconds)
  printf 'started=%s\nfinished=%s\nexit_status=%s\n' "$started" "$finished" "$result" > "$record/$mode-prepare-6e1d9a19.status"
  test "$result" = 0 || exit "$result"
done
