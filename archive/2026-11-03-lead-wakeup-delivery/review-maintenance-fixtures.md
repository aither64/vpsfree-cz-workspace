**Important findings**

1. **R1 — The VM reads preparation data that exact-UUID status deliberately omits.** General; architecture/interface; risk/compatibility. At reviewed head `bf4de3da0ed4abcb6e66188ef146d9d34bd59918`, `nix/tests/session-creation.nix:615` reads `operation["preparation"]["candidateCodex"]`. That operation is returned by `maintenance_wait(..., identity)` at607, through the public `maintenance status UUID` helper at405-407. Exact-UUID CLI status dispatches with worker:false (`libexec/workspace-maintenance.rb:56`), and `Controller.Status` explicitly clears Preparation (`portal/internal/maintenance/controller.go:25`); its omitempty field is absent from JSON. The first maintenance_case will therefore fail with a missing-key error at the target barrier instead of exercising continuation/restoration. The earlier no-UUID status uses the different active response, which explains why switch_start's initial preparation assertions do not catch this mismatch.

   Minimal remedy: carry candidateCodex from the already public prepare response through switch_start to the barrier, or compare with the established public activation identity. Retain the exact native executable comparison. Do not expose private preparation in status or read the private journal to fix the fixture. Add a focused control using the actual exact-status projection, which omits preparation; syntax and queue-predicate controls do not cover this seam. Main has accepted R1 and assigned a narrow fixture correction. That uncommitted correction is outside this reviewed head and is not accepted by this report.

2. **R2 — The VM does not establish actual restoration of a stopped managed client.** General/verification; risk/compatibility. `nix/tests/session-creation.nix:458-469` checks native/portal units, restoration.completed and worker exit; the cases at637-657 check continuation receipts, roster and replay. They never establish that a representative managed client was running and was actually stopped, require its exact TerminalIntent, or passively verify that client returned to its retained session after success/recovery. A worker that omits restore_quiesced_sessions while marking restoration complete can satisfy these assertions. `test/README.md:111-116` presents this VM as filling the previously missing actual-client-restoration boundary, so the gap is material to its advertised acceptance purpose.

   Minimal remedy: use one existing managed client in the guest. Record its positive source session/pane/thread identity and ordinary running command, require the operation's matching stopped-client intent, and passively verify ordinary same-session client restoration after successful activation and same-operation recovery. Keep this to the existing client contract; no terminal presentation, child-mail guarantee, production hook or new harness is needed. Main confirms no already-bound actual restoration acceptance or supported-boundary exclusion exists and has accepted R2 for a bounded correction.

No separate Blocking or Advisory finding is raised. These Important findings require correction or an explicit recorded disposition before the fixture is used as acceptance. This report reviews committedbf4 only, not the owner's subsequent working-tree remedies.

**Identity, settings and exact scope**

Capacity was available. I verified `dev-session current` from the exact tracking directory returned `2026-11-03-lead-wakeup-delivery`; both environment markers matched that slug and trusted workspace `/home/aither/workspace/ai/vpsfree.cz`. The live same-session roster showed retained reviewer0, purpose review, ready, thread `01a1a349-5cda-76c0-baf0-cc0765288adf`, saved **gpt-6.1-sol / xhigh / read_only**. No override, fallback or nested reviewer was used.

Repository/worktree: `git@github.com:aither64/dev-workspace.git`, `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/dev-workspace`.

- Head: `bf4de3da0ed4abcb6e66188ef146d9d34bd59918`.
- Tree: `44dbafb172ea669c02725c2872a4ceb78a76f9a7`.
- Parent: `38967de7418bbb59d5a699b86d21d58729220a65`.
- Affected range: `293d4cc915f7fde492b28b403855261cb7e507e6..bf4de3da0ed4abcb6e66188ef146d9d34bd59918`: four paths, +453/-7.
- Owning maintenance range: `38967de7418bbb59d5a699b86d21d58729220a65..bf4de3da0ed4abcb6e66188ef146d9d34bd59918`: 57 paths, +9051/-68.
- Complete range: `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7..bf4de3da0ed4abcb6e66188ef146d9d34bd59918`: five commits, 98 paths, +17352/-151.

