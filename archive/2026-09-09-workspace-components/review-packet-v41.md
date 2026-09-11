# Mandatory change review packet v41

## Requested outcome and acceptance criteria

Review the final four-layer component split and its reversible namespace
cutover:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` independently pins the same generic runtime for the
privileged host module. The tracked trees of both generic repositories must
contain no case-insensitive `vpsfree` or `aitherdev` name. Workspace domains,
display data and provider selection belong only to each registered root's
`.dev-workspace.json`.

The aitherdev cutover intentionally stops every managed session, tmux pane and
old Codex App Server before migration. Durable worktrees, tracking, portal
manifests and persisted conversation data remain. After activation, every
session is recreated through the final helper before browser admission is
reopened. A persisted thread ID may be resumed through the supported settings
refresh, but no live process or pane is preserved across the namespace change.

Initiative: `2026-09-09-workspace-components`

- Plan: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/plan.md`
- State: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/state.md`

| Component | Worktree | Base | Exact pushed head |
|---|---|---|---|
| `codex-web` | `worktrees/2026-09-09-workspace-components/codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `7a05da0cd79b19f3c9a0a8fa23b7043a1f984d4e` |
| generic `dev-workspace` | `worktrees/2026-09-09-workspace-components/dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `4b3d426d0484a62bac5bcfc7d5c7b6ff2140b045` |
| organization `dev-workspace` | `worktrees/2026-09-09-workspace-components/vpsfree-dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `a8be458b9db18033bc468a57de4981cf9d52979e` |
| workspace | `worktrees/2026-09-09-workspace-components/workspace` | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `db3dc6763f350adc13f05e9ee13713ae9c1f6e66` |
| configuration | `worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration` | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `6956ff4197d36e731084b3167b0d5e76b5003583` |

All five worktrees are clean, every exact range passes `git diff --check`, and
the remote feature refs equal these heads. The immutable workspace
compatibility bridge is
`712b3f95acbd423b2b7ff036460a3320f0e00779`; the final workspace flake does
not export it.

Exact dependency pins are:

```text
workspace@db3dc67 -> organization@a8be458
  -> generic@4b3d426 -> codex-web@7a05da0

configuration@6956ff4 -> generic@4b3d426 -> codex-web@7a05da0
```

## Review v40 findings and remediation

- General found that generic commit `a0f3f57` introduced VM assertions which
  only passed after later preflight code. The unmerged history was rewritten:
  both preflights are now in `7293387`, the commit which introduces those
  assertions, and the later repair commit no longer exists.
- General required a reproducible guard around the audited ten-session list.
  The runbook now compares a sorted expected array byte-for-byte with every
  live authority filename before it mutates state and repeats the comparison
  after forward and reverse session recreation.
- Risk found manually quiesced clients were never restored and that retained
  tmux panes, the global tmux environment and ready App Server threads would
  keep the old namespace. The user explicitly authorized the simpler contract:
  stop all sessions and the entire tmux/App Server before preflight, migrate
  with no authorities or socket, then recreate every session through the final
  helper. No retained-process bridge or pane restoration remains. Existing
  stopped-session coverage proves `thread create --thread-id` is called, and
  now asserts the complete current runtime settings passed to that operation.
  Live acceptance checks every recreated pane environment and tmux's global
  environment for absence of legacy-prefixed variables before starting the
  router.
- Risk found certificate renewal could change the rollback fingerprint after
  activation. The runbook runtime-masks the renewal timer and service before
  host preflight, keeps them masked through acceptance or rollback, and
  explicitly unmasks and starts the timer only after the chosen result is
  accepted.
- Architecture and General found intentional trailing tabs in the recovery
  manifest made exact-range whitespace checks fail. Empty link targets now use
  a literal `-`; the runbook serializer and committed manifest agree. The live
  37-line inventory matches with aggregate hash
  `837e40a5f9754a9f9ae6442dfebc356288d9f32d0d3c8e58123c9d5eb1cbe917`.
- General found the workspace deployment checker emitted a Ruby traceback for
  a non-object registration. It now validates both decoded roots before hash
  access, and a regression requires one concise contract error without a
  traceback.
- Scope v40 was clean. Architecture found no ownership or repetition defect.
  Because the deployment contract and all downstream pins changed, all four
  lanes are rerun from fresh context.

## Ownership and intended commit boundaries

- `codex-web` owns reusable Codex App Server conversation integration and its
  browser/client protocol.
- Generic `dev-workspace` owns sessions, portal, profile, host module,
  extensions and generic authority/tmux contracts. The host substrate commit
  is independently testable after the v40 fold.
- Organization `dev-workspace` owns vpsFree commands, skills, providers, site
  validation and the private one-time migration helper. The stop-and-recreate
  operating procedure, recovery manifest and generic pin live in its migration
  commit.
