---
lifecycle: complete
---

# 2026-09-07-fix-ip-charged-environments

## Repositories

- `vpsfree-maintenance-tasks`
  - branch: `2026-09-07-fix-ip-charged-environments`
  - worktree:
    `worktrees/2026-09-07-fix-ip-charged-environments/vpsfree-maintenance-tasks`
  - base: `origin/master` at
    `996585953bf54fe928843e7f21b7fd501a31375f`
  - pushed head: `6eea682ede8d8e2634b2d41e5b11cf0f02231bc6`
- `vpsadmin`: read-only implementation and disposable-test reference; no source
  changes.
  - reference branch: `2026-09-07-fix-ip-charged-environments`
  - worktree:
    `worktrees/2026-09-07-fix-ip-charged-environments/vpsadmin`
  - base: `origin/master` at
    `cd3fac386ee34ba81387c379b2b48aee9170111f`

## Current status

- Investigation confirmed that disowning an owned IP whose
  `charged_environment_id` is null fails in
  `TransactionChains::Ip::Update#reallocate_user` while looking up an
  `EnvironmentUserConfig` with `environment_id IS NULL`.
- The maintenance task discovers affected `any`/`vps` addresses, excludes
  export targets, infers environments from the assigned VPS location or the
  unassigned network's primary location, and groups work by user ID and IP
  resource.
- The preview omits user logins. It lists each target IP, VPS assignment where
  applicable, inferred environment, every charged IP contributing to expected
  accounting, existing row IDs, allocation, total use, and free capacity.
- Plain numerical mismatches are now proposed accounting corrections. The task
  creates or updates the environment's IP `ClusterResourceUse` with admin
  override, leaves the `UserClusterResource` allocation unchanged, and allows
  `free` to become negative.
- Structural inconsistencies still block the entire owner/resource group. This
  includes missing or ambiguous environment/config/resource rows, dangling or
  wrongly targeted resource uses, disabled/unconfirmed/admin-locked uses,
  unclassifiable charged IPs, invalid interfaces, owner/VPS or owner/export
  mismatches, unavailable or conflicting charged environments, non-positive IP
  sizes, invalid address/prefix data, hard-deleted VPS links, and relevant
  out-of-scope uncharged IPs.
- Valid already charged export addresses participate in total IP accounting
  and are labeled as exports in the contributor list; the task never repairs
  an export-assigned target IP.
- The task requires a maintenance window. API, scheduler, supervisor, and other
  IP/accounting writers must be stopped and transaction chains drained. The
  `--writers-quiesced` flag is mandatory, and active transaction chains are
  checked before preview and again inside the apply transaction.
- Application locks, database row locks, exact plan revalidation, atomic
  updates, post-write verification, and allocation snapshots provide
  additional safety. Actual created/updated `ClusterResourceUse` IDs are
  printed immediately after commit and before application-lock cleanup. Every
  lock release is attempted; failures report the committed state, affected lock
  IDs, and an error that requires operator intervention.
- The final accounting commit is `6eea682`. It was pushed to the existing SSH
  feature branch and fast-forwarded to `origin/master`. GitHub reports no
  Actions workflows for the merged commit.
- Applied the workspace user-facing-writing and English humanizer guidance to
  the final preview, confirmation, maintenance-window, and recovery text.
- No production command has been run and no production data has been changed.

## Validation

- `ruby -c` passes for the task and disposable validation harness.
- `git diff --check` passes for the maintenance repository.
- Focused RuboCop `Lint` passes under the vpsAdmin API development shell with
  Ruby 3.4 target configuration.
- Disposable MariaDB validation passes against the vpsAdmin API version from
  the reported production stack using its JSON 2.21.2 dependency set.
- The validation covers missing-use creation, stale-use update, unchanged
  allocation, negative free capacity, contributor output without logins,
  successful atomic apply, idempotence, rollback of IP/PaperTrail/accounting
  writes after an injected failure, and admin locks whose recorded value
  already matches inventory.
- Review-remediation coverage also includes unexpected resource-use targets,
  dangling `UserClusterResource` links, missing `ClusterResource` links,
  unclassifiable charged IPs, owner/VPS mismatches, valid export contributor
  labeling, active transaction-chain refusal, and post-commit reporting of
  actual created and updated resource-use IDs.
- Final focused coverage includes charged/VPS environment conflicts,
  unavailable charged environments for unassigned IPs, positive size and
  address/prefix validation, charged and uncharged userless IPs attached to a
  default-scope-hidden hard-deleted VPS, and an injected post-commit lock
  release failure. The latter proves that the commit result and accounting IDs
  print first and that cleanup continues for every remaining lock.