I read the current packet through its Historical packet boundary, current plan/state and sufficient design3177+ including the router correction. Repository/workspace procedures and the mandatory-change-review skill with all four references were applied; unchanged guidance already read in this context was reused. I inspected the actual four-file diff, relevant fixture/model/SDK/public host interfaces, documentation, complete series and supplied evidence. Initial source was clean; after main authorized the owner's R1 edits I used committed blobs for source identity. The head/tree/parent remained exact at final inspection. I make no final clean-working-tree claim about concurrent uncommitted remediation.

Unchanged production conclusions and main's recorded step9 R1/R2/R3 closure at ea8774d6 are reused only within their unchanged boundaries. Actual ea877..293d changes only the native fixture, and293d..bf4 changes only the four assigned test/doc paths. This review does not reopen or independently re-certify those production fixes.

**All four affected lanes**

General: The Go predicate correctly refuses an empty queue without positive persisted input evidence. It accepts either the exact original row ID/client ID/text or a passive destination userMessage with the same client ID/text and nonempty item/turn identity. The actual pinned SDK maps clientId into TranscriptEntry and uses the same queued-or-started identity distinction. The VM predicate additionally refuses duplicate queued/consumed witnesses and validates canonical text. Neither predicate treats absence, nil errors or native exit0 as preservation. Original five native modes, case/grace limits and goal/resume/replay checks remain. I independently confirmed the original creation-case block remains byte-for-byte intact.

The VM calls the public prepare/switch/status/recover paths and real user systemd worker/profile machinery. Immutable packages use the same native/SDK with supported capacity4/5 registration differences; preparation checks that native paths match and plan digests differ. It does not seed maintenance journals or forge native receipts. Failure injection is limited to the guest native unit; no-resume is checked before same-UUID recovery, followed by per-participant client-ID evidence and completed-operation replay. The two findings above are the remaining concrete problems found in this source.

Architecture/repetition: This extends the existing session-creation fixture and its existing Responses model/transport helper. The added transport action is allowlisted to queue/goal RPCs and forwards real responses. No new production interface, controller, VM harness, protocol dispatcher or generalized fault framework is introduced. The Go and Python predicates operate at different existing boundaries (SDK-normalized versus raw wire data); their small explicit duplication does not justify a cross-language abstraction. R1 is a real public/private response-boundary mismatch and can be corrected in the fixture without expanding the API.

Scope/proportionality: I compared the latest user contract with this affected +453/-7 test/doc delta and the complete branch. The additions address the actual earlier empty-queue assertion failure and the real worker/systemd/profile coverage removed with the strict protocol. They reuse existing fixtures and do not restore MCP acknowledgement, exact completion-history/native-accounting proof, transient-mail preservation or automatic child restart. Reading a bounded native userMessage to prove one queued input is preserved does not introduce new production history authority. The remaining full-branch size is material, but no additional speculative subsystem is introduced by this package. The R2 correction should remain one representative ordinary client check rather than a presentation-proof system.

Risk/compatibility: HIGH is appropriate for acceptance covering interruption, persisted recovery and profile activation. The router-only barrier is consistent with actual configure_user_services ordering: the already-active router survives enable --now, target native starts and consumes its grant, then synchronous router try-restart holds activation before completion/continuation. The fixture checks the unchanged initial router state, entered PID/invocation, replacement router invocation, target native active/ControlPID0/executable/socket identity, source disappearance, selected profile and held portals. Native ExecStartPost would interfere with grant admission; it is absent. The helper has a60-second bound and checks a40-second inspection budget, with fixture-owned cleanup. Stop is sent while the source portal still runs and another participant is held, not through a resurrected source portal at the target barrier.

The guest policy explicitly has no profile machine resource, so this VM is not real claim-path acceptance. Accepted composed R3 tests and actual rollout obligations remain separate. The same is true of final W/C consumer selection and host-first/profile-second deployment. This fixture review grants none of those operations.

