---
lifecycle: active
---

# Flake input ancestry guard

Git mirror rework in progress. The user explicitly requested replacing the
GitHub comparison backend with cached Git ancestry checks ("yup, rework it").
Architect0 owns the revised design; implementer1 owns confctl and implementer0
owns seven consumer workflows. Existing R implementation, reviews and all
completed verification below remain historical evidence for those exact heads;
they do not verify the replacement backend. The existing `inputs ls --json`
interface remains: status/IRC use its full alias-resolved revision metadata.

Current rework checklist:

- [x] Architect implementation contract accepted in current design.md.
- [x] Complete bounded verification brief accepted: [Git mirror checks](git-mirror-verification.md).
- [x] Cached Git provider committed locally at `822c0e35dbe2549111912f539116b4225dfd3035`; focused 86+36, lint/man/hooks pass; two-commit history consolidated.
- [x] All seven final pins/docs committed and clean; final-pin C40/D20/cache98+14 controls and ordinary hooks pass. Status has three intended logical commits.
- [x] Independent final review passed without findings: [Git/cache review](review-git-cache-report.md), retained reviewer0 Sol/xhigh/read_only, all four affected lanes and full eight histories.
- [x] Exact published package exported check: 203 examples, zero failures/pending ([receipts](verification/git-cache-exported-check.json)), 98 seconds.
- [x] Seven scoped updater/caller/cache paths: six original successes plus corrected org-only successor0 ([proof](verification/git-cache-selected.json)).
- [x] Actual new-provider local target race:59 commands, expected stale push1/guard3, equality0; state preserved ([proof](verification/git-cache-race.json)).
- [x] Provider and all seven exact reviewed heads published with R preservation and exact leases ([consumer proof](verification/c7-git-cache-publication/published.json)); defaults unchanged.

Backlog: root -> accept the active seven-path/caller/cache batch, then run the
local Git race through a fresh watcher. Implementer0 retains consumer and runtime
diagnosis; implementer1 retains provider diagnosis; architect0 retains design;
reviewer0 completed independent final review. Root owns serialization, acceptance
and user-facing prose. Provider and consumer prose received the lead's direct writing pass. No current blocker; cache misses must fetch
sufficient history and evidence errors must stop the update. Consumer inspection
confirmed that both configuration workflows already restore/save the shared
confctl cache and the five ordinary workflows need matching cache steps.

The complete new local sources are in [the final rework inventory](git-rework-final-source-inventory.json),
with owner [provider](git-cache-source-inventory.json) and
[consumer](package-c7-final-source-inventory.json) provenance.
[Review packet](git-rework-review-packet.md) records high risk, all four changed
lanes and the complete branch histories. The subsequent actual exported check passed
203 examples with zero failures or pending cases. Review passed. Provider `822c0e35` is published; remote R evidence ref was verified before
replacement. [Publication proof](verification/git-cache-publication/published.json).
All seven consumers are also published at the exact reviewed heads. Fresh Luna/low utility
`verify_git_cache_package` completed the exact203 packaged check successfully;
no owned process remains. Fixed launcher `package-b-git-cache-rspec-launch.py`
and aggregate `provider-git-cache-rspec.log` are retained. Fresh Luna/low `verify_git_cache_selected` finished the selected-path batch with
launcher exit2: six project receipts complete0, org configuration149 commands0
through final-status followed by a final ValueError. Implementer0 owns bounded
diagnosis and effect reconciliation; no retry or source defect is assumed. Default integration remains unapproved.

Prepared caller probe v2 is accepted: the artificial outer `bundle exec` parent
was removed before runtime. The probe uses the actual plain devShell workflow
invocation and preserves caller variables. Source/review are unchanged; the
unexecuted v1 packet/diff remain retained. All seven source publication proofs are accepted; the corrected selected-path
launcher is now running with the verified B package.

Accepted affected verification: a new exact packaged exported spec check with
real local Git DAG/cache/error/concurrency fixtures; actual package in IRC and
both old configuration shells/hooks; all seven guarded updater/commit/final
HEAD-lock paths with one shared owned cache and cold/warm receipts; a real local
Git target race. Unchanged standalone dependency-refresh/build stages may be omitted only
with explicit recording, so these are scoped updater checks, not seven complete
new workflow runs. [HaveAPI scope correction](verification/git-cache-haveapi-inline-check-scope.json):
its unchanged helper retains the conditional in-helper `nix flake check`; record
whether the revision-change branch actually runs. No new standalone check was added. Historical R full workflows and Terraform8 remain exact old
component evidence; no unrelated VM rerun is planned.

The previous R deliverable was committed, independently reviewed and published
in all eight feature branches. All its planned verification passed. No affected project default branch was changed by this session and nothing was deployed.
The session remains open. The selected-path utility has ended. No guest, repository claim or machine
claim is held; implementer0 is reconciling the failed final assertion.

[Final acceptance](verification/final-acceptance.json) binds the exact source,
review, publication and test evidence. [Complete source inventory](verification/final-source-inventory-2.json)
records full reviewed bases/heads, series, final diffs and migration conclusions.
[Final SSH observation](verification/final-remote-source-proof-2.json) confirms
all eight tested feature heads remain published and clean. Its HaveAPI target
movement is assessed below rather than hidden by an unchanged-target claim.

## Historical R phase checklist

