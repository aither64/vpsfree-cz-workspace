# Run3 verification-contract corrections: affected independent final review

## Findings and disposition

No Blocking, Important or Advisory findings in the final A c1f415ad/B d819ad04 deliverables. The affected general, architecture and risk/compatibility review is complete. These exact source units and the inspected prepared command are suitable for the planned disposable native4 verification phase.

This is not a native pass, final C/composition approval, packaged-build result, deployment/live-use certification or integration permission. Prior B1/I1/I2/I3 resolutions, unchanged A production/optional-UI conclusions and the original scope conclusion are retained. The changed certification behavior was independently assessed; it was not accepted by an equivalence shortcut.

## Reviewer, scope and exact identities

Same retained reviewer0, gpt-6.1-sol/xhigh/read_only, independently verified ready/review-purpose in the live same-session roster. No setting override or fallback. From the bound tracking directory, dev-session current printed 2026-10-22-codex-thread-retries; both DEV_SESSION markers were absent and the trusted thread/workspace binding matched. Mandatory review skill and full general/architecture/risk references, workspace/repository AGENTS and applicable procedures were read. HIGH risk: protocol and concurrent admission certification.

I read the updated review-run3-packet.md in full, including the replacement after hold; accepted architect run3 disposition, native-verification.md, prior reports, actual changed source, supporting production paths, inventories/range comparisons, quick receipts and original failed evidence. I remained read-only: no tests/native execution, builds, source or session-file edits, nested agents, claims, deployment, merge or lifecycle actions.

| Repository | Base | Final reviewed head | Final tree |
| --- | --- | --- | --- |
| codex-web | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 | c1f415ad5602c23e6443cced73cb59267a796f05 | 7e3523236dc4500b68a008398305b2290beabcc8 |
| dev-workspace | bf6d4b0c49600c15e17fe71248807ef43424e932 | d819ad044ef7fcc7bb4a111dc7676fe251383249 | 6f1f05da60b09743d3716eb1a0adf794b90cf5a3 |

HEADs, trees, clean status, merge bases and complete series independently matched. Fresh SSH remote reads confirmed both published feature heads and defaults still at their stated bases.

## A: exact native behavior and receipt reconciliation

Commit c1f415ad, codex/continuation_integration_test.go:80 and :251: the bounded helper calls only ReconcileSendWithOptions with the original thread/text/UUID/action/options. It polls only UnknownSendOutcomeError. Absent attempts and non-unknown mismatches terminate; no new UUID, send, resume or settings write exists in the loop. The focused fixtures cover delayed history, wrong text, absent attempt and context expiry retaining submitting state. Inspection of the real reconciliation implementation confirms this is observation of an existing immutable attempt, not another dispatch.

At :742, the native lost-reply case now independently requires the proxy to have dropped exactly one successful nonempty native turn receipt and counted one turn/start. Recreated-client reconciliation must recover that exact turn and client ID; the same-ID ContinueFailedTurn call must then return the identical cached receipt. Actual execution settings, one original failed input, one exact continuation input and one provider request remain asserted. Acceptance preceding history visibility is source-supported: pinned Core turn_input.rs:1 explicitly replies before rollout persistence/sampling.

At :819, the direct-native race establishes the exact active manual regular turn before forwarding the racing continuation request that passed its final preflight. It requires successful RPC, equal nonempty turn IDs, that same latest turn inProgress and one held provider request. After release it requires both exact input IDs/texts once in that same completed turn, preserved original failed input, exactly two native turns and unchanged original error code/message. Refusal, replacement, interruption or arbitrary alternate success cannot pass. Final provider count is logged separately from the held-point count.

I independently checked pinned rust-v0.163.0 turn_processor.rs:661 (Started and Steered both yield an inProgress reply), codex_thread.rs:412 and turn_input.rs:373/:813. The public start path can steer regular active work without an expected-turn condition; persistent settings apply to Started and Steered. The revised assertion matches the accepted source-backed boundary and the original run3 observation. It diagnoses the unmanaged limitation; it does not certify managed exclusion. No public CAS, native patch, normalization, policy override, dummy turn or product fallback was introduced.

All six native retry cases remain. Default/plan settings, exact cyber terminal, native queue execution context, retained partial command/history and deterministic side-effect assertions remain intact. The production preflights, exact error allowlist, queue/prompt/ledger checks and cold/current-turn refusals are unchanged from the prior review.

