# Configuration channel update execution

Package delivered and feature-published at
`e3ac35780cc909764a3bb059b4d9dfa23cf60867`; all assigned checks passed.
The lead accepted the source/history checks and relayed the user's explicit
configuration/master integration approval. The clean integration target and
Git-only hook environment are prepared; see
[integration preparation](configuration-integration-preparation.md). The lead
owns the merge critical section. No deployment was performed.

Implementer1 owns the downstream package from the accepted design addendum.
Its application scope is the generated `flake.lock` update for the `vpsadminos`
role of `staging` and `os-staging`. The lead owns the approved master integration
and summary state updates. Deployment remains outside this package.

## Preparation

- Bound session confirmed by `dev-session current` in the tracking directory:
  `2026-11-03-fedora-45-image-build`; both identity environment variables absent.
- Fresh SSH fetch confirmed configuration `origin/master`:
  `c4107822060e9e34b24a83950d618c9f28a7722b`.
- Dedicated worktree:
  `worktrees/2026-11-03-fedora-45-image-build/vpsfree-cz-configuration`, branch
  `2026-11-03-fedora-45-image-build`, registered in `portal.yml` with that exact
  initial base. Creation checked out the base successfully but the ambient
  post-checkout hook failed (exit 78, locked gems missing). No tracked changes
  resulted. Nix/hook setup is the recovery; no hook bypass.
- Current repository AGENTS, README, flake channel mapping and daily-update
  workflow checked. The workflow confirms CLI
  `github:vpsfreecz/confctl/822c0e35dbe2549111912f539116b4225dfd3035#confctl`,
  `--forward-only --commit`, and explicit `vpsadminos` role.
- Baseline committed lock exported outside the checkout as
  `configuration-baseline.lock` (raw supporting artifact).
- Both selected old pins: `b45b27b4330a08d85f413999e4bf66ba4503eee1`.
  `vpsadminosStaging` follows `nixpkgsStaging`; `vpsadminosOsStaging` follows
  `nixpkgsStable`; both preserve the `nixpkgsUnstable` follow.
- Routine generated updates need no new project documentation. Exact input
  revisions, imported changes, checks and recovery belong in this session.
- Fresh `/root/config_nix_hooks` (catalog Luna/low, full access, lifetime one
  operation) completed Nix and Overcommit preparation in 43s, exit 0. Hooks are
  installed; pre-commit signatures unchanged. See
  [setup result](config-preparation-result.md), `config-preparation.log`.
  No setup process remains; utility slot released to the lead.
- Supported `dev-session worktree add ... --base origin/master` retry after
  inspecting the successful checkout returned exit 0 and the intended path.
  Registration retained the exact baseline. Checkout remains clean.

## Dependency and acceptance

Pin mutation waits for the lead's verified vpsadminos/staging remote integration
proof. This dependency was satisfied: lead reported fast-forward integration
to `dd188397abe37d0bc33f4c5dfb3605206ce5e326`, fresh remote proof, and released
merge claim `af7e02bf-4552-4ba3-ab3f-66eb89c922ef` verified at 16:44:55Z.
Implementer1 independently confirmed that exact SSH remote head before starting
the guarded update. Fresh configuration fetch still showed `c4107822`.
The final package must preserve unrelated roots/follows, pass the
newer CLI's complete old/new committed-lock guard, list both channels and
evaluate selected `buildPlan.inputsInfo.vpsadminos` metadata for
`cz.vpsfree/nodes/stg/node1` and `cz.vpsfree/machines/build`. Keep the generated
changelog/message and active hooks. No fleet build is required.

One generated commit is the expected logical update stream. Apply the
mechanical generated-content review exemption only to the actual final diff;
record the complete branch history and explicit no-migrations conclusion.

Recovery before any deployment is reverting the generated update. This package
does not change live system state. Intervening imported vpsadminos changes need
their own target-specific assessment before a future deployment.

## Imported upstream range (prepared inventory)

