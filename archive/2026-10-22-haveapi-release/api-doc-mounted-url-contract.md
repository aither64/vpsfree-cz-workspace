# Mounted URL correction: bounded runtime contract

Design decision, 2026-10-22. Baseline `27b4f8f895a4e5401357a402187c2a4590699aec`
passed the earlier core/package checks, but installed rendered-example acceptance
exposed real mounted request failures. This document defines the corrective scope
before runtime edits. Architect writes design only; lead authorizes implementation.
No server route normalization, fixture simplification or new generator features.

## Evidence and ownership of the fault

Implementer1's [package1-mount-diagnosis.md](package1-mount-diagnosis.md) retains
the bounded Rack/native-client reproduction. Actual server OPTIONS at
`http://example.test/mount/v2/` publishes:

- Global token request: `/mount/_auth/token/tokens`.
- Ordinary nested action: `/mount/v2/parents/{parent_id}/children/{widget_id}`.
- With bound arguments: `/mount/v2/parents/7/children/name%20with%20space`.

The advertised token route returns HTTP 200 with the fixture's continuation
challenge. JS currently requests `/mount/mount/_auth/token/tokens` and receives
404. Python `parse_description` + actual `build_request` likewise duplicates
the mount for the ordinary action. Native callback resolution and the shared
async transport also demonstrate duplication. An AsyncClient.request call using
an already mounted descriptor path alone is not the regression assertion: that
public raw method has separate, deliberately preserved API-relative semantics.
The regression must exercise the described async action/authentication flow.

Authoritative source seams:

- `servers/ruby/lib/haveapi/server.rb`: `mount_version`, `mount_resource`,
  `version_prefix`, `auth_prefix`; version routes and global auth routes differ.
- `resource.rb:82` assigns the stored route to context.path;
  `context.rb:30` resolves arguments without removing the mount;
  `action.rb:245` publishes that resolved route as path.
- `clients/js/src/haveapi/protocol.ts:41` currently concatenates baseUrl + path;
  callback `client.ts#directInvoke` and async `request.ts#prepare` consume it.
- Python `_protocol/request.py#build_request` validates then separately prepends
  base.path to the bound descriptor path. `_resources/state.py` already separates
  discovery and action requests; `_transport.validate_destination` restricts
  same-origin destinations to the configured mount.

The server publishes its actual routes correctly. Fix consuming JS/Python URL
assembly, not server descriptors, generated examples or production mount settings.

## Frozen URL semantics

Configured base URL denotes API root, including the mount, without an API-version
suffix. Both trailing-slash forms continue to normalize as before. Example base:
`https://api.example/mount/` (origin is `https://api.example`).

| Input category | Input | Required URL |
| --- | --- | --- |
| Discovery, explicit version 2 | selected version, not descriptor | `https://api.example/mount/v2/` |
| Discovery default / version list | existing query path | `https://api.example/mount/?describe=default` / `?describe=versions` where supported |
| Advertised ordinary action | `/mount/v2/items/7` | `https://api.example/mount/v2/items/7` |
| Advertised global auth | `/mount/_auth/token/tokens` | `https://api.example/mount/_auth/token/tokens` |
| Advertised version-specific auth | `/mount/v2/_auth/token/tokens` | `https://api.example/mount/v2/_auth/token/tokens` |
| Public JS AsyncClient.request | `/v2/items/7` | `https://api.example/mount/v2/items/7` |

Descriptor paths are **origin-root-relative**, beginning with exactly one `/`.
Use the advertised path after existing path-parameter encoding; do not strip,
prepend, detect, infer or deduplicate mount/version components. Reject authority
switches and invalid path forms before transport/credential use under existing
security rules. This includes description-driven token request/continuation/
renew/revoke and action-state calls, not just ordinary resource actions.

Raw JS `AsyncClient.request` remains **API-base-relative** even when its path
begins with `/`; retain existing query handling, setup-free operation and public
RequestSpec. A raw caller must not pass a complete origin-root descriptor path
as though it were API-relative. No automatic prefix heuristic or fallback HTTP
retry is allowed: both conceal ambiguous paths and could duplicate mutations.

Discovery stays API-base-relative; selected version is applied only where the
existing discovery path builder applies it. Described action paths already carry
their routing/version decision. Shared auth must not acquire a guessed version.
No request-version header, server default-version change, route rewrite or new
version selection option is introduced. Keep callback version truthiness behavior
and all unrelated version handling outside this correction.

OAuth2 arbitrary URL handling is a separate existing facility. Preserve its
relative/absolute URL behavior and exact trusted-origin allowlist. Ordinary
descriptor paths must never inherit that cross-origin exception. Retain JS
credential/userinfo/control/backslash/authority rejection and Python traversal,
query/fragment, destination-origin and configured-mount restrictions. Do not
weaken Python's mount boundary to make an inconsistent schema pass.

## Minimal implementation interfaces

