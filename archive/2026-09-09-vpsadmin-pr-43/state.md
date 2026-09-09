---
lifecycle: complete
---

# 2026-09-09-vpsadmin-pr-43

## Repositories

- vpsadmin canonical bare clone: `repos/vpsadmin.git` (SSH origin).
- Review branch: `2026-09-09-vpsadmin-pr-43`.
- Worktree: `worktrees/2026-09-09-vpsadmin-pr-43/vpsadmin`.
- Current base: `41af23e207478af2469e1d6423312930e720ba87`.
- Replayed PR commit: `ed8121659686427ff6b35b898eff3d3b6c48739a`.
- Original PR head: `44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1`.
- Implementation head: `19971f039771500d5d0304610f91fe6f4af5fed3`.

## Merge and cleanup status

- User approved merging the exact reviewed head 19971f039. Upstream remained
  at 41af23e20, so no rebase, code change or repeat review was necessary.
- Created attached temporary branch 2026-09-09-vpsadmin-pr-43-merge from
  origin/master at worktrees/2026-09-09-vpsadmin-pr-43/merge/vpsadmin.
  Local git merge --ff-only reached exactly 19971f039; diff/status checks
  passed. Its packaged-dependency API boot smoke passed: five examples,
  zero failures, seed 29306.
- Pushed the approved head to codex/user-payment-period-filter with an exact
  lease for former head 44cfb4357, verified the PR head, then made an ordinary
  SSH push from the temporary checkout to master. Pushes used the root Nix
  shell so Overcommit loaded the verified repository version.
- Remote master is 19971f039; PR 43 reports MERGED at 2026-09-09 14:31:19 UTC
  with mergeCommit 19971f039. git rev-list --count --merges 41af23e20..master
  returns zero. No GitHub merge operation or deployment was used.
- All required workflows passed on this exact head before approval. Subsequent
  source/master push runs are repeats on the same head; no failure is reported,
  and extra WebUI PHPUnit 34364058726 passed. VM integration remains outside
  the gate. No current-head runs were cancelled and no obsolete active source
  runs needed cancellation.
- Temporary integration worktree removed without force; its local branch is
  retained, as are the local/remote development and PR source branches.
- Requested merge is complete. The remaining session retirement uses the
  installed dev-session archive command after the owning thread becomes idle.
  Inspected its finalize_locked!, merged-head proof, non-force cleanup,
  isolated git commit --only -F, and retirement checks. It is the compatible
  deployed equivalent of the older finalize/commit/stop sequence, as documented
  in notes/cross-project/2026-09-09-cutover-archive-helper.md. No authority or
  lifecycle guard will be bypassed. No additional user approval is needed.
- A bounded task-specific worker will verify prepared hashes and the clean
  feature head before ordinary archive. Unexpected changes/errors leave the
  initiative available and log the failure outside tracking. The helper makes
  the single final archive commit and retains all branches.
- Removed the five verified ignored gem/cache/lockfile paths. Both ordinary
  and ignored project status are clean. No task test/build process remains;
  both vpsAdmin and vpsAdminOS development clusters report stopped. The first status invocation
  omitted its positional slug and failed read-only; the corrected command
  explicitly targeted this initiative.
- Durable lessons committed separately as workspace 8234f6e, touching only
  three task-owned notes. Shared unrelated edits and index entries are preserved.
- Portal comparison base now records the rebased, reviewed base 41af23e20;
  original PR provenance 44cfb4357 remains in this record and the first review
  packet. The explicit merged-change link in implementation.md is immutable.
- Retirement worker: /tmp/vpsadmin-pr-43-archive.sh, unit
  vpsadmin-pr-43-archive.service. Its idle-check log is outside tracking at
  /tmp/vpsadmin-pr-43-archive-idle.log; archive output is in the user journal.
  The read-only guard was verified to reject this active turn with inProgress.

## Implementation history

The following records preparation and the earlier review handoff. Statements
about pending approval or retaining an active worktree describe that earlier
stage; merge and cleanup status above is authoritative.

- User explicitly approved merging reviewed head 19971f039 on 2026-09-09.
  Updating the PR source with an exact lease and fast-forwarding master through
  local Git/SSH are now authorized. No deployment is requested.
- Fresh fetch confirms master 41af23e20, source 44cfb4357 and development
  head 19971f039 are unchanged. All required checks remain successful at the
  approved head; no rebase, code change or new review is required.
- Temporary integration worktree: worktrees/2026-09-09-vpsadmin-pr-43/merge/vpsadmin,
  attached branch 2026-09-09-vpsadmin-pr-43-merge, starting from origin/master.
- Non-integration workflows must pass; long integration tests are not a
  completion gate. Keep current integration runs running.
- Current upstream master: 41af23e207478af2469e1d6423312930e720ba87.
- Initial implementation tracking committed as workspace eab840d before any
  project commit or push. Overcommit installed and signatures verified in the
  project root Nix shell; original PR replay preserves its author.
