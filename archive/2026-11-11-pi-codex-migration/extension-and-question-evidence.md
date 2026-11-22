# Extensions and optional asynchronous questions

Package H, implementer4, 2026-11-11. Bounded source investigation and proposed
capability contract for architect0's synthesis; no implementation brief is
released by this note. Owns only this file. No prior executing package.

## Decision supported by the sources

Keep the portal and use Pi's supported SDK/RPC primitives. A small first-party
host tool should publish an optional question and return immediately; a later
authenticated answer should enter the existing durable host message path.
Pi's RPC dialogs and official question examples do not provide that complete
contract. No externally maintained extension is necessary for the assessed
capabilities, and none was surveyed or accepted.

Sources are the official Pi repository at
[`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`][pi], consistent with
[accepted capability evidence](pi-capabilities-evidence.md). That revision is
main, not certification of the observed v1.5.2 release. Current host context is
dev-workspace `6587c4c1cedabee95bcc52f4667e7d33e3a82859` and codex-web
`dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`; their canonical bare/default
AGENTS blobs were read. Existing [design](design.md),
[runtime evidence](current-runtime-evidence.md) and
[resource evidence](resource-evidence.md) remain authoritative for their scope.

## Where each capability belongs

| Needed capability | Reuse or implementation choice | Evidence and limit |
| --- | --- | --- |
| Models/providers, thinking, history, streaming, compaction, abort, steering/follow-up | Built-in coding-agent SDK or subprocess RPC | Already inventoried in accepted capability evidence; no extension should duplicate these APIs. Host owns browser authentication, reconnect and durable admission. |
| Existing MCP tools | Official in-tree MCP extension | CLI loads it natively. SDK must add `createMcpExtension()`, with codemode/tool-search factories as needed, and bind extensions. Preserve caller identity and tool policy in the host; MCP itself does not establish a portal member identity. [SDK][sdk] |
| Portal reporting, peer delivery, goals, mode transitions, optional questions | Small first-party host tools | SDK `customTools` or an inline/file extension's `registerTool`; RPC can load an extension that calls the trusted host. Reuse existing domain logic and caller-bound transport. No general RPC register-tool command is needed. [Tool API][types], [SDK][sdk] |
| Later message injection | Native SDK session methods, or RPC prompt/steer/follow_up | Busy steering arrives after the current assistant/tool batch; follow-up waits until pending tool/steering work finishes. SDK `sendUserMessage` starts a turn when idle; `sendCustomMessage` supports structured details and delivery mode. These are execution primitives, not durable answer receipts. [Implementation][messages], [RPC commands][commands] |
| Blocking choice/text dialog | Built-in RPC `select`/`input`/`confirm`/`editor` | Suitable when a caller deliberately awaits an answer. Separate select and input methods do not supply a combined durable optional choice/free-text card. [UI protocol][ui] |
| Planning, subagents, question widgets | Official examples as reference material | Plan/subagent limits are already recorded. `question.ts` and `questionnaire.ts` await `ui.custom` and reject non-TUI mode; importing them does not preserve the web question workflow. [Question][question], [Questionnaire][questionnaire] |
| External extension | None selected | Reconsider only for a concrete missing capability whose maintained implementation is smaller to own than the first-party bridge, after source/dependency review. A gallery entry, download count or published package is not trust evidence. |

The official in-tree examples have upstream provenance and inspectable code;
that does not turn them into supported portal authentication, isolation or
recovery implementations. The supported public APIs are the integration seam.

## Why RPC dialogs are insufficient for ask-and-continue

[RPC UI documentation][ui] explicitly distinguishes dialog methods, which block
until a matching response, from fire-and-forget notifications/status/widgets,
which expect no response. The [implementation][dialog] creates a UUID and stores
a Promise resolver in a process-local `pendingExtensionRequests` map. Awaiting
that Promise holds the invoking tool/hook's continuation, although the process
can still service input. It is not a synchronous operating-system block.