**JS:** keep `sameOriginUrl(path, {actionPath: true})` as the strict descriptor
path route, correcting its join to the origin. Add one internal discriminator
for the shared async pipeline: `RequestContext.pathMode?: 'api' | 'descriptor'`,
default `api`. Described resource/operation/auth requests pass `descriptor`;
public request/discovery/version-list requests use `api`. The shared resolver
may accept internal `UrlOptions.pathMode` to retain strict path validation while
selecting the base; no field is added to public RequestSpec. If not specified,
`actionPath:true` means descriptor and other URL calls keep existing behavior.
Auth description validation uses descriptor mode. Preserve snapshot/staleness,
auth transition and response handling; avoid new transport abstractions.

**Python:** no public raw request method needs changing. Extend the internal
resolver only as needed to distinguish base validation from descriptor binding
(e.g. keyword-only `path_mode='api'|'descriptor'`, existing default `api`).
`build_request` explicitly validates descriptor mode and constructs the bound
URL at origin root, not base.path + path. Preserve validation of static route
before substitution: encoded slash data within bound IDs must not be decoded
and reinterpreted as structural traversal. Leave discovery URL assembly and
normalize_base_url's empty-path validation unchanged. Keep destination validation
before auth headers, and cover both sync/async facades using the common core.

## Owner packages and file boundaries

| Owner | Exclusive correction files | Acceptance |
| --- | --- | --- |
| implementer1 | `clients/js/src/haveapi/protocol.ts`, callback client only as necessary, `async/{client,request,authentication,completion,resource,types}.ts` only where needed; existing/new JS path/auth/raw tests; JS documentation of URL semantics; dynamic rendered-acceptance diagnostics | One descriptor join policy, both callback/async actions and token flows reach the real mounted routes; raw/discovery/OAuth contracts unchanged; no speculative edits to unused listed files. |
| implementer2 | Python `_protocol/request.py`, relevant protocol/client tests and Python URL documentation; `_resources/state.py` only if necessary for existing flow | Actual mounted descriptions bind once for sync/async action/auth/state; security and encoded ID tests unchanged in strength; no new public request API. |
| implementer0 | All Git/index/hooks, shared test orchestration/docs wiring as requested; separately proven PHP launcher orphan fix | Serialize commits, preserve other owners' edits and final `Version 0.30.0` commit. PHP cleanup stops/reaps only its owned process/group and is independently testable; no URL semantics changes in PHP. |
| implementer3 | No runtime change assigned | Existing Go/Rust source/fixtures stay unchanged unless a concrete failure requires a separate bounded decision. |

Synthetic mocked descriptions which currently omit a configured mount are
inconsistent with real server output. Correct them to faithfully model actual
mounted descriptors and add captured real descriptor assertions. This is not
permission to mutate server-emitted paths in the real acceptance fixture.
Retain explicit raw-request API-relative tests so fixture corrections cannot
silently change that public behavior. Keep endpoint/path-case breadth intact.

## Checks and independent-review boundary

Quick before committing/review: focused native resolver/path tests plus callback
and async described invocation/auth tests; Python core tests and both mocked
facades; security URL tables; static type/style checks; bounded Rack descriptor
contract tests without listeners. Test `/`, `/mount/`, trailing-slash variants,
explicit/default discovery, version-list where supported, global/versioned token
routes, ordinary/nested action and state routes, IDs containing slash/space/percent,
existing raw query strings, same-origin OAuth and exact trusted external origins.
Reject malformed/external descriptor destinations before a request or credentials
are consumed. No route-presence-dependent fallback and no second attempted URL.

All intended correction and launcher changes must be committed and quick-green,
then the same independent reviewer performs an affected-lane final review of
the URL contract, implementation, changed fixture assumptions and full affected
base-to-head history. Include earlier `27b4f8f8` review/verification identity and
new final head; prior green CI does not validate this correction. Review must
explicitly assess raw-vs-described semantics, origin/credential safety, encoded
path binding, auth/state paths and compatibility below. Preserve final release
commit exactly `Version 0.30.0`; record any equivalence/history consolidation.

Only after that review, rerun installed-package rendered acceptance against the
real mounted fixture: JS callback/async, TS callback/async, Python sync/async;
actual token challenge/completion and authenticated ordinary actions must succeed
at the advertised URL without transformation. Capture attempted URL/method and
redacted status on failure. Run broader affected package checks as lead selects
through the watcher. Independently verify PHP launcher cleanup leaves no owned
listener/process after success/failure. Do not rerun unaffected Go/Rust solely
because URL design changed; follow exact-head verification obligations.

## Compatibility, deployment and recovery

No server/protocol/schema/database migration. New clients work with old and new
servers emitting the existing origin-root route contract. Root-mounted usage
is unchanged. Older affected clients retain the duplicate-mount bug against
mounted servers; do not contort server descriptions to make those clients work.
Deployment is updated npm/Python client packages only (and their existing browser
bundle as applicable), independently of server upgrades. Publication remains
separately authorized. Rollback restores previous packages and their known bug;
it reads no new persisted state and cannot undo API mutations already performed.

Applications manually fabricating/caching API-relative descriptor paths under
a mounted base must refresh from actual OPTIONS or use the actual origin-root
route. Call out this correction in release notes; do not add a legacy-path guess
mode. JS raw requests and OAuth URL options remain compatible. Default/versioned
server routing and generated-client schemas/imports remain unchanged.
