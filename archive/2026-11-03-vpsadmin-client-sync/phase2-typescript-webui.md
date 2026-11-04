Current final checkpoint: WebUI affected review and exactfa7d7732 CI/smoke
passed. PR127 OPEN/ready; remote main670cf286, featurefa7d7732, clean targets.
Utility completed/slot released; awaiting explicit integration approval. See
[final rebase addendum](phase2-webui-rebase-review.md) for current exact evidence
and the recorded native mobilewebkit flaky annotation. Older checkpoints below
retain their original ranges and are historical.

Current checkpoint: affected WebUI rebase review accepted; fa7d7732 feature
published with exact old lease and PR127 ready. New exact-head CI/smoke are
being observed by a sole fresh utility. See [rebase addendum](phase2-webui-rebase-review.md);
older checkpoints retain original ranges/CI and are historical.

Current checkpoint: WebUI rule commit rebased locally onto public670cf286 as
fa7d7732, push held for affected review/audit. See
[rebase packet](phase2-webui-rebase-review.md); older checkpoints below retain
their original exact ranges and CI identities.

# Phase 2 TypeScript and WebUI documentation package

Owner: implementer2. Required quick audit and direct lead writing pass passed; both repository
documentation commits are complete and awaiting independent final review. No Phase 1 history rewrite,
application/dependency/runtime/version/workflow edit or default integration.

## Owned repositories and boundaries

- TypeScript: existing registered feature/worktree `vpsadmin-typescript-client`,
  fresh default/Phase 2 base `c53cb4dabb0b3aac8d05834478872d2cfa698fa7`.
  Append one documentation commit only; Phase 1 released commits stay immutable.
  Files: `docs/development.md`, `docs/releasing.md`.
- WebUI: new registered own worktree `vpsadmin-webui`, required repository branch
  `dev/vpsadmin-client-sync-rules`, fresh main/base
  `1c8478bceb3943645ec06ccde895ee4b0985873f`.
  Files: `AGENTS.md`, `docs/design/HAVEAPI_CLIENT.md`, dated
  `docs/work-log/2026-11-03-generated-sdk-release-rule.md` and root `WORK_LOG.md`
  pointer. No peer WIP, preview or team inspected. PR metadata only identified
  separate adoption PR126; lead coordinates overlap with its owner.

Architect brief: [design.md](design.md), Phase 2 execution packages and acceptance.
Exact prose draft: [phase2-typescript-webui-draft.txt](phase2-typescript-webui-draft.txt).
Canonical URL fixed to
`https://github.com/vpsfreecz/vpsadmin/blob/master/docs/api-schema-export.md#generated-client-synchronization`.
Owner3's ready candidate was read in full; unique exact heading verified and
SHA256 `109f3830f889d61785c17831b795ee3a611f624c3a4a25c0707eada31b3c53c2`.
Final canonical candidate is committed at
`4ac49f49e63545200df8afa920c6eafda8722523`; final anchor/hash/meaning reconciled.

## Technical content and quick evidence

Distinguish `haveapi-client` transport from `vpsadmin-typescript-client` generated
operations/types. Development feature/Git/local dependencies remain allowed;
dependent WebUI merges need a published SDK with required members and final
registry manifest/lock/provenance/integrity without temporary overrides. Backend
capability/deployment readiness remains separate. TypeScript releases default to
next minor unless explicitly overridden; ordinary source synchronization needs
no publication. Link the canonical multi-client completion workflow without
claiming automatic CI enforcement.

Whitespace and 96 relative links/anchors in the scoped documents pass. No declared
hook framework/custom hook path/active common hook entries in either repository.
WebUI author/committer are the configured contributor identity, not inferred
host defaults; recheck in actual Nix commit context. No product requirement added;
work log references existing release/provenance requirements REQ-060/068.

