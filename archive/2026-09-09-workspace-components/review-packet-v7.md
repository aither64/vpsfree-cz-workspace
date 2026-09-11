# Mandatory change review packet: URL identity remediation

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
  - head: `94977e90054000641a91c8358ba87a26d58a4e0b`
  - commits: `690ff7d`, `a1721f5`, `a44ec2b`, `327f563`, `94977e9`.
- `dev-workspace`
  - base: `f39f8e62097b5e9da9de8a5eb678131b1e478e35`
  - head: `d880db6cf7e85730b468d9ee357d8cfec7ed777c`
  - commits: `a695d7e`, `f36bd84`, `a933f6b`, `303555d`, `46ad7b8`,
    `ea5c97b`, `477483e`, `dc3a976`, `c246b6f`, `d880db6`.
- `vpsfree-cz-workspace`
  - base: `91b85b48b35cef51fd8920cd3445ca23a0023648`
  - head: `db2c24aca7303e80e2a0c02675d86bf71cae1bb4`
  - commits: `4f236bc`, `db2c24a`.
- `vpsfree-cz-configuration`
  - base: `7481618dacab04bfd5b09bc730c373c2d2bf14d7`
  - head: `2e6f55ebb3a188ca676c632126923e84222b596d`
  - commits: `137806c0`, `2e6f55eb`.

All four worktrees are clean and every local feature head equals its remote
feature head. The exact dependency direction is:

`vpsfree-cz-workspace@db2c24a -> dev-workspace@d880db6 -> codex-web@94977e9`

The configuration channel also pins `dev-workspace@d880db6`, including nested
`codex-web@94977e9`.

## Retained history and ownership boundaries

- `codex-web` separates client relocation, application policy, durable ledger
  protocol, secured conversation integration and the standalone example. The
  conversation commit owns its module cleanup, Nix vendor hash, private browser
  target identity, URL parsing and path contract tests.
- `dev-workspace` commit `a933f6b` is the complete conversation dependency
  boundary. It installs the exact shared client and handler, short durable
  transactions, shared browser storage, old compatibility path and route alias,
  real shipped-client tests, application-owned ledger path and final vendor
  hash. No later commit repairs that boundary.
- Profile ownership, host substrate, portal policy, workspace capabilities,
  generic defaults, documentation and dynamic mode rendering remain separate
  later commits.
- Downstream histories contain one owning pin/input commit each, not a chain of
  corrective dependency updates.
- The user authorized aitherdev deployment, but not release, default-branch
  integration, archival, deletion or stopping this session.

## Compatibility and security decisions

- Submission-ledger schema 3 and the serialized `retirements` key are unchanged.
  Transactions use one lock/reload/mutate/save helper and release their mode-0600
  lock on every path. `ClientOptions.SubmissionLedgerPath` lets an embedding
  application own durable storage independently of its socket directory; empty
  retains the exact socket-derived compatibility path.
- Browser client target metadata lives only in a module-private `WeakMap`; its
  value is frozen. Exported client reflection cannot discover or mutate the
  effective endpoint independently of a durable sender. Arbitrary clients must
  still provide an explicit durable target.
- Browser paths are validated before normalization. Control, query, fragment,
  percent-encoded path syntax, backslash, dot-segment and repeated-separator
  forms fail closed, while one trailing slash is normalized deliberately.
- Conversation and queue identifiers are encoded by `encodeURIComponent` in
  the browser. The Go handler parses `URL.EscapedPath()`, decodes each opaque
  segment once, reconstructs the JavaScript encoding and requires an exact
  match. Literal percent-sequence IDs remain distinct from the characters they
  resemble; dot IDs and route aliases are rejected before target mutation.
- Default retry keys derive from the canonical effective endpoint. Explicit
  namespaces allow deliberate compatibility aliases only when the embedding
  application opts into one.
- The portal emits its old `/api/sessions/<slug>/...` conversation routes from
  the first dependency commit. The server aliases only enumerated conversation
  operations to `/codex/conversations/<slug>/...`; workspace lifecycle
  operations never enter the reusable handler.
- Catalog-driven mode controls contain no hard-coded mode names. The standalone
  example remains loopback-only with anti-framing headers and documents its
  authentication boundary.
- Package transitions preserve current schemas and state paths, verify the
  dispatcher generation after the transition lock, retain compatibility
  tombstones and fail closed on pre-contract or ambiguous cluster state.
- Deploy the host substrate first and user-profile application second. Existing
  credential, PKI, certificate, socket, hostname, listener, group, firewall and
  public-CA paths remain unchanged. The preceding application and Codex pair
  remains selectable for rollback.

## v6 findings and remediation

- Architecture Blocking and Risk Blocking: exported clients stored target
  metadata in a discoverable Symbol whose object could be mutated, detaching
  the request endpoint from an existing durable key. Replaced it with a
  module-private `WeakMap`, froze the target value and added reflection
  regressions.
- General Important and Risk Blocking: Go decoded browser-encoded conversation
  and queue identifiers twice, so `%41` could alias `A` and literal percent IDs
  could fail. Parse escaped paths and decode individual segments exactly once;
  require the exact JavaScript encoding. Added resolution and deletion tests for
  literal `%`, `%41`, `%2F`, `%2e%2e`, Unicode and direct noncanonical escapes.
- General Important and Risk Important: browser and handler path validation
  admitted repeated separators, normalized terminal dot segments and trailing
  aliases. Validate the original browser syntax, reject dot IDs, stop trimming
  server paths and test leading, interior and trailing aliases.
- Scope reported no finding.

## Verification before this rerun

- `codex-web@94977e9`: Node browser contract passed; complete race-enabled Go
  suite passed; `nix flake check --print-build-logs` passed.
- `dev-workspace@d880db6`: complete race-enabled portal Go suite passed;
  `nix flake check --no-build --print-build-logs` passed with exact source,
  module checksums and vendor hash.
- `vpsfree-cz-workspace@db2c24a`: `nix flake check --no-build
  --print-build-logs` passed with the exact downstream tree.
- `vpsfree-cz-configuration@2e6f55eb`: `confctl inputs channel set --commit`
  produced the only input change, Nixfmt and commit hooks passed, and
  `nix flake check --no-build --print-build-logs` passed.
- All implementation worktrees are clean, all remote feature refs match and
  `git diff --check` passes.

Long final package/configuration builds, deployment, live App Server exercises,
profile switch/rollback and empty-workspace compatibility remain intentionally
after this review rerun.

## Review lanes and risk

Overall risk remains high. Rerun General, Architecture and repetition, Scope
and proportionality, and Risk and compatibility with `gpt-5.6-sol` at `xhigh`.
Inspect every retained commit boundary and final tree, verify each v6 finding
against the exact heads above, and report any new issue introduced by the
remediation.
