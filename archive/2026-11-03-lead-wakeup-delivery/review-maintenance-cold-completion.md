# Final affected review: cold completion and held target

## Findings

### Important R1 — Target admission does not establish the held-target contract

Lanes: risk/compatibility, architecture and general. Head: fb7820b3ddda043c4e5053201726e0fc02939d78.

Source anchors:

- libexec/workspace-maintenance.rb:90–95 accepts maintenanceMcpPolicy1 as package support; lines484–491 require only the existing maintenanceStateSchema/maintenancePolicy/maintenanceMcpPolicy1 values for retained state.
- libexec/workspace-host:682 and724 invoke those checks at preparation/fresh validation; line1202 checks them at target activation.
- New host activation at lines1216–1225 supplies the required real-operation hold locally.
- portal/cmd/workspace-portal/maintenance_control.go:60–76 routes operation semantics to SourcePackage; lines539–558 admit the exact prepared package/native/plans without establishing its held-start behavior.
- Retained86cd:libexec/workspace-host:1216–1227 lacks the new operation hold and starts deferred portals after successful reconciliation. Its runtime-contract.json advertises the same three policy/schema1 values.

A cold-protocol source can therefore admit a target such as86cd that passes the current descriptor and ordinary preparation checks but does not implement held activation. When the worker selects it and executes its _activate, the target can start application writers before the source worker reaches proveDestinationSources. The later empty-loaded check may detect the consequence and refuse, but it cannot undo work already loaded or queued/goal work already activated. Exact SourcePackage routing preserves the protocol owner; it does not constrain the target's activation implementation.

This is a source-backed compatibility gap, not a claim that such a mixed-version cutover or work loss was observed. The separate unsupported-native limitation does not supply the missing target contract.

Minimal remedy: declare the held-completion behavior in the existing package descriptor and require a supported value when a cold-protocol source admits/revalidates/activates its target, before shutdown or selection/service effects. Missing/unknown support must refuse that protocol. Preserve schema1 readers, historical SourcePackage ownership and ordinary startup-only behavior; no journal marker, generic probing framework or native API is needed. Add a focused old-policy1 target refusal control and a supported-target held-start control at the real admission boundary. The exact descriptor design/allocation remains with main/architect.

Main and B independently confirmed this gap. No remedy is implemented in the reviewed head. Under mandatory-review policy it requires a fix or an explicit recorded disposition before further acceptance work; this report grants no execution.

No additional Blocking, Important or Advisory finding was established in the affected source. The incorrect-tag verification concern was corrected during this review as described below; it is not an outstanding source finding.

## Identity, settings and exact bounds

Retained independent reviewer0, purpose review, saved gpt-6.1-sol / xhigh / read_only. Same-session roster reports that exact identity and ready state. No model/effort override, fallback or nested agent.

Before records, dev-session current from the exact tracking directory printed 2026-11-03-lead-wakeup-delivery. DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE both match the developer binding and /home/aither/workspace/ai/vpsfree.cz.

Runtime repository/worktree: git@github.com:aither64/dev-workspace.git, /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/dev-workspace.

- Affected range: 86cd0f03e9fdab2e40c80912a4284508438f3afa..fb7820b3ddda043c4e5053201726e0fc02939d78.
- Actual HEAD: fb7820b3ddda043c4e5053201726e0fc02939d78.
- Actual tree: bb9d1dd3843a8322b1ba5bef908b1c272639e89c.
- Direct parent: 3145caa8fcf23b1e825eb54fe9176258f58c6b7f.
- Affected diff:22 paths,+916/-390.
- Complete owned range:3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7..fb7820b3ddda043c4e5053201726e0fc02939d78; five commits,121 paths,+25944/-158.
- Exact source/worktree/index remains clean. The checked code matches the committed code; main's final wording changes are confined to the two documented prose files.

