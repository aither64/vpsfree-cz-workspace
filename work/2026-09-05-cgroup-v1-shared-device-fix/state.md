---
lifecycle: active
---

# Current state

## Outcome

The approved v2 shared-user regression follow-up is complete. Both local VM
suites, all required review lanes, and pushed-head CI passed. Both retained
feature branches are pushed; the production input selects the exact tested
vpsadminos revision. Nothing was merged, deployed, activated, or dry-activated.

Keep this initiative active for all remaining pre-merge follow-up. Do not
archive it or create replacement branches. There are no outstanding checks,
review findings, or cleanup tasks for the requested follow-up; the next change
or integration action requires the user's next instruction.

## Repositories

Both repositories retain branch `2026-09-05-cgroup-v1-shared-device-fix`.

- `vpsadminos`:
  - worktree: `worktrees/2026-09-05-cgroup-v1-shared-device-fix/vpsadminos`
  - base: `ec7dc42da33cd963fe63d8dde281b0e88fe790c2`
  - local and remote head: `5e31378ae42f253b4878940e3462f6e40b214fb4`
  - original runtime fix remains unchanged at `9fb79eb68`; the only new commit
    adds the cgroups-v2 tests.
- `vpsfree-cz-configuration`:
  - worktree: `worktrees/2026-09-05-cgroup-v1-shared-device-fix/vpsfree-cz-configuration`
  - base: `248e2fc614bb3bc29c0a9c9f910330ade0b3cb80`
  - local and remote head: `bc6071114994e4b481d3dc577adfeb6d98dafd16`
  - one consolidated generated production-input commit above the retained base.

Fetched upstream before pushes. Upstream staging advanced to `32767c7de` with
unrelated dependency updates; configuration master advanced to `4d570e30` with
workspace-host and unrelated input changes. Retained the authoritative bases
for this bounded follow-up instead of importing unrelated updates.

## V2 test implementation and review

- Added three ordered RSpec examples with two running Alpine containers sharing
  one osctl user: local TUN device deletion, chmod from `rwm` to `r`, and
  recursive removal from `/default`.
- Persistent `/root/test-tun` nodes and read-only/write-only opens verify real
  device access independently of configuration or TUN I/O. Denials require
  `Operation not permitted`. Assertions also cover BPF attachment shape,
  sibling/parent program stability for local changes, and health checks.
- Initial test commit `19e7601e` passed formatting/parsing, embedded Ruby syntax,
  whitespace checks, and active Nixfmt/commit-message hooks. Overcommit was
  installed and its reviewed configuration signature refreshed; RuboCop stays
  enabled but no Ruby source file was changed.
- Mandatory review classified the overall initiative high risk because of
  device isolation and production revision selection. Four fresh standalone
  `gpt-5.6-sol` reviewers at `xhigh` covered general, architecture/repetition,
  scope/proportionality, and risk/compatibility. All reported no findings.
- The first v2 VM run failed after 471.28 seconds. Both sibling-isolation cases
  passed, as did all four denied opens after recursive removal. The failing
  assertion expected a container program to reset from read-only TUN hash
  `858012c51ba` to default `946a3e34004`.
- Source and VM logs established that v2 group traversal visits child groups,
  unlike v1 which also visits containers. The v2 parent filter enforces the
  group denial without rewriting container-local programs. Corrected the test
  to retain effective denials, container attachment checks, restored parent
  policy, and final health checks; no runtime behavior changed.
- Amended the test commit to `5e31378ae`. Quick checks and active hooks passed
  again. Fresh general and risk reviewers at `xhigh` accepted the correction
  without findings. Architecture/scope were not rerun because no abstraction,
  interface, runtime behavior, or scope changed.
- Review packet and reconciliation: `review-v2-packet.md` and
  `review-v2-results.md`, both linked in the portal.
- Accepted limit: this covers immediate policy on running containers. It does
  not pin descendant program identities after parent removal or cover later
  parent re-expansion, restart, or reconfiguration.

## Local and GitHub verification

- `./test-runner.sh ls 'cgroups/devices-*'`: discovered both suites.
- `./test-runner.sh test 'cgroups/devices-v*'` on amended head `5e31378ae`:
  cgroups/devices-v2 passed in 439.27 seconds, cgroups/devices-v1 passed in
  442.22 seconds; total 881.49 seconds. All six shared-user examples passed,
  including the corrected final v2 parent/attachment/health assertions.
- Both local VM configurations used cached Linux 6.12.95; no local kernel
  compilation occurred. Both VMs shut down normally.
