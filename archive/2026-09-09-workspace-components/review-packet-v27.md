# Mandatory change review packet v27

## Requested outcome and acceptance criteria

Complete the strict four-layer split:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` separately consumes the same generic host module.
Acceptance requires the following:

- `codex-web` and generic `dev-workspace` have no case-insensitive `vpsfree`
  or `aitherdev` in their current tracked trees, and flake checks enforce it;
- generic runtime variables, paths, Ruby constants and tmux metadata use the
  new names, with no organization naming in generic source;
- generic cluster behavior uses a strictly validated immutable extension
  catalog and generic package constructor;
- Nix host, catalog and namespace tests live under `nix/tests/`, while
  `flake.nix` only wires them;
- `vpsfreecz/dev-workspace` owns KB commands, skills, cluster providers,
  embedded workspace configuration and the one-time reversible migration;
- concrete endpoints, credential paths, cluster defaults and portal domains
  come from `vpsfree-cz-workspace`;
- all three reusable repositories run full flake checks in GitHub Actions;
- the final runtime contains no legacy aliases. A package-selected
  compatibility profile exists only to bootstrap the quiesced migration and
  exact rollback.

## Initiative and repository boundaries

Slug: `2026-09-09-workspace-components`

Plan and state:

- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/plan.md`
- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/state.md`

| Component | Review base | Head | Worktree |
|---|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `c3200c4497d39e7840690cd4b205efbdd389f0f4` | `worktrees/2026-09-09-workspace-components/codex-web` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `6279fbf239b0979a97abd40a20be2cc7ae326f8b` | `worktrees/2026-09-09-workspace-components/dev-workspace` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `0f8440dd4939f5822e58e3df08611cb81338478c` | `worktrees/2026-09-09-workspace-components/vpsfree-dev-workspace` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `fd886d3fbee0ccae41cb58b7bb404f3cf59d20f5` | `worktrees/2026-09-09-workspace-components/workspace` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `b9275c30387a1c1f0a6bc5ee73b1b5ea6f32b108` | `worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration` |

All five merge-base checks equal the listed bases. All five worktrees are
clean and all five commit-range `git diff --check` commands pass. The first
three heads are pushed. Workspace and configuration histories were rewritten
after v26 and remain local until this review is reconciled.

## Commit shape

- `codex-web` retains its published feature commits. `6cc18a3` removes the
  deployment-specific names and `c3200c4` independently adds the generic-tree
  regression check.
- Generic `dev-workspace` retains published feature history. `a620db4` owns
  the namespace and extension split; `8cccdf0` permits Nix-store extension
  paths; `be33279` hardens catalog, test isolation and lifecycle boundaries;
  `e3173a9` rejects mutable extension targets; `4c6b62a` parameterizes the
  compatibility namespace/router; and `6279fbf` adds a validated list of
  activation aliases supplied by the consumer package.
- The organization feature follows 134 filtered provenance commits. Its new
  work is split into independently reviewable commits: `1d7060a` packages the
  organization extensions, `43e442b` introduces the migration and tests,
  `4b99055` embeds workspace configuration, `f14d064` fixes retry locking,
  `0b46a03` exposes the compatibility package constructor, and `0f8440d`
  requires the exact rollback bridge generation.
- Workspace commits separately delegate package ownership (`0c493a5`), add
  concrete site configuration (`cfc74cf`), select the compatibility package
  (`ee0c0d6`), and select the final generic namespace (`fd886d3`). The exact
  compatibility source is retained as a commit, not a floating expression.
- Configuration commits separately register the channel (`dba155a5`), adopt
  the reusable host module (`6d7cbf1`), switch persisted paths (`a2330e8`),
  and apply the one final generated `confctl` pin (`b9275c3`). Superseded pin
  commits were consolidated without changing the final tree or generated
  final message.

## Public interfaces, ownership and consumers

- `codex-web` owns the reusable Go/browser Codex App Server integration.
- Generic `dev-workspace` owns sessions, portals, profiles and the NixOS host.
  Public variables use `DEV_SESSION_*`, `DEV_WORKSPACES_*`,
  `DEV_WORKSPACE_NAME`, `DEV_WORKSPACE_HOST_MODE`, `DEVCLUSTER_WORKSPACE` and
  `DEV_SESSION_LIFECYCLE_*`; tmux uses `@dev_session*`.
- `dev-workspace.lib.mkPackage` validates one package-owned extension catalog.
  Extension commands/skills/configuration paths must be Nix-store backed.
  Provider IDs are their state-directory identities. The constructor accepts
  `userNamespace`, `routerSocket` and a validated
  `activationEnvironmentAliases` list; the generic defaults remain generic.
- `vpsfreecz/dev-workspace.lib.mkPackage` is the only current caller using the
  compatibility parameters and supplies the former activation variable. It
  owns organization commands, skills and providers and accepts concrete site
  configuration from its consumer.
- `vpsfree-cz-workspace` is the only discovered organization-package consumer.
  Its immutable package embeds `.dev-workspace.json`, KB endpoints, credential
  references, cluster defaults and portal domains. The shared registered root
  therefore need not integrate the feature before deployment.
- `vpsfree-cz-configuration` is the host-module consumer. It supplies nginx,
  TLS, firewall, DNS and persisted host-path values.

Exact dependency pins:

```text
workspace@fd886d3 -> vpsfreecz/dev-workspace@0f8440d
  -> aither64/dev-workspace@6279fbf
  -> aither64/codex-web@c3200c4