**Complete history, streams and migration/state lineage**

The actual complete series is:

1. `e18a1e8de4d599df830e6ac390c9ab306d23d891` — isolated tracking-admission deadline fixture.
2. `58e87f9d3ccc1aac262b29f587a1d0553257a554` — durable idle-lead wakeup delivery.
3. `f161ede8a6ea4cf540edcb7ece81ebb76f064a05` — archive hydration diagnostic.
4. `38967de7418bbb59d5a699b86d21d58729220a65` — one SDK selection.
5. `bf4de3da0ed4abcb6e66188ef146d9d34bd59918` — final bounded maintenance with its supporting tests/docs.

The first four commits are unchanged. Fixture corrections are consolidated into the owning unmerged maintenance commit. It introduces the final bounded protocol directly; superseded strict designs, prototypes and follow-up fixup commits are absent from current ancestry. The retained failed293d ref resolves exactly to293d; it is provenance, not current acceptance or literal merged ancestry. No obsolete branch history requiring further consolidation was found.

**No redundant repeated input/dependency/channel update stream remains.** There is one SDK stream to `c3c2adb705f5ff6bb42c98bd44be3649fd93bedb`. All five supplied input guards match the committed source; actual lock comparison with3bb changes only the codex-web node. The prior18→9 pruning and16 retained production semantic paths belong to unchanged38967. The native0.165/catalog/model inputs and vendor selection are unchanged by this amendment. The VM's two capacity variants are fixture packages, not additional dependency pins. W/C still select earlierf161 and do not establish current composition acceptance.

**No database migrations or seeds.** This four-file change alters no production state format, public/control API, SDK/native protocol or descriptor. The complete branch still introduces private maintenance schema2 directly, with no transitional migration or schema1 conversion. Historical schema1 stays routed to its immutable SourcePackage before semantic decoding, preserving old operation bytes and owner semantics. Existing public/session/monitor/submission/claim formats retain their contracts. Historical donor external consumption remains unproved; no global absence claim or private-state inspection is used to justify removing compatibility. No unsupported reader removal or obsolete transitional migration was found.

**Evidence and remaining acceptance limits**

I independently matched packet SHA256 `ac528b32db01dfee7a8638020f123fb995f3c368cea6c118264b41aed443c537`, all four committed source hashes, five unchanged input hashes, all three full-index/no-renames patches and their counts against actual Git, first-four ancestry, retained293d ref and the named receipt/log/artifact hash pairs. I read the actual focused result logs and source-check scripts.

B's twelve local predicate cases passed0.065s; the correct live_switch_integration command compiled0.047s with **no tests run**. D's final raw predicate controls passed2positive/17negative cases, and syntax/original-case-preservation controls passed. Existing registration/capacity tests passed0.020s. These are local/static/focused results, not native/VM acceptance. The logs preserve precommit dirty-tree/system-rename warnings. D's declaration/derivation projection is an **unbuilt prior snapshot**, not finalbf4 artifact identity.

The ea877 setup failure and293d empty-destination-queue failure remain failures. The latter proves neither actual loss nor actual consumption because the original positive payload/history was not retained. The archived invocation's Nix-path failure occurred before Go/native and is distinct. Teardown exit0 and removed fixture roots do not establish persistence or acceptance.

No new native or VM execution, package build, full suite, exact-final graph/CI or live/profile acceptance exists forbf4. The local native fixture still injects activation; the VM has not run and currently contains R1/R2. Final artifact/source/input binding, native cases, corrected real-worker VM acceptance, applicable final composition/full checks and independent wakeup acceptance remain outstanding. Earlier successes and prior projected derivations cannot be transferred automatically.

I performed no file/source writes, tests, evaluation/build, native/VM/model/browser/host execution, Git mutation/publication, CI, claims, profile/deployment/lifecycle operation or peer/private-state inspection. This report grants no execution, publication, activation, integration or lifecycle permission.

**Capacity returned.** This exact committed-bf4 affected final review is complete. No follow-up review or implementation has been started; main owns finding disposition, persistence and later execution. The session remains open.

Session portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
