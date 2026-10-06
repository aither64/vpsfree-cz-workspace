---
lifecycle: abandoned
---
# 2026-08-11-staging-cpu-monitoring

## Repositories

- `vpsfree-cz-configuration`
  - branch: `2026-08-11-staging-cpu-monitoring`
  - worktree:
    `worktrees/2026-08-11-staging-cpu-monitoring/vpsfree-cz-configuration`
  - base: `origin/master` at `c29a3c3442cddc9b7164d28bfbb6ff031c8d3ccb`
  - integration branch: `master`
  - temporary integration worktree:
    `worktrees/2026-08-11-staging-cpu-monitoring/vpsfree-cz-configuration-merge`

## Status

- Commit `f35f6d3b` is merged into local and remote `master`. Pre-push
  integration checks and cleanup are complete. Nothing was deployed.

## Commands run

- Verified `VPSFREE_DEV_SESSION_SLUG` and `bin/dev-session current` both report
  `2026-08-11-staging-cpu-monitoring`.
- Fetched `origin` for `vpsfree-cz-configuration`.
- Created the feature branch/worktree from current `origin/master` using
  `bin/dev-session worktree add`.
- Evaluated `modules/clusterconf/monitor/rules/nodes.nix` with
  `nix-instantiate --eval --strict --json` and checked the intended rule pairs
  with `jq`.
- Validated the evaluated rule file with `nix shell nixpkgs#prometheus.cli
  --command promtool check rules --lint-fatal /dev/stdin`.
- Installed hooks with `nix develop -c bundle exec overcommit --install` and
  ran `nix develop -c bundle exec overcommit --run`.
- Committed the focused rule change as
  `f35f6d3b1788ef9cd644c10b55d6e2645980769b` (`monitor: relax staging node CPU
  and load alerts`).
- Ran `nix develop -c confctl build -y
  cz.vpsfree/containers/prg/int.mon1`.
- Ran `nix develop -c confctl build -y
  cz.vpsfree/containers/prg/int.mon2`.
- Re-fetched `origin`; `origin/master` remained at the feature base, so no
  rebase was needed.
- Created a fresh detached integration worktree from `origin/master` and ran
  `git merge --ff-only 2026-08-11-staging-cpu-monitoring`.
- In the integration worktree, installed and ran Overcommit, then rebuilt
  `cz.vpsfree/containers/prg/int.mon1` and
  `cz.vpsfree/containers/prg/int.mon2` serially.
- Re-fetched immediately before push and verified `origin/master` was the
  direct parent of the integration head.
- Pushed with `nix develop -c git push origin HEAD:master` over the configured
  SSH remote.
- Fetched the pushed ref, switched the integration worktree to local `master`,
  and fast-forwarded it to the feature branch with `git merge --ff-only`.
- Queried GitHub Actions for commit `f35f6d3b`; no run was created.
- Moved generated `.bin`, `.bundle`, `.rubocop_cache`, and `.confctl` content
  from both project worktrees to temporary storage.
- Removed the feature and integration worktrees with
  `bin/dev-session worktree remove`.

## Results

- The initial worktree checkout was clean at the recorded base commit.
- Checkout printed the known ambient-shell Overcommit/Bundler error after the
  checkout completed. Hooks were subsequently installed and passed inside
  `nix develop` before committing.
- Prometheus target discovery already exports `location="stg"` for both staging
  nodes. Alertmanager severity inhibition uses `alertclass` and `instance`, not
  `alertname` or `location`.
- Added six uniquely named staging rules and excluded `location="stg"` from
  the corresponding existing rules. CPU staging alerts wait 50 minutes; load
  staging alerts wait 10 minutes.
- The structural rule assertions passed: all alert names are unique, staging
  and default selectors are disjoint, thresholds/durations are correct, and
  staging labels match existing labels plus `location="stg"`.
- `promtool` passed all 69 evaluated node alert rules with fatal duplicate lint
  enabled.
- Overcommit passed both Nixfmt and RuboCop.
- The commit-time Nixfmt and commit-message hooks passed. The TextWidth hook
  warned about its 72-character preference, but every commit-message line is
  within the workspace-required 80-character limit (maximum 74).
- The committed worktree is clean. Dev-shell-created `.bin`, `.bundle`, and
  `.rubocop_cache` directories were moved to temporary storage rather than
  retained in the worktree.
- Mandatory change review completed with no blocking or important findings.
  The reviewer confirmed the requested durations and selectors, preserved
  `alertclass`/`instance` inhibition behavior, focused commit history, and
  Prometheus rule validity. Its only advisory was to correct stale initial
  checkout wording in this file; that wording is corrected above.
- The reviewer identified the then-pending `int.mon1`/`int.mon2` builds and the
  absence of a live-series firing replay as residual gaps. Current target
  generation and node metadata support `location="stg"` as planned.
- `int.mon1` built successfully as generation `2026-08-11--19-01-12`. The
  build included the generated Prometheus rule file, NixOS `checkrules`, and
  full Prometheus configuration validation.
- `int.mon2` built successfully as generation `2026-08-11--19-02-19`, including
  full Prometheus configuration validation.
- The review's build gap is resolved. No live-series replay or deployment was
  performed.
- The worktree is clean at commit `f35f6d3b`; dev-shell `.bin`, `.bundle`, and
  `.rubocop_cache` directories created during final builds were moved to
  temporary storage.
- The fresh integration worktree passed Overcommit (Nixfmt and RuboCop).
- Integrated `int.mon1` built successfully as generation
  `2026-08-11--19-06-35`; integrated `int.mon2` built successfully as
  generation `2026-08-11--19-07-27`.
- Remote `master` was fast-forwarded from `c29a3c34` to `f35f6d3b` over SSH.
  Local `master`, `origin/master`, and the retained feature branch all resolve
  to the same commit.
- The repository has no push-triggered GitHub Actions workflow; its only
  workflow is the scheduled/manually dispatched daily update. Therefore no CI
  run is expected for this push.
- Verified local `master`, local `2026-08-11-staging-cpu-monitoring`, and
  `origin/master` all resolve to `f35f6d3b` after worktree removal.

## Open questions

- None.

## Cleanup

- Complete: both project worktrees and their transient cache/build content were
  removed.
- The local feature branch is retained as required. No remote feature branch
  was created.
- Initiative plan and state records are retained for future reference.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
