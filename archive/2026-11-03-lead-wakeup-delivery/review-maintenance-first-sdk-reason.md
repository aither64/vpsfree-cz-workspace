# Final affected review: first SDK reason diagnostic

## Findings

No new Blocking, Important or Advisory findings in the completed affected delta. No remediation is requested.

This conclusion covers diagnostic retention and its existing consumer. It does not establish a functional close correction, successful maintenance cutover or native acceptance at the new head.

## Identity, settings and exact scope

- Reviewer: retained independent reviewer0, purpose review, saved gpt-6.1-sol / xhigh / read_only. The same-session roster reports that identity, purpose, settings and ready state. No overrides, fallback or nested agents.
- Session: 2026-11-03-lead-wakeup-delivery; workspace: /home/aither/workspace/ai/vpsfree.cz. Before session records, dev-session current from the exact tracking directory printed the bound slug. Both DEV_SESSION markers were absent, consistent with the trusted thread-bound developer binding.
- Runtime worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/dev-workspace.
- Affected comparison: f168b9d4bc1141dc66c27042dc31e7385dfedbd8..9cf1c7694b3918fcef1b088669ee6241605f071f, four files, +112/-20.
- Final HEAD: 9cf1c7694b3918fcef1b088669ee6241605f071f; tree: 2c71c9b4c15da00f0353c1d31d3b2b8f70ad23b9; direct parent: 3145caa8fcf23b1e825eb54fe9176258f58c6b7f. Actual Git identity and clean worktree/index match the receipt and tested tree.
- Complete owned range: 3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7..9cf1c7694b3918fcef1b088669ee6241605f071f, five commits, 127 paths, +26547/-161. Merge base is exactly 3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7.
- Overall owning subsystem risk remains HIGH. I independently applied general, architecture/repetition, scope/proportionality and risk/compatibility to this affected diagnostic boundary.

I read the mandatory-change-review skill and all four lane references, applicable workspace/session/Git/lifecycle/documentation/verification guidance, repository AGENTS, current top review packet and state, relevant owning documentation, complete affected source/tests, SDK reason producers and existing diagnostic consumer. Unchanged runtime/SDK conclusions and accepted closures are reused only within their unchanged boundaries: full runtime5e68, prior-origin c79, goal-cleared15f, queue/goal139f, main R1–R3 closure0e725 and owner-reason112286. This is not a repeat audit or new acceptance of those implementations.

## General lane: correctness and regression evidence

At this head, portal/internal/web/activity_maintenance.go:31 passes the actual detached event.Reason in the same existing Observation.Apply invocation. The existing boundary mapping, exact normal-close special case, paused-watch refusal and outstanding-request refusal at lines15–30 are unchanged.

portal/internal/maintenance/observation.go:139–147 receives that scalar through an optional trailing internal argument and attaches only its first value to the existing origin. It does not synthesize method, thread, turn or item provenance. The first-origin record remains distinct from the ObservationSnapshot control value.

I independently compared the old/new source: the complete Apply control logic from its local invalidate closure onward, all following Snapshot logic, and the Snapshot wire struct are byte-identical. Production reads of ObserverReason are confined to attaching/bounding the diagnostic; searches find no readiness, admission, cleanup, lease, digest, source, owner or close-policy consumer of it. The web delta is precisely the additional reason argument.

The tests exercise the actual web adapter and reducer rather than a replacement serialization helper:

- activity_maintenance_test.go:91–139 establishes a covered source with a genuine reducer pending-MCP state, delivers each of seven SDK invalid reasons and an empty reason through activityObservationEvent, and requires identical full loss Snapshot values. The first origin remains at invalid gen1/seq5 while the Snapshot reaches seq6; empty original identities stay empty.
- JSON serialization at lines123–130 checks the same value representation used by the fixture, so distinct SDK reasons survive the callback/reducer/serializer chain.
- A later invalid event cannot replace an already retained empty or nonempty first cause. Mutating a detached return cannot replace the stored record.
- observation_test.go:284–326 covers the supplied reason, existing 256-byte UTF-8 bound and truncation indication, detached ObserverReason, generation reset, watch removal/replacement and no inherited reason after reset.
- activity_maintenance_test.go:142–164 preserves clean-only orderly-close annotation and refusal after prior scoped poison. It does not turn a normal-close diagnostic into coverage or wait readiness.

