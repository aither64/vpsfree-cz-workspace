# Mandatory change review packet

## Requested outcome and acceptance criteria

Implement the component split in `plan.md`:

- Keep `vpsfree-cz-workspace` as coordination records, policy, and a thin
  package-selection flake.
- Publish reusable public MIT repositories `dev-workspace` and `codex-web`.
- Preserve deployed runtime, persistence, CLI, URL, identity, credential, and
  rollback contracts during a staged aitherdev cutover.
- Move stable host resources into a reusable secure NixOS module.
- Provide reusable Go and browser Codex App Server integration without adding
  another service.
- Keep dependency direction
  `vpsfree-cz-workspace -> dev-workspace -> codex-web`.
- Do not integrate default branches, release, archive, delete, or stop
  sessions.

Initiative: `2026-09-09-workspace-components`.

Plan and state:

- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/plan.md`
- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/state.md`

## Repositories and reviewed commits

- `vpsfree-cz-workspace`
  - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/workspace`
  - Base: `91b85b48b35cef51fd8920cd3445ca23a0023648`
  - Head: `4f8b6ecda4210f36a63b35c8dc025f62f3b70adc`
  - Commits: `5387ff3 workspace: delegate reusable development components`;
    `4f8b6ec flake: select the reusable workspace package`.
- `dev-workspace`
  - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/dev-workspace`
  - Base: `f39f8e62097b5e9da9de8a5eb678131b1e478e35`
  - Head: `96b6e843bbca8f6d2659a6ba31492cd75bc0f2eb`
  - Commits: `c2a1b85 portal: consume the reusable conversation packages`;
    `8837f44 package: publish self-contained workspace applications`;
    `8df3f16 host: keep profile transitions generation-safe`;
    `25bb603 docs: describe the reusable workspace runtime`;
    `96b6e84 package: update the Codex client vendor hash`.
- `codex-web`
  - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/codex-web`
  - Base: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8`
  - Head: `8c6d43013a419a9eda671673cd9ae17193aa2c6f`
  - Commits: `9d91999 api: publish the reusable App Server client`;
    `9eaeff8 web: add a capability-checked conversation handler`;
    `8c6d430 docs: add a standalone conversation example`.
