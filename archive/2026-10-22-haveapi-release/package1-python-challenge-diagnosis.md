# Python token challenge: required request input omitted

Owner: implementer1. Read-only diagnosis at reviewed feature head
`ee150c8515aae399dc14e0fe9daefeb95a8bb17e`. Session/env binding and retained
owner/peer roster matched. Applicable workspace documentation/verification and
HaveAPI AGENTS/development guidance reread. Existing receipts and failed artifacts
remain unchanged. No source/Git/build/listener/acceptance mutation or retry.

## Installed evidence and exact owning seams

- `api-doc-url-verification.log` records the first failed panel as
  `auth-token-python-sync`, from `dynamic_acceptance.rb:110`.
- `api-doc-url-acceptance-results/dynamic-wheel/example-16.py` is the actual
  rendered program. Its `begin_token_login` mapping contains `user`, `password`
  and `scope`, obtained from their `HAVEAPI_AUTH_*` JSON environment values.
  It contains no `lifetime` or `interval`.
- `example-16.log` contains `Authenticated` for the existing-token branch.
  `example-16-challenge.log` contains `input parameters are not valid None`.
- The sanitized fixture trace shows preceding JS/TS request/verify POSTs
  succeeding, then only OPTIONS for the Python attempt. No Python token POST
  occurs: validation rejects before transport.
- `servers/ruby/lib/haveapi/client_examples/python_client.rb#auth` gets its
  fields from `dynamic_helpers.rb#token_login_fields`. That shared helper
  unconditionally removes `token`, `lifetime` and `interval`.
- `clients/python/src/haveapi_client/{client,async_client}.py` implement
  `begin_token_login` -> `_login_step` -> `_invoke` with the caller mapping.
  Neither adds a lifetime. `_resources/state.py#_token_action` reads the real
  advertised provider action; the common request builder applies typed required
  input validation. This is the documented Python input contract.
- Server `authentication/token/provider.rb` advertises required `lifetime`;
  JS token implementations independently add their own existing lifetime value.
  Reusing that JS field exclusion in Python drops a required input.

## Confirmed pure native reproduction

Known-quick command in the prepared tools-only root Nix shell, no listener:

```text
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -s
  cd servers/ruby
  bundle exec ruby (Rack::MockRequest + Open3)
```

Ruby loads `test_support/dynamic_documentation_api`, obtains the real
`OPTIONS http://example.test/mount/v2/` envelope through Rack, and passes it as
JSON stdin to `clients/python/.venv/bin/python`, with explicit
`PYTHONPATH=clients/python/src` and `PYTHONDONTWRITEBYTECODE=1`. The Python
reproduction is:

```python
import json, sys
from haveapi_client._protocol import (
    parse_description, parse_resources, CallContext, build_request,
)
from haveapi_client.exceptions import ValidationError

description = parse_description(json.load(sys.stdin))
action = parse_resources(
    description.authentication['token']['resources']
)['token'].actions['request']
for lifetime in (None, 'fixed'):
    params = {'user': 'fixture-user', 'password': 'fixture-password', 'scope': 'all'}
    if lifetime is not None:
        params['lifetime'] = lifetime
    try:
        request = build_request(
            description, CallContext(action, (), {}, 1),
            base_url='http://example.test/mount/', params=params,
        )
        print(request.url, list(json.loads(request.content)['token']))
    except ValidationError as error:
        print(error.message, {key: list(value) for key, value in error.errors.items()})
```

Actual schema and outcomes:

| Field | Required |
| --- | --- |
| user | true |
| password | true |
| scope | false |
| lifetime | true |
| interval | false |

- Exact emitted mapping: `ValidationError`, message `input parameters are not
  valid`, errors `{'lifetime': ['required parameter is missing']}`.
- Explicit `lifetime='fixed'`, one of the actual advertised allowed choices:
  request URL `http://example.test/mount/_auth/token/tokens`; JSON input fields
  `user`, `password`, `scope`, `lifetime`. Optional `interval` remains omitted.
- The first diagnostic serializer attempted to JSON-encode immutable
  `error.errors` directly and failed on `mappingproxy`; converting it to a plain
  dictionary produced the exact receipt above. This was a diagnostic-script
  issue, not a client defect. Nix substituted small cached shell dependencies;
  no application/package build or installation was run.

## Proposed smallest faithful correction, not yet authorized

Owner1 renderer/helper/harness/test package should preserve actual advertised
required request fields, including `lifetime`, as explicit environment inputs.
A harness value is deliberate fixture input, not a new client default. Keep
optional omission and client-managed continuation tokens; retain JS behavior.
No Python runtime/default change, validator relaxation, new sample key or real
fixture descriptor/route rewrite is needed.

Likely source owners: Python renderer and narrowly parameterized shared field
selection if necessary; `dynamic_python_spec.rb`; supplemental actual-Python
checks under `test_support/dynamic_protocol_spec.rb`; `dynamic_acceptance.rb`
environment setup and its guide. Exact field-selection policy belongs in the
architect's bounded brief before edits.

Proposed no-listener regression: obtain the real Rack auth schema, prove the
current emitted mapping rejects the required field, then check both actual
rendered Python variants with explicit required environment input against real
Python auth/validation through mocked transport, recording request phases and
fields. Verify existing-token and optional omission controls without relaxing
schema. Installed wheel/sdist execution remains a later lead/watcher gate.

Exact observations were sent directly to architect0 and implementer2; architect
owns contract reconciliation and lead owns the implementation grant. All source
remains untouched. No operation remains active.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