- The workspace owns repository policy, concrete site data, bridge/final
  selection and cross-repository deployment proof. Its final checker owns the
  malformed-root regression.
- Configuration owns privileged host values and activation. It contains one
  current `confctl`-generated exact-input commit; that generated message is
  preserved unchanged.

The organization repository retains filtered predecessor provenance. Those
commits predate the initiative tail and do not alter the final ownership split.

## Compatibility and deployment assumptions

This is an intentional one-time incompatible namespace change. Mixed old and
new runtime processes are unsupported. Before migration, the exact authority
inventory must match the reviewed ten-session list, all three development
clusters are reset through the installed stable helper, every session is
stopped through `dev-session stop`, and the old router, portal, App Server,
reconciler and tmux keeper are stopped. The bridge switch is followed by the
same complete service stop before either read-only preflight.

The user and host migrations remain journaled and exactly reversible. They
preserve persisted registry/profile data, active and archived portal manifests,
passwords, auth, CA, TLS and public CA state. No schema-5 migration journal has
been deployed. The occupied target tree is atomically renamed and verified
against the committed manifest; it is never deleted or merged into live state.

The privileged writer remains runtime-masked throughout the rollback window.
After final package activation, the router is stopped again, every session is
started with the final helper, exact authority identity is checked, and both
tmux global and pane-process environments are checked before browser admission
reopens. Rollback mirrors this by stopping every new session and service before
reverse preflight, then recreating all sessions with the restored helper before
reopening the old router.

The user authorized aitherdev deployment, stopping/recreating Codex sessions
and resetting development clusters. Configuration deploys from its feature
worktree and is not merged. The final registered-root package still requires a
workspace fast-forward into shared `master`; default-branch integration remains
an explicit approval boundary.

## Quick verification

- All exact heads are pushed and clean; exact-range `git diff --check` passes.
- Correct tracked-file scans are empty for case-insensitive `vpsfree` and
  `aitherdev` in both generic repositories and for `aitherdev` in the
  organization repository.
- Generic `dev_session_test.rb`: 285 runs / 2876 assertions. Generic
  `workspace_host_test.rb`: 73 runs / 453 assertions. The stopped-session
  settings regression passes with 29 assertions. Generic complete no-build
  flake evaluation passes.
- Organization migration: 43 runs / 831 assertions. Its complete no-build
  flake evaluation, including both VM derivations, passes.
- The recovery serializer reproduces the committed 37-line live inventory and
  aggregate hash exactly.
- Workspace deployment tests: 3 runs / 14 assertions. Its no-build flake
  evaluation passes. The real cross-worktree checker proves matching portal
  domains and generic revision `4b3d426`.
- Configuration was updated only by
  `confctl inputs channel set --commit`; Nixfmt and hooks passed, transient
  `.bin`/`.bundle` outputs were removed, and no-build flake evaluation passes.
- Exact `codex-web` Actions run `34555724208` passed. Generic exact-head run
  `34569227294` and organization exact-head run `34569805854` are in progress.
  Generic run `34568265248` failed because a test repeated the forbidden
  legacy prefix; its failed logs were inspected and the redundant literal was
  removed. Cancellation was submitted for superseded organization runs
  `34569273665`, `34568494154` and `34564709694`.

Long full flake builds, both NixOS VMs, bridge/final package builds, aitherdev
build and dry activation remain deferred until this review is clean.

## Review disposition and risk

Overall risk is **High** because the change affects persisted user/root state,
credentials and TLS, systemd/tmux ownership, destructive migration, public
cross-project contracts, deployment order and rollback. Run General,
Architecture, Scope and Risk with fresh `gpt-5.6-sol` reviewers at `xhigh`.

General should verify independent commit boundaries, generated-message
handling and the executable runbook. Architecture should verify ownership and
that the stop-and-recreate deployment uses existing runtime primitives rather
than adding parallel mechanisms. Scope should verify v40 remediation removed
retained-process complexity without weakening durable-state safety. Risk should
verify exact inventory comparison, complete process shutdown, settings refresh,
privileged writer barriers, reverse ordering and rollback.

## Non-goals and fixed decisions

- Do not support mixed old/new runtime processes or final legacy aliases.
- Do not preserve a live tmux pane, native Codex client or App Server process
  across the aitherdev namespace cutover.
- Do not require a persisted thread ID to survive; when reused, refresh it only
  through the supported start/settings path.
- Do not rewrite opaque identifiers or arbitrary serialized strings.
- Do not upgrade never-deployed migration journals.
- Do not delete or merge isolated test-recovery data.
- Do not expose the migration helper as a normal user command.
- Do not duplicate workspace presentation in package catalogs.
- Do not integrate default branches without explicit authorization.
- Accept the organization repository's temporary feature-branch GitHub default
  until an administrator can select the existing neutral `master`.
- Do not merge the configuration branch merely to deploy aitherdev.
- Do not archive, delete or permanently retire the initiative.
