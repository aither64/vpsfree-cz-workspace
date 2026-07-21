# 2026-07-20-security-advisory-review

## Repositories

- Top-level coordination repository
  - Branch: `master`
  - Worktree: `/home/aither/workspace/ai/vpsfree.cz`
  - Scope: add `security-advisories` to `AGENTS.md`; preserve and do not commit
    unrelated existing changes.
- `security-advisories`
  - Bare clone: `repos/security-advisories.git`
  - Remote: `git@github.com:vpsfreecz/security-advisories.git`
  - Branch: `2026-07-20-security-advisory-review`
  - Worktree: `worktrees/2026-07-20-security-advisory-review/security-advisories`
  - Base: current `origin/2026-07-13-security-advisory-automation`
- `vpsadmin`
  - Bare clone: `repos/vpsadmin.git`
  - Remote: `git@github.com:vpsfreecz/vpsadmin.git`
  - Branch: `2026-07-20-security-advisory-review`
  - Worktree: `worktrees/2026-07-20-security-advisory-review/vpsadmin`
  - Base: `origin/master` at
    `1bca29dfac3dba6a82a857ffad24d42e46ae861e`
  - Follow-up branch: `2026-07-21-security-advisory-localized-notes`
  - Follow-up worktree:
    `worktrees/2026-07-20-security-advisory-review/vpsadmin`
  - Follow-up base: `origin/master` at
    `88f03da4455f4d709ca64785b1db14db834f323a`
- `haveapi`
  - Bare clone: `repos/haveapi.git`
  - Remote: `git@github.com:vpsfreecz/haveapi.git`
  - Branch: `2026-07-20-security-advisory-review`
  - Worktree: `worktrees/2026-07-20-security-advisory-review/haveapi`
  - Base: `origin/master` at `e3749669d6034d529095ccbd3a40148fcb243a27`
- `vpsfree-cz-configuration`
  - Bare clone: `repos/vpsfree-cz-configuration.git`
  - Remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
  - Branch: `2026-07-20-security-advisory-review`
  - Worktree:
    `worktrees/2026-07-20-security-advisory-review/vpsfree-cz-configuration`
  - Base: `origin/master` at
    `36c0e9ba2f5cdca43d4d3b0541c6b6fa809f699d`
- `vpsadmin-kb-captures`
  - Bare clone: `repos/vpsadmin-kb-captures.git`
  - Remote: `git@github.com:vpsfreecz/vpsadmin-kb-captures.git`
  - Branch: `2026-07-21-security-advisory-localized-notes`
  - Worktree:
    `worktrees/2026-07-20-security-advisory-review/vpsadmin-kb-captures`
  - Base: `origin/master` at
    `6d10db3f9a395c5e786c5dc9c39019920d1f83c8`
- `vpsfree-notification-templates`
  - Bare clone: `repos/vpsfree-notification-templates.git`
  - Remote: `git@github.com:vpsfreecz/vpsfree-notification-templates.git`
  - Branch: `2026-07-20-security-advisory-review`
  - Worktree:
    `worktrees/2026-07-20-security-advisory-review/vpsfree-notification-templates`
  - Base: `origin/master` at
    `7da522e060fc18d5426e1dd6cd305b6847faf5ed`
  - The templates do not render per-Node notes, but the managed Czech advisory
    announcement included the old mitigation label and can override the
    built-in vpsAdmin mail.
- `vpsf-status`
  - Inspection only at `origin/master`
    (`9c19b23fb245910054d54f67496428f73af15f02`).
  - `security_advisories.go` fetches only advisory-level localized summary,
    description, response, CVEs, timestamps, state, and affected-Node count.
    Its client interface does not list per-Node statuses, so localized Node
    notes require no change in this repository.

## Status

- Diagnosis, implementation, mandatory review, broader verification, and the
  requested `vpsadmin` channel pin are complete and merged to both default
  branches. The configuration change has not been deployed to production.
- Advisory authentication is configured outside repository content. The token
  has not been printed, committed, or copied into work notes.
- Review of all five committed advisories is complete against one canonical
  typed production snapshot. Each advisory received a separate standalone
  review task, followed by an independent cross-check of exact build identities,
  fix ancestry, role applicability, and final Node states.
- The evidence collector now completes against continuously reporting Nodes,
  and repository instructions explicitly exclude backup/NFS-only storage Nodes
  from VPS-only kernel exposure.
- All five reviewed advisories have been synchronized to vpsAdmin as drafts and
  pass the read-only readiness check. None has been published.
- The corrected security-advisories change is committed as a focused series:
  collection consistency, configuration-identity compatibility, release
  classification, storage policy, one commit per CVE, and dossier invariants.
  Mandatory review findings have been addressed in focused follow-up commits.
  The final standalone verification passed without any remaining finding. The
  branch is pushed and its RSpec and RuboCop workflows passed.
- The follow-up redesign is complete and pushed: public English/Czech text is
  compact and uniform, reviewed per-Node evaluations are tracked beside each
  dossier, and fresh sync/readiness checks compare in memory without rewriting
  the review record. Mandatory standalone review and all local and GitHub
  checks passed.
- The useful kernel-warning monitoring statement has been restored uniformly
  for the four memory-lifetime advisories. Periodic evidence-sample churn no
  longer blocks an otherwise identical reviewed conclusion. The resulting
  commits, generated submission baselines, five remote drafts, readiness
  checks, and final CI are complete.
