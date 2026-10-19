---
lifecycle: active
---

# 2026-10-12-redesign-haveapi-github-releases

## Status

Current phase: authorized master integration and corrected 0.29.11 tag
preparation; no packages published.

The user approved v0.29.10 in GitHub as aither64, but attempt 2 failed while
retaining draft assets, before RubyGems credential setup or registry/PHP writes.
The published-only release-by-tag endpoint missed the draft it had just created.
The immutable v0.29.10 source and original tag-run artifacts are preserved.
See [execution](release-0.29.10.md) and [historical gate](release-tag-approval.md).

The fix now selects the exact tag from the paginated releases listing and keeps
query errors visible. Five regression examples fail against the old code and
pass with the correction. All 26 helper examples pass normally and with
GITHUB_RUN_ID=123 in both final worktrees; whole Ruby lint, metadata, shell,
whitespace and runtime-preservation checks pass. Commit hooks passed.

- Master fix: c14e7d3..526648131af45df68c25ac0042a52f22c7a81df5 (one commit).
- Release candidate: b27a031..7fb218e28a86ab1d27de74ccb92c2a45063a4f78
  (focused fix, then separate 0.29.11 version/changelog commit).
- No workflow/pin, application behavior, existing component test, Elixir or
  migration change in either new range. Master version remains unchanged.
- The user's ongoing patch-release request covers preparation of the corrected
  candidate. The user has now authorized the corrected version and new master integration.
  v0.29.11 still needs its own human GitHub environment approval; the earlier
  v0.29.10 environment approval does not approve it.

- [x] Diagnose the first publishing failure and preserve originals.
- [x] Commit the focused fix, regressions and corrected version metadata.
- [x] Pass quick checks/hooks for both exact new heads.
Retained reviewer0 accepted all four lanes, read-only, in native turn
01a15559-f326-70f0-9b09-29b911309fd3. Native metadata confirms its saved
 gpt-6-astra/xhigh settings and exact session CWD; no overrides or fallback.
The exact-range report, history/consolidation and no-migrations conclusions are
recorded in [review](draft-fix-review.md). The packet and both final comparisons
are registered in the session portal.
The old local build was moved to local-0.29.10-dist/; tag originals remain in
release-tag-artifacts/. Fresh SSH checks confirm targets still c14e7d3/b27a031,
v0.29.10 unchanged and v0.29.11 absent.

- [x] Complete retained independent review of both new ranges (no findings).
- [x] Pass fresh complete component/package checks and safe Actions.
  Fresh Luna/low utility completed with all status0, local component and clean
  package checks green, all eight release-candidate and both master-fix CI runs
  successful. Lead verified receipts and unchanged final diff hashes. Both
  feature refs are published; both worktrees clean after test-cache removal.
  See [verification](draft-fix-verification-summary.md).
- [x] Obtain direction for the corrected release and new master integration.
  User replied "continue" to the explicit request to merge the fix into
  haveapi/master, advance haveapi-0.29 and push v0.29.11. This authorizes those
  exact operations; the human GitHub release-environment approval remains a
  separate required publication gate. Exact heads remain 5266481 /7fb218e.
  Master-only background integration admitted as
  30712947-5d77-4f21-8bfc-c380849e9e51, selected package i144xnc9p02svar5kz6jxjjpp6gz4cwh;
  guide read via workspace-host (unchanged contract/operations hashes) and exact
  selected source integration guide. Merge-only operation has no machine
  reservation. Review/check receipts are frozen in the request.
- [ ] Run the corrected tag through its protected approval gate.
- [ ] Verify live registry/PHP receipts and Packagist indexing.

Earlier master integration is complete, as recorded below.

Phase: approved HaveAPI `master` integration complete. The user directed
"yes, merge it" on 2026-10-19. The coordinator fast-forwarded
`vpsfreecz/haveapi`, target `refs/heads/master`, to
`c14e7d3158b91c134c2817b489cd29772fc09f82`. A fresh SSH remote query independently
confirmed both master and the retained feature ref at that exact head; the
feature worktree is clean.

