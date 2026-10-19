---
lifecycle: active
---

# 2026-10-12-redesign-haveapi-github-releases

## Status

Phase: preparing approved integration into HaveAPI `master`. The user explicitly
directed "yes, merge it" on 2026-10-19 after the merge-approval handoff. Scope is
`vpsfreecz/haveapi`, target `refs/heads/master`; this does not authorize a version
tag, registry publication or integration into another target.
The release implementation and documentation are committed and published;
independent review findings are fixed. Full local verification and all five
GitHub Actions workflows passed on the previously tested head. Upstream master
has since advanced by the single Nix pin update `cb3f39f75e8a63416388d24293f936d1db97162b`.
The rebase is clean and both range-diff entries are `=`. Refreshed quick checks
passed and retained reviewer0 accepted the exact refreshed range without findings.
Refreshed full package/component tests and all five safe Actions passed on the
exact current head. The lead retained CI-before-merge timing while runners were
queued. The approved fast-forward merge was admitted through the runtime as
background integration `f06835bb-e0ed-4269-91b0-4c9f44f29914` at 15:59:53 UTC.
The initial receipt is phase `prepare`, with no merge jobs submitted yet. A fresh
Luna/low utility observes that exact run; the lead retains decision ownership.
Preparation initially stopped because the coordinator uses its own Ruby 3.4.9
to probe gems installed by the repository's Ruby 3.3.10 shell. The extensions were
present and loaded correctly under 3.3; this was an interpreter mismatch, not a
failed application check. The lead acknowledged the exact handoff and configured
Bundler's ignored local dependency path in the retained checkout to keep separate
`ruby/3.3.0` and `ruby/3.4.0` gem sets. A fresh Luna/low utility ran the bounded
dependency-setup script; both full hook loads passed (exit 0, 95s). No tracked
source or hook was changed/bypassed. See repair-merge-hooks.sh/log/status.
The same approved integration is being resumed after that verified repair.
The next preparation exposed the coordinator's explicit JSON-before-Bundler load
order: default JSON 2.9.1 was already activated, while the temporary resolved
hook lockfile selected 2.21.2. The lead acknowledged the generation-1 handoff and
aligned only the ignored hook dependency set/lockfile to allowed JSON 2.9.1.
Both Rubies then passed the exact coordinator load order (exit 0, 41s); see
repair-merge-hook-json.sh/log/status. Tracked application sources and reviewed
patches remain unchanged. The same approved integration is resumed again.
No new version was published and no default/release branch was integrated yet.
Operator setup is user-confirmed. The 2026-10-19 follow-up read-only check verifies
required reviewer `aither64` and a deployment policy allowing tags matching `v*`.
Credential use remains subject to verification during the first authorized release.

## Phase checklist

- [x] Verify thread/session identity and retained roster.
- [x] Investigate existing releases and write the accepted design.
- [x] Implement the maintained release workflow and documentation; exclude Elixir.
- [x] Pass quick checks and commit all intended changes with installed hooks.
- [x] Complete retained independent final review and whole-branch history review.
- [x] Fix both review findings through focused checks and fold them into history.
- [x] Pass full component/package verification and safe build-only Actions.
- [x] Rebase over current master and repeat quick checks, independent review and full local tests.
- [x] Pass all refreshed Actions checks before the approved merge.
- [ ] Integrate into the explicitly approved HaveAPI target branches.
- [x] Complete one-time publisher setup (user-confirmed; public approval gate verified).

## Next actions and material limits

- Integrate into the explicitly approved HaveAPI `master` through the selected
  runtime coordinator after refreshing the branch and verification. Preserve the
  two logical commits and feature refs. The workflow must also be installed on
  the supported release line before its first automated tag; that target is not
  included in this master-only integration.
- The user confirms setup is complete. The 2026-10-19 follow-up API check verifies
  required reviewer `aither64`, self-review allowed, custom deployment policies
  enabled, and the sole deployment rule `type: tag`, `name: v*`.
- Environment-secret names, the activation variable and PHP deploy-key metadata
  cannot be read with this session's API token (HTTP 403); the activation check
  was repeated after the user's confirmation with the same result. Rely on the
  operator's setup confirmation and verify actual registry/deploy-key credentials
  and Packagist indexing during the first authorized release.
- Authorize a specific new version separately; no dummy registry publication is
  part of verification. Publication can fail partially after a concurrent update
  or transport failure, and recovery requires the exact retained artifacts.
- Keep the session open and retain its branch/worktree.

## Repositories and final history

- Canonical clone: `/home/aither/workspace/ai/vpsfree.cz/repos/haveapi.git`.
- Worktree: `worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi`.
- Published branch: `2026-10-12-redesign-haveapi-github-releases`.
- Current base: `cb3f39f75e8a63416388d24293f936d1db97162b` (origin/master).
- Complete final series:
  - `82c9e778d04e0228785413a515e9ca76b2956215`: release implementation and specs.
  - `c14e7d3158b91c134c2817b489cd29772fc09f82`: release documentation.