Initial `nix develop --command npm run audit:design-docs` failed because the fresh
worktree had not installed its declared TypeScript package. Captured setup failure
in [phase2-webui-audit-setup-failure.md](phase2-webui-audit-setup-failure.md);
no source defect or script workaround inferred. Lead granted one fresh Luna/low
utility for normal locked npm ci then the required audit. It preserves the root
preinstall toolchain check and runs no broad tests/build/Playwright/security audit.
[Brief](phase2-webui-audit-watcher.md); result/log/status passed exit 0 in 23 seconds (409 packages installed, 178
documents, 76 requirements, 257 routes/65 API modules). Native utility
`/root/phase2_webui_audit_watcher` completed and released the one utility slot;
no process remains. Parent did not duplicate monitoring. No dependency lock or application source change authorized.

WebUI policy requires a focused PR. Its actual PR workflows trigger ordinary CI
and Playwright smoke without a docs-only path exemption; no optional manual or
broad/nightly workflow will be dispatched. TypeScript branch pushes trigger its
existing validation workflow. Publish after committed-deliverable review to keep
long automatic checks after that gate. Relevant exact-head CI will be inspected
under the watcher policy. No default merges or PR merge without separate approval.

## Next milestones

Lead writing pass -> finalize successful audit facts -> one docs commit per
repository -> complete Phase 2 base/head/series/no-migrations inventory and final
independent documentation/history review -> publish features/required WebUI PR
and inspect relevant native CI -> hand off concrete approved-integration targets.
No lifecycle or cleanup action authorized.

## Committed documentation checkpoint

TypeScript `c53cb4dabb0b3aac8d05834478872d2cfa698fa7..2da950a98fa13468b36d03b13fb5e81cca206e0e`
and WebUI `1c8478bceb3943645ec06ccde895ee4b0985873f..85f4f8e3820a1063058de9e12b1131eba486628f`
each contain one logical docs/instructions commit, with clean worktrees. No
migrations, repeated update streams or product changes. Lead approved exact
prose/status and permitted colon date heading before ordinary Nix-context commits.
Final packet: [phase2-typescript-webui-review.md](phase2-typescript-webui-review.md).
Feature publication/required WebUI PR and automatic CI follow review acceptance;
no optional local broad checks or manual workflows.

Final narrow work-log reconciliation folded unpushed WebUI head
`3dc264507d167208549e79a18a83d511592bbfe6` into
`85f4f8e3820a1063058de9e12b1131eba486628f`. Only four lines of transient status
wording were replaced with the lead-approved stable workflow sentence; checks,
links, headings and document count unchanged. Focused whitespace/link checks
passed, no audit/setup/suite repeat. TypeScript head remains2da950a.

## Final reversible integration preparation

Fresh SSH defaults unchanged: TypeScript main/clean existing detached target
`c53cb4dabb0b3aac8d05834478872d2cfa698fa7`; WebUI main/new native detached
target `1c8478bceb3943645ec06ccde895ee4b0985873f`. Target paths under this
session group: `vpsadmin-typescript-client-integration` and
`vpsadmin-webui-integration`. Both are detached/clean, unregistered as extra
feature obligations, and are ancestors of exact docs features2da950a/85f4f8e.
No rebase is needed. Actual target config rechecked: no custom hooks path, declared
hook framework or active common hook entries; canonical SSH origins. No app/
dependency preparation, source edit, test, build, claim/default mutation or merge.

Required WebUI draft PR command prepared locally in
[phase2-webui-publication-command.txt](phase2-webui-publication-command.txt),
body `/tmp/vpsadmin-client-sync-phase2-webui-pr.md`. Neither feature publication
nor PR/automatic CI started while independent documentation review runs. Lead
owns later named-target approval/claims. Public-main movement requires ordinary
rebase/equivalence/check handling outside claims; never use peer WIP as baseline.

## Reviewed feature publication