- `vpsfree-cz-configuration`
  - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration`
  - Base: `7481618dacab04bfd5b09bc730c373c2d2bf14d7`
  - Head: `8249c1414853b7954a6d53c39c744657a0c4e27f`
  - Commits: `5f7fc10f inputs: set devWorkspace to 96b6e843`, generated
    by `confctl`; `8249c141 aitherdev: use the reusable workspace host module`.

All implementation worktrees are clean. The `codex-web` and `dev-workspace`
heads are pushed because downstream pins need public revisions. The workspace
and configuration heads are committed locally and will be pushed after review
remediation.

## Commit split and bundling rationale

The two new repositories' bootstrap commits are already on their public
`master` branches and are the review bases.

`codex-web` separates the generic App Server client, the complete secured HTTP
and browser integration, and the example plus documentation. The handler and
browser module are one commit because the Go handler embeds and serves those
assets as one public contract.

`dev-workspace` separates portal consumption and workspace policy, package and
NixOS interfaces, generation-safe host transitions, documentation, and the
mechanical vendor-hash refresh. Tests stay with the behavior they cover. The
package commit includes the host module because its flake exports, example,
generated reconciler, and package variants are one evaluable Nix interface.

The workspace separates removal and ownership documentation from its final
dependency selector. Configuration keeps the generated `confctl` input update
unchanged and separates the machine-specific module adoption. Repeated feature
pin updates and superseded designs were removed by rewriting the unmerged
branches.

## Boundaries and decisions

Non-goals are database, vpsAdmin API, daemon protocol, deployed node, and
vpsAdminOS changes. The split must not alter persisted formats, paths,
submission ledger schema 3, runtime authorities, lifecycle journals, cluster
socket identity, command names, systemd user unit names, thread IDs, working
directories, tmux identity, or URLs. No default-branch integration is
authorized.

Rejected alternatives were a monorepo, a standalone codex-web service, moving
workspace network ownership into the reusable module, accepting
browser-selected socket, thread, or cwd values, and sourcing Codex from a
different derivation.

The user selected public MIT repositories on `master`, the three-level
dependency direction, a staged compatible cutover, and authorized aitherdev
deployment from feature branches.

## Dependencies and configuration

- `dev-workspace` pins `github:aither64/codex-web` at
  `8c6d43013a419a9eda671673cd9ae17193aa2c6f` in both `flake.lock` and the Go
  pseudo-version. A Nix build-time assertion requires the two pins to match.
- `vpsfree-cz-workspace` pins `github:aither64/dev-workspace` at
  `96b6e843bbca8f6d2659a6ba31492cd75bc0f2eb`.
- `vpsfree-cz-configuration` pins that same revision through the
  `dev-workspace` confctl channel.
- `dev-workspace` retains Numtide `llm-agents.nix` revision
  `c2a308c84bbfa9f30827344219b7284f8104bdd8` and Codex 0.153.4.
- aitherdev keeps its hostnames, groups, router socket, authentication files,
  PKI and TLS directories, CA name, listener, and WireGuard source range.
- The system Codex remains installed during the first rollout because the
  preceding system-owned application is still a supported rollback target.

## Quick verification

- `codex-web`: `CGO_ENABLED=0 go test ./...` and `CGO_ENABLED=0 go vet ./...`
  passed. The public Node syntax and browser contract test passed. Protocol
  request-corpus coverage matches `codex/client.go`.
- `dev-workspace`: `CGO_ENABLED=0 go test ./...` and `CGO_ENABLED=0 go vet
  ./...` passed, including the Node-backed end-to-end browser contract. The
  workspace-host Ruby suite passed with 51 examples and 319 assertions. The Go
  module vendor derivation and `checks.x86_64-linux.host-module` built at the
  final pin. Node syntax and unit contracts passed.
- `vpsfree-cz-workspace`: flake metadata resolves and the selected package
  evaluates to `dev-workspace-vpsfree-0.1.0` at the final pin.
- `vpsfree-cz-configuration`: the generated `confctl` input update and the
  host-module commit passed Nixfmt and all repository pre-commit hooks.
- `git diff --check` passed before the commits, and every worktree is clean.

Complete flake builds, the configuration build, runtime transitions, rollback,
and empty-workspace checks are intentionally deferred until after review.

## Risk and compatibility assumptions

Overall risk is High because authentication, secrets, host configuration,
public cross-project APIs, persisted runtime state, destructive lifecycle
helpers, rollback, and mixed package generations are affected. Every reviewer
uses `gpt-5.6-sol` at `xhigh`. Selected lanes are General, Architecture and
repetition, Scope and proportionality, and Risk and compatibility.

The migration assumes the reusable host module renders equivalent activation,
nginx, TLS renewal, group, and firewall behavior for the supplied aitherdev
options. Existing credential and certificate paths are reused. The canonical
hostname is now included explicitly in certificate SANs because the wildcard
covers only one subdomain label.

The vpsFree package keeps KB source libraries beside the installed scripts.
Stable KB commands and packaged skill links remain on the immutable dispatching
generation while rollback changes the profile, so an older target package does
not need to contain those new compatibility paths. Existing state formats are
unchanged and older packages reject unsupported in-flight state as before.

## Ownership, public interfaces, and consumers

`codex-web` owns the generic App Server client, durable operation primitives,
capability-checked conversation HTTP handler, and embedded ES module. Its
resolver maps an opaque application ID to a trusted client, thread, canonical
directory, and capabilities on every request. The handler re-verifies the
thread-directory binding. The browser cannot select those resources. Current
consumers are `dev-workspace/portal` through exact Go and Nix pins and the
bundled loopback example.

`dev-workspace` owns development-session source policy, defaults, recovery,
retirement, activity checks, lifecycle, portal policy, workspace host/profile
commands, user units, and optional vpsFree cluster providers. Public outputs
are `dev-workspace`, `dev-workspace-vpsfree`, compatibility aliases
`workspace-host` and `workspace-portal`, `nixosModules.host`, and
`nixosConfigurations.example`. Consumers are the thin workspace flake and the
aitherdev configuration feature.

`vpsfree-cz-workspace` owns coordination policy and records and consumes the
vpsFree compatibility output. `vpsfree-cz-configuration` owns aitherdev's
channel selection, network topology, concrete host-module options, and the
temporary system Codex rollback dependency.
