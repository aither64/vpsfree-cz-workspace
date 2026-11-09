# Native utility lifetime and delivery boundary

Diagnostic owner: implementer1. Scope: diagnosis/proposal only, 2026-11-03.
No application edits, commits, pushes, deployment, lifecycle actions, peer-session
access, or live native inference were performed.

## Conclusion and evidence level

The installed application has an explicit, durable submission path that starts
an idle lead or steers an active one. A temporary native watcher does not enter
that path merely by completing or sending a native collaboration message.
The inspected application observes retained session roots and roster members;
native child events are presentation/activity data, without an operation owner,
durable completion record, or completion-to-lead dispatcher.

The utility's rejection by `report_to_lead` is consistent with the intended
authorization boundary: that capability accepts exact retained roster members.
Making the utility a member would bypass the missing operation contract rather
than repair it.

These are application-source findings. The supplied incident remains seed
evidence: I did not reproduce a native child surviving its parent's completed
turn, nor prove how native `send_message` behaves when that parent is idle.
Policy wording and generated schemas do not prove those native scheduling
semantics. The narrower established defect is the absence of an application-owned
durable handoff for the temporary watcher workflow.

## Revisions and installed provenance

| Component | Inspected identity |
| --- | --- |
| Canonical generic runtime | `c2182254d29c4175c3e9fe4267e5a92dd1da6b79` |
| Canonical codex-web | `d3a29bee90ef00a08816920408c596152339a637` |
| Selected application | `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0` |
| Application derivation | `/nix/store/2jvhgyq2ilxa4cprlswc7fwh93b3snpx-dev-workspace-0.2.0.drv` |
| Derivation `src` | `/nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source` |
| Assembled Codex | `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0` |
| Native executable used for schema extraction | assembled Codex + `/libexec/codex/bin/codex` |
| Native executable SHA-256 | `647b0157e6472a793e0a0bd45bc44ef8ade673b6d8f3db4118260acda4976652` |
| Retained catalog | `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7` |

`dev-session current`, both `DEV_SESSION_*` identity variables, and this member's
live same-session roster identity agreed with the assigned session. The selected
command resolved to the application store path above. `nix derivation show`
established its source path. Byte comparisons found these canonical files
identical to that installed derivation source:

- `portal/internal/teamruntime/{reporting.go,runtime.go}`;
- `portal/cmd/workspace-portal/team_mcp.go`;
- `portal/internal/web/activity.go`;
- `skills/dev-session-monitor/SKILL.md`, `docs/dev-sessions.md`;
- `libexec/workspace-host`.

The application ships codex-web source under `share/workspace-portal/codex/`.
Its `client.go`, `transcript_activity.go`, `activity_recording.go`, and
`headless.go` were byte-identical to the canonical codex-web checkout. The
runtime's `portal/go.mod:7` also pins the inspected codex-web revision.
This binds the relevant source findings to the selected package; it does not
prove the executable identity of an already-running native daemon.

## Existing lifetime and observation contracts

