# Final affected-lane review: finite root MCP discovery

Reviewer: retained reviewer0, saved gpt-6.1-sol/xhigh/read_only. No override, fallback, nested reviewer or subagent. Session identity matched `2026-11-03-lead-wakeup-delivery` from the exact bound tracking directory and trusted developer binding; both shell markers were absent.

Applied general, architecture/repetition, scope/proportionality and risk/compatibility to the committed discovery delta. Reused the earlier independent reviews and the recorded direct R1–R4 remediation verification for unchanged paths. This report supplements the preserved review.md and review-native-adapter.md.

## Findings

No new Blocking or Important findings.

### R5 — Advisory: discovery failure logs omit the returned definitions being rejected

Lane: general / verification evidence. Commit `ad4765801a61f8025b413931212e89916f6cc958`, `portal/cmd/workspace-portal/monitor_native_integration_test.go:247–288,1163–1165,1213–1214`.

The helper validates the real definitions from tool_search_output in its local discovered slice. If identity/schema validation then fails, the backend logs monitorToolSchemaSurface(tools) using the outer request advertisement. The ordinary input trace does not classify search outputs or retain their ID/status/execution/count. A failure can therefore show the original search-only advertisement and a generic schema/unavailable error without showing which returned namespace/function/schema was actually rejected.

This does not admit false success, repeat a query or weaken ownership. It is a diagnostic gap in the new stage. The small improvement is a bounded metadata-only summary of the matching search output: expected/observed call ID, status, execution, result count and the existing schema-surface projection of returned definitions. Retain no descriptions, prompt data or full MCP payload. Reuse the existing summarizer; no generic discovery framework, extra variants or native scenario is needed. This can be accepted/deferred as an Advisory decision.

## Actual pinned protocol assessment

I independently read the official commit `360319d8dee62d87e2d59fc0c21805d79519cfed` through the GitHub contents/blob APIs, including the exact blobs supplied in the packet. This avoids relying on the previously ambiguous cached excerpts.

- `core/src/tools/context.rs`, blob `c80a89ddd1fe2adb5a36b36016cdd5f4a3198b43`, constructs a tool_search_output with the same call_id, status completed, execution client and a tools array serialized from real LoadableToolSpec values.
- `protocol/src/models.rs`, blob `351f45c03c943fac9bc9d2f195a5b927fa844ba2`, requires execution on the output and represents call arguments as a JSON object/value rather than function-call argument text. The emitted call matches the pinned router's client-execution dispatch and upstream SSE helper.
- `tools/src/responses_api.rs`, blob `aaf67c88e87d728d2813434932dc8bcb9cfa8d38`, provides the tagged function/namespace serialization used by the result.
- `core/src/tools/handlers/tool_search.rs`, blob `220fb3c11ab6a347ef2416bbfb31213c5e843628`, and `tools/src/tool_search.rs`, blob `c25daad32f5c8cc911e3a9b4d3dce8554d01a5ee`, show that direct search materializes/coalesces actual namespace/function definitions. Normalization preserves the function name and input parameters while setting defer_loading and removing output/truncation metadata. The fixture does not need to interpret a flattened alias.
- The native MCP namespace/name construction and search-prefix implementation agree with selecting mcp__team_reporting / monitor_operation. apply_search changes namespace descriptions, not callable identity.
- The real search advertisement has query:string, optional numeric limit, required query, additionalProperties:false and execution:client; the fixture's admitted shape matches it.

