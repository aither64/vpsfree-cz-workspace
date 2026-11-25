# Archive preparation timeout

Design owner: architect0. Core implementation owner: implementer0, after lead
acceptance of this brief. Deployment preflight/input lineage owner: implementer1.
This document releases a sufficient core-fix boundary; deployment source selection
remains subject to the independent preflight and the lead's allocation.

## Scope and first failure

The sole retained failed portal lifecycle operation is an explicit archive of
ordinary session `2026-10-30-oomd-abuse-policy`. Its private sensitivity registry
directory exists and contains no record for that slug. Only task-relevant metadata
was inspected; neither the session nor its worktrees were changed.

- Browser receipt: `1d67ac2326c9672f6654d63f5b9bbed7edb2a3ba1ca986880a515203823536d2`.
- Intended journal ID: `2d436becb1a344e4c98e31f9b1378cb996ce0145063f198ea1fd35b79999db27`.
- Attempt 1 ran from `2026-11-25T09:27:43.380043991Z` to
  `2026-11-25T09:28:13.402762608Z`, failing in phase `checking` with
  `context deadline exceeded` twice, separated by a newline.
- The durable preparation contains `ready=true`, six passed checks out of six,
  zero blockers, `monitorLocal.state=quiescent`, round zero, no history and
  `bestStage=-1`. Thus ordinary readiness completed, but preparation did not reach
  its progress/history update or archive handoff.
- No archive journal or cleanup sidecar exists for this target under
  `worktrees/.locks`; its creation and service-registration records remain.
  This failure is before the archive executor, not checkout removal/recovery.

Evidence locations under `~/.local/state/dev-workspaces/portal/` use workspace ID
`vpsfree.cz-8a2a555cb2f65b33`: `lifecycle-operations.json` and
`archive-preparations/2026-10-30-oomd-abuse-policy.json`. Read-only monitor inventory
currently finds 59 native monitor operations owned by that session, each with a
native thread and no archived disposition. The inventory does not establish that
those threads are executing: the accepted readiness result proved quiescence.

## Cause and source identity

In `portal/internal/web/archive_preparation.go`,
`tryArchivePreparationAdmission` creates a 30-second context covering admission
and the readiness callback. `runArchivePreparation` runs `dev-session
archive-check` in that context. `libexec/workspace-archive-check.rb` already asks
the native monitor lifecycle helper for `assess-local`, including native utility
identity/receipt/quiescence checks, and returns its typed `monitorLocal` result.

After validating that successful result, the browser unconditionally calls
`quiescePreparationMonitors`, which calls `Lifecycle.AssessLocalSafety` again.
That repeats sequential native proof for the same retained monitor inventory
using the remainder of the same deadline. The saved successful result and absent
history localize this failure to that second safety assessment. The 59-record
inventory explains why redundant proof is expensive; individual RPC timing and
the exact record at deadline were not logged and are not claimed here.

The path is present in both local `origin/master` at
`65544340f94ebb112872743738f84c1a7022b06a` and the currently selected package source
`/nix/store/vp5r16m56956rrm0dvza0li169qdjkaw-source`. Implementer1 identified selected
package `/nix/store/1zn1a51qrsin83fszrprdjp45208vsj4-dev-workspace-0.2.0`, generation
290, selected during this investigation. Package B subsequently bound its actual
deriver and immutable composition lock to runtime
`91cafd4c0c50ffb7208498a605707c4c3b1b1174`, tree
`f3bff8f5008ade6561a92856eec22a25ac48488c`. All tracked files, symlinks and
executable modes match. The equal-tree fixup predecessor `4f096ff9` is not the
selected locked revision. The shared workspace lock is not installed-source proof.
Bare repository `HEAD` is stale (`52dcd471186ef874c5c93f4133744195d4815454`) and must
not be used as an assumed current base. The incident predates generation 290;
its retained receipt establishes the failing boundary without claiming that the
current package was the incident package.

## Package C: core fix and regression

Owner: implementer0. Own only the current session's dev-workspace feature worktree.
Expected files:

- `portal/internal/web/archive_preparation.go`.
- `portal/internal/web/archive_preparation_test.go`, or its existing nearby
  monitor preparation fixture if that gives clearer coverage.
