# Final component review: maintenance SDK prerequisite

## Findings

### R1 — Important: ConditionalSteer bypasses the receiver's observer write freeze

**Lanes:** general; risk/compatibility; architecture (private transport admission).
**Reviewed head:** `035727457d0ba4c93b6dfb4f0123530cd2518063`.
**Source:** `codex/conditional_steer.go:24–54`, especially the new transport at lines 31–35; `codex/observer_events.go:138–166`; `codex/client.go:1003–1006,1147–1150,1285–1288`; `docs/reference.md:657–668`.

After a successful `FreezeObserverWrites`, calling `ConditionalSteer` with a valid new identity can still create another native connection and issue requests. The method does not use the receiver's request admission: it constructs a fresh client, copying `ObserverOnly` but not the receiver's frozen state. Its ledger reads/preparation also do not check that state. It then calls `conditionalSteerActive` on the new client, which can initialize and send `thread/read` and `thread/turns/list`. Only the later `turn/steer` is rejected by that new client's observer-only mutation restriction.

This does **not** demonstrate an observer successfully steering a turn. It demonstrates a concrete breach of the new public fence: future requests/new connections are supposed to be refused while retaining the same reader, and rejected writes are documented to return `ErrObserverWritesFrozen`. Here the private connection is outside the frozen receiver's writer serialization, and a new prepared ledger entry can also remain until the caller retires it. No actual maintenance-consumer invocation of this path or live cutover failure is claimed.

The current `TestConditionalSteerPreservesObserverOnly` (`codex/conditional_steer_test.go:319–326`) asserts zero steers, so it permits this connection/read traffic and does not cover a frozen receiver.

**Smallest remediation:** reject an observer-only receiver before preparing an attempt or using the private transport; preserve the frozen sentinel through the known-unsent error where applicable. An unconditional observer-only rejection also avoids a race between an entry-only frozen check and a subsequent freeze. Keep the private transport for eligible interactive receivers so reconnect cannot restore their unrelated watches. Add a focused regression that freezes a ready tapped observer, invokes this API, and checks the error identity, no additional connection/RPC and no new prepared attempt. No generic lifetime framework or maintenance policy belongs in this fix.

No other Blocking or Important findings were identified. R1 requires a fix or an explicit recorded decision under the mandatory review workflow before continuing to long checks. A direct narrow fix can be verified under skill step 9 without repeating this entire review.

## Exact review boundary and independence

This is the completed, committed **codex-web SDK component** final review, not an early review of the unfinished runtime consumer.

- Repository: `git@github.com:aither64/codex-web.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/codex-web`.
- Complete range: `d3a29bee90ef00a08816920408c596152339a637..035727457d0ba4c93b6dfb4f0123530cd2518063`.
- Final tree: `def761e1825ed45c4872a2248481119dca0295e4`.
- One direct-parent commit: `codex: add exact-turn notices and retained observer streams`.
- Ten paths, +1832/-15. HEAD, tree, parent and clean worktree/index were checked directly, including at review completion.
- Source packet: `/tmp/lead-wakeup-sdk-maintenance-d3-chesdaya/sdk-source-packet.json`, SHA256 `4976356980c5f549eb9bb36308b8c63189518987e4f90fb2d3454eb85115c484`. I checked the packet's artifact hashes, changed-source hashes and final patch against the actual source.

Before owned records, `dev-session current` from the exact tracking directory printed `2026-11-03-lead-wakeup-delivery`. Both shell markers were absent; the trusted developer binding supplies the matching absolute workspace/session identity.

Review performed directly as retained reviewer0 with the assigned saved `gpt-6.1-sol / xhigh / read_only`; no settings change, fallback or nested reviewer. I read the mandatory skill and all four lane references in full, applicable workspace procedures, SDK AGENTS, the maintenance brief/SDK boundary, current own plan/state, complete series/final diff, source, tests and owning documentation. I ran no tests/builds, native calls, Nix evaluation, browser/VM, Git mutations, publication, CI or live operations, and inspected no peer/private session state.

