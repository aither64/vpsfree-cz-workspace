# Mandatory change review packet v31

## Outcome and acceptance criteria

Review the final four-layer split:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` separately consumes the same exact generic runtime
for its privileged host module. `codex-web` and generic `dev-workspace` contain
no case-insensitive `vpsfree` or `aitherdev`. Concrete domains, credentials and
organization behavior remain in their consumers. The final user package has
only generic namespaces; one exact workspace bridge commit retains the old
namespace solely for the journaled cutover and rollback.

## Exact review boundaries

Slug: `2026-09-09-workspace-components`

| Component | Base | Head |
|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `c3200c4497d39e7840690cd4b205efbdd389f0f4` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `868826dfac6ec6348e53bb15383af83985087f59` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `5243d50be84d4773df0eaa3e9a90e3be865a30b7` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `83d14b711717f261ed92bb07a62516b6998738b1` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `55b87faf5935b9a34aeb841164835c895b4fce21` |

All worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/`.
All changes are committed and pushed, every worktree is clean, and
`git diff --check` passes.

Exact dependency pins:

```text
workspace@83d14b7 -> vpsfreecz/dev-workspace@5243d50
  -> aither64/dev-workspace@868826d
  -> aither64/codex-web@c3200c4

configuration@55b87fa -> aither64/dev-workspace@868826d
```

The compatibility source is workspace commit
`ae19c907e50d27e264b6160967228748faf1aa74`. The final flake neither constructs
nor exports that bridge.

## v30 findings and remediation

- Generic `dev-session` treats its explicitly configured absolute tmux socket
  as canonical. A real test renames the containing directory and proves tmux's
  stale internal `#{socket_path}` cannot leak back into authority state.
- Generic `workspace-host` removes only the exact obsolete
  `~/bin/workspace-portal -> $profile/bin/workspace-portal` link and preserves
  unrelated links. Tmux shutdown verifies inode identity and server absence
  before unlinking a socket left behind by a runtime-directory rename.
- Tmux migration now distinguishes session options from window options. Schema
  4 journals every session and window ID, migrates `session_window` and
  `session_worktree` with window-scoped commands, and tests duplicate durable
  retry states in both directions.
- `preflight --direction reverse` loads the retained user or host journal and
  performs the same locked, read-only checks needed by rollback. The runbook
  requires both reverse preflights before either scope is reversed.
- The forward journal is not created until move, profile, rewrite and tmux
  preparation has succeeded under the mutation locks. A failed preparation can
  be corrected and retried without a stale snapshot.
- Every candidate registry, authority and active or archived portal manifest is
  journaled even when its bytes need no rewrite. Reverse rejects any added or
  deleted candidate, tmux server, session or window before handoff or mutation.
  The documented rollback window freezes state-producing operations.
- Generic host defaults have one owner in `nix/host-paths.nix` and are exported
  through `lib.hostPaths`. The organization migration loads one JSON target
  contract and its flake asserts exact equality with the pinned generic owner.
  Aitherdev removes duplicated path overrides and therefore consumes the
  module defaults directly.
- Aitherdev portal names now live in one directly evaluable site file.
  `bin/check-dev-workspace-deployment` in the coordination workspace compares
  that identity with `.dev-workspace.json` and proves that the final user
  package and host configuration lock the same generic runtime.
- The generic extension documentation shows the real nested `extensions`
  constructor. The earlier workspace dependency commit no longer claims that
  source selection alone preserves runtime behavior; it explicitly defers
  activation to the later bridge.

## Compatibility and deployment assumptions

This is an intentional quiesced namespace cutover. Mixed old/new processes are
unsupported. The migration preserves exact path identities, bytes, metadata,
profile generations, tmux session/window identities, authorities, manifests,
credentials and TLS material; partial durable operations are resumable. The
old compatibility generation remains available until live acceptance passes.

No schema-3 migration journal has been deployed, so the branch directly
introduces schema 4 without a journal upgrader. Rollback is permitted only
while the journaled workspace, tmux and host inventories remain frozen.

The user authorized aitherdev deployment, transient Codex-session restarts and
resetting the running development cluster. Default-branch integration remains
unauthorized. The configuration must deploy from its feature worktree. The
registered shared workspace root still requires a separately authorized
fast-forward before the final alias-free package can become authoritative.

## Commit structure

- `codex-web`: public client/security contracts, protocol compatibility,
  standalone example, and CI are split by owning behavior.
- Generic `dev-workspace`: extraction, namespace/runtime behavior, host module,
  tests/docs, workflows, and the latest transition-identity remediation are
  focused commits. The final remediation combines the canonical socket, stale
  link/socket cleanup and exported host defaults because they are one generic
  namespace-transition contract.
- Organization `dev-workspace`: extracted tools/providers/skills, validated
  extension package, migration/runbook, CI, and review remediations are
  functional commits. The latest commit combines schema-4 migration behavior,
  tests, runbook and its exact generic pin because the target-path equality
  assertion cannot evaluate or operate against the predecessor pin.
- Workspace: policy, concrete site data, dependency selection, source removal,
  immutable bridge, final namespace and deployment checker are separate.
- Configuration: the generated input commits remain unedited and separate from
  host-module configuration. The aitherdev defaults/site-file change is one
  host configuration commit.

## Quick verification

- Generic runtime: workspace-host `73` runs / `454` assertions and dev-session
  `285` runs / `2852` assertions, all green; no-build flake evaluation passes.
- Organization migration: `27` runs / `313` assertions with live tmux coverage,
  all green. Its packaged Nix test derivation passes every tool suite (one
  supplementary-group test is skipped in the Nix build sandbox).
- Workspace deployment checker: `2` runs / `9` assertions; the live
  cross-worktree check passes for the exact domain and `868826d` pin. Workspace
  and configuration no-build flake evaluations pass.
- Configuration changes used `confctl inputs channel set --commit`; Nixfmt and
  commit hooks passed, and generated `.bin`/`.bundle` helpers were removed.
- `codex-web` exact-head Actions run `34512598834` is green. Current generic
  run `34534735689` and organization run `34535187363` are in progress.
  Superseded organization run `34531031684` accepted cancellation. The generic
  repository token still returns HTTP 403 when cancelling superseded run
  `34529633403`.

Long full package checks, the NixOS VM, exact bridge/final builds, aitherdev
configuration build and live cutover remain deferred until this review is
clean.

## Risk and lanes

Overall risk is **High** because the work changes public cross-project
contracts, persisted user/root state, credentials and TLS paths, systemd/tmux
topology, destructive migration and rollback ordering, and host deployment.

The v30 remediations expand the migration schema, rollback preflight, inventory
contract and cross-project deployment check. Rerun General, Architecture,
Scope and Risk with `gpt-5.6-sol` at `xhigh`.

## Non-goals and decisions

- Do not support mixed old/new runtime processes.
- Do not upgrade a never-deployed schema-3 migration journal.
- Do not integrate a default branch without explicit authorization.
- Do not archive, delete or permanently retire the development session.
- Do not change vpsAdmin schemas, APIs, protocols or deployed vpsAdminOS nodes.