Answer, abort or timeout removes the pending entry. `select`/`input` default to
`undefined`; `confirm` defaults to `false`. The [response handler][response]
resolves a matching ID once and ignores an unknown ID. Consequently a second
reply, a response after timeout, or a response after worker restart has no
durable dialog recipient. Browser reconnect while the worker lives could be
implemented by a host caching/replaying requests, but the inspected dialog
path supplies neither persistent replay nor authenticated browser answer
admission. RPC stdio trusts its host, not a browser-supplied ID.

Starting a dialog without awaiting it would detach an in-memory callback; it
would not add persistence, later-message receipts or restart recovery. Likewise
`notify`/`setWidget` cannot be treated as answered-question protocols. The
official question examples are even narrower: `question.ts:52–73` and
`questionnaire.ts:92–110` require TUI and await a custom widget; RPC `custom()`
returns `undefined`. These are source findings, not live execution results.

## Minimal optional-question capability contract

This proposal preserves the requested `request_user_input_async` behavior
without reproducing Codex's full protocol or changing the portal's product UI.

1. **Publish and continue.** A trusted tool accepts one or more bounded question
   texts with stable choice IDs/labels and free-text availability. The host
   assigns a question ID, immutable revision and creation receipt, binding them
   to workspace/session incarnation, logical member and conversation/branch.
   It persists the question before publication/acknowledgment, then returns
   `pending` with that ID. The agent continues independent work immediately.
   A displayed/preselected choice is not an answer. Publishing a question or
   letting time pass never supplies missing authorization for dependent work.
2. **Keep the current browser card.** Project that persisted record into the
   portal's question UI with choice and free-text input. Reconnect/page reload
   reconstructs its status from host storage and a cursor/snapshot, independent
   of whether the originating worker is currently loaded. Rendering and answer
   routes keep existing sanitization, bounds and origin protections.
3. **Authenticate and persist answers.** Resolve the opaque portal conversation
   ID server-side, recheck user/session/member authorization, and validate
   question ID, revision and choice IDs or text. Each submitted reply has a
   stable response ID and immutable payload. Commit answer plus pending delivery
   before acknowledging. Retrying the same response returns its prior receipt;
   reusing its ID for different content fails. Treat answer text as data rather
   than dispatching slash commands or expanding prompt templates. Browser input cannot choose a
   native worker, path, socket or trusted sender identity.
4. **Deliver as a later host message.** Include question ID/revision, original
   question context, response ID and attributed answer. Prefer steering for an
   active recipient when timely guidance is intended; use follow-up for queued
   delivery, or normal prompt/custom-message triggering for an eligible idle
   recipient. Preserve the existing scheduler's ordering and holds. A held or
   stopped worker retains the answer without being unheld, resumed or replaced
   implicitly. An eligible idle worker may run through ordinary host dispatch.
5. **Treat multiple replies explicitly.** Distinct replies/corrections receive
   their own response IDs and ordered deliveries. A correction identifies the
   earlier reply it supersedes; never silently overwrite an answer the agent
   may already have used. Concurrent browser retries of one reply deduplicate.
   Closed or superseded questions show their status and reject stale form
   submissions while preserving the user's draft for an explicit new message.
6. **Keep late answers attributable.** Finishing the originating turn does not
   invalidate an open optional question: an answer can become a later follow-up
   in the same valid conversation. Cancellation, supersession, a branch change
   or a different session/member incarnation requires an explicit status or
   rerouting decision. Never silently inject it into another conversation or
   revive a retired recipient. Restart of a process is distinct from changing
   the durable logical recipient; bind dispatch to its current verified worker.

