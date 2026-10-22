# Python client verification against real vpsAdmin

Status: ready to implement the test bridge, not an executed test result.
Prepared 2026-10-19 from canonical source inspection. Long checks run only after
completed implementation, committed changes, quick checks and final independent
review, through the required fresh verification watcher. Environment setup can
be separately assigned by the lead; it is not proof of compatibility.

## Least-cost real integration

Run the **real** vpsAdmin Rack application against an ephemeral MariaDB using its
existing RSpec bootstrap. Serve it on loopback while the Python client performs
HTTP requests. No node VM, RabbitMQ service, Redis service, deployment or server
application edit is planned. A HaveAPI-owned bridge is necessary; it does not
exist merely because this plan names its files.

Read-only reference checkout, created and owned by this session:

```text
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/vpsadmin-reference
fb2f51222503a45f2e5a42af505f719e44279ed0
```

HaveAPI implementation checkout:

```text
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi
```

Source evidence in the reference revision:

- `api/spec/spec_helper.rb`: establishes the test DB, loads the schema and real
  application; before-suite hooks install minimal config/resources and SpecSeed.
- `api/spec/support/db_setup.rb`: auto-starts a DB when DATABASE_URL and
  `api/config/database.yml` are absent. **RACK_ENV=test can drop/recreate the
  configured database**, so inherited database settings must be rejected/scrubbed.
- `tools/test_db.rb:auto_start!`: unique temporary state directory, random free
  port, at-exit stop/prune. Avoid the manual shared fixed-port database.
- `api/spec/support/app_helper.rb`: `ApiAppHelper.app_instance` is
  `VpsAdmin::API.default.app`.
- `api/spec/support/spec_seed.rb`: ordinary `user`/`otheruser`, `admin`,
  environments, nodes, pools, templates and fixture passwords. These node rows
  represent database records, not running machines.
- `api/spec/support/core_resource_spec_helpers.rb:create_vps!` and
  `vps_chain_spec_helpers.rb:create_network_interface!` create the minimum read
  fixtures. `api/spec/api/resources/vps_read_spec.rb` verifies ownership filtering.
- `api/spec/lib/vpsadmin/api/authentication/token_config_spec.rb` shows actual
  token, TOTP and forced-reset fixture preparation, and suppresses notification
  dispatch in reset tests. `auth_operation_helpers.rb` creates confirmed/enabled
  TOTP devices. Authentication handlers themselves must not be stubbed.
- `flake.nix` API shell supplies Ruby 3.4, MariaDB/client headers and Bundler,
  enters `api/`, and installs its Gemfile. Rackup/WEBrick are declared development
  dependencies; RSpec/rack-test are declared test dependencies.

## Independent implementation package

Lead can assign to implementer2 after C, keeping implementer1's generic harness
and root tooling files untouched. Exact new HaveAPI files:

```text
clients/python/tests/integration/vpsadmin_bridge_spec.rb
clients/python/tests/integration/test_vpsadmin_live.py
clients/python/tests/integration/vpsadmin_support.py
```

`vpsadmin_bridge_spec.rb` validates its environment first, then requires the
reference checkout's spec_helper by absolute path resolved from the API CWD. Define RSpec examples tagged
`:no_transaction`; otherwise the server thread's DB connection cannot see
uncommitted seed data created by the test thread. Existing before-suite hooks
must actually run: merely requiring spec_helper in a standalone Rack script is
insufficient. Do not patch vpsAdmin files or write API configuration into the
reference checkout. Generated Gemfile.lock/.gems from its prescribed dev shell
are dependency setup artifacts, not server source modifications.

For each scenario, restore/reseed relevant user flags/passwords, prepare records,
then start Rackup::Handler::WEBrick with Host=127.0.0.1, Port=0 and suppressed
access logging. Obtain its actual bound port from the running listener. Bound
readiness to a deadline and fail if its thread exits. Use an ActiveRecord
connection-pool scope per Rack request. Each scenario invokes the existing Python
venv interpreter with pytest for the designated case and sync/async modes. Pass
base URL and expected fixture IDs through a temporary private JSON manifest;
never add a public seed/admin endpoint. Python subprocess failure fails RSpec.

The bridge owns WEBrick shutdown/join, child cancellation/reaping and temporary
manifest cleanup in ensure blocks. MariaDB remains owned by the reference
auto-start helper and its at-exit cleanup. SIGTERM must unwind these scopes.
Stop only owned test processes, never the development session. Python subprocess
environment should remove Ruby/Bundler variables and PYTHONPATH, using the exact
provided interpreter; do not launch a second uv dependency resolution inside Ruby.

Seed three user VPS rows and one other-user VPS; add one network interface per
owner. Set enable_basic_auth/enable_token_auth explicitly; disable
enable_new_login_notification to avoid unrelated asynchronous mail. Configure
TOTP/reset users as separate scenarios or restore users between scenarios.
Use fresh real TOTP codes (standard-library HMAC in Python against a private
fixture secret, or a just-generated Ruby code); avoid recovery-code flow, which
adds a separate notification path. Use a sufficiently long fixture password.

Only external side effects may be suppressed: deterministic PTR lookup and
`TransactionChains::User::PasswordChanged.fire` for the email notification.
Document these in results. Leave password validation, TOTP verification, token
generation/continuations, session persistence, permissions, OPTIONS, serializers
and resource queries real. Fail on unexpected background-service connections;
do not broaden stubs to make an unexplained failure disappear. Existing RSpec
helpers demonstrate this boundary, but running it over HTTP remains unverified.

## Proposed commands and prerequisites