- Remote feature ref matches that exact final head. Working tree is clean.
- Original base/head: `06865bb847a564fe20e59ea6d72856c2f01a82e3` through
  `cb256a87539c4503b70594df6fe04678e1814dfb`. The two commits were rebased over
  upstream's single flake.lock update, with patch equivalence proved in
  [merge-rebase.range-diff](merge-rebase.range-diff). Approval is preserved for
  the same repository/target and unchanged patch. The feature push used an exact
  lease; there were no superseded active Actions runs to cancel.
- No obsolete branch iterations, fixup commits or repeated pin streams remain.
  No migrations, runtime version changes or flake.lock updates. The lead inspected
  the final series/diff and [remediation range-diff](review-remediation.range-diff).

## Review and verification

- High risk: OIDC/SSH credentials, immutable package pushes and PHP synchronization.
- Retained reviewer0, `gpt-6-astra/xhigh`, read-only; native metadata verified.
  All four mandatory lanes and full branch history; no fallback or overrides.
- Original reviewed head: `1bc5178c378bfb66230d15c8dd9d9c47a0051434`. One Blocking
  Actions-fixture run-ID mismatch and one Important PHP preflight ordering issue
  were fixed. Conditions/contracts stayed within the review's requested fixes;
  lead verification applies the mandatory workflow's narrow-fix policy without
  a redundant full review. [Review and reconciliation](review.md).
- Full Ruby lint, workflow lint, syntax, doc links and hooks passed. Release specs
  pass both locally and under GITHUB_RUN_ID=123 (21 examples).
- Full local results: Ruby server 355 examples, Ruby client 47, Go generator 9,
  JavaScript 43 tests, PHP 51 tests/144 assertions. Package build, npm tarball,
  extracted Ruby libraries and manifest verification passed.
- Five successful CI runs on the exact final head; release publication job skipped.
  [Verification summary and run links](verification.md), [CI results](ci-results.json).
- Fresh Luna/low utility watchers owned hook setup, dependency installation and
  final verification. Final command exited 0 in about 85 seconds. No operation
  remains active. No test failures were dismissed or blindly rerun.
- Refreshed pre-merge review: retained reviewer0, same gpt-6-astra/xhigh and
  read-only identity, accepted base `cb3f39f75e8a63416388d24293f936d1db97162b`
  through head `c14e7d3158b91c134c2817b489cd29772fc09f82`, with no findings in
  affected general/risk lanes, explicit whole-history/no-migrations conclusions
  and no new issue in unchanged architecture/scope. See [merge-review.md](merge-review.md).
- Refreshed quick checks passed: metadata, 21 specs in each environment,
  RuboCop 243 files, shell syntax and whitespace. Refreshed full local tests,
  package build, manifest and extracted-package smoke checks passed (exit 0).
  All five refreshed Actions passed; the fresh Luna/low watcher completed with
  aggregate exit 0 after 26m54s. Original local dist is retained separately in
  `artifacts-cb256a87539c/` so the new manifest binds the current source.
- Refreshed Actions runs on `c14e7d3`: release 39278682776, i18n 39278682753,
  RuboCop 39278682772, JS 39278682743, Ruby server matrix 39278682860. All were
  initially queued before running and all ultimately succeeded. GitHub's public
  status API reported operational and no unresolved incidents; the cause of the
  queue is unknown. No retry or cancellation was performed. See
  [refreshed verification](merge-verification-summary.md).
- The pre-rebase hook initially refused its configuration signature. Inspected
  `.overcommit.yml` and confirmed no upstream changes; signed it in the declared
  Nix shell and rebased successfully, without bypassing hooks.

## Documentation and evidence

- Owning repository: `doc/agent-instructions/releases.md`, linked from README and
  AGENTS.md; development.md lists release checks. Covers normal releases, setup,
  approvals, build-only packaging and immutable-artifact recovery.
- [Plan](plan.md), [accepted design](design.md), [original review packet](review-packet.md),
  [reviewed diff](haveapi-reviewed.diff), [final diff](haveapi-final.diff).
- Setup: setup.log/status; dependencies.log/status. The initial checkout hook
  signature refusal was resolved by inspecting/signing the declared hooks in Nix.
- Quick/focused results: quick-final.log, actionlint.log, review-run-id-repro.log,
  review-fixed-quick.log. Current full logs/results are linked from verification.md.
- Baseline evidence: all three gems and npm latest were 0.29.9, with the PHP
  v0.29.9 tag. Master still declares 0.29.0; the supported line declares 0.29.9.
  This implementation deliberately does not invent or bump a release version.

## Cleanup and lifecycle

No cluster, production KB write or staging ownership was created. Build artifacts
and dependency caches remain in the owned HaveAPI worktree. The generated PHP
unit-test cache was removed; no tracked source needed restoring. Unrelated shared
workspace changes are preserved. Session records remain current in the working
tree under the normal tracking-commit cadence. Session lifecycle remains active;
no archive, deletion, stop, hold change or delayed cleanup is authorized.

## Integration f06835bb-e0ed-4269-91b0-4c9f44f29914

Requested exact feature heads are integrated. See integration/f06835bb-e0ed-4269-91b0-4c9f44f29914/summary.md
and integration/f06835bb-e0ed-4269-91b0-4c9f44f29914/result.json for operation receipts. Feature refs and session retained.
