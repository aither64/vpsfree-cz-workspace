# Final review: maintenance runtime component and actual SDK consumer

## Findings

All findings below refer to runtime head **fa7ede4234a8cdc99be5f39fdd058c5c3e97d345**. These are source-backed findings; I did not execute reproductions.

### R1 — Important: worker revalidates claim and preparation only after draining the source

**Lanes:** risk/compatibility; general; architecture/repetition.
**Sources:** `libexec/workspace-maintenance.rb:198–207,258–298,314–319`; `libexec/workspace-host:720–743,3550–3561`; `libexec/workspace-coordination-host.rb:488–527`.

The initial entry checks the source/token and machine claim before creating the operation. The worker then waits for readiness without package exclusion, potentially indefinitely. When it reacquires exclusion at line 271, it checks the profile token and lifecycle admission, but does not repeat the machine-claim or prepared source/registry/registration checks before draining portals, quiescing terminals and issuing the native drain.

Those checks still exist in `activate_candidate`, but the maintenance worker calls it only after successful source exit and release of the retained portal. Thus an operation whose claim is no longer valid, or whose prepared source identity changed during the wait, can stop the source and only then discover it cannot activate. `with_transition_lock` is a flock; it does not itself refresh this authority. This regresses the ordinary activation ordering, which validates these conditions before its drain.

The current stale-source/claim test (`test/workspace_host/maintenance_test.rb:56–73`) covers initial operation creation, not invalidation while `await-ready` is in progress.

**Minimal remedy:** reuse the ordinary claim and prepared-input preflight under the reacquired transition lock **before** writer drain/terminal quiescence/HUP. Retain the later activation/completion checks too. Preserve exact original claim identity and admitted forward/source-recovery semantics; do not acquire replacement authority or relax recovery to make a stale operation proceed. A focused worker test should invalidate the claim or source during its readiness wait and prove no writer drain, terminal quiescence, HUP or selection occurs afterward. Factor only the validation needed to avoid duplicating the ordinary preflight.

### R2 — Important: maintenance holds answers to existing prompts, blocking ordinary source completion

**Lanes:** general; risk/compatibility; scope.
**Sources:** `portal/internal/web/server.go:773–777,3860–3863`; `portal/internal/web/activity_maintenance.go:28–30`; actual pinned SDK `conversation/handler.go:299–300,907–959`.

The outer HTTP maintenance gate rejects every non-GET/HEAD request except cancellation and interrupt. The conversation resolver independently rejects every mutation except interrupt. Consequently an ordinary token-bound `respond` request for an already-pending approval or user-input prompt is refused while maintenance is active.

An affected source turn cannot reach natural idle through its normal answer/completion path. The observer deliberately invalidates cooperative coverage for outstanding server requests, so the controller must wait for natural completion in this case; blocking the answer makes maintenance itself prevent that completion. Cancel or Stop remains possible, but neither preserves the supported normal prompt-completion path.

**Minimal remedy:** allow the existing, exact prompt-response operation through both maintenance gates while preserving the existing origin, authorization, prompt-token/generation and current-thread checks. Keep new messages, activation, queue dispatch, settings changes and unrelated mutations held. Add a regression with a prompt that predates maintenance: its valid answer must reach the existing responder, a stale/foreign answer must still fail, and new-work admissions must remain held. No new prompt protocol or broad mutation exemption is needed.

### R3 — Important: startup grants and reconciliation disagree for registered units that began inactive

**Lanes:** general; architecture; risk/compatibility.
**Sources:** `libexec/workspace-maintenance.rb:105–108,172–175`; `libexec/workspace-host:1492–1501`; `portal/cmd/workspace-portal/maintenance_startup.go:159–170`; `portal/internal/maintenance/startup.go:105–112`.

Operation creation omits a registered native service when it is inactive/failed with MainPID zero. Startup authorization, however, creates grants for every registered plan, and ordinary target activation enables/starts every registered native unit.

When such an omitted unit consumes its grant, `reconcileStartup` looks up its workspace in the operation's source-service list and fails with `startup service tuple changed`. Its grant cannot become ready, and startup completion requires every grant to be ready. This leaves the selected target/startup operation pending. The same mismatch applies when all registered native units begin inactive during a startup-only enablement.

