# Boundaries for adding Pi now and removing Codex later

Package N, architect2, 2026-11-12. Planning only; L was completed, reported and
accepted before assignment. Session/current/environment and own retained
workspace-write roster were verified. Required guidance/documentation skill
are reused unchanged. This file alone is owned; architect0 integrates the
brief into `implementation-plan.md`/`design.md`, implementer0 maps touchpoints,
and the lead assigns and accepts implementation packages.

**Add the separation needed by two real backends now. Defer migration tooling.**
Keep the current portal, make new Pi sessions opt-in, and leave existing Codex
sessions fully writable on their original backend. Initially one backend owns
the entire development session, including its retained members. Provider/model
selection does not change that backend. New Pi execution uses the selected
session supervisor/cgroup/exact mount namespace with loaded lead/member workers
inside; canonical shared Pi credentials remain the selected auth design.

## Small current contract

The following is an internal type sketch, not a new public protocol or export
format. Match storage versions and existing incarnation evidence in the owning
package; do not duplicate existing creation/roster identity mechanisms.

```text
SessionRef       = trusted workspace identity + development-session slug
BackendBinding   = SessionRef + backendKind(codex|pi) + contractVersion
ConversationRef  = BackendBinding + lead/member address
                   + retained incarnation + nativeConversationId
ExecutionHandle  = ConversationRef + runtimeGeneration
```

- **Trusted routing:** Resolve the opaque portal conversation/member ID on every
  operation, under existing transition/runtime/roster admission rules. Native
  IDs, paths, endpoints and generations come from host records, never browser
  or model arguments. A member belongs to its session's selected backend.
- **Legacy and version fence:** Validated known legacy records without a backend
  field resolve to Codex in memory. Keep their files, native IDs and receipts
  unchanged. New Pi records explicitly carry a schema/backend contract and
  native bindings. Unknown kinds/versions or ambiguous records fail closed.
  Package compatibility must prevent an older writer from ignoring Pi state
  and creating a Codex authority for the same session. Changing the default for
  new sessions never retags existing ones. No bulk record conversion is needed.
- **Neutral portal contract:** Use host-facing message/tool/question/activity
  views, model/settings data, opaque history cursors and operation outcomes.
  Adapters project native events into these views. Preserve current browser
  behavior; report unsupported items/capabilities honestly. Views are not the
  source transcript or execution authority. Capability support is separate
  from user/session authorization and current execution admission.
- **Narrow operations:** The interface covers the portal's create/load,
  read/page/watch, send/steer/queue/cancel, settings/models, pending responses,
  settlement and durable outcome lookup. Do not reproduce the full Codex wire
  protocol. Backend-specific optimizations stay optional and adapter-local.
- **Receipts and recovery:** Each adapter owns native dispatch, history evidence,
  receipt persistence and recovery proofs. Host lifecycle, roster, approval,
  resource ownership and operation policy remain host-owned. A stable receipt
  binds backend/conversation/member incarnation, submission ID, digest and
  action/options. Runtime generation is separate dispatch/response evidence:
  restarting a worker must not mint a new receipt identity or permit duplicate
  resubmission. Reconcile uncertain Codex effects through Codex, never Pi.
  Stale question/tool/event handles must not authorize a current-generation
  mutation. This interface does not itself prove Pi's durable admission.
- **Minimum delivery outcomes:** `Accepted` requires evidence of backend
  acceptance, not completion of tools or external effects. `NotSubmitted`
  requires proof of no native acceptance: a known-unwritten request or a
  definitive rejection before acceptance; missing history is insufficient.
  `Unknown` retains the original receipt and
  holds further delivery until reconciled; it never causes an automatic resend
  under a new ID. Keep these meanings independent of runtime generation.
- **Native provenance:** Retain original native conversation/turn/item identity,
  ordering and lineage in adapter-owned storage or source references. Keep
  history reading/projection separate from execution methods so it can later
  survive removal of an executable runtime. Do not collapse originals to a
  summary or invent a universal persisted transcript now.

## Owning modules and package boundaries

These are source ownership suggestions, not new member assignments. Sequence
shared contract edits once; implementer0's map supplies the exact edit list.

