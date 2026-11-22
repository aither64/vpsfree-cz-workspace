# Structured communication presentation findings

## P2 implementation handoff, 2026-11-20

Committed `c01815dfab007a61ba884f5bb0d92ad39f0d676e` directly on literal deployed base `25b679656bbd63d8e13406f0e2bcaec45bfa1d89` in registered `2026-11-11-pi-codex-migration-portal-communication-presentation` / `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace-portal-communication-presentation`. One new purpose commit; inherited R25b/Cb302 lineage is referenced, unchanged. Exact six files and clean/index-empty/current-equals-committed proof are in [p2-commit-receipt.json](p2-commit-receipt.json).

The shared history reader now works without optional settings controls. It freezes the page's lead selection/scope, keeps existing scoped headers/no-store visibility bounds, aborts hidden/leaving reads and drops stale responses. Both presenters reuse one anchored colon/period classifier, preserve preexisting metadata and canonical input bytes, and keep labels as presentation only. Existing app merge/filter/from-to rendering remains unchanged. `app.js`, templates, domain records, C/worker, delivery/receipts and pins are unchanged. The temporary cache-token edit was removed: the server already applies no-store to static responses. Main's direct writing pass supplied the committed narrow `docs/session-communication.md` copy; visible JS strings are reused.

Verification used the declared exact-baseline shell, `nix develop path:/nix/store/wf6yazj31l9bh9lzzlzl5qxv3ms13hf0-source --offline --no-write-lock-file --command ...`:

- First finite batch: Node syntax for communication.js and the existing composer fixture; five Go controls passed: `TestCommunicationPortalApprovalAndRevocationFromEitherSide`, `TestCommunicationTranscriptProjection`, `TestCommunicationPresenterPreservesExistingMetadata`, `TestComposerHandoffRetainsOriginalIntent`, `TestPiTranscriptUsesSharedSanitizedMarkdownForFullPageAndLive`. [Batch log](p2-focused-check.log); watcher Luna/low, installed gh680 catalog780db421 / native utility configdw_32fc0df1. The new composition test initially failed because its seed omitted the store lock file.
- Final affected command: `node --check portal/internal/web/composer_handoff_contract_test.cjs`, then `go -C portal test -mod=readonly ./internal/web -run "^TestCommunicationPresentationComposition$" -count=1 -v`: PASS1.360s. [Passing log](p2-composition-scoped.log). Actual rendered Pi/Codex markup plus scoped HTTP responses feed the shipped loader event, merge/filter and appendMessage labels. Covers incoming/outgoing mixed and same-backend rows, canonical IDs/digests, escaping, chronology, duplicate/reload/older-page/status behavior, member exclusion, failures and late scope/member/hidden/pagehide completion; retained store hash and native effect/read counters unchanged.
- Two intervening fixture-only failures are retained in [recheck](p2-composition-recheck.log) and [composition-final](p2-composition-final.log): the minimal VM element lacked dataset, then the Codex render fixture omitted the actual page's pure ObservationIdentity projection. Both fixtures were completed; production guards/assertions were preserved. Only this affected case was repeated. Production bytes were unchanged after the initial batch.
- gofmt and staged/current whitespace checks passed. Ordinary declared-Nix `git commit -F` used the temporary message file; no declared hook framework or active executable hooks, no bypass. All operation-owned tool sessions/format/test/watcher/commit effects are terminal.

No migrations, persisted-format changes, repeated pin streams, publication, integration, deployment or live/native messaging. Current package is ready for lead acceptance and committed affected independent review, then separately authorized composition/delivery. Exact reported live Codex missing-label symptom remains unconfirmed; the repaired actual-template→HTTP→event→shared-render path proves both saved labels without invented sender names. Capacity available, permanent fixes retained.

Owning documentation: session-communication.md remains the member how-to/reference for grants, display and delivery; current execution evidence stays here. The original source-only diagnosis follows.

Investigation complete; source-only, 2026-11-20. Owner: implementer4. Prior A1/frontend packages are accepted; permanent fixes retained. No application edits, tests, builds, native sends, package selection, peer-session operations, or live log/transcript reads were performed.

Selected target supplied by lead: gh680l33, R `25b679656bbd63d8e13406f0e2bcaec45bfa1d89`; inspected immutable source `/nix/store/wf6yazj31l9bh9lzzlzl5qxv3ms13hf0-source`. No f4/source3 updater content used. Own session/current and retained roster68 verified; Sol/xhigh/workspace_write preserved.

## Confirmed causes

1. **Pi never starts the retained communication display reader.** `portal/internal/web/templates/session.html:94` and `:145` restrict the Communication settings tab and `#communication` panel to Codex, while the shared Sessions transcript filter exists for Pi (`:163`). `portal/internal/web/static/communication.js:4-5` immediately returns without that panel. Consequently no GET or `session-communication-updated` display event occurs on a real Pi page. The app's ledger-based merge cannot render outgoing CLI messages, clean incoming envelopes, or provide session labels/status. This is a composition failure; the communication HTTP service already supports typed Pi endpoints (`portal/internal/web/communication.go:76-129`).

2. **Pi's native-history presenter classifies team messages but omits session messages.** `portal/internal/web/pi_workflows.go:1642-1661` recognizes only `teamEnvelopePattern`. `portal/internal/piruntime/adapter.go:286-287` projects a user input as ordinary `userMessage`; `transcript_snapshot.go:48-60` enriches original input identity without classifying it. With no ledger reader, a received cross-session envelope remains visible in Messages, rather than Sessions. Shared UI behavior is already driven by `entry.communication.kind`; no backend-specific filter is needed (`static/app.js:669-689`).