The inspected startup tests cover grant identity and failed-attempt replacement; the VM uses one initially active native service. They do not exercise this active/inactive inventory mismatch.

**Minimal remedy:** make the source capture, authorized target grant set and target reconciliation agree for the existing supported inactive-service case. Keep real source identities only for processes that actually existed; separately prove legitimate target startups from the registered unit/grant authority. Do not invent source PIDs/epochs, discard unproved consumed grants, or silently change ordinary activation's service policy. Add focused coverage for one active plus one inactive registration and the all-inactive startup-only case, including successful completion/recovery without fabricated source proof. This needs a bounded correction to the existing startup path, not another controller or schema framework.

No additional Blocking or Important findings were identified. Resolve these Important findings, or record an explicit disposition under the mandatory workflow, before long execution. The report does not certify a remediation that has not yet been made. The lead can use step 9 for direct narrow fixes; apply affected-lane review only if their design or supported contract changes.

## Exact scope and independent method

This is final review of the committed runtime component and its actual SDK consumption, before runtime long/native/VM/browser acceptance.

- Runtime repository: `git@github.com:aither64/dev-workspace.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/dev-workspace`.
- Complete range: `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7..fa7ede4234a8cdc99be5f39fdd058c5c3e97d345`.
- Exact merge base: 3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7.
- Final tree: `06bd1e334ed38032be92b24e8eccf1f2bd7d525b`.
- Complete series: five commits; 127 paths, +25063/-159.
- New delta from retained f161: 90 paths, +16771/-85.
- SDK: `d3a29bee90ef00a08816920408c596152339a637..c3c2adb705f5ff6bb42c98bd44be3649fd93bedb`, tree `f7629a0f994ad56a20dd5b92247463c28f4090a2`, one direct-parent prerequisite commit.

Runtime and SDK HEAD/tree/clean state were checked directly. The runtime's complete final patch equals the supplied full.diff. I matched all 90 accepted source hashes and all 15 main receipt artifacts, plus the B/C/D listed source hashes and B artifact hashes. The main committed receipt SHA256 is `a0abd947b0b2478e136b7e7c8af35fb051f52188ea4bb7fbbf9133e5b104ad03`.

Before owned records, exact tracking-CWD `dev-session current` printed `2026-11-03-lead-wakeup-delivery`; both shell markers were absent and the trusted developer workspace/session binding matched. Retained reviewer0 settings remained **gpt-6.1-sol / xhigh / read_only**. No override, fallback or nested reviewer was used.

I applied all four lanes independently, using the mandatory skill/references and applicable instructions. Inspection covered the bounded packet/design, complete series/diff, new production and shared consumer context, representative tests, native/VM fixture mechanisms and owning docs. Prior f161 conclusions were reused only within unchanged scope; donor behavior was not presumed accepted.

No files were written and no tests, Nix evaluation/builds, native/browser/VM, CI, Git mutations, publication, claims, profile/live operations or lifecycle actions were performed. Hash/JSON inspection was read-only evidence/source analysis. No peer or private session state was inspected.

## Independent scope and architecture conclusions

The later user requirement explicitly adds automated cooperative pause/continuation for future activations, with a main-coordinated first pause window only after verification. That justifies a maintenance component beyond the original wake-up fix. It does not authorize transparent process suspension, forced interruption, queue deletion or arbitrary lifecycle work.

The new delta is large, chiefly reused implementation and its tests. Its mechanisms have concrete current owners and consumers: Go owns the journal/controller/native evidence and private acknowledgement/observer transport; Ruby retains profile, systemd, claim and transition ownership; codex-web supplies transport/submission primitives. I found no need for a second scheduler, daemon, generalized pause framework or alternative checkpoint format. The requested remedies fit those existing boundaries.

The finite live effect reduction is needed to distinguish a continuously observed direct foreground acknowledgement from completed history or an unreported effect. Bounded memory state and explicit loss are preferable to a persisted event log. The same-reader owner/control design serves the drain boundary without creating a replacement observer or reconstructing turn-start coverage.

