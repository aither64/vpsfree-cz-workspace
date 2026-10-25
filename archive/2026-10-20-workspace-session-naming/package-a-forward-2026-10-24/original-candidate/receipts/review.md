# Independent final review

Important finding requires a fix or an explicit recorded decision before long integration checks. No Blocking findings; no other Important findings.

## Important: buffered post-terminal errors leave retry proof intact

Lane: risk/compatibility and general. Commit: codex-web 96077b6257bd7dac05930312a29eaf00fc900b3c.
Paths: codex/ephemeral.go:810, :849, :944, :1020; codex/ephemeral_retry_test.go:77.

A valid error arriving after failed completion is rejected by handle when identity is already bound, but the same evidence is ignored when buffered before the turn/start response. Example sequence, all with the exact owned thread/turn:

1. Before the start response, receive error(serverOverloaded, willRetry=false).
2. Receive turn/completed(status=failed, error=serverOverloaded).
3. Receive another valid error, for example unauthorized/willRetry=false, or a contradictory willRetry=true.
4. Receive the exact turn/start response, then successful unsubscribe.

handle queues these valid events while turnID is unbound. bind replays them through consumeLocked. The failed completion sets terminalFailure, transient, settled and s.err. consumeLocked's opening s.err guard then drops the following error without applying handle's settled-error invalidation. canRetry still returns true, allowing B's fresh utility call despite permanent or contradictory terminal evidence. With the response delivered earlier, handle:810 instead clears transient and rejects that error.

This is a source-traced ordering defect, not an executed reproduction. Early notifications and rejecting contradictory terminal errors are both explicit supported contracts. Existing tests cover early successful progress/terminal proof and late foreign/malformed errors separately, but not valid post-completion errors buffered before binding.

Apply the settled-error invalidation during buffered replay too, keeping one consistent rule for early and late delivery. Add paired early/late cases with a valid permanent error and contradictory retry progress after failed completion; require CanRetryEphemeralTurn=false and no foreign interruption. This can remain a narrow correction to the owning A commit; refresh/consolidate dependent pins and quick evidence afterward. No broader retry mechanism is needed.

## Scope and evidence

Reviewer0, thread 01a15d67-5def-7982-a0dd-56fb0b1e8e1b, verified against live roster revision22: ready, review purpose, saved gpt-6.1-sol/xhigh/read_only. No overrides, fallback, nested agents or source edits. dev-session current from the bound session directory printed 2026-10-20-workspace-session-naming; both DEV_SESSION identity variables were absent, consistent with the trusted thread binding.

Read mandatory-change-review and all four lane references, workspace/repository instructions and applicable routes; inspected packet, plan/state/design, A/B/C reports, coverage inventory, actual final code/tests/docs, pinned native error schemas/source and actual lock consumers. All four source worktrees matched exact frozen heads and were clean. Each saved final diff byte-matched the actual base-to-head Git diff. Local origin feature refs matched each head; publication itself was not re-queried remotely. No test/build, live model call, CI action, deployment, merge, claim or lifecycle action was performed by this review.

## Complete owned history and consolidation

- codex-web: ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 -> 96077b6257bd7dac05930312a29eaf00fc900b3c. One focused protocol/retry-proof commit with its tests and owning contract documentation.
- dev-workspace: bf6d4b0c49600c15e17fe71248807ef43424e932 -> a5eaeeda1e01a10c660b8eee068fc4903bc1fca2 -> ae0399b31746bc14ea2fcbe3185f36d8e4b04885. One dependency update first, then one naming behavior commit.
- workspace: 20716e4431b0c6d2d78a41e1e638a1f6305860e4 -> 98e2964727133d5a4871f70be205b90e29eff20f. One composed runtime update.
- vpsfree-cz-configuration: c1057731d34513b6ee3bb1dfb4a3e4832fdc67c9 -> c647a130564dd91219af96af8f83a1ab69fc0bb6. One generated channel update, with generated message/changelog retained under its long-line exception.

Workspace ancestry above remote default9f6968e also contains 7e66fed3, efb2448f, 21e250a1 and 20716e44. These pre-existing shared-master coordination commits precede the owned feature and affect tracking/archive records; they are not feature fixups or repeated dependency updates. Preserve them.

No obsolete unmerged approach, fixup series or transitional implementation remains in the reviewed complete owned histories. One final pin stream exists at each consumer boundary: runtime -> client96077b62; workspace -> runtimeae0399b3; configuration devWorkspace -> runtimeae0399b3. Actual changed lock nodes are respectively [codex-web], [codex-web,dev-workspace], and [codex-web,devWorkspace]. Extension767dfd58, native package, sibling nodes and input/follows mappings remain unchanged. Earlier publications were superseded together within this initiative; supplied provenance records no merged/released/deployed or supported external boundary requiring those intermediate pins. No redundant pin commits remain.

No migrations in any branch, and no persisted-state or wire-format change. Migration lineage is empty and sound; no transitional migrations remain. Existing reserved bases/slugs stay immutable, including older attachment_only records.

## Contract, ownership and proportionality conclusions

The shared provider owns notification validation, execution settlement and private retry metadata. B imports the exact selected client and owns retry policy. Repository-wide import/call discovery found dev-workspace as the external Go consumer; codex-web's own example/conversation paths retain their existing APIs. The extension composes dev-workspace.lib.mkPackage, and configuration's existing dev-workspace/devWorkspace role supplies the host module/contract. The additive accessor preserves RunEphemeralTurn and errors.Is categories; consumers that do not opt in retain compatible behavior.

Outside the finding, B creates one30s deadline before semaphore admission, retains its capacity slot, resolves provider once and makes at most two utility calls. The200ms cancellable backoff and >=1s inference+250ms cleanup checks use the original deadline and recheck it after waiting. Invalid output and unproved errors do not authorize a fresh attempt. Ultimate failure returns before base/slug/handoff reservation and retains the accepted request for existing retry/manual controls; attachment-only custom names remain supported. No speculative fallback or disproportionate framework was added.

Owning docs describe the final behavior and constraints. System then application profile is the recorded deployment order; both select the same runtime. Older writers retain their earlier naming policy while reading compatible state. Forward package recovery and exact post-activation identity/continuity checks remain required. Review grants no integration or lifecycle authority.

## Remaining verification gates

- Corrected A native ownership/protocol execution and B packaged browser/native creation remain pending. Quick tests and fixture compilation are not native acceptance evidence.
- Both failed superseded CI logs retain the original positive-case failures (512ms and470ms). Pinned native source confirms that overload requires nested response.error.headers={"retry-after":"1"} for progress; current positive fixtures include it, and terminal/fresh/persistent fixtures omit it. Two-call exhaustion in those older failures remains inferred because their wire/request counts were unavailable. The queued exact-head CI snapshot is not a passed check.
- The coverage inventory accurately distinguishes real portal admission under a manually held shared lock, collection/preparation/activation exclusion, generation-change refusal, and real collector/candidate races. It contains no single actual-sweep+portal-creation fixture. Execute the bounded disposable combined probe before declaring that mandatory acceptance item satisfied; component coverage or a green creation VM cannot establish it. The lock boundary itself is unchanged, so this gap does not justify expanding product scope.
- Session-only live discovery/overlay is prepared/compiled evidence. It uses the production naming helper and deployed private child without registered session creation or a new product API. Its quiet-backend and identity prerequisites must be checked at execution. It has not proved selected-provider availability, deployment identity, portal health or conversation continuity.
- Resolve the Important finding, then obtain current-head native/package/concurrency/CI/build evidence and post-deployment real-provider/health/continuity results before declaring the runtime ready for use.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/
