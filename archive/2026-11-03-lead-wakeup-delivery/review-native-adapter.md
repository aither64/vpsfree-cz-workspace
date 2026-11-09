# Final affected-lane review: pinned native adapter

Reviewer: retained reviewer0, saved gpt-6.1-sol/xhigh/read_only. No setting override, fallback or nested reviewer. Session identity matched `2026-11-03-lead-wakeup-delivery` from its exact tracking directory and trusted thread binding; both shell markers were absent. Applied all four mandatory review lanes, reusing the original review for unchanged runtime paths. This report supplements and does not replace review.md.

Reviewed generic successor: `c2182254d29c4175c3e9fe4267e5a92dd1da6b79..01f5b1bac08ced29fdde660fa90ba4b8c81828c3`. Workspace `adabd0bdedd45e24d7b8f00c8cbaa30987804302..a595211e2a2a0cec23632a7c9aa06b132eb5dbda` is unchanged.

## Findings, ordered by severity

### R2 — Blocking: separate the independently useful baseline test correction

Lane: general / commit coherence. Commit `01f5b1ba`, `portal/internal/repository/tracking_directory_test.go:20–26`.

The monitoring capability commit also changes the existing repository-reader test so its successful filesystem reads no longer share the 10 ms saturated-slot deadline. That is a sound, independently useful baseline test-stability fix, with its own explanation in the commit body. It neither exercises monitoring nor depends on the monitor implementation. CI discovery explains why it was fixed, not why it must be bundled with the capability.

The mandatory general lane explicitly classifies independently reviewable changes bundled without a convincing inseparability rationale as Blocking. Keep this correction, but put it in a separate focused test-stability commit. Keep monitor implementation, its directly affected fixtures and its guidance together. Preserve the historical source refs and verification receipts outside the cleaned series; no native rerun or source removal is required merely to split the commits.

The lead has acknowledged this split in current state; it is not yet present in the reviewed head.

### R3 — Important: direct-tool result parsing rejects the pinned native framing

Lanes: general and risk/compatibility. Commit `01f5b1ba`, `portal/cmd/workspace-portal/monitor_native_integration_test.go:323–366`; helper cases at `TestMonitorNativeCallOutput`.

