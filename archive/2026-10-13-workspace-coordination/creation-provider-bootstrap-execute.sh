#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
export DEV_SESSION_SLUG=2026-10-13-workspace-coordination
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
trap 'operation_status=$?; printf "%s\n" "$operation_status" > "$tracking/creation-provider-bootstrap-execution.status.tmp"; mv "$tracking/creation-provider-bootstrap-execution.status.tmp" "$tracking/creation-provider-bootstrap-execution.status"' EXIT
candidate=$(cat "$tracking/creation-provider-candidate.path")
source=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["source"])' "$tracking/creation-provider-bootstrap-prepared.json")
profile_token=$(cat "$tracking/creation-provider-bootstrap-predecessor-token")
"$candidate/bin/workspace-host" coordination-bootstrap --source "$source" --workspace vpsfree-cz --session "$DEV_SESSION_SLUG" --expected-profile-token "$profile_token" --request "$tracking/creation-provider-bootstrap-execution-request.json" > "$tracking/creation-provider-bootstrap-result.json.tmp"
python3 -c 'import json,sys;assert json.load(open(sys.argv[1]))["state"]=="deployed_review"' "$tracking/creation-provider-bootstrap-result.json.tmp"
mv "$tracking/creation-provider-bootstrap-result.json.tmp" "$tracking/creation-provider-bootstrap-result.json"