configuration@b9275c3 -> aither64/dev-workspace@6279fbf
```

## Compatibility, migration and deployment

This is an intentional incompatible namespace change. Final old/new runtime
coexistence is unsupported. The organization helper requires a workspace root,
inventories machine-consumed manifests, locks runtime and fallback lifecycle
locks in both directions, validates every path before mutation, journals exact
bytes and metadata, and recovers durable forward/reverse boundaries.

The user migration hands the live tmux server between explicit old and new
systemd keeper drop-ins. The host migration preserves content, modes, owners,
groups and symlink targets for password, auth, CA, TLS and public-CA state.
Neither migration runs automatically.

The existing profile is first switched from workspace commit `ee0c0d6`, whose
default output retains `vpsfree-workspaces` and the old router but accepts the
old activation variable through the organization package. The helper records
that exact package path and metadata digest. After quiescence, both migration
scopes run, the new host generation is activated, and the moved compatibility
profile switches to final workspace commit `fd886d3` using explicit generic
namespace/router values. Reverse refuses to proceed unless the previous
profile generation is the exact recorded compatibility package.

The complete command sequence is in
`vpsfree-dev-workspace/docs/namespace-migration.md`. Journals remain private
until user acceptance. No migration, deployment or default-branch integration
has started.

## Review-v26 remediation and quick verification

The v26 General, Scope and Risk findings were reconciled as follows:

- provider lifecycle checks now use only generic runtime variables/defaults;
- organization package, migration and compatibility work are separate commits;
- workspace and configuration consumers are rebased onto current bases;
- both generic trees enforce the forbidden-name check;
- Nix and runtime catalog validation share length/immutability boundaries;
- the lock path is consistently `/run/lock/dev-workspace-substrate.lock`;
- migration coverage now includes mounts, malformed authorities, unsafe
  portals, exact metadata, durable retry boundaries and top-level help;
- reverse rewrites and moves are retryable and both directions lock all
  lifecycle locations;
- real systemd keeper handoff is simulated with a systemctl/tmux integration
  fixture;
- ambient delete recovery is isolated from the developer's XDG state;
- workspace configuration is embedded in the package;
- public partial-migration flags were removed;
- migration wrappers include tmux;
- rollback requires the recorded compatibility generation.

Quick checks at the final heads:

- `codex-web`: complete Go/browser and flake checks passed after the source
  boundary check was added; the forbidden-name scan is empty.
- generic `dev-workspace`: focused Ruby tests passed (5 runs, 12 assertions),
  `nix flake check --no-build --show-trace` passed, and
  `nix build .#checks.x86_64-linux.user-namespace --no-link
  --print-build-logs` passed while running the embedded 284/2715 and 71/434
  package suites; the forbidden-name scan is empty.
- organization `dev-workspace`: `ruby test/migration_test.rb` passed with 11
  runs and 97 assertions; `nix flake check --no-build` and `git diff --check`
  passed; the forbidden-name scan is empty.
- workspace: both final and migration-bridge packages built before the final
  rollback metadata assertion; the exact final tree passes no-build flake
  evaluation.
- configuration: the final tree is byte-identical to the tree produced by the
  last `confctl inputs channel set --commit`; hooks and exact-tree no-build
  flake evaluation passed.

Long full component checks, both exact workspace package builds and the
aitherdev configuration build are deliberately deferred until this review.

## Risk and selected lanes

Overall risk is **High**: this changes public cross-project contracts, user and
root persisted state, credential/TLS locations, service management, deployment
ordering and exact rollback behavior. Use `gpt-5.6-sol` at `xhigh` for all four
required lanes:

- General
- Architecture and repetition
- Scope and proportionality
- Risk and compatibility

## Non-goals and explicit decisions

- Do not rewrite published generic repository history.
- Do not add legacy aliases to the final runtime or support rolling mixed
  versions. The compatibility package is restricted to cutover bootstrap.
- Do not integrate any default branch, release, archive, delete or stop the
  session. Deployment to aitherdev is authorized only after review/build gates.
- Do not change vpsAdmin databases, APIs, daemon protocols or deployed
  vpsAdminOS nodes.
- Do not move privileged TLS/nginx/firewall/DNS values out of configuration or
  concrete domains into either generic repository.
- Historical prose and archived/recovery records are not mass-rewritten.

Known external metadata issue: GitHub selected the organization feature branch
as the repository default during its initial concurrent push. The available
token receives HTTP 403 when changing it to neutral `master`. This does not
change Git refs or package pins, but an owner must correct it before normal
default-branch integration.