- The localized-note follow-up is in progress. The accepted design uses the
  historical `Local privilege escalation` / `Lokální eskalace oprávnění`
  titles, omits all notes from the current five evaluations, and permits future
  notes only as explicit bilingual per-Node exceptions. Per the follow-up
  decision, the legacy English `note` API alias will be removed rather than
  retained. `vpsf-status` is also being inspected as a possible consumer. The
  work includes no vpsAdmin deployment, configuration-channel update, KB
  publication, template upload, or advisory publication.

## Commands run

- `bin/dev-session current`
- `git status --short --branch`
- Inspected the existing `AGENTS.md` diff to identify unrelated shared changes.
- Inspected the advisory bare clone's remotes, refs, registered worktrees, and
  repository-local `AGENTS.md`.
- Queried the upstream symbolic `HEAD` and branch refs with `git ls-remote`.
- `bin/dev-session worktree add 2026-07-20-security-advisory-review
  security-advisories --as-is --branch
  2026-07-20-security-advisory-review --base
  origin/2026-07-13-security-advisory-automation`
- `git fetch origin master` in the top-level coordination repository.
- Verified advisory worktree registration, branch/ref identity, SSH remote,
  clean status, installed Overcommit hooks, and `git diff --check` results.
- Committed the scoped coordination changes with `git commit -F` and pushed
  top-level `master` over SSH.
- Fetched current vpsAdmin and HaveAPI `origin/master`, read their local
  `AGENTS.md` files, and created initiative worktrees from those refs.
- Traced the advisory client's token scope payload through HaveAPI's token
  request input and vpsAdmin's MFA continuation handling and schema.
- Measured the exact serialized continuation payload with Ruby/JSON.
- Ran a temporary, uncommitted RSpec reproduction through
  `nix develop .#api`; the temporary spec was removed after the run.
- `nix develop .#api -c bash -lc 'bundle exec rspec
  spec/lib/vpsadmin/api/authentication/token_config_spec.rb --format progress'`
- Regenerated `api/db/schema.rb` from an isolated MariaDB instance with
  `VPSADMIN_PLUGINS=none`, then verified that only the schema version and
  `auth_tokens.opts` type changed.
- Ran the new migration spec and token-configuration spec in separate RSpec
  processes after confirming that combining them leaves ordinary examples on
  the intentionally minimal migration-spec database.
- `ruby tools/check_migration_specs.rb --cached`
- `nix develop -c overcommit --run`
- `nix develop -c git commit -F /tmp/vpsadmin-token-opts-commit-message`
- `git fetch origin master`
- `git push -u origin 2026-07-20-security-advisory-review`
- `nix develop -c confctl inputs channel set --commit vpsadmin vpsadmin
  b3ec1a757c51b639b6442cd2552401688061b3e3`
- Ran 92 ordinary authentication, user-session, authentication-task, and core
  schema examples together in the normal API test database.
- `nix develop -c confctl inputs channel ls`
- `nix develop -c confctl build -y` for `int.api1`, `int.api2`, `int.webui1`,
  and `int.webui2`, serially to avoid ConfCtl log collisions.
- Pushed the configuration feature branch from `nix develop` so its pre-push
  Overcommit hook could load the locked gems.
- Monitored vpsAdmin branch workflows with `gh run list`, `gh run view`, and
  `gh run watch`.
- Downloaded the failed serialized workflow's test-log artifact and inspected
  the exact failing test's `test-result.txt` and `test-runner.log`.
- Fetched both default branches, rebased the configuration feature branch onto
  its advanced `origin/master`, and force-pushed only that unmerged feature
  branch with an explicit lease.
- Created fresh default-branch integration worktrees, fast-forwarded them with
  `git merge --ff-only`, and pushed `vpsadmin` followed by
  `vpsfree-cz-configuration` over SSH.
- Removed the completed implementation, investigation, and temporary merge
  worktrees; retained the clean `security-advisories` worktree for the pending
  token-based review.
- Loaded the configured advisory API authentication without displaying it and
  collected only the typed evidence resources authorized by the repository.
- Diagnosed repeated live-collection revision failures, split immutable event
  history from mutable current evidence, and bracketed current components one
  Node at a time.
- Diagnosed an immutable historical digest mismatch caused by the optional
  software-component rename from `vpsfree_cz_configuration` to
  `system_configuration`; added an exact legacy digest compatibility path.
- Ran focused evidence collector, evaluator, and dossier evidence specs while
  iterating on the collector.
- Collected the canonical ignored schema-7 snapshot at
  `2026-07-21T08:16:20Z` and handed that same snapshot to the standalone
  advisory reviewers. Reviewers were instructed not to recollect, synchronize,
  or publish.
- Cross-checked every accepted deployment/software digest directly from the
  canonical Node 401 snapshots and used GitHub's primary compare API to confirm
  that the deployed Linux source descends from every dossier's 6.12 fix.
- Ran a final read-only collection with the completed collector at
  `2026-07-21T08:33:27Z`, then re-evaluated all five dossiers from that same
  snapshot.
- Ran complete RSpec, RuboCop, dossier validation, `git diff --check`, and
  Overcommit checks. Rewrote the unmerged commit into a focused collector commit
  and one atomic all-dossier review commit before mandatory review.
- Rejected the gap-driven result after cross-checking the retained release
  events and Node lifecycles. Added stable release classification, global
  introduction/fix boundaries, and reviewed lifecycle starts for Nodes 126 and
  401. Stored sampling gaps now retain timing provenance without erasing a
  classifiable boot or release state.
- Assigned the corrected per-CVE results back to standalone reviewers for
  independent checks of every state and mitigation timestamp.
- Collected the final read-only schema-7 snapshot at
  `2026-07-21T09:25:44Z` and evaluated all five advisories from it.
