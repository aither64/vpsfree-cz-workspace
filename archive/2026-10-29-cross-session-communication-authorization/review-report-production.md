# Affected independent FINAL review: production composition

Report for lead persistence as work/2026-10-29-cross-session-communication-authorization/review-report-production.md. I remained read-only and did not write the artifact.

## Findings and decision

No actionable findings. Blocking: 0. Important: 0. Advisory: 0. All four affected lanes are complete for the exact final range below. The planned bounded full native run and required packaged/CI verification may begin. This decision does not establish actual-worker native delivery, complete-suite success, readiness, integration approval, deployment or installed usability.

## Identity and review boundary

Same independent retained reviewer0, ready, purpose review, access read_only, roster revision 27. Saved gpt-6.1-sol/xhigh unchanged, no fallback, requested provider codex-lb. Exact native thread 01a189c3-61ab-7770-a78e-6ef7d9c7d48b. Independently rechecked dev-session current and both DEV_SESSION identity variables against the trusted binding: 2026-10-29-cross-session-communication-authorization, /home/aither/workspace/ai/vpsfree.cz. Own exact native database row, session_meta and latest turn_context agree codex-lb, gpt-6.1-sol/xhigh, CLI 0.165.0, matching session CWD. Native danger-full-access/never execution policy did not override my retained read-only instructions.

High risk; affected lanes: general, architecture/repetition, scope/proportionality, risk/compatibility. Used the previously read mandatory-change-review skill and all four references and applicable unchanged routed workspace procedures; reread repository AGENTS, new packet, full production design addendum, B/C evidence, current state and original report. Full original user intent and accepted boundaries remain as previously reviewed. No authoring, nested agents, long tests, incident-private access, live runtime mutation, fetch/push, integration, deployment or lifecycle action.

This is final review of substantive C and revised B production-worker composition. A and all B files other than the tagged native fixture are unchanged from the original reviewed deliverable; their prior conclusions are retained, without pretending the earlier review covered C or actual-worker acceptance.

## Exact source and complete history

Repository dev-workspace; worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-29-cross-session-communication-authorization/dev-workspace. Canonical origin git@github.com:aither64/dev-workspace.git.

Final base/merge-base: 08f3dbb92bc8585929edee85a824d44dfb3b0846.
Final head: a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5.
Complete ordered series independently inspected:

1. ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387 — communication: attach verified grant context to deliveries.
2. 99da3951e621d0424f8c7ae74b30662501a1ddef — communication: clarify bidirectional runtime authorization.
3. a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5 — communication: use fresh observer activity for delivery admission.

Exact parent chain confirmed. Worktree/index clean and HEAD correct at inspection/end. Full-range git diff --check passed independently. Local origin/master remains the base; fresh-fetch evidence is lead-owned, not a new remote freshness claim from me.

Whole-series/consolidation conclusion: no obsolete unmerged approach, transitional shim, superseded fixture iteration or fixup remains. Runtime A is the identical original commit. B differs from original reviewed c43904a7 in only the tagged native fixture; policy/docs/real-command coverage are unchanged. C is a coherent separately reviewable production fix with its own focused tests. B's broader native acceptance test intentionally exercises the complete feature and requires C for active delivery; there is no second competing fixture or duplicated production mechanism.

Independently verified pre-consolidation 855eab51fcacf90f0e05c804c3e7d056d2ad7ec9 and final a6c0e10f have identical tree 7177a7a43218f4f91ad23d5be12430a1742a65d7 and an empty diff. Range-diff maps A equal, B with settled fixture adaptation, whole C equal, fixup absorbed. The old/new C production patch IDs also agree. Recorded diagnostic heads/results and original review remain separate evidence, without retaining failed fixture history in the final series.

No migrations. No transitional migration lineage or schema conversion remains; existing schema-1 communication state, saved tuple identity and recorder ownership are unchanged. No dependency/channel/input/generated-artifact update streams or pins exist in this series; no repeated stream requires consolidation. Packet/evidence records no feature release, deployment or external consumption, consistent with this diff; no deployed/migrated lineage is being rewritten.

## Scope and proportionality

Compared original one-approval/bidirectional-message intent, exact-pair/current-authority/held-delivery requirements, accepted scope decisions, final diff and delivered milestones before detailed hardening. Final series is 14 files +1599/-11, of which 1447 additions are tests. Delta from originally reviewed head is only four paths: one tagged fixture plus C's three files. C adds 37 production lines/removes one; no new scheduler, authority system, global recorder, protocol, public interface, state schema, downstream project or deployment subsystem.

Available timestamps show approximately 61 minutes from roster creation at 22:24 UTC to final consolidation at 23:25 UTC, not a measured active-work clock. There are concrete intermediate milestones: original review/idle acceptance, bounded startup/seed corrections, active-readiness diagnosis, demonstrated production client/observer mismatch, C failing-before and focused passing-after evidence, then consolidated actual-worker fixture. Those findings justify this addition within required working-recipient delivery. They do not justify broader activity refactoring or optional safety frameworks. The current small web composition repair is sufficient and conventional.

## Production C assessment

portal/internal/web/communication.go: communicationClient embeds the original communication.NativeClient and overrides only ReadActivity. Metadata, SendWithOptions and ReconcileSendWithOptions continue to delegate to the operational workspacecodex client, retaining provider/recovery/policy and receipt behavior. The observer cannot accidentally become the delivery client through this adapter.

