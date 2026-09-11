# Mandatory change review packet: reconciled final heads

## Outcome and scope

Implement the component split described in `plan.md` without integrating any
default branch:

- keep `vpsfree-cz-workspace` as policy, records, repository coordination and
  a thin package-selection flake;
- publish the reusable runtime in `dev-workspace` and reusable App Server
  conversation integration in `codex-web`;
- consume the reusable NixOS substrate from aitherdev while preserving names,
  addresses, credentials, TLS state, firewall and rollback paths;
- preserve authorities, session and thread identities, tracking files, cluster
  socket identities, profile generations and submission-ledger schema 3.

Non-goals are database, vpsAdmin API, node-daemon protocol, vpsAdminOS, release,
default-branch integration, session archival, deletion and session stopping.

## Exact repositories and ranges

- `codex-web`
  - base: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8`
  - head: `2c2d2e129bd1e162ae593228d5b59fba5b8e18bf`
  - commits: `690ff7d`, `a1721f5`, `a44ec2b`, `b892779`, `2c2d2e1`.
- `dev-workspace`
  - base: `f39f8e62097b5e9da9de8a5eb678131b1e478e35`
  - head: `70228561be446652dcca0bbf1dce7e8000ff976c`
  - commits: `a695d7e`, `f36bd84`, `9ce1cec`, `7bf1809`, `5b6023f`,
    `917cd3f`, `0718736`, `2f6a997`, `f7610ad`, `7022856`.
- `vpsfree-cz-workspace`
  - base: `91b85b48b35cef51fd8920cd3445ca23a0023648`
  - head: `b7f23e0880966418a4460383316b0c397a4038db`
  - commits: `c6df767`, `b7f23e0`.
- `vpsfree-cz-configuration`
  - base: `7481618dacab04bfd5b09bc730c373c2d2bf14d7`
  - head: `841b5c4b873a181fc898bf8356ace8f183ab9522`
  - commits: `4bda8cc7`, `841b5c4b`.

All four worktrees are clean and every local feature head equals its remote
feature head. The exact dependency direction is:

`vpsfree-cz-workspace@b7f23e0 -> dev-workspace@7022856 -> codex-web@2c2d2e1`

The configuration channel also pins `dev-workspace@7022856`, including nested
`codex-web@2c2d2e1`.

## Retained history and ownership boundaries

- `codex-web` separates client relocation, application policy, durable ledger
  protocol, secured conversation integration and the standalone example. Its
  Nix hash and module dependency cleanup live with conversation integration,
  where the final package surface is established.
- `dev-workspace` commit `9ce1cec` is the complete conversation dependency
  boundary. It installs the exact shared client and handler, short durable
  transactions, shared browser storage, the old compatibility path and route
  alias, real shipped-client tests, an explicitly owned compatibility ledger
  path and final vendor hash. That boundary passes all Go packages on its own.
- Profile ownership, host substrate, portal policy, workspace capabilities,
  generic defaults, documentation and dynamic mode rendering remain separate
  later commits. No retained commit relies on a corrective follow-up to restore
  a deployed API or safety protocol.
- Downstream histories contain one owning pin/input commit each, not a chain of
  pin corrections.
- The user authorized aitherdev deployment, but not release, default-branch
  integration, archival, deletion or stopping this session.

## Compatibility and security decisions

- Submission-ledger schema 3 and the serialized `retirements` key are unchanged.
  Transactions use one lock/reload/mutate/save helper and release their mode-0600
  lock on every path. `ClientOptions.SubmissionLedgerPath` lets the embedding
  application own durable storage independently of its socket directory; empty
  retains the exact socket-derived compatibility path, and cooperating clients
  must choose the same identity.
- Browser clients retain immutable effective endpoint metadata. Durable senders
  consume that metadata automatically and reject a conflicting override. An
  arbitrary client must supply a base path, conversation path or durable
  namespace before durable sending is enabled.
- Browser paths are parsed against a fixed same-origin base, returned in
  canonical form and joined without scheme-relative `//`. Root base and
  conversation paths have matching client/server semantics. Control, query,
  fragment, encoded, dot-segment, repeated-separator and backslash forms fail
  closed. Default retry keys derive from the canonical effective endpoint;
  explicit namespaces allow deliberate compatibility aliases.
