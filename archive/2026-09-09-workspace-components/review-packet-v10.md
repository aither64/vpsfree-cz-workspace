# Mandatory change review packet: shared path contract closure

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

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  - `690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..d09221bbbcac0aeb8fdb38ddf4b3ae91ca75e6fe`
  - `a695d7e`, `f36bd84`, `379ce5c`, `f7de3f8`, `90a974f`,
    `edb80eb`, `407e0a1`, `5ee3dd6`, `90b839c`, `d09221b`.
- `vpsfree-cz-workspace`: `91b85b48b35cef51fd8920cd3445ca23a0023648..e37479126ad592ae0169ea2848e731d3bee00772`
  - `3b6eaaf`, `e374791`.
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..d6331b2594d35598f692b19a7aa9eddbe7cd7655`
  - `5037ac6`, `d6331b2`.

All feature worktrees are clean and local heads equal remote feature refs. The
exact dependency direction is:

`vpsfree-cz-workspace@e374791 -> dev-workspace@d09221b -> codex-web@e8655b7`

Configuration `d6331b2` pins `dev-workspace@d09221b` and nested
`codex-web@e8655b7`.

## Retained boundaries

- `codex-web@994b636` owns the complete secured conversation integration,
  browser target/storage binding, machine-readable shared path contract, tests,
  module cleanup and Nix hash. `e8655b7` owns documentation and the standalone
  loopback example.
- `dev-workspace@379ce5c` is the complete behavior-preserving dependency
  boundary: exact provider pin/checksum/hash, bounded compatibility route,
  escaped-path preservation, shared browser storage, application ledger path,
  legacy API tests, and the existing 60+60-second nonblocking prompt policy.
  It passes all Go packages independently with the cache disabled. Later
  commits do not repair this boundary.
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
- `conversation/testdata/path_contract.json` is the provider-owned parity
  oracle consumed by both Go and Node tests. It defines the common base-path
  alphabet and valid, invalid, encoded, Unicode, whitespace and byte-boundary
  opaque-ID cases, including platform representations of invalid Unicode.
- Browser and Go opaque identifiers use one domain: valid Unicode, 1–256 UTF-8
  bytes, neither `.` nor `..`, slash-free and NUL-free. Queue start and deletion
  share it and never trim identity-significant whitespace. Path segments
  serialize exactly as JavaScript `encodeURIComponent`.
- `queue/start` is method-disambiguated: POST starts the selected entry, while
  DELETE removes the valid opaque queue ID `start`. Direct and legacy browser
  tests assert both downstream operations.
- Before route parsing, the reusable handler and portal legacy guard reject a
  nonempty `RawPath` that differs from `EscapedPath`. Decoded paths are quoted
  in logs so accepted control characters cannot inject log lines.
- The bounded legacy adapter includes the reusable read operations used by the
  compatibility browser, including models and collaboration modes. Destructive
  workspace operations never enter the conversation handler.
- Persistent workspace, authority, journal, cluster, credential, PKI, socket
  and profile formats and paths are unchanged. Host substrate deploys before
  the user-profile application, whose previous tested Codex pair remains the
  rollback target.

## v9 findings and post-review validation reconciled

- General/Risk Important: valid queue ID `start` could not be deleted because
  the route was reserved for POST start. Dispatch is now method-aware, the
  special rejection is removed, and direct plus legacy browser tests prove the
  exact delete/start calls.
- Architecture Important: browser and Go path validation duplicated their
  contract and tests without a shared parity oracle. Both suites now consume a
  single machine-readable provider fixture for every printable base-path byte
  and representative opaque-ID cases.
- Risk Advisory: accepted control characters could inject lines through decoded
  path logging. Logs now quote the path, with a canonical `%0A` regression.
- Scope/proportionality was clean.
- The first uncached test of the exact rewritten dependency commit found that
  the compatibility browser's collaboration-mode request lacked a bounded
  legacy GET alias. The adapter now enumerates `models` and
  `collaboration-modes`; the exact dependency commit passes with `-count=1`, the
  race detector and Node present. This also prevents Go's test cache from
  hiding changes to the external browser script.

## Verification before v10

- `codex-web@e8655b7`: every Go package passed uncached with the race detector;
  the Node browser contract and final no-build flake evaluation passed.
- `dev-workspace@379ce5c`: every portal Go package passed independently with
  `-count=1 -mod=mod -race` and Node available.
- `dev-workspace@d09221b`: the same uncached race-enabled suite passed before
  history folding, and all package, host-module and app outputs evaluate.
- `vpsfree-cz-workspace@e374791`: all delegated package/app outputs evaluate
  with the exact dependency tree.
- `vpsfree-cz-configuration@d6331b2`: each input revision was generated only
  through `confctl inputs channel set --commit`; Nixfmt and commit hooks passed,
  the pin is folded into the owning input commit, and the final flake evaluates.
- All worktrees are clean, remote refs match and object-range `git diff --check`
  passes.

Long package/configuration builds, live deployment, App Server exercise,
profile switch/rollback and empty-workspace checks remain after review.

## Review request

Risk remains high. Rerun General, Architecture/repetition, Scope/proportionality
and Risk/compatibility with `gpt-5.6-sol` at `xhigh`. Focus on the shared fixture,
method-disambiguated `start` ID, quoted logging, complete bounded legacy GET
surface, retained dependency boundary and exact downstream pins. Inspect all
final trees for regressions. Report actionable findings as Blocking, Important
or Advisory with exact evidence, impact and remediation; explicitly report
clean lanes.