- Ran the corrected focused suite (84 examples), full suite (94 examples), and
  RuboCop. All RSpec examples passed; RuboCop initially reported one
  correctable `Style/Next` offense, which was fixed before committing.
- Committed the corrected implementation as ten focused commits from
  `490a42b` through `c652de1`; every commit ran the installed Overcommit hooks
  inside `nix develop`.
- Mandatory standalone review found two affected EOL stable backport sets that
  predate the global mainline introduction, fail-open version-range validation,
  stale snapshot provenance, and missing revision-pinned storage sources.
- Added explicit open-ended ranges for all six Linux CNA backport
  introductions, strict global and stable boundary validation, canonical YAML
  branch-key validation, regression coverage, and pinned production storage
  sources.
- Rewrote the unpublished follow-up history into separate validator, evaluator
  feature, per-CVE dossier, storage-source, and snapshot-provenance commits as
  required by the mandatory review.
- Collected the final read-only schema-7 snapshot at
  `2026-07-21T10:00:32Z`, then evaluated all five committed dossiers from it at
  `2026-07-21T10:12:56Z` through `2026-07-21T10:12:57Z`.
- Ran the final full suite (100 examples), RuboCop over 25 files, all-dossier
  validation, `git diff --check`, and Overcommit. All checks passed.
- The same standalone mandatory reviewer verified the corrected final tree and
  six-commit follow-up series. It reported no blocking, important, or advisory
  findings.
- The first advisory push outside the development shell stopped safely because
  the pre-push hook could not load the locked gems. Re-running the push through
  `nix develop` executed the hook and pushed the feature branch over SSH.
- Monitored GitHub Actions runs `29821548394` (RSpec) and `29821548391`
  (RuboCop) to successful completion for final head `67e7b2d`.
- Reviewed the five public English/Czech text sets side by side, defined a
  shared response closing, and added checks against generic non-action,
  editorial first-person, and internal storage-role wording.
- Added tracked evaluation persistence, explicit reviewed-evaluation loading,
  and fresh in-memory comparison for sync and readiness. Focused reconciler and
  dossier coverage passed: 24 examples, 0 failures.
- Collected one read-only schema-7 production snapshot at
  `2026-07-21T11:00:08Z`, updated all analysis provenance, and generated five
  tracked evaluation records. All five dry-run sync commands loaded the new
  paths successfully and performed no writes.
- Removed the five obsolete ignored `.state/<CVE>/evaluation.json` copies and
  retained only raw `.state/evidence.json` as local state.
- Committed the follow-up as `c9c7caa` (public language), `d6ffa82` (tracked
  evaluation workflow), and `adddaf6` (snapshot and reviewed records).
- Assigned the committed three-change series to a fresh standalone mandatory
  reviewer with the initiative plan/state, exact base/head commits, local
  verification, compatibility assumptions, and publication exclusions.
- Ran the final full RSpec suite (105 examples), RuboCop over 25 files,
  all-dossier validation, `git diff --check`, and the installed Overcommit
  hooks. All checks passed.
- Fetched the feature branch, confirmed its remote tip was still `67e7b2d`, and
  pushed the three follow-up commits over SSH from `nix develop`.
- Monitored GitHub Actions runs `29825092311` (RuboCop) and `29825092399`
  (RSpec) to successful completion for exact head `adddaf6`.
- Restored one passive factual EN/CS kernel-warning monitoring sentence on
  CVE-2026-23111, CVE-2026-43499, CVE-2026-46242, and CVE-2026-53359. Kept
  CVE-2026-53362 unchanged because its analyzed primitive is an out-of-bounds
  overwrite rather than a memory-lifetime/UAF bug.
- Collected one read-only schema-7 snapshot at `2026-07-21T11:28:47Z` with
  unchanged Node-set digest
  `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`
  and evidence digest
  `debd61c64eae1c18b68c40dadd4c2acd71e9f93bfb1f8ec53a237b8afb4dcef1`.
  Refreshed analysis provenance and all five tracked evaluations.
- A focused dossier run initially found that analysis provenance had been
  edited after evaluation, invalidating the dossier digest. Regenerated all
  evaluations after every dossier file was final; the complete dossier spec
  then passed. Recorded the ordering in
  `notes/security-advisories/2026-07-21-evaluate-after-dossier-final.md`.
- Changed preflight comparison to treat periodic evidence revisions and the
  resulting raw evidence digest as audit provenance while retaining exact
  Node-set and all other per-Node result-field comparisons. Focused reconciler
  and dossier coverage passed: 25 examples, 0 failures.
- Committed `8cf1d8e` (monitoring text and refreshed evaluations) and `9162d66`
  (periodic sample preflight), with installed hooks passing for both.
- The mandatory standalone reviewer reported no blocking, important, or
  advisory findings. It independently reproduced every evaluation and probed
  that Node-set, state, both interval endpoints, reason, note, role, kernel
  release, and configuration drift all fail before writes.
- Ran the final full RSpec suite (106 examples), RuboCop over 25 files,
  all-dossier validation, `git diff --check`, and Overcommit. All checks passed.
- Pushed the reviewed behavior at `9162d66`; GitHub Actions runs `29827055567`
  (RSpec) and `29827055557` (RuboCop) passed on that exact head.
- Ran dry-run synchronization for all five advisories. Each planned one new
  advisory with one CVE link and the exact 13 reviewed Node statuses; no
  existing remote advisory matched.
- Applied each synchronization sequentially. vpsAdmin created draft advisory
  IDs `6`, `7`, `8`, `9`, and `10`, all at content revision `13`, for
  CVE-2026-23111, CVE-2026-43499, CVE-2026-46242, CVE-2026-53359, and
  CVE-2026-53362 respectively. No publication action was called.