The direct MCP route requires one bare Operation JSON block or string. Pinned Codex 0.165.0 adds a timing header to direct MCP results: its `McpToolOutput.response_payload` inserts a separate header block for content arrays, or prefixes the header to text. The current parser rejects the array as ambiguous or fails JSON decoding of the prefixed string. See the pinned [native output implementation](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/context.rs#L211).

This affects the required root gpt-5.5 start route, which remains a direct MCP call. A successful operation start can therefore become `backendFailure` when the next model request contains its actual acknowledgement, before the original completed-and-idle lead barrier succeeds. The pure helper test currently supplies bare Operation JSON, which omits that real framing.

The analogous direct-shell branch also expects JSON `exit_code/output`, while the same pinned native file renders direct shell output through `ExecCommandToolOutput.response_text` with status/header text. Its structured result is the separate code-mode return, not the direct model-visible body. That branch is a latent instance of the same mismatch; the selected Luna route uses code mode.

Minimal remediation: normalize the finite pinned direct output framing, then validate the exact correlated call/type and one real Operation payload or actual terminal shell result. Add representative timing-header/content-array and prefixed-text cases, plus error/duplicate/malformed rejection. Preserve exit 7, payload bounds and output correlation. Alternatively, explicitly refuse an unused unsupported direct-shell variant instead of claiming to parse it. Do not manufacture tools/results or change model policy. No native probe is needed to establish this source mismatch.

### R4 — Important: define the operation-owned cell/session boundary in production instructions and docs

Lanes: risk/compatibility, general documentation and scope.

Source at the reviewed head:
- `portal/internal/monitoroperation/launch.go:54–58` gives the production utility its reporting contract.
- `service.go:245–258` clears the reported-effects fence for terminal passed/failed with empty stillRunning, or a saved resolution.
- `service.go:293–306` labels a resolved operation quiescent after the existing proof.
- `lifecycle.go:69–73,127,148–176` delegates to thread/turn/prompt/queue/submission proofs.
- `native.go:121–140` and `delivery.go:230–238` observe the original turn, not a separate cell inventory.
- `docs/workspace-portal.md:1526–1532` and the monitor skill describe independent native-work fences without explaining this limitation.

Pinned native source explicitly retains yielded cells after their initial response and permits cells to outlive a turn. See [execute_handler.rs](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/code_mode/execute_handler.rs#L141) and [nested dispatch](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/code_mode/mod.rs#L334). The inspected managed proofs do not independently inventory those cell lifetimes. An authoritative command exit establishes the source command result, but is not by itself evidence that every other operation-owned cell/tool session ended.

Consequently, the broader “active native work remains independently fenced” explanation is stronger than the established monitor contract for CodeModeOnly utilities. The new fixture deliberately emits one awaited, non-yielding call per cell; its success would prove only those scoped calls. It cannot close the production boundary for other surviving cells.

Smallest necessary current correction:
1. Add the cell/tool-session obligation to the runtime-owned utility brief and owning skill: account for every operation-owned cell/session, finish all other outstanding work before terminal passed/failed, and await the reporting call itself before ending the turn. If an unexpected yield/session cannot be reconciled, report incomplete with its exact stillRunning identity and evidence. Do not infer completion from an idle turn or invent rerun/interruption authority.
2. Make evidence resolution explicitly cover those known cell/session effects as well as the source command. Retain known uncertainty until exact evidence accounts for it; ordinary idle proof is not a substitute.
3. Document that automated native checks cover the retained thread/turn, prompts, queues and submission ledger, not a complete cell inventory. An unreported surviving cell remains a limit of the trusted reporting contract. State the supported boundary and any accepted residual risk explicitly.

This does not require a generic cell supervisor, model/catalog substitution, automatic cleanup, new persistent schema, or unconditional permanent lifecycle refusal. A live orphan and an actual archive bypass have not been proved; native ArchiveThread behavior with a surviving cell is still untested. Do not describe either outcome as established. The bounded instruction/documentation correction can retain the existing notification mechanism and existing uncertainty fences.

## Protocol adapter assessment

The central change is justified by actual pinned transport behavior, not model-name inference. Responses Lite supplies developer AdditionalTools; CodeModeOnly exposes the outer custom executor. The fixture reads the real advertisements, validates the pinned grammar/namespace, emits custom_tool_call with raw JS input, and checks exact nested ALL_TOOLS identity plus callability before awaiting the real registered shell or candidate MCP call.

Arguments are serialized as data. The generated cells contain one awaited nested call, reject shell sessions without terminal exit, reject MCP errors, and project only actual acknowledgement identity fields. Output handling correlates call ID and output type and rejects running/failed/terminated cells, wrong slots, missing exits and duplicate markers. Durable operation/native receipt/history assertions remain authoritative; the marker alone is not accepted as wake-up evidence. The direct-output mismatch in R3 is the concrete exception found.

There is no fake lead dispatcher, synthetic receipt, substituted utility catalog/model or new native case. The existing host-selection shim still execs the candidate Go CLI. The original completed-and-idle lead barrier, source/run identity, actual turn start/steer, duplicates/restarts/cancellation and unchanged-roster assertions remain. The code-mode/native nested-result contract needs real execution after correction; pure helper success is not that evidence.

## Scope and maintenance surface

I compared the original minimal durable wake-up scope with the final 45-file +7165/-80 deliverable, the eight-file +1134/-83 delta since my original review, the E1a one-file +477/-28 adapter delta, and the recorded failed-build/diagnostic milestones. The runtime scope remains the accepted handoff capability; no scheduler or general job supervisor was added.

Most added adapter surface has a concrete current purpose: actual Lite projection, outer grammar validation, safe argument generation, nested result validation and exact output correlation. The raw-envelope/schema diagnostic helpers are broader than the accepted decode paths, but are bounded, avoid prompt/instruction values, and presently support an acceptance path that still has not passed. They are diagnostics, not additional supported protocol variants. Keep compact role/call/identity failure evidence; simplifying obsolete wrapper/type matrices after the actual shape is settled is optional follow-up, not another delivery gate. Do not grow them into a general schema/protocol framework.

The unrelated baseline reader test is separable as R2 states. The other changes since 992 are the directly related starvation remediation, original-validation-order restoration, current reporting-policy fixture alignment and native acceptance evidence.

## Earlier R1 and unchanged runtime

The successor gives dispatch and observation independent batch budgets, dispatches saved events first, bounds individual waits and advances cursors before waiting. Its focused two-operation regression exercises both blocked observation and blocked dispatch while B's saved event is accepted with the original identity. This addresses the original R1 in source. I reuse the original independent assessment for unchanged authority, state store, launch, delivery identities, lifecycle/provider inventories and package contracts, subject to the newly understood cell boundary in R4.

## Complete history, repeated streams and migration/state provenance

The complete generic range currently contains exactly one commit with parent/merge base c2182254. The workspace still contains its one unchanged reviewed guidance commit and blob `1c0f21aa79b831f65b24b68e7896979266082871`. The complete final file inventory and the 992-to-final path inventory agree with the packet. No hidden product-path delta or conflict resolution was found outside the eight supplied paths.

No obsolete prototype commit series remains in the final ancestry; historical failed/probe heads are retained as separate evidence refs, not as intermediate feature commits. However, final commit coherence is not yet approved because R2 requires isolating the independently useful baseline fix.

No repeated dependency/channel/pin/input/generated-artifact update streams exist. No consolidation exception or supported intermediate revision is needed.

No database migrations or seeds. The final private monitor-operation schema 1, roster/manifest/recovery/submission formats, and startup compatibility lineage are unchanged since the original review. No transitional migration or abandoned-prototype reader was introduced. The packet records only disposable local/CI state and no deployed/released/integrated/external persistent-state consumer. Published acfd CI used an earlier source but does not establish a supported intermediate state schema. On the inspected complete histories and supplied provenance, migration/state lineage remains sound. No global absence of every possible external user is independently proved.

## Verification and remaining acceptance

The exact committed native fixture hash matches `684303df89097f8675f0cb0593ebf7467aa22625f782a95ad13ccea0105bbf5f`; generic HEAD was 01f5 and clean during inspection. Scoped final diff whitespace checks passed. Packet/source receipt reports the focused pure-helper/JS-syntax/empty-registry/tagged compile result at 0.486 seconds; these checks execute no real nested native shell/MCP call.

Prior package/CI/probe evidence remains tied to its actual historical source. No ten-mode native acceptance has passed. A diagnostic harness against the protected acfd candidate must identify both harness and candidate heads and cannot certify final-source equivalence or acceptance. Final exact-source managed package, native matrix and required full generic/composed checks remain outstanding.

Code-cell retirement and fresh pre-bootstrap archive remain specifically unproven boundaries. Do not convert the non-yielding fixture into a claim of general native cell quiescence. Review does not authorize integration, deployment, package selection or session lifecycle actions.

## Disposition

Affected-lane review of the committed successor is complete: one Blocking history finding and two Important findings. Keep long native/probe/build/push work gated until disposition under the mandatory workflow. The described bounded fixes can be inspected and quick-checked directly under step 9; a new enforcement design, schema, public contract or expanded supported boundary would require the affected step-10 review.

Read-only scope preserved: no files written, tests/builds/native actions run, or peer-session state accessed. This Markdown is sent to the lead for verbatim persistence as review-native-adapter.md; original review.md remains intact.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
