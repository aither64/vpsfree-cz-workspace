# Mandatory change review packet v43

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

The deployment may discard every live pane, process, tmux identity and Codex
client instance. It stops all ten audited old authorities, then starts fresh
processes for the nine active sessions: eight Codex sessions and one
intentionally shell-only session. The stale authority associated with the
archived session is stopped and not recreated.

Initiative: `2026-09-09-workspace-components`

| Component | Base | Exact pushed head |
|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `7a05da0cd79b19f3c9a0a8fa23b7043a1f984d4e` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `4b3d426d0484a62bac5bcfc7d5c7b6ff2140b045` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `3e3f0ff7c2d23f08f19887822efa12f969bbb56f` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `0ec5ba403ef215e7f4923841a3f990895e4ddf64` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `6956ff4197d36e731084b3167b0d5e76b5003583` |

The immutable workspace compatibility bridge is
`120de27e384987e042c1b9424da20418cd0d56fe`. Exact pins are:

```text
workspace@0ec5ba4 -> organization@3e3f0ff
  -> generic@4b3d426 -> codex-web@7a05da0

configuration@6956ff4 -> generic@4b3d426 -> codex-web@7a05da0
```

## Final simplification after review v41

- The proposed generic `--replace-missing-thread` behavior was removed. Real
  inventory inspection proved that all eight active recorded Codex threads are
  materialized. The generic runtime and configuration therefore returned to
  their earlier clean heads, and the organization/workspace pins were rebuilt.
- Before any mutation, the site script proves the exact authority and cluster
  inventories, matches each of the eight active manifest thread IDs to its old
  authority and checks it is materialized, proves one active session is
  shell-only, and proves the tenth authority belongs to archived tracking with
  no thread. An inventory change aborts before reset or stop.
- All ten old authorities are stopped. Forward and rollback start only the
  eight active Codex sessions plus the active shell-only session. The archived
  authority is never recreated.
- Fresh tmux and native Codex client processes are created through the ordinary
  stable helper. No live process, pane or tmux identity crosses the namespace
  migration. Persisted conversations are resumed only because that is the
  normal contract of restarting these currently valid active sessions.
- Partial recreation rollback inventories actual destination authorities,
  rejects any outside the nine active-session set, stops only the proven subset,
  and proves zero authorities before reverse preflight.

## Ownership and commit boundaries

- `codex-web` owns reusable App Server transport and browser conversation
  behavior.
- Generic `dev-workspace` owns reusable session, portal, cluster and host
  primitives. It contains neither organization nor host naming and includes a
  GitHub workflow for its flake checks. It has no deployment-specific recovery
  behavior.
- Organization `dev-workspace` owns organization tools, providers, skills and
  the private journaled migration helper. Its documentation describes only the
  reusable migration contract and its GitHub workflow runs the flake checks.
- The workspace owns domains, provider selection, exact audited live inventory
  and the executable one-time aitherdev operator procedure.
- Configuration owns privileged host values and activation. Its dependency
  update was generated solely by `confctl` and precedes the two consuming
  configuration commits.

The organization repository retains filtered predecessor provenance before
the initiative tail. Its GitHub default still points at the feature branch
because the administrative update returned HTTP 403; neutral `master` exists
and consumers use exact immutable refs.

## Compatibility and deployment

This is an intentional incompatible namespace transition. Mixed old and new
runtime processes are unsupported. The script resets exactly three audited
development clusters through the installed stable helper, stops all ten old
authorities and the router, portal, App Server, reconciler and tmux keeper, then
selects an immutable source-namespace compatibility package while all access is
closed.

Both old/new authority roots and tmux sockets must be empty before migration.
The occupied target recovery tree is verified against its committed 37-line
inventory and aggregate SHA-256 before atomic preservation. Certificate renewal
is runtime-masked from host preflight until acceptance or completed rollback.

Both locked preflights pass before the forwarding stage is recorded. Forward
migration is journaled and retryable. The script deploys configuration from its
feature worktree, selects the final package from the integrated registered
workspace root, starts the nine active sessions, proves their exact authorities
and new process environments, then reopens the router.

Rollback supports preparing, prepared, forwarding and forwarded stages. It
stops only proven actual new authorities, completes an interrupted forward
journal before reverse preflight, runs both reverse migrations, activates the
recorded old NixOS closure, rolls the user profile back to the exact old store
path, starts the nine active sessions and reopens the old router.

Deployment, cluster reset and session stop/recreation are authorized. The
configuration branch is deployed directly and is not integrated. The final
registered-root package still requires explicit approval to fast-forward the
workspace feature into shared `master`; no default-branch integration is
otherwise authorized.

## Quick verification

- Generic `dev_session_test.rb`: 285 runs / 2874 assertions; generic
  `workspace_host_test.rb`: 73 / 453. Generic no-build flake evaluation and the
  case-insensitive `vpsfree|aitherdev` source scan pass.
- Organization aggregate Nix check tests: 210 runs / 1884 assertions, zero
  failures/errors and one documented skip. Its no-build flake evaluation and
  `aitherdev` source scan pass.
- Workspace cutover contract: 6 runs / 43 assertions; deployment contract:
  3 / 14. Bash syntax, ShellCheck and no-build flake evaluation pass.
- Configuration no-build flake evaluation passes and the clean exact head is
  the original `confctl`-generated final chain.
- All five exact heads are pushed and clean. `codex-web` Actions run
  `34555724208` passed. Generic exact-head run `34569227294` already passed and
  duplicate run `34574796357` is in progress. Organization exact-head run
  `34574877938` is in progress.

Long full flake builds, both organization NixOS VMs, compatibility/final
package builds, configuration build/dry activation and live cutover remain
deferred until this review is clean.

## Review disposition

Overall risk is **High** because this changes persistent user/root state,
credentials and TLS paths, service admission, session recovery, system
activation and exact rollback. Run General, Architecture, Scope and Risk from
fresh context with `gpt-5.6-sol` at `xhigh`.

- General: inspect exact commit boundaries, generated configuration update and
  executable operator flow.
- Architecture: inspect component ownership, dependency direction and whether
  the site orchestrator composes existing migration/lifecycle primitives.
- Scope: inspect proportionality and consistency with the user's explicit
  permission to stop old sessions and start fresh processes.
- Risk: inspect admission ordering, inventory classification, interruption
  states, partial recreation, forward/reverse journals, privileged writers,
  system/profile rollback and final router gates.

## Fixed decisions

- Do not support mixed runtime generations or final legacy aliases.
- Do not retain a live tmux pane, Codex client, App Server process or tmux
  identity.
- Stop the archived authority and do not recreate the archived session.
- Do not add a generic missing-thread replacement API for the audited live
  state.
- Do not rewrite arbitrary opaque identifiers or serialized strings.
- Do not expose the migration helper as a normal user command.
- Do not delete the isolated test-recovery tree.
- Do not integrate default branches without explicit authorization.
- Do not merge the configuration branch merely to deploy.
- Do not archive, delete or retire the initiative.
