# Mandatory change review packet: final exact heads

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
  cluster socket identities, profile generations, and submission ledger schema
  3 across the staged cutover.

Non-goals are database, vpsAdmin API, node-daemon protocol, vpsAdminOS, release,
default-branch integration, session archival, deletion, and session stopping.

## Exact repositories and ranges

- `codex-web`
  - base: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8`
  - head: `601c8f3b7d40178b89adb8a0ed245d68cd3c0bb0`
  - commits: pure client move; application-owned policy/API; exclusive durable
    ledger ownership; capability-checked HTTP/browser integration; example and
    documentation.
- `dev-workspace`
  - base: `f39f8e62097b5e9da9de8a5eb678131b1e478e35`
  - head: `245be26213c0b69afc604d1cba241bdbb8985528`
  - commits: module path; core/vpsFree package variants; exact conversation
    dependency; profile-owned runtime tools; NixOS module; portal policy;
    workspace capability configuration; generic runtime defaults; docs.
- `vpsfree-cz-workspace`
  - base: `91b85b48b35cef51fd8920cd3445ca23a0023648`
  - head: `a7258165314eb762c37b1f6f70572650a6410f2c`
  - commits: implementation delegation and exact package pin; explicit
    vpsFree/aitherdev workspace capabilities.
- `vpsfree-cz-configuration`
  - base: `7481618dacab04bfd5b09bc730c373c2d2bf14d7`
  - head: `d21827a110438dcb014a97558674bbdc35d9c1c0`
  - commits: final `devWorkspace` channel declaration and lock; aitherdev host
    module adoption.

The dependency pins are exact and one-way:

`vpsfree-cz-workspace -> dev-workspace@245be26 -> codex-web@601c8f3`

The configuration channel also pins `dev-workspace@245be26`, whose nested
source is `codex-web@601c8f3`.

## Compatibility and deployment decisions

- The core Codex client accepts explicit identity, defaults, runtime roots,
  source kinds, developer instructions, and optional nonblocking prompt policy.
  Generic clients do not auto-answer prompts.
- The durable ledger remains schema 3 and retains the serialized
  `retirements` compatibility key. One mode-0600 lock gives a client exclusive
  per-socket ownership; `Close` is terminal and releases it.
- Browser mutations persist a base-path and conversation-scoped operation ID
  before network I/O. Missing or corrupt storage fails closed. The server owns
  the trusted client, thread, directory, capabilities, and shared mutation
  lock.
- Package switching reconciles a fixed command and skill inventory. Tombstones
  remain for every generation in the rollback window. Only links resolving
  into selected or retained package generations are removed; unrelated
  same-name symlinks remain untouched. Rollback and compensation pass the exact
  restored generation.
- `.dev-workspace.json` opts vpsFree.cz into aitherdev labels, SSH attachment,
  and both development-cluster providers. Generic workspaces expose none.
- Deploy the system substrate first. It leaves the user-owned router, portal,
  Codex, tmux, registry, session tracking, and authority state in place. Switch
  the user profile second; the preceding profile/Codex pair remains available
  through `workspace-host rollback`.
- Existing aitherdev credential, PKI, certificate, socket, hostname, listener,
  group, firewall, and public CA paths are unchanged. System Codex remains
  installed for the first rollout's rollback window.

## Verification before review

- `codex-web`: `nix flake check --print-build-logs` passed; exact-head
  `go test -mod=mod -race ./...` passed for all packages. The API-only
  intermediate commit also passed `go test -mod=mod ./codex` and its Nix build.
- `dev-workspace`: exact-head race tests passed for every Go package. Full
  `nix flake check --print-build-logs` passed for core, vpsFree, and host-module
  checks: 285 session runs / 2721 assertions per package, 45 cluster runs / 512
  assertions per package, 55 host runs / 332 assertions per package, and all KB
  suites (121 runs / 543 assertions total) passed.
- `dev-workspace`: the direct ambient Ruby host run passed with 55 runs / 336
  assertions; its Minitest version counts the two `assert_empty` inventory
  checks differently from the Nix derivation's 332-assertion result.
- `vpsfree-cz-workspace`: `nix flake check --print-build-logs` and
  `nix build --no-link .#dev-workspace-vpsfree` passed at the exact pin.
- `vpsfree-cz-configuration`: Nixfmt and every mandatory Overcommit hook passed
  for both final commits. `confctl` generated the exact final lock before it was
  folded into the input commit.
- `git diff --check` passes and all four implementation worktrees are clean.

Long configuration builds, deployment, live App Server exercises, profile
switch/rollback, and empty-workspace compatibility checks remain intentionally
after this review.

## Review lanes and risk

Overall risk is high. Review General, Architecture and repetition, Scope and
proportionality, and Risk and compatibility. Inspect every commit boundary as
well as the final tree. Earlier review findings about corrupt browser storage,
generic prompt policy, collaboration modes, compatibility links, client ledger
ownership, false cutover documentation, orphan pins, generated update
boundaries, and commit rationales were remediated; do not assume the
remediations are correct.
