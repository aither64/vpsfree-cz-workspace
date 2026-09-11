# Mandatory change review packet v38

## Outcome and acceptance criteria

Review the final four-layer component split and the quiesced, reversible
namespace cutover:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` independently consumes the same exact generic
runtime for the privileged host module. Generic repositories must contain no
case-insensitive `vpsfree` or `aitherdev` name in tracked paths or contents.
The final package has only generic runtime names; one immutable workspace
commit exists solely as the compatibility bridge.

Acceptance requires immutable construction, strict provider/consumer
contracts, independently meaningful commits, byte-accurate and retryable
forward/reverse migration, and an operator order that prevents mixed old/new
runtime processes.

Slug: `2026-09-09-workspace-components`

Plan and state:

- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/plan.md`
- `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/state.md`

| Component | Base | Exact pushed head |
|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `7a05da0cd79b19f3c9a0a8fa23b7043a1f984d4e` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `afb7ea94a314b855f7707bf0618aab52b91aa313` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `66ae63392ebcf891405fdf168803ef5d899f529b` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `dd6e4f377040c79c4d7c87521a7021ce8fc965f8` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `49b5d792d7102133c6dec056aecd58911334aea7` |

All five worktrees are clean and their feature refs match these heads. Exact
pins are:

```text
workspace@dd6e4f3 -> vpsfreecz/dev-workspace@66ae633
  -> aither64/dev-workspace@afb7ea9
  -> aither64/codex-web@7a05da0

configuration@49b5d79 -> aither64/dev-workspace@afb7ea9
  -> aither64/codex-web@7a05da0
```

Compatibility workspace commit:
`929096f7445da74e0d40a704db9609c2de9f8ae5`. The final workspace flake does
not construct or export it.

## Review v37 findings and remediation

- The organization migration commit now directly pins the final generic
  provider. It no longer retains the known-unbuildable vendor-hash revision,
  and the site-validation commit no longer performs a hidden dependency
  repair. The migration commit evaluates independently.
- The migration commit message describes journal schema 5, matching the only
  implementation and deployment contract that can be created from this
  unmerged branch.
- Generic host-module commit `a0f3f57` introduces the two standalone Nix test
  files directly. The later component extraction only preserves and wires
  them; it no longer adds 710 inline lines and removes them later.
- The migration derives separate path sets for tmux session and window
  options, passes the correct set through capture and journal validation, and
  exercises a contract fixture in which `@dev_session_worktree` is
  path-valued across forward, retry and reverse handoffs.
- `test_remove_refuses_unmanaged_tmux_session` now gives its runner a
  workspace-local `XDG_STATE_HOME`; the focused test no longer creates state
  in the real user profile.
- Required-runtime validation now joins the already-materialized unavailable
  provider array instead of calling `keys` on it. A regression proves the
  intended `DevSession::Error` and exact provider label.
- The 11 existing `dev-session-test*` recovery roots under the otherwise
  unused `~/.local/state/dev-workspaces/removed` were inventoried. They were
  produced by the previously unisolated test on September 10-11. Deployment
  will preserve the complete tree by atomically renaming it to
  `~/.local/state/dev-workspaces-test-recovery-20260911` before preflight;
  it will not delete or merge this test data into live session state.

## Compatibility and deployment assumptions

This is an intentional one-time incompatible namespace change. Mixed old and
new runtime clients are unsupported. All conversations must be idle, all
lifecycle transactions absent, and all development cluster state reset before
the frozen migration inventory is created.

Migration preserves paths, bytes, modes, ownership, credentials, TLS material,
profile generations, tmux servers/sessions/windows, authorities and portal
manifests. Opaque identifiers and registry content are not globally rewritten.
No migration journal from this branch has been deployed, so schema 5 is the
only supported new journal rather than an upgrade target. The user and host
journals plus compatibility and final generations remain available through
acceptance and rollback verification.