Commands below are runnable **after the three bridge files are implemented**.
They are recipes for the lead/watcher, not commands already run. Ensure the
Python lock/venv has been installed with pytest through B's client shell, and
record the exact Python client commit before final execution.

Known quick preflight, from workspace root:

```bash
set -euo pipefail
haveapi_ref=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi
vpsadmin_ref=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/vpsadmin-reference
test "$(git -C "$vpsadmin_ref" rev-parse HEAD)" = fb2f51222503a45f2e5a42af505f719e44279ed0
test ! -e "$vpsadmin_ref/api/config/database.yml"
test -x "$haveapi_ref/clients/python/.venv/bin/python"
test -f "$haveapi_ref/clients/python/tests/integration/vpsadmin_bridge_spec.rb"
```

Assigned setup/verification runner, after the final-review gate for the integration
command (the Nix shell hook itself resolves/builds dependencies and needs a watcher
when duration is uncertain):

```bash
set -euo pipefail
haveapi_ref=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi
vpsadmin_ref=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/vpsadmin-reference
evidence_dir=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-dynamic-python-api-client/vpsadmin-verification
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
    --format documentation --format json \
    --out "$evidence_dir/rspec.json"
```

`api/.rspec` automatically requires spec_helper, before a bridge could guard
its database environment. Therefore `--options /dev/null` deliberately disables
that local RSpec options file; the bridge itself performs guards and then
`require File.join(Dir.pwd, "spec/spec_helper.rb")`. The command supplies its
formatters explicitly. This is RSpec configuration, not bypassing Git hooks.

Before requiring the helper, bridge verifies RACK_ENV=test, core plugin mode,
expected reference revision, absent database.yml and no externally supplied
DATABASE_URL. After helper auto-start, its generated DATABASE_URL is expected.
Verify actual HaveAPI gem equals HAVEAPI_EXPECTED_SERVER_VERSION; fail on another
version rather than claiming baseline coverage. Check/create the connection only
through the native test helper. Never point this run at a developer/production DB.

The API shell may choose a different HaveAPI patch under `~> 0.29.9`. If so,
record the lock and have the owner prepare an isolated exact-version dependency
manifest/lock (without changing vpsAdmin source) before the run. Do not silently
substitute a new baseline. No kernel or guest build is expected; an unexpected
kernel build is a stop/investigation condition under workspace verification rules.

## Actual HTTP acceptance cases (both clients)

1. Public OPTIONS works; Basic user/admin connect and `user.current` returns the
   correct identity. Unauthorized resources/actions/parameters are absent or
   unusable; changing auth refreshes description and invalidates old proxies.
2. User VPS list/show returns exactly own seeded IDs; admin sees both owners;
   other-user show is rejected. Filtered network_interface reads return the
   expected interface. Use declared names/aliases/namespaces from real discovery.
3. Request count metadata and includes; preserve `total_count`, object metadata,
   and association ID/label. Nullable filter and bad typed parameter cases must
   match core/wire behavior. Do not mistake empty list for request failure.
4. Exercise two or more bounded list calls with `limit=1` and from_id under
   the source's ascending comparison; assert IDs strictly progress and cover the
   expected seeded set. Record observed ordering. If the resource does not
   guarantee ordering, test explicit pages and report that limitation rather
   than presenting a universal stable paginator guarantee.
5. Real token password login with fixed/manual-renewable lifetime returns
   Authenticated, then authorized reads; test explicit renew where supported,
   revoke and rejection of a fresh request with revoked token. Test short expiry
   with bounded wait or separately prepared already-expired fixture token.
6. TOTP-required user: begin yields typed `totp` challenge, incomplete token
   cannot read user.current, correct code completes login and discovery refresh.
   Invalid code produces a meaningful auth/action error, without automatic retry.
7. Forced-reset user: begin yields `reset_password`; mismatched/too-short input
   fails; valid submission changes the password and returns a real usable session.
   Also exercise TOTP then reset in order if supported by this pinned source.
   Confirm old password fails and no session is presented before completion.

No vpsAdmin start/stop/create/migrate operation is executed here. Generic Ruby
HaveAPI harness verifies operation waiting/cancellation; API-only vpsAdmin proof
does not demonstrate node transaction completion, actual VPS lifecycle, browser
OAuth/WebAuthn or plugin-specific APIs. Those require a separately scoped owned
cluster/browser run and are not necessary to prove this initial HTTP client
interoperates with the real core API.

## Released HaveAPI baseline

Select **HaveAPI 0.29.12**, newest tag on the supported 0.29 release branch in the
inspected refs. `v0.29.12` peels to commit
`355c2990a4bfd3940d3234cb2077ad0127f43551`. RubyGems authoritative version metadata
at `https://rubygems.org/api/v2/rubygems/haveapi/versions/0.29.12.json` confirms
publication on 2026-10-19T19:49:02.495Z and SHA-256
`b2b180c696e8a58ff87c0ea9a7d9a5d46ae7c6203db5eb47f2af3414d024f4ed`.
This was metadata inspection, not an installation or integration test.

The real vpsAdmin test using the exact released gem gives released-server evidence
alongside the generic harness using the implementation checkout. Do not add the
older 0.29.9 matrix by default. No second HaveAPI release worktree is required for
this least-cost path; use it only if later failures justify direct released
generic-harness comparison, coordinated by the lead.

Retain concise evidence: vpsAdmin commit, Python client commit, actual
Gem.loaded_specs['haveapi'].version, Ruby/Python/Bundler versions, SHA-256 of
effective api/Gemfile.lock and Python uv.lock, scenario count/results in each
client mode, listener/database ownership and cleanup outcome. Report skipped
cases/stubs explicitly. No credentials, continuation tokens, TOTP secrets or
full authenticated envelopes go into published logs.
