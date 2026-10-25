# Installed dynamic acceptance: mounted action URL diagnosis

Owner: implementer1. Read-only followup to the first dynamic wheel acceptance
failure at `27b4f8f895a4e5401357a402187c2a4590699aec`. Lead reconciled the failed
batch's processes before the known-quick reproduction below. No listener,
acceptance rerun, source edit, Git mutation or client capability change occurred.

## Confirmed evidence

- `api-doc-verification.log`: full core tests/build/package smokes reached the
  installed wheel dynamic run; the first failure is
  `auth-token-javascript-callback`, with `Discovery or authentication failed`.
- `api-doc-acceptance-results/dynamic-wheel/example-12.mjs`: actual extracted
  callback source uses mounted base `/mount/`, exact version `2`, advertised
  login fields and the real continuation callback contract. The existing-token
  execution succeeded; the harness failed on the second execution with that
  environment value absent.
- `fixture.log` is empty. The harness asserts challenge completion before
  writing `example-12.log`; it never persists separate challenge output.
- Known-quick tools-only Nix reproduction used `Rack::MockRequest` with the real
  `DynamicDocumentationAPI.build.app` and the committed built callback package.
  No listening socket or transport retry was started.

| Operation | Result |
| --- | --- |
| Real fixture `OPTIONS /mount/v2/` | HTTP 200 |
| Advertised token request action path | `/mount/_auth/token/tokens` |
| Actual callback join with base `http://example.test/mount/` | `http://example.test/mount/mount/_auth/token/tokens` |
| Rack POST to actual joined path | HTTP 404 |
| Rack POST to advertised route with valid fixture input | HTTP 200, incomplete challenge with next action `verify` |

The immediate cause is the duplicate mount in the requested URL, before the
fixture's challenge handler. `Server#mount_resource`, `Resource.describe` and
`Context#resolved_path` retain the actual mounted path in the descriptor;
JavaScript `resolveApiUrl` appends that action path to the complete configured
base URL. Python `resolve_url` also appends action paths to the base path by
source inspection; its effect has not been separately executed here. This
boundary affects described actions generally, rather than only authentication.

## Proposed scope, awaiting lead/design direction

Do not normalize the fixture's schema or routes to conceal real mounted server
behavior. Settle the descriptor/base resolution contract before choosing a
runtime or general server fix. Existing auth and client capabilities need no
expansion to explain this failure.

The owner's smallest harness improvement is to persist ordinary and challenge
subprocess output before checking completion, and capture fixture request
method/path/status traces excluding credentials, headers, query and body.
That would preserve the actual failing route and useful output on this failure
and similar failures. Long execution remains lead/watcher-owned after approved
changes, quick checks, commits and any affected-lane review.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/

## Additional executed native seams

A second known-quick, pure reproduction used authenticated real OPTIONS output
and confirmed the ordinary action descriptor
`/mount/v2/parents/{parent_id}/children/{widget_id}`. Bound path arguments were
`7` and `name with space`. Actual committed callback resolution and actual async
request preparation (existing mocked-XHR helper) both requested
`http://example.test/mount/mount/v2/parents/7/children/name%20with%20space`.
Actual Python `parse_description`/`lookup_action`/`build_request` with that same
real envelope and base URL also produced the same duplicated mount. No network
transport, listener or mounted-schema rewriting was involved. These results and
owning source seams were sent directly to architect0, who owns the contract fix.

Lead then authorized diagnostics only. Authored delta saves subprocess output
before exit-status validation and before completion assertions, gives token
challenge output its own `example-N-challenge.log`, and wraps the fixture with a
method/PATH_INFO/status trace. It excludes headers, query strings and bodies;
real routes and descriptors remain unchanged. Focused real-Rack/subprocess
regressions passed **5 examples, 0 failures**, seed 10533, 1.88 seconds. Lead
completed source inspection and main prose approval. Final style correction,
serialized commit and affected-lane review remain pending at this checkpoint.

Diagnostics source yield: final RuboCop passed all three changed Ruby files
without offenses after alignment-only correction; `git diff --check` passed.
Exact four paths (`dynamic_acceptance.rb`, `dynamic_acceptance_spec.rb`,
`dynamic_documentation_api.rb`, `dynamic_acceptance.md`) were supplied to
implementer0 for the required hooked commit. Lead source/prose approval is
complete. No operation/source write remains active; runtime changes await the
architect's recorded brief and lead execution assignment.

Diagnostics committed by implementer0 as `164a15e4` with required hooks passing;
all four diagnostics source paths are clean and the index is empty. The mounted
URL contract is now recorded by architect0 in
[api-doc-mounted-url-contract.md](api-doc-mounted-url-contract.md). Its important
qualification is retained: the earlier raw async `request` receipt demonstrated
the shared preparation seam only. Raw requests intentionally remain API-relative;
the corrective regression must exercise described async invocation/auth. Runtime
edits still await the lead's bounded execution grant.