Lead reports final independent docs/history review no findings across all four
lanes, complete one-commit scopes and no migrations accepted. Published both
reviewed features normally. Required focused WebUI draft PR
[127](https://github.com/vpsfreecz/vpsadmin-webui/pull/127) created with prepared
body; no PR merge. Exact TS validation run41678877821 at2da950a; exact WebUI
CI41678908384 and Playwright smoke41678907770 at85f4f8e. Initial run/PR checks
retained in [phase2-typescript-webui-ci-initial.json](phase2-typescript-webui-ci-initial.json).
Automatic checks only, no manual workflow or independent watcher; lead owns
one coordinated native CI batch. Defaults remain original Phase2 bases.
No new integration approval inferred.

## Required PR ready for maintainer review

At lead direction after independent no-findings documentation/history review
and sole-watcher reports of both successful WebUI automatic workflows, marked
[PR127](https://github.com/vpsfreecz/vpsadmin-webui/pull/127) ready for review.
Verified OPEN/non-draft, base `main`, exact unchanged feature head
`85f4f8e3820a1063058de9e12b1131eba486628f` on
`dev/vpsadmin-client-sync-rules`. Existing concise body preserved unchanged.
Fresh SSH public main remains `1c8478bceb3943645ec06ccde895ee4b0985873f` and is
an ancestor of the exact PR head; prepared integration target remains compatible.
No CI/log polling, extra check, utility, source/commit change, merge, default
push, deployment or peer-file inspection occurred. Ready for the user's explicit
Phase 2 repository/target integration direction; Phase 1 approval does not cover it.

## Public WebUI adoption baseline refresh

Independently fetched main670cf286daf9bddb65594035507ca112a9e6d397 and read
public AGENTS/affected docs. Rebased only old1c8478..85f4f8e rule commit into
670cf286..fa7d7732f7982bd99712f3d43cd16086204f2629. One SDK guide EOF conflict
resolved as exact entire public file plus exact reviewed rule suffix; other3
scoped final blobs unchanged. No semantic/new prose or product/dependency edit.
Full patchIDs differ from context and are not claimed equal; bounded raw-byte
construction/range-diff proof retained. Lead reaffirmed original writing pass.
Quick whitespace/97local links pass; fresh scoped audit running for changed
public lock graph. No featurepush yet. Integration target detached/clean at
public670cf286; capture comparison refreshed.

Actual refreshed WebUI audit now passed on fa7d7732, exit0/21s, with real
log/status/result inspected:410packages,257routes/74modules,179documents/
76requirements. Original utility never ran the command; its initialization error
and owner premature-pass withdrawal are retained in the separate correction
receipt. Fresh exact environment/current checks fixed initialization. No tracked
changes or running operation; slot released. Affected review remains gate before
feature publication.

Affected review accepted nofindings. Remote/PR127 refreshed exactfa7d7732;
publicmain670cf unchanged. Native CI41699592872/smoke41699592920 assigned to
sole fresh watcher01a1a2cb-a9dc-7d41-8b1e-20cdedbe2b31 with explicit pinned
Luna/low/full-access/never. No superseded active runs, no cancellation/optional
workflow. Current CI result pending, not inferred from earlier passes.

Final new-head workflows41699592872/41699592920 bothSUCCESS and all6PRjobs
passed, actual JSON/rollup inspected. FinalPR127OPEN/non-draftfa7d7732, fresh
remote main670cf286 unchanged; clean feature. One native mobilewebkit internal
retry annotation/2skips recorded with original joblog and unknown intermittent
cause; no agent rerun or app/testsource change. Slot released; no operation
remains. Concrete docs targets ready for named-target approval; no merge done.
# Current local refresh checkpoint (2026-11-04)

Final observation/handoff complete. All eight manifest runs are terminal and
their actual JSON/head/job identities inspected: seven workflows succeeded;
API Specs41822368583 remains failed in two jobs, with owner3 baseline diagnosis
and lead's scoped residual acceptance recorded. No rerun or source fix. TSmain
default41822889192 and all three WebUImain defaults41827144373/41827144400/
41827144462 succeeded. Full logs/artifacts metadata/direct watch logs retained;
no metadata/log capture failure. Native utility ended, slot released, no remaining
observation. [Final receipt](phase2-integration/default-ci-result.md) includes
parent actual settings verification and exact outcomes. Both owner docs features
and all six Phase2 targets are integrated by the lead; PR127 MERGED. No owner
source commit, default mutation, claim, deployment or lifecycle action.
Earlier pending/failure-only checkpoints below retain their historical status.

Final default-CI batch is not all green: already-terminal API Specs run41822368583
at exact API4ac49f49 failed full/platform-operations RSpec and topic coverage.
Raw terminal JSON and both failed-job logs captured; lead notified promptly.
Other four initially completed runs passed; three new WebUI default workflows
remain owned by fresh utility01a1a67a-bc6a-7722-b09a-ed8afe3931cd. No retry,
diagnosis or source work authorized by this observation package. All six docs
integrations remain actual completed operations; final CI disposition is separate.

Both owned documentation features are now integrated by the lead: TSmain
exact2da950a and WebUImain exact47b6992e, with normal SSH remote proofs and
verified claim release; PR127 is MERGED exact47b6992e. All six Phase2 docs targets
are integrated. Final default-push eight-run observation is separately assigned
to one fresh utility; [manifest](phase2-integration/default-ci-runs.json).
Premerge four-run/ten-job successes remain retained at their actual identities.
No new source work, owner integration or lifecycle action.

Final WebUI verification complete: inspected all4 terminal run/job JSON and
PR127 rollup at exact47b6992e; all4 workflows/all10 jobs SUCCESS. PR remains
OPEN/non-draft with basebabe5142. Full native workflow logs/artifact metadata
retained, no flaky annotation visible; native skips are documented. Complete
streaming watch stdout was truncated, full workflow logs retained instead.
Utility ended and single slot released. [Final result](phase2-webui-final-ci-result.md)
and [current complete packet](phase2-webui-final-refresh-review.md). Lead owns
fresh approved integration; no owner default/claim/deploy/lifecycle action.
Below pending observations are historical checkpoints.

Lead subsequently integrated exact TS2da950a into main with fast-forward, SSH
push/remote proof and verified claim release. At lead direction, one bounded
metadata lookup found new default push run41822889192 (Package validation and
release, main, exact2da950a, created2026-11-04T11:40:54Z). Its later observation
is lead-owned; no logs/status polling or second watcher started here. WebUI
four-run utility remains sole active verification owner.

SSH recovery and feature publication are now complete: fresh TS main/feature
remain c53cb4d/2da950a; WebUI main remains babe5142 and feature/ready PR127 now
exact47b6992e after fa7d7732 lease push. Affected reviewer0 addendum has no
findings. Four exact-head automatic runs (CI41822245078, PRsmoke41822244729,
broadPR41822244823, broadpush41822238396) are owned by sole fresh utility
01a1a659-39ae-7e03-a172-9e20ab62cc68; actual Luna/low/full-access/never settings
verified. Terminal results pending; no duplicate parent polling or manual check.
The previously pending transport/publication wording below is historical.

WebUI now has one local docs commit on independently confirmed cached public
main: `babe51421bd1df61a548e7b2f047053df14ff3eb..47b6992e28c16585aa6247bd75413637a7ca6388`.
Only WORK_LOG conflicted; all newer public entries precede our exact approved
entry. All public bytes and the three other reviewed rule blobs are preserved.
No semantic prose, app/dependency/runtime/pin/workflow edits. Whitespace,
101 scoped links/anchors and fresh Nix docs audit passed (actual exit0/6s,
179 documents, 76 requirements, 257 routes, 74 modules). Utility complete,
slot released. Feature/target clean, comparison captured. TS unchanged at
2da950a over c53cb4d with prior review/CI. Fresh SSH fetch/push pending transport
recovery; no auth retries. Hold feature publication for affected review.
[Complete current packet](phase2-webui-final-refresh-review.md) retains exact
old/new ranges, proof, checks, target state and original evidence. The lead
reports conditional six-target integration approval active after the user's
migration-completion confirmation; no integration/claim is performed here.

