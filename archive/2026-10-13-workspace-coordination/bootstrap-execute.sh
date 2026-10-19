#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
export DEV_SESSION_SLUG=2026-10-13-workspace-coordination
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
trap 'operation_status=$?; printf "%s\n" "$operation_status" > "$tracking/bootstrap-execution.status.tmp"; mv "$tracking/bootstrap-execution.status.tmp" "$tracking/bootstrap-execution.status"' EXIT
candidate=$(cat "$tracking/candidate-package.path")
source=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["source"])' "$tracking/bootstrap-prepared.json")
profile_token=$(cat "$tracking/bootstrap-predecessor-token")
"$candidate/bin/workspace-host" coordination-bootstrap --source "$source" --workspace vpsfree-cz --session "$DEV_SESSION_SLUG" --expected-profile-token "$profile_token" --request "$tracking/bootstrap-execution-request.json" > "$tracking/bootstrap-result.json.tmp"
python3 -c 'import json,sys;assert json.load(open(sys.argv[1]))["state"]=="deployed_review"' "$tracking/bootstrap-result.json.tmp"
mv "$tracking/bootstrap-result.json.tmp" "$tracking/bootstrap-result.json"
