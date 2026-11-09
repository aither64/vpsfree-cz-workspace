# Final affected review: maintenance UI and switch diagnostics reduction

## Findings

No new Blocking, Important or Advisory findings in the completed deletion deliverable at 86cd0f03e9fdab2e40c80912a4284508438f3afa. No reduction-induced remediation is requested.

This is an affected source review of the deletions and required fallout. The current full automatic-maintenance capability is not certified ready. The disclosed native admission-handoff gap, unresolved close/completion boundary and absence of a successful canonical positive cutover remain unresolved. Removing these peripheral features neither fixes those issues nor settles the user's overall size concern.

## Identity, settings and reviewed boundaries

Retained independent reviewer0; saved gpt-6.1-sol / xhigh / read_only, purpose review, same-session roster ready. No model/effort override, fallback or nested reviewer. Before session records, dev-session current from /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-lead-wakeup-delivery printed exactly 2026-11-03-lead-wakeup-delivery. Both environment markers now match that slug and the developer-bound absolute workspace /home/aither/workspace/ai/vpsfree.cz.

Repository/worktree: git@github.com:aither64/dev-workspace.git, /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/dev-workspace.

- Affected range: 9cf1c7694b3918fcef1b088669ee6241605f071f..86cd0f03e9fdab2e40c80912a4284508438f3afa.
- Actual HEAD: 86cd0f03e9fdab2e40c80912a4284508438f3afa.
- Tree: 8a4639809f301f9787bbde3956959215a0778605.
- Direct parent: 3145caa8fcf23b1e825eb54fe9176258f58c6b7f.
- Affected diff: 19 paths, +20/-1146.
- Complete owned range: 3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7..86cd0f03e9fdab2e40c80912a4284508438f3afa; five commits, 121 paths, +25416/-156. Actual merge base is exact3bb.
- Actual worktree and index are clean; receipt checked/tested tree matches the committed tree.

Overall risk remains HIGH because the affected code includes host activation/recovery identity and removal of public UI/API surfaces. All four affected lanes were independently applied.

I read the current top review packet/state, accepted reduction brief, repository/workspace instructions, applicable procedures, mandatory-change-review skill and all four lane references. Unchanged procedure and prior review context was reused where permitted. The review inspected the complete affected diff, deleted owners and their tests, relevant remaining call sites, prepared-ID/startup/worker recovery, docs and quick evidence. Prior full5e68 and affected c79/15f/139f/4c308 conclusions and main R1–R3/owner-reason closures are reused only in unchanged scope. No unrelated full SDK or core implementation audit was repeated.

## General lane: removal boundaries and behavior

The changes form two complete deletions with narrowly necessary fallout:

1. Operations maintenance status/cancellation:
   - Removes web maintenance.go, its projection/reason table and status/cancel handler; removes its two route dispatches and the now-unused mutation-fence exemption in server.go:773.
   - Removes the Operations panel and script, maintenance.js and its dedicated browser test.
   - Removes only the status/projection/cancellation test block and unused unix import from maintenance_test.go. I independently reconstructed the expected retained file: its helpers, existing prompt-response test and monitor reconciliation tests remain byte-identical.
   - Existing prompt-response, interrupt/Stop, ordinary maintenance admission, activity observer and monitor admission paths remain. Removing a cancellation exemption narrows the special mutation path; it does not create a replacement route or new mutation authority.
   - Searches of the actual source/docs/tests/packaging found no remaining consumers of the deleted API, assets, panel hooks, projection or handler.

2. Separate switch timing and parallel diagnostic classification:
   - Removes workspace-switch-diagnostics.rb, its host require/package install and dedicated test require/file.
   - Removes switch_diagnostics, switch_decision and diagnostic-only registration_storage_mismatch? from workspace-maintenance.rb.
   - Unwraps recorder.measure calls to the same underlying prepare, drain, profile selection, wait/readiness and maintenance-control calls. The diff preserves their real lock, rescue and mutation order.
   - The real codex_restart_required? comparison and source, registry, claim, registration, generation and recovery checks remain. The storage-restart test still checks actual restart authority across exact/missing/wrong/absent/malformed storage; only the deleted parallel classification/privacy assertions were removed.

The VM loses only decisions() and its two diagnostic-log assertions. It retains actual native identity, profile selection, registration, pending-target, two-stage bootstrap and recovery assertions. The native fixture differs only by replacing the deleted maintenance.js smoke URL with the existing style.css URL; I verified that exact byte replacement. Its modes, 90-second deadline, ordering and maintenance acceptance assertions are unchanged. The archive-recovery layout drops only the deleted file's copy token. The test README no longer advertises a removed browser contract.

