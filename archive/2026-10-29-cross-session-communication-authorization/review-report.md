# Independent FINAL review report

Please persist this report verbatim as work/2026-10-29-cross-session-communication-authorization/review-report.md. My retained developer instruction is 'Remain read-only', so I have not written the artifact or changed source/session files.

## Findings and disposition

No actionable findings. Blocking: 0. Important: 0. Advisory: 0. This completes the independent committed-deliverable review for the exact range below and permits the planned longer verification to begin. It does not establish native acceptance, a passing full packaged suite, final branch readiness, integration approval, deployment, or usability of the installed runtime.

## Identity, independence and scope

Reviewer: retained reviewer0, review purpose, read_only access, ready, roster revision 27. Exact native thread: 01a189c3-61ab-7770-a78e-6ef7d9c7d48b. Saved model/effort: gpt-6.1-sol/xhigh; used unchanged, no fallback. dev-session current, DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE match this session and /home/aither/workspace/ai/vpsfree.cz. Independently inspected only my exact native row in state_5.sqlite, its session_meta and latest turn_context: codex-lb, gpt-6.1-sol/xhigh, CLI 0.165.0, matching session CWD. Native execution policy danger-full-access/approval never is distinct from, and did not override, retained read-only task constraints. No authorship, source edits, nested agents, incident-session private access, long checks, integration, deployment or lifecycle mutations.

Read workspace/repository AGENTS, applicable routed session/documentation/project/Git/lifecycle/verification/writing procedures, mandatory-change-review skill and all four references; full plan, design, state, review packet, and both owner evidence files. Risk High: authorization and durable retry identity. Lanes completed: general; architecture/repetition; scope/proportionality; risk/compatibility.

## Reviewed source and whole history

Repository: dev-workspace, canonical origin git@github.com:aither64/dev-workspace.git. Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-29-cross-session-communication-authorization/dev-workspace. Base/merge-base: 08f3dbb92bc8585929edee85a824d44dfb3b0846. Exact head: c43904a72d705562b79dcf9d59a29cf743bc9de7. Both complete commits inspected with messages, per-commit scope and final diff:

1. ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387 — communication: attach verified grant context to deliveries.
2. c43904a72d705562b79dcf9d59a29cf743bc9de7 — communication: clarify bidirectional runtime authorization.

Parent chain is precisely base -> ed16c606 -> c43904a7. Final HEAD matches the assignment and the worktree/index remain clean. Independent git diff --check for the full range passed. No fetch/push or other Git mutation was performed.

Whole-branch conclusion: no obsolete unmerged approach, transitional shim, fixup/tidy history or superseded branch design remains. The two commits have coherent purposes: runtime and its unit/recovery coverage; consuming policy/docs and production-path/native acceptance coverage. Tests/docs support their behavior changes. No repeated dependency/channel/input/generated-artifact update streams exist; no consolidation is required. No migrations. No transitional migrations remain; schema-1 grants/messages and existing saved tuples are preserved without migration. Packet/owner evidence records no release, deployment or external consumption of this feature, consistent with the diff's lack of migration/schema/pin changes; I did not inspect incident/private deployment state.

## Scope and proportionality

Compared full user intent and later recorded scope decisions against 11 files, 1159 insertions/10 deletions, delivered implementation/check milestones, and available timing evidence. Roster creation at 22:24 UTC and final commit at 22:45 UTC show approximately 21 elapsed minutes through implementation, without summing overlapping member time or claiming a precise active-work clock. 1044 inserted lines are tests; remaining production and documentation changes stay confined to the existing communication owner and consumers.

The smallest sufficient solution is what the branch implements: attach authoritative context using the already-pinned AdditionalContext support, retain the existing registry/locks/transport/schema, and clarify receive policy. It introduces no activation scheduler, parallel authority store, new lifecycle subsystem, transport API, downstream project or dependency update. First ordinarily eligible delivery supplies recipient context; allow's existing result informs the approving lead. This matches the recorded scope decision and preserves holds. Regression layers have distinct purposes: service/recovery invariants; real MCP/command/store/native boundary with RPC simulated; native start/steer plus a context-gated reverse tool reply. Their size alone is not a reason to remove necessary authorization/recovery coverage. No optional hardening is required for this change.

