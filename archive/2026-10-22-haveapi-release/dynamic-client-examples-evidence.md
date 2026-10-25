# Dynamic client documentation package

Implementer1 executed the approved
[renderer contract](api-doc-contract.md) and accepted plan. Scope: six dynamic
renderers (JavaScript callback/async, TypeScript callback/async, Python sync/async)
and a small typed callback action lookup. Shared context/profile/templates/UI,
File system removal, runners and dependency manifests remain implementer0-owned.

## Implementation

The six variants use the frozen context/result ABI, fixed IDs/orders and no SDK
profile requirement. Programs include actual imports, discovery/authentication
completion, mounted API URL and explicit version. Callback examples use typed
`CallbackClient.findResource`/`findAction` and `directInvoke` for a raw response;
async JS/TS uses the real invocation receipt; Python uses exact-name maps,
context managers and the complete asyncio wrapper. Supported authentication uses
environment credentials, existing access tokens or actual token challenge APIs.

Samples retain exact names/path order and literal values. Limitations explain
unsupported input instead of dropping it: JavaScript list or nested query input,
unsafe legacy callback parameter names, numbers outside exact JS precision,
prose-only/incomplete samples, hidden parameters and unsupported providers.
Python retains its supported object/list forms. No public sample wire keys or
metadata values were added. Operation handling uses existing client APIs.

`findAction` adds a private null-prototype index behind the typed public static
helper. Canonical names win; only unambiguous aliases resolve. Unknown or
ambiguous names raise `ProtocolError`. Existing direct attachment and
`actions: string[]` behavior remains covered by compatibility checks.

## Quick evidence

Executed in the prepared root Nix shell with
`HAVEAPI_RELEASE_TOOLS_ONLY=1`, no dependency setup in parallel:

- Server `dynamic_js_spec.rb`, `dynamic_python_spec.rb`,
  `dynamic_acceptance_spec.rb`: **15 examples, 0 failures**, final seed 13622,
  13.53 seconds. Includes ten actual renderer-produced TS programs checked with
  strict semantics against emitted declarations; JS/Python native parsing;
  mounted real HTML extraction; real fixture success/failure request receipts.
- Ruby style for all 13 owned Ruby source/test files: **no offenses**.
- JS `npm run build`: passed, generating bundle/declarations normally.
- `npm run test:compatibility`: **29 passed** including three new action lookup
  runtime cases; legacy callback globals/control flow preserved.
- Description member-clobbering suite: **7 passed**.
- Emitted callback and async TypeScript declaration suites: passed.
- Real Node ESM named imports from the built UMD bundle: passed.
- Final whitespace diff check: passed.

Initial fixture assumptions about callable function `.name`, Python indentation,
compiler fixture path, Rack host and action input namespace were corrected before
final checks. They did not require changing public client behavior. Nix concurrent
evaluation sometimes printed ignored SQLite cache contention; commands completed
with their own pass/fail results.

## Longer acceptance source and remaining gate

`servers/ruby/spec/client_examples/dynamic_acceptance.rb` and its mounted fixture
are authored **before final review**. The harness installs retained npm and
Python artifacts into an isolated consumer/venv, fetches real served HTML,
extracts actual snippets, compiles TS with strict checking against installed
package declarations, executes JS/Python and verifies fixture receipts. It covers
Basic/existing token/OAuth credentials and a deterministic two-step token flow.
Run for wheel and sdist separately, with evidence retained. Startup/execution
cleanup owns only its disposable fixture and consumer. Exact commands are in
the prose-reviewed `dynamic_acceptance.md` beside the harness and were sent to
implementer0 for shared runner orchestration.

The long installed-package operation has **not** run yet. It waits for completed,
committed-deliverable independent review. No claim that quick parse/type checks
establish full client execution acceptance is made.

The lead applied the main prose pass to all seven renderer files/labels, JS
helper README addition and dynamic acceptance guide. All paths and approved
three-way commit split were delivered to implementer0, which retains sole
Git/index/hooks ownership and can commit on this package owner's behalf. No Git,
registry publication, tag, default integration or lifecycle operation was run
by implementer1 for this package. No database/protocol/persistent-state migration.
