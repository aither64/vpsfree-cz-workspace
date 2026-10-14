#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
mode=${1:?Missing config/kb mode}
head=${2:?Missing exact published pin head}
branch=2026-10-05-network-ipv4-left-counter
case "$mode" in
  config) repo=vpsfree-cz-configuration ;;
  kb) repo=vpsfree-kb-contracts ;;
  *) exit 2 ;;
esac
repo_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/$repo
[[ ${DEV_SESSION_SLUG-} == "$branch" && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
[[ $# == 2 && $head =~ ^[0-9a-f]{40}$ && $(cat "$tracking/visibility-$mode-published.sha") == "$head" ]]
[[ $(pwd -P) == "$repo_root" && $(git branch --show-current) == "$branch" ]]
[[ $(git remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
[[ $(git rev-parse HEAD) == "$head" && -z $(git status --porcelain) ]]
[[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$head" ]]
for status in queued in_progress; do
  [[ ! -e "$tracking/visibility-ci-$mode-$status.json" ]]
  # Branch filtering previously missed active owned runs; filter exact branch below.
  gh run list --repo "vpsfreecz/$repo" --status "$status" --limit 1000 \
    --json databaseId,headSha,headBranch,status >"$tracking/visibility-ci-$mode-$status.json"
done
python3 - "$tracking" "$branch" "$head" "$mode" <<'PY' >"$tracking/visibility-ci-$mode-candidates.txt"
import json
import sys
from pathlib import Path
tracking, branch, head, mode = Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
seen = set()
for status in ['queued', 'in_progress']:
    runs = json.loads((tracking / f'visibility-ci-{mode}-{status}.json').read_text())
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
  gh run view "$run_id" --repo "vpsfreecz/$repo" --json headSha,headBranch,status \
    >"$tracking/visibility-ci-$mode-$run_id-before.json"
  if python3 - "$tracking/visibility-ci-$mode-$run_id-before.json" "$branch" "$head" <<'PY'
import json
import sys
run = json.load(open(sys.argv[1]))
assert run['headBranch'] == sys.argv[2]
sys.exit(0 if run['headSha'] != sys.argv[3] and run['status'] in ['queued', 'in_progress'] else 1)
PY
  then
    gh run cancel "$run_id" --repo "vpsfreecz/$repo"
  fi
done <"$tracking/visibility-ci-$mode-candidates.txt"
