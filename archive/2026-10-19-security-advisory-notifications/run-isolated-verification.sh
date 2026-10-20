#!/usr/bin/env bash
set -u
record_dir=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-security-advisory-notifications
project_dir=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-security-advisory-notifications/vpsfree-irc-bot
state_dir=/tmp/2026-10-19-security-advisory-notifications-94ac4eb-isolated
exec 9>"$record_dir/isolated-runtime.lock"
flock 9
if test -f "$record_dir/isolated-runtime.exit"; then
  status=$(cat "$record_dir/isolated-runtime.exit")
  printf 'Existing verification result: %s\n' "$status"
  exit "$status"
fi
cd "$project_dir" || exit 2
if test "$(git rev-parse HEAD)" != 94ac4eb5a7caf0456fff7df86a44cae198463276 || test -n "$(git status --porcelain)"; then
  printf '2\n' > "$record_dir/isolated-runtime.exit"
  exit 2
fi
date -u +%Y-%m-%dT%H:%M:%SZ > "$record_dir/isolated-runtime.started"
printf '%s\n' "$state_dir" > "$record_dir/isolated-runtime-state-dir.txt"
./test-runner.sh test --state-dir "$state_dir" vpsadmin-events > "$record_dir/isolated-runtime.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record_dir/isolated-runtime.exit"
date -u +%Y-%m-%dT%H:%M:%SZ > "$record_dir/isolated-runtime.finished"
printf 'Verification finished with status %s\n' "$status"
exit "$status"