- Pushed vpsadminos over SSH from `9fb79eb68` to `5e31378ae`.
- [CI 34131696175](https://github.com/vpsfreecz/vpsadminos/actions/runs/34131696175)
  passed on the exact amended head: OS build/cache, Intel livepatch lifecycle,
  AMD livepatch lifecycle, and full test suite.
- Full CI suite: 266 scripts across 76 tests, all successful, in 2696.21
  seconds. CI devices-v2 passed in 148.10 seconds and devices-v1 in 94.04
  seconds. This test-only push did not trigger separate RuboCop/RSpec jobs.
- Inspected the full-suite log: its only script retry was the intentional
  `driver/rspec#script-attempts` test, which sets two attempts and deliberately
  fails the first using a marker. No workflow rerun or unexplained retry was
  used as validation. No superseded branch runs existed to cancel.

## Production input refresh

- Verified the retained configuration branch and remote were both `72af910e5`
  before changing the input.
- Used `confctl inputs channel set production vpsadminos 3bf14ec6...` without
  committing to restore the original input baseline locally, then
  `confctl inputs channel set --commit production vpsadminos 5e31378ae...` to
  generate the complete original-to-final changelog. No manual lockfile edit.
- Generated intermediate commit `45b05dcf`, then consolidated it with the
  original unmerged input update via an interactive `fixup -C` rebase onto the
  retained base. Final commit is `bc607111`. Verified its tree and generated
  message are byte-for-byte unchanged by consolidation, and exactly one
  input-update commit remains above the base.
- Applicable pre-commit and commit-message hooks passed. The generated message
  retained its text-width warning under the documented confctl exception.
- Verified only the production vpsadminos input node differs from the original
  configuration base. Every source identity field matches independent
  `nix flake metadata`: revision `5e31378ae42f253b4878940e3462f6e40b214fb4`,
  NAR hash `sha256-YU4USvAAIo1bes/kiMzqxtUH8lF0Gs0thiqpg2u1CCo=`.
  The independent metadata's `__final: true` bookkeeping marker is absent from
  lockfiles; verified and excluded it when comparing source fields.
- `nix flake check --no-build --no-update-lock-file`: all checks passed.
- The generated pin is a mechanical selection of already reviewed provider
  code and meets the review workflow's dependency-only skip criteria; no
  duplicate source review was needed.
- Fetched again and pushed over SSH with an explicit lease on old remote head
  `72af910e51cc729e65faa4a8507b9e3e0649be8b`. Remote now matches `bc607111`.
  This configuration branch has no triggered workflows or superseded runs.
- Full production node builds retain the established external limitation:
  deployment-only `/secrets/nodes/initrd/ssh_host_ed25519_key` is unavailable
  in normal feature worktrees. The approved follow-up did not repeat that
  known failed build or perform any deployment/activation.

## Session, tracking, and cleanup

- Resumed the explicitly requested initiative. Reopened active tracking was
  already committed as workspace `02a456c` before follow-up project changes.
- `dev-session start <slug> --as-is --no-attach --no-codex` initially rejected
  an old completed creation journal lacking newer provenance fields. Preserved
  it under a dated legacy filename while holding the per-slug lock, then the
  normal helper resumed the existing ready session. Verified current-session
  identity with both explicit slug and workspace environment variables.
- Stable portal:
  https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-05-cgroup-v1-shared-device-fix/
  Verified TLS with the documented public CA; the protected listener returned
  its expected HTTP 401 challenge without using credentials.
- Both project worktrees have attached retained branches, clean ordinary and
  ignored status, and heads matching their remote feature branches. Removed
  vpsadminos `.gems/`, `Gemfile.lock`, and `result/`, and configuration `.bin/`,
  `.bundle/`, and `.gems/` using verified untracked exact paths. No process
  remains that can write to either worktree.
- Preserved unrelated shared workspace changes. The initiative stays active
  with both worktrees and branches retained for the user's next instruction.
- Durable lessons:
  `notes/vpsadminos/2026-09-07-cgroup-v2-parent-device-denial.md`,
  `notes/cross-project/2026-09-07-completed-legacy-session-journal.md`,
  `notes/cross-project/2026-09-07-portal-curl-private-ca.md`, and
  `notes/cross-project/2026-09-07-nix-final-source-metadata.md`.

## Original v1 implementation and validation history

- `bin/dev-session current`: no owned prior session.
- `bin/dev-session start cgroup-v1-shared-device-fix --no-attach --no-codex`:
  created this managed initiative.
- `bin/dev-session worktree add 2026-09-05-cgroup-v1-shared-device-fix
  vpsadminos --as-is --base origin/staging`: created the vpsadminOS worktree.
- `nix develop --command nixfmt tests/suite/cgroups/devices-v1.nix`: passed.
- `nix develop --command bundle exec rubocop` for the changed Ruby
  implementation and unit spec: 2 files inspected, no offenses.
- Ruby syntax checks for the implementation and unit spec: passed.
- `nix-instantiate --parse tests/suite/cgroups/devices-v1.nix`: passed.
- `GITHUB_WORKSPACE="$PWD" nix develop .#vpsadminos --command bash
  .github/workflows/scripts/run-rspec-all.sh`: all 13 suites passed, including
  1,017 osctld examples and the new configurator examples.
- `git diff --check`: passed.
- Verified Overcommit is installed and both the configuration and Nixfmt hook
  signatures are present.
- Committed the implementation and regression coverage as vpsadminOS commit
  `9fb79eb68` (`osctld: keep container device denies private`). Overcommit's
  Nixfmt and RuboCop pre-commit hooks passed; the commit-message width hook
  emitted warnings for lines over its stricter 72-character preference, while
  all lines remain within the workspace's required 80-character limit.
- Mandatory change review ran with four fresh `gpt-5.6-sol` reviewers at
  `xhigh` effort, one each for general, architecture/repetition,
  scope/proportionality, and risk/compatibility. All four lanes reported no
  Blocking, Important, or Advisory findings.
- Review residuals were limited to the then-pending kernel-backed cgroup-v1 and
  cgroup-v2 VM runs, the accepted lack of automatic repair for already-damaged
  cgroups, optional stronger ordering/TUN-I/O assertions, and the accepted
  broader risk of the later 26-commit production-channel advance.
- `./test-runner.sh test cgroups/devices-v1`: passed in 423.05 seconds. All
  three new examples passed against the cgroup-v1 kernel interface.
- `./test-runner.sh test cgroups/devices-v2`: passed in 329.76 seconds as the
  unchanged cgroup-v2 regression guard.
- Both VM tests reused the cached vpsAdminOS `linux-6.12.95` kernel; no local
  kernel compilation occurred.
- Pushed the vpsadminOS branch to `origin` at full SHA
  `9fb79eb68ba4f7b9d9a9c6e2e985556a10aa725e`.
- GitHub Actions runs for that SHA:
  - RuboCop `33950917664`: passed;
  - RSpec `33950917681`: passed;
  - CI `33950917654`: passed, including the OS build/cache job, both livepatch
    lifecycle jobs, and the 1 hour 1 minute full test-suite job.
- Inspected and removed generated `.native/` and `libosctl/tmp/` trees. The
  command runner rejected exact-path `rm -rf`, so cleanup used verified exact
  paths with `find ... -depth -delete`; the reusable workaround is recorded in
  `notes/vpsadminos/2026-09-05-test-artifact-cleanup.md`.
- `bin/dev-session worktree add ... vpsfree-cz-configuration` created the
  requested branch and worktree, but returned non-zero because its
  post-checkout Overcommit hook could not load repository gems from the ambient
  shell. The worktree was verified as registered and clean, and subsequent
  hook-triggering commands ran through `nix develop`. This known behavior is
  documented in `notes/vpsfree-cz-configuration/2026-06-13-overcommit-hooks-need-nix-develop.md`.
- `nix develop --command bundle exec overcommit --version` and
  `--list-hooks` verified Overcommit 0.72.0 with Nixfmt and RuboCop enabled.
- `confctl inputs channel ls production` confirmed the original production
  vpsAdminOS pin `3bf14ec679229ab6c19387593e3a34db2da20220`.
- `confctl inputs channel set --commit production vpsadminos
  9fb79eb68ba4f7b9d9a9c6e2e985556a10aa725e` generated configuration commit
  `72af910e51cc729e65faa4a8507b9e3e0649be8b`. It changed only `flake.lock`,
  preserved the generated 26-commit changelog, resolved to the exact requested
  SHA and NAR hash, and passed the active Nixfmt pre-commit hook. Its generated
  message was left unmodified.
- The generated configuration pin is a dependency-only lock update selecting
  the already reviewed provider change, so it met the mandatory review
  workflow's skip criteria and did not receive a duplicate source review.
- `nix flake check --no-build --no-update-lock-file`: passed; all declared
  checks evaluated successfully.
- `confctl ls 'cz.vpsfree/nodes/{brq,pgnd,prg}/*'` selected all 11 production
  vpsAdminOS machines: brq node5/node6, pgnd node1, and prg backuper2 plus
  node19 through node25.
- `confctl build 'cz.vpsfree/nodes/{brq,pgnd,prg}/*' -y` composed the pinned
  inputs and reached derivation
  `vpsadminos-system-node5.brq.vpsfree.cz-26.05.git.9fb79eb`, then stopped at
  the documented external `/secrets/nodes/initrd/ssh_host_ed25519_key`
  dependency. That deployment secret is intentionally unavailable in normal
  feature worktrees. No derivation, Linux kernel, deployment, or activation
  was started. See
  `notes/vpsfree-cz-configuration/2026-07-13-confctl-node-build-initrd-secret.md`.
- Pushed the configuration branch to `origin` at full SHA
  `72af910e51cc729e65faa4a8507b9e3e0649be8b`. The repository has no
  push-triggered workflow for this branch.
- A final vpsAdminOS fetch found that `origin/staging` advanced after this
  branch's CI had started by one unrelated scheduled `nixpkgsUnstable` lock
  update (`09a29c7bb`). The feature and production pin intentionally retain the
  exact fully reviewed and green-CI SHA instead of invalidating that evidence
  to chase a moving scheduled-update target.
