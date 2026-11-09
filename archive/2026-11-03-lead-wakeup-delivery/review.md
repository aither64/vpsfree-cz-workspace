# Final independent review

Reviewer: reviewer0, retained review-purpose member, saved gpt-6.1-sol/xhigh/read_only; no override, fallback or nested reviewers. Identity verified with `dev-session current` in the exact tracking directory and the trusted thread binding. Both environment markers were absent. All four mandatory lane references were read and applied.

## Findings

### R1 — Important: a blocked observation can indefinitely starve unrelated outcome delivery

Generic commit `992fc0074f29ab0cad3ad7cb45694ddac528d7b8`, `portal/internal/web/monitor.go:111–128` (also `monitoroperation/delivery.go:Observe`).

The worker shares one 20-second context between the entire observation pass and subsequent event dispatch. It observes up to 16 operations before even listing pending events. Observation can wait for session/team/operation ownership or a native metadata/history response.

Concrete case: two operations exist. A's utility is not yet marked terminated, and its observation remains blocked; B already has a persisted terminal outcome and an otherwise eligible idle lead. Each pass reaches A and spends the remaining deadline there. If B comes first it is observed, but A still consumes the rest of that same pass. Pending(ctx) then fails on the expired context and the dispatch loop cannot run. Rotating nextOperation does not provide delivery fairness when every small-set pass still visits A before dispatch. B remains unwoken for as long as A remains blocked. This reproduces the core symptom across otherwise independent operations/sessions.

Give saved-event dispatch independent progress from utility observation, and bound individual waits so one operation cannot consume every delivery opportunity. A small scheduling/budget change is sufficient; no new scheduler or framework is requested. Add one focused worker regression with A's observation held beyond its allowed wait while B's saved event reaches accepted, retaining existing cancellation, admission and immutable-ID behavior. The current web tests cover preparation and immediate shutdown, not this case.

No Blocking findings and no other Important findings were established. R1 needs a fix or explicit recorded acceptance under the mandatory-review workflow before proceeding.

## Scope and proportionality

I compared the original wake-up request and subsequent “implement it” boundary with plan/state, the full +6110/-76 generic diff, the separate 17-addition/5-deletion workspace guidance diff, and delivered quick-check milestones. The size warrants scrutiny, but the substantive mechanisms remain tied to the accepted capability: fresh utility authority, immutable launch/outcomes, existing native send/reconcile, and inclusion in existing lifecycle/provider inventories. Launching a utility in the session cwd without those inventories would break existing ownership proofs. Evidence resolve is bounded to clearing the external-effects fence and cannot override native uncertainty.

The implementation reuses the configured client and submission ledger instead of adding command execution/retry supervision, roster membership or a general delivery framework. I found no independently useful unrelated subsystem bundled into the capability commit and do not request optional hardening or a native-adoption experiment. The one generic capability commit with its tests/docs is coherent; consuming workspace instructions are correctly separate. The available records do not support reconstructing a complete nonoverlapping team working-time total, so no elapsed-time stall inference is made.

## Architecture, correctness and risk

Generic dev-workspace owns the behavior. Actual consumers/contracts inspected include its portal worker, MCP/Go/Ruby adapters, session recovery, retained-team observations, provider inventory, host package checks, the workspace flake override/policy and pinned codex-web APIs. The dependency direction remains one-way; neither codex-web nor the vpsFree extension needs a source change.

The operation store uses private bounded schema-1 files, locked immediate saves and atomic publication. Launch records thread-start/bootstrap intent before those native effects, retries use the original identity and frozen policy, and a lost start does not spawn a replacement. Utility reports derive identity from native metadata and cannot select a recipient/operation. Ordinary retained-member report authority remains separate.

Delivery preserves one event/message/options identity and reconciles uncertain receipts before another send. Cancel/revoke retain uncertain effects; status/resolve recovery is tied to the original root/incarnation and pending journal and does not send or resume work. Utilities are outside automatic turn retry. Native termination observation is cold and cannot infer test success. The worker-progress defect in R1 is the material exception found.

The separate inventories preserve utility ownership without changing roster formats. Native/receipt uncertainty and external effects remain independent lifecycle fences. Retirement uses exact quiescence and positive archived proof; no deletion/recycling fallback was introduced. These conclusions are within the trusted-local-operator boundary and do not establish live native success.