## B: production-path contention and secure fixture setup

Commit aafaf419, portal/internal/workspacecodex/turn_retry_contention_test.go:140: twelve root/member x send/queue x manual/automatic/unknown cases use actual managed SendWithOptions or QueueWithPolicy against real Controller.Step, backend and A continuation. Independent clients have separate connections and local queue locks; they share the real durable admission/ledger paths. Store.Lock uses the per-thread flock. The native receipt barriers wait outside the fake native-state mutex (:113), so fixture serialization cannot provide the asserted exclusion.

The source task obtains settings authority through real explicit activation and managed queue admission, including inherited role/common instructions, access and MCP. Scheduling uses exact native-style context/history. Manual admission winning the fence must cancel/supersede pending work with zero automatic start/steer. Automatic ownership excludes all competing manual native mutations through receipt handling; the fixture checks that the durable automatic receipt exists before later manual mutations. The same waiting manual operation then follows normal steer/queue behavior.

The unknown branch retains a real schema3 submitting ledger entry created by the generic writer, exact pending UUID/action/content and unchanged Pending through the manual hold. It exposes exact history only for reconciliation, persists the accepted result before unlocking and permits ordinary manual input afterward. No manufactured accepted ledger state substitutes for the writer. Existing cross-process and roster/resolver tests remain; the new composed regression supplements those primitive/outer-boundary checks.

At portal/cmd/workspace-portal/turn_retry_native_proxy_test.go:225, HTTPS, a private 0600 transition.lock and an absent private provider-catalog path satisfy fixture prerequisites without relaxing production origin, lock or provider checks. TestNativeRetryPortalSecureSetup calls the actual constructor and closes it. Production server validation still requires HTTPS. The retained native fixture continues to demand genuine accepted-start proof, exact schema3 uncertainty, recreated-client/real resolver recovery, one continuation and opt-out prevention. Constructor success alone does not establish those later native assertions; native4 must execute them.

## Added browser synchronization integrity

Commit aafaf419, portal/internal/web/attention_browser_test.cjs:1611: the only b695-to-d819 source delta is this test (+7/-5). Independent excluded-path comparison is empty. The test installs the deferred release callback and then signals stageEntered; it waits for that actual phase before issuing Disable. Both permission and registration stages remain. The two-second test bound and synthetic phase diagnostic replace the finite 100-setImmediate assumption; storage, cross-tab gate, unsubscribe, status and no-register assertions are unchanged. This is a bounded fixture repair, not a notification product change.

The preserved731 fast job119988219484 log records registration-stage release undefined versus expected function, 70/71 browser passes. I verified its SHA256 e6eda7f03d1ae461139e2b2552250262b092b0d80433b13c31e097a1172fc2cf. Metadata shows archive/creation passed and host skipped. Source explains why a finite event-loop spin need not establish completion, but the old evidence does not empirically identify WebCrypto latency as the cause. The packet correctly avoids that stronger claim.

Owner receipts show syntax success, exact case1/1 and full file71/71, zero skips. Go/production/pin files are identical to b695, whose Go race/compile receipts apply to that unchanged Go source. This does not establish exact Nix derivation reuse or final-head full CI success.

## Prepared native command

Reviewed session native-final-command.sh, SHA256 d81583688d251d52d7d90e4df24b08b8605d1fb037a644785ce2819cfbab448a, unrun. It checks session/optional environment binding, validates supplied full head arguments, records and rejects dirty/mismatched source, and uses a new evidence-directory mkdir as its once guard. It neither retries nor overwrites an existing evidence batch.

The library command runs from A; runtime runs from B/portal. Both use the final B shell, explicit -mod=readonly, exact required top-level selectors, count1/json/five-minute bounds and the matching native environment variable. Separate cwd, full stdout JSONL, stderr, command/test exit and monotonic elapsed receipts are retained for both operations; a failed first operation is not replaced by the second result.

Both immutable native paths and full hashes match the brief. I independently hashed the wrapper and underlying binary without executing them:
- wrapper dd356114c45b6b78617be9da9c21ab6d284a8d3c7de1e5a39abf45be2cabed8b;
- underlying 5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5.

Lead must supply literal reviewed c1f/d819 arguments and keep them frozen. The watcher still must assess every required named PASS and absence of selected skip/fail/missing events; wrapper exit zero alone is not the native evidence gate.

