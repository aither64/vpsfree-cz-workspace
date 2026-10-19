#!/usr/bin/env bash
# Launch only after final committed-deliverable review is accepted.
set -euo pipefail

task_workspace=/home/aither/workspace/ai/vpsfree.cz
task_records="$task_workspace/work/2026-10-19-dynamic-python-api-client"
task_haveapi="$task_workspace/worktrees/2026-10-19-dynamic-python-api-client/haveapi"
task_vpsadmin="$task_workspace/worktrees/2026-10-19-dynamic-python-api-client/vpsadmin-reference"
mkdir -p "$task_records/verification"

test -n "${HAVEAPI_REVIEWED_HEAD:?Provide the independently reviewed client head}"
test "$(git -C "$task_haveapi" rev-parse HEAD)" = "$HAVEAPI_REVIEWED_HEAD"
test -z "$(git -C "$task_haveapi" status --porcelain --untracked-files=normal)"
test "$(git -C "$task_vpsadmin" rev-parse HEAD)" = fb2f51222503a45f2e5a42af505f719e44279ed0
test ! -e "$task_vpsadmin/api/config/database.yml"

cd "$task_haveapi"
nix develop -c bash -euo pipefail -c '
  cd servers/ruby
  bundle install
  cd ../../clients/python
  uv sync --locked
  uv run --locked pytest tests/integration/test_ruby_server.py
' > "$task_records/verification/generic-server.log" 2>&1

nix develop .#client-python -c bash -euo pipefail -c '
  cd clients/python
  uv run --locked python utils/package_smoke.py
' > "$task_records/verification/package-smoke.log" 2>&1

nix develop -c make release-test \
  > "$task_records/verification/release-tests.log" 2>&1

cd "$task_vpsadmin"
env -u DATABASE_URL -u BUNDLE_GEMFILE -u RUBYOPT \
  RACK_ENV=test VPSADMIN_PLUGINS=none VPSADMIN_TEST_DB_AUTO=1 \
  HAVEAPI_PYTHON_PROJECT="$task_haveapi/clients/python" \
  HAVEAPI_PYTHON_EXECUTABLE="$task_haveapi/clients/python/.venv/bin/python" \
  HAVEAPI_VPSADMIN_EXPECTED_REV=fb2f51222503a45f2e5a42af505f719e44279ed0 \
  HAVEAPI_EXPECTED_SERVER_VERSION=0.29.12 \
  nix develop .#api -c bundle exec rspec --options /dev/null \
  "$task_haveapi/clients/python/tests/integration/vpsadmin_bridge_spec.rb" \
  --format documentation --format json \
  --out "$task_records/verification/vpsadmin-rspec.json" \
  > "$task_records/verification/vpsadmin.log" 2>&1
