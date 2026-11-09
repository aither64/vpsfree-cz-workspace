# Final component review: runtime rollout successor R

## Findings

No new Blocking, Important or Advisory findings.

R5 from review-native-discovery.md remains explicitly deferred. This review does not claim that its optional diagnostic enrichment was implemented. Earlier R1–R4 closures remain applicable to the unchanged owned behavior.

## Reviewed deliverable and independence

Reviewer: retained reviewer0, saved gpt-6.1-sol/xhigh/read_only. No model/effort override, fallback, nested reviewer or subagent.

Session identity matched `2026-11-03-lead-wakeup-delivery` from the exact bound tracking directory, with both shell markers absent and the trusted developer binding matching the absolute workspace. I read the mandatory-change-review skill and all four lane references, applicable workspace/repository instructions and procedures, current packet/state/design, source receipts, commit series and relevant source context.

Exact reviewed component:
- Base: `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7`.
- Head R: `58e87f9d3ccc1aac262b29f587a1d0553257a554`.
- Tree: `f42361496cab566c9d066f43ede240a44fd82239`.
- Complete range: 47 paths, +8271/-80, two commits.
- Worktree: `worktrees/2026-11-03-lead-wakeup-delivery/dev-workspace`, clean at the stated head.

This is final review of the completed, committed runtime component before publication and dependent pins. It is not an early advisory review, a review of final W/C composition, or a claim that the unbuilt successor is usable live.

## Scope and proportionality

I compared the original reliable idle-lead wake-up request and later implementation/deployment direction with the complete diff, prior reviewed result, recorded milestones and current refresh. The owned capability remains durable non-roster utility outcome delivery through the existing native sender. Current public baseline obligations justify refreshing the runtime rather than selecting the older verified package.

The complete feature is substantial, including a roughly 2,000-line native fixture, the configured-client repair regression and transparent race helper. Those mechanisms address actual caller, receipt, busy-to-idle routing, lifecycle and acceptance boundaries encountered by this feature. The refresh adds no new diagnostic subsystem or scenario: its owned diff is four lines smaller than the old reviewed series.

I found no additional subsystem to remove from R to meet the supported goal. The selected smallest correction here is preservation of the newer public implementation plus the already reviewed monitor capability, with localized reconciliation in two existing owners. No command supervisor, replay mechanism, general search/protocol framework, catalog substitution, timer/poller or forced lifecycle helper is introduced. Optional R5 diagnostics remain follow-up work.

## Independent source reconciliation

I independently computed stable per-path patch identities for old `c2182254..925a76e7` and new `3bb08df2..58e87f9d`. Exactly 45 of 47 owned patches match; only `libexec/dev-session` and `libexec/workspace-host` differ. I also recomputed the complete range-diff, checked the actual committed complete diff against its supplied artifact, verified the recorded artifact hashes, and inspected the reconciled code with its newer surrounding implementation.

Eight owned files have different final blobs from925 because their baseline advanced: the two guides, dev-session, workspace-host, runtime-contract.json, web/server.go and two Ruby test owners. Equal owned patch identity does not mean those complete files or the package are equivalent to925.

The four owned prose patches retain their prior wording. The independently useful tracking-directory test fix remains patch-equivalent and separately committed.

### Lifecycle and registered services

At R, `libexec/dev-session:2546–2557` performs the public baseline's tracking/recovery-location validation before coordination, retirement identity and the monitor idle check. Removing the old four-line duplicate validation block retains those checks rather than weakening them. Pending removal parsing and existing recovery remain in the baseline path.

Archive processing retains the service-cleanup prelude's operation ID, mode and automatic policy (`libexec/dev-session:2107–2145,2189–2219`). Registered-service cleanup and handoff remain ahead of monitor revocation; monitor archival remains inside the ordinary authorized retirement phases. Delete retains saved-service evidence, cleanup guards and preservation before finalization (`2557–2615`). No independent cleanup or lifecycle execution route was added.

The runtime's actual `session.PendingLifecycle` reader includes the registered-service cleanup prelude (`portal/internal/session/lifecycle.go:117 onward`, `service_cleanup.go`). Monitor readiness therefore observes pending service cleanup as a hold, and CLI mutation admission retains the same conflicting-journal guard. It does not rely only on the ordinary archive/removal journal appearing later.

