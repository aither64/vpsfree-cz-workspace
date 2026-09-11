# Mandatory change review packet v37

## Outcome and acceptance criteria

Review the final four-layer component split and its quiesced namespace cutover:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` independently consumes the same exact generic
runtime for the privileged host module. The generic repositories must contain
no case-insensitive `vpsfree` or `aitherdev` names in tracked paths or file
contents. Site domains are supplied by the workspace consumer. Host-only
values stay in configuration. The final runtime exposes only generic names;
one exact workspace commit exists solely as the reversible compatibility
bridge.

Acceptance requires correct immutable construction, strict cross-project
contracts, non-vacuous provider/consumer tests, byte-accurate and retryable
forward/reverse migration of user, root and tmux state, and an operator order
that never permits mixed old/new runtime processes.

Slug: `2026-09-09-workspace-components`

Plan and state:

- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/plan.md`
- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/state.md`

| Component | Worktree | Base | Head |
|---|---|---|---|
| `codex-web` | `worktrees/2026-09-09-workspace-components/codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `7a05da0cd79b19f3c9a0a8fa23b7043a1f984d4e` |
| generic `dev-workspace` | `worktrees/2026-09-09-workspace-components/dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `58b11a112c9f3ba1b79094dae8a4d4f1df2b6a52` |
| organization `dev-workspace` | `worktrees/2026-09-09-workspace-components/vpsfree-dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `a7c37dc861bd7d63bd92117a93d47884f5e566ce` |
| workspace | `worktrees/2026-09-09-workspace-components/workspace` | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `da52c005afe5e541592a3d6b21412e2914fff71c` |
| configuration | `worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration` | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `d2aa88dee5f00d71a57db69c51a8cad7f1beefe2` |

All five heads are committed, pushed and clean. Exact pins:

```text
workspace@da52c00 -> vpsfreecz/dev-workspace@a7c37dc
  -> aither64/dev-workspace@58b11a1
  -> aither64/codex-web@7a05da0

configuration@d2aa88d -> aither64/dev-workspace@58b11a1
  -> aither64/codex-web@7a05da0
```

Compatibility workspace commit:
`f88aa74325b0ce143d40f1dd96e309fb86234dfc`. The final workspace flake does
not construct or export it.

## Review v36 findings and remediation

- Namespace migration no longer applies a global string replacement to
  serialized documents. It parses authority JSON and changes only the two
  declared socket fields; portal YAML changes only `codex.socket_path`.
  Registry data and opaque IDs/content remain byte-for-byte unchanged.
- Generic `runtime-contract.json` now owns the complete tmux metadata
  inventory and marks which values contain paths. The organization helper
  consumes that pinned contract through `DEV_WORKSPACE_RUNTIME_CONTRACT`
  instead of owning an overlapping list.
- Tmux values preserve exact whitespace and empty strings. Removed inherited
  environment entries are journaled as a distinct tombstone state and restored
  with `set-environment -r`; value presence is never inferred from `.strip`.
- Journaled tmux mappings require exactly four tuple items. Extra or missing
  values fail preflight rather than being partially interpreted.
- Namespace move records explicitly list parent directories created by the
  forward operation. Reverse removes only those exact parents, performs their
  durable cleanup before advancing the journal, and safely retries an
  interruption at that point. The never-deployed journal schema is now 5.
- Generic source checks inspect tracked filenames as well as contents in both
  generic repositories.
- The shared authority-corpus tests enforce the exact valid/invalid manifest
  inventory at both provider and organization consumer boundaries.
- The generic feature history now introduces only the reusable package. The
  removed organization variant, incomplete test-extraction commit and repair
  commits were folded into their owning changes. Configuration likewise has
  one untouched `confctl` update directly from the generic base to the final
  runtime.
- The Nix Go vendor hash is derived for the final `codex-web` module pin and is
  folded into the original generic dependency-integration commit. The two CI
  failures that exposed the stale hash were investigated rather than rerun.

## Compatibility and deployment assumptions

This is an intentional one-time incompatible namespace change. Mixed old and
new runtime clients are unsupported. The migration runs only with all
conversations idle and no lifecycle transaction pending. It preserves exact
paths, bytes, modes, ownership, credentials, TLS material, profile generations,
tmux sessions/windows, authorities and portal manifests. Partial operations
are journaled and retryable.

No migration journal from this branch has been deployed. Therefore schema 5
is the only supported new journal, not an upgrade target. Rollback is allowed
only while the journaled workspace, tmux and host inventories remain frozen;
both locked reverse preflights must pass before either scope mutates.

The user authorized deployment to aitherdev, restarting Codex sessions and
resetting development clusters. Deployment must consume the configuration
feature worktree. Default-branch integration remains a separate authorization
boundary. The registered shared workspace root must fast-forward to the exact
reviewed workspace head before the alias-free package may become authoritative.