- `nix develop .#vpsadmin -c rake vpsadmin:gems:api` generated only the intended
  JSON 3.0.2 -> 2.21.2 downgrade and explicit constraint. No other dependency
  versions changed. Seeded ignored api/Gemfile.lock from this packaged lock.
- Nix API package build passed. Its wrapped Ruby passed ActiveSupport JSON
  decoding with positional options and ActiveRecord serialized-JSON roundtrip
  with JSON 2.21.2 / ActiveSupport 8.1.3.1.
- Implemented action-specific from_id description and five new request specs:
  bilingual OPTIONS with inherited metadata preservation on User::Index;
  nonexistent, foreign-user and period-excluded cursors return empty pages.
- Locale generator compacts the sole application-owned from_id description to
  vpsadmin.attributes.from_id. Other actions retain HaveAPI-owned descriptions;
  bilingual request assertions check that they are unaffected.
- Packaged-dependency API boot smoke passed: five examples, zero failures,
  seed 51726. Ran the package's generated ruby-env/bin/rspec against the
  worktree smoke spec; this forces packaged dependencies while using the
  normal isolated MariaDB setup.
- Development payment request suite passed: 25 examples, zero failures,
  seed 54261. Retained boundary probes passed: seven examples, zero failures,
  seed 6292. Isolated migration up/down passed: one example, zero failures.
- API i18n update and health passed. API-shell RuboCop inspected the source
  Gemfile, changed request spec and payment resource: three files, no offenses.
  Diff whitespace check passed.
- Committed JSON compatibility as a22f37263 and cursor description/specs as
  19971f039. All mandatory pre-commit hooks passed. Commit-message hooks passed
  with advisory 72-column warnings; all lines comply with the required 80.
- Re-fetched origin: base unchanged at 41af23e20; clean project worktree.
- Fresh mandatory review launching on 41af23e20..19971f039: High risk for API
  cursor semantics, tenant isolation, migration and dependency compatibility;
  general, architecture, scope and risk lanes, gpt-5.6-sol/xhigh. See the
  implementation-review-packet.md for the exact scope and verification.
- All four mandatory lanes completed on 41af23e20..19971f039 with no Blocking,
  Important or Advisory findings. No review remediation or reruns were needed.
  Residual limits accepted: production index timing/query plans and
  WebUI Next E2E; permanent equal-timestamp and exact date-filter metadata
  assertions remain optional gaps (retained boundary probes cover timestamps).
- Risk review clarified future rollback ordering: disable new date-filter
  clients before API rollback. Keep the JSON fix or use a known-bootable older
  artifact; this exact master base packages incompatible JSON 3. Updated plan.
- Pushed only 2026-09-09-vpsadmin-pr-43 at 19971f039 over SSH after re-fetching
  unchanged master. PR source/master remain unchanged and no merge was made.
- First ambient push was rejected locally by Overcommit signature validation:
  ambient Ruby loaded 0.71.0, root bundle uses 0.73.0. Hook/config diffs were
  unchanged; pushing from nix develop .#vpsadmin succeeded without re-signing
  or bypassing hooks. Recorded notes/vpsadmin/2026-09-09-push-overcommit-version.md.
- GitHub validation completed on exact head 19971f039 at 2026-09-09 14:14 UTC:
  RuboCop 34358367558, API Migration Specs 34358367602, i18n health 34358367595,
  and API Specs 34358367616 all passed. All 26 API topic jobs and the separate
  topic-coverage job succeeded. No failed workflow attempts or reruns.
- Current integration CI 34358367645 is running and remains excluded from the
  gate. All five runs belong to the current head; no superseded runs to cancel.
- Remote initiative branch matches local HEAD; project status is clean.
  PR 43 remains OPEN at 44cfb4357 with autoMergeRequest null. Initiative remains
  active for user review;
  no finalization, worktree removal or session stop is planned.
- Implementation is ready for user review; see implementation.md and the
  portal's four implementation review reports. Portal manifest parsed and all
  13 artifact paths exist. Master/source branch were not updated. The next
  action is explicit user merge approval; eventual integration must use local
  fast-forward-only Git and SSH, with re-review if the approved head changes.
- Keep the clean project worktree and its ignored development gems/lockfile
  available for review. No local test/build process remains. Current tracking
  edits are consolidated in the working tree after initial commit eab840d;
  no routine per-result tracking commits or archive transition were made.
- Previous cleanup service failed on deployed authority-format incompatibility;
  it is inactive and made no archive/worktree removal. Do not queue cleanup
  while user review is pending.
- The initial review is preserved below as historical evidence. Its former
  terminal status and read-only scope are superseded by this implementation.

## Initial review status

Everything below records the original read-only review, including its former
cleanup plan. It is historical; current implementation status above takes
precedence. Original base: 3a64784708faef5e9f4f093255954b14e396904c;
original head: 44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1.

