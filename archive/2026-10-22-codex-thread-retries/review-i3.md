# I3 affected independent final review

## Findings and disposition

No Blocking, Important or Advisory findings in the reviewed I3 correction. I3 is resolved for the accepted managed-authority contract. The earlier B1 safety, I1 reconciliation and I2 quota conclusions remain valid; unchanged A and scope conclusions are retained.

The correction does not promise automatic proof after native turnover, cold load or uncertain settings. Those cases deliberately retain the new epoch with no binding and require the existing later explicit managed binding owner. This is the architect/lead's recorded conservative boundary, not an unresolved I3 finding.

## Authority and production composition

Reviewed dev-workspace commit 5347f5ddacf321216b818a1e8a0373b7edbb3304, particularly portal/internal/workspacecodex/turn_retry.go:511-579.

UpdateThreadSettings acquires managed admission, obtains the exact current state and retains only an already verified current-epoch binding. Before the settings effect it advances the provenance epoch, consumes the prior active/failed turn and durably writes Binding=nil. Outstanding automatic uncertainty refuses the effect without changing its immutable Pending tuple.

Only an unambiguous successful explicit settings operation can promote the locally retained inherited binding. Both cold observations must show loaded active status, a nonempty identical latest TurnID and inProgress status. The owner rechecks provider, socket identity, authorized policy including MCP/access, common instructions and managed execution permission. It updates only the binding epoch/digest, saves under admission, and leaves prior snapshots and queue admissions unchanged. Failed or unavailable continuity checks cannot promote; no persisted sessionId is used. The promotion introduces no additional resume, rebind, native settings write, display-derived authority or public A contract.

I independently checked the cited pinned rust-v0.163.0 source:
- app-server/src/request_processors/thread_lifecycle.rs:59-83 permits automatic unload only after both no subscribers and inactive state.
- app-server/src/request_processors/thread_processor.rs:3872-3886 selects the warm path; :4520-4530 obtains the existing object; :4566-4616 only permits override-driven replacement when idle/unsubscribed/not running; :4664-4783 rejoins and responds from that existing object.
- core/src/session/session.rs:932-952 restores sessionId from persisted metadata, confirming it cannot establish loaded-instance continuity.

Also checked the actual application client composition at portal/cmd/workspace-portal/main.go:58-66 and the selected A client's settings/resume policy implementation: PreserveThreadInstructionsOnResume=true keeps implicit resume from supplying role/MCP/access rebinding. Together with the same ongoing turn and the existing managed lifecycle/admission fence, the inherited-witness promotion is supported. This conclusion does not extend to unmanaged direct native writers.

The production active QueueWithPolicy path now captures the successfully promoted current binding without needing the idle-only binding helper. Subsequent execution still requires exact client-ID/content history plus the exact native turn context for actual model/effort/mode and policy; enqueue defaults do not become execution authority. Old-epoch active/queued work stays excluded. The controller's scheduling and Check paths do not repair settings or alter native queue order.

## Tests and residual native gate

Inspected all of portal/internal/workspacecodex/turn_retry_settings_test.go and the provided final logs. The tests establish prior binding through actual ActivateThread with role/common instructions, MCP/report tool and execution policy. The eight root/member positives call actual UpdateThreadSettings and active QueueWithPolicy, then exercise the real rollout/context reader, receipt correlation, Backend.Prove/Check and Controller scheduling. They verify old queued input is refused, new-epoch input qualifies with actual execution settings, FIFO/old snapshots/quota remain unchanged, and proof/scheduling adds no native mutation. This corrects the helper-only composition gap from the prior report.

The 22 refusal variants cover pre/post cold or idle state, completion/queue turnover, missing prior binding, provider/socket/policy/MCP/access/common changes, authority/postcheck errors, failed/uncertain settings and failed promotion persistence. Additional tests cover refusal before the durable boundary and preservation of the old uncertain tuple.