Question creation also needs stable host request identity so a lost tool-result
acknowledgment does not publish duplicate cards. Reuse the existing host
receipt/retry machinery rather than introducing another orchestration service.
Pi `appendEntry` can persist extension data outside model context, but is not
an atomic browser-answer/outbox store. SDK queues are in memory. A Pi RPC
request ID is correlation, not a durable admission identity. Therefore the
design's unresolved supported admission/reconciliation gate applies equally
to answer delivery: a host outbox alone cannot justify retrying an uncertain
Pi acceptance. Preserve honest pending/unknown status until reconciled.

The single development-session cgroup and mount namespace contains lead,
workers and tools, as confirmed by the user. Either SDK host plus children or
RPC workers can implement this contract inside that boundary. No per-worker
security isolation or process shared across development sessions is assumed.

## Practical extension acceptance and updates

Use the normal package/change review and checks, not a separate approval board:

- Pin a coherent Pi runtime and the exact enabled extension source; prefer a
  full commit plus source hash, or a reviewed package artifact with integrity
  and a locked dependency graph. Reuse official built-ins from that same tree.
  Record the small enabled inventory and owner in existing package records.
- Read the actual loaded code and transitive runtime/install dependencies,
  including install scripts, shell/process/network/credential access, hooks,
  tool overrides and resource discovery. Match the reviewed source to the
  packaged artifact. A clean source repository alone does not verify a registry
  artifact or its dependencies. Check licensing and supported Pi API versions.
- Establish current maintenance from upstream ownership, compatible changes,
  release/changelog and issue/security handling evidence for the concrete
  dependency. Record remaining gaps rather than labeling popularity as trust.
  Official provenance narrows the source search; it does not waive code review.
- Bundle reviewed resources through the existing reproducible packaging path;
  disable floating startup installs/updates and unexpected project/global
  executable-resource discovery in managed workers. Keep intended instruction
  and skill loading. Required host tools must fail startup validation if absent:
  Pi otherwise warns/skips a package whose startup installation fails.
- Update deliberately with the Pi/dependency diff, run focused contract checks
  and the existing final review workflow, then package/deploy under ordinary
  authorization. Do not add per-question or per-tool user approval. Freeze or
  replace an extension when maintenance/compatibility fails; preserve readers
  and recovery for existing sessions under the forward-only package policy.

[Pi's package documentation][packages] explains exact npm/commit pins, floating
`-e` updates and dependency installation. Its [security guide][security] states
that extensions execute inside Pi with the launcher's permissions. Project
trust controls resource loading, not tool access. Review is necessary for the
user's trust requirement; it is not an operating-system security boundary.

## Acceptance evidence still required

No application, prototype, build, model call, service or lifecycle mutation ran.
Checks were source/document comparison, pinned official raw reads of both
question examples, source-line verification and a whitespace check of this
file. Source copies reused only this session's accepted evidence directory.

A later authorized prototype must show: publish returns while the agent keeps
working; choice/free-text answers authenticate and reach the correct member;
browser reconnect restores questions; lost acknowledgments/retries do not
duplicate cards or replies; distinct replies/corrections retain order; timeout,
cancel and late-answer behavior is explicit; idle/held recipients behave as
above; restart recovers records and reconciles uncertain delivery. No result
here proves those runtime properties or certifies an extension trustworthy.
No migrations, repository feature heads or integration were created. Lead owns
acceptance/tracking; architect0 owns incorporation into the design.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

[pi]: https://github.com/earendil-works/pi/tree/a22b888a58fe55b668cc45b80749ec88d4eb4ddc
[sdk]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/sdk.md#L96
[types]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/extensions/types.ts#L1716
[messages]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/agent-session.ts#L2370
[commands]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/rpc-commands.md#L46
[ui]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/rpc-extension-ui.md#L3
[dialog]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/modes/rpc/rpc-mode.ts#L80
[response]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/modes/rpc/rpc-mode.ts#L784
[question]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/examples/extensions/question.ts#L52
[questionnaire]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/examples/extensions/questionnaire.ts#L92
[packages]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/packages.md#L19
[security]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/security.md#L1
