# Mandatory change review packet v42

## Requested outcome

Review the final four-layer component split and the concrete stop-and-recreate
namespace deployment:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` independently pins the same generic runtime. The
tracked trees of both generic repositories contain no case-insensitive
organization or deployment-host naming. Workspace domains, presentation and
provider selection belong to the registered workspace's
`.dev-workspace.json`.

The deployment intentionally stops every managed session, tmux pane and old
Codex App Server. It preserves durable worktrees, tracking, manifests and
Codex storage, then creates fresh tmux and Codex client processes. Existing
thread IDs resume when available; the compatibility helper replaces only a
missing ready-session thread before migration is journaled.

Initiative: `2026-09-09-workspace-components`

| Component | Base | Exact pushed head |
|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `7a05da0cd79b19f3c9a0a8fa23b7043a1f984d4e` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `2e4382145e1ae3123a251e2797660dcb76931f37` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `0d3fbb15c278305e652a919ce0849876478bc5f0` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `7be93a189af4a058566dcfbb0808e66d9613df42` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `c75b9e9f9a6eb4ec42cb2be5e3c7996cd4b74abc` |

The immutable workspace compatibility bridge is
`57ffc0b7918f7a3274775af2bc857133b12f057d`. Exact pins are:

```text
workspace@7be93a1 -> organization@0d3fbb1
  -> generic@2e43821 -> codex-web@7a05da0