## Correctness, architecture, security and compatibility

portal/internal/communication/authorization_context.go builds application context exclusively from the locked stored grant/message, with exact endpoint slug/thread/incarnation, grant and message IDs, approving session, faithful stored approval audit evidence, grant creation time and message-only scope. JSON encoding separates audit data from the runtime statement. Peer text remains in the ordinary envelope and cannot choose context source, grant, caller or pair. The wording explicitly distinguishes recorded audit text from independently proved natural-language consent, respecting the trusted local operator/consent-recording lead boundary.

service.go Dispatch resolves both current endpoints after sorted runtime locks, takes the existing store lock, validates active grant/endpoints, and only enriches Options when nil. Complete encoded options, including context, face the existing 64 KiB limit before a durable save and native Send. Cloning AdditionalContext avoids mutating transport preparation inputs. Existing saved options/envelopes are reused exactly across restart, held-after-submission, loss of acknowledgement and reconciliation; no timestamps or context refresh are inserted into prepared tuples. Current authority still controls new submission. Reconciliation may prove earlier acceptance after revocation without granting a new send. Existing revoke/Expire/reapproval semantics remain intact.

Reviewed Native.Ready/Prepare/Send/Reconcile, identity resolution, store validation/capacity accounting, MCP native caller binding, command expected-root path, portal dispatch/generation guard, and relevant existing tests. Native remains the owner of recipient eligibility and retained policy. The context helper introduces no second authorization implementation. The existing codex-web module pinned at 9d337b70987f independently confirms AdditionalContext on both turn/start and turn/steer and inclusion in normalized durable options identity. No codex-web consumer/API/pin change is needed.

lead_policy.go, MCP description and existing feature/upgrade guides agree on one approval in either session, bidirectional exact-pair authority, list before refusal for legacy/ambiguous deliveries, no peer-claim authority, submission snapshot freshness and message-only limits. Saved role instructions are retained. Upgrade guidance preserves legacy prepared tuples and forward recovery; an older compatible package can read options but restores the previous missing-context ambiguity. No host/fleet ordering or DB/API/CLI contract change is introduced beyond the already-documented communication prerequisites. Existing README links expose the changed guides in the correct owning repository.

## Verification inspected and remaining limits

Read all newly added tests and relevant existing service/native/capacity/revocation and Ruby CLI coverage. Owner quick evidence reports communication package pass (6.191s), focused workspacecodex/MCP/real-command pass, web approval/revocation/transcript pass, formatting/diff checks and native-tag compile-only pass. I did not rerun already-passing tests or execute longer tests. The independent review does not convert compile-only evidence into native execution.

The native regression is suitable in design for the required boundary: real pinned App Server, actual native MCP caller metadata, production MCP and communication command, persisted registry/service, real Native dispatch and receipts, separate model-facing developer context for idle start and active steer, context-gated immediate reverse MCP reply, and one grant. Its host-selection adapter explicitly substitutes for the unchanged Ruby wrapper, checks fixture workspace/state/profile/CWD/session/member absence/expected root, and does not fabricate sends or receipts. Existing packaged Ruby checks remain necessary for the real CLI boundary. The synthetic Responses backend proves transport/policy inputs and deterministic tool behavior, not arbitrary model judgment.

Required outstanding evidence before readiness:

- Execute TestNativeSessionCommunicationAuthorizationRoundTrip for both idle and steer using the exact pinned LIVE_SWITCH_CODEX path in implementation-b.md, under its bounded watcher command. Any native failure must be diagnosed rather than described as model nondeterminism.
- Obtain the full post-review packaged result, including complete workspacecodex and Ruby CLI checks. The prior 45s whole-workspacecodex timeout in an existing fsync fixture is not a pass and is not established as a product defect; the focused passes do not close this obligation.
- Ordinary publication/CI and lead readiness checks remain as required. No default-branch integration or deployment has been approved; selected installed runtime remains unchanged.

Snapshot limitations are intentional: legacy prepared deliveries retain old context/options, and later revocation cannot recall accepted native traffic. A remembered or copied context block cannot authorize subsequent sends; tool-side current registry checks remain authoritative. This report does not request broader hardening, a provider campaign or new VM suite.

Session portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-cross-session-communication-authorization/
