# Mandatory change review packet v36

## Outcome and acceptance criteria

Review the final four-layer component split and quiesced namespace-cutover
contract:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` independently consumes the same exact generic
runtime for its privileged host module. The generic repositories must contain
no case-insensitive `vpsfree` or `aitherdev` naming. Concrete site domains and
credentials come from the workspace consumer, host-only values remain in the
configuration repository, the final runtime exposes only generic namespaces,
and one exact workspace commit is retained solely as the reversible bridge.

Acceptance requires safe exact-head construction, strict cross-project
contracts, complete non-vacuous tests at provider and consumer boundaries,
reversible preservation of all migrated user/host/tmux data, retryable partial
operations, and an explicit deployment order that does not support mixed old
and new runtime processes.

Slug: `2026-09-09-workspace-components`

| Component | Base | Head |
|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `c3200c4497d39e7840690cd4b205efbdd389f0f4` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `295ed3cf80b52dfa9caa25fcf5ca9c9db8139274` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `1221833dd6f365a58c2a0de5328e49b03ce3d24e` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `d908b27c77aba249e3752c8e5a8cb9067a103d4a` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `cc2a7365e524bd1b81c3f6dffcea220fab7a2c36` |

All source changes are committed and pushed, all five project worktrees are
clean, and quick verification passes. Exact pins:

```text
workspace@d908b27 -> vpsfreecz/dev-workspace@1221833
  -> aither64/dev-workspace@295ed3c
  -> aither64/codex-web@c3200c4

configuration@cc2a736 -> aither64/dev-workspace@295ed3c
```

Compatibility source:
`24f0755ec812b34c943347343a011981b5792958`. The final workspace flake neither
constructs nor exports the bridge.

## v35 findings and remediation

- Generic runtime verification now permits a retained tmux server's original
  reported `#{socket_path}` only when the authority supplies a nonempty
  identity that exactly matches the connected live server. The selected new
  socket remains canonical and no old filesystem socket or alias is retained.
- Generic `dev-workspace` owns and exports
  `lib.runtimeAuthorityCorpus`, a schema-versioned manifest that names
  nonempty valid and invalid fixture sets. Its Go test rejects malformed,
  duplicate or path-bearing entries and validates every named fixture.
  Organization migration tests consume that exact pinned provider export and
  cannot skip or pass vacuously.
- The migration journal records every managed tmux value as an exact
  `[oldName, newName, originalValue, migratedValue]` tuple. Path-bearing values
  are translated forward, the original bytes are restored in reverse, and
  directional preflight/retry checks validate both states. Post-forward and
  post-reverse checks correlate rewritten authorities with the corresponding
  metadata view and live server.
- Every migrated ready authority must carry the live tmux identity before the
  journal is written. Extra path components no longer enter the authority or
  portal-manifest inventory. Live migration tests prove that the retained
  server reports its original internal socket while clients use the renamed
  socket, and that Codex, authority-directory and tmux-socket metadata migrate
  and restore exactly.
- The final workspace checker commit message now describes only the checker;
  organization pinning remains in the earlier dependency-selection commit.
- The configuration history contains one declaration, one untouched
  `confctl`-generated lock-only update from `f39f8e62` directly to
  `295ed3cf`, and two independent aitherdev module/configuration commits.

The prior Scope advisory remains an explicit decision: deployment inputs must
be direct immutable GitHub refs, and a `follows`/indirect topology must fail the
gate until its proof is deliberately updated. The retained filtered history is
intentional source provenance; only the focused initiative tail owns the new
organization behavior.

## Compatibility and deployment assumptions

This is an intentional quiesced namespace cutover; mixed old/new processes are
unsupported. The migration preserves paths, bytes, modes, ownership,
credentials, TLS material, profile generations, tmux session/window identities,
authorities and portal manifests. Durable partial operations are retryable.
The exact compatibility generation remains available until live acceptance.

No schema-4 journal has ever been deployed, so there is no predecessor journal
to upgrade. Rollback is permitted only while the journaled workspace, tmux and
host inventories remain frozen, and both locked reverse preflights must pass
before either scope mutates.

