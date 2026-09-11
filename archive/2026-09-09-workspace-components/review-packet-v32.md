# Mandatory change review packet v32

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
no case-insensitive `vpsfree` or `aitherdev` naming. Concrete domains,
credentials, commands, skills and cluster providers remain in consumers. The
final user package has only generic namespaces; one exact workspace commit is
the immutable compatibility source used solely for the journaled cutover and
rollback.

## Exact review boundaries

Slug: `2026-09-09-workspace-components`

| Component | Base | Head |
|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `c3200c4497d39e7840690cd4b205efbdd389f0f4` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `a6713badeec5afcbf22c6375eb0480417bda79d5` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `bc337355fa63c7568bdb63a227bb4c498fac424b` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `7c1ea44bf2ce13b97dc1c4c23b8f4f1bb160fefd` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `ebc3de33fb1693098563764b8ca241c0c3fd7c36` |

All worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/`.
All changes are committed and pushed, every worktree is clean, and
`git diff --check` passes.

Exact dependency pins:

```text
workspace@7c1ea44 -> vpsfreecz/dev-workspace@bc33735
  -> aither64/dev-workspace@a6713ba
  -> aither64/codex-web@c3200c4

configuration@ebc3de33 -> aither64/dev-workspace@a6713ba
```

The exact compatibility source is workspace commit
`2fb148f32e28e5c7b616dfa73ce6669a22ade04d`. The final flake neither
constructs nor exports that bridge.

## v31 findings and remediation

- Migration schema 4 now journals both the presence and absence of every
  managed tmux option and environment entry for the frozen session/window
  inventory. Reverse preflight rejects metadata added during the rollback
  window, with regressions for late session and window additions.
- The generic v31 remediation was split into owning commits. Host-path exports
  live with the host module, user-state propagation lives with namespace
  support, home-link cleanup lives with activation behavior, tmux socket
  identity lives with runtime behavior, and the documentation correction is a
  dedicated documentation commit.
- Portal lifecycle receipts, completed-removal state and `dev-session` delete
  recovery all derive from one explicit namespace state root. A cross-language
  regression proves a non-default namespace reaches the Go operation store and
  Ruby deletion recovery consistently.
- The generic package constructor derives the router socket from
  `lib.hostPaths.routerSocket`; the lower portal builder requires that value
  instead of owning another default. Generic and organization package-metadata
  tests prove the effective router socket equals the exported host contract.
- The immutable compatibility source is the actual workspace commit
  `2fb148f32e28e5c7b616dfa73ce6669a22ade04d`, and every downstream pin and
  deployment-check input was regenerated after the history rewrite.
- Migration journals the tmux server socket's device, inode, owner, type and
  nanosecond ctime. It rejects socket symlinks, symlinked ancestors and a
  socket replaced after preparation before keeper handoff or metadata writes.
- Migration serializes and enforces the 16 MiB journal ceiling before the
  atomic write, so it cannot create durable state which its own loader rejects.
  A regression constructs an aggregate oversized inventory.
- Generic stale-socket cleanup probes the exact UNIX socket directly with a
  bounded wait and rechecks its identity before unlink. It no longer infers
  liveness from a particular keeper session, and a live unrelated-server
  regression prevents deletion.

## Compatibility and deployment assumptions

This is an intentional quiesced namespace cutover. Mixed old/new processes are
unsupported. The migration preserves exact path identities, bytes, metadata,
profile generations, tmux session/window identities, authorities, manifests,
credentials and TLS material; partial durable operations are resumable. The
old compatibility generation remains available until live acceptance passes.

No migration journal from this feature has been deployed, so schema 4 needs no
upgrader. Rollback is permitted only while the journaled workspace, tmux and
host inventories remain frozen. Reverse migration requires both locked,
read-only scope preflights before either scope mutates.

The user authorized aitherdev deployment, transient Codex-session restarts and
resetting the running development cluster. Default-branch integration remains
unauthorized. The configuration must deploy from its feature worktree. The
registered shared workspace root still requires separately authorized
fast-forward integration before the final alias-free package can become its
authoritative policy and metadata.

## Commit structure

- `codex-web`: client/security contracts, protocol compatibility, standalone
  example and CI are split by owning behavior.
- Generic `dev-workspace`: extraction, namespace/runtime behavior, host module,
  activation, tests/docs and CI are functional commits. The v31 follow-up is
  folded or split by the subsystem that owns each contract.
- Organization `dev-workspace`: extracted tools/providers/skills, validated
  package, migration/runbook, CI and review remediations are functional
  commits. The latest migration commit contains one coherent schema-4 frozen
  inventory and journal-safety change with its tests and runbook.
- Workspace: policy, concrete site data, dependency selection, source removal,
  immutable bridge, final namespace and deployment checker are separate.
- Configuration: the one final `confctl`-generated input update follows the
  host-module configuration commits; the superseded intermediate pin was
  removed without editing the generated final message.

## Quick verification

- Generic runtime: workspace-host `74` runs / `457` assertions and dev-session
  `285` runs / `2,852` assertions, all green. Focused Go session, web and portal
  command packages pass with module mode in the Nix shell.
- Organization migration: `31` runs / `358` assertions, all green. Its
  no-build flake evaluation includes the package metadata and compatibility
  package checks.
- Workspace deployment checker: `2` runs / `9` assertions; the live
  cross-worktree check passes for the exact domain and `a6713ba` pin. Workspace
  and configuration no-build flake evaluations pass.
- Configuration changes used `confctl inputs channel set --commit`; Nixfmt and
  commit hooks passed, and generated `.bin`/`.bundle` helpers were removed.
- `codex-web` exact-head Actions run `34512598834` is green. Current generic
  run `34539084838` and organization run `34539152574` are in progress.
  Superseded organization run `34535187363` accepted cancellation. The generic
  token returned HTTP 403 when cancelling superseded run `34534735689`.

Long full package checks, the NixOS VM, exact bridge/final builds, aitherdev
configuration build and live cutover remain deferred until this review is
clean.

## Review disposition carried forward

- GitHub selected the organization feature branch as the repository default.
  The current token cannot change it (HTTP 403). Neutral `master` exists and
  all consumers pin an explicit immutable feature revision, so this has no
  runtime or deployment effect; repository administration must change the
  default before normal integration.
- The retained older generic hardening commit spans related catalog and
  migration boundaries. Further history churn would not improve the current
  ownership or deployment contract; the v31 catch-all follow-up itself was
  split as required.
- The small organization CI commit's concise message accurately describes its
  single workflow addition. No runtime or compatibility behavior is hidden in
  that commit.

## Risk and lanes

Overall risk is **High** because the work changes public cross-project
contracts, persisted user/root state, credentials and TLS paths, systemd/tmux
topology, destructive migration and rollback ordering, and host deployment.

The v31 remediations change namespace state ownership, socket identity,
rollback inventory and commit structure. Rerun General, Architecture, Scope
and Risk with `gpt-5.6-sol` at `xhigh`.

## Non-goals and decisions

- Do not support mixed old/new runtime processes.
- Do not upgrade a never-deployed migration journal.
- Do not integrate a default branch without explicit authorization.
- Do not archive, delete or permanently retire the development session.
- Do not change vpsAdmin schemas, APIs, protocols or deployed vpsAdminOS nodes.
