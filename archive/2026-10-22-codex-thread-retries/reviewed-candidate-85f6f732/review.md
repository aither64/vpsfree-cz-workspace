# Independent final review

Reviewer: reviewer0, retained review-purpose member, gpt-6.1-sol/xhigh/read_only. Identity verified against the trusted session/workspace binding and live roster; no fallback or setting override. Session: 2026-10-22-codex-thread-retries. HIGH risk. General, architecture, scope and risk references read and all four lanes performed directly. No nested agents, source edits, native/integration tests, deployment, merge or lifecycle actions.

Report delivered through report_to_lead and saved by lead, preserving reviewer's read-only role.

## Findings

### Blocking B1: A settings change can leave the current task eligible under an obsolete loaded-binding proof

Lanes: risk/compatibility, general, architecture.
Commit: dev-workspace 0398d16bb166ccc2e16b683b9d45672172961d0c.
Locations: portal/internal/workspacecodex/turn_retry.go:482-498; portal/internal/turnretry/state.go:150-157 and 249-256; portal/internal/workspacecodex/turn_retry_proof.go:184-226.

cancelRetryAdmission calls State.Cancel, but Cancel only consumes a turn when Pending.ResultTurn exists. For an ordinary manually started active turn, or a newly failed turn not yet observed by the scheduler, Pending is nil. Changing settings leaves that turn unhandled and leaves State.Binding and its digest unchanged. On the subsequent eligible failure, Observe resets Cancelled=false as a new chain. Prove accepts the old admission/native context, and Check compares the same old context and policy/provider digest without learning that the managed loaded mode changed.

Concrete scenario: a managed turn executes in plan mode; while it runs, the user changes the next mode to default. The turn then fails with serverOverloaded. A fresh automatic continuation is scheduled from the original plan context, but ContinueFailedTurn sends no mode override and inherits the now-default loaded mode. This violates preservation of the failed turn's mode inside the accepted managed-authority boundary. A model/effort update can similarly be overwritten by the old explicit retry options. The upstream client supports settings updates for subsequent turns without replacing the active turn's settings; the new native queue fixture also relies on this distinction.

Fix within the existing boundary: invalidate the affected execution proof/binding or consume the relevant current task when settings intent changes, including before a retry Pending exists. Keep later independent managed tasks eligible. Do not restore authority from display caches or add automatic policy writes. Add focused tests for settings changes during an ordinary active task and after failure before first observation, then assert that its original turn cannot dispatch; retain a test that a later independent task can retry.

### Important I1: The scheduler's ordinary-session resolver prevents its own uncertain submission recovery

Lanes: general, risk/compatibility.
Commit: dev-workspace 0398d16bb166ccc2e16b683b9d45672172961d0c.
Locations: portal/internal/web/turn_retry.go:221-236; portal/internal/web/server.go:3632-3635 and 3518-3545; portal/internal/workspacecodex/observation.go:252-254. Provider behavior: codex-web/codex/client.go:3074-3109.

stepTurnRetry must resolve a mutation before Controller.Step can run. For ordinary retained sessions without creation evidence, that resolution calls requireOrdinaryRetainedMutation -> ObserveRetained -> ObserveThreadIdentity -> RequireSubmissionAttemptsKnown. The latter rejects prepared/submitting native ledger entries without reconciling them.

Concrete scenario: automatic turn/start is accepted, but the portal dies before its schema-3 submitting entry becomes accepted and before the retry result is saved. On restart the native input exists and the exact saved UUID could reconcile it, but the resolver rejects the unresolved ledger entry before the controller reaches Backend.Reconcile. A crash after the automatic native prepared entry is saved has the same gate problem. The rejection can affect all retries in that session because the ordinary retained observer checks the full team. Automatic input IDs are not browser outbox IDs that a page reload can acknowledge.

Provide a narrow reconciliation-only admission path for an exactly owned automatic attempt while retaining identity, lifecycle, generation, provider and foreign-submission checks. Do not relax ordinary fresh-send admission. Test through Server.stepTurnRetry on a creation-less retained fixture with prepared/submitting retry entries and exact accepted history. The current native B fixture calls Controller.Step directly and therefore misses this gate.

### Important I2: A delayed proved-unsubmitted restart dispatch uses an expired cyber quota charge

Lanes: general, risk/compatibility.
Commit: dev-workspace 259fcd636ecb4afa0c7c4a2384c6f91d7ef8b353.
Locations: portal/internal/turnretry/controller.go:68-105; portal/internal/turnretry/state.go:280-298.

Begin records ChargedAtMS and a cyber timestamp before Continue. If the process dies after this save but before a native attempt exists, a later Step gets no receipt/error and goes directly from Check to dispatch, reusing the already-charged slot. It neither refreshes that charge nor checks whether it has aged out.

