# Mandatory change review packet v26

## Requested outcome and acceptance criteria

Complete the strict four-layer split:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` separately consumes the generic host module.

Acceptance requires:

- current tracked trees of `aither64/codex-web` and
  `aither64/dev-workspace` have no case-insensitive `vpsfree` or `aitherdev`;
- their published history is preserved;
- generic runtime environment variables, state paths, Ruby constants and tmux
  metadata use the new namespace with no runtime aliases;
- generic cluster integration is a strictly validated immutable extension
  catalog rather than built-in vpsAdmin conditionals;
- the large host checks live outside generic `flake.nix`;
- `vpsfreecz/dev-workspace` owns the KB commands, all previously bundled
  skills, both cluster providers, and a one-time reversible migration helper;
- the organization repository contains no case-insensitive `aitherdev`;
- concrete endpoints, credential paths, cluster defaults and portal hostnames
  come from `vpsfree-cz-workspace`;
- both generic repositories retain complete flake-check workflows and the new
  organization repository adds one using current official action releases;
- old and new runtime versions do not coexist. Forward and reverse cutovers
  are explicit operator actions after all conversations and lifecycle
  operations are quiesced.

## Initiative and repository boundaries

Slug: `2026-09-09-workspace-components`

Plan and state:

- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/plan.md`
- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/state.md`

Repositories:

| Component | Review base | Head | Worktree |
|---|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `6cc18a3257d31d454bc12e7554c8c5db84deca61` | `worktrees/2026-09-09-workspace-components/codex-web` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `8cccdf06fffea8540f767b3cb0402bb358694303` | `worktrees/2026-09-09-workspace-components/dev-workspace` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `51ee4295268071044088ce9fce78f80f3dc5eff3` | `worktrees/2026-09-09-workspace-components/vpsfree-dev-workspace` |
| workspace | `26606cfa0134ce3680cf592f9ab3c345683fbdc2` | `905b10ac91f4e9a2915925fa57a091af2290b8a6` | `worktrees/2026-09-09-workspace-components/workspace` |
| configuration | `7481618dacab04bfd5b09bc730c373c2d2bf14d7` | `76b29bb14df9659cca8918cf239ee34958864e2c` | `worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration` |

The organization repository's neutral `master` root is its review base. The
feature branch contains 134 path-filtered historical commits replayed from the
generic repository, followed by `51ee429`. That history is intentional source
provenance, not a claim that each historical filtered snapshot is independently
buildable.

## Commit shape

- `codex-web`: the five existing implementation commits remain published;
  `6cc18a3` removes deployment-specific names from the final tree.
- generic `dev-workspace`: previously published feature history remains intact.
  `4ee9168` preserves the independent host preflight hardening,
  `a620db4` performs the ownership split and namespace break, and `8cccdf0`
  makes the catalog derivation-safe after downstream evaluation exposed the
  Nix restriction.
- organization `dev-workspace`: filtered provenance is retained, while
  `51ee429` is one cross-cutting package boundary commit. Its source moves,
  wrapper configuration, provider catalog, migration, tests and documentation
  are inseparable because no partial subset provides a usable organization
  package.
- workspace: the prior two consumer commits remain; `905b10a` supplies the
  complete site configuration and organization pin.
- configuration: the generated `98b4c67b` commit is exactly the `confctl`
  input update; `76b29bb1` changes only the host paths. Do not reformat the
  generated commit message.

Some retained generic commits describe the superseded combined package. The
user explicitly prohibited published-history rewriting, so the final ownership
boundary is introduced additively rather than rewriting those commits.

## Public interfaces and ownership

- `codex-web` owns the reusable Go/browser Codex App Server integration. Its
  test-only binary variable is `CODEX_WEB_TEST_BINARY`.
- generic `dev-workspace` owns session, portal, profile and host behavior. Its
  public variables are `DEV_SESSION_*`, `DEV_WORKSPACES_*`,
  `DEV_WORKSPACE_NAME`, `DEV_WORKSPACE_HOST_MODE`, `DEVCLUSTER_WORKSPACE`, and
  `DEV_SESSION_LIFECYCLE_*`. Tmux uses `@dev_session*`.
- generic `dev-workspace.lib.mkPackage { pkgs; extensions; }` owns catalog
  validation and derives command, skill and provider wrappers from one catalog.
  Provider IDs, labels and executable paths come from the immutable package;
  workspace manifests select only IDs.
- `vpsfreecz/dev-workspace.lib.mkPackage { pkgs; siteConfig; }` owns KB and
  cluster packaging. Required site configuration includes both production and
  staging KB endpoints, credential paths, staging identity/container helper,
  and both default cluster JSON paths.
- `vpsfree-cz-workspace` is the only consumer found for the organization
  package. It supplies those concrete values, selects `vpsadmin` and
  `vpsadminos`, and declares the portal hostname/alias in workspace schema 2.
- `vpsfree-cz-configuration` consumes generic `dev-workspace@8cccdf0` for the
  privileged NixOS host module and supplies TLS, nginx, firewall and DNS
  configuration.

Exact dependency pins:

```text
workspace@905b10a -> vpsfreecz/dev-workspace@51ee429
  -> aither64/dev-workspace@8cccdf0
  -> aither64/codex-web@6cc18a3

