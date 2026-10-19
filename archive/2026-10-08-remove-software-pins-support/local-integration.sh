#!/usr/bin/env bash
set -u
local_repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-08-remove-software-pins-support/confctl
local_records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-08-remove-software-pins-support
cd "$local_repo" || exit 1
[[ $(git rev-parse HEAD) == 3be154b5f86125146e444d5fb6aa60916e99b77d ]] || exit 2
[[ -z $(git status --porcelain=v1) ]] || exit 3
local_state=$(mktemp -d /tmp/confctl-integration-3be154b5.XXXXXX)
printf '%s\n' "$local_state" > "$local_records/local-integration.state-path"
printf 'Owned integration state: %s\n' "$local_state"
./test-runner.sh test -f --jobs 2 -t ci --state-dir "$local_state"
local_status=$?
printf '%s\n' "$local_status" > "$local_records/local-integration.exit"
git status --porcelain=v1 > "$local_records/local-integration.source-status"
[[ ! -s "$local_records/local-integration.source-status" ]] || exit 4
exit "$local_status"