- Committed each generated `submission.yml` recovery baseline separately as
  `7229778`, `14f7e1b`, `1cd15d0`, `6380e89`, and `06ddc84`, then pushed the
  branch over SSH.
- Ran `bin/security-advisory ready` for all five drafts. Each fresh read-only
  preflight returned `ready: true`, the expected 13-Node completeness summary,
  its tracked advisory ID, content revision `13`, and no blocking Node IDs.
- GitHub Actions runs `29827735706` (RSpec) and `29827735679` (RuboCop) passed
  for final generated-baseline head `06ddc84`.

## Results

- Verified active session slug: `2026-07-20-security-advisory-review`.
- The bare clone already exists and uses the required SSH origin.
- Upstream `HEAD` currently resolves to
  `origin/2026-07-13-security-advisory-automation` at
  `55e26c3ad6bc548e7b40b0cc1dddd47c41e2da11`.
- The new advisory worktree is clean on
  `2026-07-20-security-advisory-review` at that same commit.
- The repository's Overcommit hooks are installed in the canonical bare
  clone. During worktree creation, the post-checkout hook could not find the
  locked RuboCop gems in the ambient shell; `bin/dev-session` recovered and
  completed the registered, clean worktree. Future hook/test commands must run
  from the repository's `nix develop` environment.
- The top-level `master` matched `origin/master` after fetching.
- Coordination commit `eaaf844f150dc52470ab8cb9ce001fd5cdb06350` was pushed
  to `origin/master`.
- `git diff --check` passed for the advisory worktree and this initiative's
  top-level documentation.
- Repository-local rules require evidence-backed platform assessment, resolved
  evidence before a publishable draft, and prohibit advisory publication.
- `security-advisories` requests 34 action scopes. Their space-separated value
  is 924 characters; vpsAdmin serializes the MFA continuation options to 1,042
  JSON bytes. The current `auth_tokens.opts` column is `VARCHAR(255)`, and the
  exact payload first exceeds that limit at the ninth scope (269 bytes).
- vpsAdmin creates the temporary `AuthToken`, then stores `lifetime`,
  `interval`, and the split scope list in `opts` before returning the TOTP
  continuation. Strict MariaDB therefore raises `ActiveRecord::ValueTooLong`.
  Forced-password-reset token continuations use the same column and have the
  same boundary.
- Password-only token issuance bypasses `auth_tokens.opts` and writes the final
  scope to `user_sessions.scope`, which is already `TEXT`. This explains why
  short or non-MFA token creation can work.
- HaveAPI accepts the scope as an unconstrained string but does not own the
  continuation persistence. The defect is in vpsAdmin's application schema;
  no HaveAPI change is needed.
- The exact long-scope MFA reproduction passed by observing the expected
  `ActiveRecord::ValueTooLong`: 1 example, 0 failures.
- The existing vpsAdmin token-config spec passed: 6 examples, 0 failures. It
  uses only the one-word `all` scope and does not cover MFA token issuance, so
  it cannot detect this overflow.
- Recommended fix: migrate `auth_tokens.opts` to `TEXT` with a 65,535-byte
  limit, regenerate the core-only schema, and add a token-config regression
  that completes MFA with a representative long scope and verifies the final
  session scope. No advisory-client scope broadening or MFA bypass is
  appropriate.
- The documented command must retain the versioned API URL and separate option
  argument: `bin/create-token --api https://api.vpsfree.cz/v7.0 --user LOGIN`.
  The unversioned URL and the displayed `--usermyuser` typo do not cause the
  reported database exception, but would make the saved configuration invalid
  for later versioned API resource requests or be rejected by `OptionParser`,
  respectively.
- Durable diagnostic note:
  `notes/vpsadmin/2026-07-20-auth-token-opts-overflow.md`.
- The `vpsfree-cz-configuration` worktree was created from current
  `origin/master`; its post-checkout Overcommit hook lacked locked gems in the
  ambient shell, and `bin/dev-session` recovered to a registered clean
  worktree. Hook and `confctl` commands must run from `nix develop`.
- Added a reversible core migration from `VARCHAR(255)` to `TEXT`, regenerated
  the core-only schema, and added migration plus end-to-end long-scope TOTP
  token coverage.
- The migration spec passed in both directions: 2 examples, 0 failures.
- The focused token-configuration spec passed: 7 examples, 0 failures.
- Migration specs use an isolated minimal database and must not share an RSpec
  process with ordinary API specs. Durable note:
  `notes/vpsadmin/2026-07-20-migration-spec-database-isolation.md`.
- Ruby syntax checks and `git diff --check` passed for all changed vpsAdmin
  files. The cached migration inventory confirmed that the new migration has a
  matching spec.
- A full explicit Overcommit run found one correctable string-concatenation
  style issue in the new migration spec. After correction, RuboCop passed for
  all three hand-written Ruby files, and the actual commit reran every
  configured pre-commit and commit-message hook successfully.
- vpsAdmin implementation commit:
  `b3ec1a757c51b639b6442cd2552401688061b3e3` (`api: allow long MFA token
  scopes`). The feature branch was pushed over SSH so the configuration flake
  could resolve the exact revision. Current `origin/master` remained at the
  recorded base before push.
- Before the final rebase, `confctl` updated only `flake.lock`, pinning
  `vpsadminServices` from
  `1bca29dfac3dba6a82a857ffad24d42e46ae861e` to the exact vpsAdmin feature
  commit. After rebasing onto the advanced configuration default branch, the
  generated commit is `791439abcec85a6c689837cae27758f65861904e`
  (`inputs: set vpsadminServices to b3ec1a75`). Its generated message was
  retained exactly.
