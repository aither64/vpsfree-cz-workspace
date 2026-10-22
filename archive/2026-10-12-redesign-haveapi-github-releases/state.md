---
lifecycle: archived
---

# 2026-10-12-redesign-haveapi-github-releases

## Status

Current phase: HaveAPI 0.29.12 published and independently checked at every
destination. The requested release-process test is complete and the packages
are ready for consumers. No release work or blocker remains. This session stays
open with lifecycle active; no lifecycle or cleanup action was requested.

[Public release](https://github.com/vpsfreecz/haveapi/releases/tag/v0.29.12),
[successful Actions run](https://github.com/vpsfreecz/haveapi/actions/runs/39313082898),
[execution record](release-0.29.12.md),
[publication verification receipt](patch12-publication-verification.json).

- HaveAPI master correction: c58704a08451a231fdf6c6123437133422af46dc.
- haveapi-0.29 / peeled v0.29.12: 355c2990a4bfd3940d3234cb2077ad0127f43551.
- Annotated v0.29.12 object: d1867e0a1432cd29c00fad39805d0e475a872b76.
- PHP mirror master / peeled v0.29.12:
  84c46343171d3839c5de011035d96a0f50425a86.
- GitHub Release ID417680904, public since2026-10-19T19:50:18Z;
  publishing job completed successfully at19:50:21Z.
- Original artifact12217296363 retained in patch12-tag-artifacts/;
  manifest SHA256563ed9d468a5357a8a290a0e5ef6f6a973b844fd5b9b0db443b7ea732797a00c
  binds source355c299/version0.29.12/tagv0.29.12/run39313082898.

The user explicitly authorized "yes, merge and release" and then approved the
protected release environment as aither64 (patch12-approvals.json). Master merge
used coordinator run44265246-96eb-4791-a5be-bbc594dd8f4d generation1, succeeded
job504e3a79-f801-4e9e-aedf-03b823b874e4. Release branch/tag were pushed atomically
over SSH with normal hooks after exact final history/diff/clean-head checks.
Prior tag objects/sources remain unchanged. Both feature worktrees are clean at
the reviewed heads, and all refs/worktrees remain retained.

Independent source review passed all four lanes with no findings. Full local
component/package checks, all11safe feature workflows, and all7ordinary tag
checks passed. No runtime behavior, protocol, persisted-state, migrations or
Elixir changes. Scope/history/no-migrations proof: pending-tag-review.md;
full verification: pending-tag-verification-summary.md. The live user diagnostic
confirmed the real pending draft before another tag. Permanent release procedure
covers setup, human approval, immutable originals, recovery and tagged-source
corrections; no further source documentation change was needed after publication.

Fresh Luna/low publication observation confirmed both jobs succeeded, including
draft preparation, trusted-credential setup and final publishing. A separate
fresh Luna/low destination verification then passed in8seconds; the lead inspected
its log and receipt. Registry-served bytes for all3gems and npm match the originals;
npm's repository URL is vpsfreecz/haveapi and latest is0.29.12. PHP tag content,
source provenance and master agree; Packagist indexes that same PHP commit.
All8public GitHub assets (including the manifest) match the retained files, and
the Release is finalized. Actual trusted publishers, scoped PHP push and indexing
have now been exercised successfully. No local verification process remains.

- [x] Diagnose failed drafts and preserve original0.29.10/0.29.11 artifacts/tags.
- [x] Commit pending-tag fix, regressions, recovery docs and separate0.29.12 version.
- [x] Pass quick checks/hooks, independent final review and complete history gate.
- [x] Pass fresh component/package verification and safe exact-head Actions.
- [x] Confirm actual pending-draft lookup and obtain new integration/release approval.
- [x] Integrate master, advance stable and push annotatedv0.29.12 atomically.
- [x] Pass tag tests/build and verify its original source/run/hash-bound artifacts.
- [x] Human approves publication; tagged workflow publishes successfully.
- [x] Verify RubyGems/npm bytes, PHP provenance, public Release assets and Packagist.

Cross-registry publication remains non-atomic by design. Future failure recovery
must preserve accepted originals and diagnose before retrying; the successful
first release does not change that contract. Earlier failed drafts and originals
are retained. No unrelated repository, deployment, session or lifecycle action
was performed.

## Final merge confirmation

After the user's final status question, fresh SSH reads confirm both remote
feature heads equal their intended target heads: HaveAPI masterc58704a and
haveapi-0.29 /v0.29.12 source355c299. PHP mirror master andv0.29.12 both resolve
to84c4634. All project changes are integrated into their intended branches;
release metadata remains on the supported stable branch. Receipt:
final-merge-confirmation.json. No additional merge or publication is needed.

Handoff artifact paths were corrected to be relative to this tracking directory
using the public artifact writer. Its interface is add-only; the mistaken
workspace-prefixed registrations are labeled superseded, and current canonical
entries are registered. No manifest was edited by hand. Session remains open.

## Preserved prior release attempts

The user approved v0.29.10 and v0.29.11 in GitHub, but both publishing jobs
failed during draft preparation. Credential setup and registry/PHP publication
were skipped; post-failure exact-version gem/npm checks were all 404. No blind
retry, tag move or artifact substitution was performed.

- v0.29.10 source b27a031, annotated tag object cd6a5f4c248de748d1b40bd54aeceedb4ebb743c;
  tag run 39291918638. Saved originals: `release-tag-artifacts/`, manifest SHA256
  b0b8600ee048019a48ef15d7e418c766eba8e7e300edc57e83a93428dc2755e4.
  History: [release-0.29.10.md](release-0.29.10.md).
- v0.29.11 source 7fb218e, annotated tag object df335479937a43f93e508ee19b93ba11f0fed8c3;
  tag run 39305802582. Saved originals: `patch11-tag-artifacts/`, manifest SHA256
  80006e3a986ba713401587f5067c58358f320bf54a681c55d27b31055779dfcf.
  Failure/approval/registry evidence: `patch11-publish-attempt1-final.json`,
  `patch11-publish-attempt1-failed.log`, `patch11-approvals.json`,
  `patch11-post-failure-registry.json`; [release-0.29.11.md](release-0.29.11.md).

Original files and both source/run/version/hash bindings were independently
reverified in the latest source review. The first master fix5266481 and release
7fb218e were integrated after the user's explicit "continue" direction; that
approval does not authorize the new master correction or 0.29.12. Master merge
run30712947-5d77-4f21-8bfc-c380849e9e51 is complete with succeeded job3335e2a3;
prior original master integration runf06835bb-e0ed-4269-91b0-4c9f44f29914 is also
complete. Both completion notices were reread and acknowledged with fresh
schema-1 request IDs this turn; no new operation was submitted.

Actual RubyGems/npm OIDC, scoped PHP key use and Packagist indexing remain
first-publication checks. Cross-registry publication is non-atomic. Preserve
accepted originals and diagnose any partial failure before retrying. Both
feature refs/worktrees and retained targets remain; this session stays open.

## Original master implementation history

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

## Pending-tag correction implementation

Source fix committed with hooks as c8cfb16 on release feature. New regressions
against the old implementation:9examples,8failures (explicit-null example alone
passed), pending-tag-repro.log/status. Fixed30examples pass normally and with
GITHUB_RUN_ID=123; focused Ruby lint and whitespace pass after the required
anonymous argument-forwarding style correction. Evidence pending-tag-fixed-quick.
Code resolves exact pending tag via GraphQL, retrieves REST metadata by returned
ID, keeps failures at either stage visible, and explicitly reports a missing
post-create draft. Release docs clarify unchanged tagged-source rerun behavior.
Prepare successor0.29.12 metadata separately, preserving both merged/tagged
predecessors and originals. No new version tag or master integration is authorized
yet; requested read-only diagnostic from user's logged-in gh remains pending.

Final new heads: masterc58704a08451a231fdf6c6123437133422af46dc (one focused
helper/spec/recovery-doc commit) and release355c2990a4bfd3940d3234cb2077ad0127f43551
(c8cfb16fix, then separate0.29.12version/changelog). Both exact-head quick suites
pass metadata,30normal+30runID123 examples, whole lint243/244files, shell/whitespace,
and stable runtime preservation. Review packet pending-tag-review-packet.md;
retained reviewer0 assigned all four lanes at saved settings. User live-draft
query output and fresh new-version/master integration authorization still pending.
Long checks not started; planned master CI includes serverRSpec due to the changed
doc path in addition to release and RuboCop. Release safeCI expects all8workflows.

Pending-tag final review native turn01a15592-4953-78d1-8237-ffd406b099e1 verified
from retained reviewer metadata: gpt-6-astra/xhigh and exact sessionCWD. No setting
override/fallback. Both final comparisons captured with exact current bases/heads.
Project recovery docs and nearby API rationale updated with implementation;
reusable draft-lookup lesson corrected to GraphQL pending-tag resolution.

Retained reviewer accepted both complete new ranges, all four lanes, no findings;
whole-history/no-stream/no-migrations conclusion recorded in pending-tag-review.md.
Native settings verified. Public live schema/semantic-error contract checked by
reviewer; actual write-authorized pending-draft lookup remains unverified and
required before another tag. Full source/local/package and safe CI may now run.

## Integration 44265246-96eb-4791-a5be-bbc594dd8f4d

Requested exact feature heads are integrated. See integration/44265246-96eb-4791-a5be-bbc594dd8f4d/summary.md
and integration/44265246-96eb-4791-a5be-bbc594dd8f4d/result.json for operation receipts. Feature refs and session retained.
