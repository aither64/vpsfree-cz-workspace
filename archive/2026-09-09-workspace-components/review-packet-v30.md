# Mandatory change review packet v30

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
tools and the one-time namespace migration belong to `vpsfreecz/dev-workspace`.

The final package has no old activation variable, user namespace, router path,
tmux metadata alias, or compatibility output. One immutable compatibility
package exists only at the exact workspace bridge commit.

## Exact review boundaries

Slug: `2026-09-09-workspace-components`

| Component | Base | Head |
|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `c3200c4497d39e7840690cd4b205efbdd389f0f4` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `ee4e282bdab641186e8bbdc268600d248b44d3e0` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `e399c8601af888e704ac2aea9ad9ddeb56c3cfea` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `7bd8f5c0789cfcf7adb8ea9a2b6f2689d98c91bd` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `031104a6e4ccad6783e9feccb255aa0457b27f10` |

All worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/`.
Every exact head is committed, pushed, clean, descendant from its listed base,
and passes `git diff --check`.

Exact dependency pins:

```text
workspace@7bd8f5c -> vpsfreecz/dev-workspace@e399c86
  -> aither64/dev-workspace@ee4e282
  -> aither64/codex-web@c3200c4

configuration@031104a -> aither64/dev-workspace@ee4e282
```

The exact compatibility source is workspace commit
`5cfcd61d6879eb1821ff71dcec97181f22f1f517`. The final workspace flake exports
only `default` and `vpsfree-dev-workspace`; it neither constructs nor exports
the bridge.

## v29 findings and remediation

- Separated public home commands from reserved package executables. The runtime
  reserves `workspace-portal` against extension collisions but links only
  `workspace-host` and `dev-session` into `~/bin`; tests preserve an unrelated
  `workspace-portal` symlink and check both contracts independently.
- Consolidated the organization and configuration generic-runtime pins into
  their original dependency commits. Each retained history now contains one
  dependency-update stream with the final `ee4e282` revision.
- Any occupied legacy registry path is inventoried and must be an owned regular
  file. Directory, dangling-symlink and directory-symlink regressions prove the
  migration leaves all namespace roots and tmux preparation untouched.
- Added a complete move preflight in both directions before any handoff,
  rewrite, or rename. It validates every source/destination state, identity,
  fingerprint where stable, mount tree and parent chain as one gate and repeats
  the validation after mutation locks are acquired.
- Reverse validates every rewrite's bytes and exact metadata before keeper or
  tmux mutation. A live-keeper regression proves a changed late rewrite leaves
  the keeper PID, generic tmux metadata, sockets, files, and roots unchanged.
- The canonical user profile transition lock is now required and acquired
  before profile selection is verified. Tests cover an absent lock and a
  profile change at lock acquisition without namespace mutation.
- Rollback accepts the exact recorded bridge while it is current, as well as a
  final current generation with the bridge immediately previous. Tests cover
  pre-final rollback, compensated final switch, and the guarded final case.
- Interrupted tmux option and environment conversions accept the durable
  duplicate state and converge by removing the source, in both directions.
- User rewrites verify group preservability, restore the recorded group even
  for a supplementary group, and verify all recorded metadata before mutation.
- Added a journal-free `preflight` command. The deployment runbook requires
  user and host preflights in the same quiesced maintenance window before either
  scope transitions, so cross-scope invalid state is found before mutation.

## Compatibility and deployment gate

The migration is an intentional quiesced namespace cutover; mixed old/new
runtimes are unsupported. The helper records exact path identities, bytes,
metadata and package generations, supports durable retries, inventories active
and archived portal manifests, and provides explicit pre-final and post-final
rollback states.

The user authorized aitherdev deployment, transient Codex-session restarts, and
resetting the current development cluster. Default-branch integration is not
authorized. The configuration remains on its dated feature branch. The shared
workspace root must nevertheless use the reviewed workspace policy and package
metadata before the alias-free cutover; this is still an explicit integration
gate under the root workspace rules.

Generic `workspace-host` and `workspace-portal` output aliases remain published
as organization-neutral compatibility names. New switching uses the default
output. The final organization workspace does not expose those aliases; the
exact bridge does because the deployed predecessor builds `#workspace-portal`.

## Quick verification

- Generic runtime tests: 71 runs, 449 assertions, no failures.
- Organization migration tests: 23 runs, 264 assertions, no failures.
- Generic, organization, bridge and final workspace no-build flake evaluations
  pass at their exact dependency pins.
- Final workspace package keys are exactly `default` and
  `vpsfree-dev-workspace`.
- Configuration input changes were made through `confctl`; repository hooks
  passed, repeated pin commits were consolidated, and generated helpers were
  removed.
- Forbidden-name scans remain empty in both generic repositories.

Long full package checks, the NixOS VM, exact bridge/final builds, aitherdev
configuration build, and live cutover remain deferred until the affected v30
review lanes are clean.

## Risk and rerun lanes

Overall risk remains **High** because this changes public cross-project
contracts, persisted user/root state, credentials and TLS paths, systemd/tmux
topology, destructive migration ordering, deployment and exact rollback.

Review v29 Scope was clean. Rerun the affected General, Architecture and Risk
lanes with `gpt-5.6-sol` at `xhigh` against this complete packet and exact heads.

## Non-goals

- Do not support mixed old/new runtime processes.
- Do not integrate a default branch without explicit authorization.
- Do not archive, delete, or permanently retire the development session.
- Do not change vpsAdmin schemas, APIs, protocols, or deployed vpsAdminOS nodes.