- The configuration worktree is clean after removing `.bin/` and `.bundle/`
  files generated by development-shell setup.
- Mandatory standalone review completed with no blocking findings. It found
  one important documentation issue: logical five-minute expiry does not
  remove an overlong row until the scheduled `vpsadmin:auth:close_expired` task
  runs. Rollback guidance now requires confirmed cleanup and a zero result from
  `SELECT COUNT(*) FROM auth_tokens WHERE OCTET_LENGTH(opts) > 255`.
- The reviewer also advised that the existing boot-evidence deployment runbook
  pins all application and Node channels to its older release revision. The
  runbook now explicitly identifies those checks as release-specific so this
  later `vpsadminServices` application update is not mistaken for a violation
  of a current global pin. The rebased configuration documentation commit is
  `a2482851753e4e23dec488a34ee3a318e6cb1db5` (`docs: mark boot evidence
  pins as release-specific`).
- Reviewer residual gaps: broader API/configuration builds were still pending,
  production MariaDB DDL locking has not been measured, and the regression uses
  a representative over-255-byte 12-scope list rather than all 34 advisory
  scopes. The representative payload directly exercises the failed boundary;
  the exact 34-scope payload was separately measured and reproduced during
  diagnosis.
- Broader related API coverage passed: 92 examples, 0 failures across
  authentication configurations, authentication operations, user-session
  operations, the expired-authentication task, and the core-schema smoke spec.
- `confctl inputs channel ls` reports channel `vpsadmin`, role `vpsadmin`, input
  `vpsadminServices` at `b3ec1a75` while staging and production Node channels
  remain unchanged at `1bca29df`.
- Configuration builds passed serially for `int.api1`, `int.api2`, `int.webui1`,
  and `int.webui2`. The first `int.api1` invocation omitted `-y` and stopped
  safely at its confirmation prompt without building; the non-interactive
  rerun and all subsequent builds succeeded.
- The rebased configuration feature branch was pushed over SSH at
  `a2482851753e4e23dec488a34ee3a318e6cb1db5`. Its exact
  `vpsadminServices` pin remained unchanged through the rebase.
- vpsAdmin GitHub Actions passed RuboCop, API migration specs, libnodectld
  specs, i18n health, and all 26 parallel API/topic jobs for
  `b3ec1a757c51b639b6442cd2552401688061b3e3`. The separate serialized `CI`
  workflow run `29781749917` completed 116 of 117 integration tests and failed
  only `client/snapshot-download`. Its downloaded artifact shows that Nix
  evaluation stopped before the test ran because the runner no longer had the
  `rabbitmq-server-4.2.5.drv` store path. This pre-test runner/store failure is
  unrelated to the authentication-token schema and regression changes, so it
  does not block integration and was not treated as evidence repaired by a
  blind rerun. Durable note:
  `notes/vpsadmin/2026-07-21-ci-missing-rabbitmq-derivation.md`. The
  configuration repository produced no branch-triggered workflow runs.
- `vpsadmin` was fast-forwarded and pushed to `master` at
  `b3ec1a757c51b639b6442cd2552401688061b3e3`.
- `vpsfree-cz-configuration` was fast-forwarded and pushed to `master` at
  `a2482851753e4e23dec488a34ee3a318e6cb1db5`, after vpsAdmin was available at
  the pinned revision.
- On the vpsAdmin default-branch push, API migration specs, RuboCop, i18n
  health, and libnodectld specs passed. API topic specs run `29810531250`
  remains in progress and serialized CI run `29810531324` remains queued; the
  same commit already passed the feature-branch API topic run. The
  configuration repository has no workflow run for its default-branch push.
- The token-fix implementation stage performed no deployment, production
  database migration, production API request, or token handling. This later
  advisory stage made only authenticated read-only production API requests.
- The canonical advisory snapshot contains all 13 active Nodes: 12 compute
  Nodes with the `node` role and `backuper2.prg` with the `storage` role. It
  records `CONFIG_FUTEX_PI=y`, `CONFIG_IPV6=y`, `CONFIG_KVM=m`,
  `CONFIG_NF_TABLES=m`, and `CONFIG_USER_NS=y` for the deployed kernel
  configuration digest.
- Eleven current compute reports do not expose an exact kernel source revision.
  Stable release history nevertheless has enough typed evidence to classify
  upstream stable fixes. Node 401 additionally has two accepted exact fixed
  deployment/software identities; its optional dirty `system_configuration`
  identity is permitted by the evidence contract and retained in the software
  digest. No historical attestations were invented.
- The storage Node has no current kernel evidence, but that is not relevant to
  VPS-only advisories: it stores backups and exports data over NFS, and does not
  run VPS workloads. It is `not_affected` unless the advisory's primitive is
  reachable through its actual backup, NFS, or host workload.
- The original mandatory review blocked the first implementation because one
  Node collection could mix reconstruction data from a different evidence
  revision, the commit series bundled independent changes, and dossier
  invariants were too weak. The collector now brackets the complete per-Node
  bundle, its regression changes reconstruction between reads, the history is
  split by concern and CVE, and dossier tests lock the complete accepted build
  identities, roles, and lifecycle overrides.
- Focused evidence collector, evaluator, reconciler, dossier, and advisory
  coverage passed together: 84 examples, 0 failures. The final full suite
  passed: 100 examples, 0 failures; RuboCop inspected 25 files without an
  offense.
- The final schema-7 snapshot has evidence digest
  `252d2e0292cec6bb207e2cec73ae931384e8961cd5867aaa2cff593867810695`
  and the unchanged 13-Node set digest
  `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`.
