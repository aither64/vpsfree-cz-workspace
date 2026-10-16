#!/usr/bin/env bash
# Lead-owned build/copy preparation only; no approval or activation.
set -eo pipefail
umask 077
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
config=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/vpsfree-cz-configuration
cd "$record"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  test "${DEV_SESSION_SLUG-}" = 2026-10-14-i-d-like-the-dev-workspace
  test "${DEV_SESSION_WORKSPACE-}" = /home/aither/workspace/ai/vpsfree.cz
fi
test -s "$record/notification-activation-composition-review.md"
test -s "$record/verification-notification-activation.json"
test ! -e "$record/machine-prepared-notification-activation.json"
test ! -e "$record/profile-prepared-46975718.json"
test ! -e "$record/preparation-notification-activation-env.log"
cd "$config"
source "$record/config-130c-dev-env.sh" > "$record/preparation-notification-activation-env.log" 2>&1
bundle check >> "$record/preparation-notification-activation-env.log" 2>&1
cd "$record"
for mode in machine profile; do
  output="$record/$mode-prepared-notification-activation.json"
  if [[ "$mode" = profile ]]; then output="$record/profile-prepared-46975718.json"; fi
  started=$(date --iso-8601=seconds)
  set +e
  dev-session coordination prepare 2026-10-14-i-d-like-the-dev-workspace --as-is --request "$record/$mode-prepare-notification-activation-request.json" --json > "$output" 2> "$record/$mode-prepare-notification-activation.log"
  result=$?
  set -e
  printf 'started=%s\nfinished=%s\nexit_status=%s\n' "$started" "$(date --iso-8601=seconds)" "$result" > "$record/$mode-prepare-notification-activation.status"
  test "$result" = 0 || exit "$result"
done