- Session created with an initial request.
- Verified `dev-session current` matches `VPSFREE_DEV_SESSION_SLUG`.
- Read workspace/repository instructions and mandatory-change-review and
  dev-session-handoff skills. Existing shared changes are unrelated and preserved.
- Review risk classified High because the PR changes an API pagination
  contract, handles tenant-scoped records, and adds a database migration.
- Required lanes: general, architecture, scope, risk; model `gpt-5.6-sol`,
  reasoning `xhigh`. No code changes or external mutations planned.

## Commands run

- `gh pr view 43 --repo vpsfreecz/vpsadmin ...`: captured scope, head, base,
  six-file diff, and CI metadata; PR is open with one commit and no reviews.
- Fetched `origin master refs/pull/43/head` in the canonical bare repository.
- `dev-session worktree add 2026-09-09-vpsadmin-pr-43 vpsadmin --as-is
  --base 44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1 --no-fetch` created the
  attached clean review worktree. The positional order is slug then project;
  the reversed attempt failed before creating anything.

## Results

- Quick checks passed: committed diff whitespace, syntax on four Ruby files,
  API-shell RuboCop (four files, zero offenses).
- All 63 GitHub PR checks report SUCCESS; base/head unchanged on recheck.
- Payment API spec: 20 examples, zero failures (seed 11707).
- Migration spec: one example, zero failures, up and down both verified.
- The first RSpec attempt failed before examples: unlocked development
  dependencies selected JSON 3.0.2, incompatible with ActiveSupport's positional
  options argument to JSON.parse. Recreated ignored api/Gemfile.lock from
  packages/api/Gemfile.lock, retaining packaged JSON 2.21.2 and HaveAPI 0.29.8;
  subsequent focused suites passed. No tracked dependencies changed.
- Final combined run: 27 examples, zero failures (seed 7091), covering the
  original 20 payment examples and seven review probes. Extra probes verify
  equal-timestamp pagination with resolved associations, timezone offsets,
  standalone date bounds, filtered total_count, foreign-cursor isolation,
  invalid datetime rejection, and an inverted period.
- Initial probe assertions incorrectly expected HTTP 400 instead of HaveAPI's
  HTTP 200/status:false validation response, and put metadata inside the
  resource input instead of top-level `_meta`. Corrected the harness after
  inspecting existing API specs; no product change was needed. One rerun using
  an alternation string with `-e` selected zero examples and was not accepted
  as verification. Location selection on the reopened example group ran the
  full 27-example group; all passed.
- Independent general, architecture, scope, and risk lanes completed at the
  exact base/head above, using `gpt-5.6-sol` / `xhigh` and fresh contexts.
- Reconciled finding: one Advisory/P3, stale inherited `from_id` OPTIONS
  description. The implementation now requires a cursor row in the same
  scoped/filtered query; inherited metadata still advertises a numeric ID
  threshold. Recommend an action-specific bilingual description. No Blocking
  or Important findings, project fixes, or review reruns.
- Risk lane's initial potential compatibility concern was reduced to the
  advisory metadata issue after checking the intended ordering correction and
  actual WebUI caller. No inspected consumer relies on arbitrary thresholds.
- Residual limits: no production-scale index timing/query-plan measurement,
  exact bilingual OPTIONS-value test, or dependent WebUI Next end-to-end run.
- Review outcome is complete in review.md. No user action is required to finish
  this review; PR authors can address the advisory separately.
- Test commands use `nix develop .#api`; payment spec runs normally, migration
  spec uses `--options /dev/null` to avoid the API suite's schema hooks. Each
  process uses an automatic isolated MariaDB instance and removes it on exit.
- Portal is deployed; TLS check uses the public CA documented in
  notes/cross-project/2026-09-07-portal-curl-private-ca.md.

## Open questions

- No clarification needed. Review findings do not authorize fixes or publishing
  comments to GitHub.

## Cleanup

- Seven focused review probes are retained as useful evidence; bulk test logs
  remain outside tracking. All test processes and reviewers finished; removed
  worktree-local gems and ignored lockfile. Ordinary and ignored Git status
  are clean. The guarded finisher will remove the review worktree.
- Keep the local review branch; no branch push is needed for a read-only review.
- Automatic test databases stop and prune on process exit.
- Installed dev-session offers an older archive flow and lacks finalize. Use
  the inspected current `libexec/dev-session finalize` workflow, as documented
  in notes/cross-project/2026-09-09-dev-session-profile-missing-finalize.md.
- The portal's read-only require-idle check confirms the owning thread cannot
  finalize while this turn is inProgress. A task-specific user service will
  wait for idle, verify file checksums and shared-master ancestry, run the
  guarded finalizer, commit only this initiative's archive move and dependency
  lesson, then stop the managed session. No lifecycle guard is bypassed.
- Finisher: /tmp/vpsadmin-pr-43-finalize.sh; unit vpsadmin-pr-43-finalize.
  Any unexpected idle/checksum/history failure leaves tracking available for
  inspection and records the reason in the user-service journal.
