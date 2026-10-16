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
test ! -e "$record/machine-prepared-notification-activation-v2.json"
test ! -e "$record/profile-prepared-46975718.json"
test ! -e "$record/preparation-notification-activation-v2-env.log"
cd "$config"
source "$record/config-130c-dev-env.sh" > "$record/preparation-notification-activation-v2-env.log" 2>&1
bundle check >> "$record/preparation-notification-activation-v2-env.log" 2>&1
cd "$record"
nix build --impure --file "$record/notification-activation-retain-env.nix" --out-link "$record/notification-activation-confctl-environment-root" > "$record/notification-activation-retain-env.log" 2>&1
test "$(readlink -f "$record/notification-activation-confctl-environment-root")" = /nix/store/zwnp17zzpqbgnqgac2h69j02j06khzh7-workspace-confctl-environment
for mode in machine profile; do
  output="$record/$mode-prepared-notification-activation-v2.json"
  if [[ "$mode" = profile ]]; then output="$record/profile-prepared-46975718.json"; fi
  request="$record/$mode-prepare-notification-activation-v2-request.json"
  if [[ "$mode" = profile ]]; then request="$record/profile-prepare-notification-activation-request.json"; fi
  started=$(date --iso-8601=seconds)
  set +e
  dev-session coordination prepare 2026-10-14-i-d-like-the-dev-workspace --as-is --request "$request" --json > "$output" 2> "$record/$mode-prepare-notification-activation-v2.log"
  result=$?
  set -e
  printf 'started=%s\nfinished=%s\nexit_status=%s\n' "$started" "$(date --iso-8601=seconds)" "$result" > "$record/$mode-prepare-notification-activation-v2.status"
  test "$result" = 0 || exit "$result"
done