Overall risk HIGH: persisted operation semantics, protocol ordering, host startup/forward recovery and continuation. All four affected lanes were independently applied. I read the current complete top packet and state, mandatory skill/all four lane references, repository instructions, applicable workspace procedures and relevant design/docs/source/tests. Unchanged prior full and affected reviews/closures retain only their original boundaries. No unrelated SDK or native-producer audit was repeated.

## General lane: completion ordering and source preservation

The runtime removes the post-finish observer-completion loop and maintenanceOrderlyExitCandidate/transport-error classifier. Normal/going-away close no longer receives a maintenance completion annotation: web activity passes the ordinary invalid event, and disconnect invalidates coverage while retaining the first diagnostic origin. Pre-cutover continuity, poison, wait readiness and exact effect membership remain required. This adds no EOF-success rule.

maintenance_cutover.go:182–198 now publishes finish only after global drain, then deliberately releases/joins the existing owner before waiting for native exit. maintenance_owner.go:126–147 requires every service's drain and every originally acknowledged call's finish publication before this post-cutover release. Exact owner disappearance/join and exact source successful service exit remain separate requirements; release does not set Finished or a resume obligation.

The new proveDestinationSources pass at maintenance_cutover.go:310–369 precedes delivery. It checks all captured services cold, each participant's destination/process/epoch/session identity, acknowledged finish proof or natural-terminal cleanup, then checks service coldness again before writing resuming. A later participant failure prevents an earlier pending participant's first continuation. recordDestinationFinish clears stale Finished on failed proof and retains Stop-aware obligation creation.

NativeAdapter.VerifyFinished at native.go:403–510 composes the exact latest completed source turn, original MCP item/three arguments/successful literal finish result with completed-parent and descendant cleanup. It uses cold parent samples, complete existing item/turn pagination, notLoaded/absent-loaded proof and no active-source pending-item exception. VerifyColdIdle reuses the natural-terminal cleanup for participants with no maintenance finish, without inventing a finish result or obligation. The descendant path now also refuses synthesized interrupted histories lacking positive terminal timestamps.

Focused tests inspected include wrong/missing finish, later missing participant, old Finished bit, natural late effect, loaded target/child, missing/nested child edge, unresolved grandchild effect, normalized interrupted history, Stop-suppressed completion, owner release before native exit, source-owner routing, held mismatch refusal and ordinary startup-only behavior. They exercise the actual reducers/adapters/controller or local transport boundaries. Controlled responses and injected identities are unit evidence, not native cutover receipts.

The native fixture adaptation uses original drain/finish, owner release/join, source Wait and passive restart proof. It retains wrong-item rejection, queue/goal preservation, Stop, provider-call guard, modes and original90-second budget. It has not been executed on this head.

## Architecture and repetition lane

Completion authority is moved to one explicit history phase rather than maintained in both observation-close classification and passive history. The change reuses the existing adapter, effect validators, journal, worker, startup grants and stable continuation identities. There is no new history service, event buffer, scheduler, native RPC or completion-state table.

Historical operation ownership is now explicit: maintenance_control.go resolves the immutable SourcePackage from the scoped request/validated record and forwards the unchanged request, arguments and worker flag to that package. The Ruby worker does the same before worker claim or phase interpretation. Missing/mismatched owner refuses; current profile or CandidatePackage is not substituted. Global no-operation status/startup remains outside continuation authority.

Once resuming has been recorded or a continuation has been admitted, recovery reconciles the original attempt rather than demanding that an already resumed thread remain cold. The inspected original explicit-send test primes and reconciles a real SDK persisted receipt; unknown activation recovery uses loaded membership. Known-unsent retry retains the original kind/identity. These are consistent with the all-source-before-first-admission ordering in the new source owner's protocol.

The new held-target implementation uses the existing defer_portals path and blocks its post-reconcile portal-start branch. Generic reconciliation with a registration mismatch refuses before drain/quiesce/adopt/restart or its compensation path; a matching passive inventory refresh does not start writers. Ordinary startup-only pending grants without a real nonterminal operation keep their previous restoration behavior.

