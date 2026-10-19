#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination
export DEV_SESSION_SLUG=2026-10-13-workspace-coordination
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
trap 'operation_status=$?; printf "%s\n" "$operation_status" > "$tracking/bootstrap-prepare.status.tmp"; mv "$tracking/bootstrap-prepare.status.tmp" "$tracking/bootstrap-prepare.status"' EXIT
candidate=$(cat "$tracking/candidate-package.path")
if ! test -x "$candidate/bin/workspace-host"; then
  printf 'Candidate package is unavailable: %s\n' "$candidate" >&2
  exit 1
fi
profile_token=$(ruby -r "$group/dev-workspace/libexec/workspace-profile-identity" -e 'puts DevWorkspaceProfileIdentity.token(ARGV.fetch(0))' /home/aither/.local/state/dev-workspaces/profile)
test -n "$profile_token"
printf '%s\n' "$profile_token" > "$tracking/bootstrap-predecessor-token"
"$candidate/bin/workspace-host" coordination-bootstrap --source "$group/workspace" --workspace vpsfree-cz --session "$DEV_SESSION_SLUG" --expected-profile-token "$profile_token" --request "$tracking/bootstrap-prepare-request.json" --prepare > "$tracking/bootstrap-prepared.json.tmp"
python3 - "$tracking/bootstrap-prepared.json.tmp" "$tracking/bootstrap-execution-request.json" <<'PY'
import json,sys
from pathlib import Path
v=json.loads(Path(sys.argv[1]).read_text())
assert v['schema']==1 and v['source'].startswith('/')
Path(sys.argv[2]).write_text(json.dumps(v['request'],separators=(',',':'))+'\n')
PY
mv "$tracking/bootstrap-prepared.json.tmp" "$tracking/bootstrap-prepared.json"