configuration@c75b9e9 -> generic@2e43821 -> codex-web@7a05da0
```

## Review v41 findings and remediation

- General found the inventory admission check occurred after cluster and
  session mutation, shell snippets could continue after failed checks, and
  forward/rollback activation commands and paths were incomplete. The exact
  site procedure now lives in the consuming workspace as executable
  `bin/aitherdev-workspace-cutover`. It uses strict shell mode, one immutable
  session and service inventory, explicit failure branches, concrete package,
  configuration and host paths, actual forward/reverse helper invocations,
  exact NixOS closure activation and profile-generation rollback.
- General's runbook-test advisory is remediated by
  `test/cutover_contract_test.rb`, wired into the workspace flake check. It
  checks shell syntax, admission-before-mutation ordering, forward and reverse
  calls, partial-authority handling and router reopening order.
- Architecture advised eliminating three repeated raw systemd lists. The exact
  site procedure defines the non-router user unit array once. The organization
  repository now documents only its generic migration helper contract; it no
  longer duplicates the consuming workspace's deployment topology.
- Risk found that a missing persisted ready-session thread would block final
  recreation and any post-migration manifest edit would invalidate rollback.
  Generic `dev-session start --replace-missing-thread` is an explicit opt-in
  for a stopped, existing session. The portal resumes the exact active thread,
  starts a new thread only if none exists in that session directory, and
  refuses a different active candidate. The site procedure starts and stops
  all sessions through this mode while the compatibility package is selected,
  before either migration preflight, so replacement metadata belongs to both
  journal directions.
- Risk found rollback stopped all expected sessions even if final recreation
  failed partway. Rollback now inventories actual destination authorities,
  rejects any outside the audited set, stops only the proven subset while
  aggregating failures, and proves zero authorities before reverse preflight.
  An interrupted forward migration is completed through its retryable journal
  before reverse preflight.
- Scope and General found stale authorization and review state. The durable
  state now consistently records the user's permission to stop/recreate all
  sessions and reset clusters, while retaining the separate default-branch
  integration boundary.
- Risk advised checking every current thread-create setting. The stopped-session
  regression now asserts both portal URL fields and `--require-runtime` in
  addition to the complete workspace, lifecycle, tmux and Codex provenance.
- The compatibility bridge was rebuilt at `57ffc0b` with the exact final
  organization and generic pins, so its source-namespace package contains the
  explicit missing-thread option used by the cutover. The final flake still
  does not export the bridge.

## Ownership and commit boundaries

- `codex-web` owns reusable App Server transport and browser conversation
  behavior. It is unchanged from v41.
- Generic `dev-workspace` owns session restart policy and the new explicit
  missing-thread replacement primitive. This is one independently tested final
  runtime commit after the previously reviewed functional chain.
- Organization `dev-workspace` owns organization tools, providers, skills and
  the private migration helper. Its rewritten migration commit pins the generic
  replacement primitive and describes the generic forward/reverse contract.
- The workspace owns exact site configuration and now also its one-time
  executable cutover procedure and structural test.
- Configuration owns privileged host values and activation. Its single
  dependency update was generated solely by
  `confctl inputs channel set --commit`; the generated message is unchanged
  and precedes the two configuration commits that consume it.

The organization repository retains filtered predecessor provenance before
the initiative tail. Its GitHub default still points at the feature branch
because the administrative update returned HTTP 403; neutral `master` exists
and consumers use exact immutable refs.

## Compatibility and deployment

This is an intentional incompatible namespace transition. Mixed old and new
runtime processes are unsupported. The site script compares all ten live
authorities before any reset, restart or service mutation, then repeats the
comparison after adding identities to five legacy sessions. It resets exactly
the three audited clusters through the installed stable helper and stops all
sessions, router, portal, App Server, reconciler and tmux keeper.

The compatibility package retains only the source namespace and router path.
During its short selected interval, sessions are started with the explicit
missing-thread option and immediately stopped. Both authority roots and both
tmux sockets must then be empty. The occupied target recovery tree is verified
against its committed 37-line inventory and aggregate SHA-256 before an atomic
rename; it is preserved and never merged into live state.

Certificate renewal is runtime-masked from host preflight until acceptance or
completed rollback. Both locked preflights pass before the script records a
forwarding stage and invokes either migration. Forward migration is journaled
and retryable. The script activates the configuration feature worktree, selects
the final package from the integrated registered workspace root, recreates all
sessions, checks exact authorities and all pane/global environments, then
reopens the router.

Rollback supports preparation and forward in-progress stages. After stopping
the proven actual authority subset, it completes an interrupted forward
journal, runs both reverse preflights and both reverse commands, activates the
recorded `/run/current-system` closure, rolls the user profile back to the exact
pre-cutover store path, recreates all reviewed sessions and only then reopens
the old router.

Deployment, cluster reset and session stop/recreation are authorized. The
configuration branch is deployed directly and is not integrated. The final
registered-root package still requires explicit approval to fast-forward the
workspace feature into shared `master`; no default-branch integration is
otherwise authorized.

## Quick verification

- Generic portal Go packages pass. Generic `dev_session_test.rb` passes with
  286 runs / 2887 assertions, including two focused replacement/restart tests.
- Workspace deployment contract passes with 3 runs / 14 assertions and the
  new cutover contract passes with 5 runs / 29 assertions. Workspace and
  organization no-build flake evaluations pass at their current pins.
- Organization migration remains 43 runs / 831 assertions at the unchanged
  helper implementation. The final generic pin evaluates in every organization
  check.
- The configuration input update was created only by `confctl`; Nixfmt and all
  hooks passed, and transient helper directories were removed.
- All five exact heads are pushed and clean, equal their remote feature refs
  and pass exact-range `git diff --check`. The generic and organization source
  scans are empty. The real cross-worktree deployment checker passes at generic
  revision `2e438214`.
- Exact `codex-web` Actions run `34555724208` passed. Exact generic run
  `34572091420` and organization run `34572849148` are in progress. Cancellation
  of superseded organization run `34569805854` was submitted; cancellation of
  superseded generic run `34569227294` again returned HTTP 403.

Long full flake builds, both organization NixOS VMs, compatibility/final
package builds, configuration build/dry activation and live cutover remain
deferred until this review is clean.

## Review disposition

Overall risk is **High** because this changes persistent user/root state,
credentials and TLS paths, service admission, session/thread recovery, system
activation and exact rollback. Run General, Architecture, Scope and Risk from
fresh context with `gpt-5.6-sol` at `xhigh`.

- General: inspect exact commit boundaries, generated configuration update and
  executable operator flow.
- Architecture: inspect component ownership, dependency direction and whether
  the site orchestrator composes existing migration/lifecycle primitives.
- Scope: inspect proportionality and consistency with the user's simplified
  stop-and-recreate instruction.
- Risk: inspect admission ordering, missing-thread replacement, interruption
  states, partial recreation, forward/reverse journals, privileged writers,
  system/profile rollback and final router gates.

## Fixed decisions

- Do not support mixed runtime generations or final legacy aliases.
- Do not retain a live tmux pane, Codex client or App Server process.
- Preserve an available thread ID; replace only a missing thread explicitly
  before migration is journaled.
- Do not rewrite arbitrary opaque identifiers or serialized strings.
- Do not expose the migration helper as a normal user command.
- Do not delete the isolated test-recovery tree.
- Do not integrate default branches without explicit authorization.
- Do not merge the configuration branch merely to deploy.
- Do not archive, delete or retire the initiative.
