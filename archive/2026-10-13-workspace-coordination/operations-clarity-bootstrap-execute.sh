#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
export DEV_SESSION_SLUG=2026-10-13-workspace-coordination
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
trap 'operation_status=$?; printf "%s\n" "$operation_status" > "$tracking/operations-clarity-bootstrap-execution.status.tmp"; mv "$tracking/operations-clarity-bootstrap-execution.status.tmp" "$tracking/operations-clarity-bootstrap-execution.status"' EXIT
candidate=$(cat "$tracking/operations-clarity-candidate.path")
source=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["source"])' "$tracking/operations-clarity-bootstrap-prepared.json")
profile_token=$(cat "$tracking/operations-clarity-bootstrap-predecessor-token")
"$candidate/bin/workspace-host" coordination-bootstrap --source "$source" --workspace vpsfree-cz --session "$DEV_SESSION_SLUG" --expected-profile-token "$profile_token" --request "$tracking/operations-clarity-bootstrap-execution-request.json" > "$tracking/operations-clarity-bootstrap-result.json.tmp"
python3 -c 'import json,sys;assert json.load(open(sys.argv[1]))["state"]=="deployed_review"' "$tracking/operations-clarity-bootstrap-result.json.tmp"
mv "$tracking/operations-clarity-bootstrap-result.json.tmp" "$tracking/operations-clarity-bootstrap-result.json"