## Independent scope and architecture assessment

The current user requirement extends beyond the original wake-up feature: future activations need automated cooperative pause/continuation, while only the first migration has a bounded manual pause/resume allowance. SDK transport primitives are a legitimate prerequisite to that requirement. This review does not treat an architect's acceptance as scope authorization or assume reused maintenance source was already reviewed or deployed.

The production surface is bounded: an exact-turn submission primitive and exact discard, detached RPC error data, and an opt-in observer event stream/write fence. Most growth is focused tests. The shared SDK owns transport ordering and durable submission identity; the application retains authorization, terminal disposition, observation reduction, readiness, checkpoints and continuation policy. There is no new scheduler, pause supervisor, automatic replay, reporting2 bridge, native upgrade, or queue-deletion mechanism in this component.

The existing client/ledger machinery is reused rather than reimplemented. A separate never-subscribing transport for conditional input has a concrete purpose: `Ensure` on the receiver could restore unrelated watches and implicitly resume cold work. R1 is a missing admission boundary around that transport, not a reason to remove the isolation or broaden lifecycle policy.

The tap is opt-in only for observer clients, synchronous, detached and bounded. Its serial callback slot and read-loop subscription boundary address a real ordering requirement; a generic event bus, persisted event log or downstream policy catalog would add unnecessary scope. I found no additional harmful repetition requiring extraction.

Actual consumer context was checked in the supplied own runtime checkout: `portal/internal/workspacecodex/client.go` embeds/imports the SDK, `portal/go.mod` still selects d3, and the unfinished maintenance package exposes requester/observation interfaces. The final SDK wiring and published dependency selection are not yet present there. That is an explicit remaining consumer/composition gate, not evidence against reviewing this completed provider independently.

## General and risk/compatibility conclusions

**Conditional submission.** The action context binds canonical cwd, expected turn and caller action; thread/message/text/options remain exact ledger identity. Existing accepted or submitting attempts are reconciled before examining current activity. Passive metadata/current-turn reads precede native `expectedTurnId` admission; no stale-turn fallback, start, resume, queue or settings call is added. Durable claim admission occurs immediately before writing. Explicit no-effect refusals and provably unwritten failures restore prepared state; possible writes, wrong receipts and storage failures remain uncertain unless exact native history establishes acceptance. Missing history never authorizes another dispatch.

The tests exercise both JSON and SQLite, immutable retry identity, shared admission, refusal/discard, cancellation, lost/wrong replies and receipt-storage failure. These are controlled-RPC tests, not proof that the selected native implements every expected refusal or history path.

**Discard/crash boundary.** Exact discard refuses queued, submitting, accepted or changed attempts and is idempotent when absent. The owner must durably save terminal disposition and the complete original identity before discarding and must never dispatch a terminal notice again. A crash between owner save and discard is recovered by repeating that discard. The docs correctly state that SDK and owner storage are not one transaction; the SDK does not manufacture terminal authority.

**Observer ordering and retention.** Detached notification bytes are delivered before ordinary coalescing; successful subscription acknowledgement is marked by the reader before waking its waiter or reading the next frame. Local final retirement and transport events share callback serialization. Generations identify connections, not a native epoch or coverage. Invalid frames, decode failures, loss and typed close annotations cannot create coverage. Consumers must reject malformed relevant data, overflow and stale-generation authority themselves.

Ordinary freeze admission checks the exact ready connection, pending RPCs and the shared writer lock; later ordinary writes/restoration are fenced while the same reader/control handling remains. Caller-owned polling/subscription work must first be stopped and joined, and the activity recorder must be closed separately. R1 is the exception identified above. I found no separate lock-order or event-copy defect in the inspected supported callback contract.