Primary source links: [output constructor](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/context.rs#L284), [protocol output/call types](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/protocol/src/models.rs#L872), [loadable serialization](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/tools/src/responses_api.rs), [search normalization](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/tools/src/tool_search.rs).

These are source-contract conclusions, not evidence that this fixture has executed the native route successfully.

## State, dispatch and acceptance evidence

The finite helper has three local fields: search identity, captured start JSON and whether start was sent. If the actual direct MCP definition is available, the existing direct start path remains. Only the exact missing-MCP sentinel permits discovery; malformed/conflicting advertisements are not silently converted into a search.

The new path emits one fixed query for monitor_operation using an actual advertised client search tool. Its discovery call ID is separate from the later MCP call ID. Recovery of the next model request requires one same-ID completed/client output with a bounded, nonempty array of real function/namespace definitions. Wrong IDs, duplicate outputs, aliases, malformed/empty/oversized results and unsupported schemas refuse. The original start JSON must remain identical, and discovery cannot repeat after a saved search or repeat start after StartSent.

The helper feeds the actual returned definitions to the existing direct-MCP selector and schema checks. It never fabricates a tool definition. Search output is not placed in pendingCalls as an Operation acknowledgement and does not advance utility/report phases. Once start is emitted, its separate pending MCP acknowledgement still has to pass the existing framed-result/operation validation.

The root's original completed-and-idle barrier, launch/source binding, real command/PID/exit evidence, exit 7 handling, saved operation outcomes, actual start/steer receipts, transcript correlation, duplicates, restarts, cancellation and unchanged roster assertions remain. The utility's actual ALL_TOOLS/callability and awaited nested-call path is unchanged; no utility search stage was added. No fake tools, dispatcher or receipts, model/catalog/configuration substitution, new native scenario or longer case budget was introduced.

## Scope and architecture

I compared the user's minimal durable wake-up request, the supplied failed bab diagnostic, the final +7328/-80 complete diff and the +211/-7 single-file discovery delta. The failed diagnostic has a concrete boundary: 13 root tools, no MCP definition, actual native client tool_search, and failure before utility start. A single root-only discovery step is a conventional response to that established native deferral contract.

The change remains local to the synthetic native test backend and its focused helpers. It neither exposes a production discovery interface nor introduces a reusable search registry, scheduler, fallback matrix or persisted state. The existing direct selector owns MCP identity/schema checking, so the new stage does not duplicate that policy.

The additional helper tests are proportional to the new state/correlation boundary: immediate direct start, exactly one discovery, immutable start, no discovery-as-acknowledgement and finite refusal paths. No extraction into a general protocol framework is justified. The existing diagnostic projections still serve the unpassed acceptance path; R5 identifies the small place where the new stage does not yet feed them its relevant evidence.

## R1–R4 and complete branch history

I confirmed the complete generic base-to-head series:
1. `468bb300ff13924da8e4ecd2b3d6cdb61486a880` — test: isolate tracking directory admission deadline. Only tracking_directory_test.go, +4/-2.
2. `ad4765801a61f8025b413931212e89916f6cc958` — monitor: deliver durable utility outcomes to idle session leads. The capability commit excludes that baseline test path.

This resolves R2's commit-coherence objection. The baseline test correction and monitoring capability now have separate independently reviewable purposes. The other R1/R3/R4 fixes remain in the capability commit; their supplied direct verification is reused. The R4 launch instructions explicitly account for other cells/tool sessions and the reporting cell, and owning docs state the trusted-reporting limitation rather than claiming complete automated cell inventory.

The capability is 44 paths +7324/-78; complete range is 45 paths +7328/-80. The only bab-to-final source delta is the reviewed native fixture. Generic HEAD/tree match `ad4765801a61f8025b413931212e89916f6cc958` / `f8e61e9cffe73fb3bfd7b872dc99e7e25dc27901`.

Workspace remains the previously reviewed single guidance commit `adabd0bdedd45e24d7b8f00c8cbaa30987804302..a595211e2a2a0cec23632a7c9aa06b132eb5dbda`, with blob `1c0f21aa79b831f65b24b68e7896979266082871`. It has no new affected content.

No obsolete prototype/fixup series remains in either final branch ancestry. Historical failed/probe heads and receipts are retained separately as provenance; they are not transitional feature commits. The final two-commit generic series is coherent. No repeated dependency/channel/pin/input/generated-artifact update streams exist, so no consolidation exception is required.

## Migration/state lineage and compatibility

No database migrations or seeds. No new state format, persisted schema, dependency pin, public runtime protocol, package capability or deployment contract was introduced by discovery. The private operation schema 1 and existing manifest/roster/recovery/submission formats retain the original reviewed lineage. No obsolete prototype reader or migration path was added.

The supplied provenance records disposable local/CI fixture state and no deployed/released/integrated/known external persistent-state consumer. Published historical acfd diagnostics do not require an intermediate state schema or retained pin stream. Nothing in the inspected series contradicts that provenance. Migration/state lineage remains sound, without claiming global proof of absence of every possible external user.

The utility cell/session boundary remains the explicitly documented trusted reporting/evidence contract. This adapter does not introduce automated cell inventory. Native archival with a surviving cell and fresh pre-bootstrap retirement remain unproven; this source review establishes neither a live orphan nor archive safety for those cases.

## Verification limits and disposition

I verified clean worktrees at the stated generic/workspace heads, the complete commit/path inventories, final scoped whitespace checks, and native fixture SHA256 `a9b1c63c8f795a8df13d0bc0c00ae132d7faf89d25d0d24b8f3afc844a6b13a7`. The earlier reports retain their recorded hashes: review.md `da0b2afeaafce5650c5fd85cdfb48f05efcce690641baa2863743edf71314ec3`; review-native-adapter.md `9dfba6ed0c5171563ebd5316c1f4f620acc25dad7a21ed5a2642d3b6005456df`.

Packet reports the affected helper batch at 0.453 seconds, followed by final exact-source TestMonitorRootDiscovery at 0.078 seconds and tagged compilation. These are pure/compile checks, not real native discovery, nested tool execution or wake-up acceptance.

Affected-lane review is complete with one Advisory finding and no Blocking/Important findings. Record its disposition and proceed under the lead's existing verification authorization. Final-source managed build, native matrix, full generic/composed checks and source-specific CI remain outstanding. A diagnostic harness against the older protected acfd candidate must retain both source identities and cannot establish final-source acceptance or equivalence.

I performed no file writes, tests/builds/native/probe/push/CI/lifecycle actions, or peer-session access. This report is sent for verbatim persistence as review-native-discovery.md. Review itself grants no integration, deployment, package selection or session lifecycle permission.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
