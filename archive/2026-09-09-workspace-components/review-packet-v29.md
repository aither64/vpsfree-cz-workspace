# Mandatory change review packet v29

## Outcome and acceptance criteria

Review the strict four-layer split:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` separately consumes the generic host module. Both
generic repositories must contain no case-insensitive `vpsfree` or `aitherdev`.
Concrete domains and defaults belong to the workspace consumer. Organization
tools belong to `vpsfreecz/dev-workspace`.

The final package must have no old activation variable, user namespace, router
path, tmux metadata alias, or compatibility output. One immutable compatibility
package exists only at the exact workspace bridge commit.

## Exact review boundaries

Slug: `2026-09-09-workspace-components`

| Component | Base | Head |
|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `c3200c4497d39e7840690cd4b205efbdd389f0f4` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `ddba3ca9e3e59b01bf183d4a29ba76a7de06e28c` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `4dd1e546578458a81302bc13ddc903d676fdf339` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `2276ccd28dbda8dab638ec4c67d42844fceaa657` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `b85582eca7f7d24e0f52f46966695a08a739e2b2` |

Worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/`.
All exact heads are committed, pushed, clean, and descendant from the listed
bases. Range diffs pass `git diff --check`.

Exact dependency pins:

```text
workspace@2276ccd -> vpsfreecz/dev-workspace@4dd1e54
  -> aither64/dev-workspace@ddba3ca
  -> aither64/codex-web@c3200c4

configuration@b85582e -> aither64/dev-workspace@ddba3ca
```

The exact compatibility source is workspace commit
`5ef5845edca7038a4d58f7880148174da8eb7feb`. The final workspace flake exports
only `default` and `vpsfree-dev-workspace`; it neither constructs nor exports
the bridge.

## Commit organization

Generic hardening is separated into focused commits:

- `503b264` validates exact catalog shapes and reserved executable names;
- `635e5a9` validates runtime target types;
- `d772375` makes activation aliases immutable package metadata;
- `19200fa` switches profiles through the canonical default output;
- `ddba3ca` completes host-test extraction from `flake.nix`.

The organization tail has policy/license, extension package, migration, CI,
generic pin, exact site validator, and migration-preflight commits. Nontrivial
commits include rationale and compatibility bodies.

Workspace changes are separated into policy, site configuration, dependency,
mechanical source removal, exact bridge, and final namespace commits. The
67,000-line delegated-source removal is isolated from policy and configuration.

Configuration keeps its module and path changes, followed by a
`confctl`-generated update to the rewritten generic head.

## v28 findings and remediation

- Removed `migration-bridge` construction/export from final workspace source;
  the bridge remains only in `5ef5845`.
- Reserved `workspace-portal` against extension command collisions in Nix and
  runtime validators, with negative tests at both boundaries.
- Added exact organization site-config validation for top-level, KB endpoint,
  cluster-default, and workspace-configuration records. Inputs must be
  immutable JSON objects; tests reject mutable, wrong-shaped, and misspelled
  configurations through the public organization constructor.
- Migration now inventories and journals rewrite bytes before tmux keeper
  handoff or namespace moves. It validates ownership and every existing parent
  component first. End-to-end regressions prove wrong ownership and symlinked
  ancestors leave all three namespace roots unmoved and tmux unprepared.
- Split bundled generic/workspace commits and supplied rationale plus
  compatibility bodies for nontrivial rebuilt commits.
- Removed the contradictory deployment statement from the durable plan and
  updated stale push work.

## Compatibility and deployment gate

The migration is an intentional quiesced namespace cutover; mixed old/new
runtimes are unsupported. The helper records exact path identities, bytes,
metadata and package generations, supports retry, inventories active and
archived portal manifests, and permits reverse only with the final generation
selected and the recorded bridge immediately available as the previous profile.

The user authorized aitherdev deployment, transient Codex-session restarts, and
resetting the current development cluster. Default-branch integration remains
separately governed. The registered shared root still uses old policy and
source-local commands, so final deployment is gated on explicit authorization
to fast-forward this workspace branch into local shared `master`.

Generic `workspace-host` and `workspace-portal` output aliases remain published,
organization-neutral compatibility names. New switching uses the default output.
The final organization workspace does not expose them; the exact bridge does
because the deployed predecessor builds `#workspace-portal`.

## Quick verification

- Generic runtime tests: 71 runs, 446 assertions, no failures; no-build flake
  evaluation passes.
- Organization migration tests: 13 runs, 123 assertions, no failures; no-build
  flake evaluation passes.
- Exact bridge and final workspace no-build evaluations pass.
- Configuration pin update was generated and committed through `confctl`; all
  repository hooks passed.
- Generic forbidden-name scans remain empty. `codex-web@c3200c4` CI was green
  before the dependency-history rewrite; new generic and organization CI runs
  were triggered by the pushed v29 heads.

Long full package checks, the NixOS VM, exact bridge/final package builds,
aitherdev configuration build, and live migration remain deferred until this
review is clean.

## Risk and required lanes

Overall risk is **High** because this changes public cross-project contracts,
user/root persisted state, credential and TLS paths, systemd topology,
destructive migration ordering, deployment, and exact rollback. Run General,
Architecture, Scope, and Risk with `gpt-5.6-sol` at `xhigh`.

## Non-goals

- Do not support mixed old/new runtime processes.
- Do not integrate a default branch without explicit authorization.
- Do not archive, delete, or permanently retire the development session.
- Do not change vpsAdmin schemas, APIs, protocols, or deployed vpsAdminOS nodes.
