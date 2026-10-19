#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
export DEV_SESSION_SLUG=2026-10-13-workspace-coordination
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
trap 'operation_status=$?; printf "%s\n" "$operation_status" > "$tracking/merge-fix-bootstrap-execution.status.tmp"; mv "$tracking/merge-fix-bootstrap-execution.status.tmp" "$tracking/merge-fix-bootstrap-execution.status"' EXIT
candidate=$(cat "$tracking/merge-fix-candidate.path")
source=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["source"])' "$tracking/merge-fix-bootstrap-prepared.json")
profile_token=$(cat "$tracking/merge-fix-bootstrap-predecessor-token")
"$candidate/bin/workspace-host" coordination-bootstrap --source "$source" --workspace vpsfree-cz --session "$DEV_SESSION_SLUG" --expected-profile-token "$profile_token" --request "$tracking/merge-fix-bootstrap-execution-request.json" > "$tracking/merge-fix-bootstrap-result.json.tmp"
python3 -c 'import json,sys;assert json.load(open(sys.argv[1]))["state"]=="deployed_review"' "$tracking/merge-fix-bootstrap-result.json.tmp"
mv "$tracking/merge-fix-bootstrap-result.json.tmp" "$tracking/merge-fix-bootstrap-result.json"