- The portal emits its old `/api/sessions/<slug>/...` conversation routes from
  the first dependency commit. The server aliases only the enumerated
  conversation operations to `/codex/conversations/<slug>/...`; workspace
  lifecycle operations never enter the reusable handler. Removal criteria are
  documented against every retained rollback generation and open browser tab.
- Catalog-driven mode controls contain no hard-coded mode names. The shared
  conversation client and durable store are exercised from the exact served
  module, not copied test fakes.
- The standalone example accepts only loopback listen addresses and origins,
  sends `frame-ancestors 'none'`, `X-Frame-Options: DENY` and `nosniff`, and
  documents that remote embedding requires application authentication.
- Package transitions preserve current schemas and state paths, verify the
  dispatcher generation after the transition lock, retain compatibility
  tombstones for every rollback generation and fail closed on pre-contract or
  ambiguous cluster state.
- Deploy the host substrate first and the user-profile application second.
  Existing credential, PKI, certificate, socket, hostname, listener, group,
  firewall and public-CA paths remain unchanged. The preceding application and
  Codex pair remains selectable for live rollback.

## v5 findings and remediation

- General Blocking: dependency commit temporarily moved production requests to
  the new route and only a later commit restored rollback compatibility. Folded
  the alias, old browser path, shared storage and all associated tests into
  `9ce1cec`; tested that exact boundary independently.
- Risk Blocking: a custom client and durable sender could derive different
  endpoints. Bound immutable target metadata to exported clients, consume it in
  sender and mount paths, reject conflicts and require explicit targets for
  arbitrary clients. Tests cover direct composition and mounting without
  redundant path options.
- Architecture Important: ledger storage was forced beside the Unix socket.
  Added application-owned storage with the old default, a split-permission test
  and explicit vpsFree selection of the old identity.
- General Important: root, dot-segment and backslash paths could escape or split
  request and storage identity. Added canonical path validation, root-safe
  joining, matching Go root semantics and client/server regressions.
- General Advisory: removed six unused Go module dependencies and updated the
  exact Nix vendor hashes.
- Risk Advisory: restricted the privileged example to loopback, added
  anti-framing/security headers and documented its authentication boundary.
- Scope reported no finding.

## Verification before this rerun

- `codex-web`: browser contracts and the race-enabled complete Go suite passed.
  After investigating exact-head CI run `34433947701`, updated its deterministic
  Nix vendor hash and passed `nix flake check --print-build-logs` at exact head
  `2c2d2e1`.
- `dev-workspace`: the race-enabled complete portal suite passed at exact head
  `7022856`. Every Go package also passed independently at the rewritten
  exact dependency boundary `9ce1cec`.
- `vpsfree-cz-workspace`: `nix flake check --no-build --show-trace` passed at
  exact head `b7f23e0` and its complete final dependency tree.
- `vpsfree-cz-configuration`: its generated `confctl` input update passed Nixfmt
  and commit hooks; `nix flake check --no-build --show-trace` passed at exact
  head `841b5c4b`.
- All implementation worktrees are clean, all remote feature refs match and
  `git diff --check` passes.

Long final package/configuration builds, deployment, live App Server exercises,
profile switch/rollback and empty-workspace compatibility remain intentionally
after this review rerun.

## Review lanes and risk

Overall risk remains high. Rerun General, Architecture and repetition, Scope
and proportionality, and Risk and compatibility with `gpt-5.6-sol` at `xhigh`.
Inspect every retained commit boundary and final tree, verify each v5 finding
against the exact heads above, and report any new issue introduced by the
remediation.
