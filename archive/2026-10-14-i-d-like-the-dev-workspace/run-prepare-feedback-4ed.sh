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
test -s "$record/feedback-composition-review.md"
test -s "$record/verification-feedback.json"
test ! -e "$record/machine-prepared-feedback-4ed.json"
test ! -e "$record/profile-prepared-4ed9af55.json"
test ! -e "$record/preparation-feedback-4ed-env.log"
cd "$config"
source "$record/config-130c-dev-env.sh" > "$record/preparation-feedback-4ed-env.log" 2>&1
bundle check >> "$record/preparation-feedback-4ed-env.log" 2>&1
cd "$record"
for mode in machine profile; do
  output="$record/$mode-prepared-feedback-4ed.json"
  if [[ "$mode" = profile ]]; then output="$record/profile-prepared-4ed9af55.json"; fi
  started=$(date --iso-8601=seconds)
  set +e
  dev-session coordination prepare 2026-10-14-i-d-like-the-dev-workspace --as-is --request "$record/$mode-prepare-feedback-4ed-request.json" --json > "$output" 2> "$record/$mode-prepare-feedback-4ed.log"
  result=$?
  set -e
  printf 'started=%s\nfinished=%s\nexit_status=%s\n' "$started" "$(date --iso-8601=seconds)" "$result" > "$record/$mode-prepare-feedback-4ed.status"
  test "$result" = 0 || exit "$result"
done