- A short clarification in `docs/session-archive-recovery.md`, beside readiness
  and local CI observation, if useful to explain the proof's lifetime.

Use the CLI's just-returned, validated `monitorLocal.state=quiescent` result to
avoid redundant monitor assessment/quiescence work in the same admitted readiness
callback. This is a local control-flow fix; do not persist or cache an accepted
proof, add a new backend interface, increase global deadlines, parallelize the
native inventory or rewrite lifecycle contracts to solve this case.

The shortcut must depend on the typed monitor result, not merely `ready=true`.
When the optional field is absent, retain the existing fallback assessment.
When it is blocked or quiesceable, retain the existing fresh local assessment,
coordination and complete-blocker admission, exact observer ownership, durable
archive binding, original-worker cancellation/join, and full readiness recheck
after detachment. Respect context cancellation before proceeding. Do not turn an
unavailable or inconsistent result into quiescence.

The readiness result is advisory and is consumed immediately under its existing
generation/runtime admission. It is not authority to remove resources. An
observer or native utility that changes after this sample is caught by the
ordinary executor's required fresh readiness and lifecycle checks before
shutdown/removal. Those checks must remain intact. Sampling again immediately in
the portal is not atomic exclusion and does not strengthen that executor contract.

### Dependencies and ownership

The core control-flow contract is settled and independent of deployment routing.
Lead acceptance releases implementation. Implementer1 owns deployment input
inventory and rollout preparation; architect0 owns this design file. The lead
owns source/base selection where current installed lineage differs, worktree
allocation, Git mutation sequencing, review invocation and activation authority.
No other member should edit core files concurrently. Report consequential scope
or safety changes through the lead; routine clarification goes to architect0.

Before choosing a core base, obtain implementer1's exact installed-source/input
comparison. Preserve all unrelated deployed changes in any candidate. A focused
patch can be prepared on the lead-approved repository base independently of that
later composed candidate; do not select a different package merely because the
shared lock points to it.

### Acceptance and quick checks

1. A fresh validated quiescent readiness result reaches archive handoff without
   reenumerating native monitor identities or performing observer mutation.
   Cover the expensive native-history case with a synthetic fixture: native
   proof on the redundant path would consume a short parent deadline, while the
   already successful CLI result is sufficient. Assert native call counts and
   handoff/progress state, without a real 30-second sleep or real sessions.
2. Absent monitor data keeps the existing assessment path. Blocked, unknown-owner,
   coordination-blocked and truncated-blocker cases still refuse without repair
   sends or detach mutation. A quiesceable observer follows its original owner and
   joins, then receives a full new readiness check without spending repair rounds.
3. Cancellation, changed receipt/target and package/runtime admission fences remain.
   Ordinary executor revalidation remains visibly unchanged; no new journal,
   receipt, manifest or recovery format is introduced.
4. Focused Go checks in the repository Nix shell, with `-mod=readonly`, cover
   archive preparation and monitor lifecycle/refusal tests. Run quick syntax/
   formatting and applicable hooks. Do not rerun unrelated passing suites for
   reassurance; report exact base/head, files and command/results.

Existing tests include `TestArchivePreparationDetachesQueuedCIWithoutRepairAccounting`
and `TestArchivePreparationMonitorRefusalsDoNotRepairOrDetach`; preserve their
coverage and extend the nearest fixture. Use synthetic native identities and
disposable state, never copies of another session's mutable runtime.

## Compatibility, delivery and recovery

No CLI/HTTP shape, optional field, on-disk schema, provider behavior or ownership
authority changes. Older packages can read the same preparation and lifecycle
records. They retain the old timeout risk, not a new compatibility obligation.
No database migrations. Existing failed receipts remain untouched; there is no
archive execution journal from this attempt to repair.

The owning project is generic dev-workspace. A runtime source fix normally needs
the workspace's composed user-profile package; it does not by itself require a
NixOS host configuration change. Implementer1's preflight owns that conclusion
and exact input lineage. User permission to deploy aitherdev does not authorize
default-branch integration or any target session's archive/revive/stop/delete.