portal/internal/web/activity.go: readFreshActivity takes the existing per-thread and global acquireRead gates and directly reads the already-owned observer. It does not call display readSnapshot, consume warm UI snapshots, observe failure backoff, or substitute stale success. Gate release covers both success and error. Cancellation is passed through, and existing gate cancellation behavior is exercised without a second concurrency framework.

The adapter rejects errors, Stale snapshots and mismatched ThreadID on both observer and monitor-free direct paths. It does not manufacture working state or treat incomplete historical counts alone as a hold. Native.Ready's existing provider admission, runtime authority, exact socket/recovery epoch, recipient metadata, current activity and blocking wait checks remain intact. Unclassified/user-input/approval states still hold with no send.

Inspected actual startup composition, monitor ownership/subscriptions, observer-only configuration, provider/resume/recovery checks, provider watch refresh, normal worker generation admission and shutdown. NewContext initializes activity before communication. The existing observer shares workspace/socket/history and uses the existing provider/recovery admission callback; C creates no observer/subscription on demand and alters no worker lifecycle. The pinned codex-web ReadActivity contract is read-only and does not subscribe, resume, answer requests or change settings. ReadFresh uses that owning contract rather than attempting to recreate activity classification.

The global/per-thread gates remain shared with browser/background reads. Dispatch's existing exact-pair runtime/store locks and durable submission ordering are unchanged. Existing saved options/envelopes/grant snapshots are untouched, so C introduces no new retry or mixed-version storage boundary. Older compatible runtime packages can decode state but retain their prior missing-context/activity-composition behavior.

Focused C tests exercise the real communicationService constructor and Dispatch with poisoned operational activity; verify operational metadata/send/reconciliation delegation; bypass warm idle/working cache and active failure backoff; cover current/automatic wait/incomplete history versus error/stale/wrong-thread/blocked states; retain valid provider reservation/runtime/recovery/socket/metadata holds before activity; and test gate cancellation plus monitor-free guarded reads. The source and recorded failing-before result support the identified composition defect. No broad hostile-local-operator threat model was added.

Existing feature/upgrade guides remain accurate: this repairs already-promised working lead delivery and adds no operator action. Nearby comments explain the important fresh-admission/display distinction. No new guide or public copy change is necessary; original policy/docs/context review remains applicable.

## Revised B native fixture assessment

The final tagged fixture constructs the actual recorder-free production client with newCodexClientWithHistory, the public portalweb.NewContext with ObserveActivity and RecoverSessions enabled, and lets its actual communication worker deliver both messages. The fixture's communication.Service instance only reads ordinary registry status. There is no direct Dispatch, test-owned recorder/subscription, activity override, private worker call or transport decorator.

Isolation is explicit: disposable workspace and separate private state outside it, temporary Codex home/socket/authority, absent provider catalog, owned profile symlink and synthetic Responses endpoint. Native MCP children receive explicit fixture env, retaining the strict checked host-selection adapter. Manifests provide exact native root/socket/version and ordinary empty scope; execution-active/automatic-restoration-off recovery records permit normal gates without invoking absent tmux restoration. Profile generation identity is established through normal constructor behavior and remains stable while the actual generation-guarded worker runs. The fixture does not select an installed/live profile or workspace authority.

The bootstrap uses the existing native first-turn contract and no activity recorder. In steer mode, a real held provider request and public activity endpoint require the portal-owned observer to report the exact live turn as working before send admission. The recorded delivery receipt must match client message ID and the requested start/steer mode. A developer-channel registry snapshot is checked against the grant from A, including endpoints/incarnations, approving session/evidence, creation time, message ID and limited scope, separately from forged peer user text. Only then does the synthetic backend produce B's reverse native MCP reply. The actual worker must deliver that reply, with original reference/endpoints, one grant and retained roster/model evidence. No local allow in B or fake receipt substitutes for the exchange.

Cleanup releases the held Responses stream before portal Close, drains portal observer/worker shutdown while native remains available, then closes clients/history and cancels/signals/waits for the owned native group. This ordering addresses the documented held-stream shutdown dependency without touching real sessions. The original checked host adapter still substitutes for unchanged Ruby host selection; full packaged Ruby checks remain required. Synthetic Responses verifies protocol/policy inputs and deterministic tool behavior, not arbitrary model reasoning.

## Verification and residual required evidence

No long tests or redundant quick reruns were executed during review. Inspected recorded evidence: C failing-before 0.099s, focused communication/activity pass 2.133s and strengthened provider-reason pass 0.261s; B actual constructor/health pass 1.415s, native-tag compile-only 0.050s and focused MCP/real-command pass 0.500s; formatting/range diff checks. Independent source/history/diff checks above passed.

Required next evidence before readiness:

- A fresh verification watcher must execute the full exact pinned-native TestNativeSessionCommunicationAuthorizationRoundTrip command from implementation-b.md against a6c0e10f, both idle and steer. Constructor health and compilation are not delivery proof. The old direct-path idle pass does not certify this changed production-worker composition. The current native test remains unexecuted, so this review makes no actual-worker acceptance claim.
- Obtain complete packaged Go/workspacecodex/Ruby results and ordinary feature CI. The prior 45s broad workspacecodex timeout remains an open verification obligation; it is neither a pass nor, by itself, proof of a product defect. Investigate any failure from preserved evidence rather than blindly retrying or weakening admission.
- Preserve source/head identity and normal final readiness checks after verification/publication. No default-branch integration, deployment or session lifecycle action is authorized.

I found no additional production repair required before those checks. Do not broaden the observer subsystem or verification campaign without new concrete evidence. Retain original review and diagnostic provenance; update current state/backlog to the final consolidated heads when recording this review.

Session portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-cross-session-communication-authorization/