The retained red log fails on all seven nonempty reasons against f168 production, with the same final callback test; the empty case is correctly not a missing-value failure. Final focused green logs pass. This is meaningful evidence for the lost diagnostic, not evidence that native closes are orderly.

## Architecture and repetition lane

Ownership remains appropriate: codex-web owns transport reason production; the web adapter forwards it; maintenance owns one finite reduction per existing watch; the existing fixture consumes the detached diagnostic.

The selected published c3c2 SDK already emits the seven reason constants from client.go:1358–1394 and1463–1484. observer_events.go:44–52 derives normal-close from typed WebSocket close status and otherwise returns read-error. These sources were inspected at the actual pinned module revision and their hashes matched the packet. No new transport decoder, reason-classification registry, observer, subscriber, RPC, dispatcher, hook or cross-project contract is introduced. The reason enumeration is confined to regression examples.

The scalar is stored under the existing Observation.mu in the same event application as its generation, sequence and origin. rememberPrior at observation.go:56–67 still admits only the first record. The existing watch removal and generation replacement end its lifetime; later ordinary events do not rewrite it. PriorOrigin at lines486–495 returns a detached value under that mutex. SDK event callbacks remain the existing ordered synchronous path; this change introduces no asynchronous work or callback under the reducer lock.

The only non-test diagnostic consumer found is the existing fixture observationFields at maintenance_native_integration_test.go:1169–1176, which includes the returned value in firstPriorOrigin. The fixture file is unchanged. Its existing source-close failure branch at lines1543–1551 retains the separateNonAtomicReads label and original failing assertion. No HTTP, MCP, private-control or persisted Snapshot response acquires this field.

## Scope and proportionality lane

The user outcome is automated cooperative activation/continuation, with the separately authorized bounded first migration pause window. The immediate demonstrated obstacle is narrower: actual f168 failure evidence retained an invalid boundary but discarded the SDK's existing reason. Copying that scalar into the existing bounded first origin is a proportionate next diagnostic step; changing close policy without that datum would not be justified.

The production change is one optional diagnostic field, inclusion in the existing bound, same-lock attachment and one adapter argument. Most apparent observation.go churn is alignment of the existing struct; the 77-line callback regression additions are directly tied to this seam and its existing normal-close refusal boundary. No second retained record, frame history, raw error text, generalized diagnostics framework, policy expansion or new native scenario is present.

The nearby first-origin and Apply comments explain purpose, bounds, lifetime and lack of authority. Existing docs/maintenance-mcp.md and docs/workspace-updates.md retain the distinction between lost observation, typed orderly close and independently verified drain/completion. Their README links remain discoverable. No operations-document change is necessary for this internal scalar.

## Risk and compatibility lane

The new ObserverReason shares the existing 256-byte field cap and truncation indication (observation.go:61–65). At the actual current SDK boundary, reasons are fixed local scalar constants, not native message contents, argument payloads, settings or arbitrary error text. Existing identity/status minimization remains unchanged. No extra payload or native read is introduced.

ObservationPriorOrigin gains an optional observerReason JSON member, omitted when empty. This is the existing internal volatile diagnostic value serialized by the fixture, not a public/control schema or persisted checkpoint. Production SDK APIs, module/Nix/native/model/catalog selections, ordinary event classification and existing JSON/SQLite formats are unchanged by the affected delta. Existing callers can omit the trailing argument; current callback and tagged consumer compile evidence is retained.

The reason supplies no coverage, wait readiness, membership, source identity, lease, completed-history or close reconciliation authority. Unknown events, malformed data, prior poison and lost observation still refuse identically. A standalone normal-close retains its preexisting mapping; prior poison is not cleared. There is no fallback from unsuccessful or unknown observation to source exit alone.

The original f168 evidence remains failure evidence: two positive cases reached their one-HUP/structured-drain/host-finish/native-exit0 point, then failed the retained close assertion; three refusal cases passed. First origins were unscoped invalid gen1/seq30 andseq26, followed by loss Snapshots seq31 andseq27. The lack of method/thread/turn identity is genuine absence, not a license to attribute the frame using the enclosing fixture source tuple. The reads are separate/non-atomic. The new scalar has not yet been captured in native execution.