After committed quick checks, independent final review covers the complete branch
and the unchanged executor safety boundary. After review, run the package check
and the required `session-archive-lifecycle` NixOS check against disposable test
state before deployment, with the monitor skill for uncertain/long execution.
These fixture lifecycle operations are part of the isolated test, never live
session actions. Other VM checks are required only if changed inputs or repository
rules justify them.

Prepare a composed candidate preserving the complete current deployed lineage,
then follow the selected package's transition and machine-ownership procedure.
Do not select an older profile for rollback: current package policy is forward
only. Recover a failed switch through its existing journal or a newer corrected
candidate, preserving the original contract. Record exact candidate/profile,
source graph and verification in the rollout receipt owned by implementer1/lead.

After deployment, verify portal health and conversation continuity by permitted
reads. No live archive/revive smoke, failed-target retry or session cleanup is
authorized by this package; any procedure requiring such a live action must be
reported to the lead as an explicit remaining verification boundary. A later
user-authorized retry uses the ordinary accepted request and fresh checks, never
receipt editing or private lifecycle helpers.

## Settled and remaining

Settled: exact failed receipt, pre-executor boundary, redundant proof/deadline
cause, narrow fix, safety invariants, file owner and regression acceptance.
Ready for lead acceptance and implementation release. Remaining: exact deployment
input graph/base alignment from package B; implementation/check evidence; review;
isolated packaged checks; authorized deployment and its permitted verification.
No broader history investigation or actual archive retry is needed for the fix.

## Candidate composition follow-up

The lead accepted the core brief and separately assigned this bounded deployment
design question. Package C remains independently implementable on the approved
current-default base. These findings do not authorize a build, switch, peer
recovery, integration or live lifecycle operation.

### Exact deployed baseline and existing proof

Package B resolved the selected derivation's composition source as
`/nix/store/csv89jnlh1zrbi9xff9ahmkzjsg6zmgf-source`. Its immutable lock selects:

- Runtime `91cafd4c0c50ffb7208498a605707c4c3b1b1174`, NAR
  `sha256-w8rK1jDoPlHI8Z/Im0Zeo/1qA5OkgCMhZEYCXOF6vSk=`.
- Extension `bf12ac71a8a00b1581eed5352f99c1b2daaeff5b`.
- codex-web `2547d535eefd4154afef4125ea0fb76e5894a8b6`.

The installed runtime has 34 changed tracked files from `65544340`
(4217 insertions, 232 deletions); its complete
unmerged series is `9bf34aa1963e3ba226ec678237cee3dacb2e7a25` followed by `91cafd4c`.
The three proposed C file paths are unchanged between those two baselines.
This supports an independent additive patch; it does not prove future patch
equivalence without checking C's actual final content.

The existing owner is ordinary session `2026-11-23-pi-message-delivery`; source
sensitivity was checked before retaining these references. Its `review.md:1992`
records the accepted final affected review by retained reviewer0/Sol/xhigh and
retains the full `65544340..91cafd4c` history conclusion: unchanged P plus one
consolidated R, no obsolete final update stream and no migrations. The preceding
affected review is at `review.md:1972`. Preserve and cite those original reports;
do not recreate review of the unchanged Pi implementation here.

Its `rollout.md:3` and `/tmp/pi-d13-91ca-composed-source-proof.json` bind the final
application/deriver/source to all 1148 tracked runtime blobs, the unchanged worker,
Node and SDK, site catalog, 26 immutable inputs, and exact final checks. The
mechanical receipt `/tmp/pi-d13-91ca-mechanical-pin-review.json` binds workspace
`9d302f8fa4ad70f0281d5cbd8b5bd0f84b2ac0fc` and configuration
`9bdb0c68b47ceebde450fcdf018727b382cacc09`, including full graph reconstruction.
It also records a patch-equivalent workspace successor
`e7b876f69aca4554d52a3ac19ed097263847ad43` on `172c1457646b06fe082364ebf4d2f9aba7199d09`
with identical six derivation/output/metadata identities. These receipts are
reference evidence, not authority to mutate their sources or inherit approval.

### Smallest supported delivery path

Prefer completing C's independent patch/checks/review while the existing owner
finishes its already-running recovery and integration. Once a fresh default
contains the selected runtime lineage, rebase C onto that default and record the
old/new base/head ranges and patch equivalence. This avoids creating an additional
delivery branch carrying another session's still-unmerged commits. The lead owns
the final base choice and allocation; do not wait to implement the settled fix.

