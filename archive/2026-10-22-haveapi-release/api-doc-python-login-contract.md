# Python rendered token-login input correction

Bounded design, 2026-10-22. Source baseline remains immutable until the lead's
implementation grant: `ee150c8515aae399dc14e0fe9daefeb95a8bb17e` (tree
`fed8aea303bb91eb488c4c4bbc639356a7488c21`). Earlier core/build/package/smoke
checks passed; actual installed wheel no-token login failed. This is a renderer
contract defect, not a Python runtime/authentication or mounted-path defect.

## Established evidence

- `api-doc-url-verification-result.json`, `.log` and `.exit` retain the failed
  run, ending 2026-10-22T18:01:09Z. `dynamic_acceptance.rb:110` rejected the
  missing Authenticated marker for `auth-token-python-sync`.
- `api-doc-url-acceptance-results/dynamic-wheel/example-16.py` supplies user,
  password and scope to `begin_token_login`. Existing-token execution passed;
  the separate `example-16-challenge.log` reports local input validation failure.
- Implementer1's pure Rack OPTIONS → actual Python parse/build_request receipt:
  token request route `/mount/_auth/token/tokens`; required metadata is user=true,
  password=true, scope=false, lifetime=true, interval=false. Missing lifetime
  raises `ValidationError.errors == {'lifetime': ['required parameter is missing']}`.
  Adding explicit advertised `lifetime='fixed'` succeeds and includes that field
  in the body; interval remains absent. No listener or runtime change was needed.
- `DynamicHelpers#token_login_fields` drops token/lifetime/interval by name.
  Python renderer reuses it, but `Client` and `AsyncClient.begin_token_login`
  pass caller values unchanged to the same validator. JS supplies its own
  renewable_auto lifetime internally; Python intentionally does not.
- Server `authentication/token/provider.rb` declares required lifetime with
  choices fixed/renewable_manual/renewable_auto/permanent. Interval is optional
  with server-side default 300 and fill=true. Preserve these declarations.

See [package1-python-challenge-diagnosis.md](package1-python-challenge-diagnosis.md)
for the implementer's detailed receipt. Architect did not repeat the native test.

## Frozen correction and interface

For Python initial login examples, retain the existing provider field selection
and include every additionally advertised **required** request field, including
lifetime. Render the value using the existing JSON environment convention:
`"lifetime": json.loads(os.environ["HAVEAPI_AUTH_lifetime"])`.
Read the actual authorized request descriptor; do not infer fields from the
server implementation, hard-code a runtime default or invent fields not advertised.

Keep optional lifecycle fields omitted: specifically, interval remains absent
when optional, letting the existing server default apply. If a schema declares
one required, do not silently exclude it. The smallest implementation can merge
required request-descriptor fields into the Python-only field selection, leaving
the shared helper's JS behavior intact. Shared helper extraction is allowed only
if needed to avoid duplicate descriptor traversal; its existing default behavior
and all JS callers must remain unchanged.

Existing-token `TokenAuth(HAVEAPI_TOKEN)` behavior and challenge continuation
ownership remain intact. Python's challenge object already owns/injects its
continuation token; do not require its token from environment, print it, or alter
`step.submit`/the runtime. This defect concerns the initial request, not a new
token/default API. No changes to client validation, default filling, server schema,
auth provider, actual fixture fields, URL rules or JS lifetime selection.

The installed acceptance harness supplies
`HAVEAPI_AUTH_lifetime=JSON.generate('fixed')` as an explicit fixture input, a
value from the actual advertised enum. It is a test-user choice, not a new client
default. Both Python variants consume it in the no-token branch. Keep optional
interval absent in the harness and assertions. No production credentials used.

## Execution package and boundaries

**implementer1**, after lead grant:

- `servers/ruby/lib/haveapi/client_examples/python_client.rb`: Python-only
  selection of required initial-login fields and its emitted JSON env reference.
- `servers/ruby/lib/haveapi/client_examples/dynamic_helpers.rb`: only optional
  shared descriptor accessor extraction if necessary; preserve JS output/defaults.
- `servers/ruby/spec/client_examples/dynamic_python_spec.rb`: sync+async
  required/optional field-selection regressions and existing-token preservation.
- `servers/ruby/spec/client_examples/dynamic_acceptance.rb`: explicit fixture
  lifetime environment value, no server/fixture schema rewrite.
- Dedicated no-listener auth-render regression spec/support beside the existing
  dynamic specs: actual Rack descriptor → emitted Python → native request builder.
  Prefer a new focused file over unrelated test refactoring. Guide text may clarify
  HAVEAPI_AUTH_* required inputs in the existing dynamic acceptance documentation.

**implementer2** supplies factual Python validator/auth receipt and assesses the
test's fidelity; no Python runtime edit is needed. **implementer0** retains all
Git/index/hooks and any agreed shared test orchestration. Lead owns final prose,
review/verification grants and history. Architect edits design records only.

## Quick regression and acceptance gates

Before commits/review, use actual unchanged Rack-emitted token-request metadata,
not a hand-simplified schema. For both Python sync and async renderers:

1. Verify required lifetime is preserved as HAVEAPI_AUTH_lifetime JSON input;
   optional interval is omitted and existing user/password/scope behavior retained.
2. Obtain the mapping from the actual rendered program (AST extraction or execute
   against a no-network transport), then pass it through real Python
   parse_description/build_request. Explicit valid lifetime produces the exact
   mounted token route and body fields without interval/default invention.
3. Remove required lifetime from that mapping: assert native ValidationError and
   exact lifetime missing-field error before transport. Include a renderer-level
   required-interval case so name-based filtering cannot hide a required field.
4. Preserve existing-token bypass and continuation token ownership. If mocking
   transport for full emitted sync/async control flow, feed real captured Rack
   envelopes and assert request phases/fields; never replace the Python validator.
5. Run the bounded Ruby renderer/style checks and affected quick Python fixture
   checks using declared environments. No listener or installed long acceptance
   is part of the architect's diagnosis or pre-grant work.

This is a **new auth-render contract correction**. Complete and commit all
intended source/tests/guide changes with quick checks passing. The same reviewer
then performs affected-lane final review: actual required metadata fidelity,
runtime/default/continuation ownership, no credential disclosure, sync/async
parity, harness inputs, negative controls and complete affected history. Prior
ee150c85 acceptance/review does not cover the correction. Preserve final release
commit message exactly `Version 0.30.0` during approved history consolidation.

Only after review and lead grant rerun installed wheel and sdist rendered
acceptance, including no-token initial login → challenge → authenticated result
for both Python variants and the actual mounted fixture. Retain emitted programs,
separate existing-token/challenge logs and exact source/artifact identity. Keep
the ordinary examples/actions and JS auth regressions. A local validator error
must not be presented as a transport failure or hidden by a fabricated success.

## Compatibility and recovery

No public runtime API, URL, protocol, schema, database or state migration changes.
Corrected generated documentation asks users for a required value they already
must supply to Python. Existing-token users are unchanged; optional interval
continues using the server's established default. Deploying corrected docs/server
package does not require a Python/JS runtime upgrade or coordinated server change.
Rollback restores the defective example without affecting stored tokens or state.
Publication, default integration and lifecycle actions remain unauthorized.