**Compatibility.** The surrounding shared client changes were inspected, not inferred safe merely because monitor methods are unchanged. The nine listed existing send/prepare/discard/reconcile method bodies remain unchanged, as do `send_delivery.go`, submission database/migration/lock behavior and selected Go/Nix dependency files. Structured RPC error data is copied at decode and access; callers must validate its shape and it grants no retry authority. Existing clients without the tap preserve their prior behavior; interactive clients ignore it.

No new native, SDK dependency, catalog, model or execution-policy selection occurs. The tagged native fixture expectation changes only from 0.164 to the already selected 0.165; it supplies no native acceptance by compilation alone. The API promises exact active-turn targeting, not an independently enforced regular-turn classification.

Owning contracts are discoverable through README links to `docs/reference.md` and `docs/submission-storage.md`. They explain submission uncertainty, owner-before-discard recovery, observer ordering/loss, callback restrictions, recorder ownership and the lack of readiness/continuation authority. Their fence statement needs the R1 correction in implementation, not a silent weakening to accommodate the bypass.

## Complete history, consolidation and migration/state lineage

I inspected the **entire** d3-to-035 series and final diff. It is one coherent prerequisite API commit with supporting tests, protocol corpus and owning docs. Conditional notice identity, structured refusal data and ordered retained observation jointly serve the current cooperative maintenance consumer; no unrelated baseline fix or dependency update is bundled.

The supplied donor range `f6f4a187509b3bebfc81585c535be856eaab0d04..b193883a5ea6694231cece42f78e05d29e2c31b0` comprises the three named reuse commits c91d89e, 786a391 and b193883. The final branch composes their additive source onto current public d3; it does not select the old donor tree wholesale. The five listed new API/unit files are byte-identical to the donor. The bounded integration-version/documentation adaptations and shared client composition retain current d3 obligations. This is source reuse, not a claim that donor history was literally merged or previously accepted.

**Obsolete history:** no obsolete prototype, fixup stream, superseded approach or transitional compatibility implementation remains in the reviewed one-commit branch. Donor/old rollout provenance is separate from the final series.

**Repeated update streams:** none. There is no dependency/channel/input/pin/generated-update stream to consolidate. The five added protocol corpus lines describe requests used by the new primitive; they are not a dependency update.

**Migrations:** **no DB migrations or seeds**. JSON schema 3, SQLite schema 1, import journals/fences and predecessor recovery rules are unchanged. The conditional action uses the existing opaque context field with a versioned identity string; it introduces no database/checkpoint schema or conversion step. Observer events and frozen-client state are volatile. No supported persisted format or recovery path was removed.

The packet records no current publication/live consumption of this component. Historical donor consumption is unproved; I make no global absence claim and did not inspect private state. Compatibility rests on preserving existing formats and contracts, not on assuming nobody used the donor.

## Verification evidence and remaining acceptance

I read the original quick logs and bound them to the source receipt/current hashes:

- Focused new API plus monitor/storage-control tests: exit 0, 2.361 s.
- Protocol corpus `--coverage-only`: exit 0.
- Tagged `codex_integration -run '^$'`: exit 0, 0.013 s, explicitly **compile only**.
- Formatting and whitespace checks: recorded exit 0.

Precommit dirty-tree warnings and Nix's ignored cache-busy warning remain in the original evidence. They are not presented as product failures, native success or a test retry. Review-time Git state is clean.

No real native, live maintenance, packaged suite or long integration acceptance was executed for this SDK head. Remaining checks must establish actual selected-native exact-turn refusal/correlation, uncertainty reconciliation and retained-stream behavior, then the completed runtime consumer's admission, cutover, recovery and continuation semantics on its final published dependency graph. Old monitor/runtime/composition successes do not transfer automatically.

**Disposition:** final SDK component review complete with R1 Important pending disposition. No unfinished-runtime acceptance, whole-package equivalence, publication, deployment, integration, claim, activation or lifecycle permission is granted by this report.

Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