R1 is the missing cross-generation half of this ownership: the source cannot assume another package contains that held-target implementation merely because it can read schema1.

## Scope and proportionality lane

The user's size concern and explicit choice to retain coupled delivery with full automatic pause/resume were treated as the scope authority. Accepted design text did not expand that scope.

The production portion is11 files,+292/-272, net+20. It deletes a separate transport-completion classifier and post-finish observation authority, replacing them with composed passive proof and held startup. The larger test additions directly cover the new phase, recovery and refusal boundaries. Net line count alone is not a simplification proof, but removing the competing completion authority is a concrete reduction in concepts.

Source-owner dispatch is justified by the changed meaning of resuming/Finished across current and retained operations. The target hold is required to keep completion proof passive before any resumed work. Neither is an optional general framework. R1 calls for a finite owned contract distinction, not another compatibility subsystem.

The complete branch still adds about26k lines and does not yet prove smallest-sufficient whole automation or successful delivery. The native task/admission/accepted-mail work remains separately unresolved. This component review does not choose safe mailbox refusal versus preserving park/restore, authorize a native patch, drop durable queue/goal automation or approve the unimplemented terminal-tail reduction.

## Risk, compatibility and recovery

The new protocol does not equate native exit0, dropped terminal socket delivery, a stored Finished bit or a finish-publication intent with persisted completion. Missing or negative completion remains a held-target recovery condition. Stop-suppressed acknowledged actors still pass finish proof and receive no continuation; natural actors pass cleanup without synthetic acknowledgement.

The worker's original startup/profile/claim/token and source/destination process/session bindings remain. Original invocation and uncertain-send ownership are preserved. Continuation and restoration are not inferred from a sent pause message or a transport close. Writer restoration remains after continuation settlement under its retained journal.

No new public native API, SDK pin, model/catalog selection or persisted checkpoint format is added. The same schema1 operation records are retained, with changed protocol semantics owned by exact SourcePackage dispatch. This is a substantive semantic change despite stable serialized fields; it is why old phase/Finished values cannot independently certify the new ordering. R1 separately prevents the current target-support declaration from being treated as sufficient compatibility evidence.

Owning docs/workspace-updates.md and docs/maintenance-mcp.md now explain held startup, all-source cold completion, exact source-owner recovery and the native prerequisite. They retain the existing unreported-cell limitation and distinguish ordinary first reader installation from later automatic operation. Main's final prose accurately states that accepted native mail may survive only in memory and that an empty durable user queue is different evidence. These docs remain reachable through the existing README/portal links.

Remaining native limitations are material and not waived:

- Continuous task/admission ownership through dispatch and cleanup is not corrected by this delta.
- Accepted memory-only child mail may remain after a sender finishes. Completed send/child history and an empty user queue do not establish consumption or preservation.
- The user product choice for that mail remains pending; no native API, patch or pin has been selected by this review.
- There is no successful canonical positive cutover. No inference of captured work loss, global cell quiescence, persistence from exit0 or live usability is made.
- A newer target cannot retroactively establish source-native guarantees. First-install/initial-window and later automatic-source acceptance remain separate obligations.

## History, consolidation, streams and migration lineage

The actual complete current series is:

1. e18a1e8de4d599df830e6ac390c9ab306d23d891 — independent tracking-directory admission deadline fixture.
2. 58e87f9d3ccc1aac262b29f587a1d0553257a554 — coherent durable monitor capability.
3. f161ede8a6ea4cf540edcb7ece81ebb76f064a05 — adopted archive-hydration diagnostic.
4. 3145caa8fcf23b1e825eb54fe9176258f58c6b7f — final maintenance SDK plus genuine historical test input.
5. fb7820b3ddda043c4e5053201726e0fc02939d78 — current coherent maintenance protocol.

The first four are unchanged. Superseded observer-close machinery is folded out of the final owning capability, not retained through fixup ancestry or dual production paths. Old strings in serialization/negative tests do not preserve that completion branch. No obsolete unmerged approach or transitional migration stream remains in current ancestry within the full-history review boundary; R1 is a current compatibility defect, not an obsolete-history defect.

