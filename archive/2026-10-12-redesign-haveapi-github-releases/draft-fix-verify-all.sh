#!/usr/bin/env bash
set -uo pipefail
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases
bash "$records/release-verify-local.sh" 7fb218e28a86ab1d27de74ccb92c2a45063a4f78 > "$records/draft-fix-release-verification.log" 2>&1
local_result=$?
printf '%s\n' "$local_result" > "$records/draft-fix-release-verification.status"
printf 'Local verification completed: %s\n' "$local_result"
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c python3 "$records/draft-fix-watch-ci.py" 7fb218e28a86ab1d27de74ccb92c2a45063a4f78 2026-10-19-haveapi-0.29.10 draft-fix-release > "$records/draft-fix-release-ci-watch.log" 2>&1 &
release_pid=$!
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c python3 "$records/draft-fix-watch-ci.py" 526648131af45df68c25ac0042a52f22c7a81df5 2026-10-12-redesign-haveapi-github-releases draft-fix-master '["release", "RuboCop"]' > "$records/draft-fix-master-ci-watch.log" 2>&1 &
master_pid=$!
wait "$release_pid"
release_result=$?
printf '%s\n' "$release_result" > "$records/draft-fix-release-ci-watch.status"
wait "$master_pid"
master_result=$?
printf '%s\n' "$master_result" > "$records/draft-fix-master-ci-watch.status"
printf 'Local verification: %s; release CI: %s; master CI: %s\n' "$local_result" "$release_result" "$master_result"
if [[ $local_result -ne 0 || $release_result -ne 0 || $master_result -ne 0 ]]; then exit 1; fi