Even a future read-error value would still omit typed error/status details; it would not prove an intentional EOF or authorize an orderly-close policy. A first record with an empty reason remains empty and cannot be upgraded from later evidence. The existing trusted reporting boundary for unreported cells and the previously documented bootstrap/archive limits remain; this diagnostic establishes no global cell quiescence.

## Complete history, consolidation and state lineage

I compared the actual complete series, final diff inventory and current four-file change with the supplied full/affected artifacts. The five current commits are:

1. e18a1e8de4d599df830e6ac390c9ab306d23d891 — independent tracking-directory admission deadline fixture.
2. 58e87f9d3ccc1aac262b29f587a1d0553257a554 — coherent durable monitor capability.
3. f161ede8a6ea4cf540edcb7ece81ebb76f064a05 — adopted passive archive-hydration diagnostic.
4. 3145caa8fcf23b1e825eb54fe9176258f58c6b7f — final maintenance SDK and genuine historical test input.
5. 9cf1c7694b3918fcef1b088669ee6241605f071f — coherent maintenance capability, containing the final diagnostic directly.

The first four commits are unchanged; the final owning capability was amended rather than accumulating diagnostic fixups. f168 is a retained comparison/evidence head, not a required ancestor of the successor. Its exact retained ref resolves correctly. Prior failed/reviewed heads remain provenance, with no claim that their results transfer to this head or that nonancestor revisions were literally merged.

No obsolete unmerged approach or transitional diagnostic implementation remains in the current series. The maintained component split remains coherent within the previously reviewed full-runtime boundary.

No repeated dependency, channel, lockfile or generated-artifact update stream remains. The Go SDK, Nix SDK source and vendor hash select production c3c2 in3145. The genuine original3bb test-only predecessor with SDKd3 is a separate fixture consumer with its own graph, not a second production pin iteration. The final capability's flake.nix/nix/workspace-portal.nix edits add the maintenance check and install its files; they do not change those pins. The current delta changes no dependency input.

No database migrations or seeds are present in the full changed-path inventory. The affected diagnostic adds no on-disk format or state transition. Private maintenance schema1 is introduced directly by its owning capability; no branch-only migration ladder or seed stream remains. Existing public, monitor, submission, services, retry, claim and recovery formats retain their prior reviewed obligations. Donor historical external consumption remains unproved; this review does not assert global absence or inspect private state to infer it. No new persisted-state consumer is introduced by this patch.

Current W/C consumers still pin historical f161. Final consumer pins, composition, artifacts, mixed-version rollout and live admission remain separate gates; their old evidence does not accept the current runtime.

## Evidence inspected and remaining verification limits

Main receipt: /tmp/lead-wakeup-maintenance-main-o26asc9e/first-sdk-reason/committed-first-sdk-reason.json, SHA256 1310b785b7275f53fdb58b22245cc5c66ff86fbd3d5e38b4dca98f74d6534e2f.

B packet: /tmp/lead-wakeup-first-sdk-reason-B-g_4ofb4s/final-B-source.json, SHA256 d5b4fed01cdd7cd9a79d6ef79d29d52680c3f34e4f1f42124bb3df4383064cc6.

I matched both receipt hashes, all five main artifacts, all20 B artifacts, four source/base hashes, twelve frozen inputs, two actual SDK source hashes and two original evidence-packet hashes. Actual Git affected/full diffs match the main artifacts. B's plain unified diff reconstructs exactly from baseline/current bytes; its different headers/order are formatting, not source drift. The fourteen original native artifacts named by the diagnosis also match their hashes.

Read retained logs only:
- Expected red callback regression: package0.053s/exit1, seven missing-reason failures on old production.
- Final canonical observation/activity selector: maintenance0.228s and web1.380s, exit0.
- Tagged live_switch_integration command:0.043s, exit0, NO TESTS TO RUN.
- Module environment: actual portal/go.mod, no GOWORK override, -mod=readonly. The recorded absent provider-catalog fixture setting is explicit.
- Nix dirty-tree/system-rename warnings and ignored eval-cache SQLite-busy warning remain in the original logs. They are not final source drift or native success evidence.

No tests, evaluations, builds, native calls, browser/VM runs, CI, Git mutations, publication, claims, profile/live operations, lifecycle actions or peer/private-state inspection were performed for this review. The complete native/consumer/full-suite/rollout acceptance remains outstanding and separately released by main. This review grants no execution, publication, integration, activation or lifecycle permission.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/)