- The standalone load-based entry point was previously reproduced with the
  deployed `vpsadmin-api-ruby` runner. The CLI executes at top level and does
  not depend on `$PROGRAM_NAME == __FILE__`.

## Review findings and disposition

- First High-risk review used General, Architecture, Scope, and Risk lanes with
  `gpt-5.6-sol` at `xhigh` reasoning.
- Blocking findings fixed after the first review:
  - config-side resource uses hidden by inner joins are now read and validated;
  - every use on the affected `UserClusterResource` is checked for the expected
    discriminator;
  - already charged contributors are classified and structurally validated;
  - owner/VPS mismatches and invalid contributors block instead of being
    silently counted;
  - admin locks block even when the current numerical total already matches;
  - the unsupported online-safety claim was replaced by an explicit quiesced
    maintenance-window contract.
- Important findings fixed after the first review:
  - export contributors are distinguished from VPS contributors;
  - authoritative `UserClusterResource#used` and `#free` values drive totals;
  - exact created or updated accounting row IDs are printed after commit.
- Because those remediations changed the design and accepted concurrency
  boundary, General, Architecture, Scope, and Risk were rerun on `a8683a5` with
  the same model and effort. Scope reported no findings. General and
  Architecture found missing handling for hard-deleted VPS links and
  charged/VPS environment disagreement. Risk also found unavailable charged
  environments, non-positive or address-invalid inventory, and loss of the
  post-commit audit output when lock cleanup fails.
- `6eea682` fixes every rerun finding. Focused disposable-DB cases exercise each
  fix. The fixes add narrow fail-closed validation and cleanup reporting inside
  the reviewed boundary; they do not add a new design, public contract, or
  supported execution mode, so another reviewer rerun is not required by the
  mandatory-review workflow.
- Hard-kill recovery prints every lock target before acquisition and every
  acquired `ResourceLock` ID. An operator must first prove that no task copy is
  running and then remove only lock rows proven orphaned for those targets.
- Task output contains infrastructure identifiers and must be retained as
  restricted operational evidence.

## Commands and environment notes

- Session and worktrees were created with `dev-session` under this slug.
- The feature branch uses SSH remote
  `git@github.com:vpsfreecz/vpsfree-maintenance-tasks.git`.
- The repository declares no hook framework. Ruby syntax, focused RuboCop, the
  disposable database harness, and diff checks are the available local checks.
- Entering `nix develop .#api` changes the working directory to `api`; paths in
  commands and disposable harnesses must account for that.
- The current vpsAdmin source lock selects JSON 3, which cannot boot the tested
  ActiveSupport serialized attributes. Validation therefore uses the deployed
  wrapped Ruby environment with JSON 2.21.2.
- An attempted standalone `nixpkgs#rubyPackages.rubocop` invocation had an
  inconsistent Prism dependency. The vpsAdmin API development-shell bundle
  provided the successful focused RuboCop run; a durable note records this.
- Fetched `origin/master` before integration; it remained at the initiative
  base, so no rebase was required.
- Pushed `6eea682` to
  `origin/2026-09-07-fix-ip-charged-environments` with an explicit lease against
  the previous remote head `c3d8b49`.
- Published the unchanged vpsAdmin reference branch at
  `cd3fac386ee34ba81387c379b2b48aee9170111f` so both registered initiative
  branches are retained locally and remotely.
- Created a fresh detached integration worktree from `origin/master`, merged
  the feature branch with `git merge --ff-only`, reran Ruby syntax and
  `git diff --check`, and pushed the exact resulting commit to
  `origin/master`.
- Verified after fetching that `origin/master` is
  `6eea682ede8d8e2634b2d41e5b11cf0f02231bc6`. GitHub reports no Actions runs
  for that commit.
- The installed `dev-session` profile lacked the documented `finalize`
  subcommand. After checking the current workspace implementation, used the
  version-controlled `./libexec/dev-session finalize` with the same slug and
  safety contract. A durable note records the mismatch.

## Cleanup

- Finalization removed both clean initiative project worktrees. Their feature
  branches remain available locally and on `origin`.
- Removed the clean detached integration worktree after the default-branch
  push and remote-ref verification.
- Removed the ignored disposable harness, generated API `Gemfile.lock`, local
  Bundler cache, and temporary lint/commit-message files after validation. The
  Bundler cache was moved to the desktop trash because direct recursive removal
  is disallowed in this environment.
- No production command has been run and no production data has been changed.

## Operator follow-up

- Run the task during the documented maintenance window when the production
  repair is scheduled. This is a separate operational action; the requested
  implementation, review, default-branch integration, and development cleanup
  are complete.

## Portal

- Stable initiative URL:
  `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-07-fix-ip-charged-environments/`
