#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
v_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
branch=2026-10-05-network-ipv4-left-counter
head=${1:?Missing exact published V head}
[[ ${DEV_SESSION_SLUG-} == "$branch" && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $head =~ ^[0-9a-f]{40}$ && $(cat "$tracking/visibility-review-fixed-v-published.sha") == "$head" ]]
[[ $(cat "$tracking/visibility-review-fixed-v.sha") == "$head" ]]
[[ $(pwd -P) == "$v_root" && $(git branch --show-current) == "$branch" ]]
[[ $(git remote get-url origin) == git@github.com:vpsfreecz/vpsadmin.git ]]
[[ $(git rev-parse HEAD) == "$head" && -z $(git status --porcelain) ]]
[[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$head" ]]
for status in queued in_progress; do
  [[ ! -e "$tracking/visibility-review-fixed-ci-v-$status.json" ]]
  # Branch filtering previously missed active owned runs; filter exact branch below.
  gh run list --repo vpsfreecz/vpsadmin --status "$status" --limit 1000 \
    --json databaseId,headSha,headBranch,status >"$tracking/visibility-review-fixed-ci-v-$status.json"
done
python3 - "$tracking" "$branch" "$head" <<'PY' >"$tracking/visibility-review-fixed-ci-v-candidates.txt"
import json
import sys
from pathlib import Path
tracking, branch, head = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
seen = set()
for status in ['queued', 'in_progress']:
    runs = json.loads((tracking / f'visibility-review-fixed-ci-v-{status}.json').read_text())
    assert len(runs) < 1000, 'Active-run inventory reached its bound'
    for run in runs:
        if run['headBranch'] != branch:
            continue
        if run['status'] not in ['queued', 'in_progress'] or run['headSha'] == head:
            continue
        run_id = int(run['databaseId'])
        if run_id not in seen:
            seen.add(run_id)
            print(run_id)
PY
while IFS= read -r run_id; do
  [[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$head" ]]
  gh run view "$run_id" --repo vpsfreecz/vpsadmin --json headSha,headBranch,status \
    >"$tracking/visibility-review-fixed-ci-v-$run_id-before.json"
  if python3 - "$tracking/visibility-review-fixed-ci-v-$run_id-before.json" "$branch" "$head" <<'PY'
import json
import sys
run = json.load(open(sys.argv[1]))
assert run['headBranch'] == sys.argv[2]
sys.exit(0 if run['headSha'] != sys.argv[3] and run['status'] in ['queued', 'in_progress'] else 1)
PY
  then
    gh run cancel "$run_id" --repo vpsfreecz/vpsadmin
  fi
done <"$tracking/visibility-review-fixed-ci-v-candidates.txt"