Provided receipts show the final committed-head selector passing in2.680s; affected race packages passing core4.565s/workspacecodex8.480s/web7.566s; and tagged native compile/list passing with TestNativeTurnRetryController listed. These are inspected owner results; this reviewer ran no tests. Synthetic wrapper tests model the pinned warm-object semantics and do not constitute an empirical native inheritance result.

Residual verification remains the planned pinned-native campaign, including settings/queue inheritance and busy-race compatibility, full package checks/builds and later live acceptance. Native compile/list is not native execution. Native-direct busy behavior remains a compatibility gate and cannot prove global exclusion. Review approval supplies no deployment, merge or lifecycle authorization.

## Exact review scope and identity

Same retained reviewer0: gpt-6.1-sol/xhigh/read_only, ready review-purpose identity confirmed through the live roster. No model/effort override or fallback. dev-session current returned2026-10-22-codex-thread-retries; both DEV_SESSION markers were absent, consistent with the trusted developer workspace/session binding.

HIGH risk; affected general, architecture and risk/compatibility lanes performed directly using the mandatory skill and references, prior reports, current packet and precise architect brief. Unchanged applicable procedures/repository guidance were retained/rechecked. No source edits, tests, nested agents, resource claims, deployment, merge or lifecycle actions.

Repository: git@github.com:aither64/dev-workspace.git, target master.
Common base: bf6d4b0c49600c15e17fe71248807ef43424e932.
Prior reviewed head: cca49782ebd2d5135352cea4cb140548b36f7de9.
New reviewed head:61de5e28d1cb1936aeb3ef2376cdaf17f6034e4b.
Final tree independently confirmed:401177e01abbba13009e4a197d694b15d0e58839.
HEAD, merge base, clean worktree and complete final diff whitespace independently checked.

## Whole-branch history, schema and consumers

Complete base-to-head series inspected with the previous full-branch review and current old/new comparison:

1.7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99 core, unchanged.
2.b3c7187c6e26e269994433716a0ee719d0a7edf7 package capability, unchanged.
3.5347f5ddacf321216b818a1e8a0373b7edbb3304 owning runtime, with I3 folded.
4.61de5e28d1cb1936aeb3ef2376cdaf17f6034e4b sole final codex-web pin, unchanged patch.

The I3 delta contains only the explicit settings owner, production-wrapper tests and owning recovery-guide paragraph. Core/schema/I1/I2 and public A behavior are unchanged. The logical commit split remains adequate. No obsolete unmerged approaches, fixups, redundant pin updates, transitional migration steps or branch-iteration compatibility shims remain. The runtime patch deliberately changed; this is affected independent review, not a patch-equivalence claim.

The sole B codex-web stream remains consolidated to d2d74f931cc50e39345c6c15931748062ee51951 across Go/Nix/vendor metadata. The final pin patch ID independently remains54bed62a7a4a2053fde96119c5b8d6f018a21082, and the old/new B lockfiles are identical. No new consumer contract or dependency stream was introduced. Original A review remains applicable. Matching final workspace/configuration repins and complete composed input graphs remain the lead's separate final-readiness check; this B report does not certify unfinished or stale downstream pins.

No migrations: no database migration or private-state upgrade sequence. Final prerelease retry schema1/capability1, required epochs/keyed charges and native submission schema3 are unchanged. Provenance remains unmerged/unreleased/undeployed with no external predecessor; earlier shapes were only disposable fixture data. No intermediate format or compatibility bridge is required.

## Documentation and readiness

The new paragraph in docs/turn-retry-recovery.md accurately states successful same-active continuity, inherited MCP/instructions/access, conservative turnover/cold/uncertainty refusal and the sessionId limitation. It remains discoverable in the owning recovery guide and leaves individual rollout evidence in session records. Documentation placement and adequacy are acceptable.

All reported B findings are now resolved for this exact reviewed head. B is ready for the post-review verification phase, subject to final matching C inventory and the existing native/package gates. This is not readiness for live use or integration approval.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
