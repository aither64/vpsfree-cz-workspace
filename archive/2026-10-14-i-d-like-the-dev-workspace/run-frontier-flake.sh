#!/usr/bin/env bash
# Verification only, exact committed source. No retries or deployment.
set -eo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
checkout=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace
revision=bb9e6291bec10227c961c36559fba406938f1eaa
cd "$record"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace || exit 2
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  test "${DEV_SESSION_SLUG-}" = 2026-10-14-i-d-like-the-dev-workspace || exit 2
  test "${DEV_SESSION_WORKSPACE-}" = /home/aither/workspace/ai/vpsfree.cz || exit 2
fi
test ! -e frontier-runtime-flake.log && test ! -e frontier-runtime-flake.status || exit 2
test "$(git -C "$checkout" rev-parse HEAD)" = "$revision" || exit 2
test -z "$(git -C "$checkout" status --porcelain)" || exit 2
source "$record/runtime-dev-env.sh"
started=$(date --iso-8601=seconds)
set +e
nix flake check --no-write-lock-file --print-build-logs "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/dev-workspace.git?rev=$revision" > "$record/frontier-runtime-flake.log" 2>&1
result=$?
set -e
finished=$(date --iso-8601=seconds)
printf 'revision=%s\nstarted=%s\nfinished=%s\nexit_status=%s\n' "$revision" "$started" "$finished" "$result" > "$record/frontier-runtime-flake.status"
printf 'Full flake verification exit=%s revision=%s\n' "$result" "$revision"
exit "$result"
