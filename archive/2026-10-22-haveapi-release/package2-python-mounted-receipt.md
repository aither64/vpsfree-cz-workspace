# Python mounted descriptor correction

Owner: implementer2. Source follows the architect-owned
[bounded mounted URL contract](api-doc-mounted-url-contract.md), with explicit
lead implementation grant. Session identity/environment and saved workspace_write
roster member verified. No Git/index/hook operations were performed by this owner.

## Runtime change and compatibility

Only `clients/python/src/haveapi_client/_protocol/request.py` changes runtime
behavior. `resolve_url` has a keyword-only internal `path_mode` with the existing
`api` default. Descriptor mode requires an origin-root-relative path and validates
its static form before substituting encoded path IDs. `build_request` uses that
mode and constructs the bound URL at the API origin, preserving the descriptor's
mount/version components exactly. No prefix heuristic or retry is used.

Discovery/base normalization remains API-relative. No public request API, version
selection, transport, authentication/state API or server route was changed.
`_resources/state.py` already validates the final destination before computing
authentication headers, so no edit to it was necessary. Configured-origin and
mount restrictions, nested encoded static traversal rejection, query/fragment,
userinfo/authority/control/backslash rejection and bound-ID quoting remain.
Tests prove invalid/outside routes trigger no transport or provider-header calls,
and malformed token routes send no login credentials.

The correction affects ordinary actions, global and version-specific token
request/continuation/renew/revoke, and operation-state calls through the existing
shared sync/async request core. Root-mounted APIs retain their URLs. Fabricated
or cached API-relative descriptors beneath a mounted base must be refreshed from
real OPTIONS. No legacy guessing mode or persistent-state/schema migration.

## Exact source package

1. `clients/python/src/haveapi_client/_protocol/request.py`
2. `clients/python/tests/unit/client/test_clients.py`
3. `clients/python/tests/unit/protocol/test_core.py`
4. `clients/python/tests/unit/protocol/test_query_encoding.py`
5. `clients/python/tests/unit/protocol/test_mounted_urls.py`
6. `clients/python/tests/integration/test_mounted_description.py`
7. `clients/python/README.md`
8. `clients/python/CONTRIBUTING.md`

Synthetic unit descriptors were corrected to include their configured mount,
matching the actual server contract; endpoint/query/security coverage remains.
New mocked facade flows cover root/mounted bases, both trailing-slash forms,
default/explicit discovery, global/versioned token routes, continuation and
operation show/cancel. Path tests retain slash/space/percent and encoded slash/
traversal-as-ID-data distinctions.

The additional Rack check obtains the real authenticated OPTIONS envelope from
`DynamicDocumentationAPI.build.app` through `Rack::MockRequest`, then parses and
binds it with Python. It asserts unchanged actual ordinary and global token/
continuation routes. It starts no listener and performs no generated-client or
installed-package acceptance. Its first token-binding attempt omitted the
fixture's required lifetime input; the test was corrected to supply the actual
required input, without changing client defaults or the fixture/server schema.

## Known-quick evidence

Declared environment: `nix develop .#client-python`; prepared locked uv environment,
all commands use `uv run --locked --no-sync`. No dependency installation ran.

- `pytest -q tests/unit tests/integration/test_mounted_description.py`:
  **364 passed in 4.55 seconds**. The Rack subprocess is bounded and no listener
  starts. This includes both mocked facades and all existing unit areas.
- `python utils/run_ruff.py format --check .` and
  `python utils/run_ruff.py check .`: **38 files already formatted; all lint
  checks passed**.
- `mypy src`: strict source typing, **18 source files**, no issues.
- `git diff --check -- clients/python`: clean.

README/CONTRIBUTING prose, new origin-root-relative error and resolver docstring
received the lead's main prose pass unchanged. The lead owns CHANGELOG facts.
No version files or retained old build artifacts were changed by this package.

Implementation is ready for implementer0's required hooked source commit. Same
independent reviewer affected-lane review and actual installed mounted
challenge/action/state acceptance must follow the committed intended changes;
no compiler or longer acceptance campaign was launched by implementer2.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