The retained86cd review ref resolves exactly. Earlier reviewed/failed heads remain refs and evidence, not claims of successor acceptance or literal merging of nonancestor revisions. The final message describes the cold-completion result and its source-native prerequisite.

No repeated dependency/channel/pin/generated-artifact stream remains. The sole production SDKc3 selection in3145 binds Go/Nix/vendor inputs; original3bb/SDKd3 is a distinct test-only historical consumer with its own graph. Later flake/package changes install capability/checks rather than select another SDK. All eight supplied input hashes match86cd, including the runtime contract and maintenance types; no native input changed here.

No database migrations or seeds appear in the complete changed-path inventory. This delta introduces no durable format or migration. Private maintenance schema1 is introduced directly; its retained readers and original public/monitor/submission/claim/service/retry formats remain. Historical donor external consumption remains unproved, so no global absence claim or private-state census is used. Source-owner routing preserves historical operation semantics instead of silently converting records.

W/C still pin historicalf161 and provide no current composition acceptance. Final consumer pins, builds, mixed-version rollout and default integration remain separate.

## Exact evidence and verification correction

Main receipt: /tmp/lead-wakeup-maintenance-main-o26asc9e/cold-completion/committed-cold-completion.json, SHA256 a7106d22f9ab741cda69f149f2d65c9e661e8ac5b4bcab26633b7e1fad6e7169.

B frozen packet: /tmp/lead-wakeup-cold-completion-B-yb2p9qj3/final-source.json, SHA256 5cf93f1a3efecf64ba5e47d9074089cc89ac7b523cc13b031ce5a99842373780.

I matched both packet hashes, all five main artifacts,22 final sources/base pairs, eight unchanged inputs and21 original log hashes. Actual affected/full full-index Git diffs match the main artifacts. Checked code matches final code; only the two main-edited docs differ from B's draft hashes.

Read retained focused results: full internal maintenance4.778s; affected command0.904s; final owner/drain/all-source/routing0.873s; exact SDK receipt reconciliation0.140s; startup0.724s; web activity0.301s. Ruby held/restoration2/64, ordinary deferred2/8, owner/client restoration3/24, ordinary startup-only1/3, held mismatch1/16 and corrected helper1/21 pass. Original incomplete-session, missing-helper, unforced-branch, ordinary-fixture and assert_nil failures remain, including the partial failing ruby-held-final batch. They are not relabeled overall success. Nix warnings remain.

The frozen packet's -tags native_integration command did not include maintenance_native_integration_test.go, whose line1 requires live_switch_integration. I reported this concrete gap; it is excluded-fixture evidence, not changed-fixture compilation.

Main separately authorized B's one correct-tag compile, now retained in review-followup-result.json SHA256 afffcce5d147f413585eb3fee3ccff4c4744574451163b1bc01b675dd59a4dd9. I inspected the exact command/log and matched its five fixture/input hashes and log SHA256 7ee5b06bf3ef116818770f019a8a0fcb3f54597e04d7e9f3964eb00a621c606d. It used declared Nix Go1.26.6, actual portal/go.mod, -mod=readonly, -tags live_switch_integration, -run ^$, -count=1; PASS0.058s, NO TESTS RUN. GOWORK=off explicitly disabled workspace use; it was not empty. Main accepted that exact qualification. No second compile is needed for this evidence correction, and no native/fixture execution is inferred.

I performed only read-only source/history/evidence inspection. No tests, evaluation, build, native/browser/VM call, CI, Git mutation/publication, claim, profile/live operation, lifecycle action or peer/private-state inspection was performed by this reviewer. B's separately authorized compile is attributed to B above.

Review is complete; reviewer0 returns capacity explicitly. No new follow-up work is implied. Main owns R1 disposition and subsequent source/acceptance release. This review grants no execution, publication, integration, deployment or lifecycle permission; session remains open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/)
