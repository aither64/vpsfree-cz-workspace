# Final affected-lane review: known-unsent monitor delivery repair

Reviewer: retained reviewer0, saved gpt-6.1-sol/xhigh/read_only; no overrides, fallback, nested reviewer or subagent. Session identity matched `2026-11-03-lead-wakeup-delivery` from the exact tracking directory and trusted developer binding, with both shell markers absent.

Read the mandatory skill and all four lane references, applicable instructions, current packet/state/design, exact-source inventory and changed source/SDK context. Applied general, architecture/repetition, scope/proportionality and risk/compatibility to the repair and revised native fixture. Reused earlier unchanged-path assessments and R1–R4 closures. Original reports remain preserved.

Reviewed generic range: `c2182254d29c4175c3e9fe4267e5a92dd1da6b79..925a76e7974784204be15edcf3f3305cbe362e4a`, tree `70995f985386dbb7b44730b1dfa2b604dc3ca561`. Workspace remains `adabd0bdedd45e24d7b8f00c8cbaa30987804302..a595211e2a2a0cec23632a7c9aa06b132eb5dbda`.

## Findings

No new Blocking, Important or Advisory findings.

R5 from review-native-discovery.md remains explicitly deferred. This review does not claim that advisory enrichment was implemented.

## Production behavior and safety

The changed production path is small: `monitoroperation/native.go:109–135` extends the internal client interface with the existing option-aware preparation proof/discard methods and uses them only after a typed known-unsent result. `delivery.go:141–154` makes uncertainty take precedence over NotSent classification.

I inspected the actual unchanged pinned codex-web `d3a29bee90ef00a08816920408c596152339a637` implementation, including `client.go:5146–5179,5196 onward,5277 onward,5469–5504` and `send_delivery.go`:

- Reconciliation leaves prepared/absent attempts unsent and retains unknown submitting outcomes.
- The exact proof checks thread/message, text digest, action context, normalized options, prepared state and no queue attempt. False/absence alone does not authorize discard.
- Discard rechecks the same identity and prepared/noqueue state in its own durable transaction. It retains submitting/accepted/queued attempts. Its “already absent” success is not used as initial authority: the monitor first requires positive preparation proof.
- The normal SDK refusal path restores a definitively rejected claim to prepared. This explains why its retained busy routing can otherwise refuse a later idle send indefinitely.

The repair uses the normal configured SendWithOptions, preserving managed admission/snapshots and SQLite receipts. A receipt, success, generic error or UnknownSendOutcomeError does not enter discard. Unknown wins even when a wrapped/joined chain also contains MessageNotSentError, both in NativeDelivery.Send and in Dispatch.

After positive proof, Ready rechecks the exact current owner/socket epoch, execution permission, lifecycle/provider holds and activity under the caller's existing session/operation admission. A readiness hold leaves the preparation intact. Proof/discard errors or an intervening submitting/accepted state remain unconfirmed for reconciliation.

Successful discard returns the original unsent outcome. No second send occurs inline, and the operation/event/message/body/context/options are not replaced. The later ordinary scan repeats owner, cancellation and readiness admission and lets the existing SDK choose current start/steer routing for that same tuple. Status/resolve reconciliation does not invoke the repair. No unknown native attempt is reset.

This maintains the existing cooperating-writer contract; it adds no guarantee against an unmanaged writer deliberately reusing the same message identity.

## Crash and admission boundaries

The persisted operation is submitting before the first send. Before discard, the exact preparation remains recoverable. If discard commits and the process stops before saving held status, the operation can still be submitting while the SDK row is absent, with the complete original tuple retained. No replacement native call occurred in that interval.

Recovery uses ordinary SDK reconciliation and fresh session admission before any send. It does not infer permission to discard from absent history. Once a new submission claim exists, missing history stays unknown; once accepted, the original receipt wins. Failed/ambiguous storage is not reported as successful retirement.

Cancellation after repair prevents the next scan from sending. Current readiness holds defer it. Transactional discard protects an intervening accepted/submitting writer even after an earlier positive observation. The configured wrapper continues to own normal retry snapshots and bindings; the repair does not bypass it with a raw sender or create a new command attempt.

## Verification source assessment

The new 495-line `native_repair_test.go` is a focused configured-client/SQLite fixture, not a substitute native server acceptance claim. Its assertions meaningfully exercise:

- one definitively rejected steer, one discard, no inline start, then one later same-ID idle acceptance;
- reopening clients and retaining managed snapshot identity/options and accepted receipt;
- the crash after committed discard but before held save;
- cancellation and readiness holds between scans;
- no repair for accepted, queued or unknown attempts;
- absent/mismatched proof, proof/storage errors, fresh readiness refusal;
- intervening accepted/submitting state at discard and joined uncertainty precedence.

The test RPC endpoint deliberately supplies controlled responses. Those results establish the application/SDK composition being tested, not actual native refusal semantics.

The new steer-race native helper in `turn_retry_native_proxy_test.go:166–403` is separate from the older receipt-rewriting proxy. It forwards original request/reply frames unchanged, binds only the exact root/event/expected turn, and counts actual refusal and acceptance replies. Its pure transport check verifies byte-preserving forwarding and that an arbitrary upstream error does not become a fabricated refusal/acceptance.