The candidate range from the old pins to the Fedora feature head is
`b45b27b4330a08d85f413999e4bf66ba4503eee1..dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
This matches the integrated remote head independently verified before mutation.
The range contains eleven commits:

- `f40afdf844223410767a04d2a96215b1d796b967` packaged gem dependencies
- `449b1dc561bd76e574830a163210b916217940d2` nixpkgs update
- `8ce6234db194ccb934db724c7262aeab7fd26915` nixpkgs update
- `a5ad64f818a7a208e5f2308295c14c6a776eea6d` packaged gem dependencies
- `05201326975fc19d20a545c52f651cce0420dbc9` OOM killer queued-miss pruning fix
- `4dfed86538fcfaf7f5b43fdf2afcb2cadd4aa58d` CI Ruby patch selection
- `628b4a7c43b51d11ed8726188497a09f64814833` nixpkgsUnstable update
- `e4f9a472dad4a438b32606541749d12393d029be` nixpkgs update
- `823d7b7a84277edfd77f474fc1640a1cf756e8f7` both nixpkgs inputs update
- `5918f94e5e4eef3733b60aca4e03c1a6c0d43748` nixpkgs update
- `dd188397abe37d0bc33f4c5dfb3605206ce5e326` Fedora 45 addition

The upstream delta is 17 files (158 additions, 27 removals), including OOM killer
code/tests and packaged Ruby dependencies beyond the image. Upstream nixpkgs
lock movement is overridden by the configuration's existing follows edges;
the configuration's root selections must remain unchanged. No database or
on-disk migration is introduced by this range. Image verification does not
establish deployment compatibility for every intervening change.

## Generated result and quick checks

Guarded update completed in 53.47s, exit 0, producing
`e3ac35780cc909764a3bb059b4d9dfa23cf60867`. Full mutation log:
`config-channel-update.log`; status: `config-channel-update-status.json`.
The package owner launched the mutation; fresh Luna/low utility
`/root/config_update_watch` observed its independent status/log to completion.
The watcher first attempted identity discovery from an unbound directory and
stopped; its same-operation continuation from the exact bound directory
resolved identity. No operation was relaunched, no kernel build observed.

Only `flake.lock` changed: two raw nodes, six additions and six removals.
Both selected pins are exactly the remotely integrated
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`, source hash
`sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=`. The generated message and
complete eleven-commit changelog remain unchanged. Pre-commit and commit-msg
hooks passed; commit-message width warnings are permitted for generated confctl
messages. Working tree is clean and base-to-head `git diff --check` passed.

Complete semantic lock comparison passed (JSON parsed, 158 logical paths and
62 follows edges). Exactly six effective vpsadminos paths changed, including
four pre-existing downstream follows consumers; all 152 other logical paths
and every follows edge are unchanged. No descendant dependency change was
needed. Results: `configuration-lock-graph-result.json`.

Committed lock exports outside the checkout:

- `configuration-baseline.lock`: SHA256
  `507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098`
- `configuration-final.lock`: SHA256
  `6ccdd82be94a9d61571c9e6c5a67bd89ec9089116ccf6988a352e407e0702fd0`

### Mechanical review exemption and complete history conclusion

Applied `mandatory-change-review` step 1 to the actual final diff: this is a
mechanically generated dependency lock update with no handwritten substantive
content. Standalone content review is exempt. The complete configuration
base-to-head series is the single generated commit `c4107822..e3ac3578`, one
logical vpsadminos channel-update stream covering staging and os-staging.
There are no repeated or superseded update commits, transitional approaches,
unused compatibility paths, or migrations. No configuration change was
released, deployed or externally consumed. No history consolidation is needed.
This is the implementer's complete history inventory. The lead will obtain the
required independent whole-branch history/no-migrations conclusion; no redundant
substantive content review is required for generated pins. This inventory does
not grant configuration-master merge approval.

## Complete verification batch

Fresh Luna/low utility `/root/config_final_checks` ran the three read-only
commands at exact `e3ac35780cc909764a3bb059b4d9dfa23cf60867`. All exited 0,
54s total, no process remains; single utility slot is released.
[Result](config-final-checks-result.md), raw output `config-final-checks.log`:

- Newer CLI `inputs check-update` over exported committed baseline/final locks
  passed, reporting exactly six expected vpsadminos paths.
- Newer CLI `inputs channel ls '{staging,os-staging}'` confirmed both vpsadminos
  roles at `dd188397`; staging nixpkgs remains `718f670e`, vpsadmin `ff730be4`.
- `nix eval --impure --json` selected `confctl.buildPlan` input metadata:
  `cz.vpsfree/nodes/stg/node1` uses `vpsadminosStaging` and
  `cz.vpsfree/machines/build` uses `vpsadminosOsStaging`; both exact revisions
  are `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.

The initial JSON parser assertion rejected the dev-shell startup banner in
`config-inputs-info.json`. Parent extracted its one JSON object and confirmed
the exact selected identities; raw stdout remains in the complete log. This
was an artifact formatting correction, with no rerun or source mutation.
The exported final lock equals `git show HEAD:flake.lock` byte for byte.
Fresh fetch after the batch still found configuration `origin/master` at
`c4107822060e9e34b24a83950d618c9f28a7722b`; quick checks remain clean.

## Feature publication and handoff

`nix develop -c git push --set-upstream origin 2026-11-03-fedora-45-image-build`
succeeded over SSH with active hooks. Fresh SSH `ls-remote` proved:

- Feature branch: `e3ac35780cc909764a3bb059b4d9dfa23cf60867`
- Configuration `master`: `c4107822060e9e34b24a83950d618c9f28a7722b`

`dev-session worktree capture-comparison` saved that exact base/head. The
checkout remains clean. Exact-head GitHub Actions listing returned no runs;
the repository has only its scheduled/manual daily-update workflow, with no
feature-push CI trigger. No workflow was dispatched or awaited.

The independent [history packet](configuration-history-packet.md) is complete.
All application work is the single generated lock commit; no master merge,
deployment, machine reservation or lifecycle action was performed.

Stable session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-fedora-45-image-build/>.
