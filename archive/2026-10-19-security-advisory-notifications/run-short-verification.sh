#!/usr/bin/env bash
set -u
record_dir=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-security-advisory-notifications
project_dir=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-security-advisory-notifications/vpsfree-irc-bot
state_dir=/tmp/sa-94ac4eb-r1
exec 9>"$record_dir/short-runtime.lock"
flock 9
if test -f "$record_dir/short-runtime.exit"; then
  status=$(cat "$record_dir/short-runtime.exit")
  printf 'Existing verification result: %s\n' "$status"
  exit "$status"
fi
cd "$project_dir" || exit 2
if test "$(git rev-parse HEAD)" != 94ac4eb5a7caf0456fff7df86a44cae198463276 || test -n "$(git status --porcelain)"; then
  printf '2\n' > "$record_dir/short-runtime.exit"
  exit 2
fi
date -u +%Y-%m-%dT%H:%M:%SZ > "$record_dir/short-runtime.started"
printf '%s\n' "$state_dir" > "$record_dir/short-runtime-state-dir.txt"
./test-runner.sh test --state-dir "$state_dir" vpsadmin-events > "$record_dir/short-runtime.log" 2>&1
status=$?
printf '%s\n' "$status" > "$record_dir/short-runtime.exit"
date -u +%Y-%m-%dT%H:%M:%SZ > "$record_dir/short-runtime.finished"
printf 'Verification finished with status %s\n' "$status"
exit "$status"
