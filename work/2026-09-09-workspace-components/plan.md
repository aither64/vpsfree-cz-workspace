# 2026-09-09-workspace-components

## Goal

Split the development environment into four layers:

- `codex-web`: reusable Codex App Server conversation integration.
- `dev-workspace`: reusable session, portal, profile and host runtime.
- `vpsfreecz/dev-workspace`: vpsFree-specific commands, skills and development
  cluster providers, parameterized by a consuming workspace.
- `vpsfree-cz-workspace`: development records, policy and the concrete
  aitherdev/domain configuration.

The final dependency direction is:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` separately consumes the same generic
`aither64/dev-workspace` revision for the privileged host module.

## Repositories

Use these SSH remotes:

```text
git@github.com:aither64/codex-web.git
git@github.com:aither64/dev-workspace.git
git@github.com:vpsfreecz/dev-workspace.git
git@github.com:aither64/vpsfree-cz-workspace.git
git@github.com:vpsfreecz/vpsfree-cz-configuration.git
```

The two `dev-workspace` repositories share a basename. Keep the existing
generic repository under local project name `dev-workspace` and use local
project name `vpsfree-dev-workspace` for `vpsfreecz/dev-workspace`.

## Implementation

1. Make the tracked trees of `codex-web` and generic `dev-workspace` contain
   no case-insensitive `vpsfree` or `aitherdev` matches. Preserve published Git
   history and enforce the current-tree boundary in flake checks.
2. Rename the generic runtime namespaces: `VPSFREE_DEV_SESSION_*` becomes
   `DEV_SESSION_*`, `VPSFREE_WORKSPACES_*` becomes `DEV_WORKSPACES_*`, and the
   singleton workspace, host-mode and dev-cluster variables receive equivalent
   generic names. Rename Ruby modules and tmux metadata in the same change.
3. Replace the hard-coded vpsAdmin/vpsAdminOS integration with a package-owned,
   strictly validated extension catalog. The catalog declares exported
   commands, installed Codex skills and development-cluster providers. A
   workspace may select provider IDs, but executable paths and labels come
   only from the immutable package catalog.
4. Expose a Nix package-construction interface from generic `dev-workspace`.
   Remove its vpsFree package variant, KB tooling, skills, provider sources and
   organization-specific documentation.
5. Bootstrap the empty public `vpsfreecz/dev-workspace` repository from
   filtered relevant history. Keep a neutral default-branch root and replay
   the extracted history on the dated feature branch so later integration can
   fast-forward. The repository owns KB tooling, all currently bundled skills,
   vpsAdmin/vpsAdminOS providers and the one-time namespace migration helper.
   Its tracked tree must contain no case-insensitive `aitherdev` matches.
6. Require concrete site configuration when building the vpsFree package.
   Move aitherdev KB endpoints and vpsAdmin cluster defaults into
   `vpsfree-cz-workspace`. Extend `.dev-workspace.json` to carry the portal
   hostname and aliases as workspace configuration. Keep privileged TLS,
   nginx, firewall and DNS values in `vpsfree-cz-configuration`.
7. Move the inline host checks out of generic `flake.nix`: evaluation checks
   go in `nix/tests/host-module.nix` and the NixOS VM goes in
   `nix/tests/host-module-idempotency.nix`.
8. Keep the existing GitHub Actions checks in `codex-web` and generic
   `dev-workspace`. Add the same complete flake check to
   `vpsfreecz/dev-workspace`, using verified current official actions.

## Public interfaces

Generic runtime variables use the prefixes `DEV_SESSION_*` and
`DEV_WORKSPACES_*`. The remaining public names are `DEV_WORKSPACE_NAME`,
`DEV_WORKSPACE_HOST_MODE`, `DEVCLUSTER_WORKSPACE` and
`DEV_SESSION_LIFECYCLE_*`. Generic tmux options use `@dev_session*` names.
There are no legacy environment or tmux aliases after cutover.

Generic user state defaults to:

```text
~/.config/dev-workspaces
~/.local/state/dev-workspaces
$XDG_RUNTIME_DIR/dev-workspaces
```

Generic host state defaults to:

```text
/run/dev-workspaces/router.sock
/run/lock/dev-workspaces-substrate.lock
/var/lib/dev-workspaces/password/password
/var/lib/dev-workspaces/auth/htpasswd
/var/lib/dev-workspaces/pki
/var/lib/dev-workspaces/tls
/var/lib/dev-workspaces/public/ca.pem
```

The extension catalog is package-owned and schema-versioned. Provider entries
contain an ID, display label, executable and state-directory identity. Helpers
retain the existing `status`, `reset`, `cleanup-paths` and `transition-adopt`
protocol, but receive the workspace through `DEVCLUSTER_WORKSPACE`.

Workspace configuration schema 2 retains display, host and SSH labels, adds a
`portal` mapping with `hostname` and `aliases`, and selects provider IDs. The
registry stores the resolved domain snapshot. CLI hostname flags remain
available as explicit overrides.

## Compatibility and migration

This is an intentional one-time incompatible namespace cutover. Mixed old and
new runtime clients are unsupported. The migration must run only when all
conversations are idle and no lifecycle operation is unfinished.

A journaled vpsFree migration helper moves the user registry, profile and
runtime roots; updates live tmux environment/options and runtime authority
paths; and supports an exact reverse operation. Machine-consumed `portal.yml`
socket paths are updated in the coordination checkout after a fresh inventory.
Historical prose remains unchanged.

The root-owned password, auth, CA, TLS and public-CA directories move into the
generic host state layout. The exact password, CA, leaf certificate, private
keys, selected pair, ownership and modes must be preserved. New targets must
be absent before migration. Keep a private rollback journal until the user
accepts the deployed result.

Deployment order is `codex-web`, generic `dev-workspace`, vpsFree
`dev-workspace`, `vpsfree-cz-workspace`, then `vpsfree-cz-configuration` and
the user-profile cutover. On failure, stop new services, reverse the journaled
state move, select the previous system and profile generations, and verify the
original hashes before restart.

Deployment to aitherdev is authorized. Default-branch integration of the
feature repositories, releases, archival, deletion and session stopping are
not authorized.

## Testing and review

- Run focused Go, Ruby, Node and Nix checks in each repository.
- Test strict extension-catalog validation, collisions, provider selection,
  absent providers and transitions with existing provider state.
- Test the namespace migration and reversal in isolated fixtures, including
  occupied targets, unsafe links or mounts, interrupted retries, malformed
  authorities and exact credential/CA preservation.
- Test the extracted host module checks, then commit and push immutable heads.
- Run the mandatory high-risk General, Architecture, Scope and Risk review
  lanes with `gpt-5.6-sol` at `xhigh` before long NixOS VM and full integration
  checks.
- Require successful exact-head GitHub Actions in both generic repositories
  and `vpsfreecz/dev-workspace`.
- Live acceptance requires the same domains, TLS identity, credentials,
  conversation thread IDs and workspace roots; restored terminal sessions;
  working KB commands and both cluster providers; and no active old runtime
  paths.

No database, vpsAdmin API, daemon protocol or deployed vpsAdminOS node change
is part of this initiative.