The changed commit description also drops the former browser-coverage claim. Docs/workspace-updates.md and docs/maintenance-mcp.md remove the corresponding UI/timing claims and retain CLI instructions. The existing portal compatibility/admission explanation remains accurate for the deletion boundary.

## Architecture and repetition lane: prepared identity and owning mechanisms

The important functional dependency was preserved rather than deleting the recorder indiscriminately.

workspace-host:649–712 prepares and validates the source/candidate and now generates switchOperationId once with SecureRandom.uuid at line701. SecureRandom remains explicitly required by the retained maintenance owner. The prepared property name and representation are unchanged.

Actual remaining consumers use that prepared value:

- workspace-maintenance.rb:91–111 binds startup-stage/authorize/reconcile and exact selection checks to prepared.switchOperationId.
- Lines192–208 use it as the operation ID and retain the same entire preparation in the Go-owned operation.
- Lines209–226 use that operation ID for roots, worker unit and ordinary waiting/recovery output.
- Worker lines238–245 recover the operation by the supplied exact ID and read its saved preparation. They do not call prepare_profile or mint an ID during recovery.
- The coordinated profile path retains the prepared artifact and passes it into start_maintenance_switch/activate_candidate; it does not rely on the removed diagnostic environment variable.
- DEV_WORKSPACE_SWITCH_OPERATION_ID and all recorder consumers are absent. The distinct DEV_WORKSPACE_MAINTENANCE_ACTIVATION/startup operation grant remains.

The disposable prepared-ID control exercises real prepare_profile and the existing host/worker fixtures: one direct operation UUID generation, same ID in prepare/startup requests, unchanged saved preparation, and a before-finalize failure followed by recovery without any permitted UUID replacement. It requires one profile selection, one continuation and one native drain. The controller/systemd/native effects in these fixtures are controlled test seams, not real cutover acceptance.

Removing the parallel diagnostic registration classifier eliminates a second ruleset that could drift from actual restart admission. Remaining status/cancel/recover ownership stays with the existing CLI/controller. No replacement diagnostics framework, registry, observer or API is added.

## Scope and proportionality lane

The user's size concern and subsequent explicit decision to keep wakeup delivery coupled to full automatic pause/resume both remain binding. I compared those decisions with the final diff rather than accepting the internal reduction design as extra scope.

Deleting the isolated maintenance browser presentation/API and timing/classification layer is a maintainable reduction with clear owners and no replacement subsystem. The +20/-1146 affected diff includes tests and packaging fallout directly tied to those removals. It preserves the required cooperative transaction, ordinary CLI visibility/cancellation and durable recovery.

The complete branch still adds roughly25k lines across121 paths. These peripheral deletions do not demonstrate that the remaining core is the smallest sufficient implementation, and test removal alone would not demonstrate architectural simplification. The packet correctly leaves the core redesign and native prerequisite under separate ownership and unreleased. This report does not approve the unimplemented terminal-tail reduction in design2004–2133 or any later core design.

No optional hardening or new diagnostic framework is needed to complete this deletion package.

## Risk and compatibility lane

The removed browser status/cancel schema and assets were part of the unshipped maintenance addition, not an existing public3bb capability or the historical W/C f161 composition. Current source search finds no remaining consumer. The intentional product consequence is that maintenance status/cancel/recover is CLI-only; the Operations page retains existing coordination controls.

CLI handling at workspace-maintenance.rb:42–57 still supports active/exact status, exact UUID cancellation and same-UUID recovery. Existing ordinary operation-ID, waiting, selected-package and recovery-error output remains. CLI cancellation still records intent through the existing controller; deleting the UI does not convert a cancel request into terminal success or waive cutover restrictions.

The operation UUID remains in the existing prepared record and flows into all functional startup/recovery consumers. No state reader, persisted property, startup schema, journal or recovery handler was deleted. Removal of diagnostic environment propagation does not remove the maintenance activation grant. Existing prepared records with an ID remain usable within their prior supported contracts.

Terminal intents/receipts/restoration, ownership, controller/observer, close classification, native scheduling, EOF policy and SDK transport are outside this affected delta and unchanged. There is no source change that resolves the known core issue. In particular:

- The packet's separate source analysis establishes shared post-HUP queue/goal admission, but identifies a pre-admitted task permit/running-count handoff gap. That concern is not waived here.
- Source exit0 is not a positive persistence/completion proof.
- No successful canonical positive maintenance cutover has been shown.
- The trusted reporting limitation for unreported surviving cells remains; this source review establishes no global quiescence.