| Owning area / current source | Deliverable now | Dependency and acceptance boundary |
| --- | --- | --- |
| Generic conversation surface: C `conversation/handler.go`, browser `conversation/assets/`; D `portal/internal/web/` | Neutral view/operation types and trusted resolver seam; remove new generic dependence on `codex.*` DTOs | Contract owner settles types before adapter/UI consumers edit them. Existing portal controls and authorization remain equivalent |
| Codex adapter: C `codex/`, D `portal/internal/workspacecodex/` and Codex-specific wrappers | Wrap existing execution/history/receipt/recovery behavior behind the seam | Preserve current native identity, ledger fences and recovery rules; no legacy state rewrite |
| Pi adapter/session runtime: new bounded D implementation modules named in the touchpoint map | Implement required neutral operations, native identity mapping and generation checks in the selected supervisor/worker topology | Depends on agreed host admission, containment and durable-delivery contracts; no unrelated migration prerequisite |
| Host authorities: D `portal/internal/session/`, `teamruntime/`, web resolver, package/runtime contract and CLI entry points | Version-aware session backend lookup, caller binding and old-writer fencing | Host owns domain policy; adapters provide native proofs. One session cannot route its lead and members to different backends |

The generic `conversation/` package may remain in the repository named
`codex-web`; that historical repository name is not a reason to split projects.
Its generic API must not require importing the Codex client/types. During review,
reject new direct Codex calls or native-field assumptions in generic UI, team,
session and workflow code. Put them behind the existing backend boundary rather
than adding scattered `if pi` branches. Keep genuinely Codex-specific terminal
or recovery behavior in its adapter with explicit capabilities.

Suggested future checks for these packages: contract/compile checks for type
independence; resolver fixtures for legacy-default, explicit Pi and unknown
versions; wrong member/backend/generation and old-writer rejection; stable
receipt reconciliation after restart; and browser parity for existing Codex
plus required Pi operations. These are acceptance requirements, not tests run
by this planning package. Adapter independence does not waive the separately
identified Pi admission, tool identity and recovery gates.

An early **manual, opt-in Pi milestone** can expose only the basic operations
whose behavior is proved, with uncertain delivery held and unsupported
automation disabled. Queue execution, automatic retries/fallback and other
dependent automation wait for their delivery/recovery evidence; they need not
block independent legacy extraction or manual evaluation. A missing Daybreak
entitlement does not block a separately proved provider path. Preserve full
legacy Codex functionality throughout and do not present the limited Pi
milestone as completed parity.

## Deferred, explicitly outside the Pi-addition work

No converter/import pipeline, export standard, portability framework,
cross-backend handover, cutover state machine, archive conversion, retirement
command or cleanup package is required now. No existing session is moved,
retagged, made read-only or retired.

Later, prefer conversion of the full conversation where representable,
preserving original source and identifying omissions. A summary continuation
is an alternative if full conversion proves too costly; that is a later scoped
decision, not a current product question or implementation dependency.

Eventually the Codex execution adapter, launcher and runtime dependency can be
removed after remaining execution/recovery obligations have supported
successors. Generic portal views, session/resource policy and Pi execution
should remain intact. Keep original history artifacts and whatever retained
reader is still necessary until a verified successor can serve them; removing
an executable does not authorize deleting history. Separating read/projection
from execution now makes that later choice possible without implementing the
reader replacement or migration machinery today.

## Evidence and limits

No new source research was needed. Reused accepted [runtime evidence](current-runtime-evidence.md)
and [coexistence evidence](coexistence-evidence.md), with fixed D
`6587c4c1cedabee95bcc52f4667e7d33e3a82859` and C
`dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`:
[trusted Target/Client seam][target], [host routing/admission][routing],
[strict legacy authority][authority], [runtime contract][contract] and
[receipt uncertainty/version fences][receipts]. Only this planning file changed;
no application edits, branches/commits, prototypes, tests/builds, model/auth
calls, credentials, services, deployment or lifecycle actions. No automatic
independent review is triggered. Lead acceptance and architect0 synthesis follow.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

[target]: https://github.com/aither64/codex-web/blob/dd90fb4308ba85617ee2a4267cc835aa9a4f11ce/conversation/handler.go#L44
[routing]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/portal/internal/web/server.go#L3877
[authority]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/portal/internal/session/authority.go#L21
[contract]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/portal/internal/session/runtime-contract.json
[receipts]: https://github.com/aither64/codex-web/blob/dd90fb4308ba85617ee2a4267cc835aa9a4f11ce/docs/submission-storage.md#L16