- CVE-2026-23111 evaluates ten Nodes as `mitigated` and three as
  `not_affected`. CVE-2026-43499, CVE-2026-46242, CVE-2026-53359, and
  CVE-2026-53362 each evaluate twelve Nodes as `mitigated` and the storage Node
  as `not_affected`. All five have zero `unknown`, zero `vulnerable`, and no
  blocking Node IDs.
- Direct evaluator probes classify Node 401's exact event 700 and current
  snapshot as fixed for all five CVEs. GitHub compare results report the exact
  deployed Linux source `a2384967b90f24d2470c9eb15f0e66d938df7e08`
  ahead of all five 6.12 stable fixes with `behind_by=0`.
- Corrected security-advisories commits:
  `490a42b`, `28cf60a`, `7a2eaf0`, `a01eabe`, `ecfdb7f`, `60c890a`,
  `9c447c4`, `670a94a`, `4d82845`, `c652de1`, `8689387`, `bc75010`,
  `485ec5d`, `37562d1`, `b2acf0e`, and `67e7b2d`.
- Final mandatory standalone review passed at `67e7b2d` with no findings. The
  reviewer independently confirmed canonical branch validation, the focused
  history, 13-Node coverage, snapshot provenance, and source-pinned storage
  exclusions.
- Feature branch `2026-07-20-security-advisory-review` was pushed over SSH at
  `67e7b2d412b83c23f2f5295bc8a96046229d66d7`. Its RSpec and RuboCop GitHub
  workflows passed.
- The follow-up production snapshot contains the unchanged 13-Node set digest
  `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`
  and evidence digest
  `479926d12587cb805955230ae9799be01d4564edc1a462bb5dd168c86d42a68f`.
  CVE-2026-23111 remains ten `mitigated` and three `not_affected`; every other
  advisory remains twelve `mitigated` and one `not_affected`, with no blocking
  Node.
- Each `advisories/<CVE>/evaluation.json` is tracked, contains all exact 13
  reviewed Node IDs, matches its dossier digest and shared evidence digest, and
  records `backuper2.prg` as storage and `not_affected`.
- Reviewed evaluations no longer expire by wall-clock age. `sync --apply` and
  `ready` instead recollect evidence without rewriting the tracked file and
  require matching Node-set, evidence, and canonical per-Node results.
- The follow-up mandatory standalone review reported no blocking, important,
  or advisory findings. It independently reproduced the tracked evaluations
  from the retained evidence and confirmed fail-closed comparison before remote
  writes. Residual risks are limited to the normal lack of a fleet-wide lock
  after preflight and intentionally omitted real apply/ready integration; a
  later run detects evidence drift before it can proceed.
- Feature branch `2026-07-20-security-advisory-review` is pushed over SSH at
  `adddaf60c386a671676ae24afda22132ed55a437`. Its final RSpec and RuboCop
  GitHub workflows passed.
- The restored public monitoring sentence is present in matching passive EN/CS
  form on the four memory-lifetime advisories and absent from CVE-2026-53362.
  Generic user non-action, first-person editorial, and public storage-role
  wording remain excluded.
- Periodic Node report sampling changes `evidence_revision` and the evidence
  digest without necessarily changing the evaluated outcome. Those values are
  retained in tracked records as provenance; apply/readiness comparisons omit
  only `evidence_revision` and still require the exact Node set and every other
  per-Node result field.
- vpsAdmin draft mapping: CVE-2026-23111 is advisory `6`, CVE-2026-43499 is
  `7`, CVE-2026-46242 is `8`, CVE-2026-53359 is `9`, and CVE-2026-53362 is
  `10`. All are drafts at content revision `13`, contain 13 Node statuses, and
  passed a subsequent fresh readiness check. None is published.
- Final feature branch head is
  `06ddc840b6f1ad56c607c3b5a15fa7e9d9dab59c`; its RSpec and RuboCop GitHub
  workflows passed.
- Durable collector note:
  `notes/security-advisories/2026-07-21-live-evidence-collection.md`.

## Localized-note follow-up

- vpsAdmin commit `438a92515` adds the Node-status translation table, explicit
  `en_note`/`cs_note` API fields, localized administrator inputs, locale-aware
  public rendering with English fallback, and generated API/WebUI catalogs.
  The migration copies legacy values into English translation rows and removes
  the `note` column. Rollback recreates the column from English before dropping
  the table; Czech is intentionally lost. The legacy `note` field is not
  exposed as an API compatibility alias.
- vpsAdmin focused verification passed: 3 localized Node-status API examples,
  2 bidirectional migration examples, 3 WebUI examples, API i18n health, WebUI
  gettext health, migration-spec coverage, and all Overcommit hooks.
- security-advisories commits `25d0b99`, `4f4f656`, and `018fc1c` separately
  add reconciler compatibility, define the bilingual dossier/evaluator
  contract, and activate strict schema 4 with all five reviewed dossiers and
  generated evaluations. The reconciler accepts exact schema-1 submission
  baselines, clears empty generic notes through the deployed legacy API, and
  refuses to flatten non-empty bilingual notes before the localized API is
  deployed.
- A fresh read-only production collection at `2026-07-21T13:54:17Z` has Node
  set digest
  `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`
  and evidence digest
  `d3ef095d5e0d5b701ff8384d9f61e3e8abb00ae9dc015e5917ab87340f45148a`.
  All five evaluations cover the same 13 Nodes, have no blocking states or
  public notes, and retain Node 161 as workload-excluded storage.