`libexec/workspace-host:2986–2993` retains BOTH session-services and monitor compatibility checks, followed by the existing communication, submission, archive and retry gates. The service implementation and its pending-cleanup refusal (`3014–3029`) remain intact; monitor state adds its own gate (`3032–3050`). The reconciliation does not replace either owner with the other.

### Managed-turn proof and delivery

All listed critical retry/service/claim/identity/pin files are unchanged from3bb. I additionally inspected the managed-send and prefix-proof implementation to assess interaction, rather than inferring compatibility solely from file equality.

Lead outcome sends still enter the configured `workspacecodex.Client.SendWithOptions` through `web/monitor.go` and `monitoroperation/native.go:109 onward`. The baseline wrapper reconciles the generic immutable identity before new admission, captures the managed snapshot, retains the active binding for steering, binds the accepted receipt, and advances managed-turn proof after acceptance (`workspacecodex/turn_retry.go:324–375`). Prefix proof remains based on positively observed native user items, exact binding/epoch/context and saved contributors (`turnretry/managed_turn.go`, `workspacecodex/turn_retry_reader.go`, `turn_retry_proof.go`). Optional proof advancement cannot erase an already durable acceptance.

The known-unsent monitor repair still retires only the existing exact prepared/noqueue input after typed NotSent and fresh readiness; Unknown takes precedence, and the later scan uses the same immutable tuple. It does not discard managed-turn evidence or bypass the configured sender with a raw lead send.

Utility launch deliberately receives the underlying SDK client (`portal/cmd/workspace-portal/monitor.go:289`) and sends its retained launch tuple (`monitoroperation/launch.go:150–167`). This preserves the non-roster, non-automatic-retry boundary. Monitor inventory joins retained ownership for lifecycle/provider proof without turning the utility into a team role or managed retry target.

I found no new conflict between these paths and the baseline managed-turn proof. Existing prefix/recovery and final native/composition coverage must still be exercised on the new source inputs; source inspection is not their acceptance result.

## Contracts, state and rollback

I independently compared both runtime-contract objects: all 35 baseline keys are retained. The only changed baseline value is `workspaceReportingPolicy: 2 -> 3`; the only additions are `monitorOperationStateSchema: 1` and `monitorOperationPolicy: 1`.

The selected public managed-turn proof1, registered-service state/lifecycle1, typed machine claims and machine identity implementation remain. In particular, the public retry state writer/reader and its managed-turn support are retained; R is not a return to925's older retry/state boundary.

The 21 preservation-list files have no base-to-R diff, including flake.nix/flake.lock, machine-claim contract, claim/identity helpers, session-services implementation and listed retry source/tests. The complete changed-path inventory contains no native, SDK, catalog, dependency, channel pin or generated-lock update.

Reporting policy3 intentionally changes the daemon-start MCP invocation. Exact retained policy1/2 proof support remains in the startup validator; new tool availability still requires the ordinary idle daemon cutover. Same Codex bytes do not establish a live-switch equivalence.

The outgoing package gate refuses readers lacking monitor support once operation state exists, including malformed state. Existing service, retry, submission and typed-claim recovery obligations remain independent. Forward recovery is the accurate posture; reverting to925 or removing records to select an older reader is not a supported rollback. The rollout's host-first/user-profile sequence and unresolved external invoker belong to subsequent composition/activation work, not an executable result of this review.

## Architecture and documentation

The generic runtime remains the owner of operation persistence, caller authority, outcome delivery and lifecycle inventory. Existing configured SDK/SQLite submission ownership remains the transport boundary. The refresh combines the service and monitor guards in their existing owners; it does not duplicate the service subsystem or generalize the monitor abstraction.

The guides are discoverable from README's session, portal and monitoring links. `docs/dev-sessions.md#monitor-long-verification`, `docs/workspace-portal.md#runtime-monitor-operations`, the installed monitor skill and `test/README.md` explain distinct workflow, contract and verification responsibilities.

