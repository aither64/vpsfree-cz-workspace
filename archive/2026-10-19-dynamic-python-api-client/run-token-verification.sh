#!/usr/bin/env bash
set -euo pipefail
task_workspace=/home/aither/workspace/ai/vpsfree.cz
task_haveapi="$task_workspace/worktrees/2026-10-19-dynamic-python-api-client/haveapi"
task_vpsadmin="$task_workspace/worktrees/2026-10-19-dynamic-python-api-client/vpsadmin-reference"
task_evidence="$task_workspace/work/2026-10-19-dynamic-python-api-client/verification/tokens-rerun"
: "${HAVEAPI_REVIEWED_HEAD:?Provide exact reviewed correction head}"
test "$(dev-session current)" = 2026-10-19-dynamic-python-api-client
test "$(git -C "$task_haveapi" rev-parse HEAD)" = "$HAVEAPI_REVIEWED_HEAD"
test -z "$(git -C "$task_haveapi" status --porcelain --untracked-files=normal)"
test "$(git -C "$task_vpsadmin" rev-parse HEAD)" = fb2f51222503a45f2e5a42af505f719e44279ed0
test ! -e "$task_vpsadmin/api/config/database.yml"
mkdir -p "$task_evidence"
cd "$task_vpsadmin"
env -u DATABASE_URL -u BUNDLE_GEMFILE -u RUBYOPT \
  RACK_ENV=test VPSADMIN_PLUGINS=none VPSADMIN_TEST_DB_AUTO=1 \
  HAVEAPI_PYTHON_PROJECT="$task_haveapi/clients/python" \
  HAVEAPI_PYTHON_EXECUTABLE="$task_haveapi/clients/python/.venv/bin/python" \
  HAVEAPI_VPSADMIN_EXPECTED_REV=fb2f51222503a45f2e5a42af505f719e44279ed0 \
  HAVEAPI_EXPECTED_SERVER_VERSION=0.29.12 \
  HAVEAPI_VPSADMIN_EVIDENCE_DIR="$task_evidence" \
  nix develop .#api -c bundle exec rspec --options /dev/null \
    "$task_haveapi/clients/python/tests/integration/vpsadmin_bridge_spec.rb" \
    --example 'supports tokens with' \
    --format documentation --format json --out "$task_evidence/rspec.json"