- The full security-advisories suite passed with 113 examples; RuboCop checked
  25 files without offenses and Overcommit passed.
- `vpsfree-notification-templates` at `7da522e` and `vpsf-status` at `9c19b23`
  do not consume advisory Node-status notes, so neither needs a code change.
- The localized-note mandatory change review found one blocking commit-series
  issue, two important implementation issues, and one advisory wording issue:
  `dbc2772` combined independently reviewable concerns, one-time English
  backfill could become stale under old API writers, `after_initialize` added a
  translation query per Node status, and Czech API summary metadata retained
  the old sentence wording.
- The implementation fixes remove all database work from `after_initialize`
  and bulk-preload translation rows. Regression coverage proves two localized
  statuses use one translation query. The Czech metadata now describes the
  short vulnerability-class title.
- The user selected a normalized translation-only schema instead of the
  temporary canonical-English-column design. Because old code requires the
  removed column, deployment must drain every old API and WebUI process before
  running the migration and starting the new code; mixed old/new service
  operation is unsupported at this boundary.
- Each coherent security-advisories intermediate commit passed the full suite:
  109 examples at `25d0b99`, 111 at `4f4f656`, and 113 at `018fc1c`.
- vpsadmin-kb-captures commit `f6c8207` is the single consolidated pin update;
  `flake.nix`, `flake.lock`, `captures.json`, and `contract/navigation.yml` all
  reference exact vpsAdmin commit
  `438a92515fe397b32e94923d84eea76edc39e327`.
- The KB contract check passed at that exact pin: 39 controls, 29 paths, 32
  capture concepts, 3 selectors, 65 bindings, 9 exceptions, and all contract,
  routing, inventory, and screenshot assertions.
- A fresh storage-topology development cluster was started with the bridge
  network. The first build exposed a class-load query against `languages`
  before a fresh database had created that table. vpsAdmin `438a92515` moves
  localized accessor definition to the API resource, where the schema exists.
  Focused API regression coverage passed with 4 examples and all commit hooks
  passed.
- The corrected services closure deployed successfully. The database setup
  unit completed every migration and seed with `Result=success`; migration
  `20260721120000` is recorded, the Node-status translation table exists, and
  the legacy `security_advisory_node_statuses.note` column is absent. The WebUI
  and API return HTTP 200, and the WebUI build footer identifies exact commit
  `438a92515`.
- The running development cluster is
  `2026-07-20-security-advisory-review`. Dev-only draft advisory `1` provides
  three representative Node rows for visual review: bilingual live-patch text,
  an English-only kernel-upgrade note to exercise Czech fallback, and a
  note-free storage exclusion. This fixture is local to the development
  cluster and must not be synchronized to production.
- The standalone mandatory re-review cleared exact vpsAdmin commit
  `438a92515fe397b32e94923d84eea76edc39e327` and KB commit
  `f6c8207f990f9b5513eca038c8d751b88131ef67` with no blocking, important, or
  advisory findings. It confirmed that localized accessors remain registered
  at the API resource boundary and found no model-only caller that needs them
  earlier.
- Visual review found that both localized Node-status tables were too wide.
  vpsAdmin commit `a1a4f21ed` reduces date and note inputs to size 14 in the
  embedded new-advisory and standalone existing-advisory forms, including bulk
  and per-Node rows. Preceding focused commit `70d265a8c` repairs the dedicated
  Playwright and VM fixtures so they write and exercise `en_note`/`cs_note`
  translations rather than the removed legacy column.
- vpsAdmin commit `0e389a1ef` standardizes Czech mitigation wording on
  `Ošetřeno`, updates the WebUI placeholder and advisory mail label, and adds
  concrete live-patch, kernel-upgrade, and BPF LSM examples to
  `doc/i18n-cs.md`. Focused WebUI coverage passed with 4 examples and 16
  assertions; the localized API example passed with 1 example.
- The unrelated publish-form correction is isolated in vpsAdmin commit
  `19e613c2a`. It moves `expected_content_revision` into the form hidden-field
  area so the publication-time row begins with its label. Fast and browser
  regressions cover the cell structure.
- Every vpsAdmin commit ran from the root Nix development shell and passed all
  Overcommit hooks. The first ambient-shell attempt stopped without committing
  because the expected hook tools were unavailable; the staged changes were
  then checked normally in the documented shell.
- security-advisories commit `c909aca` adds the same Czech terminology rule to
  its assessment instructions and updates all Node-note contract examples.
  Its focused advisory, evaluator, and reconciler specs passed with 76 examples
  and all Overcommit hooks passed.
- Current review heads are vpsAdmin
  `19e613c2ae72103fc04265002402544f387e08c0` and security-advisories
  `c909aca9d0271a27e01f2597394fe54acdbdac51`. KB capture commit
  `7248a8b8c714335d5459d802a91e03d085acca8a` pins the exact vpsAdmin review
  head in all four contract locations. All four worktrees are clean.
- Full quick verification passed: vpsAdmin WebUI PHPUnit has 82 tests and 332
  assertions; the complete security-advisory API spec has 29 examples; the
  security-advisories suite has 113 examples and RuboCop reports no offenses;
  and `vpsadmin-kb-captures` `bin/check` validates the contract, inventory,
  screenshots, and both test suites. The long WebUI browser integration test
  remains intentionally deferred until the mandatory review clears.
- Mandatory review found two blocking completeness/history issues and no other
  findings. The localized browser and VM fixture repair has been split into
  focused vpsAdmin commit `70d265a8c`, followed by the size-only layout commit
  `a1a4f21ed`; the final tree is byte-for-byte identical to the previously
  verified head. Rewritten terminology and publish commits are `0e389a1ef` and
  `19e613c2a`. Focused WebUI PHPUnit still passes with 4 tests and 16
  assertions.
