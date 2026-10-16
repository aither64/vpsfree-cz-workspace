#!/usr/bin/env bash
# Obtain declared tools from the integrated configuration baseline only.
set -eo pipefail
umask 077
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
cd "$record"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  test "${DEV_SESSION_SLUG-}" = 2026-10-14-i-d-like-the-dev-workspace
  test "${DEV_SESSION_WORKSPACE-}" = /home/aither/workspace/ai/vpsfree.cz
fi
test ! -e "$record/config-130c-dev-env.sh"
test ! -e "$record/config-130c-dev-env.status"
started=$(date --iso-8601=seconds)
set +e
nix print-dev-env --no-write-lock-file 'git+file:///home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git?rev=130c22480fab70ac9b0d175df875d01f2c03d696' > "$record/config-130c-dev-env.sh" 2> "$record/config-130c-dev-env.log"
result=$?
set -e
printf 'revision=130c22480fab70ac9b0d175df875d01f2c03d696\nstarted=%s\nfinished=%s\nexit_status=%s\n' "$started" "$(date --iso-8601=seconds)" "$result" > "$record/config-130c-dev-env.status"
printf 'Configuration tool environment exit=%s\n' "$result"
exit "$result"