Refreshed quick checks, retained independent review, full component/package tests
and all five safe Actions passed before submission. Integration
`f06835bb-e0ed-4269-91b0-4c9f44f29914` finished at 16:15:42 UTC on 2026-10-19;
authoritative status is `complete`, generation 2, and merge job
`49b8f02d-632b-4e6b-bf99-1e0799b10051` succeeded. The lead read session coordination
status and acknowledged completion event `8cf46842-a931-4513-6c88-57434df35393`.
The generated integration result captures the preceding `operations_complete`
snapshot; the final status query confirms completion. No operation remains active.
See [the final coordinator status](merge-integration-final-status.json).

Coordinator hook preparation required separate ignored Ruby 3.3/3.4 dependency
sets and a temporary JSON lock compatible with its JSON-before-Bundler load
order. Exact-order hook probes passed under both interpreters. No tracked source,
reviewed patch or hook was changed or bypassed. See
[the observed coordinator issue](../../notes/haveapi/2026-10-19-coordinator-hook-ruby-mismatch.md)
and repair-merge-hooks / repair-merge-hook-json scripts, logs and status files.

At the original master integration, no release branch had been integrated or
version tagged; no registry package or PHP mirror update had occurred. Operator setup is user-confirmed; the required reviewer and
`v*` tag deployment policy were verified read-only. Actual credential use remains
a first-authorized-release check. Session remains open.

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
- [x] Integrate the exact reviewed/tested head into the approved HaveAPI `master`.
- [x] Complete one-time publisher setup (user-confirmed; public approval gate verified).

## Original master integration limits (historical)

- Master integration is complete. Before an automated patch release, install
  the workflow on supported line `haveapi-0.29` under separate explicit target
  authorization. A new minor release can branch from updated master.
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
- Pre-merge base: `cb3f39f75e8a63416388d24293f936d1db97162b`.
- Complete final series:
  - `82c9e778d04e0228785413a515e9ca76b2956215`: release implementation and specs.
  - `c14e7d3158b91c134c2817b489cd29772fc09f82`: release documentation.
- Remote master and feature refs match that exact final head. Working tree is clean.
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
- Five successful original CI runs on the previous head; publication job skipped.
  [Verification summary and run links](verification.md), [CI results](ci-results.json).
- Fresh Luna/low utility watchers owned hook setup, dependency installation and
  verification. Original verification exited 0 in about 85 seconds. No test
  failures were dismissed or blindly rerun.
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

## New master integration: hook preparation recovery

Integration 30712947-5d77-4f21-8bfc-c380849e9e51 stopped in prepare,
generation0 needs_attention, no merge jobs submitted. Lead read the authoritative
status/session coordination and acknowledged event e79d2c9e-90ca-f56a-4caf-695cdf864215.
It repeats the previously diagnosed Ruby3.3 repository /Ruby3.4 coordinator gem
ABI mismatch in the new isolated source5266481, before any Git write. Preserved
status: draft-fix-integration-attention.json; observer exit2.
Adapted the proven two-ABI and JSON-default-compatible hook setup to this exact
new source; only ignored dependencies/config/lock are repaired. Tracked source,
reviewed diff and hooks remain unchanged. Fresh Luna/low utility owns setup and
exact-order probes; resume the same run only after successful evidence.

Hook recovery completed with exit0; exact-order probes pass for repository
Ruby3.3.10 and coordinator Ruby3.4.9, both JSON2.9.1. Lead verified isolated
source5266481 and tracked diff unchanged. Resumed same integration through stable
selected command; no new approval, source change or hook bypass. Fresh observer
owns the resumed operation evidence separately from the first failure.

## Integration 30712947-5d77-4f21-8bfc-c380849e9e51

Requested exact feature heads are integrated. See integration/30712947-5d77-4f21-8bfc-c380849e9e51/summary.md
and integration/30712947-5d77-4f21-8bfc-c380849e9e51/result.json for operation receipts. Feature refs and session retained.
