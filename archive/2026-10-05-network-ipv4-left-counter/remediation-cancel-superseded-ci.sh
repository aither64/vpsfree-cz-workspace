#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
command -v gh >/dev/null
case "${1-}" in
  v) repo=vpsadmin; branch=2026-10-05-network-ipv4-left-counter ;;
  w) repo=vpsadmin-webui; branch=dev/network-enabled ;;
  *) exit 2 ;;
esac
revision=$(cat "$tracking/remediation-published-$1.sha")
repo_root="/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/$repo"
for status in queued in_progress; do
  gh run list --repo "vpsfreecz/$repo" --branch "$branch" --status "$status" --limit 1000 \
    --json databaseId,headSha,headBranch,status >"$tracking/remediation-ci-$1-$status.json"
done
python3 - "$tracking" "$1" "$branch" "$revision" <<'PY' >"$tracking/remediation-ci-$1-candidates.txt"
import json, sys
from pathlib import Path
tracking, mode, branch, head = Path(sys.argv[1]), *sys.argv[2:]
seen = set()
for status in ['queued', 'in_progress']:
    runs = json.loads((tracking / f'remediation-ci-{mode}-{status}.json').read_text())
    assert len(runs) < 1000, 'Active-run inventory reached its bound'
    for run in runs:
        assert run['headBranch'] == branch
        if run['status'] not in ['queued', 'in_progress'] or run['headSha'] == head:
            continue
        run_id = int(run['databaseId'])
        if run_id not in seen:
            seen.add(run_id)
            print(run_id)
PY
while IFS= read -r run_id; do
  [[ $(git -C "$repo_root" ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$revision" ]]
  gh run view "$run_id" --repo "vpsfreecz/$repo" --json headSha,headBranch,status >"$tracking/remediation-ci-$1-$run_id-before.json"
  if python3 - "$tracking/remediation-ci-$1-$run_id-before.json" "$branch" "$revision" <<'PY'
import json, sys
run = json.load(open(sys.argv[1]))
assert run['headBranch'] == sys.argv[2]
sys.exit(0 if run['headSha'] != sys.argv[3] and run['status'] in ['queued', 'in_progress'] else 1)
PY
  then
    gh run cancel "$run_id" --repo "vpsfreecz/$repo"
  fi
done <"$tracking/remediation-ci-$1-candidates.txt"
