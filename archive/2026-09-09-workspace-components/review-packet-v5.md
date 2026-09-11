# Mandatory change review packet: exact final heads

## Outcome and scope

Implement the component split described in `plan.md` without integrating any
default branch:

- keep `vpsfree-cz-workspace` as policy, records, repository coordination, and
  a thin package-selection flake;
- publish the reusable runtime in `dev-workspace` and the reusable App Server
  conversation integration in `codex-web`;
- consume the reusable NixOS substrate from aitherdev while preserving its
  names, addresses, credentials, TLS state, firewall, and rollback path;
- preserve runtime authorities, session and thread identities, tracking files,
  cluster socket identities, profile generations, and submission-ledger schema
  3 across the staged cutover.

Non-goals are database, vpsAdmin API, node-daemon protocol, vpsAdminOS, release,
default-branch integration, session archival, deletion, and session stopping.

## Exact repositories and ranges

- `codex-web`
  - base: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8`
  - head: `a59181e0802b0eebee89e09afdce55199666d149`
  - commits:
    `690ff7d`, `a1721f5`, `7a58c0a`, `8f77fc9`, `a59181e`.
- `dev-workspace`
  - base: `f39f8e62097b5e9da9de8a5eb678131b1e478e35`
  - head: `9ea5d2769130549ed55477f43652789cc59df8af`
  - commits:
    `a695d7e`, `f36bd84`, `0d85ebb`, `1766fef`, `597fb03`, `7d4fc7e`,
    `ed80fac`, `22635e7`, `7082ec1`, `0e68baf`, `8945304`, `9ea5d27`.
- `vpsfree-cz-workspace`
  - base: `91b85b48b35cef51fd8920cd3445ca23a0023648`
  - head: `8a769cb2a15ce31817ff290d239e4dbb571e5571`
  - commits: `fa8438a`, `8a769cb`.
- `vpsfree-cz-configuration`
  - base: `7481618dacab04bfd5b09bc730c373c2d2bf14d7`
  - head: `b3b6c2062aec2ea5b893605480fcfa53c1a84655`
  - commits: `67dea2e3`, `b3b6c206`.

All four worktrees are clean and each local feature head equals its remote
feature head. The dependency pins are exact and one-way:

`vpsfree-cz-workspace@8a769cb -> dev-workspace@9ea5d27 -> codex-web@a59181e`

The configuration channel also pins `dev-workspace@9ea5d27`, whose nested
source is `codex-web@a59181e`.

## Commit structure and bounded decisions

- Reusable APIs, packaging, host ownership, portal policy, workspace
  capabilities, downstream selection and configuration adoption are separate
  commits where each can build and be reviewed meaningfully.
- The exact `codex-web` source and vendor hash are part of the original
  `dev-workspace` dependency commit. The workspace and configuration histories
  contain no repeated pin-only correction commits.
- No commit installs a lifetime-held submission-ledger lock. The first commit
  that owns ledger mutations contains the short transaction helper used by all
  callers and its failure-path tests.
- Rejected alternatives remain a separate App Server proxy, browser-selected
  sockets/threads/directories, two durable browser-store implementations,
  lifetime-exclusive ledger ownership, generic prompt auto-answering, and
  merging configuration merely to deploy.
- The user authorized deployment to aitherdev. They did not authorize release,
  default-branch integration, archival, deletion, or stopping this session.

## Compatibility, security and deployment decisions

- The reusable Codex client accepts explicit identity, runtime roots, source
  kinds, developer instructions and optional nonblocking prompt policy. Generic
  consumers do not auto-answer prompts.
- Submission-ledger schema 3 and the serialized `retirements` compatibility key
  are unchanged. Every transaction takes the mode-0600 interprocess lock,
  reloads state under that lock, mutates it and releases the lock. A shared
  helper owns the protocol and releases the lock on error.
- Browser send and queue mutations use the single durable-store implementation
  exported by `codex-web`. Existing key prefixes and record shapes remain
  unchanged for the default endpoint. Custom conversation endpoints derive a
  distinct namespace from the effective endpoint; applications may declare an
  explicit stable alias namespace when old and new routes intentionally name
  the same authority. Missing, corrupt or silently discarded storage fails
  closed before network I/O.
- Browser conversation targets are parsed against the current origin and must
  retain that exact origin. Control characters, queries, fragments and
  normalization tricks including backslash-to-authority forms are rejected.
  Browser input still cannot select a trusted socket, thread or working
  directory.
- Collaboration controls are rendered from the server catalog. A regression
  test covers an additional mode, and no mode name is embedded in the template.
- The public reusable API is `/codex/conversations/<id>/...`. For the documented
  rollback window, the portal continues to generate the old exact
  `/api/sessions/<slug>/...` conversation routes and aliases only conversation
  operations to the shared handler. Workspace session operations remain owned
  by the portal. The shipped browser contract exercises the real exported
  client at the old route. Alias removal requires expiration of the rollback
  window and successful verification with only the public route.
- `codexController` embeds the shared conversation client and adds only
  workspace-specific behavior; it does not duplicate the provider interface.
- Package switching reconciles a fixed command and skill inventory. Compatibility
  tombstones remain until every retained generation in the rollback window no
  longer needs the removed name; only package-owned links are removed.
- `.dev-workspace.json` opts vpsFree.cz into aitherdev labels, SSH attachment
  and both cluster providers. A workspace without that configuration exposes
  generic labels and no providers.
- Deploy the system substrate first, then the user profile. Existing aitherdev
  credential, PKI, certificate, socket, hostname, listener, group, firewall and
  public-CA paths are unchanged. The preceding profile/Codex pair remains
  available through `workspace-host rollback`; system Codex remains installed
  for the first rollout window.

## v4 findings and exact remediation

- General blocking: rejected intermediate ledger ownership and a combined
  portal correction commit. Rewrote the still-unmerged histories so every
  retained commit has the final safe protocol and independently reviewable
  catalog, storage and compatibility-route changes.
- General blocking / Scope important: repeated downstream pin corrections.
  Folded final exact revisions into their owning dependency/input commits.
- Architecture blocking: custom conversation paths shared durable retry keys.
  Bound the default namespace to the effective endpoint and exposed a deliberate
  alias namespace for route continuity; added isolation and alias tests.
- Architecture blocking: callers repeated the ledger lock/reload/mutate/save
  sequence. Added one generic transaction helper, migrated all callers and
  covered release after an error.
- Scope important: the portal browser contract duplicated a fake client.
  Replaced it with the exact served `conversationAssets.createConversationClient`
  and retained end-to-end legacy-route coverage.
- Risk important: `//evil`-style backslash normalization could turn an accepted
  relative string into a cross-origin URL in the browser. Parse and compare the
  final URL origin and reject control/query/fragment input; added regression
  cases.
