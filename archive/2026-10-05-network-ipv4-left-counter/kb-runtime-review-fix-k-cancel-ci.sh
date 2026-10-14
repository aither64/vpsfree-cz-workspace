#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
branch=2026-10-05-network-ipv4-left-counter-kb-runtime
head=$(cat "$tracking/kb-runtime-review-fix-publish1.published.sha")
[[ "$head" =~ ^[0-9a-f]{40}$ ]]
test "$(cat "$tracking/kb-runtime-review-fix-publish1.published.sha")" = "$head"
test "$(git -C "$repo" rev-parse HEAD)" = "$head"
test "$(git -C "$repo" ls-remote --heads origin "refs/heads/$branch" | cut -f1)" = "$head"
set -o noclobber
for status in queued in_progress; do
  gh run list --repo vpsfreecz/vpsfree-kb-contracts --status "$status" --limit 1000 \
    --json databaseId,headSha,headBranch,status > "$tracking/kb-runtime-review-fix-k-ci-$status.json"
done
python3 - "$tracking" "$branch" "$head" <<'PY' > "$tracking/kb-runtime-review-fix-k-ci-candidates.txt"
import json,sys,pathlib
tracking,branch,head=pathlib.Path(sys.argv[1]),*sys.argv[2:]
seen=set()
for status in ('queued','in_progress'):
 runs=json.loads((tracking/f'kb-runtime-review-fix-k-ci-{status}.json').read_text())
 assert len(runs)<1000,'active CI inventory saturated'
 for run in runs:
  if run['headBranch']!=branch or run['headSha']==head or run['status'] not in ('queued','in_progress'): continue
  ident=int(run['databaseId'])
  if ident not in seen:
   seen.add(ident); print(ident)
PY
while IFS= read -r run; do
  test "$(git -C "$repo" ls-remote --heads origin "refs/heads/$branch" | cut -f1)" = "$head"
  gh run view "$run" --repo vpsfreecz/vpsfree-kb-contracts --json headSha,headBranch,status \
    > "$tracking/kb-runtime-review-fix-k-ci-$run-before.json"
  if python3 - "$tracking/kb-runtime-review-fix-k-ci-$run-before.json" "$branch" "$head" <<'PY'
import json,sys
value=json.load(open(sys.argv[1]))
assert value['headBranch']==sys.argv[2],'CI branch changed'
sys.exit(0 if value['headSha']!=sys.argv[3] and value['status'] in ('queued','in_progress') else 1)
PY
  then
    gh run cancel "$run" --repo vpsfreecz/vpsfree-kb-contracts
  fi
done < "$tracking/kb-runtime-review-fix-k-ci-candidates.txt"
