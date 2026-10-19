#!/usr/bin/env bash
set -u
retry_repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-08-remove-software-pins-support/confctl
retry_records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-08-remove-software-pins-support
cd "$retry_repo" || exit 1
[[ $(git rev-parse HEAD) == cc40679d267165aecfa569128438bb55fe910268 ]] || exit 2
[[ -z $(git status --porcelain=v1) ]] || exit 3
./test-runner.sh ls '{deploy/flakes,carrier/netboot}' > "$retry_records/fixture-integration-retry.selection" || exit 5
python3 - "$retry_records/fixture-integration-retry.selection" <<'CHECK'
import sys
from pathlib import Path
lines=Path(sys.argv[1]).read_text().splitlines()
assert sorted(lines) == ['carrier/netboot', 'deploy/flakes'], lines
CHECK
[[ $? == 0 ]] || exit 6
retry_state=$(mktemp -d /tmp/confctl-integration-cc40679d.XXXXXX)
printf '%s\n' "$retry_state" > "$retry_records/fixture-integration-retry.state-path"
printf 'Owned retry state: %s\n' "$retry_state"
./test-runner.sh test -f --jobs 2 --state-dir "$retry_state" '{deploy/flakes,carrier/netboot}'
retry_status=$?
printf '%s\n' "$retry_status" > "$retry_records/fixture-integration-retry.exit"
git status --porcelain=v1 > "$retry_records/fixture-integration-retry.source-status"
[[ ! -s "$retry_records/fixture-integration-retry.source-status" ]] || exit 4
exit "$retry_status"
