# Mandatory change review packet v39

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

| Component | Worktree | Base | Exact pushed head |
|---|---|---|---|
| `codex-web` | `worktrees/2026-09-09-workspace-components/codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `7a05da0cd79b19f3c9a0a8fa23b7043a1f984d4e` |
| generic `dev-workspace` | `worktrees/2026-09-09-workspace-components/dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `006de94602a5e42c00bbb7f3fea3d705c03ed64a` |
| organization `dev-workspace` | `worktrees/2026-09-09-workspace-components/vpsfree-dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `ca782c585aac6a2c28df970fab1a9b3d76343294` |
| workspace | `worktrees/2026-09-09-workspace-components/workspace` | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `7bbb9ae7683d8535b78de3794658acf4732942c5` |
| configuration | `worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration` | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `4a347d4335af2feaa11c246752702cbfdb743659` |

All five worktrees are clean and their feature refs match these pushed heads.
Exact pins are:

```text
workspace@7bbb9ae -> vpsfreecz/dev-workspace@ca782c5
  -> aither64/dev-workspace@006de94
  -> aither64/codex-web@7a05da0

configuration@4a347d4 -> aither64/dev-workspace@006de94
  -> aither64/codex-web@7a05da0
```

Compatibility workspace commit:
`f8a05c21c53e5d4abde2b389a3daccb61fbc8e0b`. The final workspace flake does
not construct or export it.

## Review v38 findings and remediation

- General found that the generic extension-hardening commit also introduced
  tmux adoption, state isolation and a lock-path documentation repair. The
  unmerged history now puts state isolation and the documentation correction
  in the component-extraction commit and coalesces all tmux socket-identity
  behavior in `aa35b9e`; `27cf51d` contains only the extension and workspace
  configuration boundary.
- General and Scope found that the extraction message claimed to extract tests
  already introduced as standalone files. The rewritten `81009c6` message now
  says it preserves those tests, matching the tree transition.
- Scope found obsolete add/delete churn for the organization `invalid.json`
  fixture and a meaningless `jq` check. The owning organization package
  commit no longer introduces either.
- Architecture found that packet v38 named a nonexistent compatibility SHA.
  The correct exact bridge after the final pin cascade is
  `f8a05c21c53e5d4abde2b389a3daccb61fbc8e0b`.
- Architecture found that the runbook did not preserve the known occupied new
  user-state target. It now requires rechecking the exact 11-root inventory
  and metadata hash, verifying the backup target is absent, atomically moving
  the complete tree to
  `~/.local/state/dev-workspaces-test-recovery-20260911`, and verifying the
  renamed inventory. It explicitly forbids deletion or merging.
- Architecture found that the final package switch was sourced from the
  unintegrated feature worktree. The runbook and plan now require explicit
  approval, fast-forward integration of the reviewed workspace feature into
  the registered shared root, and the final switch from that registered root.
- Architecture advised exact authority-format validation. Generic Go and Ruby
  consumers now compare the value to the canonical twelve-field tuple rather
  than accepting an arbitrary non-empty array.

The Risk lane could not start in v38 before remediation began because only
three reviewer slots were free. This v39 review therefore runs all four lanes
from fresh context.

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
all current development cluster state. Configuration is deployed directly from
its feature worktree and is not merged to `master`. The registered shared
workspace root must fast-forward to the reviewed workspace feature before the
alias-free package is authoritative; that default-branch integration remains
an explicit approval boundary.

The live new namespace currently contains only 11 test-created recovery roots
under `removed/`; its inventory metadata hash is
`2d96774d8b15210437befc21ba37d0e9bc750d9d3faead49f2594f3dc1dfdcc7`.
It will be preserved by the exact atomic rename above immediately before
preflight. Three existing development clusters will be reset through the
stable helper, never by direct removal.

Order: build bridge/final packages and aitherdev; validate authorities and tmux
identities; initialize the five missing tmux identities by stable session
restart; reset cluster state; quiesce sessions and old non-tmux services;
install the bridge; stop services restarted by activation; recheck and preserve
the isolated test-recovery tree; run both locked read-only preflights; migrate
user and host scopes; activate feature configuration; install the final profile
from the integrated shared root; verify services, domains, credentials, thread
IDs and provider behavior. Reverse uses the recorded bridge and exact journal
inventory.

## Ownership and intended commit boundaries

- `codex-web` owns the reusable App Server browser/client protocol, durable
  request behavior, client security boundaries, example and source-boundary
  check. Its seven feature commits separate moves, policy, persistence,
  integration, documentation and generic-name enforcement.
- Generic `dev-workspace` owns session, portal, profile and host runtime,
  extensions, generic namespaces, shared authority/tmux contracts and corpus.
  Host tests are standalone from their first owning commit. Component
  extraction owns state isolation; extension commits own catalog and
  activation rules; tmux adoption is localized in `aa35b9e`; the final two
  commits publish the validation corpus and exact metadata contract.
- Organization `dev-workspace` owns vpsFree commands, skills, cluster
  providers, site configuration and the private migration helper. Its
  initiative tail after retained predecessor history is exactly five commits:
  policy, package, complete schema-5 migration, workflow and site validation.
- The workspace owns repository policy, concrete user-side site data,
  bridge/final selection and cross-repository deployment proof. Its seven
  commits separate registration, configuration, consumption, source removal,
  bridge, final namespace and verification.
- Configuration owns privileged host values and activation. Its four commits
  are channel declaration, one generated exact pin, host-module adoption and
  concrete aitherdev defaults. The generated `confctl` message is untouched.

The retained predecessor commits in the organization repository preserve
filtered source provenance; they predate the initiative tail and have no
final-tree or runtime effect. Re-filtering them would destroy useful identity.

## Quick verification

- All five flakes pass `nix flake check --no-build`; all worktrees pass
  `git diff --check` and are clean.
- Correct tracked-file scans are empty for case-insensitive `vpsfree` and
  `aitherdev` in both generic repositories, and for `aitherdev` in the
  organization repository.
- Generic focused regressions pass 2 runs / 26 assertions with no failures.
  The preceding exact generic package build passed all packaged Go tests,
  285 Ruby lifecycle runs / 2715 assertions and 74 host-helper runs / 442
  assertions after deriving the corrected Go vendor hash.
- Organization migration passes 43 runs / 827 assertions with no failures,
  errors or skips against the exact generic runtime contract and corpus.
- Workspace deployment tests pass 2 runs / 9 assertions. The cross-worktree
  checker proves domain equality and shared generic revision `006de94`.
- Configuration was updated only through
  `confctl inputs channel set --commit`; Nixfmt and hooks passed, the generated
  message remains exact, and transient `.bin`/`.bundle` helpers were removed.
- Exact `codex-web` Actions run `34555724208` is green. Exact generic run
  `34560736452` and organization run `34561021962` are in progress.
  Superseded organization run `34559395554` accepted cancellation. The token
  still returns HTTP 403 when cancelling superseded generic runs.

Long full flake builds, the NixOS VM, bridge/final builds, aitherdev build and
dry activation remain deferred until all required v39 review lanes are clean.

## Review disposition and risk

Overall risk is **High**: persisted user/root state, credentials/TLS,
systemd/tmux ownership, destructive migration, public cross-project contracts,
deployment order and rollback all change. Run General, Architecture, Scope and
Risk with fresh `gpt-5.6-sol` agents at `xhigh`.

General should verify the rewritten commit boundaries and clean feature
histories. Architecture should verify exact contract ownership, the corrected
bridge identity, exact authority tuple, registered-root switch and preservation
runbook. Scope should verify that the v38 history and fixture cleanups remove
obsolete surface without losing required behavior. Risk should verify state
isolation, the occupied-target preservation procedure, migration safety,
quiescence and rollback. All lanes should report only current Blocking,
Important and Advisory findings plus residual gaps.

## Non-goals, rejected alternatives and fixed decisions

- Do not support mixed old/new runtime processes or final legacy aliases.
- Do not rewrite opaque identifiers or arbitrary serialized strings.
- Do not upgrade never-deployed migration journals.
- Do not infer or recreate a retained tmux server's old filesystem alias.
- Do not delete or merge the isolated test-recovery data during deployment.
- Do not expose the private migration helper as a normal user command.
- Do not duplicate organization/site values inside generic providers.
- Do not integrate default branches without explicit authorization.
- Do not merge the configuration branch merely to deploy aitherdev.
- Do not archive, delete or permanently retire the initiative.