The SDK's private conditional transport avoids restoring unrelated receiver watches. The runtime uses its durable exact identity and retains terminal notice retirement intent before discarding. Notice cleanup deliberately knows the pinned SDK's conditional context encoding for read-only reconciliation; that coupling is bounded by the exact dependency and matching identity checks, not permission to guess another format.

Registration/launch/policy checks validate distinct trust boundaries; diagnostics confer no admission authority.

## General, protocol and safety assessment

Native caller metadata is resolved against exact retained root/member/incarnation, cwd, source turn, socket epoch, pending tool and operation/ack identity. Readiness requires continuously observed turn-start coverage and the direct foreground call, with effective policy/startup checks; notice receipts and timers grant no readiness.

The volatile bounded observer invalidates authority on unknown/malformed relevant events, pending server requests, missing watch coverage and loss. Statusless search/sleep completion uses exact thread/turn/full-item digests from live completion events, checked in both cleanup passes and the final snapshot. Descendant cleanup, prompts, queues, ledger and command-exit evidence remain separate obligations.

Activity polling/subscription/read work joins before same-reader freeze; the recorder closes separately. HTTP/application and interactive/history/naming resources drain before tail release. Owner PID/start/InvocationID and observer generation remain bound; ordinary shutdown closes the tail. No generation lock spans the cooperative wait. R1 concerns authority after reacquisition; R2 concerns existing completion while waiting.

HUP intent precedes one pidfd-bound signal to the captured process. Structured native refusal proves admission drain; successful source exit is independently checked through systemd. There is no forced second signal or turn interruption. The original invocation's in-memory finish permission grants no replacement call or renewed lease. Orderly close may defer history proof but cannot create a finished participant; exact destination history is still required before continuation. Abnormal loss retains recovery.

Only proved maintenance finish creates a resume obligation. Cold histories, natural completion, uncovered turns and utilities receive no synthetic continuation. Queues/goals use activation; explicit continuation uses one stable identity. Unknown submissions reconcile without replay. Stop is recorded before outer admission and linearized against continuation; restoration must finish before terminal state.

Utilities retain exact monitor ownership and existing lifecycle/effects proof. Original reports and receipt reconciliation continue while new launches/delivery are held; maintenance does not cancel/archive/replay utilities.

None of this proves global cell/process quiescence. Actors must join/account for known work; unreported surviving cells and ambiguous effects remain outside the proof. Terminal turns/drain are not generalized cell checkpoints. Prior cell/archive limitations and deferred R5 advisory retain their original scope.

## SDK review reuse and compatibility

The retained SDK report reviewed 035 and its R1. I inspected the final production delta: observer-only refusal now performs only exact local attempt-state classification before preparation/private transport, preserves the frozen sentinel and avoids relabeling a prior submitting attempt as unsent. The subsequent fixture-only changes do not alter production interfaces. The original report and clarification remain authoritative within that narrow corrected boundary.

The runtime selects **c3c2adb705f5ff6bb42c98bd44be3649fd93bedb** in both Go and Nix:
module `v0.0.0-20261105132033-c3c2adb705f5`;
source NAR `sha256-oXED0TaBUsl4cyKXgQ8JNGCVAO6Xck95MUjHI4WHUzk=`;
vendorHash `sha256-2a/wzBO8ZzpBYZtDPOy1/UcoEClRBWycWvZDBlX/oHU=`.
No temporary replace/modfile or native/model/catalog upgrade is selected.

Current public runtime obligations are preserved: existing managed-turn, service, retry, recovery, submissions, monitor schema1, typed claims and machine identity formats remain. Three maintenance contract keys are additive. A predecessor without the reader may install the final reader only through the ordinary guarded no-enable path; same-source enablement is a distinct startup operation. Retained maintenance state intentionally requires a compatible reader and forward recovery; software rollback must not discard the journals, grants, ledger or pending evidence.

W1b219/Ce3 still consume f161 and are historical deployment provenance only. This review does not accept them as new consumer pins or artifacts. Application selection remains a composed user profile, with the matching host substrate first. Final W/C graphs and actual rollout remain separate gates.

## Full history, repeated streams and migration/state lineage

The complete five-commit runtime series is:

