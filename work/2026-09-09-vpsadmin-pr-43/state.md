---
lifecycle: active
---

# 2026-09-09-vpsadmin-pr-43

## Repositories

- vpsadmin canonical bare clone: `repos/vpsadmin.git` (SSH origin).
- Review branch: `2026-09-09-vpsadmin-pr-43`.
- Worktree: `worktrees/2026-09-09-vpsadmin-pr-43/vpsadmin`.
- Base: `3a64784708faef5e9f4f093255954b14e396904c`.
- Head: `44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1`.

## Current implementation status

- User approved implementation of the development-branch plan, including the
  separate API JSON compatibility fix. Push only the initiative branch.
- User explicitly requires a review before merging. No update of master or
  PR source branch is authorized at this stage; no merge/deployment performed.
- Non-integration workflows must pass; long integration tests are not a
  completion gate. Keep current integration runs running.
- Current upstream master: 41af23e207478af2469e1d6423312930e720ba87.
- Previous cleanup service failed on deployed authority-format incompatibility;
  it is inactive and made no archive/worktree removal. Do not queue cleanup
  while user review is pending.
- The initial review is preserved below as historical evidence. Its former
  terminal status and read-only scope are superseded by this implementation.

## Initial review status

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
