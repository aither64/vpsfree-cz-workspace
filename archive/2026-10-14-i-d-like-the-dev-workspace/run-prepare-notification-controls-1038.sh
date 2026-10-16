#!/usr/bin/env bash
# Lead-owned exact artifact build/copy preparation, no activation/approval.
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
test -s notification-controls-composition-review.md
test -s verification-notification-controls.json
test "$(git -C "$config" rev-parse HEAD)" = 2dfbf7ade3bfc9a7c60dd827959319c63b93c154
test "$(readlink -f notification-controls-confctl-environment-root)" = /nix/store/w6iahs0amv82p59kxsr5bdw8mmf9lp3y-workspace-confctl-environment
test -x notification-controls-confctl-environment-root/bin/workspace-confctl-environment
for name in machine-prepared-notification-controls-1038.json profile-prepared-notification-controls-1038.json preparation-notification-controls-1038-env.log preparation-notification-controls-1038.status; do test ! -e "$record/$name"; done
cd "$config"
source "$record/config-130c-dev-env.sh" > "$record/preparation-notification-controls-1038-env.log" 2>&1
bundle check >> "$record/preparation-notification-controls-1038-env.log" 2>&1
cd "$record"
started=$(date --iso-8601=seconds)
result=0
for mode in machine profile; do
  step_started=$(date --iso-8601=seconds)
  set +e
  dev-session coordination prepare 2026-10-14-i-d-like-the-dev-workspace --as-is --request "$record/$mode-prepare-notification-controls-request.json" --json > "$record/$mode-prepared-notification-controls-1038.json" 2> "$record/$mode-prepare-notification-controls-1038.log"
  result=$?
  set -e
  printf 'started=%s\nfinished=%s\nexit_status=%s\n' "$step_started" "$(date --iso-8601=seconds)" "$result" > "$record/$mode-prepare-notification-controls-1038.status"
  if [[ "$result" != 0 ]]; then break; fi
done
printf 'revision=1038d4abdde8b115c21b5940b14be637cfa967b6\nstarted=%s\nfinished=%s\nexit_status=%s\n' "$started" "$(date --iso-8601=seconds)" "$result" > "$record/preparation-notification-controls-1038.status"
exit "$result"
