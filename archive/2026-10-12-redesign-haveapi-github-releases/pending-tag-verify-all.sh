#!/usr/bin/env bash
set -uo pipefail
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases
bash "$records/release-verify-local.sh" 355c2990a4bfd3940d3234cb2077ad0127f43551 > "$records/pending-tag-release-verification.log" 2>&1
local_result=$?
printf '%s\n' "$local_result" > "$records/pending-tag-release-verification.status"
printf 'Local verification completed: %s\n' "$local_result"
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c python3 "$records/pending-tag-watch-ci.py" 355c2990a4bfd3940d3234cb2077ad0127f43551 2026-10-19-haveapi-0.29.10 pending-tag-release > "$records/pending-tag-release-ci-watch.log" 2>&1 &
release_pid=$!
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c python3 "$records/pending-tag-watch-ci.py" c58704a08451a231fdf6c6123437133422af46dc 2026-10-12-redesign-haveapi-github-releases pending-tag-master '["release", "RuboCop", "servers/ruby RSpec"]' > "$records/pending-tag-master-ci-watch.log" 2>&1 &
master_pid=$!
wait "$release_pid"
release_result=$?
printf '%s\n' "$release_result" > "$records/pending-tag-release-ci-watch.status"
wait "$master_pid"
master_result=$?
printf '%s\n' "$master_result" > "$records/pending-tag-master-ci-watch.status"
printf 'Local verification: %s; release CI: %s; master CI: %s\n' "$local_result" "$release_result" "$master_result"
if [[ $local_result -ne 0 || $release_result -ne 0 || $master_result -ne 0 ]]; then exit 1; fi