The user authorized aitherdev deployment, Codex session restarts and resetting
the running development cluster. Configuration is deployed directly from its
feature worktree and is not merged to `master`. The registered shared workspace
root must fast-forward to the reviewed workspace feature before the alias-free
package is authoritative; that default-branch integration remains an explicit
approval boundary.

Order: build bridge/final packages and aitherdev; validate authorities and tmux
identities; preserve the isolated test-recovery tree; reset cluster state;
quiesce sessions and old non-tmux services; install the bridge; stop services
restarted by activation; run both locked read-only preflights; migrate user and
host scopes; activate feature configuration; install the final profile; verify
services, domains, credentials, thread IDs and provider behavior. Reverse uses
the recorded bridge and exact journal inventory.

## Ownership and intended commit boundaries

- `codex-web` owns the reusable App Server browser/client protocol, durable
  request behavior and client security boundaries.
- Generic `dev-workspace` owns session, portal, profile and host runtime,
  extensions, generic namespaces, shared authority/tmux contracts and corpus.
  Host tests are standalone from their first owning commit. The component
  extraction owns the test-state isolation and required-runtime error fix.
- Organization `dev-workspace` owns vpsFree commands, skills, cluster providers,
  site configuration and the private migration helper. Its five-commit feature
  tail is policy, package, complete migration, workflow and site validation.
- The workspace owns policy, concrete user-side site data, bridge/final
  selection and cross-repository deployment proof.
- Configuration owns privileged host values and activation. Its four commits
  are channel declaration, one generated exact pin, host-module adoption and
  concrete aitherdev defaults. The generated `confctl` message is untouched.

## Quick verification

- All five flakes pass `nix flake check --no-build`; all worktrees pass
  `git diff --check` and are clean.
- Generic focused regressions pass 2 runs / 26 assertions with no failures.
  The preceding exact generic package build passed all packaged Go tests,
  285 Ruby lifecycle runs / 2715 assertions and 74 host-helper runs / 442
  assertions after deriving the corrected Go vendor hash.
- Organization migration passes 43 runs / 827 assertions with no failures,
  errors or skips against the exact generic runtime contract and corpus.
- Workspace deployment tests pass 2 runs / 9 assertions. The cross-worktree
  checker proves domain equality and the shared generic revision `afb7ea9`.
- Configuration was updated only through
  `confctl inputs channel set --commit`; Nixfmt and hooks passed, and generated
  `.bin`/`.bundle` helpers were removed.
- Exact `codex-web` Actions run `34555724208` is green. Exact generic run
  `34559366247` and organization run `34559395554` are in progress.
  Superseded organization runs accepted cancellation. The token still returns
  HTTP 403 when cancelling superseded generic runs.

Long full flake builds, the NixOS VM, bridge/final builds, aitherdev build and
dry activation remain deferred until this rerun is clean.

## Review disposition and risk

Overall risk is **High**: persisted user/root state, credentials/TLS,
systemd/tmux ownership, destructive migration, public cross-project contracts,
deployment order and rollback all change. Rerun General, Architecture, Scope
and Risk with fresh `gpt-5.6-sol` agents at `xhigh`.

General and Scope must verify the rewritten commit boundaries. Architecture
must verify the distinct tmux window path contract. Risk must verify test-state
isolation, intended error behavior and the explicit preservation decision for
already-created test recovery data. All lanes should report only current
Blocking, Important and Advisory findings plus residual gaps.

## Non-goals and fixed decisions

- Do not support mixed old/new runtime processes or final legacy aliases.
- Do not rewrite opaque identifiers or arbitrary serialized strings.
- Do not upgrade never-deployed migration journals.
- Do not infer or recreate a retained tmux server's old filesystem alias.
- Do not delete the isolated test-recovery data during this deployment.
- Do not integrate default branches without explicit authorization.
- Do not merge the configuration branch merely to deploy aitherdev.
- Do not archive, delete or permanently retire the initiative.
