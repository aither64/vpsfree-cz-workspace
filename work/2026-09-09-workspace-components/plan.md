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
   filtered predecessor history. Preserve selected source ancestry, including
   add/evolve/delete cycles whose paths are absent from the final tree, so the
   original provenance and commit identities remain auditable. Keep a neutral
   default-branch root and replay the current initiative as a clean functional
   tail on the dated feature branch so later integration can fast-forward. The
   repository owns KB tooling, all currently bundled skills, vpsAdmin/vpsAdminOS
   providers and the one-time namespace migration helper. Its tracked tree must
   contain no case-insensitive `aitherdev` matches.
6. Require concrete site configuration when building the vpsFree package.
   Move aitherdev KB endpoints and vpsAdmin cluster defaults into
   `vpsfree-cz-workspace`. Extend `.dev-workspace.json` to carry the portal
   hostname and aliases as workspace configuration. Keep privileged TLS,
   nginx, firewall and DNS values in `vpsfree-cz-configuration`.
7. Move the inline host checks out of generic `flake.nix`: evaluation checks
   go in `nix/tests/host-module.nix` and the NixOS VM goes in
   `nix/tests/host-module-idempotency.nix`. Keep namespace/package-construction
   coverage in `nix/tests/user-namespace.nix` and catalog coverage in
   `nix/tests/extension-catalog.nix`; `flake.nix` only wires those checks.
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
/run/lock/dev-workspace-substrate.lock
/var/lib/dev-workspaces/password/password
/var/lib/dev-workspaces/auth/htpasswd
/var/lib/dev-workspaces/pki
/var/lib/dev-workspaces/tls
/var/lib/dev-workspaces/public/ca.pem
```

The extension catalog is package-owned and schema-versioned. Provider entries
contain an ID, display label and immutable executable. The provider ID is also
its state-directory identity. Helpers retain the existing `status`, `reset`,
`cleanup-paths` and `transition-adopt` protocol, but receive the workspace
through `DEVCLUSTER_WORKSPACE`.

Workspace configuration schema 2 retains display, host and SSH labels, adds a
`portal` mapping with `hostname` and `aliases`, and selects provider IDs. The
registry stores the resolved domain snapshot. CLI hostname flags remain
available as explicit overrides.

## Compatibility and migration

This is an intentional one-time incompatible namespace cutover. Mixed old and
new runtime clients are unsupported. The migration must run only when all
conversations are idle and no lifecycle operation is unfinished. The final
package has only generic runtime names. A separately built compatibility
profile generation retains the old user namespace and router path and allows
the former activation variable solely to bootstrap the final profile during
the quiesced cutover.

A journaled vpsFree migration helper preflights both scopes before either
transition, then moves the user registry, profile and runtime roots and
supports an exact reverse operation. Although the helper can migrate retained
tmux metadata, the aitherdev deployment does not use that compatibility path:
all managed sessions, panes, authorities and the tmux server are stopped before
preflight. Its never-deployed journal schema is 5; there is no supported
predecessor journal to upgrade. The migration window freezes the complete
registry and portal-manifest inventory and requires runtime authorities,
sessions and the tmux socket to remain absent until migration completes.
Both scopes have a locked read-only reverse preflight that must pass before
either reverse operation. Active and archived machine-consumed
`portal.yml` socket paths are updated in the coordination checkout after a
fresh inventory so retained threads remain revivable. Each registered root is
the sole authority for its `.dev-workspace.json` presentation and provider
selection; reusable packages do not duplicate that workspace configuration.
The registered shared checkout must fast-forward to the reviewed feature before
alias-free deployment so its configuration, policy and metadata become
authoritative together.
Historical prose remains unchanged.

The generic user-state root is one explicit namespace contract shared by the
profile, portal lifecycle receipts, completed-removal state and dev-session
deletion recovery. A non-default compatibility namespace therefore moves and
reverses one complete state tree instead of leaving portal-owned state behind.

Generic host path defaults are exported by their owning runtime. The
organization migration asserts its target contract against that exact pinned
export, while aitherdev consumes the module defaults without repeating them.
The remaining portal domain identity is intentionally represented in both the
workspace registration and privileged host configuration; a durable
cross-repository predeployment checker requires exact equality and also proves
that user and host packages pin the same generic runtime revision.

The root-owned password, auth, CA, TLS and public-CA directories move into the
generic host state layout. The exact password, CA, leaf certificate, private
keys, selected pair, ownership and modes must be preserved. New targets must
be absent before migration. Keep the private migration journal until the user
accepts the deployed result.

The generic test suite previously left 11 `dev-session-test*` deletion
recovery roots below the otherwise unused target
`~/.local/state/dev-workspaces/removed`. Before forward preflight, preserve
that complete tree with an atomic rename to
`~/.local/state/dev-workspaces-test-recovery-20260911`. Do not delete it and do
not merge it into migrated live state. Verify the renamed inventory before
allowing the migration to create `~/.local/state/dev-workspaces`.

Deployment order is `codex-web`, generic `dev-workspace`, vpsFree
`dev-workspace`, and `vpsfree-cz-workspace`. Build the compatibility and final
generations first, compare the reviewed session list with the complete live
authority inventory, then stop every managed session, the tmux server, portal,
Codex, router and reconciliation services. Switch the existing profile to the
recorded compatibility generation, immediately stop any compatibility services
restarted by activation, and prohibit reconnects and lifecycle commands
throughout this narrow bridge window. Run both locked read-only preflights,
freeze their exact inventories, migrate both scopes, activate
`vpsfree-cz-configuration`, and only then switch the migrated profile to the
final package. Stop all ten audited authorities and recreate only the nine
active sessions through the final helper before reopening the router. Eight
receive fresh Codex client processes and one remains intentionally shell-only;
the stale authority for the archived session is not recreated. Existing live
processes, panes and tmux identities are not preserved. The recorded active
conversations are validated before any mutation and resumed by the ordinary
stable start path; if that audited inventory changes, the cutover fails closed
and its explicit site inventory must be reviewed instead of adding a
speculative recovery API. The site deployment is forward-only. On failure,
leave admission closed, diagnose the concrete stage in place and continue
forward through the retryable migration journals. The generic reverse primitive
remains implemented, but this deployment neither invokes nor validates an
automated rollback. Certificate renewal remains runtime-masked from host
preflight until forward acceptance.

Deployment to aitherdev and fast-forward integration of the workspace feature
into its `master` branch were authorized and completed. Default-branch
integration of the component and configuration feature branches, releases,
archival and deletion remain outside this deployment. The user explicitly
permitted stopping and recreating all aitherdev workspace/Codex sessions and
resetting the running development clusters; durable worktrees and tracking were
preserved.

## Testing and review

- Run focused Go, Ruby, Node and Nix checks in each repository.
- Test strict extension-catalog validation, collisions, provider selection,
  absent providers and transitions with existing provider state.
- Test the namespace migration and reversal in isolated fixtures, including
  occupied targets, unsafe links or mounts, interrupted retries, malformed
  authorities, wrong-owned rewrite files, symlinked ancestors and exact
  credential/CA preservation. Keep retained-tmux coverage for the reusable
  helper, while the aitherdev runbook proves the deployment-specific empty
  authority and stopped-socket precondition before namespace moves and rejects
  additions during the migration window.
- Run the cross-repository deployment checker against the exact workspace and
  configuration worktrees before every development deployment.
- Test the extracted host module checks, then commit and push immutable heads.
- Review checkpoints through v44 were used before deployment. The user ended
  further review cycles and directed deployment to proceed with forward fixes
  on aitherdev.
- Require successful exact-head GitHub Actions in both generic repositories
  and `vpsfreecz/dev-workspace`.
- Live acceptance verified the same domains, TLS identity, credentials and
  workspace roots; all nine active sessions recreated under the generic
  environment and the archived authority absent; working KB commands and both
  cluster providers; and no active old runtime paths or `VPSFREE_*` process
  environments.

No database, vpsAdmin API, daemon protocol or deployed vpsAdminOS node change
is part of this initiative.