The documentation accurately distinguishes events/queues from native acceptance, known-unsent repair from uncertain reconciliation, reporting from acceptance decisions, and ordinary package/lifecycle permission from monitor completion. The policy3 idle-cutover and forward-recovery requirements are explicit. Individual rollout revisions and prepared steps stay in session design/state rather than being promoted into permanent feature documentation.

The trusted reporting limit remains explicit at `docs/workspace-portal.md:1642–1654`: native proof inventories retained thread/turn, prompts, queues and ledger, not every code cell/tool session. Unreported surviving work is not automatically detected. Fresh pre-bootstrap retirement and archival with a surviving cell remain unverified native boundaries, without a delete/recycle fallback.

## Complete history, consolidation and migration provenance

I independently confirmed that3bb is the merge base and that the complete base-to-R ancestry contains exactly:
1. `e18a1e8de4d599df830e6ac390c9ab306d23d891` — independently reviewable baseline tracking-directory deadline fixture correction, +4/-2.
2. `58e87f9d3ccc1aac262b29f587a1d0553257a554` — one coherent monitor capability, 46 paths +8267/-78, excluding that baseline test.

The capability's production, compatibility, documentation and acceptance changes support the same handoff. Follow-up repairs are incorporated into the capability rather than retained as obsolete iterations. The complete series has no obsolete prototype, superseded implementation, fixup stream or transitional monitor reader. Earlier925 and prior heads/reviews/receipts are preserved separately as provenance, not as extra commits in R's feature ancestry.

There are no repeated dependency/channel/input/pin/generated-artifact update streams in3bb..R. No intermediate-update exception is needed. Later W/C pins are not part of this reviewed range.

No database migrations or seeds are introduced. The private monitor schema1 is introduced directly in its final form. There is no branch-iteration migration, prototype compatibility guard or new format for manifests, rosters, existing recovery, registered services, retry proof or submissions in this range. Existing public baseline formats and their supported legacy readers remain current compatibility obligations, not obsolete branch history.

The supplied monitor provenance is disposable/CI fixture usage with no known deployed/live persistent feature consumer. Nothing inspected contradicts that provenance. I did not inspect private/peer state and do not claim a global absence proof. Historical build/native receipts and old published revisions do not by themselves create a transitional schema requirement. History consolidation and migration/state lineage are sound for this exact component range.

## Verification evidence and remaining gates

I read the retained quick commands/logs. The first batch passed monitoroperation4.172s, teamruntime10.042s and turnretry7.924s. Its agentteams failure was before fixture assertions: inherited DEV_SESSION_REQUIRE_RUNTIME required absent runtime endpoints. The corrected invocation removes that variable, reruns the failed package and previously unrun checks, and records agentteams9.772s, cmd0.070s, web6.075s, session0.055s, repository0.186s and tagged pure transport/compilation0.513s.

The corrected Ruby batches total87 runs/1157 assertions, with no failures/errors/skips; syntax checks pass. The corrected run does not claim rerunning the three already successful first-batch packages. Final R and tested41a8605b have the identical recorded tree; the final change is commit-message metadata. This supports the stated quick-source attribution, not reuse of different Nix derivations or complete-package acceptance.

No new managed package, App Server/native matrix, VM/full runtime suite, composed suite, exact-source CI or live usability verification has run for R. Old925's native11/runtime28/composed6/CI successes remain evidence only for their exact old sources and inputs. R's retained baseline and altered package/input graph require the applicable new verification, including managed-turn/recovery and service/lifecycle interactions.

Final W/C pins, matching nested/root R identities and their composition review remain outstanding. The external invoker and ordinary idle policy2->3 cutover remain activation prerequisites. This component review grants no new execution, activation, integration, deployment or session lifecycle permission.

## Disposition

Final affected-lane review of completed runtime component R is complete with no new findings. General, architecture/repetition, scope/proportionality and risk/compatibility were independently assessed. Earlier unchanged-path review conclusions are reused only within the verified patch boundary; whole-package equivalence is not asserted.

Read-only constraints preserved: no files written, tests/builds/probes/native/push/CI/claims/profile/deployment/lifecycle actions run, or peer-session state accessed. This full report is sent to the lead for verbatim persistence as review-rollout-runtime.md; original reports remain intact.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