1. **Watcher lifetime is policy, not supervision.**
   [Monitor skill](https://github.com/aither64/dev-workspace/blob/c2182254d29c4175c3e9fe4267e5a92dd1da6b79/skills/dev-session-monitor/SKILL.md)
   requires fresh `fork_turns: "none"`, one operation per identity, and explicitly
   says the watcher is not a team member. It asks the parent to use native waits
   and continue automatically on results. The
   [session guide, lines 203–242](https://github.com/aither64/dev-workspace/blob/c2182254d29c4175c3e9fe4267e5a92dd1da6b79/docs/dev-sessions.md#monitor-long-verification)
   calls this agent-directed delegation, not a persistent job supervisor.
   Neither establishes an idle-parent activation mechanism.

2. **Application activity observation enumerates roots and retained members.**
   [activity.go:244](https://github.com/aither64/dev-workspace/blob/c2182254d29c4175c3e9fe4267e5a92dd1da6b79/portal/internal/web/activity.go#L244)
   builds its wanted threads from owned session roots and ready, non-retiring
   roster members. Lines 336–342 verify and subscribe to those threads.
   Native watcher descendants are not added by this loop.

3. **Native child records are understood for display and wait accounting.**
   [transcript_activity.go:82](https://github.com/aither64/codex-web/blob/d3a29bee90ef00a08816920408c596152339a637/codex/transcript_activity.go#L82)
   projects `collabAgentToolCall` into labels, receiver IDs, and agent states.
   Lines 118–126 project `subAgentActivity` into a path/kind/thread display.
   [activity_recording.go:194](https://github.com/aither64/codex-web/blob/d3a29bee90ef00a08816920408c596152339a637/codex/activity_recording.go#L194)
   only treats sleep and the sender's in-progress collaboration wait as tool
   waits. [turn_history.go:117](https://github.com/aither64/codex-web/blob/d3a29bee90ef00a08816920408c596152339a637/codex/turn_history.go#L117)
   counts collaboration calls and reconstructs wait state. These are not durable
   operation registration or outcome interpretation.

4. **Event delivery to application subscribers is a lossy invalidation signal.**
   [client.go:1385](https://github.com/aither64/codex-web/blob/d3a29bee90ef00a08816920408c596152339a637/codex/client.go#L1385)
   updates item timestamps and broadcasts thread changes. At lines 1955–1967,
   `broadcast` sends only `struct{}{}` to thread-filtered channels using a
   nonblocking send. Consumers must reread authoritative state. This is useful
   for prompting reconciliation; it is not a durable completion queue and does
   not call `turn/start`.

A bounded source search for `collabAgentToolCall`, `subAgentActivity`,
`spawn_agent`, `send_message`, and `receiverThreadIds` found no native-child
operation handler in the runtime's `portal/internal`, `libexec`, `docs`, or
`skills`; the relevant codex-web hits were the projections above and tests.
This negative search is scoped evidence, not proof about native binary internals.

## Why ordinary member reporting differs

[team_mcp.go:283](https://github.com/aither64/dev-workspace/blob/c2182254d29c4175c3e9fe4267e5a92dd1da6b79/portal/cmd/workspace-portal/team_mcp.go#L283)
accepts only message text and stable message ID for `report_to_lead`. Lines
310–322 derive the caller from native `_meta.threadId` and call
`Store.ResolveReporter`; failure produces the exact incident error:
`This caller is not an active team member in this workspace.`

[reporting.go:20](https://github.com/aither64/dev-workspace/blob/c2182254d29c4175c3e9fe4267e5a92dd1da6b79/portal/internal/teamruntime/reporting.go#L20)
requires a unique roster match, a ready/non-retiring member, and a live session
with the exact current root. A native temporary child is not such a member.
The runtime's reporting contract explicitly says completed turns are not
automatically forwarded (`docs/workspace-portal.md:1646`).

Once authorized, reporting reaches
[runtime.go:2322](https://github.com/aither64/dev-workspace/blob/c2182254d29c4175c3e9fe4267e5a92dd1da6b79/portal/internal/teamruntime/runtime.go#L2322):
the service locks the team operation, revalidates caller/root, builds its member
envelope, and calls `SendWithOptions` at line 2428 with exact destination thread,
message ID, action context, and turn options. The existing member identity gates
must remain intact. The normal reports sent during this investigation returned
native receipts with `steered: true`; the lead was active, so those receipts do
not establish idle activation.

## Native-child provenance: available protocol, missing verifier

I ran only `app-server generate-json-schema` using the exact packaged executable,
an isolated temporary working directory, isolated `CODEX_HOME`, and isolated
`XDG_RUNTIME_DIR`. It returned exit 0, without starting a live App Server or
using account/provider state. The generated `v2/ThreadReadResponse.json` hash was
`8aa88b8203cf3cc29fe474595f5d3645c9f0d26d1294ce342ac5d69de1313211`.

The exact schema exposes:

- `Thread.parentThreadId`: optional nullable string described as the subagent's
  parent; `Thread.sessionId`: required session-tree ID.
- `Thread.source.subAgent.thread_spawn`: required `parent_thread_id` and `depth`,
  optional `agent_path`, `agent_role`, and nickname.
- `collabAgentToolCall`: required native item ID, sender thread, receiver thread
  IDs, tool, status, and agent-state map; optional prompt, model, and effort.
- `subAgentActivity`: required item ID, child thread ID, path, and kind.

Thus the protocol has a potential authoritative parent-child proof, rather than
requiring trust in a bare child ID supplied in prose. This is a schema-level
finding. Actual emission, retention, and replay of these fields must still be
tested with the exact native binary before adoption is supported.

[ThreadMetadata, client.go:510](https://github.com/aither64/codex-web/blob/d3a29bee90ef00a08816920408c596152339a637/codex/client.go#L510)
retains `Source` as `any`, so structured `thread_spawn` source is available to a
new strict parser. It currently omits top-level `parentThreadId` and `sessionId`.
`ReadThreadMetadata` at line 3739 checks the returned exact thread ID, but does
not validate parent provenance. Generic `VerifyThread` at line 4274 checks only
ID and working directory and is insufficient for child adoption.
`HeadlessThreadMaterialized` (`headless.go:30–39`) and fresh application-thread
helpers require string application sources; they must not be relabeled as
native-child verifiers. The workspace wrapper sets source kinds to `vscode`
(`portal/internal/workspacecodex/client.go:55`).

Reproduce the schema boundary without touching session state:

```python
import json, os, pathlib, subprocess, tempfile

binary = "/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex"
with tempfile.TemporaryDirectory(prefix="lead-wakeup-native-schema-") as directory:
    env = os.environ.copy()
    env["CODEX_HOME"] = str(pathlib.Path(directory) / "home")
    env["XDG_RUNTIME_DIR"] = directory
    subprocess.run([binary, "app-server", "generate-json-schema", "--out", directory],
                   cwd=directory, env=env, capture_output=True, check=True, timeout=20)
    definitions = json.loads((pathlib.Path(directory) /
                              "v2/ThreadReadResponse.json").read_text())["definitions"]
    print(definitions["Thread"]["properties"]["parentThreadId"])
    print(definitions["Thread"]["properties"]["sessionId"])
    print(definitions["SubAgentSource"]["oneOf"][1])
```

## Minimum robust handoff to assess

This is a proposal for the architect, not an approved implementation.

1. Record one operation durably under the exact owning live session/root before
   launching its fresh native watcher. Retain operation ID, exact source/run/
   attempt identity, expected policy/catalog, and delivery identity. Registration
   must derive the caller from runtime identity and cannot select another root.
2. Bind the exact watcher through native caller metadata and verified parent/
   source metadata, with a matching native parent spawn record and operation
   marker where the pinned runtime actually preserves them. A bare child ID,
   path, shared CWD, or model name is insufficient. Reject ambiguity; do not
   silently add a roster member. This route can preserve native spawning without
   introducing a general command supervisor, if the native proof passes.
3. Give operation watchers a separate completion/escalation capability resolving
   `_meta.threadId` through the operation registry. Persist the first exact
   outcome before acknowledging it. Keep native completion events as reconciliation
   triggers; a completed watcher turn alone does not establish CI success, exit
   status, exact run attempt, or a successful completion report.
4. Feed the immutable outcome to the trusted application submission path with a
   stable operation-specific message ID and action context. Reuse
   [SendWithOptions, client.go:5272](https://github.com/aither64/codex-web/blob/d3a29bee90ef00a08816920408c596152339a637/codex/client.go#L5272),
   `PrepareSendWithOptions`, and `ReconcileSendWithOptions` as appropriate.
   `SendWithOptions` serializes per thread, reconciles prior acceptance, starts
   an idle thread at lines 5407–5432, or steers an exact active turn at
   lines 5382–5405. Model/effort apply only to a newly started turn. This is the
   smallest existing activation primitive worth reusing; member envelopes and
   team sender addresses are not needed for operation notifications.
5. Restart/disconnect recovery must reread durable operation outcome and exact
   native submission receipts. Unknown submissions keep their identity and
   reconcile; no new message ID or automatic rerun. If the watcher ends without
   a valid outcome, surface one incomplete/escalation result, never infer pass.
   Binding loss or unproven native ancestry blocks adoption. Stop/archive/revoke
   and changed-root boundaries must fence delivery under the existing runtime
   authority; this report authorizes no such lifecycle action.

The launch-to-bind gap remains material: the parent must obtain durable bind
acknowledgment before promising automatic continuation. Schema evidence alone
does not justify a design that assumes a child can always be rediscovered after
the parent has gone idle or the daemon restarts. If actual native provenance or
retention is inadequate, runtime-owned utility-thread creation is the fallback
design to evaluate, preserving utility policy outside the roster.

## Verification limits and next acceptance evidence

Executed: identity verification, bounded read-only source/provenance comparison,
exact-binary isolated schema extraction, and ordinary same-session reporting.
No tests/builds or inference runs were needed for this source diagnostic. All
temporary schema directories were removed by their owning context manager.

Not established: native child lifetime after parent finalization; native message
delivery to idle parents; real parent/source fields for a launched watcher;
native completion persistence across disconnect/restart; actual idle lead turn
activation by a proposed operation notifier; completion-loss/cancellation fences.
Existing `TestSendWithOptionsUsesStartAndSteerProtocolFields` is a useful Unix
socket fixture (`codex/turn_options_test.go:38`), but its fake server cannot prove
native lead execution. It was inspected, not executed here.

Before implementation acceptance, use disposable state/sockets and the exact
native binary to verify parent-child metadata and parent spawn history; finish
an owned operation while its lead is idle and observe a new real lead turn;
repeat for failure/escalation, busy steering, duplicate outcome/retry, lost
acknowledgment, disconnect/restart, and revoked/canceled ownership. Keep native
scheduling observations separate from application fixture assertions. No
proprietary native behavior is claimed from monitor-policy text.