- [x] Architect design, scope and compatibility assessment.
- [x] Shared confctl guard and seven workflow adoptions implemented.
- [x] Owning docs/manual/help, quick checks and ordinary hooks completed.
- [x] Independent final and affected reviews; no findings.
- [x] Complete branch history/pin consolidation and no-migrations conclusions.
- [x] Exact published provider identity and 197 exported examples, zero failures/pending.
- [x] Both old configuration shell probes and all seven complete real update workflows.
- [x] Actual local Git target-movement race with strict preservation assertions.
- [x] Terraform's eight ordered VM workflow examples and post-run closure checks.
- [x] Exact-head CI/publication proof, including refreshed HaveAPI.
- [x] Assess latest HaveAPI default movement; preserve reviewed/tested head.
- [ ] Explicit repository/target integration approval, then fresh preparation and merges.

## Historical R behavior

Provider R is `5436d3d7c36d3d5174eab3c44e3578830749d3db`.
`--forward-only` prepares a separate candidate lock, resolves complete follows
paths and validates every changed reachable dependency before atomic install.
Equal or descendant revisions in supported GitHub sources are accepted. Known
regressions reject with status3; unknown evidence/tool errors return1. Both stop
publication. Workflows additionally validate the committed HEAD lock against
the original baseline before an ordinary nonforce push.

Configuration deployment-tool pins and manual update/set behavior remain
unchanged. There are no schema/persisted-state changes, migrations or coordinated
node updates. The guarantee retains commits in history; later upstream reverts
and semantic software compatibility remain outside it.

## Historical R verification and review

- [Current seven exact-source workflow receipts](verification/final-workflow-summary.json).
- [Published/local provider identity](verification/provider-R-published-identity.json)
  and [197-example check](verification/provider-R-exported-check/retained.json).
- [Terraform8 VM result and full receipts](verification/terraform-workflows-success/retained.json).
- [Real Git race](verification/git-race-r-success/retained.json): stale push1,
  regenerated stale candidate3, equality0, manual lock/index/HEAD/remote preserved.
- [Provider/config handoff](package-bd-r-final-handoff.md),
  [C consumer handoff](package-c-final-handoff.md), and
  [HaveAPI refresh publication/CI](package-c-haveapi-refresh-final-receipt.json).
- Final review reports: [initial](review-report.md),
  [package/status follow-up](review-followup-report.md),
  [R/history](review-r-report.md), [status metrics](review-status-metrics-report.md),
  [HaveAPI refresh](review-haveapi-refresh-report.md). Retained reviewer0:
  independent gpt-6.1-sol/xhigh/read_only; no nested agents or settings overrides.

Earlier failures, source-bound receipts and their fixes remain preserved.
Status's baseline vendor-hash/test-dependency and metrics-test fixes are separate
logical commits. The package startup compatibility fix is separate from the
guard. No obsolete repair, repeated pin or transitional history remains.
See [historical state](state-history-before-final-handoff.md) for the complete
chronology and interrupted test/authentication effects. The separate
[fixture authentication classification](verification/terraform-fixture-auth-scope.json)
contains source locations and scope, with no values. No credential values were
copied into these tracking files.

## Current Git-cache sources and integration preparation

All projects use feature branch `2026-10-24-flake-update-downgrade-guard-replacement`.
Full SHAs and paths are in the source inventory above.

| Repository | Tested/published head | Target |
| --- | --- | --- |
| confctl | 822c0e35 | master |
| haveapi | c7bfc1aa | master |
| terraform-provider-vpsadmin | c3f20203 | master |
| vpsadminos | 889f14e5 | staging |
| vpsf-status | 018b700f | master |
| vpsfree-irc-bot | 0a160463 | master |
| vpsfree-cz-configuration | 5f0f4466 | master |
| vpsadminos-org-configuration | ca96c95a | master |

HaveAPI master advanced again to `1103a3a14b1dc6dec17fc4859df80220a54f111d`
after the reviewed/tested refresh based on7ac977a2. The new upstream commit
changes library dependency-lockfile/release tooling in24 paths. It does not
contain our adoption. The guard workflow/helper, flake/lock/root Gemfile and
custom hooks are unchanged; the shared development-doc edits occupy different
paragraphs. Owner0 assessed this read-only without changing the tested branch.
The branch is not immediately fast-forwardable onto that target.

The current Git-cache adoption is c7bfc1aa on the same retained7ac base;
74f1cef6 remains historical R evidence. Preserve both ranges for this handoff. After explicit
HaveAPI/master integration approval, fetch the then-current target and prepare
the sole adoption on that base, preserving upstream deletions and both doc
changes. Stop on conflicts/material edits. Prove the exact old/new range and
patch/tree relationship, apply narrow review/verification to affected deltas,
and never describe74f's test receipt as a run on a future SHA. Other seven
repo targets also need ordinary fresh pre-merge checks. Do not chase unrelated
upstream movement with repeated full-suite runs before integration is approved.

## Owners and next action

Lead owns user contact, acceptance and approval-bound integration coordination.
Implementer0 retains C5/HaveAPI preparation and diagnosis; implementer1 retains
provider/D2; architect0 owns design; reviewer0 retains independent review.
Saved member settings/access remain unchanged.

Next action is the C7 bounded final CI/source observation and consolidated
handoff. Org-only successor is accepted0; all runtime operations are finished. Package203 and real local target race59commands passed;
provider exact-head CI is all green. No source change is planned.
No repository/target integration has been approved. Implementation/review/CI approval is not merge approval. Prepare
outside claims; only approved fresh merge/push/proof uses the short repository
claim. Preserve all feature refs, worktrees, failed attempts and Nix roots.
No cleanup, deployment or session lifecycle action is authorized.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
