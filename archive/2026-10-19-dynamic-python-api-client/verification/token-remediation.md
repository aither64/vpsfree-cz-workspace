# vpsAdmin token verification correction

Status: verified. Final head326c05b78cec149b81e2c516c5cdcb7d1810d678,
tree0882b639badb5c917dd20918f63a803058001785. Fresh targeted token verification
passed both modes:2examples0failures,exit0/64seconds. Native cleanup complete.

The completed batch at Python client `7cb07fa77dd048fa46241a766dfacbbea946f04f`
passed generic server checks, package smoke, release checks and eight of ten
actual vpsAdmin examples. Only tokens/sync and tokens/async failed. Original
artifacts are `vpsadmin.log` and `vpsadmin-rspec.json` in this directory. They
contain no Python failure frames because the original bridge suppressed them
and removed its private child output. The precise original assertion line is
therefore unavailable.

Source inspection of installed HaveAPI 0.29.12 establishes that OPTIONS calls
nonrequiring `authenticated?` and can return public discovery for an unrecognized
token. Protected action routes use `authenticate!` and require authentication.
vpsAdmin ResumeToken excludes closed and expired sessions. The prior test's
expectation that `set_auth` must reject a revoked/expired token at discovery is
incorrect. The correction retains the authorized description and sends a fresh
request to its described `user.current` action using each invalid credential;
HTTP 401/403 and envelope status=false are required. Runtime code is unchanged.
The next run still owns confirming the actual failure disposition.

On a failed child, the bridge now saves only bounded known project file/line
locations, allowlisted exception types and test identity. Messages, source lines,
function names, locals, raw output and manifests are excluded. Files have mode
0600 under the explicitly supplied evidence directory. Secret-injection checks
covered forged locations/types, source/local filtering, permissions and the
80-line bound. Python Ruff and collection, Ruby syntax/RuboCop, and whitespace
checks passed. The original eight passing examples and unrelated successful
verification stages do not need repeating for this test-only correction.

## Targeted recipe after committed-head inspection

Run through a fresh policy verification watcher, after the bounded review of
this correction. It selects exactly the two token examples. The native helper
owns ephemeral MariaDB startup/stop/prune; the bridge owns its loopback listener,
Python children and private manifest cleanup. No production services or node
operations are used.

```bash
set -euo pipefail
haveapi_ref=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi
vpsadmin_ref=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/vpsadmin-reference
evidence_dir=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-dynamic-python-api-client/verification/tokens-rerun
HAVEAPI_REVIEWED_HEAD=326c05b78cec149b81e2c516c5cdcb7d1810d678
test "$(git -C "$haveapi_ref" rev-parse HEAD)" = "$HAVEAPI_REVIEWED_HEAD"
test "$(git -C "$vpsadmin_ref" rev-parse HEAD)" = fb2f51222503a45f2e5a42af505f719e44279ed0
test ! -e "$vpsadmin_ref/api/config/database.yml"
mkdir -p "$evidence_dir"
cd "$vpsadmin_ref"
env -u DATABASE_URL -u BUNDLE_GEMFILE -u RUBYOPT \
  RACK_ENV=test VPSADMIN_PLUGINS=none VPSADMIN_TEST_DB_AUTO=1 \
  HAVEAPI_PYTHON_PROJECT="$haveapi_ref/clients/python" \
  HAVEAPI_PYTHON_EXECUTABLE="$haveapi_ref/clients/python/.venv/bin/python" \
  HAVEAPI_VPSADMIN_EXPECTED_REV=fb2f51222503a45f2e5a42af505f719e44279ed0 \
  HAVEAPI_EXPECTED_SERVER_VERSION=0.29.12 \
  HAVEAPI_VPSADMIN_EVIDENCE_DIR="$evidence_dir" \
  nix develop .#api -c bundle exec rspec \
    --options /dev/null \
    "$haveapi_ref/clients/python/tests/integration/vpsadmin_bridge_spec.rb" \
    --example 'supports tokens with' \
    --format documentation --format json --out "$evidence_dir/rspec.json"
```

The watcher retains complete stdout/stderr in `tokens-rerun/vpsadmin.log` with
the original exit status. On failure, bounded sanitized child evidence is
`tokens-rerun/vpsadmin-tokens-sync-failure.log` or
`tokens-rerun/vpsadmin-tokens-async-failure.log`. Raw child output and private
manifests are not retained. `--options /dev/null` is necessary so database guards
run before the reference checkout's spec_helper.

## Diagnostic review disposition

Retained reviewer accepted protected-token proof and history at9cdb038, requested
D1 source-line range/width/canonical integer and D2 removal of raw child summary
forwarding. Lead accepted and inspected exact narrow Ruby-only reductions;
owner proves huge digits/zero/out-of-range/leading zeros and oversized/fake
summary secret exclusion, bounded bytes/0600. No further review required for
these exact reductions. Bind final folded head in HAVEAPI_REVIEWED_HEAD.

## Verified outcome

Fresh utility verify_python_tokens_2 ran the exact recipe at326c05b and passed
sync+async token scenarios. RSpec duration32.36seconds; full shell operation64s.
Artifacts in tokens-rerun: vpsadmin.log,rspec.json,driver.status,elapsed-seconds.
No raw child diagnostics were retained because both children exited0. Native
helper owns database stop/prune; no verification processes remain. Eight earlier
passing API scenarios plus these two complete the intended core API proof.
