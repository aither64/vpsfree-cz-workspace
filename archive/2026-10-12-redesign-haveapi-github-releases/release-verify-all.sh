#!/usr/bin/env bash
set -uo pipefail
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases
expected=b27a031fa03d8d985a3abd2679ce2fc14fe53602
bash "$records/release-verify-local.sh" "$expected" > "$records/release-verification.log" 2>&1
local_result=$?
printf '%s\n' "$local_result" > "$records/release-verification.status"
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c python3 "$records/release-watch-ci.py" "$expected" \
  2026-10-19-haveapi-0.29.10 release > "$records/release-ci-watch.log" 2>&1
ci_result=$?
printf '%s\n' "$ci_result" > "$records/release-ci-watch.status"
printf 'Local verification: %s; CI: %s\n' "$local_result" "$ci_result"
if [[ $local_result -ne 0 || $ci_result -ne 0 ]]; then
  exit 1
fi
