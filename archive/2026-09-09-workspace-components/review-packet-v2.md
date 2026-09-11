# Mandatory change review packet, remediation rerun

## Requested outcome and acceptance criteria

Implement the component split in `plan.md`:

- Keep `vpsfree-cz-workspace` as coordination records, policy, and a thin
  package-selection flake.
- Publish reusable public MIT repositories `dev-workspace` and `codex-web`.
- Preserve runtime, persistence, CLI, URL, identity, credential, and rollback
  contracts during an aitherdev cutover from feature branches.
- Move stable host resources into a reusable secure NixOS module.
- Provide reusable Go and browser Codex App Server integration without another
  service.
- Keep dependency direction
  `vpsfree-cz-workspace -> dev-workspace -> codex-web`.
- Do not integrate default branches, release, archive, delete, or stop sessions.

Initiative: `2026-09-09-workspace-components`.

Plan and state:

- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/plan.md`
- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/state.md`

This is a full rerun after the first four-lane review found invalid initialize
JSON, unsafe browser retries, an obsolete packaged protocol corpus, mutation
lock and deadline regressions, missing policy tests, incomplete compatibility
link activation, slow event-stream shutdown, passive data overexposure, a
message-limit mismatch, and non-buildable or poorly separated commits. Inspect
the rewritten series directly and do not assume those remediations are correct.

## Repositories and reviewed commits

- `vpsfree-cz-workspace`
  - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/workspace`
  - Base: `91b85b48b35cef51fd8920cd3445ca23a0023648`
  - Head: `86bac06a2c92178b62ce18e8c50e3fef58d2bd01`
  - Commit: `86bac06 workspace: delegate reusable development components`.
- `dev-workspace`
  - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/dev-workspace`
  - Base: `f39f8e62097b5e9da9de8a5eb678131b1e478e35`
  - Head: `80b12cfe78a3ce8308976263456c6731f6f743be`
  - Commits: `798f430 package: consume the reusable conversation runtime`;
    `a323a4c host: keep profile transitions generation-safe`;
    `bc893ee host: publish the reusable NixOS substrate module`;
    `80b12cf docs: describe the reusable workspace runtime`.
- `codex-web`
  - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/codex-web`
  - Base: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8`
  - Head: `b7881e009447816ddcc977a55020fb760f5d423e`
  - Commits: `703e798 web: publish reusable Codex conversation components`;
    `b7881e0 docs: add a standalone conversation example`.