If a candidate must be prepared before that integration, allocate only this
session's own runtime worktree/branch, rooted at immutable `91cafd4c`, and apply
only C's completed patch. Do not use or alter the owner's branch/worktree/index.
Require the final tree to equal the installed tree plus that patch, and preserve
the complete source/input graph in this session's rollout receipt. Existing
code outside C's boundary must remain byte-identical to the installed baseline.

Use this session's own workspace/configuration branches to select the published
candidate runtime through the established nested runtime override and confctl
channel. Preserve the installed extension, codex-web, sibling inputs and follows
paths, site catalog and runtime contracts. Run the normal cross-lock check and
compare effective host derivation/modules before deciding whether a system
change is needed. Parent receipts support a profile-only candidate, but the
actual final candidate must independently establish that same boundary.

Retain the existing accepted review as evidence for unchanged baseline behavior.
C is substantive, so adding it is not a certified mechanical refresh that waives
independent final review. This session's reviewer receives the complete candidate
range/diff, the original baseline review/history/migration conclusions, C's patch
and equivalence evidence; the lead invokes only applicable affected lanes under
the review skill. Mechanical pin reconstruction can use the existing mechanical
exception, while whole-branch history/consolidation conclusions remain required.
Check reuse requires exact derivation and complete input identity; tree equality
alone cannot reuse the old application test/build result after C changes source.

### Remaining activation boundary

At this inspection the owner's current `state.md` reports its approved profile
activation running under Aitherdev claim `6097deba`, with retained-runtime recovery
and integration next. The selected new profile proves selection, not that those
effects have finished. Its rollout header still says prepared/not deployed;
therefore do not treat that document as final activation/claim-release proof.

No source-ownership blocker prevents C or an isolated content-preserving candidate.
Activation is blocked on the other operation's actual recovery/integration and
authoritative machine release, followed by this session's own fresh machine
ownership and selected-package freshness checks. Do not claim, switch, stop,
repair or message the other session to clear that boundary. Lead/implementer1
must inspect authoritative state at allocation/activation time; no broad peer
history read or polling loop is needed. Later package changes require refreshing
the candidate proof, rather than overwriting a newer selected lineage.

### Final candidate reconciliation

The lead selected the isolated installed-preserving path. Implementer0 published
`f6d60bf87002fb1896599f35f0284743c16d7e6f` directly above `91cafd4c`.
[Core evidence](core-evidence.md) records byte-identical old/new C patches,
range-diff equality, stable patch ID
`ea289e0482d2c0a6289b45abc29526862c1fbbe5`, and independent application of the
original patch producing final tree `0ab8c211365bedcd18ddc8fd5074db72b54df562`.
The original installed range changes 34 files, not the earlier reported 27;
the complete candidate changes 37 files. This count correction does not change
the preserved content or the three-file C boundary.

Implementer1's final workspace `18275679109c2adda4084af1ea7474e21be98b4e` and
configuration `6f6cb452e17ca663114a07013a0402ef85a7fee3` select that exact runtime
with only the existing runtime lock nodes changed. Their complete graphs and
checks belong in [deployment evidence](deployment-evidence.md), with execution
in [rollout.md](rollout.md).

The host comparison from parent configuration `9bdb0c68` to final `6f6cb452`
follows all differing dependencies through five paired derivations. It terminates
at the two confctl provenance JSON files. The system, activation and `/etc`
derivations differ only through those metadata contents and resulting store-path
references; service, module, kernel and native payload dependencies are unchanged.
This supports the existing profile-only design relative to that parent candidate.
It does not prove that parent equivalent to the live `109d789` system, that prior
activation/recovery finished, or that either exact system derivation was deployed.

There is no new core design or configuration implementation requirement. Before
profile-only activation, the lead must connect the parent host-compatibility proof
to the freshly observed live system and reconcile the prior owner's effects and
machine release. That is the remaining host proof dependency. If it cannot be
established, retain the hold and return the specific gap to the deployment owner;
do not label a different system derivation identical or activate merely to publish
provenance. Independent review and required candidate checks remain as allocated.
