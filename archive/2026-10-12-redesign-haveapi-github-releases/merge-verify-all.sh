#!/usr/bin/env bash
set -uo pipefail
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases
bash "$records/verify.sh" "$1" > "$records/merge-verification.log" 2>&1
local_result=$?
printf '%s\n' "$local_result" > "$records/merge-verification.status"
python3 "$records/merge-watch-ci.py" "$1" \
  2026-10-12-redesign-haveapi-github-releases merge \
  > "$records/merge-ci-watch.log" 2>&1
ci_result=$?
printf '%s\n' "$ci_result" > "$records/merge-ci-watch.status"
printf 'Local verification: %s; CI: %s\n' "$local_result" "$ci_result"
if [[ $local_result -ne 0 || $ci_result -ne 0 ]]; then
  exit 1
fi
