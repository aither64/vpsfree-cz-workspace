# Rust HaveAPI generator and vpsAdmin client

## Accepted goal and scope

Implement the user-approved Rust generator and actual vpsadmin-rust-client.
Use Ruby/ERB in HaveAPI, embedding maintained runtime source in each generated
crate. Support async by default and optional sync via reqwest::blocking, sharing
models, builders, validation, auth and decoding. No public HaveAPI runtime crate.

Authoritative initial schema: unauthenticated OPTIONS at
https://api.vpsfree.cz/v7.0/, explicit API 7.0 / HaveAPI protocol 2.0.
Save sanitized schema, digest, inventory and provenance; generation must work
identically offline. Local fixtures must never add local-only API descriptions.
Only the API version determines server compatibility, never application release.

## Ownership and dependencies

Architect0 owns the frozen technical contract in [design.md](design.md).
The lead coordinates acceptance, tracking, shared edits and Git operations.

| Owner | Package | Acceptance and dependencies |
| --- | --- | --- |
| implementer0 | Embedded runtime and async/blocking adapters | After contract freeze; shared protocol/auth/errors and input-state fidelity |
| implementer1 | Ruby generator, templates, unit specs, HaveAPI tooling/docs | After contract freeze; deterministic fetch/generate/check, diagnostics, safe generated ownership |
| implementer2 | Protocol fixtures and integration harness | After contract freeze; async/blocking parity and real HaveAPI/vpsAdmin behavior fixtures |
| implementer3 | Actual new-client repo, production schema, examples, regeneration and CI | Capture first; generation follows runtime/generator; actual crate must compile/package/regenerate |
| reviewer0 | Independent final review | All intended changes committed and quick checks pass; all applicable review lanes/history |
| fresh utility watcher | Longer verification | After final review; required Nix builds, feature/MSRV checks, integration and package acceptance |

Each implementer owns source/tests/docs/checks/commits and follow-up fixes within
its boundary. HaveAPI index and Git operations are serialized by lead permission.
No default-branch integration or registry publication is authorized by implement.

## Public contract and defaults

Crate vpsadmin-client (vpsadmin_client), MIT, edition 2024, initial Rust 1.95
support floor, same pinned Nix toolchain as HaveAPI. Use rustls verified TLS.
Client actions use fluent builders ending send().await? or send()? and return
Result<Response<T,M>,Error>. Preserve omitted/null/value input states, optional
ordinary outputs, Custom JSON and partial associations. Support Basic, existing
HaveAPI/OAuth2 tokens and explicit request/challenge/renew/revoke token actions.
Blocking client construction/use/drop stays outside async execution.

Require explicit API version; reject mismatch and unknown schema rather than
fallback or drop fields. Preserve global auth paths and versioned resource paths.
Export API_VERSION/SCHEMA_SHA256. Crate SemVer is independent of API version.
No automatic mutation retries, paging/polling, token refresh or browser auth.
No server changes, database migration, node rollout or configuration deployment.
Recovery is pinning previous client/generated revision; it cannot undo API actions.
Runtime source fixes require regeneration/release of each affected client.

## Verification and documentation

Generated production client must include all supported captured fields/actions
without hand patches. Compile actual async/blocking library/examples, test
fixture HTTP behavior, deterministic offline generation and read-only --check,
formatting/lint, MSRV and crate packaging. Cover VPS show/partial update, paging,
null/omission/zero/false, Custom, associations, auth challenges/errors, version/path
failures, deadlines, credential redaction and redirects. Mutations only disposable;
public read-only live smoke supplements CI, never replaces fixture verification.

Commit completed deliverable and pass quick checks, then independent review of
all branches/history/migrations, then longer watcher-run checks. Resolve findings
through package owners. Publish feature branches; integration needs explicit
repository/target approval. Retain refs and leave session open.

Maintain lasting generation/runtime docs in HaveAPI, consumer usage/regeneration
and CI in vpsadmin-rust-client; apply writing skill before committing user prose.
Planning/state/review evidence remains in this session. Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-rust-client-generator/

## Accepted DELETE correction

Real-server acceptance showed that the initial DELETE query assumption differed
from HaveAPI and its Go client. [Design Clarification 5](design.md) controls:
GET uses query input; DELETE uses the common JSON body encoder with POST, PUT
and PATCH. Public Rust signatures, generated models and the API 7.0 snapshot
remain fixed. No fallback, replay or server compatibility mode was added.

The runtime, copied client, strict fixtures and docs were corrected, committed
and independently reviewed before fresh verification. Corrected runtime,
client, MSRV, package, generic root/mounted and actual disposable vpsAdmin
checks all passed. The public GET smoke was unaffected and was not repeated
solely for this classifier change. See [verification summary](verification-summary.md)
and [current state](state.md) for exact evidence. Final published-head CI also
passed in both repositories; default-branch integration awaits explicit approval.

## User-requested library README and Cargo publication

The user subsequently requested a library-user README inspired by
vpsadmin-go-client and publication using Cargo when finished. Refocus the README
on installation, public and authenticated usage, input setters, blocking calls
and library documentation. Keep generator/provenance details in their existing
maintenance documentation. Release `vpsadmin-client` 0.1.0 to crates.io after
the committed docs delta passes independent review and focused Cargo release
verification. Check credentials without exposing values. Registry publication
does not authorize merging either feature branch into its default branch.

The user prefers GitHub Actions and asked about trusted publishing for both
registries. Do not publish locally or request local Cargo login. Current
official crates.io guidance requires an API-token first upload before a trusted
publisher can be configured; that upload can itself run in Actions with a
one-time bootstrap secret. RubyGems supports a pending trusted publisher for a
new gem, including its first release. HaveAPI already uses RubyGems OIDC in its
release workflow; the Rust generator must be included in the maintained
artifact contract before that workflow can release it. Exact implementation
and one-time owner setup are being checked by architect0.


## Approved integration, releases held (2026-10-21)

The user explicitly requested merging the code into default branches and said
"no releases yet". Integrate HaveAPI into master and vpsadmin-rust-client into
main using the reviewed final series, after fresh remote checks. Use one short
repository claim per fast-forward, normal SSH push and remote proof; release
before CI monitoring and cleanup. No registry upload, tag, release dispatch,
secret configuration or token-file access is part of this action. The reported
RubyGems pending publisher is noted for future release work. Keep release work
deferred until fresh direction; integration does not authorize it.


## Client claim catalog boundary (2026-10-21)

HaveAPI default integration and all six default CI workflows completed at
e09142a. Client945 remains fully reviewed, published and CI-green, with mainb67
unchanged. The coordinator refused the new repository because its immutable
catalog omits it; no claim or client mutation occurred. Design Clarification8
records the exact two-entry source proposal and why current selected runtime
differs from shared workspace master. Do not deploy/revert/consume that other
source history merely to obtain this claim. Await an explicit one-off exception
to the claim rule for this exact new-repository merge, or separately authorized
workspace catalog/profile scope. Existing user approval for client/main merge
remains valid; no second merge approval is requested. Releases and token access
stay on hold.


## Client integration resumed (2026-10-22)

User requested another merge attempt after the coordinator update. Selected
packagef5h1qmr supports session-registered repositories without catalog entries.
The ordinary claim succeeded; all fresh identity/head/cleanliness/ancestry
guards passed. Fast-forward and normal SSH push merged client945af6a into
main, independently verified remotely, then claim62cb6ae8 was released.
No workspace configuration change, policy exception or runtime activation
was needed. Preserve the earlier catalog diagnosis as historical evidence.
Fresh default-branch CI39739951412 is monitored separately; no releases,
tags, credential access or publishing dispatch.