- Advisory cleanup: removed the unused `validID` extension and redundant key
  method, embedded the provider client, documented compatibility exit criteria,
  and updated `state.md` to the exact final heads.

## Quick verification before this rerun

- `codex-web`: `nix develop -c node
  test/conversation_browser_contract_test.cjs` passed; `nix develop -c sh -c
  'env TMPDIR=/tmp go test -mod=mod -race ./...'` passed every package.
- `dev-workspace`: `nix develop -c sh -c 'cd portal && env TMPDIR=/tmp go test
  -mod=mod -race ./...'` passed every package. Focused route and shipped-client
  integration cases also passed.
- `vpsfree-cz-workspace`: `nix flake check --print-build-logs` passed at the
  exact final pin tree.
- `vpsfree-cz-configuration`: `nix flake check --no-build --show-trace` passed
  at the exact final input tree.
- `git diff --check` passes and all implementation worktrees are clean.

Long final package/configuration builds, deployment, live App Server exercises,
profile switch/rollback and empty-workspace compatibility remain intentionally
after this review rerun.

## Review lanes and risk

Overall risk is high. Rerun General, Architecture and repetition, Scope and
proportionality, and Risk and compatibility with `gpt-5.6-sol` at `xhigh`.
Inspect every retained commit boundary and final tree, verify every v4 finding
against the exact heads above, and report any new issue introduced by the
remediation.