The user authorized aitherdev deployment, transient Codex-session restarts and
resetting development-cluster state. Deployment must use the feature
configuration worktree. Default-branch integration remains a separate
authorization boundary: the registered shared workspace root requires an
explicitly authorized fast-forward before the alias-free package can become
authoritative.

Deployment order is: build bridge and final outputs; validate every authority
and tmux identity; quiesce sessions and old non-tmux services; install the
bridge; stop services activation restarted; run both locked preflights; freeze
inventory; migrate user and host scopes; activate the host configuration; then
install the final user profile. Reverse uses the recorded bridge package and
exact original journal values.

## Ownership, public contracts and consumers

- `codex-web` owns the App Server client, browser integration, durable request
  protocol and reusable client security rules. Generic `dev-workspace` is its
  direct pinned consumer.
- Generic `dev-workspace` owns session/portal/profile/host runtime behavior,
  generic namespace and host paths, extension contracts, runtime-authority
  parsing/live verification, and the exported authority corpus. Its consumers
  are the organization package, workspace package through that organization
  pin, and the independent configuration host module.
- Organization `dev-workspace` owns vpsFree commands, skills, cluster
  providers, required site configuration and the private one-time migration.
  The migration helper, private packaging, runbook and tests are deliberately
  one introduction commit because none is useful or safely reviewable without
  the exact protocol it documents and verifies. The final dependency/corpus
  pin is an independent update commit.
- `vpsfree-cz-workspace` owns policy, records, concrete user-side site data,
  the immutable compatibility revision, final package selection and the
  deployment checker. Its source-removal, bridge, final namespace and checker
  commits are separate.
- `vpsfree-cz-configuration` owns privileged NixOS deployment values and host
  module activation. Its generated input update is isolated from the two
  hand-written aitherdev commits.

## Quick verification

- Generic: `CGO_ENABLED=0 go test ./internal/session` passed; the shared corpus
  checks all 3 valid and 7 invalid provider fixtures; `nix flake check
  --no-build` and `git diff --check` passed.
- Organization migration: `41` runs / `731` assertions, zero failures/errors/
  skips, using the provider manifest; Ruby syntax and `nix flake check
  --no-build` passed.
- Workspace: `nix flake check --no-build` passed. The live cross-worktree
  checker passed for `vpsfree-cz.workspace.aitherdev.int.vpsfree.cz` at generic
  revision `295ed3cf80b52dfa9caa25fcf5ca9c9db8139274`.
- Configuration: the required `confctl` update, Nixfmt and hooks passed;
  `nix flake check --no-build` passed and generated `.bin`/`.bundle` helpers
  are absent.
- Codex-web exact-head Actions `34512598834` is green. Replacement exact-head
  generic run `34551919708` and organization run `34552141719` are in progress;
  superseded organization run `34549692881` was cancelled.

Long full flake checks, the NixOS VM, exact bridge/final builds, aitherdev
configuration build and deployment dry activation remain deferred until this
review is clean.

## Review disposition and risk

Overall risk is **High**: this changes public cross-project Nix/runtime
contracts, persisted user and root state, credentials/TLS, systemd/tmux
topology, destructive migration, exact rollback behavior and host deployment.
Every lane uses `gpt-5.6-sol` with `xhigh` reasoning.

GitHub selected the organization feature branch as that new repository's
default. The current token cannot change it (HTTP 403). Neutral `master` exists
and all consumers pin immutable revisions; repository administration must
correct the default before normal integration.

The v35 remediation changes runtime-authority verification, a new exported
provider contract and consumer, journaled tmux transformation/rollback,
post-mutation verification, exact dependency pins and commit history. Rerun
General, Architecture, Scope and Risk.

## Non-goals and explicit decisions

- Do not support mixed old/new runtime processes.
- Do not upgrade a never-deployed journal.
- Do not infer or recreate a retained tmux server's old filesystem alias.
- Do not integrate a default branch without explicit authorization.
- Do not archive, delete or permanently retire the development session.
- Do not change vpsAdmin schemas, APIs, protocols or deployed vpsAdminOS nodes.