3. **The Codex fallback classifier does not cover the mixed-backend envelope actually generated by the owner.** Legacy Codex-only `communication/service.go:212` uses a colon after `(message ID)`. Any exchange involving Pi uses a period (`communication/authorization_context.go:76-86`). `web/server.go:4301` accepts only the colon form. Therefore mixed traffic lacks fallback session metadata/from/to when the retained projection has not loaded or cannot be read. The browser's ledger deduper already accepts either punctuation (`static/app.js:655`). Preserve both forms for retained history; do not rewrite envelopes or receipt digests.

## Labels: established behavior and limit

The current typed endpoint DTO is already sufficient: Codex has `{slug,thread,incarnation}`, Pi has `{backend,session:{workspace,slug,incarnation},leadIncarnation,nativeId}` (`communication/service.go:20`, `pi_records.go:18-41`). `ReadEndpoint` returns validated exact-endpoint records and strips private delivery tuples, then sorts stably by createdAt (`endpoints.go:163-187`). HTTP adds sanitized message HTML (`web/communication.go:110-117`).

`mergeSessionCommunicationRows` already matches both thread/nativeId and reads both slug/session.slug (`static/app.js:648-667`). Its projected rows contain both from/to, and the renderer emits `Session · from → to` (`:669-674`, `:5707-5710`). Existing mixed-shape helper assertions explicitly check both labels (`web/composer_handoff_contract_test.cjs:818-826`). Thus an endpoint-field/schema mismatch is **not** supported by the inspected source. The exact reported Codex Sessions row without labels is not conclusively reproduced by this source-only pass. A native session tool row can have only `{kind:"session"}` by design (`server.go:4311-4312`), producing the generic label in All; mcpToolCall is excluded from Sessions (`app.js:682`). Do not infer missing names or alter delivery authority to fill it.

No live content was needed for the confirmed Pi and mixed-envelope defects. If the missing-label symptom persists after the bounded repairs, inspect only the affected row kind, communication keys, message ID correlation and loader status after the required sensitivity check; do not copy payload/envelope content into tracked records.

## Team versus session, both directions

- Incoming Pi team assignment/report uses the established `Team assignment from MEMBER to MEMBER:` envelope (`teamruntime/pi_delivery.go:13-19`); both portal presenters recognize it. It belongs in Team/All, not Sessions/Messages.
- Outgoing Pi `report_to_lead`/`team_message` tool calls/results already carry team metadata (`piruntime/adapter.go:200-210`, `:309`, `:326`). Sender may be absent for a tool row; do not fabricate it. CLI team assignment history is activity unless independently projected.
- Incoming cross-session input is native history with its original accepted-input identity. Classification is presentation only. When a matching retained record is loaded, replace its display with one canonical session row; preserve native paging and input acknowledgement ownership.
- Outgoing cross-session CLI/MCP sends need the retained message projection because a shell/tool call is not the message itself. That same projection handles Pi→Codex, Codex→Pi, Pi→Pi and legacy Codex→Codex without a second store or new SDK extension.

## Smallest implementation boundary for architect acceptance

Use the existing neutral `TranscriptCommunication{kind,from,to}` and typed communication API. No DTO/schema migration, new native tool/extension, receipt/digest change, delivery retry, or backend framework is required by these findings.

1. Make retained communication display loading independent of the optional settings form. Keep one loader for both backends; obtain current selected lead/scope from the existing page carriers. Settings controls may stay optional, or the architect may release the existing shared panel for Pi after confirming that product boundary. Do not add a separate Pi display implementation. Preserve existing scoped headers, generation handling, no-store reads, visibility bounds and member exclusion.
2. Reuse one presentation-only envelope classifier for both `presentTranscript` and `presentPiTranscript`, covering historical colon and current period headers, preserving preexisting metadata and canonical bytes. Classifier output is never identity, grant, authority or send acceptance proof.
3. Retain the existing merge/filter/renderer. Preserve IDs `session-message:ID`, ledger-createdAt ordering, native duplicate suppression by original input ID or recognized envelope ID, and original history cursors. Pending/held→delivered status updates replace the same display row. No optimistic send/replay.

Expected owning source boundary: `web/templates/session.html`, `web/static/communication.js`, the two presenter spans in `web/server.go` and `web/pi_workflows.go` (a tiny shared presentation helper if useful), plus focused existing fixtures. `app.js` should need change only if a fixture proves a consumer defect beyond the missing producer. Coordinate server/template versus frontend ownership through lead; latency owner0 and activity owner1 remain separate.

## Finite regression proposal; not run

- Use the actual rendered Pi and Codex page composition, rather than inventing a Pi `#communication` panel as the current VM helper does. Pi lead Sessions/All must cause one scoped no-store history load even without settings controls; retained-member views must not include lead exchanges.
- A small table covers incoming/outgoing Pi↔Codex, Pi↔Pi, legacy Codex↔Codex; native historical colon/current period envelopes; exact session labels and sanitized payload; Messages/Team/Sessions/All separation and always-visible errors.
- Join an incoming native input plus matching ledger record into exactly one displayed row; leave canonical native text/digest/input ID/history cursor unchanged. Repeat reload, older-page merge and status refresh. Order two records around a native entry and assert stable creation-time order and stable IDs.
- Cover incoming/outgoing team rows separately so session fixes do not reclassify team or ordinary quoted text. Cold/failed ledger reads must still classify actual envelopes; raw user prose mentioning an envelope inside its body remains ordinary.
- Assert the actual Codex mixed row carries both from/to at the HTTP→event→merge→render boundary. A test using only a manually preclassified row does not resolve the reported symptom.

Next action: architect0 accepts the bounded presentation/composition brief and lead allocates implementation. Investigation has no remaining execution; capacity available with presentation/frontend fixes retained.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