## Complete history, update streams and migrations

The complete A series is:
1. df00fa36c820fc7a62ee5b8dd6e1745940ff8e15 client/context/predicate/docs.
2. 6c828759440705c632e1902fa8309ccac446b050 optional HTTP/UI.
3. c1f415ad5602c23e6443cced73cb59267a796f05 native fixture.

The complete B series is:
1. 7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99 durable core.
2. b3c7187c6e26e269994433716a0ee719d0a7edf7 package capability.
3. aafaf4195d695c4641ce4f9342d56a1786f237c3 runtime and supporting verification/docs.
4. d819ad044ef7fcc7bb4a111dc7676fe251383249 sole final A pin.

Complete base-to-head series/final diffs were assessed with the earlier full review and current full deltas/range comparisons. A differs from665 only in native tests/reference docs; B differs from731 only in tests/docs and the five coordinated pin files. Core/capability are exact unchanged commits. Optional UI stable patch ID remains4f906eb1dd62001465e5419ac67d8f97b8af592a. B b695/d819 final pin patch IDs both equal086b095cf727736a15b0a9b36618f46da5bdaec9.

Corrections are folded into their owning unmerged commits; the small notification-fixture synchronization repair remains test-only support as explicitly assigned. The logical split is adequate. No obsolete unmerged implementation, fixup/transitional commit, abandoned compatibility shim or superseded pin remains in these final A/B series. Original reviewed/failed ranges and bundles remain evidence, not intervening feature commits.

A has no dependency-update stream. B's single codex-web stream is consolidated once to c1f across Nix source/lock, Go module/sums and vendor hash. I independently compared lock JSON: only codex-web changes, all input edges unchanged. The selected pseudo-version is v0.0.0-20261022181203-c1f415ad5602; vendor hash is sha256-CUZc7zj3bNr75y+7Rv3mPjEtVLT+iUNaLQ7EOH7RkQE=. No separate supported release/consumer/state boundary requires old iteration pins.

No migrations: no database migration, retry-state conversion or transitional format. Direct final private retry schema1/capability1, required nonzero epochs/UUID-keyed charges and existing submission schema3 remain unchanged. Provenance is unmerged, unreleased, undeployed, with no external retry-state predecessor/consumer; disposable failed native fixtures do not create a supported migration lineage.

## Consumers, documentation and residual verification

A owns native protocol observations/continuation and exact execution context; B remains its concrete managed controller consumer through imports/wrappers and the matching Go/Nix pin. Provider ownership and consumer integration are unchanged. Source-unit private native verification is valid independently of the pending mechanical C refresh.

A docs/reference.md and B docs/workspace-portal.md correctly explain delayed immutable reconciliation, implicit native steering/settings, receipt-path meaning and managed admission/uncertainty. B docs/turn-retry-recovery.md preserves exact authority/epoch, cancellation/quota and forward-package recovery constraints. README links make owning explanations discoverable. Lasting behavior belongs with those projects; per-run source identities, failed evidence and prepared execution stay in session records. Placement and adequacy are acceptable; documentation makes no native/deployment success claim.

Owner quick evidence inspected: A focused races8.554s and reconciliation races1.283s; B runtime21.646s/core4.836s/resolver6.892s/secure fixture1.225s; both native top-level names compiled/listed; final Node checks above. I ran none of these tests myself.

Original A665 run3 has four passing retry subcases but failed lost-reply/direct-native cases and the overall package. Corrected-CWD B731 run3b reconnect passed; controller reached genuine acceptance/completion then failed HTTPS construction, before resolver/opt-out proof. Those are scoped historical observations, not current-head passes. Exact-head native4 with complete named-case evidence remains required.

C/W remain explicitly held at W06ea83416387ebb16ecbb91acbf079cfdda1500b/C01634abe06fc618fd3d55fea1df455dbe574cbf0 selecting old3f/A b6. This report gives them no stale approval. After native A/B success, each downstream stream still needs its single consolidated final pin and complete input-graph/history inspection, followed by package/full-composition/build/deployment gates.

Disposition: affected FINAL source review complete with no findings; proceed to the separately authorized native4 verification workflow for A c1f/B d819. Preserve this and prior reports and retain the same reviewer for material protocol/authority follow-ups. No deployment, integration, resource or lifecycle action is authorized by this report.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