- `vpsfree-cz-configuration`
  - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration`
  - Base: `7481618dacab04bfd5b09bc730c373c2d2bf14d7`
  - Head: `831fa603da5b2a398c3de9e64adf7036340b5a8c`
  - Commits: `424775da inputs: set devWorkspace to 80b12cfe`, generated
    unchanged by `confctl`; `831fa603 aitherdev: use the reusable workspace host module`.

All four worktrees are clean. The new repositories' heads are pushed because
downstream inputs require public revisions. The workspace and configuration
heads remain local until this review is resolved.

## Commit split and bundling rationale

The new repositories' public bootstrap commits are the review bases.

`codex-web` has one implementation commit because its Go module move, App
Server client, HTTP handler, embedded browser assets, request corpus, and flake
checks form one buildable public module. The second commit contains the example,
README, and repository guidance. Neither commit needs a later fixup to build.

`dev-workspace` first moves the portal to the public dependency and publishes
the core and vpsFree package outputs at the same exact revision. Those code and
package changes are inseparable: deleting the local client without updating
the package's protocol source and Go/Nix pins leaves the flake broken. Host
profile transition behavior, the independently consumed NixOS host module, and
documentation are separate commits. The final package vendor hash is part of
the package commit.

The workspace change is one commit because deleting the delegated
implementation without selecting its replacement makes the workspace flake
unevaluable. Configuration keeps the generated `confctl` pin unchanged and
separates aitherdev's host-module adoption.

## Boundaries and decisions

Non-goals are database, vpsAdmin API, daemon protocol, deployed node, and
vpsAdminOS changes. The split does not alter manifest schemas, lifecycle or
creation journals, runtime authorities, operation receipts, submission-ledger
schema 3, cluster state or socket identities, registry data, profile identity,
thread IDs, working directories, tmux identity, command names, service names,
URLs, or credential material. No default-branch integration is authorized.

The unreleased public HTTP surface uses only canonical endpoints. The rejected
`snapshot`, `/send`, and `{text}` compatibility spellings were removed.
Transcript, pending-request, and queue-read capabilities are independent.
Every mutation target supplies an application-owned lock shared with
workspace-only plan and lifecycle operations. Non-streaming operations have a
30-second default deadline, and applications can close streams with a shutdown
channel. `dev-workspace` supplies its published 20,000-byte message limit.

Browser send and queue operation IDs are written to required storage before
network I/O. Keys include the base path and opaque conversation ID. The mounted
UI takes explicit capabilities, does not call or render unavailable surfaces,
and initializes settings from the current thread. Lack of storage fails closed
before a mutating client is mounted.

The submission ledger remains schema 3. A mode-0600 lock file next to it gives
one client process exclusive ownership; rollback versions ignore the lock only
after the new portal and client have stopped. The supported topology has one
client per App Server socket.

Rejected alternatives remain a monorepo, a standalone codex-web service,
moving workspace network ownership into the host module, browser-selected
socket/thread/cwd values, and a different Codex derivation.

## Dependencies and configuration

- `dev-workspace` pins `github:aither64/codex-web` at
  `b7881e009447816ddcc977a55020fb760f5d423e` in its Go pseudo-version and
  flake lock. A Nix build assertion requires the pins to match.
- `vpsfree-cz-workspace` pins `github:aither64/dev-workspace` at
  `80b12cfe78a3ce8308976263456c6731f6f743be`.
- `vpsfree-cz-configuration` pins the same revision through the
  `dev-workspace` confctl channel.
- `dev-workspace` retains Numtide `llm-agents.nix` revision
  `c2a308c84bbfa9f30827344219b7284f8104bdd8` and Codex 0.153.4.
- aitherdev retains its hostnames, groups, socket, authentication files, PKI
  and TLS paths, CA name, listener, and WireGuard source range.
- The system Codex remains installed for the first rollout because the prior
  system-owned application remains a supported rollback target.

## Quick verification

- `codex-web`: `CGO_ENABLED=0 go test ./...` and `go vet ./...` passed.
  Node syntax, the low-level browser contract, durable send/queue response-loss
  tests, unavailable-storage tests, and a mounted DOM/settings/capability test
  passed through `nix develop`. The protocol corpus covers `codex/client.go`.
- `dev-workspace`: `CGO_ENABLED=0 go test ./...` and `go vet ./...` passed.
  Added tests cover shared plan/browser serialization, application shutdown of
  event streams, passive transcript-only access, exact 20,000/20,001-byte send
  and queue boundaries, and the moved recovery/retirement policy. The host
  suite passed with 52 runs and 330 assertions. Four KB suites passed with 121
  runs and 543 assertions and are now part of the vpsFree derivation check.
  The Go vendor derivation builds, the owning codex-web protocol corpus matches
  the owning client, and `nix flake check --no-build` passes.
- `vpsfree-cz-workspace`: `nix flake check --no-build` resolves the final
  `dev-workspace-vpsfree` package.
- `vpsfree-cz-configuration`: `confctl` created the exact input update. Nixfmt
  and all repository pre-commit hooks passed for both rewritten commits.
- `git diff --check` passed, and all implementation worktrees are clean.

Complete package builds, configuration builds, live App Server exercises,
profile switch and rollback, deployment, and empty-workspace checks remain
deferred until this mandatory review is resolved.

## Risk and compatibility assumptions

Overall risk is High because the change affects authentication, secret paths,
host configuration, public cross-project APIs, persisted runtime state,
destructive lifecycle helpers, deployment, rollback, and mixed package
generations. Every reviewer uses `gpt-5.6-sol` at `xhigh`. Selected lanes are
General, Architecture and repetition, Scope and proportionality, and Risk and
compatibility.

The host module must render equivalent activation, nginx, TLS renewal, group,
and firewall behavior for aitherdev. The certificate reconciler now compares
the exact sorted SAN set, so removing an alias also renews the leaf certificate.
Existing credential and certificate paths are reused.

Candidate activation relinks candidate-provided compatibility commands and
skills after a successful switch. Rollback still runs from the newer immutable
dispatcher, so commands that did not exist in an older target remain available.
Failed candidate activation compensates by restoring links from the initiating
generation. Stable core commands and units continue to follow the selected
profile.

## Ownership, public interfaces, and consumers

`codex-web` owns the generic App Server client, durable submission primitives,
capability-checked conversation HTTP handler, and embedded ES module. Its
resolver maps an opaque application ID to a trusted client, thread, canonical
directory, capabilities, and shared mutation lock on every request. The
handler verifies the thread-directory binding. The browser cannot select those
resources. Consumers are `dev-workspace/portal` through exact Go and Nix pins
and the bundled loopback example.

`dev-workspace` owns development-session source policy, defaults, recovery,
retirement, activity checks, lifecycle, portal policy, workspace profile
commands, user units, and optional vpsFree cluster and KB helpers. Its public
outputs are `dev-workspace`, `dev-workspace-vpsfree`, compatibility aliases,
`nixosModules.host`, and `nixosConfigurations.example`. Consumers are the thin
workspace flake and aitherdev's configuration feature.

`vpsfree-cz-workspace` owns coordination policy and records and consumes the
vpsFree package. `vpsfree-cz-configuration` owns the channel selection, network
topology, concrete host-module options, and temporary system Codex rollback
dependency.