configuration@76b29bb -> aither64/dev-workspace@8cccdf0
```

## Namespace migration and compatibility

This is deliberately incompatible. There are no legacy environment, tmux,
path, package-output, or provider aliases in the new runtime.

The organization helper has separate `user` and `host` scopes so the user
scope can update an owner-checked tmux server without running as root. Both
scopes require `--yes`, use private locked journals, reject occupied targets,
symlink roots and mount trees, recover a rename interrupted before its journal
update, and provide an exact reverse operation.

The user scope moves config, state and runtime roots; locks lifecycle files;
rewrites live authority JSON and active `work/*/portal.yml` paths; and renames
tmux session options/environment. Rewrites retain original bytes in the private
journal and reverse refuses files modified after cutover.

The host scope moves the password, htpasswd, CA, TLS, public CA, router and lock
state. Renames stay on their original filesystems and preserve inode metadata.
Tests verify contents and modes before and after exact reversal. The migration
is not run automatically by either package or activation.

Deployment order is Codex source pin, generic runtime, organization package,
workspace package, host configuration and user profile. Operators must quiesce
all conversations and lifecycle operations, stop affected services, run both
migration scopes, activate the new host/profile generations, and verify the
retained identities. Rollback stops the new services, reverses user and host
journals, selects the old generations and verifies the old paths before restart.

Mixed old/new operation is unsupported. Journals remain private until the user
accepts the deployment.

## Quick verification completed

- `codex-web`: `CGO_ENABLED=0 go test ./...`; complete
  `nix flake check --print-build-logs`; case-insensitive forbidden-name scan.
- generic `dev-workspace`: Ruby syntax; `CGO_ENABLED=0 go test ./...`;
  `ruby test/dev_session_test.rb` (284 runs); `ruby test/workspace_host_test.rb`
  (65 runs); `nix flake check --no-build`; complete generic package and source
  check build; case-insensitive forbidden-name scan.
- organization `dev-workspace`: all five inherited Ruby suites plus migration
  tests; migration has 5 runs and 51 assertions including live tmux reversal;
  package/source/test derivations all built successfully; no `aitherdev` match.
- workspace: no-build flake evaluation and complete concrete package build.
- configuration: exact input changed only with
  `confctl inputs channel set --commit`; formatting/commit hooks passed;
  `nix flake check --no-build --show-trace` passed.
- `codex-web` exact-head GitHub Actions succeeded. Generic and organization
  exact-head workflows are still running. Cancellation of the superseded
  generic run was attempted and rejected with HTTP 403 due token permissions.

## Risk and review lanes

Overall risk: **High**. The work intentionally breaks public runtime names,
moves user and privileged persisted state, touches credential/TLS material,
changes cross-project package composition, and relies on ordered deployment and
exact reversal.

Run all lanes with `gpt-5.6-sol` and `xhigh` reasoning:

- General
- Architecture and repetition
- Scope and proportionality
- Risk and compatibility

## Non-goals and explicit decisions

- No default-branch integration, release, deployment, session archival,
  deletion or stopping is authorized by this review.
- No vpsAdmin database/API/daemon protocol or deployed vpsAdminOS node change.
- No legacy runtime aliases or mixed-version compatibility period.
- Do not rewrite published generic repository history.
- Historical prose and archived/recovery records are not mass-rewritten.
- `vpsfreecz/dev-workspace` must not contain personal host naming; concrete
  values stay in the workspace/configuration layers.
- A reverse migration and previous generations are the rollback mechanism.

Known external repository metadata issue: GitHub selected the feature branch as
the new organization repository's default branch during its initial concurrent
push. The token receives HTTP 403 when changing it to the neutral `master`.
This does not affect Git refs or package pins, but must be corrected by an owner
before normal integration.