1. `e18a1e8de4d599df830e6ac390c9ab306d23d891` — independent tracking-directory test deadline isolation.
2. `58e87f9d3ccc1aac262b29f587a1d0553257a554` — coherent durable monitor capability.
3. `f161ede8a6ea4cf540edcb7ece81ebb76f064a05` — separately adopted passive archive-hydration diagnostic.
4. `3145caa8fcf23b1e825eb54fe9176258f58c6b7f` — final SDK dependency and genuine historical fixture input.
5. `fa7ede4234a8cdc99be5f39fdd058c5c3e97d345` — maintenance behavior with its supporting tests, docs and packaging.

This is coherent consolidation: prior independent deliverables retain their purpose; final prerequisites are separated from maintenance behavior. No obsolete donor approach, prototype/fixup chain or transitional implementation is retained merely as development history. The donor fc7/c8ee source is additive reuse onto current f161, not a wholesale older runtime selection or a literal-merge claim.

**Repeated update streams:** none in the final series. There is one final production SDK selection; intermediate SDK heads are retained evidence/refs, not successive runtime pin commits. The lock's second SDK d3 node belongs to the deliberately independent original 3bb predecessor graph. It is a different fixture consumer, not a redundant production pin. I independently compared the predecessor's reachable locked/input graph with the original 3bb lock, ignoring node names; they agree. Unrelated production nixpkgs/llm-agents graphs are preserved. No incidental dependency deduplication is required.

**Migrations:** **no database migrations or seeds**. The feature introduces the final private maintenance schema1 directly. Existing operation/startup/store types and validation/recovery structures are retained from the donor; no intermediate branch-format migration or removed reader path was found. Native item-shape adaptations do not rewrite persisted operation state. Existing JSON3/SQLite1 submission formats and migration fences remain SDK-owned and unchanged.

Historical donor publication, deployment and external state consumption remain unproved. The review does not infer global absence or inspect private state. Compatibility is justified by retaining supported schema1 readers/recovery and existing public formats, not by treating retained donor state as disposable. The current runtime component has not established live consumption; pending/old rollout records remain separate provenance.

## Verification evidence and acceptance limits

I read the supplied canonical quick receipts/logs and matched their source boundaries:

- B: maintenance package pass 4.461 s; affected workspacecodex/web/cmd selector pass 0.177/0.903/1.525 s, canonical published SDK, no override.
- C: retained unchanged Ruby host/diagnostics/startup/terminal evidence totals 42 runs and 1046 assertions; inspected host 22/272 and diagnostics 15/640 logs. Canonical agentteams pass 0.022 s, source/graph/module/vendor/parse guards recorded.
- D: exact canonical tagged compile pass 0.031 s, explicitly **no tests run**; retained static syntax/AST/whitespace logs. This is not native/VM/browser execution.
- SDK: exact c3c2 acceptance receipt reports both canonical checks, real native conditional-steer acceptance and exact-head CI success with source/native/NAR/effects evidence. That is SDK evidence, not runtime maintenance acceptance.

Original dirty-tree and ignored cache-busy warnings remain disclosed. Current committed source is clean and matches the retained owner hashes. Earlier SDK setup failures and original R58 hydration failure/unknown cause remain historical failures.

The native fixture uses real selected native exposure, call/output identities, direct MCP, the production observer/controller and real receipt/history effects; its injected parent control does not prove host activation. The VM uses the genuine historical factory with its original dependencies, then public source-bound A refusal/pendingA, natural source completion, final B replacement/pendingB/verified clear without selecting A, followed by same-B enablement. This is meaningful prepared coverage. It has **not run** for this runtime. Its single initially active service does not cover R3.

Remaining acceptance includes corrected-source focused checks, actual maintenance native/VM/browser execution, the full declared runtime checks including the new maintenance check, exact final W/C pins/artifacts/composition, and separately authorized live proof. No old f161/W/C or donor test result substitutes for those graphs. No transparent/global cell guarantee can be claimed from a green fixture.

**Disposition:** all-four-lane final component/consumer review complete; R1–R3 Important await lead disposition. No long execution, publication, deployment, machine-claim action, integration, session lifecycle or activation permission is granted by this review.

Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
