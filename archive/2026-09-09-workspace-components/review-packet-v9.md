# Mandatory change review packet: canonical request remediation

## Outcome and scope

Implement the planned component split without integrating any default branch:

- `vpsfree-cz-workspace` retains policy, records and repository coordination;
- `dev-workspace` publishes the reusable runtime and vpsFree package variant;
- `codex-web` publishes the reusable App Server client and conversation layer;
- aitherdev consumes the reusable host substrate without changing existing
  names, addresses, credentials, TLS state, firewall or rollback paths.

Preserve authorities, sessions, threads, tracking files, development-cluster
socket identities, profile generations and submission-ledger schema 3.
Database, vpsAdmin API, node protocol, vpsAdminOS, release, default-branch
integration, archive, delete and session stop are outside scope.

## Exact repositories and ranges

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..a46ccd2c4bffc764aee916fafdc79b5b9fe60998`
  - `690ff7d`, `a1721f5`, `a44ec2b`, `abe91d0`, `a46ccd2`.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..014092dc25c4228b7061e3357c8d46393d636459`
  - `a695d7e`, `f36bd84`, `6a1fd10`, `e7d35c0`, `cf7a319`,
    `64702a2`, `5414b0b`, `dd8408b`, `4145bc2`, `014092d`.
- `vpsfree-cz-workspace`: `91b85b48b35cef51fd8920cd3445ca23a0023648..3fb1eab283fbf816742f6b8f506c7dd0c20edc2a`
  - `7b62f3b`, `3fb1eab`.
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..0c6447ae4266b4aef36fc06477d21ac88c602253`
  - `69af96b`, `0c6447a`.

All feature worktrees are clean and local heads equal remote feature refs. The
exact dependency direction is:

`vpsfree-cz-workspace@3fb1eab -> dev-workspace@014092d -> codex-web@a46ccd2`

Configuration `0c6447a` pins `dev-workspace@014092d` and nested
`codex-web@a46ccd2`.

## Retained boundaries

- `codex-web@abe91d0` owns the complete secured conversation integration,
  browser target/storage binding, canonical cross-language path domain, tests,
  module cleanup and Nix hash. `a46ccd2` owns documentation and the standalone
  loopback example.
- `dev-workspace@6a1fd10` is the complete behavior-preserving dependency
  boundary: exact provider pin/checksum/hash, compatibility route, escaped-path
  preservation, shared browser storage, application ledger path, legacy API
  tests, and the existing 60+60-second nonblocking prompt policy. It passes all
  Go packages independently. Later commits do not repair this boundary.
- Profile ownership, host substrate, generic portal presentation, workspace
  capability, deployment-default removal, documentation and mode catalog
  changes remain separate cohesive commits.
- Workspace and configuration each contain one owning downstream pin commit.
- Deployment to aitherdev is authorized. Release, default-branch integration,
  archive, delete and stop remain unauthorized.

## Security and compatibility contracts

- Submission-ledger schema 3, serialized keys, application-owned storage path,
  mode-0600 files, interprocess locking and rollback default are unchanged.
- Browser client target records are frozen and held only in a module-private
  `WeakMap`. Arbitrary clients must supply a semantically valid explicit target;
  falsy or non-string path values fail before durable storage is touched.
- Browser and Go opaque identifiers share one validator domain: valid Unicode,
  1–256 UTF-8 bytes, neither `.` nor `..`, slash-free and NUL-free. Queue start
  and deletion use the same domain and never trim identity-significant
  whitespace. Path segments serialize exactly as JavaScript
  `encodeURIComponent`.
- Browser paths and configured Go base paths use the identical explicit ASCII
  alphabet. Printable-ASCII table tests enforce parity, including rejection of
  brackets and the vertical bar.
- Before route parsing, the reusable handler and the portal's pre-ServeMux
  legacy guard reject every nonempty `RawPath` that differs from `EscapedPath`.
  This prevents Go from reconstructing canonical escapes from raw Unicode or
  raw browser-escaped punctuation before exact spelling checks. Canonical
  encoded Unicode and encodeURIComponent-safe literal characters remain valid.
- Old `/api/sessions/<slug>/...` conversation URLs remain during the rollback
  window. Only enumerated conversation operations are aliased; destructive
  workspace operations never enter the reusable handler.
- Persistent workspace, authority, journal, cluster, credential, PKI, socket
  and profile formats and paths are unchanged. Host substrate deploys before
  the user-profile application, whose previous tested Codex pair remains the
  rollback target.

## v8 findings reconciled

- General Important: queue start accepted IDs outside the shared opaque domain
  and trimmed whitespace server-side. The browser now validates before fetch;
  Go start, delete and conversation routing share `validOpaqueID`; tests cover
  invalid values, no-call behavior, exact whitespace and multibyte boundaries.
- General Important: browser paths accepted `[`, `]` and `|` while Go rejected
  them. Both implementations now use the same explicit alphabet and exhaustively
  test every printable ASCII character.
- Risk Important: Go `EscapedPath()` could hide noncanonical raw Unicode and
  punctuation. Both routing layers now reject mismatched nonempty `RawPath`
  before resolver, conversation or lifecycle dispatch; direct and legacy route
  tests cover conversation and queue spellings.
- Architecture Advisory: retained commit text attributed the 60+60-second
  nonblocking prompt policy to the later presentation commit. The dependency
  commit now records preservation and its behavioral test; the later commit is
  accurately named `portal: make workspace presentation configurable`.
- Scope/proportionality was clean.

## Verification before v9

- `codex-web@a46ccd2`: complete race-enabled Go suite and Node browser contract
  passed; the final flake evaluates with `nix flake check --no-build`.
- `dev-workspace@6a1fd10`: independent `go test -mod=mod -race ./...` passed.
- `dev-workspace@014092d`: complete portal `go test -race ./...` passed and all
  package, host-module and app outputs evaluate with a no-build flake check.
- `vpsfree-cz-workspace@3fb1eab`: all delegated package and app outputs evaluate
  with the exact dependency tree.
- `vpsfree-cz-configuration@0c6447a`: the pin was generated only through
  `confctl inputs channel set --commit`; Nixfmt and commit hooks passed, the pin
  was folded into its owning input commit, and the final flake evaluates.
- All worktrees are clean, remote refs match and object-range `git diff --check`
  passes.

Long package/configuration builds, live deployment, App Server exercise,
profile switch/rollback and empty-workspace checks remain after review.

## Review request

Risk remains high. Rerun General, Architecture/repetition, Scope/proportionality
and Risk/compatibility with `gpt-5.6-sol` at `xhigh`. Focus on the v8 fixes,
their retained commit boundaries and exact downstream pins, then inspect all
final trees for regressions. Report actionable findings as Blocking, Important
or Advisory with exact evidence, impact and remediation; explicitly report
clean lanes.
