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
test -s notification-compact-composition-review.md
test -s verification-notification-compact.json
test "$(git -C "$config" rev-parse HEAD)" = 228ec56345912d9a07f29713d031b6e7c1ad1a28
test "$(readlink -f notification-compact-confctl-environment-root)" = /nix/store/w6iahs0amv82p59kxsr5bdw8mmf9lp3y-workspace-confctl-environment
test -x notification-compact-confctl-environment-root/bin/workspace-confctl-environment
for name in machine-prepared-notification-compact-8cb1c0e5.json profile-prepared-notification-compact-8cb1c0e5.json preparation-notification-compact-8cb1c0e5-env.log preparation-notification-compact-8cb1c0e5.status; do test ! -e "$record/$name"; done
cd "$config"
source "$record/config-130c-dev-env.sh" > "$record/preparation-notification-compact-8cb1c0e5-env.log" 2>&1
bundle check >> "$record/preparation-notification-compact-8cb1c0e5-env.log" 2>&1
cd "$record"
started=$(date --iso-8601=seconds)
result=0
for mode in machine profile; do
  step_started=$(date --iso-8601=seconds)
  set +e
  dev-session coordination prepare 2026-10-14-i-d-like-the-dev-workspace --as-is --request "$record/$mode-prepare-notification-compact-request.json" --json > "$record/$mode-prepared-notification-compact-8cb1c0e5.json" 2> "$record/$mode-prepare-notification-compact-8cb1c0e5.log"
  result=$?
  set -e
  printf 'started=%s\nfinished=%s\nexit_status=%s\n' "$step_started" "$(date --iso-8601=seconds)" "$result" > "$record/$mode-prepare-notification-compact-8cb1c0e5.status"
  if [[ "$result" != 0 ]]; then break; fi
done
printf 'revision=8cb1c0e545e1343d311f7cb9405eee83c468b4a6\nstarted=%s\nfinished=%s\nexit_status=%s\n' "$started" "$(date --iso-8601=seconds)" "$result" > "$record/preparation-notification-compact-8cb1c0e5.status"
exit "$result"