- vpsfree-notification-templates commit `04921d75ab5321962b207bb380deff90906bd662`
  changes the managed Czech advisory announcement label from `Mitigováno od:`
  to `Ošetřeno od:`. ERB compilation and `git diff --check` passed; the
  repository declares no local hook framework or standalone offline suite.
- The mandatory standalone re-review passed the corrected four-repository
  series with no blocking, important, or advisory findings. It independently
  confirmed the commit split, migration rollback behavior, absence of the
  legacy API alias, managed template wording, exact KB pins, and that
  vpsf-status does not consume per-Node notes.
- The long `./test-runner.sh test 'webui#security-advisories'` integration
  passed. Its Playwright example succeeded in 278.74 seconds and the complete
  test finished successfully in 834.28 seconds.
- Pushed exact reviewed heads over SSH: vpsAdmin `19e613c2a`,
  security-advisories `c909aca`, KB captures `7248a8b`, and managed templates
  `04921d7`. The security-advisories ambient-shell push first stopped in its
  pre-push hook because the ambient Ruby could not load repository gems; the
  documented `nix develop -c git push` path passed. Exact-head
  security-advisories RSpec/RuboCop and vpsAdmin API Specs, WebUI PHPUnit,
  i18n, and RuboCop workflows are green; the aggregate vpsAdmin CI workflow is
  still running.
- The first devcluster update evaluation detected the initiative's newly added
  notification-template worktree and tried to enable a Nix option unavailable
  on the vpsAdmin feature base. No running machine was changed. The clean,
  already-pushed template worktree was temporarily removed from devcluster
  auto-discovery, the services update completed, and the worktree was restored
  on the same branch and exact commit afterward.
- Development cluster `2026-07-20-security-advisory-review` remains running and
  ready with the `storage` topology on the bridge network. Services now report
  vpsAdmin revision `19e613c2ae72103fc04265002402544f387e08c0`;
  `systemctl is-system-running` reports `running`, no failed units were listed,
  and `vpsadmin-database-setup.service` is active/exited with result `success`
  and exit status zero.
- Preserved dev-only advisory `1` and updated exactly its Node 101 Czech note
  from `Mitigováno live patchem` to `Ošetřeno live patchem`. The English live
  patch note, Node 102 English kernel-upgrade note, and fallback/no-note rows
  remain in place for visual review. No production data or template upload was
  performed.
- The user accepted the development WebUI review and authorized default-branch
  integration. Fresh detached integration worktrees were created from each
  fetched target, fast-forwarded with `git merge --ff-only`, tested, used for
  the target push, and removed afterward. Feature branches and their ordinary
  initiative worktrees remain available.
- Upstream default refs now resolve exactly to the reviewed commits:
  vpsAdmin `master` is `19e613c2ae72103fc04265002402544f387e08c0`;
  security-advisories' actual remote default
  `2026-07-13-security-advisory-automation` is
  `c909aca9d0271a27e01f2597394fe54acdbdac51`; vpsadmin-kb-captures `master`
  is `7248a8b8c714335d5459d802a91e03d085acca8a`; and
  vpsfree-notification-templates `master` is
  `04921d75ab5321962b207bb380deff90906bd662`.
- Integration-worktree verification passed: focused vpsAdmin WebUI PHPUnit has
  4 tests and 16 assertions; security-advisories has 113 RSpec examples and 25
  RuboCop-inspected files; the KB contract/inventory and both test suites pass;
  and the managed Czech ERB compiles. Default-branch security-advisories RSpec
  and RuboCop workflows are green. vpsAdmin default-branch migration specs,
  libnodectld specs, WebUI PHPUnit, RuboCop, and i18n workflows are green while
  its longer API/aggregate workflows continue on the same already-verified
  commit.
- A fresh configuration integration worktree from `origin/master` used
  `confctl inputs channel update --commit vpsadmin`. Generated commit
  `3313c5841d4be30327294c1f5ee215405cf24817` moves `vpsadminServices` from
  `88f03da4` to merged revision `19e613c2` and is pushed to
  vpsfree-cz-configuration `master`.
- `confctl build -y 'cz.vpsfree/vpsadmin/*'` built generation
  `2026-07-21--19-55-54` successfully for all 11 vpsAdmin systems, including
  both APIs, all three WebUIs, the database, supervisor, Redis, and RabbitMQ
  systems. The first non-interactive invocation omitted `-y` and stopped at
  its confirmation prompt before building; it made no state change. No
  production deployment was run.

## Open questions

- No advisory-review blocker remains. Future production evidence or Linux CNA
  changes require a new collection and evaluation rather than reuse of this
  snapshot.
- Production deployment of the already merged token fix and channel update is
  outside this advisory-review stage. Publishing the five verified drafts also
  remains a separate administrator action. The configured advisory credential
  is used without exposing it.

## Cleanup

- Keep the review worktree until the advisory review is finished or abandoned.
- Keep the feature branch after integration unless the user explicitly asks to
  delete it.
- Removed the `vpsadmin`, `vpsfree-cz-configuration`, and `haveapi` initiative
  worktrees plus both temporary default-branch merge worktrees. Their feature
  branch refs were retained.
- Removed transient development-shell files and the downloaded CI artifact.
- The clean `security-advisories` initiative worktree is twenty-six commits
  ahead of base `55e26c3ad6bc548e7b40b0cc1dddd47c41e2da11` at `06ddc84` and
  tracks the pushed feature branch. It is retained for draft review and any
  later publication decision.