Concrete scenario: reserve a cyber retry at t=1000, crash before native submission, restart at t=1301. The same UUID is actually sent at t=1301 with its quota timestamp still at t=1000. Subsequent failed continuations can reserve 30 fresh slots because the old charge is outside the rolling window. This permits 31 actual automatic submissions in one 300-second interval. This is a proved-unsubmitted restart case, not permission to resend an unknown native submitting attempt.

Before a newly possible dispatch, preserve one effective reservation for its current possible-send window, using positive absent/prepared native-ledger proof. Keep genuinely uncertain sends reconcile-only and never charge an accepted reconciliation twice. Add a fake-clock/controller restart regression with more than 300 seconds between Begin and first possible submission, followed by a full quota chain. Also ensure reservation expiration cannot precede the possible outbound time when preflight/dispatch is delayed.

No separate Advisory findings.

## Whole-branch history and pin conclusions

Inspected the complete commit series, final diffs and adjacent consumers at these exact ranges; final HEADs and clean worktrees independently rechecked:

| Repository | Base | Head |
| --- | --- | --- |
| codex-web | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 | d2d74f931cc50e39345c6c15931748062ee51951 |
| dev-workspace | bf6d4b0c49600c15e17fe71248807ef43424e932 | 85f6f7327e6948a13ad110c4c058d8b96b6ab2b9 |
| workspace | 9f6968ebae4f1fbb26ff548ddcbd6cf8332a5b8b | 31dc79ec37f3fffc8b0940e15ba532be3051c00c |
| vpsfree-cz-configuration | c1057731d34513b6ee3bb1dfb4a3e4832fdc67c9 | 37af6aaf2e635146de6c449f088088e1165c4ab7 |

Nine commits: A af2d5bf,25f115f,d2d74f9; B 259fcd6,1f76716,0398d16,85f6f73; workspace31dc79ec; configuration37af6aaf. Logical split is adequate: provider primitives/context, optional HTTP/UI, separate real-native fixture, durable runtime core, package compatibility, inseparable capture/admission/scheduler integration, and isolated dependency/composition updates. Adjacent tests/docs belong with their behavior. No obsolete unmerged approaches, fixup commits, transitional schema versions or compatibility shims for abandoned branch iterations remain in the reviewed series. Prior superseded development SHAs are evidence, not retained feature commits.

Independently grouped the update streams. B updates codex-web once to d2d74f9 across Go/Nix/vendor metadata. Workspace updates its nested runtime once to85f6f73, including the resulting library node. Configuration updates its devWorkspace channel once to85f6f73, including the resulting library node. These are separate owning consumer streams, not redundant sequential bumps. No superseded pin commits remain. Direct JSON comparison confirms that the only changed lock nodes are B codex-web; workspace dev-workspace/codex-web; configuration devWorkspace/codex-web. All input edges/root identities remain unchanged; extension767dfd5 remains selected.

## Migration and compatibility conclusion

No migrations: no database migrations or retry-state upgrade sequence. Private retry schema1 is introduced directly; native submission schema3, roster and history formats remain unchanged. Package capability turnRetryStateSchema=1 and the new candidate gate preserve retry records, including cancelled records, across forward recovery and refuse an incompatible predecessor. Provenance supplied in the packet says no feature/schema has been merged, released, deployed or externally consumed; publication and the same undeployed companion branch are the only current consumption. No intermediate migration or source ref needs preservation on deployment grounds.

The optional provider/capability leaves the required conversation.Client interface unchanged. Consumers were derived from Go imports/wrappers, module/Nix pins, workspace composition and the unchanged extension's mkPackage/runtimeContract integration. The provider/application ownership split is appropriate; no additional speculative abstraction is needed. Current findings are inside the managed-authority contract and do not demand native CAS, arbitrary external-writer exclusion, Codex changes or broader policy recovery.

## Documentation and verification

Placement and discoverability are adequate: codex-web README/reference owns generic continuation/context/HTTP/UI contracts; dev-workspace README/portal/recovery guide owns enrollment, quota, authority, state bounds and forward recovery; the individual prepared rollout/native campaign remains in session records. Documentation states the accepted external-writer/no-CAS limit and avoids claiming a completed rollout. The intended behavior is explained sufficiently; the implementation defects above must be fixed or claims explicitly revised through the lead rather than hidden by prose changes.

Reviewed the provided focused/race/Ruby/browser/schema/compile evidence and test source. No long or native tests were run by this reviewer. Existing quick tests do not cover B1, I1 or I2's composed failure scenarios. The planned post-review native tests and full package checks remain necessary; native-direct busy behavior remains a compatibility gate, not proof of global exclusion. No deployment or live acceptance has occurred.

Disposition: final review is complete for the exact nine-commit candidate, with Blocking B1 and Important I1/I2 unresolved. The branch set is not ready for long integration verification or deployment until the review policy's remediation/decision gates are met. Preserve this review and use the same reviewer for relevant contract/design changes; narrow fixes can follow the skill's direct-verification rule.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