The package keeps these concerns visible rather than adding an EOF fallback or relaxing evidence. Their further design, correction and acceptance require their separately bounded disposition.

## Complete history, repeated streams and migration lineage

I compared the actual base-to-head series and final diff inventory with the supplied artifacts. Current ancestry is:

1. e18a1e8de4d599df830e6ac390c9ab306d23d891 — independent tracking-directory admission deadline fixture.
2. 58e87f9d3ccc1aac262b29f587a1d0553257a554 — coherent durable monitor capability.
3. f161ede8a6ea4cf540edcb7ece81ebb76f064a05 — adopted passive archive-hydration diagnostic.
4. 3145caa8fcf23b1e825eb54fe9176258f58c6b7f — maintenance SDK and genuine historical test input.
5. 86cd0f03e9fdab2e40c80912a4284508438f3afa — final current maintenance capability.

The first four commits are unchanged. The deletions are folded out of the final owning capability, so the current series does not introduce then remove the browser/recorder subsystem through extra fixup commits. The actual final message describes the remaining result. No obsolete branch history, transitional diagnostic owner or redundant removal commit remains within this affected comparison and reused full-history boundary.

The retained reviewed9cf1 ref resolves to exact9cf1. It and earlier failed/reviewed heads remain comparison/rollout evidence rather than extra current ancestry. No claim is made that a nonancestor old revision was literally merged or that its checks automatically accept the successor.

No repeated dependency/channel/generated update stream remains. One production SDKc3 selection in3145 binds Go/Nix/vendor inputs. The original3bb/SDKd3 test-only predecessor has a distinct historical consumer and graph; it is not an intermediate production pin. Later flake/package edits install the capability/check, not another SDK selection. All four immutable module/flake inputs match the packet; the packaging delta removes only installation of the deleted Ruby file. Native/model/catalog pins are unchanged.

No database migrations or seeds occur in the full changed-path inventory. This reduction changes no persisted format and removes no supported state reader. Private maintenance schema1 is introduced directly by the owning capability rather than through a branch-only migration ladder. Existing public/monitor/submission/claim/service/retry/state-recovery obligations retain their prior reviewed boundaries. Historical donor external consumption remains unproved; no global absence or private-state census is inferred.

Current W/C pins remain historicalf161. Final composition, mixed-version rollout, artifacts, forward recovery and integration require their separate final evidence and approval.

## Evidence and remaining limits

Main receipt: /tmp/lead-wakeup-maintenance-main-o26asc9e/scope-reduction/committed-reduction.json, SHA256 dd909acc8d8d09ae205d4ffc030bbf6fb7573bcb7b7a65c6d250856900e25101.

D frozen packet: /tmp/lead-wakeup-maintenance-D-reduction-6k84w047/final-D-source.json, SHA256 8aa2703223b61b9a135de43b5b7a011eede7d378d56a80a80979f477cfff17cc. This packet describes the precommit freeze; the main receipt and actual source establish its subsequent committed/tested-tree equality.

I independently matched both packet hashes, seven main artifacts, all19 source/base hashes including deletions, four immutable inputs, eight quick receipts and their logs, and five evidence-script hashes. The D and main full-index affected diff exactly match actual Git; the complete full-index diff also matches. The earlier abbreviated-index comparison mismatch is disclosed formatting only.

Read original quick logs and inspected their scripts without running them:

- Ruby focused:27 runs /377 assertions,0 failures/errors/skips,7.278988s.
- Focused web:1.760s,exit0.
- Tagged command compile:0.047s,NO TESTS TO RUN.
- Static evidence: affected Ruby syntax, Nix parse, embedded VM Python AST, Go formatting/whitespace and deleted-reference absence.
- Corrected disposable prepared-ID control:1 run /16 assertions,0 failures/errors/skips,0.334144s. The first missing-minitest/mock load failure and second overbroad UUID counter failure remain preserved. The latter counted coordination_build's preparation-directory UUID as well as the direct operation UUID. The final harness narrows that count and prohibits replacement IDs during worker recovery; product source did not change to make those harness failures pass.
- Nix dirty-tree/system-rename/cache-busy warnings remain in the original logs; they are not native success evidence.

No tests/evaluation/build/native/browser/VM execution, Git mutation/publication, CI, claims, profile/live activation, lifecycle action or peer/private-state inspection was performed for this review. No acceptance transfers from older native/full-suite/CI graphs.

This report grants no execution, publication, integration, activation or session lifecycle permission. The session remains open; main owns finding disposition and any later source or acceptance release.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/)
