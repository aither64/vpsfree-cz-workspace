# 2026-09-09-workspace-components

## Goal

Split the development workspace into three components:

- `vpsfree-cz-workspace`: initiative records, durable notes, workspace policy,
  local bare repositories and worktrees, plus a thin flake that selects the
  installed tooling.
- `dev-workspace`: reusable development-session lifecycle, portal shell,
  host/profile management, packaged workspace skills, and optional
  vpsAdmin/vpsAdminOS cluster providers.
- `codex-web`: reusable Go and browser integration for Codex App Server
  conversations, with an example application.

The new repositories are public and MIT licensed. Their SSH remotes are:

```text
git@github.com:aither64/dev-workspace.git
git@github.com:aither64/codex-web.git
```

Both new repositories use `master` as the default branch. The workspace
`AGENTS.md` will list them in the Project Map and record these exact remotes as
narrow exceptions to the normal `vpsfreecz` organization rule.

## Affected repositories

- `vpsfree-cz-workspace`, branch `2026-09-09-workspace-components` in
  `worktrees/2026-09-09-workspace-components/workspace`.
- `dev-workspace`, branch `2026-09-09-workspace-components` in
  `worktrees/2026-09-09-workspace-components/dev-workspace`.
- `codex-web`, branch `2026-09-09-workspace-components` in
  `worktrees/2026-09-09-workspace-components/codex-web`.
- `vpsfree-cz-configuration`, branch `2026-09-09-workspace-components` in
  `worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration`.

The dependency direction is
`vpsfree-cz-workspace -> dev-workspace -> codex-web`.

## Implementation

1. Seed both empty repositories from disposable, path-filtered clones of
   workspace baseline `3580e60bb035c2d0ba5be6f0d2489bbbf30ded3d`. Add MIT
   licenses, provenance READMEs, repository-specific `AGENTS.md` files and
   verified CI before starting their dated feature branches.
2. Extract the portal, session helpers, host/profile manager, cluster sources,
   tests and operational documentation into `dev-workspace`. Package the KB
   helpers and reusable vpsFree skills as a separate compatibility output so
   the core application remains reusable.
3. Export `nixosModules.host` under `services.dev-workspaces`. Its secure
   preset provides generated basic authentication, local-CA TLS, nginx
   proxying and a closed firewall until source networks are configured. The
   module owns stable host resources, not the user application.
4. Source Codex unchanged from
   `numtide/llm-agents.nix@c2a308c84bbfa9f30827344219b7284f8104bdd8`,
   currently version 0.153.4. Preserve Numtide's pinned nixpkgs and package
   derivation. The user-profile application owns this runtime and retains the
   preceding profile generation for rollback.
5. Convert `vpsfree-cz-workspace` to a records and policy checkout. Its thin
   flake re-exports `dev-workspace-vpsfree` with the current package and app
   names. Remove executable tooling only after the installed package and a
   second empty workspace pass compatibility tests.
6. Add `devWorkspace` to `vpsfree-cz-configuration` through `confctl`, replace
   aitherdev's inline workspace substrate with the host module and preserve all
   existing credentials, paths, hostnames, groups, sockets and network policy.
   Keep the shared bridge, DHCP and NAT configuration owned by aitherdev.
7. Deploy this parity-preserving `dev-workspace` stage and test a rollback.
   Then extract `codex-web`, port the portal to its public Go and ES-module API,
   deploy the second profile generation and test rollback again.

## Public interfaces

`dev-workspace` exports the `dev-workspace` and `dev-workspace-vpsfree`
packages, compatibility aliases `workspace-portal` and `workspace-host`, the
current commands and user units, `nixosModules.host`, and
`nixosConfigurations.example`. Existing `VPSFREE_*` environment variables,
runtime paths and command contracts remain unchanged during the split.

`codex-web` uses module path `github.com/aither64/codex-web`. It exports a Go
App Server client, secured conversation HTTP handlers and embedded assets. The
browser entry point is `mountConversation(element, options)` and returns an
unmount function. An application resolver maps an opaque conversation ID to a
trusted App Server connection, thread ID, canonical working directory and
explicit capabilities on every request. Browser input cannot select these
resources. Version 0.1 supports Unix sockets only.

Workspace actions such as session creation, plan implementation, archive,
delete, artifacts, repositories and clusters remain in `dev-workspace`.
`codex-web` exposes callbacks for application actions without implementing
workspace policy.

## Compatibility and deployment

The first two deployments do not change manifest schemas, lifecycle or
creation journals, runtime authorities, operation receipts, submission-ledger
schema v3, cluster state/socket identities, registry data, profile-generation
identity, thread IDs, working directories, tmux identities, URLs or credential
material. New code must read state created by the deployed package, and the
previous profile generation must read all state written during the test.

Run profile transitions only when no lifecycle journal is unfinished and every
managed conversation is idle. Recheck that the independent controller is
outside the managed Codex and tmux service cgroups before each transition.

Deployment to aitherdev is authorized. Default-branch integration, releases,
archival, deletion and session stopping require a separate explicit request.
When integration is authorized, fast-forward in this order: `codex-web`,
`dev-workspace`, `vpsfree-cz-workspace`, then `vpsfree-cz-configuration`.

## Testing and review

- Run race-enabled Go tests, Ruby helper suites, browser contract tests,
  JavaScript checks through Nix, Codex protocol-corpus coverage, shell checks,
  Nix formatting/evaluation and complete flake/package builds.
- Test exact-origin and per-operation authorization, rejection of arbitrary
  thread/socket/cwd selection, payload limits, Markdown sanitization,
  interactions, durable retry receipts and private state permissions.
- Exercise send, steer, queue/retry, reconnect, settings, questions, approvals,
  interrupt and event-stream recovery through the standalone `codex-web`
  example.
- Register a second empty workspace using only installed packages and verify
  that current sessions retain their identities and transcripts through both
  upgrades and rollbacks.
- Before long integration tests for each deployable stage, commit all intended
  changes, run quick checks, then perform the mandatory high-risk review using
  General, Architecture, Scope and Risk lanes with `gpt-5.6-sol` at `xhigh`.
- Push dated branches, monitor GitHub Actions, investigate every failure and
  cancel only superseded runs whose SHA is no longer current.

No database, vpsAdmin API, daemon protocol, deployed node or coordinated
vpsAdminOS machine change is part of this initiative.