## Whole-branch history, repeated streams and state provenance

Reviewed complete ranges:
- dev-workspace: `c2182254d29c4175c3e9fe4267e5a92dd1da6b79..992fc0074f29ab0cad3ad7cb45694ddac528d7b8`, exactly one commit, “monitor: deliver durable utility outcomes to idle session leads”; merge base equals the supplied base.
- Workspace: `adabd0bdedd45e24d7b8f00c8cbaa30987804302..a595211e2a2a0cec23632a7c9aa06b132eb5dbda`, exactly one commit, “docs: define durable monitor continuation workflow”; parent/merge base equals the supplied base. I independently ran range-diff against `6383e8848c92c06a9d817f8109853b5b61305c89..66f69418d`; it reports patch equality. Reviewed guidance blob is `1c0f21aa79b831f65b24b68e7896979266082871`.

No obsolete unmerged approaches, fixup series or transitional migrations remain in either reviewed series. No repeated dependency/channel/input/pin/generated-artifact update streams exist; no consolidation exception is needed. The old workspace drafting history is absent from the final one-commit range.

No database migrations or seeds. The only new persisted format is the final private monitor-operation schema 1, introduced directly with no reader/migration for an abandoned prototype. Existing manifests, rosters, recovery and submission-store formats remain unchanged; same-epoch ActiveThreads enrollment preserves prior entries. Policy-1/2 startup support is compatibility for existing baseline contracts, not obsolete feature history.

The packet records prototype state only in disposable fixtures and no feature merge, release, deployment or external consumption. The inspected history/tree contains no evidence contradicting that provenance and requires no supported intermediate schema. On that evidence, migration/state lineage is sound. The branch review does not supply independent proof of absence of every possible external consumer.

## Compatibility and verification limits

The pinned codex-web revision `d3a29bee90ef00a08816920408c596152339a637` supplies the actual start/steer/reconcile and bootstrap contracts used here. Workspace still selects generic baseline c2182254 through extension e4e7e95; no dependency pin or runtime deployment is included. Consuming guidance is capability-conditional and preserves the active-parent fallback.

Reporting policy 3 changes the MCP tool invocation, requiring an ordinary idle daemon cutover on a future authorized rollout. Exact startup policy-1/2 proofs remain. Existing operation state, including malformed state, fences selection of a package lacking schema/policy support. Recovery is forward-only, not arbitrary downgrade compatibility. Native epoch change holds automatic execution; retained outcomes can deliver after ordinary explicit lead activation. Review grants no integration/deployment/lifecycle permission.

I inspected the quick evidence: all three combined status files are exit 0; five selected Go packages passed; Ruby monitor 4 tests/25 assertions and host 4 tests/26 assertions passed. Final tagged advertised-shell check passed without launching the App Server. Final source hashes match the packet: native fixture `289fabc80c1d447cc4988299141bba3d2fc3d6b5f3f2da37bcf92fe9d778b0be`, teamruntime/runtime.go `97cc0032a658a9a003e7c5d4151924d7512133a82a2273e56eab698fe4bf2c74`. Both worktrees were clean at their exact reviewed heads at completion; scoped diff whitespace checks passed.

I ran no tests/builds or runtime/lifecycle operations. The ten-mode native fixture is prepared, not executed. Real idle activation, busy steering/settings, original-receipt reconciliation under lost replies, restarts, cancellation and missing-report behavior remain post-review acceptance gates. Provider/user/stop holds currently have deterministic evidence, not a new real-native acceptance result. Fresh pre-bootstrap retirement remains specifically unproven; preserve refusal/archiving recovery if native cannot prove archival rather than claiming universal support or adding a fault framework.

Owning skill/session/portal/test guidance is discoverable from the README and describes these constraints; the workspace change agrees with its capability/fallback boundary. Full package checks and native acceptance remain for the lead after R1 reconciliation.

## Disposition

Final independent review of the exact committed ranges is complete with one Important finding. The history/consolidation and migration-lineage portions pass. Native usability and final branch readiness are not established. Next action: bounded R1 remediation/verification, then the already planned packaged/native acceptance.

Read-only constraint preserved: this report is sent to the lead for verbatim persistence as review.md; I did not write session records.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
