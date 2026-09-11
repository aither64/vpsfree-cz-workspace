# Mandatory change review packet: final compatibility remediation

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

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..dc52d0d6039bf9d2006b7168eff8330f5eef4dc2`
  - `690ff7d`, `a1721f5`, `a44ec2b`, `b90fbcc`, `dc52d0d`.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..9f934d21893db97dfa5d5f340b1b1b5a59700f76`
  - `a695d7e`, `f36bd84`, `dbb617a`, `a1fc287`, `b52bd84`,
    `84894cd`, `96811a7`, `0820346`, `6da2030`, `9f934d2`.
- `vpsfree-cz-workspace`: `91b85b48b35cef51fd8920cd3445ca23a0023648..50de231f197ab6e27ce672f32dc27efff2382716`
  - `8747d05`, `50de231`.
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..f8619943a258f0941af08862a91209df707a5617`
  - `7122036f`, `f8619943`.

All feature worktrees are clean and local heads equal remote feature refs. The
exact dependency direction is:

`vpsfree-cz-workspace@50de231 -> dev-workspace@9f934d2 -> codex-web@dc52d0d`

Configuration `f8619943` pins `dev-workspace@9f934d2` and nested
`codex-web@dc52d0d`.

## Retained boundaries

- `codex-web@b90fbcc` owns the complete secured conversation integration,
  browser target/storage binding, canonical cross-language path domain, tests,
  module cleanup and Nix hash. `dc52d0d` owns documentation and the standalone
  loopback example.
- `dev-workspace@dbb617a` is the complete behavior-preserving dependency
  boundary: exact provider pin/checksum/hash, compatibility route, escaped-path
  preservation, shared browser storage, application ledger path, legacy API
  tests, and the existing 60+60-second nonblocking prompt policy. It passes all
  Go packages independently. Later commits do not repair this boundary.
- Profile, host substrate, generic portal labeling, workspace capability,
  deployment-default removal, documentation and mode catalog changes remain
  separate cohesive commits.
- Workspace and configuration each contain one owning downstream pin commit.
- Deployment to aitherdev is authorized. Release, default-branch integration,
  archive, delete and stop remain unauthorized.

## Security and compatibility contracts

- Submission-ledger schema 3, serialized keys, application-owned storage path,
  mode-0600 files, interprocess locking and rollback default are unchanged.
- Browser client target records are frozen and held only in a module-private
  `WeakMap`. Arbitrary clients must supply a semantically valid explicit target;
  falsy or non-string path values fail before durable storage is touched.
- Browser and Go opaque segments share one domain: valid Unicode, 1–256 UTF-8
  bytes, neither `.` nor `..`, slash-free and NUL-free, serialized exactly as
  JavaScript `encodeURIComponent`. Go parses `EscapedPath`, decodes once,
  requires valid UTF-8 and compares exact canonical reconstruction.
- Configured Go base paths use the browser-compatible ASCII path alphabet and
  reject values whose serialized request form cannot match.
- The portal validates untouched escaped legacy URLs before ServeMux can clean
  them. Slug and operation spellings must be canonical; opaque queue spelling
  is preserved in `RawPath` for the reusable handler. Malformed conversation
  and lifecycle paths return 404 before resolver or lifecycle dispatch.
- Old `/api/sessions/<slug>/...` conversation URLs remain during the rollback
  window. Only enumerated conversation operations are aliased; destructive
  workspace operations never enter the reusable handler.
- Persistent workspace, authority, journal, cluster, credential, PKI, socket
  and profile formats and paths are unchanged. Host substrate deploys before
  the user-profile application, whose previous tested Codex pair remains the
  rollback target.

## v7 findings reconciled

- Risk Blocking: falsy custom-client target fields counted as explicit but fell
  back to `/codex`. Default only on `undefined`; reject empty, null, false and
  numeric fields before storage, with no-call/no-write browser tests.
- General/Risk/Architecture Important: browser and Go differed on ID length and
  invalid UTF-8. Enforce the same 256-byte UTF-8 domain and test ASCII,
  multibyte, surrogate, `%FF`, literal percent and queue boundaries.
- General Important: Go accepted unroutable non-ASCII, whitespace and control
  base paths. Restrict the public base-path alphabet and test safe reserved
  punctuation plus rejected serialized forms.
- Architecture/Risk Important: the portal trimmed decoded legacy URLs and
  discarded `RawPath`. Parse the escaped URL before ServeMux cleaning, preserve
  opaque spelling when delegating and assert malformed read/mutation paths call
  neither conversation nor lifecycle code.
- Risk Important: retained dependency commit omitted the old nonblocking prompt
  expiry until a later commit. Move the explicit workspace policy and behavior
  test into `dbb617a`; `84894cd` no longer changes that file.
- Scope remained clean.

## Verification before v8

- `codex-web@dc52d0d`: complete race-enabled Go suite, Node browser contract and
  `nix flake check --print-build-logs` passed.
- `dev-workspace@dbb617a`: independent `go test -mod=mod -race ./...` passed.
- `dev-workspace@9f934d2`: complete portal `go test -race ./...` and
  `nix flake check --no-build --print-build-logs` passed.
- `vpsfree-cz-workspace@50de231`: no-build flake evaluation passed with the
  exact dependency tree before the history-only pin fold.
- `vpsfree-cz-configuration@f8619943`: the pin was generated only by
  `confctl inputs channel set --commit`; Nixfmt and commit hooks passed, and the
  final tree passed a no-build flake evaluation before its history-only fold.
- All worktrees are clean, remote refs match and object-range `git diff --check`
  passes.

Long package/configuration builds, live deployment, App Server exercise,
profile switch/rollback and empty-workspace checks remain after review.

## Review request

Risk remains high. Rerun General, Architecture/repetition, Scope/proportionality
and Risk/compatibility with `gpt-5.6-sol` at `xhigh`. Focus on each v7
remediation and exact retained boundary, then inspect all final trees for new
regressions. Report actionable findings as Blocking, Important or Advisory with
exact evidence, impact and remediation; explicitly report clean lanes.