The native case deliberately pauses the exact steer before forwarding, releases the already-held real lead, and uses a separate passive native client to prove that exact turn completed and native status became idle. Avoiding full ledger-idle proof at this particular barrier is correct: the deliberately pending steer still owns its submission claim. Final full configured native/ledger idle proof is retained after settlement.

Successful acceptance still requires one real native no-active-turn refusal, one later same-ID accepted idle start, one matching history input, unchanged source/owner/event/settings and actual native receipts. The case fails if it cannot obtain the actual refusal. It does not hide history or manufacture a response.

The revised setup now requires the exact accepted materialization TurnID to complete before initial lead input. The native-restart precondition uses the already-open configured client's underlying SDK with the correct shared SQLite ledger, preserving the complete guard instead of relaxing the deliberate legacy-JSON migration fence. These are justified fixture preconditions; neither has native validation at this successor.

## Scope, architecture and documentation

I compared the original reliable idle-lead wake-up goal with the complete 47-path +8275/-80 deliverable, the eight-path +956/-9 delta since reviewed/published ad476, and the new eight-path +861/-7 package over630. The production routing gap is an ordinary busy-to-idle race within that goal.

The fix delegates persistence/routing ownership to the existing SDK. It adds no command supervisor, generalized retry API, scheduler, schema, dependency change or public MCP/CLI contract. The internal interface extension is supported by the actual configured client; production composition continues to supply its admission and receipt behavior.

The additional configured-client controls and one transparent native race case address the new safety boundary. The helper remains local to acceptance testing. A generic proxy/protocol framework or broader tool policy is not needed. The native-restart diagnostics remain bounded evidence for the previously unclassified failure; they are not promoted into product policy.

The owning portal paragraph accurately describes positive unsent proof, current admission, one preparation retirement, later-scan routing and continued reconciliation for unknown/accepted/queued input. The documented trusted cell/session reporting limitation is unchanged.

## Complete history, consolidation and migration/state lineage

I independently confirmed the full generic series:
1. `468bb300ff13924da8e4ecd2b3d6cdb61486a880` — isolated baseline tracking-directory test correction, +4/-2, parent c2182254.
2. `925a76e7974784204be15edcf3f3305cbe362e4a` — coherent monitor capability, parent468bb300, 46 paths +8271/-78, excluding the baseline test.

The capability message now explicitly explains known-unsent re-admission and preservation of unknown/queued/accepted inputs. The workspace still has one unchanged guidance commit and reviewed blob `1c0f21aa79b831f65b24b68e7896979266082871`.

No obsolete prototype/fixup history or transitional migration remains in either final ancestry. Historical failed/probe/source heads and receipts are separate retained provenance, not redundant feature commits. The complete series remains coherent.

No repeated dependency/channel/pin/input/generated-artifact update streams exist. No retained-update exception is needed.

No database migrations or seeds. The original private operation schema1 is still introduced directly. This repair changes no persisted schema or existing manifest/roster/recovery/submission format and adds no abandoned-prototype reader. Known-unsent preparation retirement uses an existing SDK state transition, not a storage migration. Existing package-transition and forward-recovery restrictions remain.

The supplied provenance records disposable known fixture state and no known deployed/released/integrated/external persistent feature consumer. Prior ad476 build/CI/native results do not require an intermediate supported schema. Nothing inspected contradicts that provenance; migration/state lineage remains sound without claiming global proof about all possible external consumers.

## Exact evidence and remaining acceptance

Both worktrees were clean at the stated heads. I verified generic HEAD/tree/merge base, complete series, changed-path inventories, final range whitespace, and all eight final file hashes against final-source.json. The preserved original/adapter/discovery report hashes still match the source receipt.

Reported quick checks are full monitoroperation3.675s, web monitor0.438s, command monitor0.089s, pure proxy0.063s and tagged compile0.056s. I also read the final combined tagged pure-proxy log showing exit0/0.065s. Its precommit dirty-tree notice does not change the source scope: final hashes and committed tree match. No real App Server was exercised by these checks.

Five actual native passes and successful CI belong only to published ad476 / package Pn9. They are not verification of925a76e7. Full current-source managed build, native11, runtime28, composed6 and source-specific CI remain outstanding. A diagnostic combining a new harness worker with an older candidate MCP/CLI must retain both identities and cannot establish final packaged-source acceptance or equivalence.

The trusted utility/lead evidence contract for cells/tool sessions and the unverified fresh pre-bootstrap archive boundary remain explicit. This review proves neither global cell quiescence nor native archival with surviving cells.

## Disposition

Affected final review of the committed repair is complete with no new findings. Earlier R1–R4 closures and the recorded R5 deferral remain intact. The lead can continue the already authorized verification workflow after recording this disposition; review itself grants no new execution, integration, deployment, package selection or session lifecycle permission.

Read-only scope preserved: no files written, tests/builds/probes/native/push/CI/lifecycle actions run, or peer-session state accessed. Full Markdown is sent to the lead for verbatim persistence as review-unsent-repair.md.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