Deployment order is: build bridge/final outputs; validate every authority and
tmux identity; reset owned clusters as needed; quiesce sessions and old
non-tmux services; install the bridge; stop services restarted by activation;
run both locked preflights and freeze inventory; migrate user and host scopes;
activate the feature configuration; install the final profile; verify services,
domains, credentials, thread IDs and provider behavior. Reverse uses the
recorded bridge and exact journal values.

## Ownership, interfaces and consumers

- `codex-web` owns the reusable App Server client, browser integration, durable
  request protocol and client security rules. Generic `dev-workspace` is its
  direct pinned consumer.
- Generic `dev-workspace` owns session/portal/profile/host runtime behavior,
  generic environment/path names, the extension catalog, runtime authority
  and tmux metadata contracts, and their shared fixture corpus. Its consumers
  are organization `dev-workspace`, the workspace through that pin, and the
  configuration host module.
- Organization `dev-workspace` owns vpsFree commands, skills, cluster
  providers, required site configuration and the private migration helper.
  The migration code, runbook and tests are deliberately one functional commit
  because none is safe or independently useful without the exact protocol it
  documents and verifies. Earlier selected history is retained as source
  provenance; the initiative tail is clean.
- `vpsfree-cz-workspace` owns policy, active records, concrete user-side site
  configuration, bridge selection, final namespace and the cross-repository
  deployment checker.
- `vpsfree-cz-configuration` owns privileged NixOS values and activation. Its
  history is channel declaration, one generated exact input update, host-module
  adoption and concrete aitherdev defaults.

## Intended commit boundaries

- `codex-web`: focused reusable protocol/security changes, tests, packaging and
  workflow/source-boundary enforcement stay with the behavior they validate.
- Generic `dev-workspace`: repository/module adoption, reusable package,
  conversation dependency, host/profile/portal responsibilities, extension
  boundaries, generic namespace, authority/corpus and tmux contract are
  separate functional commits. Follow-up fixes have been folded into owners.
- Organization `dev-workspace`: retained predecessor provenance precedes five
  clean initiative commits for policy, organization package, migration,
  workflow and complete site validation.
- Workspace: seven commits independently own repository registration, site
  data, package consumption, delegated-source removal, bridge, final namespace
  and deployment proof.
- Configuration: declaration, generated pin, module use and site defaults are
  four independent commits. The generated `confctl` message is untouched.

## Quick verification

- All five worktrees pass `git diff --check` and are clean at their pushed
  heads. All five flakes pass `nix flake check --no-build` at the final pins.
- Generic `portal/internal/session` passes with `CGO_ENABLED=0`. Building the
  exact generic package passes all packaged Go tests plus 285 Ruby lifecycle
  runs / 2715 assertions and 74 host-helper runs / 442 assertions, with zero
  failures or errors. The corrected Go fixed-output closure builds with
  `sha256-saNgFV7yWM6k4BIJO+8BepcQ2tDOLXIeDLOOM5939kY=`.
- Organization migration passes 43 runs / 827 assertions with zero failures,
  errors or skips against the generic runtime contract and fixture corpus.
- Configuration was updated only with `confctl inputs channel set --commit`;
  Nixfmt and commit hooks passed and generated `.bin`/`.bundle` helpers were
  removed.
- Exact `codex-web` Actions run `34555724208` is green. Exact generic run
  `34556902789` and organization run `34556934552` are in progress. The
  preceding exact runs `34556107322` and `34556143630` failed only at the same
  stale Go vendor hash; their logs were inspected and the corrected closure was
  built locally.

Long full flake checks, the NixOS VM, bridge/final builds, aitherdev build and
dry activation remain deferred until this review is clean.

## Review disposition and risk

Overall risk is **High**: persisted user/root state, credentials/TLS,
systemd/tmux ownership, destructive migration, public cross-project Nix and
runtime contracts, deployment order and exact rollback all change. Run
General, Architecture, Scope and Risk with `gpt-5.6-sol` at `xhigh`.

The v36 remediation changes serialized-state boundaries, the public tmux
metadata contract, journal schema/rollback behavior, cross-project tests,
dependency pins and commit history. All lanes must rerun.

GitHub selected the organization feature branch as that new repository's
default. The available token cannot change it (HTTP 403). Neutral `master`
exists and all consumers use immutable revisions; repository administration
must correct the default before normal integration.

## Non-goals, rejected alternatives and user decisions

- Do not support mixed old/new runtime processes or legacy aliases after the
  final switch.
- Do not rewrite opaque identifiers or arbitrary serialized strings merely
  because they contain an old namespace substring.
- Do not upgrade never-deployed migration journals.
- Do not infer or recreate a retained tmux server's old filesystem alias.
- Do not integrate a default branch without explicit authorization.
- Do not merge the configuration branch merely to deploy aitherdev.
- Do not archive, delete or permanently retire the initiative.
- Do not change vpsAdmin schemas, APIs, protocols or deployed vpsAdminOS nodes.
