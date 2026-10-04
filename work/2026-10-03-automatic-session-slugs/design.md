# Automatic portal session slugs: technical design

Status: coordinator accepted the independent preparation, upload, collision,
browser and verification design on 2026-10-03. Those units are ready for bounded
implementation. The coordinator subsequently selected the restricted utility
contract in [plan.md](plan.md): pure clock may remain, questions fail immediately,
and model action tools plus project/workspace/team instruction injection must
be disabled. The user confirmed: "Keep model naming, disable tools that access
files or networks, and reject questions immediately (recommended)." The
coordinator clarified the trusted-operator boundary: serving-instance global
user policy remains, and operator MCP reconfiguration pauses naming through
existing service/package procedures. These are documented operating boundaries,
not release blockers. Exact-binary runtime proof remains required.

Current naming-model decision: the coordinator explicitly selected `gpt-5.5` /
`low`, superseding Luna for this utility only. The
[Direct-profile supplement](#selected-direct-profile-and-serving-catalog-gate)
owns the current implementation brief. Its serving-catalog prerequisite is not
yet established; model-name selection alone cannot enforce Direct mode on the
shared daemon. Native proof and the separate logging decision remain open.
The [naming-only static-runtime proposal](#candidate-naming-only-static-runtime)
below supplies a source-supported candidate for that prerequisite; it awaits
coordinator selection and implementation/native verification.

## Scope, ownership and evidence

New session in the portal accepts an initial request and team selection, with
an optional custom short name under expanded options. Forks, approved-plan
creation and CLI name syntax keep their current behavior. Generated names use
the accepted date plus a short name of at most 48 ASCII characters. Once a
destination is reserved, retries never rename it.

The architect owns this brief and verification planning; the coordinator owns
consequential decisions, tracking and rollout; the implementer owns application
edits. No commits, pushes, application edits, live turns or long checks were
performed for this investigation. `dev-session current`, run from this session's
tracking directory, returned the exact bound slug; both environment identity
variables were absent. The shared checkout has unrelated changes, which were
left untouched. The initial plan/state commit is `c9366959`.

Initial worktree inspection (historical starting points, not the final deployment
ancestry): application bases then equalled their local `origin/master` refs.

| Repository | Base | Owning interfaces and likely files |
| --- | --- | --- |
| codex-web | `4c170393a96ed0a6ac2e43488d073f6fcab36132` | New `codex/ephemeral.go` and focused tests; bounded private notification handling in `codex/client.go`; `test/codex_protocol_contract.py`; `docs/reference.md` |
| dev-workspace | `924c0ec28c41dd8b56aaf17f2212b302ca614899` | New preparation/naming files under `portal/internal/web/`; existing `creation.go`, `creation_store.go`, `server.go`, `uploads.go`; `portal/internal/uploads/store.go`; `portal/internal/session/authority.go`; bounded reservation guard in `libexec/dev-session`; `static/app.js`, `static/creation.js`, `templates/index.html`, `templates/creation.html`; focused Go/Ruby/browser tests; README and portal/session guides |
| vpsfree-dev-workspace | `8f8d8ecf5031c40d3e4a4ee2e9425721fc035800` | Runtime dependency pin only |
| workspace | `c9366959fd4a5deea5a8205b73044091951dc597` | Assembled package dependency pin and initiative rollout records |

Worktrees are beneath `worktrees/2026-10-03-automatic-session-slugs/`.
Host configuration is expected unchanged. The application is an assembled user
profile, never a system pin. The coordinator must refresh upstream refs before
final integration; this read-only inspection did not fetch or rebase them.

### Deployed predecessor and required preservation

The coordinator's subsequent source/installed-contract inspection establishes
the actual predecessor. The shared root's pre-feature lock consumes extension
`399c33023a568a8d7a21e4e4df52829628720a28`, which pins generic runtime
`4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4`. Runtime `origin/master` remains
`924c0ec28c41dd8b56aaf17f2212b302ca614899`; the coordinator verified refreshed
refs. This is an already consumed descendant, not stale remote tracking.

`4ef298b3` is one published, unmerged commit after `924c0ec2`, titled
`runtime: require maintenance-aware cluster transition policy`. It advances
cluster transition policy 2 to 3 while retaining schema 1. Its `workspace-host`
change is refusal text; documentation explains policy-2 refusal with registered
clusters and profile-transition tests add 144 lines. The installed package
identified by the coordinator as `zmwh78…` declares policy 3. A package built
only from `924c0ec2` plus this feature would regress that consumed contract.

The coordinator selected preserving exact `4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4`
unchanged as an ancestor of this initiative's runtime feature. After helper work
is committed and the runtime worktree is clean, rebase only this initiative's
unpublished upload/preparation/namer commits onto that exact commit. The
coordinator/implementer owns this operation; this design update performs no
rebase. Never rewrite, fold or replace the published predecessor, and never
change its owner's branch or records. No default-branch integration is authorized
by this preservation decision.

The deployed extension predecessor is exact
`399c33023a568a8d7a21e4e4df52829628720a28`, four published, unmerged descendants
of actual remote default `8f8d8ecf5031c40d3e4a4ee2e9425721fc035800`.
The coordinator verified this consumed lineage, oldest first:

| Preserved extension commit | Subject |
| --- | --- |
| `5b2e9a4bb95bcf4070d62da33b219ed3c5a33f12` | flake: require the maintenance-aware runtime transition policy |
| `101d31264fb54cc39b2d0d9519a202d0705a7078` | vpsadmin: preserve stopped clusters through maintenance copy |
| `f50c92bf146c3f3d93a5293e0c005f5fdb3a26e2` | vpsadmin: preserve assignments in the development storage profile |
| `399c33023a568a8d7a21e4e4df52829628720a28` | vpsadmin: test retained services through interrupted maintenance |

These four commits change 25 files, with 5,288 additions and 67 deletions.
They are already deployed behavior, not new feature scope. Preserve every exact
SHA unchanged as an ancestor of our extension feature. Deploying the old
`8f8d8ecf` extension tree with only a corrected runtime pin would remove consumed
maintenance, storage-profile and retained-service behavior.

The coordinator verified our extension branch is clean with no own commits and
selected fast-forwarding that branch to exact `399c3302` before updating its
runtime dependency pin. The coordinator owns this branch/pin operation; this
brief performs none. Our intended extension diff against deployed `399c3302`
remains pin-only. Preserve the complete nested dependency closure and source
behavior, changing only intended feature pins; carry runtime `4ef298b3` plus
our feature into the extension and assembled root. Never rewrite/fold any of
the four published extension commits or change another owner's refs/records.
No integration or host mutation is authorized by this preservation decision.

Codex-web's actual deployed/current-default base remains
`4c170393a96ed0a6ac2e43488d073f6fcab36132`. The unrelated `FETCH_HEAD` beginning
`7a` refers to another fetched branch and is not this feature's base.

Final whole-branch review must inventory `924c0ec2..final-runtime-head`, including
the deployed inherited `4ef298b3` commit, its published/unmerged provenance and
policy-3 consumption. Also show `4ef298b3..final-runtime-head` to isolate this
initiative's functional diff. For the extension, inventory
`8f8d8ecf..final-extension-head`, including all four consumed commits and their
published/unmerged provenance, alongside `399c3302..final-extension-head` for
our intended pin-only diff. Keep the inherited commits distinct from any
consolidation of our unpublished work. Review deployment ancestry and complete
nested lock diffs against the consumed packages, not only current default refs.

Existing contracts that constrain the design:

- `codex.Client.Subscribe` calls `resumeWatched`; `Send` and high-level
  interruption/history helpers also assume persisted conversations. None is an
  ephemeral execution primitive.
- `creationRequest` and receipts have strict readers. Schema 3 already stores
  the exact expanded `teamruntime.Preset`; preserve schemas 1/2/3 and the CLI
  evidence and journal formats.
- `acceptCreation` currently identifies replay by slug and request equality,
  allocates its own random receipt ID and immediately launches a worker. The
  new request-ID path needs stronger identity without weakening legacy replay.
- `resolveManagedCreation` currently calls `ListModels(context.Background())`
  for explicit overrides. This is an unbounded network dependency in acceptance.
- Upload catalog schema 1 rejects unknown fields. `Prepare(initial)` writes
  `prepared`, which collection may expire. Existing `pending` submissions pin
  their files even with no slug. Use that behavior without adding catalog fields.
- Receipt startup loading can retire completed receipts. Load and reconcile
  preparation mappings before allowing a referenced receipt to retire.
- CLI start uses host-private creation and slug locks, but an unrelated start
  without a receipt does not currently honor a portal-only reservation.

## Utility gate and accepted clarifications

1. **Restricted utility selected; runtime proof required.** The installed Codex 0.160.0 schema
   accepts `ephemeral`, `environments: []`, `runtimeWorkspaceRoots: []`,
   `dynamicTools: []`, explicit instructions and `outputSchema`. It exposes no
   general tool allowlist in thread/turn parameters. Its bundled
   `models-manager/models.json` gives `gpt-6-luna` the experimental tools
   `send_user_message_async` and `clock`. `core/src/tools/spec_plan.rs` adds the
   corresponding async-input and clock tools from model metadata independently
   of several feature toggles. Internal
   `ext/extension-api/src/tool_policy.rs` supports an empty `allowed_tools`
   ceiling, but no public App Server/config mapping was found. Empty MCP maps
   also merge with inherited configuration; they do not prove its removal.
   `dynamicTools: []`, read-only sandboxing, approval policy `never`, refusing
   client-side approvals, or prompt instructions alone do not satisfy the
   original literal no-tools wording. The coordinator explicitly selected pure
   clock plus immediately rejected questions as the working contract; all action
   capabilities remain forbidden. No Codex patch, model bump, shared metadata
   rewrite or separate production App Server process is authorized. Keep the
   model `gpt-6-luna` unchanged. Do not describe the result as zero tools.
2. **Acceptance validation timing: accepted by coordinator.** Accept structurally
   valid explicit model/effort overrides into the exact team snapshot using only
   local installed policy, then validate live availability in the existing
   initialization worker. This preserves the accepted settings and immediate
   acceptance, including when App Server is unavailable. Never substitute
   another model/default; expose a precise failed/retry status on unavailable
   settings. Legacy callers retain their current validation path.
3. **Cross-CLI reservations: accepted by coordinator.** Have CLI creation check
   frozen preparation/receipt reservations under its existing creation and slug
   locks, allowing only the exact portal receipt owner. It changes no CLI syntax
   or journal schema. Without this, a CLI can claim a slug after its preparation
   record is saved but before the existing creation worker writes its journal.
   The coordinator explicitly accepted this narrow guard and the shared locks;
   it is not CLI automatic naming. Do not weaken collision serialization to an
   in-process Go mutex.

Source evidence for gate 1 was read from the local Nix source
`/nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source/codex-rs/`.
The installed 0.160.0 binary generated experimental schemas into
`/tmp/automatic-session-slugs-schema` in about half a second. This proves those
schema fields exist, not runtime isolation or identity with a future assembled
package. Recheck the exact candidate package. Nix daemon access is denied in
this architect thread; no permission bypass was attempted.

### Bounded investigation of supported alternatives

`model_catalog_json` does not solve the per-thread problem on the inspected
shared App Server. `core/src/thread_manager.rs:build_models_manager` passes the
catalog when constructing its shared manager. `models-manager/src/model_info.rs`
applies context/token/base-instruction overrides, without replacing experimental
tool metadata. `core/src/session/step_settings.rs:ModelInfoOverrides` explicitly
sets `model_catalog: None` when deriving turn settings because the manager owns
its catalog. No supported per-thread capability replacement was found. A
temporary catalog path in `thread/start.config` is not sufficient evidence.
Do not rewrite shared metadata, global configuration or the selected model.

| Option | Implication and current status |
| --- | --- |
| Literal zero tools | Requires an effective empty tool allowlist. No public mechanism found in inspected 0.160.0. Codex patch/model bump is not authorized. |
| Restricted utility | Selected by coordinator and confirmed by the user. Pure clock may remain; async questions are immediately rejected without a user-facing request. Model action tools, memory/goals/hooks and project/workspace/team instruction injection are disabled. Global user policy remains trusted serving-instance policy. Exact-binary runtime proof remains a release gate. |
| Separate App Server with startup catalog | Adds process, authentication/configuration and latency ownership; exceeds the minimal shared-service helper design. Not proposed for implementation. |
| Injected naming test boundary | Allows independent preparation/browser implementation and deterministic fallback tests now. Does not complete the accepted model-naming feature. |

The restricted option is a candidate to prove, not an already verified recipe.
Available controls include empty environments/runtime roots/capability roots
and dynamic tools; read-only/never approval; disabled web search; feature
controls for shell, images, apps, plugins, code execution, delegation, goals,
memory, hooks and sleep; disabled update-plan and ordinary request-input tools;
explicit base/developer instructions and disabled project/skill injection.
Inherited MCP names must each receive supported `enabled: false` overrides;
an empty map does not clear them. Resolved config must not be logged. A removed
`tool_search` feature flag is a no-op: actual absence requires that no deferred
tools remain. A managed requirement preventing isolation must fail the utility.

Before enabling live naming, a pinned local mock-provider test must
inspect the actual model-facing tool list and attempt tool calls under hostile
synthetic prompts. Include inherited MCP/plugin configuration, hook and
instruction sentinels, empty environments, search/image/delegation attempts and
a concurrent ordinary conversation. Only pure clock and immediately rejected
question requests may remain, and no tool may execute filesystem/network or
persistent goal/memory mutations. The private sink fails immediately on question
notifications and rejects question RPC requests only when an actual request ID
exists, before ordinary UI/prompt or final-answer admission. Then the utility
falls back; no pending UI request, auto-answer timer or forwarded notification.
If this representative proof fails, this alternative also remains
blocked. No such runtime test was run during this design assignment.

### Restricted utility supplement: supported controls and fail-closed limits

This supplement is source/schema design only. Paths below are relative to the
inspected `codex-rs` source identified above. The implementer must use supported
per-thread overrides, without editing shared config or model metadata. The
public helper owns a fixed restriction policy; callers cannot provide arbitrary
config, capabilities, tools, thread identity or browser-controlled paths.

`thread/start.config` accepts dotted keys through
`app-server/src/config_manager.rs:load_with_cli_overrides`. The following is the
configuration recipe to implement and prove, not a passed isolation result.
Validate spelling/types against `core/config.schema.json` as well as the App
Server schema. The latter permits arbitrary config JSON and cannot catch a
misspelled or ineffective override.

| Boundary | Explicit request/config values | Source evidence and limit |
| --- | --- | --- |
| Filesystem and execution | Both thread and turn use `environments: []`, `runtimeWorkspaceRoots: []`; thread uses `selectedCapabilityRoots: []`, `dynamicTools: []`, `sandbox: "read-only"`, `approvalPolicy: "never"`. Disable `features.shell_tool`, `features.unified_exec`, `features.shell_snapshot`, `features.shell_snapshot_v2`, `features.deferred_executor`, `features.view_image`, `features.code_mode`, `features.code_mode_host`, `features.code_mode_only`, `features.code_mode_prewarm` and `features.code_mode_interrupt`. | `core/src/tools/spec_plan.rs:add_shell_tools`, `add_core_utility_tools` require an execution environment for shell, patch and image reading. Code-mode registration is separate. Read-only/never alone does not block reads or host-side tools. No environment IDs may be copied from the parent. |
| Search and images | `web_search: "disabled"`; `features.standalone_web_search: false`, `features.image_generation: false`. | `hosted_model_tool_specs`, `append_extension_tool_executors`, `image_generation_available` in `spec_plan.rs` exclude both hosted search and extension executors. `ext/web-search/src/extension.rs` also tests disabled mode. Do not rely on removed `search_tool`/`tool_search` flags. |
| Apps, plugins and skills | Disable `features.apps`, `features.enable_mcp_apps`, `features.plugins`, `features.remote_plugin`, `features.tool_suggest`, `features.recommended_plugins`, `features.skill_mcp_dependency_install`, `features.skill_search`; set `orchestrator.mcp.enabled: false`, `cloud.skills.enabled: false`, `skills.bundled.enabled: false`, `skills.include_instructions: false`. | `Config::plugins_config_input`, `to_mcp_config_with_loaded_plugins`, `TurnContext::apps_enabled`, `ext/skills/src/tools/mod.rs:skill_tools`. No environments plus no cloud skills excludes skill list/read. `orchestrator.mcp.enabled` is an apps boundary, **not** a universal MCP-off flag. |
| Configured MCP | Read effective static configuration once at utility start for the same private cwd and construct a nested `mcp_servers` map with `enabled: false` for **every** configured server name; preserve names as literal map keys. Do not launch MCP discovery to learn names. | `config/src/merge.rs` merges tables recursively; `config/src/mcp_types.rs` supports per-server `enabled`. An empty map preserves inherited entries; JSON null becomes an empty string in `utils/json-to-toml`, not deletion. Unreadable/malformed inventory fails closed. Operator reconfiguration follows the procedure below. |
| Delegation and persistent utilities | `agents.enabled: false`; disable `features.multi_agent`, `features.multi_agent_v2`, `features.agent_message_board`, `features.memories`, `features.external_agent_memory_import`, `features.goals`, `features.token_budget`, `features.context_management`, `features.guardian_conversation_history_tools`; set `memories.use_memories`, `memories.generate_memories`, `memories.dedicated_tools` false and `history.persistence: "none"`. | `Config::multi_agent_version`, `spec_plan.rs:collab_tools_enabled`, `app-server/src/extensions.rs`, `ext/memories/src/extension.rs`, `ext/history-notes/src/extension.rs`. `ephemeral: true` is still required; history preference is not a substitute. |
| Hooks and notifications | `features.hooks: false`, `features.plugins: false`, `notify: []`; no executor environments/plugins or bypass-hook-trust override. | `core/src/session/mod.rs` constructs hooks; `hooks/src/registry.rs` runs nonempty legacy `notify` independently of hook enablement. `hooks/src/engine/mod.rs` can retain built-in plugin hooks when plugin sources exist, so disabling the hook flag alone is insufficient. Required/host-supplied hooks that cannot be excluded make this utility unavailable. |
| Explicit instructions | Nonempty fixed `baseInstructions`; explicit fixed/empty `developerInstructions`; `project_doc_max_bytes: 0`; `include_permissions_instructions`, `include_apps_instructions`, `include_collaboration_mode_instructions`, `include_environment_context` false; `skills.include_instructions: false`. Set both `model_instructions_file` and `experimental_compact_prompt_file` to the required trusted `InstructionFile`, plus empty `compact_prompt`. | `core/src/config/mod.rs` reads and requires nonempty instruction files **before** selecting explicit base instructions. `InstructionFile` is a canonical mode-0600 regular file containing exactly `codex.EphemeralInstructionFileContent`, in private utility state outside the empty cwd and project trees; it must not be a symlink. Empty `compact_prompt` is normalized away, so the fixed file supplies that prompt. See the nonempty-file correction below. Global user instructions remain serving-instance policy. |
| Remaining utility tools | `tools.update_plan.enabled: false`, `tools.experimental_request_user_input.enabled: false`; disable `features.send_message_to_user_async`, `features.sleep_tool`, `features.current_time_reminder`. | `spec_plan.rs:add_core_utility_tools` still adds metadata-driven `clock.curr_time` and async request-input. With current-time-reminder disabled, `core/src/current_time.rs:resolve_time_provider` defaults to system `Utc::now()`. No external clock provider or sleep tool is allowed. |

The coordinator-approved trust boundary follows dev-workspace's repository-local
trusted-development-host rules. Model input and remote tool calls remain
untrusted; the local operator administers the serving instance. Preserve these
two operating limits in the public helper docs and independent review packet:

- **Global instructions:** `core/src/thread_manager.rs:instructions_for_spawn`
  attaches the shared startup `user_instructions_provider` to new roots.
  `core/src/agents_md_manager.rs:refresh` calls it and appends its result after
  project discovery, independently of `project_doc_max_bytes` and empty
  environments. `codex-home/src/instructions/mod.rs` loads global `AGENTS.md` or
  `AGENTS.override.md` and can retain last-good instructions on read errors.
  The internal `supplied_user_instructions` escape hatch has no public
  `ThreadStartParams` field. Explicit base/developer text does not suppress this
  source. This is expected trusted serving-instance user policy, not a model
  action capability. Do not require its absence, remove/rename global files,
  change Codex home, or claim that all inherited policy is suppressed. The
  fixture must retain a global policy sentinel while excluding project,
  workspace, team and skill injection. If global policy asks for an action or
  question, unavailable action tools and immediate question rejection still
  enforce the utility boundary.
- **Configuration refresh:** `app-server/src/mcp_refresh.rs:load_refresh_config`
  rebuilds active threads using latest global layers plus their session layers.
  Disabling captured MCP names does not cover a new name introduced by an
  administrator during the call. Operator MCP reconfiguration must pause/stop
  naming using the existing service/package procedures, then let fresh calls
  read the new effective configuration. Normal package transitions already stop
  workers and revalidate generation. Support one bounded call under its captured
  restriction settings; arbitrary concurrent administrator reconfiguration is
  outside that supported boundary. Do not add a config lease, repeated config
  polling, global writer lock or process framework. Deliberately changing this
  trusted policy mid-call is not a release test; unexpected action tools under
  the supported captured configuration remain a real release failure.

Read-only `config/read` with the exact private cwd and `configRequirements/read`
provide the startup inventory and managed constraints. Bound and discard their
responses without logging them. Refuse unreadable/malformed required settings,
requirement conflicts, unsupported restriction controls or unexpected action
capabilities. The release gate verifies the pinned serving binary/profile. The
helper returns a typed/static isolation error; the naming adapter
selects deterministic fallback. These errors must contain no prompt, raw config,
credential, model output or MCP command. Failure before `thread/start` has no
thread to clean up; failure afterward uses the bounded lifecycle below. A
restriction failure never retries with fewer restrictions or another model.

This clarification supersedes the earlier proposals to require absent global
policy or a proof against concurrent administrator reconfiguration. Neither is
required. Implementation proceeds with the finite recipe below; live enablement
still requires the representative exact-binary action-tool and lifecycle proof.

## Public ephemeral client boundary

Proposed additive API, with final type names owned by the implementer:

```go
type EphemeralTurnOptions struct {
    Directory       string          // trusted, canonical, private empty directory
    InstructionFile string          // trusted absolute file with provider-owned fixed bytes
    Model           string
    Effort          string
    Instructions    string
    Input           string          // text only
    OutputSchema    json.RawMessage
}
type EphemeralTurnResult struct { Text string }
func (c *Client) RunEphemeralTurn(context.Context, EphemeralTurnOptions) (EphemeralTurnResult, error)
```

Keep this utility independent of slug generation, portal types, durable sends,
thread policy and activity recording. It returns one completed final message
or an error; the caller validates application JSON and chooses fallback.
Do not expose it as a browser-selected socket/thread/cwd API.

The selected provisioning boundary is the coordinator-approved required
`InstructionFile string`, supplied explicitly by the trusted application. One
file serves both fixed-content config overrides; two paths provide no useful
distinction. Keep `Directory` empty. The application provisions and owns the
file for the whole call and bounded teardown, then handles its scratch-state
removal. The helper neither provisions/deletes it nor derives a
hidden sibling filename. An open descriptor or inline text is insufficient for
these App Server path-valued settings; a provisioning callback/config map would
add unnecessary machinery.

Require an existing canonical absolute path to a non-symlink regular file
containing exactly `codex.EphemeralInstructionFileContent`, mode 0600 and
application-user ownership, in mode-0700 private utility state outside
`Directory`. The trusted application guarantees
placement outside workspace/project trees. The helper validates these ordinary
path/type/size/content/permission constraints before connecting; it does not
scan all projects or add defenses against a hostile local administrator.
Reject missing, empty, different-content, wrongly placed or nonprivate files
without a thread/model call. Do not rewrite shared instructions/config or log
file contents. This additional field
only affects the new additive helper, not existing conversation callers.

Use a short-lived connection to the client's trusted socket with an internal
ephemeral event sink installed before starting the thread. This prevents
shared-client prompts, workspace roots, resume policy, MCP policy and activity
recording from being copied into the utility. It also gives response-loss and
cancellation a bounded connection lifetime without disrupting live sessions.
Share low-level transport code; do not build a second general client framework.
The existing public client remains concurrently usable.

Required lifecycle under the restricted contract:

1. Validate nonempty explicit model/effort, UTF-8 text, a bounded JSON object
   schema, trusted absolute directory and `InstructionFile` as specified above.
   Reject observer-only invocation.
   Directory setup belongs to the application, under mode-0700 private state,
   outside workspace/project trees, with no AGENTS/config/skill files. Keep cwd
   empty; the required instruction file is provisioned separately in private
   utility state, outside that cwd and outside project trees.
2. Connect and initialize within the caller's deadline. Start an ephemeral
   thread with explicit model, provider-model fallback disabled, explicit base
   and developer instructions, no environments or runtime workspace roots,
   no project/workspace/team/skill instruction injection and the restricted utility
   policy above. Never call `StartThreadWithSettings`, `Subscribe`, `Send`, `Resume`,
   history reads, bootstrap injection or durable submission helpers.
3. Check returned cwd, model, ephemeral identity and absent rollout path.
   Bind events to this connection generation, exact thread and exact turn.
   Notifications may precede their RPC response: retain a bounded provisional
   buffer and reconcile identity when the response arrives. Unrelated events
   and stale generations cannot complete the call.
4. Send one `turn/start` with text input, explicit effort and `outputSchema`.
   Classify question/async-delivery items before considering answer text:
   the pinned async question tool itself uses phase `final_answer`. Consume
   only ordinary completed agent-message items, not streamed partial JSON,
   commentary or async questions. Return only after both a completed final answer and matching
   successful `turn/completed`; failed/interrupted turns are errors. Bound
   output/event memory and fail closed on overflow, missing final answer or
   ambiguous final messages. Accept only the pinned protocol's documented
   final-message phase convention.
5. On cancellation, timeout, disconnect or protocol failure, never resume or
   repeat the turn. Interrupt the exact known active turn and unsubscribe from
   the exact known thread while budget remains. Close the private connection
   on every exit, including loss of `thread/start` response. Never archive or
   delete persisted threads as cleanup. A disconnect is an error; no reconnect
   adoption. Server unload timing is not a client persistence guarantee.

Reserve a small portion of the caller's hard deadline for cleanup rather than
adding another timeout after ten seconds. The naming adapter can end inference
early enough for bounded interrupt/unsubscribe; final connection close is
unconditional. Explicit early cancellation may use only the remaining original
hard deadline, with a small bounded cleanup ceiling. No detached unbounded
cleanup goroutine, prompt logging, transcript storage or submission-ledger file.

Add every outgoing call site and consumed response/notification shape to the
existing protocol corpus. Its scanner already reads non-test Go files beside
`client.go`; maintain its exact call-count check. Schema validation alone cannot
validate arbitrary `config` overrides or prove that inherited tools disappeared:
use the exact binary plus a local mock model endpoint and synthetic sentinels
to inspect actual model-facing tools/instructions before any live use.
The [official App Server guide](https://learn.chatgpt.com/docs/app-server)
describes unsubscribe and ephemeral behavior; the candidate binary/source and
generated schema remain authoritative for this experimental protocol.

### Helper/adapter implementation and protocol requirements

Keep `RunEphemeralTurn` additive in `codex/ephemeral.go`, with only the small
private event-hook seam needed in `client.go`. Copy the trusted socket/client
identity, not `ClientOptions` wholesale: no observer recorder, role/thread
instructions, runtime roots, nonblocking question policy, durable ledger,
queue/reconnect state or parent watchers. The private connection shares existing
framing and generation-bound request transport. No new App Server is launched
by production code. Require a finite context deadline and validate text/schema
size before allocating buffers. Model availability/effort checks use this
private connection and the same deadline; pagination is bounded and only the
exact requested model/effort is accepted. No provider/model fallback.

Use this finite RPC sequence on the private connection, all under the caller's
single deadline. It adds no config lease or background discovery:

| Step | Request and handling |
| --- | --- |
| Initialize | Existing `initialize`/`initialized` transport handshake with `experimentalApi: true`; install the private event/request sink before thread creation. |
| Capture restrictions | One `config/read` with `{cwd: privateDirectory, includeLayers: false}` and one `configRequirements/read` with omitted params. Read the effective `mcp_servers` names, construct literal nested per-name `enabled: false` entries, and apply every explicit restriction in the table above, including both file overrides set to validated `InstructionFile`. Do not merge the parent's thread/team config or modify the serving instance's config. |
| Check settings | Bounded `model/list` pagination verifies the exact requested model and effort. Missing settings, malformed responses or budget exhaustion return an error; do not choose substitutes. |
| Start thread | `thread/start` with `ephemeral: true`, exact model, `allowProviderModelFallback: false`, private cwd, explicit base/developer instructions, `approvalPolicy: "never"`, `sandbox: "read-only"`, empty `environments`, `runtimeWorkspaceRoots`, `selectedCapabilityRoots` and `dynamicTools`, plus the complete captured restriction config. Check returned model/cwd/ephemeral identity and absent rollout path. |
| Start turn | One `turn/start` with the exact returned thread ID, a single `{type: "text", text: input}` item, exact model/effort, output schema, and empty environments/runtime roots. Inherit the thread's restriction config; never perform a normal Send/Resume/Subscribe or tools/settings refresh. Reconcile bounded early notifications and require successful matching completion plus one final answer. |
| Finish | Immediately fail on question notifications; reject question/other server requests only when an outer RPC request ID exists, as specified below. On failure/cancel interrupt only the exact known turn; unsubscribe the exact known thread within the remaining deadline and close the private connection on every exit. Normal completion also unsubscribes/closes. |

Operators must pause/stop naming through existing service/package procedures
before MCP reconfiguration; the next fresh helper call captures the updated
configuration and disables all names then present. Document this support
condition in `codex-web/docs/reference.md`
and the owning deployment guide, and carry it into the review packet.

Before normal `readLoop` activity recording, prompt normalization, `admitPrompt`,
pending-prompt storage, broadcast, answer accumulation or timer creation, the
private utility sink classifies both notifications and server requests:

- **Async notification path:** In Codex 0.160.0,
  `core/src/tools/handlers/request_user_input_async.rs:131-154` emits started and
  completed `agentMessage` items with `delivery: "async"`, `questions`, and
  `phase: "final_answer"`; it returns `{"accepted":true}` internally to the
  model. App Server sends `item/started` and `item/completed` notifications, with
  no JSON-RPC request ID. On the first matching item with async delivery or
  nonempty questions, latch terminal utility failure immediately. Malformed
  question metadata is also a protocol failure. Do not wait for completion,
  another item, a user response or the ten-second timeout. Never classify this
  item as the naming answer, even if its text happens to be valid JSON. Send no
  fabricated error/answer envelope: the item/tool-call ID is not an RPC request
  ID, and the internal `accepted:true` cannot be retroactively rejected. The
  coordinator accepts immediate private failure, teardown and deterministic
  fallback as the selected question-rejection behavior.
- **Server-request path:** The separate `EventMsg::RequestUserInput` branch in
  `app-server/src/bespoke_event_handling.rs` sends `item/tool/requestUserInput`
  with a real outer request ID. Immediately reply with that exact ID, JSON-RPC
  error code `-32601`, and fixed text such as `Questions are unavailable for
  ephemeral utility turns`, then fail the utility. `on_request_user_input_response`
  accepts client errors and converts them internally to an empty response; the
  helper does not create a user answer. Reject other actual server requests
  with a fixed error and fail the call as an isolation/protocol violation.

For both paths, make failure irreversible even if a later final answer or
successful turn completion arrives. Start exact-turn interruption and thread
unsubscribe within the existing remaining deadline, then close the private
connection. Early question notifications arriving before the `turn/start`
response must trigger failure as soon as their private generation/thread is
bound; retain only bounded identity data needed for exact cleanup. Do not admit
their content to ordinary UI/prompt handling while reconciling an in-flight
response. No pending prompt, notice, broadcast, question persistence or timer is
created. Do not call existing `rejectUnsupported`, which adds notices and its
own five-second timeout. Malformed/oversized envelopes and uncertain identity
fail closed; never forward them to the normal client. Inability to fail promptly
or leakage into ordinary UI/persistence is a material contract failure to report,
not a reason to weaken the selected boundary.

Expose errors by stable category (isolation unavailable, unavailable settings,
protocol/server failure, canceled/deadline exceeded), preserving context
cancellation for worker shutdown. Keep detailed synthetic diagnostics in tests
only. The naming adapter lives under `portal/internal/web/`, calls this one API,
and retains the already accepted `gpt-6-luna`/`low`, 8192-byte UTF-8 boundary,
single ten-second whole budget, two-per-workspace bound and deterministic
fallback. Custom names and attachment-only requests never enter the helper.
Do not commit fallback on worker shutdown or across a changed package generation.

Extend the **existing** protocol corpus for every new literal RPC call site:
initialize/initialized as applicable, `config/read`, `configRequirements/read`,
`model/list`, ephemeral `thread/start`, text-only `turn/start`, exact-ID
`turn/interrupt` and `thread/unsubscribe`. Include the explicit empty arrays,
model fallback flag, read-only/never values, instructions, full restriction map,
effort and output schema. The source scanner counts call sites across non-test
Go files; preserve exact coverage counts instead of hiding method names in
variables. Extend consumed-shape fixtures for `ThreadStartResponse`,
`TurnStartResponse`, `item/started`, `item/completed`, `turn/completed`,
`item/tool/requestUserInput`, `serverRequest/resolved` if consumed, error envelopes
and unsubscribe response. Prove required identity/status/phase fields rather
than treating optional schema properties as guaranteed. Validate control keys
against the pinned config schema separately; keep schema fixtures and source
pins in agreement. No unrelated corpus rewrite.

The item fixtures must include `agentMessage.delivery: "async"`, nonempty
`questions`, and `phase: "final_answer"` on both started/completed notifications
without outer RPC IDs. The generated schemas make delivery/questions optional;
test ordinary messages with them absent/null as well. Separately retain the
request-ID-bearing question fixture and its error response. There is no outgoing
question-response corpus entry for the notification-only path. Include the
explicit `InstructionFile` path in both thread config overrides, with file
validation covered by local helper tests rather than schema validation alone.

### Exact-binary mock-provider release fixture

Implement `TestEphemeralProtocolIntegration` with the helper, before review,
behind the Go build tag `codex_integration` so quick tests cannot launch it.
It starts the exact candidate's Codex binary only in disposable test storage,
using a loopback mock Responses provider and private socket/home/cwd. This is a
test harness, not a new production process manager. Require
`CODEX_EPHEMERAL_TEST_BINARY` for the explicit integration invocation and fail if
it is missing or differs from the reviewed candidate. Verify `gpt-6-luna` and
`low` in actual provider requests. Do not supply a reduced model catalog, a
different model, patched binary or production credentials. The mock provider
must preserve the deployed provider's relevant tool/capability path; a custom
provider that inherently lacks image/search/apps support would be a false proof.

Use these fixture cases and evidence:

1. Seed disposable global/project AGENTS, base/developer/file instructions,
   skills, plugin/host hooks, legacy notify, MCP subprocess/HTTP endpoints,
   environment selection and memory/goal state with distinct synthetic
   sentinels. Record whether each source is eligible in a separate control
   conversation. Capture model requests in bounded test memory only; assert
   naming instructions/schema and raw-text prefix. The global user-policy
   sentinel must remain visible as expected serving-instance policy; project,
   workspace, team, skill and inherited base/developer-file sentinels and
   attachment paths/content must be absent. Include global policy requesting
   an action/question to prove that policy text cannot restore action tools or
   bypass immediate question rejection.
2. Inspect all actual model-facing tool schemas, including namespace tools,
   deferred/search catalogs and code-mode metadata. Allow only the pinned
   representations of `clock.curr_time` and async request-input; sleep,
   wrappers, skill readers and any action tool fail. Do not use a prompt saying
   "do not use tools" as evidence. Include hostile inherited feature settings
   and a managed-constraint rejection case.
3. Emit malicious synthetic function/custom calls despite their absence from
   advertised schemas: shell/exec, patch, image/file read, web/image generation,
   MCP calls/resources, apps, tool search, code-mode execution, delegation,
   memory, goals and plugin installation. Assert router rejection, zero canary
   file changes/reads, zero hook/notify/MCP process starts and zero canary network
   requests. File-read sentinels must never appear in subsequent provider input.
   Use isolated canary endpoints/storage and an egress guard allowing only the
   mock provider; normal inference transport is outside the forbidden action
   network boundary. Test actual server dispatch; rejecting a notification in
   the client after a tool executes is insufficient.
4. Exercise both real pinned question paths. The metadata-driven async tool must
   produce its started/completed notification with async delivery/questions and
   internal `accepted:true`; assert immediate helper failure from the first
   matching notification, no fabricated RPC reply and deterministic fallback.
   Separately exercise the `EventMsg::RequestUserInput` request path and assert
   `-32601` only for its real outer request ID. In both cases assert exact private
   teardown, zero normal prompts/notices/timers/UI events or persisted questions,
   and no later successful result. Include an async item whose phase/text could
   otherwise resemble the final naming answer, and one arriving before the
   turn-start response. Exercise clock then ordinary completion and bounded
   clock/question loops. No background goal or memory extraction may result.
   Because the ordinary request-input tool is disabled by production restrictions,
   use a separately labelled exact-binary control to produce its genuine RPC
   request and exercise the same private sink/teardown path. Any test-only
   enablement needed for that control is not a public helper option and must not
   be counted as evidence of the production model-facing tool set. The async
   notification case runs under the actual production restriction config.
5. Verify the startup inventory disables all configured MCP names, including
   names containing dots, and that unreadable/malformed config or conflicting
   restrictions fail before inference. Between bounded calls, pause/stop the
   worker, change the synthetic MCP config, then start a fresh call and verify
   the new name is also disabled. Cover package-generation cancellation with
   the existing worker lifecycle tests. Do not require resilience against an
   administrator deliberately reconfiguring the server mid-call; that is outside
   the documented operating procedure. Actual model tool dispatch must remain
   blocked under the supported configuration, before any action executes.
6. Cover notification-before-response, canceled start response, timeout during
   config/model discovery and inference, lost connection, malformed/ambiguous
   completion, stale IDs and pending question at cancellation. Verify no
   persisted thread/rollout, submission ledger, goal/memory mutation, hook output
   or utility prompt in persistent stores/logs, allowing only explicitly
   inventoried ordinary service metadata. Keep an ordinary conversation active
   and verify its subscriptions/requests/settings still work unchanged.

Known quick tests use a fake transport/provider to cover the same Go lifecycle,
both question paths, deadline and adapter fallback, plus required `InstructionFile`
validation and equal file overrides. Those are not the
binary proof. After quick checks, committed implementation and independent
review, a fresh watcher runs the integration fixture and exact protocol schema
validation before live naming/deployment. Record binary/package/model identities,
tool-name-only assertions, canary counts and pass/fail summaries without raw
prompts/config. Unexpected model-facing action tools, workspace/team instruction
injection, question admission or side effects in the supported configuration
fail the release gate and must be reported. Retained trusted global user policy
and the documented operator-reconfiguration procedure do not fail this gate.

## Preparation API and immutable identity

`POST /sessions` accepts the existing form fields plus `clientRequestId`.
Require a canonical random UUID for the new browser flow. No ID plus an
explicit name continues through legacy `createSession`; no ID plus no name is
invalid. Keep existing form/body, UTF-8, attachment-count, date, origin and
authorization limits. Reject ambiguous duplicate scalar fields.

For a new ID, freeze these values before any naming call:

- Workspace identity and validated request ID; accepted time and creation date.
- Exact raw textual prompt bytes, ordered attachment IDs and upload scope.
  Keep text used for naming separate from the attachment-expanded CLI goal.
- Optional custom name with existing explicit-name normalization/syntax.
- Submitted team/catalog/model/effort values and field-presence semantics.
- Deep copy of the resolved preset, including instructions, purposes, access,
  member identities and lead settings. A catalog digest alone is insufficient.
- A random 64-hex receipt ID allocated now, and preparation attempt 1.
- SHA-256 of a versioned canonical encoding of all submitted input; a separate
  digest may bind the resolved snapshot. This is an integrity/replay key, not a
  password hash. No prompt text or model output in operational logs.

Replaying an ID first compares its input digest to the original submission,
before resolving the current team catalog, checking current uploads or naming.
Same input returns the saved operation; differing input is HTTP 409, including
changes only to raw whitespace, attachment order, scope or date. Two different
IDs with the same prompt are separate operations. A replay after catalog change
uses the accepted snapshot; the unaccepted stale-draft catalog warning remains.

Accepted JSON is HTTP 202 with request ID, immutable receipt ID, attempt,
`url: /creations/<id>/`, state/phase/timestamps and the accepted raw prompt.
Non-JSON form submission gets a 303 to the same preparation URL. Naming,
App Server connection, tmux, Git and session scans stay out of acceptance.
Disk/capacity errors before acceptance remain errors; uncertain writes are
recovered with the same request ID, never compensated by discarding identity.

`GET /creations/<id>/` server-renders the accepted prompt and progress controls.
`GET /api/session-creations/<id>` returns status with optional final slug and
canonical URL. `POST /api/session-creations/<id>/retry` accepts only receipt ID
and expected attempt, under existing exact-origin and generation guards.
Malformed/traversal/encoded-separator paths fail closed. URLs are constructed
from validated identifiers; no browser-supplied redirect target.

Use states `accepting`, `running`, `paused`, `failed`, `handed_off` and a compact
terminal mapping, with stable machine phase values separate from visible copy.
Failed/paused retry increments the preparation attempt before launching once.
Running retry replays status; stale token/attempt is 409. After handoff, the
preparation endpoint delegates to the exact receipt's current attempt checks
and projects its progress. Do not use a stale preparation attempt to restart a
newer ordinary creation attempt. A POST replay never implicitly retries failure.

The preparation URL remains valid through handoff. Redirect the browser to the
canonical session page only after a matching receipt is durably installed; that
page may still show normal initialization progress. Preserve the original
accepted timestamp in preparation progress. A name conflict must not redirect
to an unrelated session as though this request created it.

## Private records, upload transaction and recovery

Store version-1 preparations in a separate mode-0700 directory beneath
`operationStore.directory`, with mode-0600 files named by validated request IDs.
Use strict shape/value readers, bounded records, atomic rename, file fsync and
parent-directory fsync, following existing store code. Do not add fields to
receipt, manifest, journal, runtime-authority or upload-catalog schemas.

Each unfinished record contains the full immutable snapshot and mutable attempt,
phase, status, timestamps, naming outcome/base and optional final reservation.
The reservation includes final slug, predetermined receipt ID, exact ordinary
creation request, exact preset and captured deletion-history epoch. Bounds must
account for JSON expansion of prompts, attachment-expanded goals and presets;
do not apply the 256-KiB lifecycle-operation-store limit to these records.

Admission permits at most 512 unfinished records and 10,000 eventual compact
mappings per workspace. Reserve mapping capacity at admission too
(`terminal mappings + admitted unfinished <= 10,000`), so finishing cannot
become impossible at the terminal limit. Replays bypass new-admission limits.
Never evict unfinished work or mappings to admit a new ID. Admission failure
does not create uploads, naming calls or sessions. Define record/aggregate byte
bounds alongside count bounds and retain space for updates/compaction.

Upload ownership uses existing schema-1 submission fields: a reserved initial
submission with `Attempt` in a private request-ID namespace such as
`preparation:<uuid>` and `State: pending`, plus the full preparation record.
Do not add a new field to `Scope`/catalog: old strict readers would reject it.
The ownership check must run inside the catalog transaction for every mutation,
not merely in an HTTP resolver that can race a later claim. Claims are exclusive
for a scope; a second ID, legacy initial preparation or conversation submission
cannot reuse it. Replaying the same ID must also match exact text/files.

Acceptance under the transition lock and `uploadCreationMu`:

1. Validate input, capacity, local team snapshot and ready attachments; stage a
   durable `accepting` record containing the complete snapshot and receipt ID.
2. Atomically claim its upload scope and write the pending initial submission
   in the existing upload catalog. Generate and save the exact attachment wire
   goal; raw text remains separate. With no selected attachments, do not claim
   an otherwise unused empty draft or create an upload submission.
3. Persist `running` acceptance and only then acknowledge and start naming.
   Keep acceptance independent of the HTTP connection after this durable point.

A crash before step 2 has not accepted the request. A recovered `accepting`
record must validate/finish the same intent before naming; if an older collector
expired unclaimed files meanwhile, report failure without pretending they were
accepted. A crash after step 2 is recoverable from the complete intent plus its
pending claim; no new ID or text/team resolution. Failure after any durable
intent write keeps that identity available for an uncertain-response retry.

Startup and collection reconcile accepting/prepared/handed-off records before
upload expiry and receipt retirement. A pending owner whose preparation needs
repair is retained and reported, never guessed abandoned. Existing older
collectors retain pending submissions without knowing the new request ID.
Do not treat successful age-based collection as authority to release a claim.
Reads may show accepted files; mutating accepted scopes is refused until they
have ordinary session ownership. `Create`, `Append`, `Complete`, `Delete` and
all `Prepare` entry points need transactional checks. Returning an already
existing upload identity read-only is safe; it must not allow further writes.

On handoff, bind the same initial submission to final slug/epoch; when ordinary
creation proves the thread and initial goal, transfer to its existing
slug/thread/epoch ownership through `BindCreation`/`AdoptInitial`. Do not release
pending retention before the replacement ownership is durable. Existing sent,
forked and deletion retention continues unchanged. Old-reader compatibility
means preservation/collection compatibility, not teaching old UI code how to
resume a preparation.

## Naming and destination reservation

For nonempty textual automatic requests use exactly `gpt-6-luna`, effort `low`.
Never use development-team settings for the utility. Start a single ten-second
hard budget when the naming attempt begins, before semaphore admission,
connection and model lookup. Permit two simultaneous utility calls per
workspace; queue time consumes that same budget. No second inference attempt
inside a naming attempt. Shutdown cancellation pauses the preparation; it must
not commit a fallback merely because the server is stopping.

Send at most 8192 bytes of the raw prompt, cut before an incomplete UTF-8 rune,
with a fixed naming instruction and JSON output schema requiring only `name`.
Do not include filename lists, expanded attachment paths, file contents, team
instructions or workspace instructions. Require valid single-object JSON,
one name field, lowercase ASCII kebab syntax, 3–6 tokens and at most 48 bytes;
reject extra output, prose, punctuation, empty names and invalid Unicode.

Unavailable model/effort, timeout, invalid output or utility failure falls back
deterministically. Attachment-only input skips inference. Fallback uses the
first nonempty raw-text line, Unicode lowercase and diacritic decomposition,
removes combining marks, selects up to six ASCII alphanumeric words, joins with
hyphens and keeps whole words within 48 bytes. If no whole useful word fits,
use `session`. Nondecomposing non-ASCII letters become separators; do not invent
language-dependent transliterations. A small Unicode normalization dependency
is preferable to an incomplete accent table; include its module/vendor pin.
Specify this behavior in fixtures, including an overlong first token.

Persist the selected generated base and outcome before attempting reservation.
An ordinary retry with a saved base does not run naming again. A crash before
the base is durably saved may repeat the bounded naming attempt; no destination
has been reserved yet. Persisted final slug is immutable even if a later suffix
becomes free. Log duration and bounded outcome codes only.

Serialize candidate allocation with ordinary creation acceptance and CLI
creation: transition shared lock with generation check, upload coordination
when needed, portal operation mutex, then the existing per-slug creation lock
and slug lock. Use a narrow common reservation routine so locked and unlocked
helpers cannot recursively acquire the same mutex/lock. Never hold a slug or
operation lock while awaiting model inference. Define and test lock order
against collection, lifecycle commands and the Ruby worker.

Candidates exclude active/archived tracking, worktrees, any extant receipt,
other frozen preparations, lifecycle journals, creation/start/fork journals,
runtime authority and retained team/runtime state. Unknown or unreadable
occupancy fails closed; it is not an invitation to skip arbitrary names forever.
A busy candidate lock is retriable, not proof the name is available. Automatic
collisions use `base`, `base-2`, `base-3`, etc.; trim the base on a word boundary
to keep the suffix inside 48 bytes and avoid an empty prefix. Custom names
preserve existing syntax and collision errors; no automatic suffixing.

Under these locks, save final slug, receipt ID, epoch and exact handoff request
to the preparation before installing its ordinary receipt. The accepted CLI guard
recognizes this durable reservation and refuses an unrelated first creation;
the exact receipt owner may continue. It must also cover destination creation
by forks and other new-session
paths, without scanning completed mappings or changing their naming semantics.

Refactor receipt acceptance into a narrow internal variant accepting the
predetermined ID and expected deletion epoch. Validate the ID. Existing receipt
replay succeeds only if ID, workspace, request, resolved preset and epoch all
match. A different receipt with identical prompt/name is a conflict. Never call
retirement first and silently replace such a receipt. Legacy acceptance keeps
its current equality replay. Installation and worker registration happen once;
the preparation is marked handed off after the receipt write. An already
existing paused receipt is status/recovery, not a reason to launch a second worker.

Every mutation after a wait reacquires the transition lock and validates the
current package identity. Persisted snapshots survive compatible forward
updates, but work started by a superseded process does not mutate state.
Inference may run without holding the transition lock; its result can be
committed only after revalidation. Server shutdown cancels and joins tracked
workers and leaves running preparations paused for explicit retry.

## Crash and replay matrix

| Durable boundary / interruption | Recovery authority and action |
| --- | --- |
| Intent saved; upload claim absent | Same intent/ID; finish validation and claim before acceptance or report pre-acceptance failure |
| Upload claim saved; final acceptance response absent | Complete snapshot plus matching pending claim; finish acceptance, return same URL/receipt ID |
| Accepted; naming outcome absent | Pause on restart; retry same snapshot within a new bounded naming attempt |
| Base saved; no reservation | Reuse base; serialize candidate allocation |
| Slug/receipt ID saved; receipt absent | Prove exclusive reservation, unchanged epoch and absence of other effects; install that exact receipt |
| Receipt saved; preparation handoff marker absent | Verify exact receipt ID/request/preset/epoch; adopt its status, never allocate another ID |
| Worker ready; mapping not compacted | Prove ready through existing exact receipt evidence and upload binding; compact before receipt retirement |
| Compact mapping; receipt evicted | Return recorded destination/outcome, never create again; deletion does not forget request identity |
| Same slug deleted/recreated, or receipt replaced | Never adopt replacement; retain terminal/gone/conflict result for the original ID |
| Missing/contradictory evidence | Pause or conflict for diagnosis; do not infer success from equal prompt text or recreate blindly |

Compact only after the ordinary operation is terminal and exact ownership is
known. Preserve immutable request ID, input digest/version, receipt ID, slug,
epoch and terminal outcome in the same atomic record replacement. Keep full
snapshots while initialization can still need replay, not merely until a slug
has been chosen. Hook compaction before receipt eviction, including startup
retirement; a compaction failure retains the receipt. Replaying a terminal
request may return its saved destination after deletion, but cannot initialize
anything there or claim that a replacement session belongs to it.

## Browser boundary

Extend only the New session draft with a verified-persisted random request ID,
full submission snapshot, upload scope/selection and submission state. Reuse the
existing draft and upload components. Leave plan/fork draft keys and behavior
unchanged. Migrate old unsubmitted drafts by assigning an ID before their first
submission. Verify storage writes/readback; the present optional-storage helper
can report success with no storage and is insufficient for replay safety.

Keep the same ID/date/prompt/team/attachments through network failure, reload,
double-click and a lost acceptance response. Before an uncertain retry,
GET status for that ID; if present, follow its accepted operation without
rebuilding settings from current form options. If absent, resubmit the exact
snapshot with that ID. A 404 alone does not prove an older concurrent POST
cannot still accept, so it does not authorize editing/reusing that ID. Editing
a definitely unsubmitted draft may allocate a new ID; after uncertain submission
recover the previous operation before offering a distinct new request.

Keep uploads locked while outcome is uncertain. Distinct tabs currently share
one localStorage upload scope; bind a draft's scope to its request identity and
allocate a fresh scope for a distinct draft, rather than silently sharing file
ownership. The server still enforces exclusive ownership. Clear the submitted
draft/scope pointer only after verified acceptance and verified browser storage
update; a storage failure leaves recoverable state.

Remove `required` from the optional custom-name control; move it and advanced
model settings under expanded options. Preserve its maxlength and legacy syntax.
Keep CLI preview explicitly named and independent: no new CLI automatic-name
behavior. Validate both allowed preparation URLs and canonical session URLs
strictly before navigation. Display prompt/error/model-derived text with text
nodes/escaped templates. A raw `<script>` in the prompt remains literal.
The coordinator applies the user-facing writing skill to final visible copy.

## Compatibility, deployment and recovery

No SQL changes, seeds, API client generation, Terraform behavior, service wire
protocol, host module option or coordinated node update is involved. The Go
helper and preparation HTTP endpoints are additive. Existing explicit-name
portal requests without a request ID, forks, plan creation and CLI arguments
retain their contracts. New and old frontends must fail/replay safely when one
side lacks the new endpoint; never fall back to a name-only POST after an
uncertain request-ID submission.

Old readers retain separate preparation files and understand pending upload
submissions. Standard schema-3 receipts remain readable by the immediately
preceding inspected package; this does not promise compatibility with packages
before expanded team snapshots. Unfinished pre-slug work has no old recovery UI
and pauses until compatible preparation code returns. Test this using isolated
old-source reader/collector fixtures, not a live profile downgrade. Earlier
receipt retirement must not cause the newer service to recreate a completed
operation; missing exact proof fails closed.

The old-reader fixture's source baseline
`924c0ec28c41dd8b56aaf17f2212b302ca614899` is byte-identical to deployed predecessor
`4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4` for the entire
`portal/internal/uploads/` subtree, `libexec/dev-session`, `portal/go.mod` and
`portal/go.sum`, as verified by the coordinator. That establishes predecessor
source equivalence only for those fixture inputs. It does not establish whole
package equivalence or executed compatibility; the old-reader fixture still
requires its post-review run.

Older CLI code does not know these reservations. Compatibility guarantees safe
preservation and conflict detection, not prevention of every collision caused
by that old code. A resumed preparation must reject an older-created competing
destination, even when its name/prompt matches. Do not adopt or rename it.
Pending-upload mutation behavior also needs an actual old-source fixture:
exercise old draft delete/prepare/create against the reserved catalog and
verify selected accepted files remain intact. Do not infer mutation safety
from the separate fact that age-based collection pins pending files.
At the inspected base, `uploads.Backend.Delete` explicitly refuses any file
referenced by `pending` or `queued`, while `Append` requires an `uploading`
file. That supports the proposed representation but is not executed fixture
evidence. Old `Prepare`/`Create` may still add competing records to a draft:
new recovery must validate exact ownership and refuse contradictions rather
than adopting an old-created session or reassigning its scope.

Pin in order: codex-web commit/pseudo-version and vendor hash → dev-workspace
input → vpsfree-dev-workspace input → assembled workspace input. Check complete
nested lock diffs and retain unrelated Codex/llm-agents/nixpkgs inputs. A solution
to gate 1 that needs a Codex change expands this order and requires an amended
plan through the coordinator. Host configuration remains unchanged unless
inspection proves a new requirement.

The runtime pin must include preserved `4ef298b3`; extension and assembled root
pins must retain all four exact extension ancestors through `399c3302`. Assess
the host-migration trigger against deployed extension `399c3302` plus runtime
`4ef298b3`, not old defaults `8f8d8ecf` plus `924c0ec2`. Preserving those already
consumed changes and schema 1/policy 3 does not introduce a new host-state
compatibility transition or newly trigger the extension's host-migration VM.
The inherited four-commit extension diff is part of whole-branch review, but
is not an incoming change relative to this installed predecessor.

### Host-migration applicability for runtime `51dca869`

**Decision: no new `.#host-migration-test` trigger for this incoming feature
delta.** This source assessment compares deployed extension
`399c33023a568a8d7a21e4e4df52829628720a28` / runtime
`4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4` with runtime
`51dca869fe50c20b6669d4770856fca0971fc9c2` and the prepared extension pin diff.
That extension diff changes only `flake.nix`/`flake.lock`: runtime to `51dca869`
and nested codex-web to `ca0f3bc980ca99454d000761aeee37b4b9bbafc3`, retaining
the other nodes and inherited extension source. The exported runtime contract
is coordinator-confirmed unchanged, including cluster schema 1, policy 3 and
authority policy 1; the source contract and host-path definitions also have no
diff. The decision additionally rests on the private-state boundaries below,
not only matching contract numbers.

- **Move and rewrite inventory.** Extension
  [bin/vpsfree-dev-workspace-migrate](../../worktrees/2026-10-03-automatic-session-slugs/vpsfree-dev-workspace/bin/vpsfree-dev-workspace-migrate)
  `migration_pairs` (line 519) moves the whole user config/state/runtime roots.
  `fingerprint` (1940) recursively includes every entry's relative path, type,
  mode, owner and file bytes; `apply_moves` (586) verifies that inventory and
  renames the tree. It does not enumerate allowed portal-state subdirectories.
  `rewrite_candidates` (800), `rewrite_path_allowed?` (904) and
  `rewrite_machine_state` (1029) restrict content handling to runtime authority
  JSON, registry JSON and active/archived `portal.yml`. Socket fields are
  rewritten; the registry is preserved. Preparation files, compact mappings,
  receipts and upload catalogs are not rewritten or schema-validated by this
  helper. They are included in the generic tree move without changing bytes.
  Its 1 MiB rewrite limit therefore does not become a preparation-record limit.
- **Private storage and identity.** Runtime
  [operation_store.go](../../worktrees/2026-10-03-automatic-session-slugs/dev-workspace/portal/internal/web/operation_store.go)
  `newLifecycleOperationStore` (34) and unchanged
  [userstate/paths.go](../../worktrees/2026-10-03-automatic-session-slugs/dev-workspace/portal/internal/userstate/paths.go)
  derive `<user-state-root>/portal/<workspace-basename>-<workspace-hash>/`.
  [preparation_store.go](../../worktrees/2026-10-03-automatic-session-slugs/dev-workspace/portal/internal/web/preparation_store.go)
  (58, 94, 110) places schema-1 records in `session-preparations/` and terminal
  mappings in `session-preparation-mappings/` there, with private directories
  and regular JSON files. Workspace identity is the unchanged checkout path;
  IDs, slug, epoch and digests do not encode the state-root namespace. Byte
  preservation retains their input/snapshot digest bindings. Compaction in
  `preparation.go:653` removes the full snapshot/handoff before receipt
  retirement; it adds no authority or host-path field. The frozen team snapshot
  uses the existing `teamruntime.Preset` value format (model, effort, access and
  instruction text), already consumed by receipt schema 3's `directTeam`.
  `creation_store.go` changes only the pre-retirement compaction call.
- **Upload ownership.** [web/uploads.go](../../worktrees/2026-10-03-automatic-session-slugs/dev-workspace/portal/internal/web/uploads.go)
  `initUploads` (22) retains the sibling `uploads/` tree. In
  [uploads/store.go](../../worktrees/2026-10-03-automatic-session-slugs/dev-workspace/portal/internal/uploads/store.go)
  (82, 377, 812, 882, 900), catalog schema 1 and `files/<id>/file<extension>`
  remain unchanged. The new claim uses existing submission fields:
  `initial`, `preparation:<request-id>`, `pending`, scope/file IDs and wire text;
  binding later adds the existing slug/epoch/thread values. Exclusive claim and
  mutation checks change application semantics, not migration discovery,
  catalog schema or path layout. Their bytes and upload files move together.
- **Locks and quiescence.** `session/authority.go:51` reuses the CLI's existing
  creation/slug lock names; migration's `lock_mutation_files` (716) already
  covers `authority/*.lock` and the transition lock. No authority schema or
  socket identity changed. The namespace runbook still requires stopped writers
  and frozen inventory. `web/server.go:595` cancels/joins preparation workers
  before final pause records. Naming scratch state under the same portal tree
  (`session_namer.go`) introduces no external persistent host path.

Scope of this conclusion: generic preservation is not proof of pending prompt
replay after arbitrary state-root relocation. Upload wire text already contains
absolute file paths at deployed `4ef298b3`; its immutable receipt goals and the
new preparation snapshot preserve that same text. Migration does not rewrite
those fields. This feature rollout keeps the existing namespace, user-state
root and workspace path, and adds no relocation guarantee or newly required
rewrite. No incoming namespace/host-state compatibility change was found.

This is a source-based applicability decision, not an executed migration or
independent-review result. Normal packaged Ruby migration and host-path contract
checks remain required, as do the feature's post-review compatibility and
exact-binary isolation gates. Generation revalidation, maintenance/transition
holds, cluster/socket ownership and refusal checks remain enforced. Reassess
if the final pin changes these boundaries; an actual new migration/host-state
change would require the post-review VM through a watcher. No host mutation or
default-branch integration is authorized by this assessment.

### Application deployment and recovery

Build/review the assembled feature package and deploy from the workspace
feature worktree using `workspace-host switch --source "$PWD"`, through the
authorized rollout workflow. Record exact refs/package paths and canary
evidence. Readiness, deployment and default-branch integration are separate;
no merge or lifecycle action is authorized by this brief.

Switches are forward-only. Record the previous package as a source/behavior
reference; recovery selects a **newer** package containing the previous behavior
and preserving the forward state readers. Never invoke `workspace-host rollback`
or switch to an earlier profile. Repeating the same interrupted switch uses its
normal recovery. Do not discard preparation/upload state to unblock deployment.
No session archive, deletion, stop, finalization or delayed cleanup is part of
this initiative's design handoff.

## Acceptance criteria and verification brief

The implementer must demonstrate:

1. Acceptance returns durably before blocked naming/model lookup; original raw
   prompt and exact team snapshot are visible immediately and survive restart.
2. Automatic valid output, missing model, invalid/oversized JSON, malformed name,
   timeout, queue saturation, Unicode 8-KiB boundary and attachment-only fallback
   obey the exact naming contract. At most two model calls run per workspace.
3. Duplicate-ID replay, changed-input conflicts, distinct IDs with identical
   text, midnight/date preservation, deterministic suffixes and custom-name
   conflicts work across concurrent requests and real CLI lock contention.
4. Fault injection at every table boundary produces one destination/receipt and
   preserves uploads. It never adopts a different equal-content receipt.
   Capacity rejection leaves all earlier replay identities recoverable.
5. New code rejects all accepted-scope mutations; old-source collection retains
   pending pre-slug files. Ownership transfers exactly once, with no collection
   window or broad deletion by goal digest.
6. The ephemeral helper uses no persistent resume/send/history path, excludes
   action tools and project/workspace/team instruction injection, retains trusted
   global user policy, permits only pure clock plus
   immediately failed async question notifications and rejected question RPCs,
   handles early notifications and
   cancellation/disconnect, leaves no transcript/submission ledger, and does
   not disturb another active client call. The exact-binary fixture must prove
   this boundary and record the operator MCP-reconfiguration procedure.
7. Browser reload, lost response, storage failure, multi-tab attachment scopes,
   catalog change, double-click, retry tokens, XSS and URL validation all work;
   legacy explicit-name, fork and plan flows retain existing tests.
8. Superseded generations cannot commit naming/reservation/upload changes; the
   exact final candidate passes protocol checks and deployment canaries.

Quick checks below are **planned, not executed**. Commands run from each named
repository. Use its Nix-derived build environment; these flakes declare no
`devShell`. The commands below select package/check derivations to obtain their
build environments; they do not refer to an explicit devShell API.
These package-derived shells export `GOFLAGS=-mod=vendor`, but source worktrees
have no vendor tree. Source Go commands below explicitly use `-mod=readonly`;
packaged Nix checks retain their generated vendor tree and remain unchanged.
See the [Go module-mode note](../../notes/dev-workspace/2026-10-03-package-shell-go-modules.md).
Preparing an uncached Nix environment/build belongs to a fresh authorized
Luna/low verification watcher. Once the environment is ready, focused checks
may run inline if known quick. Proposed new test names use the listed prefixes.
Keep `PORTAL_BROWSER_TEST` unset for pre-review checks. The new pure preparation
Node suite must run through its registered entry point once the implementer
confirms it; its exact filename/selector is pending the frontend report and
registration barrier, not an established command below.

```sh
# codex-web: preparation of this Nix environment may require a watcher
nix develop .#checks.x86_64-linux.default -c go test -mod=readonly ./codex -run '^TestEphemeral' -count=1
nix develop .#checks.x86_64-linux.default -c python3 test/codex_protocol_contract.py --coverage-only codex/client.go

# dev-workspace, from repository root
nix develop .#packages.x86_64-linux.dev-workspace -c env -u PORTAL_BROWSER_TEST sh -c 'cd portal && go test -mod=readonly ./internal/web ./internal/uploads -run "^Test(SessionPreparation|SessionName|PreparationUpload)" -count=1'
nix develop .#packages.x86_64-linux.dev-workspace -c node --check portal/internal/web/static/app.js
nix develop .#packages.x86_64-linux.dev-workspace -c node --check portal/internal/web/static/creation.js
nix develop .#packages.x86_64-linux.dev-workspace -c env -u PORTAL_BROWSER_TEST sh -c 'cd portal && go test -mod=readonly ./internal/web -run "^TestShippedBrowserClientMatchesSessionAPI$" -count=1'
nix develop .#packages.x86_64-linux.dev-workspace -c ruby test/dev_session_test.rb --name '/portal_start_persists_receipt_bound|portal_creation_retry|preparation_reservation/'
git diff --check
```

The existing `browser_contract_test.cjs` is an ordinary Node contract whose
normal entry point is `TestShippedBrowserClientMatchesSessionAPI` in
`server_test.go`. That Go harness supplies the HTTP fixture URL, allowed origin
and generated module path. Direct `node --test` without those arguments is not
its normal standalone entry point. `team_settings_browser_test.cjs` imports
`@playwright/test` and launches Chromium; `question_browser_test.go` registers
it under `TestQuestionBrowser`, gated by `PORTAL_BROWSER_TEST=1`. It belongs to
post-review live integration checks, not pre-review Node unit checks.

Register the new pure preparation Node suite explicitly in its harness/package
entry and use the implementer's confirmed command. Do not claim a passing
`-run` check if it selected zero tests or a required contract skipped for missing
Node. Add focused crash/fault tests rather than assertions merely mirroring
private helper implementation.

After committed changes, quick verification and mandatory independent review,
fresh utility watchers run the longer checks (not the architect):

```sh
# In codex-web and dev-workspace, separately
nix flake check --print-build-logs

# Race/regression checks; each command from its owning repository
nix develop .#checks.x86_64-linux.default -c go test -mod=readonly -race ./codex -count=1
nix develop .#packages.x86_64-linux.dev-workspace -c sh -c 'cd portal && go test -mod=readonly -race ./internal/web ./internal/uploads ./internal/session -count=1'

# Dependency/deployment layers, in their own feature worktrees
nix flake check --print-build-logs
nix build --no-link --print-build-logs .#packages.x86_64-linux.default
```

Exact protocol and browser entry commands after the watcher resolves tools
from the selected candidate/Nix environment (variables are prerequisites,
not permission to use arbitrary ambient versions):

```sh
# CODEX_BIN is the exact assembled candidate's bundled Codex executable.
# SCHEMA_DIR is a new private temporary directory.
"$CODEX_BIN" app-server generate-json-schema --experimental --out "$SCHEMA_DIR"
python3 "$CODEX_WEB_SOURCE/test/codex_protocol_contract.py" "$SCHEMA_DIR" "$CODEX_WEB_SOURCE/codex/client.go"

# From dev-workspace root; these variables match existing test documentation.
# PLAYWRIGHT_MODULE: Nix Playwright module; CHROMIUM_EXECUTABLE: matching browser.
CODEX_WEB_SOURCE="$CODEX_WEB_SOURCE" PLAYWRIGHT_MODULE="$PLAYWRIGHT_MODULE" CHROMIUM_EXECUTABLE="$CHROMIUM_EXECUTABLE" node test/creation_browser.cjs

# From dev-workspace/portal, only after mandatory review, in the prepared Nix
# environment with Node, Playwright modules and PLAYWRIGHT_BROWSERS_PATH.
PORTAL_BROWSER_TEST=1 go test -mod=readonly ./internal/web -run '^TestQuestionBrowser$/^team_settings_browser_test[.]cjs$' -count=1

# Proposed new integration test, implemented before this command is usable:
# synthetic prompts/private mock provider; no production prompt capture.
CODEX_EPHEMERAL_TEST_BINARY="$CODEX_BIN" go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeralProtocolIntegration$' -count=1
```

The last command runs from codex-web and must cover the real model-facing tool
list and instruction sentinels with a local mock provider. Only after that
passes should an authorized live canary use `gpt-6-luna`/low and a harmless
synthetic task. Live portal canaries cover automatic/custom creation, response
loss/retry and upload retention using explicitly designated test sessions.
Do not archive/delete any canary without explicit direction for that session.

Independent review receives complete base-to-head series, final diffs, every
new private state shape, crash matrix and old-reader fixtures. Require explicit
whole-branch history and migration conclusions: no database migrations, new
isolated preparation format, unchanged existing receipt/journal/catalog schemas.
For runtime, include both `924c0ec2..final-head` with inherited deployed `4ef298b3`
and our own `4ef298b3..final-head` diff. For the extension, include
`8f8d8ecf..final-head` with the four exact consumed commits and
`399c3302..final-head` for our pin-only change. Record the narrow old-reader
source equivalence, pending fixture execution, policy-3 preservation, complete
consumed extension ancestry and the actual host-migration-VM applicability
decision against deployed `399c3302` plus `4ef298b3`.
Review general, architecture and compatibility/risk boundaries, especially
gate 1 and cross-language reservation ownership. No default-branch integration
or deployment-readiness claim before those results are reconciled.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/>

## Accepted remediation design: R1 and R2

Status: the completed independent review in [review.md](review.md) records R1
and R2 as Important findings. The coordinator accepted this bounded design and
assigned implementation to implementer0, including the stopped-worker
clarification below. Implementation is active; completed fixes, verification
and renewed independent review remain pending. This document does not assert
that the active implementation conforms or that either finding is resolved.

All source traces and line references in this supplement describe the reviewed
predecessor runtime `edcfc18f2fdc3bdebfec7089e2bd79b2d9b918b1`, with provider
`ca0f3bc9`; they are not current implementation line numbers. The coordinator
owns tracking, finding reconciliation, new review heads and release gates.
This reconciliation edits only the two design documents and runs no tests.

### Published preparation writes whose durability is uncertain

Source trace: `portal/internal/web/preparation_store.go:322` publishes the
renamed JSON into `s.preparations` before its directory sync. In
`preparation.go:240,318`, an error after publishing `running/naming` prevents
worker launch; an identical POST later returns the running record without
launching it because only `accepting` enters admission completion. Explicit
retry (`preparation.go:509`) also returns a running record unchanged. Collector
reconciliation (`preparation.go:597`, `uploads.go:210`) can repair upload claims
but does not dispatch that missing worker. Startup turns running into paused,
so a restart can make it retryable; same-process recovery remains incomplete.
The accepting-write failure is also significant: an already-published intent
must be made durable before its replay acquires an upload claim. A later write
failure must not erase a published base, reservation, receipt ID or attempt.

Accepted bounded repair, retaining preparation/catalog/receipt schemas:

1. Keep a renamed record reserved in memory, but distinguish **published** from
   **durably confirmed**. Add private per-request unconfirmed-write bookkeeping
   to the preparation store, set at publication and cleared only after all
   required directory syncs succeed. No generic filesystem framework or new
   persisted state machine is needed. Moving the map assignment after `Sync`
   alone is insufficient: a same-process replay must still recognize the
   published file and its predetermined receipt instead of allocating another.
2. Before another transition, upload claim, success response or retirement for
   that request, confirm the exact published record and required parent syncs
   under the existing transition/upload/operation locks. Preserve the most
   recently published input, preset, base, handoff and attempt. Repeated I/O
   failure remains recoverable and returns an explicit temporary persistence
   error; it must not produce an accepted/running success response, replacement
   identity or a compensating write assembled from stale memory. Apply this to
   the completed-directory move too, before deleting the ordinary receipt.
3. Track the narrow pending-dispatch obligation for `(requestId, attempt)` when
   admission or explicit retry saves `running` before launching its worker.
   Consume that obligation exactly once under `operationMu`, after durability
   confirmation; normal replay must not restart an already dispatched worker.
   Identical POST repair completes the same intent/attempt and dispatches it,
   rather than incrementing an attempt to escape a stuck `running` state.
   This is bounded in-memory bookkeeping, not another scheduler or durable
   journal. Startup keeps the existing paused/explicit-retry behavior; do not
   claim exactly-once model inference across a process crash before a saved base.
   Distinguish this unlaunched obligation from an already dispatched worker
   that later stops after a base, reservation or failed-outcome write error.
   Confirming the latter's write must not dispatch its naming attempt again
   or leave a stopped worker presented as running indefinitely. Once durability
   is confirmed, use the existing failed/paused status and explicit-retry
   semantics, preserving the saved base/handoff and exact current receipt and
   attempt. Any retry increments only through the ordinary explicit action;
   it reuses a saved base rather than re-running naming unnecessarily.
4. Check the adjacent upload boundary: `uploads/store.go` publishes catalog JSON
   before its final directory sync, and an existing claim can return unchanged
   wire text without another write. `ClaimPreparation` replay must confirm the
   existing catalog claim's durability before preparation acceptance advances;
   finding a pending entry is not proof that the failed sync succeeded. A
   narrow file/directory confirmation inside that catalog transaction suffices;
   keep its schema and exclusive scope checks. Never release the pending claim
   because the caller received an error.
5. Make unconfirmed status distinguishable from an ordinary accepted result.
   Accepted additive JSON error: HTTP 503 with the exact `requestId` and a fixed
   `code: "preparation_persistence_unconfirmed"`. An identical recovery POST
   can perform confirmation and dispatch repair. For this exact bound error,
   browser recovery may resend its frozen body after GET; otherwise preserve
   the existing unknown-outcome rules. Do not return 404 or use a validation
   rejection classification to imply that an unconfirmed published request is
   absent. Collector reconciliation confirms pending writes before collection;
   on failure it aborts collection and retains evidence/files. It must preserve
   the pending-dispatch obligation until the common admission repair handles it.
   Progress-page retry needs the same usable recovery: if an incremented attempt
   was published before a retry response failed, healthy confirmation exposes
   the current matching receipt/attempt and either its one pending launch or
   its stopped, explicitly retryable outcome. Neither a stale token nor a
   persistent GET-503/running projection may hide recovery after I/O is healthy.
   Keep this within the bound 503 and existing status/retry contract; refer any
   required public-contract expansion to the coordinator before implementation.

Implementation boundary: preparation store/admission/status/retry and narrowly
scoped upload-claim confirmation, with the browser's existing recovery helper
recognizing the fixed persistence-error code. Do not change ordinary explicit
creation behavior, naming policy, ID/body immutability or package-generation
checks. The implementer may choose the smallest private bookkeeping and status
projection satisfying these accepted durability, dispatch and stopped-worker
obligations. This is not authorization for another workflow framework.

Mandatory focused regressions inject real post-rename directory-sync failure
during both initial admission and explicit retry. Cover repeated failure then
healthy same-process confirmation/replay: no unsafe 202/redirect, no worker or
model call before confirmation, exact published receipt/request/attempt and
one dispatch of the pending attempt. Use minimal private directory-sync/fault
seams, not a broad filesystem abstraction.

Other fault coverage follows the ownership boundaries changed by the repair:
catalog-claim replay, compact-mapping durability before receipt retirement,
and an already dispatched worker stopping after later persistence failure.
For the stopped worker, prove confirmation exposes a usable explicit retry,
retains the saved base/reservation and does not repeat that attempt's naming.
Verify progress-page recovery after publishing an incremented retry attempt,
including current token recovery rather than indefinite 503/running. Retain
focused collector/file-retention, concurrent replay, restart and generation
refusal assertions where those paths change. Persistent failure stays visible
with evidence/files retained; it must not spin or require a replacement ID.
These are application recovery regressions, not exhaustive upstream filesystem
write/fsync conformance coverage.

### Definitive admission rejection versus unknown browser outcome

Source trace: stale catalog rejection occurs in `freezePreparationPreset`
before the new record is saved. But `createPreparation` returns the same HTTP
409/error shape for that branch, upload failures and errors after persistence.
GET 404 only describes current visibility. It cannot exclude an earlier delayed
POST, a duplicate tab or later acceptance of the same immutable body. Therefore
neither all 4xx responses nor a rejection followed by 404 establishes that the
request ID/upload scope is globally unowned.

`static/preparation.js` freezes `draft.body` before POST; `receive` throws on
every non-success; `recover` sends the same bytes after 404. `static/app.js`
locks fields/files whenever that body exists and automatically recovers on
reload. This protects unknown outcomes but offers no usable continuation when
the immutable body contains a rejected old catalog. The existing frontend
report already treats another tab as a separate request; make that route an
explicit visible action instead of requiring the user to discover it.

Accepted UX repair: after a failed attempted submission, retain
**Recover saved request** and offer **Start a separate request**. The latter
opens the current New session page in a new tab with `rel="noopener"`, leaving
the original tab's storage/envelope untouched. The destination uses a new UUID,
current catalog and a fresh upload scope; it never imports old file selections,
scope ownership or a serialized body. Do not put prompts/settings in a URL or
logs. Keep the original raw text/settings/envelope and file selection accessible
for recovery and deliberate copying; an existing copy helper may make that
usable without introducing a clone mechanism. Files are reattached deliberately
to the new scope. The action starts an independent draft and never automatically
submits it. Original files remain under their normal retention contracts.

For a received validation error, show that error and this new-request route.
For a lost/ambiguous response, keep recovery primary and state that the original
may still finish if the user chooses a separate request. Do not describe either
action as cancelling, replacing or proving non-admission of the old request.
An accepted response still follows its original operation. Existing attempts
remain immutable even when a later GET returns 404. Do not clear their browser
records, unlock their uploads, adopt a competing scope or call deletion/release.
If the browser restores an attempted draft in the destination, preserve its
normal recovery behavior rather than overwrite it to force a fresh identity.

This accepted alternative needs only the existing request helper/index UI plus
tests; it needs no rejection ledger, rejection tombstone or new admission-success API.
A future same-form edit/reuse design would require stronger explicit request-
scoped rejection evidence and concurrency reasoning; an HTTP status or a parsed
error string is not that proof. Same-form reuse is outside this bounded repair.

Required verification: extend the registered pure preparation Node contract
through `TestShippedBrowserClientMatchesSessionAPI` for stale 409 then 404,
lost response then 404, accepted response after a lost response, repeated
recovery and storage failures. Assert original ID/body/scope/selection bytes
never change and no old-scope delete/release/transfer occurs. Implement actual
Playwright cases in `test/creation_browser.cjs` and run them only after renewed
mandatory review: stale catalog
offers the explicit new-tab route; the original remains recoverable across
reload; the new tab has no opener, a different UUID and fresh scope/current
catalog; ambiguous old acceptance can still complete without being adopted by
the new draft. The new tab requires deliberate submission and reattachment.
Test restrictive storage/pop-up behavior without clearing either attempt.

Both accepted remediations are runtime-local and additive; provider/tool
restrictions, deployed ancestry, host paths, existing persisted schemas and forward-only
deployment recovery remain unchanged. New test names/selectors await the
implementer's registration; source Go commands retain `-mod=readonly` and
pre-review browser checks keep `PORTAL_BROWSER_TEST` unset. No quick or live
checks were run for this reconciliation. Private bookkeeping and the bound 503
preserve persisted schemas and the host contract; provider behavior and the
existing host-migration applicability decision remain unchanged. Implementation
and its focused verification must finish, then renewed independent review must
assess the changed heads before the parent can resolve R1/R2 or claim readiness.

## Native fixture transport decision, 2026-10-04

Recommend the bounded mock-server correction: return HTTP 426 only for a real
WebSocket upgrade request to `/v1/responses`, then require actual native HTTP
POST inference through the existing SSE mock. Keep ordinary GET at 404,
including the firewall/provider-connectivity positive probe. This is a supported
native transport fallback, not a provider/capability substitution. Full mock
WebSocket support is not required for the currently defined action-tool gate.

Primary evidence is pinned Codex 0.160.0 source under
`/nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source/codex-rs/`:

- `core/src/client.rs:1024` enables Responses WebSockets from provider
  `supports_websockets` and session fallback state only. Removed
  `features.responses_websockets[_v2]` flags cannot establish HTTP selection.
- `preconnect_websocket` at 1451 handles HTTP 426 at 1507 by activating native
  fallback; `stream_responses_websocket` handles it at 1922 by returning
  `FallbackToHttp`. `stream` at 2220 onward switches and invokes
  `stream_responses_api`; `force_http_fallback` at 648 changes the transport
  flag/cache, not provider capabilities or model metadata.
- Both paths call `build_responses_request` (885; callers 1702 and 1877), which
  builds instructions/tools from the same prompt, provider and model, and both
  use `map_response_stream` (1768 and 2097). Builtin OpenAI construction at
  `model-provider-info/src/lib.rs:520` retains its Responses API, WebSocket,
  standalone-search and internal-metadata capabilities with a base-URL override.

The diagnostic log `/tmp/automatic-session-slugs-native-diagnostic-proof.log`
shows twelve WebSocket GET attempts failing with 404 and no inference POST;
the coordinator reports the positive connectivity probe passed. This diagnoses
the fixture's missing handshake response, not isolation success.

Implementer scope is the fixture responder and its focused tests only. Match
GET plus the exact endpoint and valid WebSocket upgrade headers, including the
case-insensitive `Connection: upgrade` token and `Upgrade: websocket`; validate
the version/key as a WebSocket handshake rather than treating every GET as an
upgrade. Plain GET and unrelated/malformed requests retain their existing
refusals. Keep POST decoding/SSE responses and all substantive assertions.
Quick responder tests must distinguish upgrade-426 from plain-GET-404; the
watcher-run native fixture must observe the native upgrade/fallback and real
POSTs carrying `gpt-6-luna`/`low`, full tools and instruction sentinels. A 426
or a successful connectivity probe without inference is not a passing case.

Coverage must be labelled **native builtin OpenAI HTTP-fallback coverage**.
It exercises actual tool construction/dispatch, questions, private teardown,
cancellation and persistence through native HTTP/SSE. It does not exercise
successful WebSocket framing, continuation/delta caching, reconnect behavior or
malicious tool delivery specifically over WebSockets. Retain the subsequent
positive live naming/model canary on the unchanged serving transport, with no
forced fallback or capability override; deterministic naming fallback alone
does not satisfy that canary. The canary verifies real serving-path success,
not an exhaustive hostile-WebSocket isolation matrix. Add a WebSocket mock only
if a concrete transport-specific requirement/failure makes those extra cases
necessary; refer that scope back to the coordinator.

Production helper/policy, exact binary, builtin provider/model/catalog,
deadlines, egress and canary controls, trust boundary and persistence/notification
assertions remain unchanged. Normal inference transport remains outside the
forbidden model-action network boundary. No custom provider, reduced model,
metadata rewrite or Codex patch is allowed. The correction still needs quick
checks, independent review and watcher-run native proof before the live gate.
This is a source-based design decision only; no test was run here and no
native isolation or readiness pass is claimed.

## Nonempty instruction-file correction, 2026-10-04

This bounded correction supersedes the earlier empty-file contract. Source
inspection confirms that contract cannot start the pinned native utility.
The coordinator reports all eight ordinary source/tool controls and Luna/low
passed, while all 36 utility leaves failed during setup before inference.
Those controls do not establish utility isolation. Implementation and renewed
review of this correction, native proof and final package refresh remain pending.

Primary evidence is the same pinned Codex 0.160.0 source identified above:

- `core/src/config/mod.rs:3992-4003` reads `model_instructions_file` before
  choosing explicit `base_instructions.or(file_base_instructions).or(cfg.instructions)`.
  `app-server/src/request_processors/thread_processor.rs:1200,1680` passes
  `thread/start.baseInstructions` through `ConfigOverrides`. Thus nonempty
  explicit utility instructions still win once file loading succeeds, with
  `BaseInstructionsProvenance::Custom`; the file must nevertheless be readable.
- `core/src/config/mod.rs:3980` trims an empty `compact_prompt` to `None`;
  4059-4065 reads the compact file before selecting `compact_prompt.or(file_compact_prompt)`.
  The current empty inline override therefore selects the private file's
  trimmed contents, not an empty effective compact prompt. `core/src/compact.rs:115`
  uses that configured text for local automatic compaction when invoked. This
  correction must not claim compaction is disabled or inherit the operator's
  compact-file instructions.
- `try_read_non_empty_file` at 4570-4604 rejects empty/whitespace-only text with
  `InvalidData`. The inspected codex-web `23d1aaa67574c849b933178400058f46d53ef3e1`
  helper instead requires `info.Size() == 0`; runtime
  `d05e75270a9bed417d07e9be8bc082c906f6846a` writes zero bytes in
  `portal/internal/web/session_namer.go`. These are source checkpoints, not a
  claim about subsequent implementer edits or proof of every native failure.

Selected public interface: retain required `EphemeralTurnOptions.InstructionFile`
and add one exported **string constant owned by codex-web**, with exact bytes:

```go
const EphemeralInstructionFileContent = "Preserve the current utility task and its explicit instructions.\n"
```

The same file remains the override for both path-valued config keys. This
generic text contains no naming rules, project instructions, paths, tool grants
or user data. Explicit `baseInstructions` remains authoritative for the utility
task; the fixed text supplies the otherwise inherited compact-file prompt.
Keep the existing empty inline `compact_prompt` and all restriction controls.
Do not copy application naming instructions into this file, expose a content
option, remove the file overrides, use JSON null, change model/provider/catalog,
or patch Codex. The supported loader requires a nonempty file even if another
value wins precedence; an inline-only override cannot fix that requirement.

The helper must validate an exact-length, bounded read against the constant
byte-for-byte before connecting, retaining canonical absolute path, regular
non-symlink file, owner, mode 0600, single-link and private-parent/placement
checks. Reject empty/whitespace, another nonempty value, missing final newline,
extra bytes, unreadable or unsafe files with the existing static isolation
error and no connection. Do not normalize caller bytes or log contents.
`Directory` remains empty. The trusted caller creates a unique per-call file
before invocation and keeps its path and bytes unchanged through bounded
teardown. Mode 0600 is not filesystem immutability; this is an application
ownership/lifetime contract, not protection against an administrator rewriting
the file between validation and Codex's read. No config lease, immutable-file
framework, shared rewrite or extra provisioning API is needed.

Implementer edits are limited to the provider validator/API documentation,
provider-owned test provisioning and the consuming naming adapter/tests/docs.
The consumer writes `[]byte(codex.EphemeralInstructionFileContent)` once, rather
than duplicating the literal. Use a neutral scratch filename such as
`instructions.txt` in the adapter, fixture and policy-corpus example; the
helper still accepts the explicit validated path, with no filename convention.
Update `codex/ephemeral.go`, `codex/ephemeral_test.go`, the tagged native fixture,
`codex/ephemeral_policy.json` example paths and `docs/reference.md`; on the
consumer side update `session_namer.go`, `session_namer_test.go` and
`docs/session-preparations.md`. Refresh dependency/resource hashes through the
coordinator's existing pin/package workflow. Runtime schemas, receipts, upload
ownership, generation checks, deadlines, two-call limit and fallback are unchanged.

Required verification for the correction:

- Quick provider tests prove exact bytes succeed and each invalid-content/path
  case fails before connection, both config keys use the same validated path,
  and explicit base/developer text remains unchanged. Adapter tests read the
  supplied `InstructionFile` and compare it to the provider constant while
  preserving empty cwd, permissions, unchanged deadline and per-call cleanup
  assertions. The native fixture must provision the same constant. In the
  already prepared owning Nix environments, use
  `go test -mod=readonly ./codex -run '^TestEphemeral' -count=1` from codex-web
  (without the integration tag), and
  `go test -mod=readonly ./internal/web -run '^TestSessionNamingUtility' -count=1`
  from dev-workspace/portal. Compile the tagged fixture and run only its
  registered pure diagnostic/responder/schema helpers before review; the
  native integration entry remains a post-review check. Keep the exact protocol
  corpus and fixed-key/type validation, with no new RPC methods or schema fields.
- After committed changes, have the same reviewer0 reassess the affected
  provider/API, adapter, native-fixture and compatibility lanes. Then a watcher
  reruns the exact-binary utility matrix with unchanged builtin provider,
  model/catalog, assertions, ten-second budget, action-tool restrictions,
  egress guard, persistence and question/teardown boundaries. Require actual
  inference with explicit naming instructions and absent inherited base/compact
  sentinels; retain the expected global-policy sentinel. The file fix and mock
  transport tests alone are not isolation proof. Retain the HTTP-fallback
  coverage limit and unchanged-serving-transport positive model canary above.
- Denied-egress cases remain unresolved. Record bounded synthetic phase
  evidence separating handshake/config/model lookup, thread start, turn start,
  provider inference, tool dispatch and teardown, with the existing network
  counters and positive controls. Explain any denied attempt at its actual
  phase; do not ignore/reset unexplained counters or treat setup failure as
  successful action denial. Keep raw prompts/config/credentials out of logs.

Refresh the final assembled package, source/resource hashes and review packet
before release. This file-content correction changes no browser behavior,
preparation worker ownership, upload/old-reader format, host path or namespace
migration boundary. Existing Chromium, runtime race, old-source and actual
host-VM evidence need not be repeated solely for this correction; repeat the
owning check if implementation changes its behavior or evidence no longer
matches its inputs. The prior host-migration applicability decision remains.
Ordinary conversation callers are unaffected. This unreleased helper's empty
file callers must update together with their provider dependency; no legacy
empty-file fallback is supported. Failures still select deterministic naming
fallback without changing accepted identity. Deployment remains the assembled
user profile with forward-only recovery; no deployment/readiness pass, merge
approval or lifecycle action follows from this design. No tests were run here.

## Native contract diagnosis after the fixed-file run, 2026-10-04

This source-only assessment uses committed fixture
`5f6c7e255c2bd18361107cf322be1ec3e3e91ea2`, the unchanged pinned Codex 0.160.0
source above, [fixed-file-review.md](fixed-file-review.md) and the existing
`/tmp/automatic-session-slugs-fixed-file-native.log`. The lead closed that
review's three diagnostic findings with direct inspection and seven focused
race groups/61 cases; that does not close the native isolation gate. Only this
design document is edited here. Diagnostic implementation remains implementer-owned.

The log contains 35 utility leaf phase records. Baseline reaches one provider
POST and passes its expected-result check before the tool-inventory failure;
clock reaches two POSTs, and both question paths reach one. The two 400 ms
preflight leaves pass the real withheld-response and error-category checks but
later fail the unchanged deny-counter check. `question-at-cancel` reaches zero
POSTs. The final reconfiguration snapshot reports a SQLite prompt sentinel,
preventing the fresh-MCP leaf and later managed-conflict/persistence gates from
completing. Neither an earlier fatal nor a satisfied result category proves
the assertions that follow it. No utility matrix pass is claimed.

### Tool inventory: retain the restriction until observed shapes explain failure

Selected metadata fields in `models-manager/models.json` confirm Luna uses
Responses Lite, supports search, and declares only `send_user_message_async`
and `clock` in its experimental tool list. Metadata is not the complete tool
inventory. Pinned source establishes:

- `core/src/client.rs:902-936` puts Lite tool schemas in a developer-role
  `additional_tools` input item and omits the top-level tool list. With native
  namespace capability, `tools/src/tool_spec.rs:95-143` groups plain functions
  into `functions`, preserving named namespaces. `tools/src/responses_api.rs:59-81`
  serializes namespace children as tagged `function` or `custom` entries.
- `core/src/tools/spec_plan.rs:1171-1201` registers the plain
  `request_user_input_async` handler from Luna's legacy metadata name;
  1225-1233 adds clock. `handlers/current_time.rs:54-82` advertises
  `clock.curr_time` as a namespace/function, without deferred loading.
  `handlers/request_user_input_async.rs:37-91` advertises a plain function.
  The separately labelled ordinary-question control intentionally adds only
  `request_user_input`; it is not the production policy.
- `spec_plan.rs:371-404` adds tool search only when an eligible deferred tool
  exists, despite Luna's search capability. Hosted tools are omitted for Lite
  at 627-630. This does not establish that every action extension was disabled
  in the observed request; the actual inventory and dispatch still decide.

The fixture's `integrationToolNames` (1266-1343) already handles these direct
and Lite shapes. Its `respond` predicate (1177-1188) combines parser errors,
missing clock/question names, unexpected count and the control's third tool
into one failure string. The current log cannot distinguish them. Source
inspection alone supplies no justified parser fix or additional allowed tool.
First obtain the bounded name/type/role/count/error-category inventory already
assigned by the coordinator, from every model-facing catalog location. Preserve
duplicate, deferred, hosted/custom and unknown-tool rejection. Correct only a
demonstrated source-supported representation mismatch; an actual action tool
requires tracing its eligibility and supported restriction, not an allowlist
exception. No prompt/schema descriptions or tool arguments belong in diagnostics.

### Persistence: a real conflict with the existing daemon contract

`core/src/session/session.rs:1008-1010` skips `LiveThread` creation for ephemeral
threads; 1112-1113 omits their session state-DB handle. App Server's
`request_processors/thread_processor.rs:1471-1485` also skips staged persistent
thread metadata. These are supported thread/history-persistence boundaries.
They do not suppress process-wide diagnostics:

- `app-server/src/request_processors/turn_processor.rs:651-658` submits the
  input through `TurnInputRequest`. `core/src/session/submission.rs:7-12`,
  `protocol/src/protocol.rs:587-628`, `protocol/src/turn_input.rs:33-53` and
  `protocol/src/user_input.rs:14-24` use derived `Debug` with the input text.
  `core/src/session/handlers.rs:427-432` logs `debug!(?sub, "Submission")` for
  all operations except `ResolveElicitation`, without an ephemeral check.
- `app-server/src/lib.rs:655,735-746` initializes the shared SQLite runtime
  and installs its log layer. `state/src/log_db.rs:61-88` independently defaults
  that sink to TRACE; the submission target is not excluded. At 276-345 the
  sink retains event fields and span/thread context; `format_feedback_log_body`
  at 434-472 includes the formatted debug fields. `state/src/runtime/logs.rs:11-40`
  inserts that body into `logs`; `state/src/sqlite.rs:28` names `logs_2.sqlite`.
  There is no ephemeral filter in this path. Its ordinary batching (512 entries
  or ten seconds, `log_db.rs:56-58,480-523`) also means immediate absence is
  insufficient proof of non-persistence.

This is a concrete source path for persisting utility input and identity in
diagnostic storage even when there is no resumable thread/rollout. It is a
source-supported explanation for the observed sentinel, not attribution of
the actual failing database/table: the assigned safe diagnostic must identify
that using filename/table/count only. Other stores must still be checked.
`RUST_LOG` filters stderr separately (`lib.rs:709-723`); it does not disable
this SQLite layer. `history.persistence`, per-thread file overrides, OTEL or
feedback preferences do not provide a per-call filter for the inspected sink.
No supported helper/config remedy was found for the strict no-prompt/no-identity
logging invariant on this already running native daemon.

**Consequential boundary: keep release blocked and refer this conflict to the
coordinator before any public change.** Keep the persistence assertion. Do not
exclude `logs_2.sqlite`, erase rows afterward, shorten the observation window,
relocate shared SQLite state, change the model or hide failure behind naming
fallback. A native privacy/logging capability change would require separate
authorization, source/protocol review and exact-binary proof; no Codex patch or
new daemon/process framework is authorized. Permitting native prompt logs would
change the accepted contract and is not selected by this brief. Existing
ephemeral API/source inspection cannot support the current broad no-logging
claim. Independent fixture corrections may proceed while this gate stays open.

### Cancellation must target the actual question

The committed proxy at 1814 cancels on any `item/started`; an initial user item
can therefore win before inference, matching the observed zero POSTs. Pinned
`core/src/tools/handlers/request_user_input_async.rs:131-154` instead emits an
`agentMessage` with async delivery and nonempty questions, then completes it
and returns internal `accepted:true`. Target the first such real native
`item/started` bound to the current leaf, thread and turn. Record one-shot
question-observed proof before cancelling, then forward through the same
private sink. Require provider POST, synthetic tool dispatch and matching
question emission before accepting the cancellation category. Ignore ordinary
user/agent items and unrelated identities; a missing question fails the case.
Quick negatives cover those non-question/foreign events; the native case must
retain immediate rejection, exact teardown, zero ordinary UI/timers/answers and
no persistence. Keep deadline and production notification handling unchanged.

### Own the firewall positive-control dial

Owning Go 1.26.7 source is
`/nix/store/hfb2fkwkkr6jdcg2ggibvf1zablw7i57-go-1.26.7/share/go/src/`.
`net/http/transport.go:1523-1529` detaches dialing from request cancellation;
`wantConn.cancel` at 1390 stops waiting without cancelling that dial.
`CloseIdleConnections` at 909-917 cancels no-longer-wanted pending dials. The
fixture's default-transport blocked HTTP probe (1003-1018) supplies only a
100 ms client timeout and never closes the retained dial. Later SYN retries
are therefore a concrete possible counter producer, not proven attribution.

Select the smaller fixture correction: keep the allowed provider GET/404
connectivity proof, but make the blocked endpoint probe one owned
`net.Dialer.DialContext` call with the existing 100 ms budget, `tcp4` and the
synthetic canary's literal IPv4 host/port. Require failure, zero canary requests
and a positive deny-counter increase attributable to the controlled probe;
synchronously finish it and close any returned connection before the ordinary
control/baseline. No shared HTTP transport, DNS, fallback address race, sleep or
baseline reset is needed. `net/dial.go:526-557,655-657` takes the serial path
without fallback addresses; `net/fd_unix.go:78-108` interrupts the pending
connect on cancellation and `net/sock_posix.go:70-73` closes its FD on error.
An owned HTTP transport would require extra dial-completion ownership with no
benefit for this connectivity assertion.

The log's first fixed-baseline change is 3 to 4 during an early-events
thread-start sample, before that leaf's POST; subsequent increases include
between-leaf activity. Counter samples do not identify packet/process owners.
Retain every strict final comparison to the one captured post-control baseline;
the direct-dial repair is not permission to disregard residual increments.
Quick fixture tests establish probe ownership/cancellation and meaningful
negative cases; actual native stability and attribution remain release gates.

All proposed immediate changes are fixture diagnosis/ownership corrections.
No production policy, helper, browser, preparation/worker/upload state, module,
schema, host path or migration change is selected. Commit and quick-check any
assigned fixture changes, reconcile affected review lanes, then use the existing
watcher workflow only when the coordinator authorizes another native run.
The complete matrix, fresh MCP, managed constraints, delayed persistence,
forbidden dispatch, fixed egress and unchanged-serving-transport canary gates
remain. Final pins/resources/deployment stay pending; unchanged browser/race/
old-source/host-VM evidence is unaffected by fixture-only changes. No tests,
serving inference, Git mutation or deployment were performed for this assessment.

## Native Code Mode boundary investigation, 2026-10-04

This supplement addresses the actual wrapper catalog observed at provider
`4651d76447cdbd1fa742358baeef01f0ebcdf250` / runtime
`8acd722029f3c1d0abd8c2801b734a554a4a2eef`. It is a source-backed recommendation
to the coordinator, not an implemented policy change or completed isolation
proof. All Rust references below are relative to the unchanged pinned source
`/nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source/codex-rs`.
The user's selected restriction forbids model file/network actions and rejects
questions immediately; it does not forbid pure computation. Earlier blanket
rejection of every Code Mode wrapper must therefore be assessed by capability,
not retained as an unsupported claim that the false feature flags remove it.
No action tool, model/provider override or logging exception is selected here.

### Observed catalog and the supported selection mechanism

[native-observation.md](native-observation.md) records the actual developer
`additional_tools` catalog: namespace `functions`, custom `exec`, function
`wait`, function `request_user_input_async`. The separate ordinary-question
control additionally has `request_user_input`. No direct clock namespace was
advertised. All 35 main leaves entered, all recorded deny samples remained
2 to 2, and the corrected timeout/question-cancellation controls reached their
intended boundaries. These observations do not establish the wrapper's nested
registry or pass later assertions. The strict catalog predicate still failed.

Selected original `models-manager/models.json` fields at 527, 543, 546 and
648-651 are `gpt-6-luna`, `tool_mode: code_mode_only`,
`use_responses_lite: true`, and experimental tools
`[send_user_message_async, clock]`. No metadata was edited or substituted.

- `core/src/tools/mod.rs:75-99` gives explicit model `tool_mode` precedence
  over `features.code_mode_only` and `features.code_mode`. Its unavailable-host
  fallback applies only to `CodeMode`, never `CodeModeOnly`.
- `core/src/tools/spec_plan.rs:794-804,819-937` hides ordinary nested tools
  from the direct catalog in Only mode and always registers custom `exec` and
  function `wait`, even with an empty nested inventory. At 1171-1201 the
  question handler is `DirectModelOnly`; at 1225-1233 clock is an ordinary
  registered tool. Thus clock moves inside exec and the question stays direct.
  Lite serialization at `core/src/client.rs:902-936` and
  `tools/src/tool_spec.rs:95-143` explains the observed namespace/role/types.
- `features/src/feature_configs.rs:22-71` and
  `core/src/config/mod.rs:2725-2758` define the supported typed feature objects.
  `features.code_mode` accepts `enabled`, `excluded_tool_namespaces` and
  `direct_only_tool_namespaces`; `features.code_mode_host` accepts `enabled`
  and `disable_in_process_fallback`. These are not top-level `code_mode` keys.
  A typed `features.code_mode` value with `enabled: false` and
  `direct_only_tool_namespaces: ["clock"]` would move clock direct and remove
  it from the nested inventory (`spec_plan.rs:520-548`). It still leaves
  exec/wait. Merely excluding clock does not make it visible in Only mode.
- `core/src/thread_manager.rs:557-564` chooses the shared session provider
  from daemon startup settings. `CodeModeHost` enabled **or**
  `disable_in_process_fallback` true selects `ProcessOwnedCodeModeSessionProvider`;
  otherwise it selects the disabled provider. The default host feature is
  enabled (`features/src/lib.rs:1074-1080`). Changing a private thread's flag
  does not replace this shared provider. Setting disable-fallback true is not
  a way to disable execution.

There is no supported per-call Direct-mode override in the inspected config
and model override paths. Rewriting metadata or changing startup host policy
would alter the selected serving contract and is not this remedy.

### What the native wrapper can actually execute

Each thread constructs its own `CodeModeService` with the shared provider and
thread config (`core/src/session/session.rs:1768-1774`). Exec passes its real
step context and a tool list derived from the handler's captured nested specs
(`core/src/tools/code_mode/execute_handler.rs:36-104`), then lazily opens that
service's session (`code_mode/mod.rs:129-148,232-258`). This does not recheck
`features.code_mode_host` before execution. The selected provider lazily starts
the installed native host (`code-mode/src/remote_session.rs:35-110` and
`remote_session/connection.rs:156-169`), over its private protocol. That host
runs `InProcessCodeModeSession` inside the host process; the name does not mean
a feature-controlled fallback to unrestricted Node or a shell.

The following support a no-file/no-network capability boundary, subject to
native proof of the actual restricted registry:

- `code-mode-runtime/src/runtime/mod.rs:172-214` creates a fresh bare V8
  isolate/context. `runtime/globals.rs:15-47` installs only `tools`, `ALL_TOOLS`,
  timers, output helpers, `store`/`load`, `notify`, `yield_control` and `exit`;
  it removes console, Atomics, SharedArrayBuffer and WebAssembly. It installs
  no Node/Deno/process/require/fetch/filesystem/socket API. Ordinary JavaScript
  computation, including Date, remains available.
- `runtime/module_loader.rs:166-238` routes static and dynamic import through
  a resolver that rejects every specifier; no file or network module loader
  exists there. Empty cwd alone is not the protection.
- `runtime/globals.rs:51-110` builds `tools` and `ALL_TOOLS` from the supplied
  enabled-tool inventory. `runtime/callbacks.rs:15-74` binds each callable to
  an internal index, checks that index, and obtains the backend name/kind from
  the inventory. Calling a function with a different receiver or editing a JS
  property cannot supply an arbitrary backend name. The plan collects nested
  specs only after registry construction (`spec_plan.rs:831-895`); it does not
  manufacture shell/network tools for exec.
- Nested calls re-enter the same step router via
  `core/src/tools/code_mode/mod.rs:335-412`. The registry resolves the actual
  registered name and rejects absent names (`core/src/tools/registry.rs:491-495,
  542-580`). This lookup is not an advertised-name security filter: hiding a
  registered action tool would be insufficient. Empty execution environments,
  the fixed action restrictions and captured MCP disables must prevent action
  registration. Shell requires an environment and its feature at
  `spec_plan.rs:1079-1089`; patch and image reading require an environment at
  1269-1283. Existing extension/action controls remain required independently
  of the wrapper inventory.
- `store`/`load` use serialized values in a session-local HashMap
  (`runtime/callbacks.rs:206-267`, `session_runtime/mod.rs:41-74,170-172`), not
  persistent memory tools. `notify` produces a tool-output item in the same
  thread (`core/src/tools/code_mode/delegate.rs:464-498`), not a shell notify
  command or user question. These values/output still face the unresolved
  daemon logging boundary; in-memory storage is not a no-logging proof.
- `image`, `generatedImage` and `audio` format supplied data. Image/audio URL
  normalization accepts only data URLs and rejects file/HTTP(S) references
  (`runtime/value.rs:46-105,190-237`; `runtime/callbacks.rs:149-185`). Their
  names do not enable image generation, local-file reads or remote fetching.
  Output and timer helpers still require private-sink/size/deadline tests.

**Smallest recommended surface:** retain the current 55 fixed restrictions,
private start inputs and captured MCP disables; document the native pure-JS
exec/wait wrappers, with **exactly `clock__curr_time` as their callable backend**
and direct async questions rejected immediately. Do not turn a wrapper name
into an unconditional allowlist entry. The direct-clock typed-object alternative
above adds a policy change without removing wrappers and is not recommended.
No public options/config map, native patch, custom provider, metadata change,
global rewrite or additional process framework is needed for this surface
interpretation. The actual backend and lifetime still require the gates below.

### Lifetime limit requiring explicit evidence and coordinator reconciliation

Pure computation does not make wrapper cleanup automatic. Exec's yielded cells
can outlive their originating turn (`core/src/tools/code_mode/mod.rs:356`).
`core/src/tasks/mod.rs:935-946` terminates active cells on interruption only
when `features.code_mode_interrupt` is enabled; the current fixed policy sets
it false. Thread unsubscribe acknowledges subscription removal
(`app-server/src/request_processors/thread_processor.rs:1020-1045`), not host
session shutdown. Unloading waits for no subscribers and an inactive thread
plus the daemon's configured delay (`thread_lifecycle.rs:55-60,360-398`);
the default is 60 seconds (`core/src/config/mod.rs:3911-3912`). A per-thread
override must not be assumed to replace that processor's startup delay.

Actual session shutdown does call Code Mode shutdown
(`core/src/session/handlers.rs:294-325`); its session runtime cancels and joins
cells (`code-mode-runtime/src/session_runtime/mod.rs:142-151`), including V8
termination (`cell_actor/mod.rs:618-628`). Those are useful cleanup mechanisms,
but unsubscribe success and the helper's 250 ms cleanup reserve do not prove
they have finished. Model `wait` yield time is an observation timeout, not an
execution deadline. The current provider uses default cell limits.

This is a source-supported lifecycle limitation, not an observed hostile-cell
failure or permission to extend the 10-second whole-call budget. Before claiming
bounded wrapper support, prove actual exec completion/yield/CPU-loop/cancel and
post-return behavior. If the existing deadline/teardown contract cannot be met,
bring the concrete failure and smallest supported change to the coordinator.
Do not silently enable CodeModeInterrupt, change a daemon delay, accept lingering
work or claim that enabling interruption alone handles already-completed turns.
The global host process may serve ordinary threads; its continued existence is
distinct from this utility's live cells or cross-session retained values.

### Verification and implementation boundary

Implementation remains assigned through the coordinator. A fixture/parser-only
change can correct the catalog expectation and add these native cases; public
helper documentation must describe the proven surface and lifetime honestly.
If cleanup needs a production change, it requires a separate concrete design
decision, quick checks and affected-lane review before native execution.

1. Parse every actual schema location with exact pinned namespace, custom/function
   type and count: normal catalog is exec, wait and async question; only the
   labelled ordinary-question control adds request_user_input. Reject unknown,
   duplicated, hosted/deferred or additional action entries. Include unchanged
   `tool_mode` and Responses Lite in selected-field catalog validation. Do not
   mistake generic examples in the built-in exec description for registered
   capabilities, or log that description/prompt to explain a mismatch.
2. Send a **real custom-tool** exec response through the native provider and
   require its native output/follow-up POST. A function call named exec only
   exercises incompatible-payload rejection (`execute_handler.rs:249-260`).
   In the real cell inspect only bounded names/types from `Object.keys(tools)`
   and `ALL_TOOLS`: require exactly `clock__curr_time`, then call it. Check that
   async questions and all action categories are absent from the nested set.
   Keep direct hostile dispatch tests as a separate registry check.
3. Exercise native JS attempts to use file/network/process globals, static and
   dynamic imports (`node:fs`, filesystem paths, network modules/URLs), forbidden
   nested tool names and forged callback receivers/properties. Test HTTP/file
   image/audio arguments and notification output. Require errors or unavailable
   APIs, unchanged file/read canaries, no action process starts, zero canary
   requests and unchanged deny counters. The installed native interpreter host
   is serving infrastructure, not permission for a model-selected command.
4. Prove per-call store/load separation and private notify output; no UI,
   ordinary-client event, persistent application state or later call can adopt
   utility state. Exercise real yielded-cell wait, awaited timer and CPU-loop
   cancellation, including lost turn response, normal final completion with a
   yielded cell, and disconnect. Keep the original whole-call deadline and
   exact-identity cleanup assertions; distinguish client return, provider
   cancellation, cell termination and eventual daemon unload in the evidence.
   Do not add sleeps, relax counters or call eventual unload timely cancellation.
5. Retain both actual question paths, all instruction/control sentinels, fresh
   MCP inventory, managed restrictions, delayed persistence and ordinary-client
   continuity. Corrected source/unit tests are followed by independent related
   review, then one coordinator-authorized watcher run of the full native
   fixture. HTTP/SSE fallback coverage and the required unchanged-serving-
   transport positive model canary retain their existing limits.

Quick fixture selector, from codex-web's existing Nix package environment:
`go test -mod=readonly -race -tags=codex_integration ./codex -run
'^TestEphemeralIntegration' -count=1`. This selects the registered fixture unit
groups, not `TestEphemeralProtocolIntegration`; new unit group names must be
registered under that prefix or explicitly added by the implementer. Run the
ordinary provider quick checks if helper/docs/policy are changed. The existing
exact-binary native command and all absolute binary/hash/source/tool prerequisites
in the provider reference remain the post-review entry; no native command was
executed for this investigation.

The actual `logs_2.sqlite` / `logs` prompt-and-identity observation now identifies
the store described as a source candidate in the previous supplement. Its
user-choice gate remains pending; no persistence assertion is waived here.
Stable counters in this run do not attribute earlier packets. No full isolation
pass exists, and fresh-MCP/final persistence gates have not completed. Browser,
preparation/receipt/upload state, provider model, module/host-state contract and
migration applicability are unchanged by this design-only investigation. Their
existing checks need no repeat solely for this supplement; any later owning
behavior change must be assessed separately. Final package/resource hashes,
pins, deployment and activation remain coordinator-owned and gated.

## Yielded-cell teardown decision, 2026-10-04

Scope: the same pinned Codex 0.160.0 source and provider `4651d764` helper;
runtime `8acd7220` is unchanged. The coordinator accepted the preceding pure-V8
capability interpretation conditional on actual nested-clock proof. That accepts
neither a cleanup guarantee nor native logging. This investigation edits only
this design; the implementer's separate wrapper fixture work can continue.

**Decision: no supported scoped App Server operation in this pinned version
provides the required acknowledged teardown of an owned ephemeral session and
its yielded cells after both successful and failed turns.** Enabling the fixed
`features.code_mode_interrupt` flag and interrupting on both paths is a partial
active-turn improvement, not a remedy for the accepted lifetime contract. Do not
implement or label that pair as sufficient. The missing capability is a real
release blocker, independent of the logging decision and action-tool proof.

### Why exact interrupt cannot close the gap

`app-server/src/request_processors/turn_processor.rs:1598-1655` loads the named
thread and checks a nonempty turn ID. An active mismatching ID fails. With no
active ID, the last terminal ID matching the request or a non-running agent
causes `no active turn to interrupt` **before** `Op::Interrupt` is submitted.
The helper currently requires successful `turn/completed` before returning its
answer, so sending an interrupt during successful cleanup naturally reaches
this completed-turn case. A failed/lost-response call can race with the same
completion and has the same limitation.

Even `{}` from the interrupt RPC is insufficient evidence of cell termination:
`app-server/src/bespoke_event_handling.rs:185-188,1203-1207,1563-1577` responds
to pending interrupts on normal `TurnComplete` as well as `TurnAborted`.
Completion can therefore win after interrupt admission. The response does not
report whether any Code Mode cell was found, terminated or joined.

When cancellation does reach Core, `core/src/session/handlers.rs:57-59` calls
`Session::interrupt_task` (`core/src/session/mod.rs:5054-5060`). It aborts the
current task if any; with none, it only cancels MCP startup. In
`core/src/tasks/mod.rs:536-560,923-946`, Code Mode interruption is inside the
existing task's abort path and conditional on `Feature::CodeModeInterrupt`.
`core/src/tools/code_mode/mod.rs:162-177` waits on its current cell termination
requests but logs their errors without returning them to the interrupt caller.
It is not a thread-wide shutdown acknowledgement. Sending an empty turn ID
would only take the startup-interrupt submission-acknowledgement path; it neither
fixes idle-cell cleanup nor preserves the helper's exact-turn safeguard.

Consequently, enabling the flag could reduce residual work after a genuine
active-turn abort, but it cannot establish the universal bound. Do not start a
second turn to manufacture an active task for cleanup, inject a model `wait`
call, accept an interrupted partial answer as success, or use unvalidated cell
IDs. Those would alter the one-turn contract without providing a reliable join.

### Supported thread methods checked

The public request inventory is
`app-server-protocol/src/protocol/common.rs:549-865,1032-1084,1451-1491`,
including its remaining deprecated methods. There is no thread shutdown,
close, immediate unload or direct Code Mode cell-termination request.

| Candidate | Actual boundary in the pinned source |
| --- | --- |
| `thread/unsubscribe` | `thread_processor.rs:1020-1045` removes the subscription and replies. It does not submit shutdown or await cells. |
| Closing the private socket | `thread_processor.rs:3588-3600` and `thread_state.rs:606-633` remove connection membership. They do not abort an extant thread; normal idle unloading remains responsible. |
| `thread/delete` | `request_processors/thread_delete.rs:75-85` explicitly rejects a loaded ephemeral thread as not persisted, before removal/shutdown. It is not an ephemeral close API. |
| `thread/archive` | `thread_processor.rs:1709-1747` requires the stored thread before reaching removal; ephemeral threads deliberately have no such persistence. Creating persistence to archive it would violate this feature. |
| `thread/revert` | `thread_processor.rs:2147-2158` explicitly rejects ephemeral threads; its later shutdown/replacement behavior is unrelated to utility cleanup. |
| Background-terminal cleanup | `thread_processor.rs:2387-2400`, `core/src/session/handlers.rs:61-63` and `core/src/tasks/mod.rs:903-908` affect unified-exec processes, not Code Mode sessions. |
| `thread/realtime/stop` | `turn_processor.rs:1369-1383` submits realtime-conversation close, not Core session shutdown. |

All abbreviated processor paths above are under `app-server/src/`.
Archive/delete removal would not be a suitable success barrier even apart from
their persistence requirements: `thread_processor.rs:1055-1081` logs shutdown
failure/timeout and proceeds with the removal operation.

Core does have the appropriate internal lifetime machinery:
`core/src/codex_thread.rs:276-277` delegates `shutdown_and_wait` to
`core/src/session/mod.rs:1047-1057`, which submits `Op::Shutdown` and awaits the
session loop. `core/src/session/handlers.rs:286-325` stops admission, aborts
tasks and shuts down the Code Mode service even when no turn is active.
`code-mode-runtime/src/session_runtime/mod.rs:142-151` joins its cell tasks;
`cell_actor/mod.rs:618-628` requests V8 termination. These are internal Rust
interfaces, not remotely callable methods available to the Go helper. Shutdown
errors also need honest treatment, rather than inferring successful joins from
a generic notification.

App Server eventually uses that machinery after its no-subscriber/inactive
delay (`request_processors/thread_lifecycle.rs:55-60,360-398,408-468`). The
default serving delay is 60 seconds (`core/src/config/mod.rs:3911-3912`), then
shutdown itself has a separate timeout. `thread/closed` is a notification after
that path, not a command or a way to request immediate teardown. Per-call flags
do not replace the request processor's startup delay; reducing a global delay
or waiting beyond the existing deadline is not selected.

### Smallest safe production consequence and ownership rules

Under the unchanged native/shared-daemon constraints there is **no complete
helper-only remedy** to select. Keep model-naming activation gated. The smallest
safe interim behavior, if the coordinator chooses to ship the independent
runtime work, is refusal **before `turn/start`** when the required isolation
contract is unavailable, using existing `ErrEphemeralIsolation` and deterministic
adapter fallback. Refusal must precede inference, not relabel an unconfirmed
cleanup as safe after cells have already started. A disabled model path is not
completion of the user's selected model-naming feature; the coordinator must
reconcile that concrete limitation. No new API option or persistent schema is
needed to preserve the existing fallback behavior.

Enabling model naming with the stated lifetime would need an additional
supported native capability that closes admission and terminates/joins **this
owned ephemeral runtime even when idle**, with a result distinguishable from
subscription removal or mere cancellation submission. Lost transport also
cannot manufacture that acknowledgement. This is the identified missing
capability, not a proposed native patch/process framework or permission to
change the pinned binary. No deadline relaxation, global host/config change,
metadata override, native-host kill or logging waiver is recommended here.

Any subsequently authorized solution must preserve this ordering and evidence:

1. Keep the completed answer provisional. Within the existing reserved cleanup
   portion of the original context deadline, request only a supported operation
   on the owned thread/runtime and wait for its actual termination result.
   Do not return successful naming merely because unsubscribe or interrupt
   returned. Error and success paths need the same lifetime guarantee.
2. Keep one private connection generation and validated ephemeral thread identity.
   A lost turn-start response may use only the helper's existing unique matching
   early-event turn ID (`codex/ephemeral.go:762-807`) for an active-turn interrupt;
   it never authorizes success, resume, a second turn or another generation.
   Ambiguous/foreign identities authorize no mutation. A thread-start failure
   without a trusted returned ID cannot be repaired by guessing or listing and
   adopting a thread.
3. Never extend the caller's hard deadline or create a detached cleanup retry.
   Keep existing cancellation/error precedence and deterministic fallback.
   An unavailable/timed-out/unconfirmed termination result cannot be reported
   as success or proof of no residual cells. Close the private transport without
   touching the serving daemon or other threads; record the release failure.
4. Preserve the shared native host for ordinary threads. Per-thread cell/session
   state is the ownership boundary, not a process PID. Keep ordinary Send,
   Subscribe, Resume, persisted receipts, browser preparation, package schema and
   deployment contract unchanged. This investigation selects no migration or
   new compatibility branch.

The current `codex/ephemeral.go:80-118` reserves at most 250 ms, interrupts only
on failure, ignores that interrupt error, checks unsubscribe on success, and
closes its private transport. Changing only the error condition to run on both
paths, even with CodeModeInterrupt enabled, cannot supply the missing result.
Do not spend the remaining budget attempting unsupported RPC names.

### Finite verification brief; no execution in this assignment

Quick transport/unit regressions, if a remedy is later assigned, must cover
completed-answer plus no-active-turn rejection; successful interrupt response
followed by normal completion; explicit abort with a cell-termination error;
lost response with a unique early ID; ambiguous IDs and generation loss; and
cleanup deadline exhaustion. None may turn subscription removal or `{}` into
proof of a cell join. A pre-inference refusal must make zero turn/start calls
and preserve the adapter's existing deterministic fallback. Use the existing
provider/adapter Nix quick entries with `-mod=readonly`; exact new test selectors
remain implementer-owned. Source tests do not establish native lifetime.

Native cases must separately observe an actual yielded exec cell, normal final
completion while that cell remains live, abort of an active cell, completion
racing interrupt, lost response and disconnect. Exercise both an awaited timer
and a CPU loop. Tie terminal cell/session evidence to that same native runtime,
cell and deadline; silence, an absent subscriber, an idle turn, an RPC response
or an eventually absent loaded-thread entry is not sufficient by itself.
Maintain an ordinary concurrent thread/cell to prove scoped cleanup leaves it
usable. Missing observability is an unresolved proof obligation, not a pass.
Do not shorten daemon unload delay in the fixture to stand in for production,
waive the time bound, or add sleeps/counter resets. The existing restricted
registry/canary/persistence gates remain independent and mandatory.

No native run is needed to establish the absent RPC and explicit ephemeral
refusals above. A coordinator-selected supported remedy would still require
quick verification, affected-lane independent review and exact-binary watcher
proof before activation. Only this design was changed; no application edit,
test, inference, Git/pin/deployment or session lifecycle action was performed.

### Conditional alternative: explicitly select an original Direct-mode model

A selected-field inspection of the unchanged pinned catalog confirms 11 models:
10 have `tool_mode: code_mode_only`; `gpt-5.5` alone has `tool_mode: null`,
`use_responses_lite: false` and `experimental_supported_tools: []`
(`models-manager/models.json:1349,1365,1368,1430`). Its catalog lists `low`
effort. With the existing false CodeMode/CodeModeOnly flags,
`core/src/tools/mod.rs:75-85` resolves that original metadata to Direct mode;
`core/src/tools/spec_plan.rs:825-828` then skips wrapper registration. This is
a source-supported way to avoid the demonstrated Code Mode cell path, not an
additional teardown RPC or native isolation proof.

If the coordinator needs a model-naming alternative, explicitly selecting such
a model is a possible separate decision. It requires serving availability and
exact-effort validation, naming quality/cost/latency assessment within the
unchanged ten-second budget, and review/native proof of its actual Direct-mode
tool catalog, dispatch and non-Lite protocol behavior. Catalog presence alone
does not establish account availability or suitability. The pending native
logging decision and all other isolation gates remain independent.

Historical status: this alternative required explicit selection and was not an
automatic model fallback. The coordinator subsequently selected `gpt-5.5/low`
as recorded below. The scoped teardown API gap for unchanged Luna remains valid;
it is avoided only when the utility actually resolves to the supported Direct
profile. No model was queried through inference in this design investigation.

## Selected Direct profile and serving-catalog gate

Decision and scope: the coordinator explicitly selected `gpt-5.5/low` for
automatic naming. This supersedes the utility's earlier Luna selection and the
proposed positive Code Mode/V8 fixture lanes, not ordinary development-team or
watcher settings. The user-approved boundary remains model naming with no
file/network action tools and immediate question rejection. Pure computation
or clock permission is not a requirement to expose those capabilities. There
is no alternate-model retry. Keep the ten-second whole-call budget, two calls
per workspace, first 8 KiB of raw UTF-8 text, existing output validation,
deterministic fallback, and dispatched-attempt/crash bookkeeping unchanged.

Evidence here refers to unchanged Codex 0.160.0 source at
`/nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source/codex-rs`, provider predecessor
`4651d76447cdbd1fa742358baeef01f0ebcdf250`, and runtime predecessor
`8acd722029f3c1d0abd8c2801b734a554a4a2eef`. Implementation is pending; frozen
uncommitted wrapper-fixture work is not an accepted compatibility requirement.
The coordinator's installed portal `GET /api/models` observation establishes
advertised `gpt-5.5`/`low` availability, not its tool mode. The official
[GPT-5.5 model page](https://developers.openai.com/api/docs/models/gpt-5.5)
documents low effort and structured outputs, with published API rates of
$5/M input and $30/M output tokens. These prices do not establish serving
ChatGPT/Codex quota charges, parity with Luna, naming quality, or latency.

### Original metadata, expected catalog and request shape

The original `models-manager/models.json:1349,1365,1368,1430` entry has
`slug=gpt-5.5`, `tool_mode=null`, `use_responses_lite=false`, supported effort
`low`, and no `experimental_supported_tools`. With the existing false
CodeMode/CodeModeOnly flags, `core/src/tools/mod.rs:75-99` selects Direct;
`core/src/tools/spec_plan.rs:825-828` returns before registering exec/wait.
Async questions require experimental metadata (`spec_plan.rs:1178-1202`),
clock requires metadata or CurrentTimeReminder (`1225-1233`), and ordinary
questions require the explicitly disabled setting (`1169-1175`). Thus the
expected **normal utility catalog is empty**, including no clock, async
question, exec or wait. This is source inference under that effective metadata,
not an observed native pass or permission for a wrapper allowlist.

Retain all 55 fixed restriction settings byte-for-byte, including false
CodeModeInterrupt, empty environments/roots/dynamic tools, captured MCP-name
disables, disabled action/hosted search/image/app/plugin/delegation tools,
memory/goals/hooks, and project/workspace/team instruction isolation. Non-Lite
mode can otherwise expose hosted tools; it does not itself disable search.
The existing restrictions still own that boundary. Hidden registered handlers
must also reject hostile dispatch; an empty advertised list alone is not proof.

`core/src/client.rs:902-938,989-1007` builds non-Lite Responses with top-level
`instructions` and `tools: []`, not the Lite developer `additional_tools`
catalog. Assert the explicit base-instruction sentinel at that actual location,
`model=gpt-5.5`, `reasoning.effort=low`, the requested structured-output schema,
`store=false`, and streaming. Non-Lite reasoning omits the Lite `all_turns`
context (`client.rs:870-880`). Do not invent a `tool_choice=none` override:
the native request uses `auto` with the empty tool list. Keep builtin OpenAI,
original metadata and exact binary. The mock returns 426 only to real WebSocket
Upgrade requests, retains plain GET 404 and verifies actual POST inference.
That proves the supported native HTTP fallback path, not WebSocket frames;
the live positive canary must use unchanged serving transport.

### Public helper boundary and the unresolved production prerequisite

Keep `EphemeralTurnOptions.Model` and `Effort` explicit. Select a narrow private
supported-profile predicate, initially the exact pair `gpt-5.5`/`low` only;
reject unsupported pairs with `ErrEphemeralSettings` before connecting or
starting a thread. Preserve context-cancellation precedence and existing
isolation validation. No aliases, implicit defaults, alternative model, new
public profile/config map, caller tool override, or metadata-path convention is
needed. Existing model/list pagination still verifies exact availability and
effort, and both starts still forbid substitution. This limits the unreleased
API's supported surface; it is **not a security proof based on a model name**.

The reusable caller precondition is a serving profile whose effective model
metadata is established to resolve to Direct with the empty experimental-tool
set and the tested non-Lite request path. Public API docs must explicitly say
that this helper does not support CodeModeOnly models or certify an arbitrary
daemon/catalog. No supported per-call capability attestation was found:

- `app-server-protocol/src/protocol/v2/model.rs:119-178` exposes model identity,
  effort and other picker metadata, but omits `tool_mode`,
  `experimental_supported_tools` and `use_responses_lite`. Provider capability
  RPC fields (`41-50`) also do not attest the selected model's tool registry.
- `models-manager/src/model_info.rs:20-60` applies instruction/context/output
  overrides, not tool mode. Model metadata takes precedence over feature flags
  in `core/src/tools/mod.rs:75-99`. No thread/turn setting forces Direct against
  a refreshed CodeModeOnly entry.
- The manager is shared startup state (`core/src/thread_manager.rs:432-444`).
  A per-thread `model_catalog_json` path does not replace it. Do not use that
  path as a purported scoped fix, mutate shared metadata/cache, or add an
  inferred capability field to the protocol corpus.

The original bundled entry does **not** establish the production precondition.
`models-manager/src/cache.rs:65-86` stores full `ModelInfo`; eligible cached
entries are version/identity/TTL checked and applied (`manager.rs:704-753`,
`cache.rs:184-226`). A fetched catalog replaces matching bundled entries, or
becomes remote-only for eligible authenticated catalogs (`manager.rs:672-700`).
Root session startup calls OnlineIfUncached (`core/src/session/mod.rs:638-652`),
as does model/list (`app-server/src/request_processors/catalog_processor.rs:280-294`).
The app-server refresh worker calls Online immediately and every 270 seconds
(`app-server/src/models_refresh_worker.rs:9,39-59`); a response ModelsEtag can
refresh the same manager (`core/src/session/turn.rs:2924-2929`). Model resolution
then reads that shared catalog (`core/src/session/step_settings.rs:243-253`).
These are ordinary native operations, not only administrator reconfiguration.

The API-key mock's bundled-only path follows
`models-manager/src/manager.rs:545-553`; a serving Codex/ChatGPT identity can
refresh through `665-668`. A one-time cache read, matching binary, model/list
response, or successful canary cannot bind later session resolution to the
inspected metadata. Cache write failure also does not prevent in-memory catalog
replacement (`579-648`). Do not add cache polling, a cache lock, sleeps, or a
name-only admission claim to disguise this gap.

Consequently model naming must remain unenabled on a serving instance whose
compatible effective catalog cannot be established and kept within this
profile. The coordinator must resolve this concrete prerequisite before live
utility inference/deployment; retain the deterministic fallback when the
application cannot call a supported utility. The current public RPC cannot
automatically refuse a same-named model whose hidden tool mode changed before
inference. That limitation must remain explicit, not advertised as fail-closed
per-call metadata validation.

Smallest source-supported fixed-catalog alternative, **not selected or
authorized here**: startup `model_catalog_json` creates `StaticModelsManager`
(`model-provider/src/provider.rs:421-430`; manager methods `794-826` ignore
refresh). Supplying an unchanged original catalog could preserve its actual
metadata without editing entries, but changes the shared serving catalog and
requires operator selection, startup/restart and assessment of ordinary-model
availability. It is not a per-call remedy and is outside the current no-global-
configuration-change scope. Existing API-key bundled-only operation is another
bounded source profile, not permission to change production authentication or
account charging. Under the currently authorized unchanged dynamic daemon,
there is no proven automatic pre-inference Direct guarantee. No new process,
Codex patch, model rewrite or relaxed lifetime is proposed.

### Bounded implementation and native proof changes

Implementer-owned changes are limited to the helper's supported-pair guard and
tests, explicit model selection in `portal/internal/web/session_namer.go`, its
focused adapter expectations, and the tagged fixture/corpus expectations.
Lead-owned public documentation must state the supported serving profile and
catalog limitation in codex-web `docs/reference.md`, with the consumer contract
linked from runtime `docs/session-preparations.md`. Do not extend CLI naming,
change the browser/worker/upload design, or introduce an enablement framework.

The fixture must switch normal utility and ordinary positive-control model/
effort coherently to `gpt-5.5/low`, validate the original selected metadata, and
inspect the actual non-Lite request representation. Retain all eight ordinary
source/action controls so disabled utility inheritance is meaningful. Ordinary
controls intentionally have enabled tools and are not subject to the utility's
empty-catalog expectation. Neither a synthetic fixture nor a new Go unit test
can attest the production dynamic catalog described above.

| Case | Required evidence under the selected profile |
| --- | --- |
| Normal utility | Native POST, exact model/low, empty direct catalog, exact structured result; no Lite catalog or wrapper exposure. |
| Absent tools | Inject real native calls for clock, async question, exec/wait and representative forbidden action handlers; observe registry rejection and no side effects, including hidden dispatch. Do not claim a clock/question handler ran because the model emitted its name. |
| Actual server-ID question control | A separately labelled fixture control enables only the existing ordinary request-user-input setting; preserve its native Plan-mode eligibility with gpt-5.5. Reach the actual server request ID and private `-32601` response before UI admission; production settings remain unchanged. |
| Async notification sink | Keep bounded transport/unit coverage for real protocol Async delivery/questions without a request ID, including early notifications and malformed/conflicting identity. Fail immediately, without fabricated response, UI, timers or persistence. Do not add metadata just to produce a native async handler. |
| Question at cancellation | Use the actual server-ID question control, observe native POST plus that request before cancellation, then require context cancellation/private teardown. An unrelated item/started is not the target. |
| Early/lost turn response | Preserve exact generation/thread/turn ownership, no resume/adoption or repeat. Use a tool-free native turn with a withheld final stream and a lost turn/start RPC reply, so actual early identity and interruption are exercised without a successful clock call. |
| Timeouts and continuity | Retain both reached/withheld 400 ms preflight controls, inference stall/cancellation/disconnect and ordinary concurrent-thread continuity within the original budget. |
| Isolation and persistence | Preserve exact denied-counter baseline, positive egress controls, canary files, current MCP/config conflicts, managed restrictions, SQLite and rollout/submission/history assertions, and final snapshots. No resets, ignored owners, sleeps or weakened assertions. |

Delete obsolete positive wrapper/V8/cell-lifetime fixture lanes from the intended
implementation instead of retaining unreachable Luna compatibility branches.
At most retain a small unsupported-Luna **pre-inference rejection** unit case.
No exhaustive V8 test expansion is useful for this Direct-only profile. A
hostile exec/wait dispatch must demonstrate registry rejection, not start a
cell and infer its death from subscriber removal. The source teardown gap is
unchanged; exact interruption on failure and bounded unsubscribe/private close
remain useful, but neither promises immediate native thread unload or joins a
Code Mode cell. Do not enable CodeModeInterrupt or add success interrupt as a
substitute for establishing the supported profile.

Private cwd, fixed nonempty `EphemeralInstructionFileContent`, explicit base/
developer overrides, global user-policy inheritance and immutable file lifetime
remain unchanged. So does the observed native diagnostic persistence issue:
earlier native evidence found synthetic prompt/owned-ID data in
`logs_2.sqlite`/`logs`; ephemeral/non-stored Responses do not imply no daemon
logging. The logging choice remains independently pending and the strict native
assertion stays. This decision grants no privacy waiver or release pass.

### Quick and release gates; commands are proposed, not executed

From the codex-web feature worktree, after the bounded edits:

```sh
nix develop .#checks.x86_64-linux.default -c go test -mod=readonly ./codex -run '^TestEphemeral' -count=1
nix develop .#checks.x86_64-linux.default -c go test -mod=readonly -race -tags=codex_integration ./codex -run '^TestEphemeralIntegration' -count=1
nix develop .#checks.x86_64-linux.default -c python3 test/codex_protocol_contract.py --coverage-only codex/client.go
nix develop .#checks.x86_64-linux.default -c python3 test/codex_ephemeral_config_contract.py /nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source/codex-rs/core/config.schema.json
```

The tagged quick selector is fixture logic, not the differently named native
`TestEphemeralProtocolIntegration`. Add focused pair rejection cases with zero
thread/turn calls, exact accepted requests, unavailable/effort mismatch, and
direct-catalog request parsing including unexpected nonempty/wrapper catalogs.
Do not fabricate metadata fields in model/list tests. From runtime:

```sh
nix develop .#packages.x86_64-linux.dev-workspace -c env -u PORTAL_BROWSER_TEST sh -c 'cd portal && go test -mod=readonly ./internal/web -run "^TestSessionNamingUtility" -count=1'
```

Retain `-mod=readonly` because package-derived environments export vendor mode;
these `nix develop` selections are package/check derivations, not a devShell API.
After quick checks, commit and independently review affected provider/fixture/
consumer/docs lanes through the coordinator. Then a fresh watcher runs the
existing prepared native environment, exact original source/binary/hash and
network/SQLite prerequisites, using:

```sh
go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeralProtocolIntegration$' -count=1 -timeout=180s
```

That suite timeout does not change the ten-second utility deadline. Missing
metadata prerequisites, an unexpected tool, unexplained denied packet, prompt
persistence under the still-strict requirement, or a skipped downstream gate
is not a pass. Complete the exact-binary matrix, resolve the serving-catalog and
logging gates, and obtain a successful real positive naming canary under ten
seconds; deterministic fallback is not canary success. Refresh final packaged
checks/resource hashes/dependency pins through their owners. Existing browser,
Ruby lifecycle, old-reader and host-migration checks need repetition only if
their owning behavior changes; this model/profile/fixture correction adds no
receipt/upload schema, journal, migration, host path, cluster policy or exported
host-contract change. Preserve deployed runtime `4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4`
and extension `399c33023a568a8d7a21e4e4df52829628720a28` ancestry. Recovery remains a
newer assembled user-profile package containing prior behavior, never an
earlier-profile switch or rollback.

Only this assigned design document was edited. No source/test/config/cache
changes, inference, checks, Git operations, deployment or session lifecycle
actions were performed. The coordinator owns resolution of the production
catalog gap and all implementation/verification/rollout assignments.

## Candidate naming-only static runtime

Status: design recommendation for coordinator selection, not an implemented or
verified deployment. Run one additional standard Codex app-server for each
portal service lifetime. Only the naming adapter uses it. Keep the ordinary
socket, dynamic catalog, team registrations and existing serving identity
unchanged. The second process uses the same pinned native binary, existing
auth/provider configuration and the complete unchanged original catalog, loaded
through a startup CLI override. It is not a session/team member, independent
systemd service, per-call process, or new lifecycle authority.

This resolves the dynamic-catalog problem through a separate supported static
manager, conditional on the startup/config-read checks and native proof below.
It does not solve or waive the pending logging boundary. All 55 per-call
restrictions, gpt-5.5/low selection, question handling and the preceding Direct
fixture requirements remain in force. No global catalog pin, reduced catalog,
model metadata rewrite, Codex patch or new dependency input is needed.

### Catalog and startup evidence

The full original file is 472512 bytes with SHA-256
`fd219bd9f061278275f528939f82f54d2eb97df4b25c23b022adbe48813d920b`.
This was checked by read-only hashing of the pinned source. The coordinator's
Nix evaluation confirms that the existing selected upstream `codex.src` is
`/nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source`; its resource is
`codex-rs/models-manager/models.json`. Package those exact full bytes at
`share/workspace-portal/codex-models.json`. Do not serialize selected entries or
copy a mutable live `models_cache.json`.

The source chain is concrete:

1. `cli/src/main.rs:1219-1272` passes root `-c` overrides to the standard
   app-server. `app-server --strict-config` is supported (`553-572`) and
   prevents a configuration-load failure from silently choosing defaults
   (`app-server/src/lib.rs:554-575`).
2. App-server parses overrides once into ConfigManager (`lib.rs:517-539`),
   then loads the startup config. `core/src/config/mod.rs:2143-2171,4074`
   reads and parses the full catalog before building the manager.
3. `app-server/src/message_processor.rs:334-338` calls
   `core/src/thread_manager.rs:432-444` with that startup config;
   `model-provider/src/provider.rs:421-430` selects StaticModelsManager when
   a catalog is present. `models-manager/src/manager.rs:794-827` returns its
   retained catalog and ignores refresh/ETag requests. Neither ordinary remote
   refresh nor cache loading can replace this manager's selected metadata.

Use a direct argv, with TOML-string encoding of the absolute catalog path, not
a shell command or credentials interpolated into flags:

```text
<package-native-codex> -c model_catalog_json="<canonical-packaged-catalog>" app-server --strict-config --listen unix://<owned-runtime-alias>
```

The native entrypoint in the assembled workspace package is exactly
`<packageRoot>/libexec/codex/libexec/codex/bin/codex`: the first component is
the link installed by `nix/workspace-portal.nix:260`, and the assembled package
layout comes from `nix/codex-package.nix` and `docs/codex-package.md`. Resolve
the trusted package path once. Do not use PATH, a daemon updater-selected copy,
or the mutable system command; do not edit wrappers/native assembly. A bounded
startup version probe (at most two seconds) of this same immutable executable
must require 0.160.0;
package/native checks establish its exact bytes. A failed probe disables naming
for that service lifetime. It must not block the portal or extend a naming
call's budget.

Set the child's CODEX_HOME to the already host-selected
DEV_WORKSPACE_CODEX_HOME; otherwise preserve the trusted service auth/provider
environment. No credentials are copied, printed, passed in argv or placed in a
new home. Do not append ordinary team-registration `-c` arguments. Start in an
empty private cwd outside project trees. This retains global user policy and
existing account configuration while excluding project configuration at
startup; each utility still has its own empty cwd and fixed instruction file.

One additional version-bound launcher setting is necessary for a naming-only
child: set `CODEX_INTERNAL_APP_SERVER_REMOTE_CONTROL_DISABLED=1` in **that
child's environment**. Pinned upstream's own daemon uses this exact marker
(`app-server-daemon/src/backend/pid.rs:404-410`); the CLI consumes/removes it
before worker startup and selects DisabledEphemeral
(`app-server-transport/src/transport/remote_control/mod.rs:79-95`,
`cli/src/main.rs:1249-1258`). Plain app-server otherwise resolves the existing
persisted remote-control preference. This is an existing internal native launch
interface tied to the pinned version, not a newly invented public config key.
It must receive affected-lane review and native coverage. Do not alter global
enrollment or use `--managed-daemon`; the latter requests saving loaded threads
on shutdown. No new model-action capability is enabled by this launch recipe.

### Provider preflight: check CLI origin as well as immutable bytes

Add required trusted `ModelCatalogFile string` to EphemeralTurnOptions. Keep
the exact gpt-5.5/low profile guard. Before connecting, require a canonical
absolute regular read-only file, bounded to at most 1 MiB, with the exact full
catalog SHA-256 above. The supported caller supplies an immutable resource for
the daemon's entire lifetime; the deployment supplies a regular Nix-store
resource. It is public metadata, so do not reuse private InstructionFile
ownership/mode-0600/hardlink rules or introduce compromised-operator filesystem
defenses. Resolve package links before supplying the canonical file path. A
missing, writable, wrong, oversized or changed resource fails with the static
isolation error. Keep source/profile digest ownership in codex-web; the
consumer must not accept a caller-supplied hash or Boolean assertion.

On the private connection's existing config/read, before thread/start, require
both:

```text
config.model_catalog_json == opts.ModelCatalogFile
origins["model_catalog_json"].name.type == "sessionFlags"
```

Continue to use `includeLayers=false`. Source evidence:
`app-server/src/config_manager_service.rs:123-175` resolves current layers with
the retained CLI overrides and returns both effective config and origins;
only the full layer list is conditional. The path is retained in ApiConfig's
flattened additional fields (`app-server-protocol/src/protocol/v2/config.rs:278-315`).
`SessionFlags` serializes as `sessionFlags` (`29-31,96-97`), inside each
origin's `name` (`321-324`). Check typed structure and exact path; missing,
malformed, user/project/managed origin or conflicting requirements fail closed.
Do not require or log complete layers/configuration.

Why the origin matters: a dynamic daemon could later read an original-catalog
path written into user config without replacing its startup manager. Such a
path-only response is insufficient. ConfigManager captures the CLI vector at
construction and only reads it thereafter (`config_manager.rs:75-85,116-121`);
config/read reuses it (`481-500`). Ordinary config writes do not mutate it.
SessionFlags outranks user/project sources (`config/src/config_layer_source.rs:33-49`).
Higher legacy-managed layers change the origin; exact managed requirements
remove their paths from origins (`config_manager_service.rs:141-156`), so the
proposed check refuses these ambiguous cases even if their path happens to
match. No catalog is added to thread/start or turn/start config.

Together, the owned pinned child, unchanged immutable file, retained CLI-origin
check and source-selected static manager establish this finite profile. This
is not cryptographic remote attestation of an arbitrary server. Trusted operator
changes to managed policy, authentication/provider settings or the resource
require stopping/restarting naming through existing service/package procedures;
there is no configuration lease. Ordinary user-config writes cannot replace
the startup CLI catalog. MCP capture remains per call with every configured
literal name disabled; pause naming before operator MCP reconfiguration as
already required. Native proof must confirm the path/origin wire representation,
CLI precedence and static refresh behavior before relying on this recipe.

### Portal-owned lifetime and bounded failure behavior

Add one private owner in `portal/cmd/workspace-portal/naming_runtime.go`, wired
from `serve` in `main.go`. Existing `--package-root`, `--unix-socket` and
host-selected CODEX_HOME inputs suffice; `libexec/workspace-host:1225-1262`
already supplies them. No new host launcher flags, runtime-contract fields,
service unit or PID/journal record is needed. Create a unique mode-0700
directory under the existing workspace runtime parent, containing an empty
startup cwd and this lifetime's socket alias. Never reuse/adopt a previous
process or discover a peer from another service/session.

Pinned Unix transport intentionally publishes a rendezvous symlink to its
hashed mode-0600 physical socket (`app-server-transport/src/transport/unix_socket.rs:50-110,282-295`).
Preserve that supported layout; do not reject the expected alias, reimplement
its hashing, scan/delete upstream socket directories, or copy daemon state.
The runtime directory belongs only to the portal lifetime; remove it after the
owned process/group has been stopped and joined. Forced death can leave native
stale socket/lock artifacts under native ownership; that is not a live process
or permission for a new daemon-state reconciliation framework.

Use the existing `portal/internal/processgroup` ownership pattern. Its
RunGraceful starts a separate process group, waits, sends TERM on cancellation,
then KILL after a bounded grace; WaitDelay is two seconds. Its early normal-exit
branch does **not** kill remaining descendants. The private owner must account
for that branch too, either by a small local lifecycle wrapper following the
same pattern or a narrowly reviewed reuse that kills the owned residual group
on every exit. Do not broaden unrelated subprocess APIs merely to manage one
child. Exactly one waiter reaps the child; Close is idempotent and joins it.
Use a two-second graceful stop, then group KILL and wait. Keep process output
discarded, with only fixed startup/exit categories in portal diagnostics; do not
relay native stderr/configuration/prompts into portal logs. Existing native
SQLite logging is still governed by the unresolved privacy gate.

Start once per serve lifetime, with no automatic retry/backoff/respawn loop.
The bounded version probe and child startup may run while the portal becomes
available; naming is unavailable until the child accepts a private helper
connection. Each call's existing initialize/config-read/profile/model preflight
is the readiness gate, within that call's original deadline. Connection refusal
while starting, startup error, invalid profile, child loss or timeout yields
the existing deterministic fallback. There is no wait outside the ten-second
queue/setup/inference/cleanup budget and no replacement inference after loss.
Restarting the portal through normal operator procedures gives a new lifetime.
Never redirect a failed naming attempt to the ordinary socket.

Add internal web Config fields `NamingSocket` and `NamingModelCatalogFile`;
normalSessionNamer uses those only, passes ModelCatalogFile, and retains
gpt-5.5/low. Remove its default routing through Config.CodexSocket. Preserve
SessionNamer injection for tests. When startup configuration is missing or the
owner cannot start, leave naming unavailable and keep ordinary portal behavior.
The ordinary client/controller and its ledger still use Config.CodexSocket.

Arrange one cleanup path for constructor/listener failures, HTTP errors and
signals. On graceful shutdown: stop admissions and call application.Close;
that cancels operations, waits workers and pauses preparations
(`server.go:598-607`). Keep the child available during bounded worker interrupt/
unsubscribe cleanup; then cancel and join the owned child before serve returns.
Do not let the HTTP-error return path skip application.Close or child cleanup.
Do not turn shutdown cancellation into a committed fallback or reservation;
existing preparation context and generation checks remain authoritative.

The current portal unit has KillMode=mixed and TimeoutStopSec=150s; the main
HTTP shutdown allowance is 130s (`main.go:304-318`). Mixed mode's initial TERM
must not be treated as child cancellation. Explicit stop/join fits the remaining
service allowance; the systemd cgroup is the final forced-exit boundary for all
descendants, even if the portal dies abruptly. Test that actual managed-service
case. Do not promise equivalent forced-parent cleanup for an uncontained manual
launcher. This child is outside session/team registration and cluster ownership.

### Implementation units, compatibility and verification

| Owner/file area | Bounded change |
| --- | --- |
| codex-web `codex/ephemeral.go`, focused tests and reference | Required immutable ModelCatalogFile; exact digest and startup CLI-origin check; supported gpt-5.5/low profile, unchanged 55 restrictions and private protocol flow. |
| Runtime `portal/cmd/workspace-portal/{main.go,naming_runtime.go}` and focused tests | One owned child/group, package-derived paths, existing auth environment, startup/loss/failure/shutdown handling with join. |
| Runtime `portal/internal/web/{server.go,session_namer.go}` and adapter tests | Separate trusted naming socket/catalog; no ordinary-socket fallback; unchanged worker deadline and state ownership. |
| Runtime `flake.nix`, `nix/workspace-portal.nix` and package assertions | Pass original catalog from already selected codex.src, install full immutable resource, compare source bytes/hash and native version/layout. No native assembly or input changes. |
| Lead-owned documentation | Provider profile in codex-web reference; child lifetime, operator restart/MCP rules and fallback in runtime session-preparations/portal/codex-package docs. Remove obsolete shared-socket/Luna claims. |

This adds transient portal-owned process/socket state and an immutable package
resource. It changes no receipts, journals, preparation/upload schemas, authority
records, namespace migration inputs, cluster policy or exported host contract.
The consumed runtime 4ef and extension 399 ancestors remain unchanged. Existing
package activation/reconciliation restarts portals and therefore their children
(`workspace-host:1075-1078,2710-2722`); generation checks continue to reject an
old worker's mutation. No new host-namespace migration VM trigger follows from
this design, but service-child cleanup is new owning behavior and needs a
targeted packaged service-lifetime test. Forward recovery selects a newer
assembled user-profile package; no earlier switch/rollback is introduced.

Quick checks extend the previous provider/adapter commands. Add meaningful
provider cases for wrong hash/path/mode, no startup origin, matching path with
user origin, matching CLI origin, requirements conflict and zero thread/start
on failure. Preserve the request corpus and config-key validator. Add owner
tests for startup error, not-yet-listening fallback, no respawn/adoption, child
exit with descendants, repeated Close, cancellation during naming, constructor/
HTTP failure and ordinary-client socket separation. Proposed owner selector
awaits the implementer's actual test names:

```sh
nix develop .#packages.x86_64-linux.dev-workspace -c env -u PORTAL_BROWSER_TEST sh -c 'cd portal && go test -mod=readonly -race ./cmd/workspace-portal ./internal/processgroup ./internal/web -run "^(TestNamingRuntime|TestSessionNamingUtility|TestRunGraceful)" -count=1'
```

After committed quick verification and affected-lane independent review, use a
fresh watcher for the tagged native fixture and packaged checks, retaining the
existing exact native command. The fixture now starts its utility daemon with
the same full static CLI catalog, strict config and local-only launch marker;
ordinary controls retain their ordinary profile. Prove config/read path and
sessionFlags origin with includeLayers=false; a dynamic daemon whose user
config later gains the same path must be rejected before inference. In private
fixture configuration, show that ordinary config writes cannot replace the CLI
catalog, managed conflicts fail, and ETag/catalog-refresh events cannot replace
the static manager. Never alter the original catalog to manufacture a pass.

Retain empty Direct catalog, hidden hostile dispatch, actual server-ID question,
private async sink, early/lost responses, deadlines, denied-counter/canary/MCP/
persistence and ordinary continuity gates. Add a bounded real child-service
smoke proving two-slot calls use one child, failed startup falls back, signal/
HTTP failure/forced portal exit leave no live child group, and an ordinary
concurrent app-server remains usable. Run it in the reviewed disposable managed
service fixture or existing host VM, not by mutating a live workspace. Package
checks from the runtime worktree include:

```sh
nix build .#checks.x86_64-linux.package .#checks.x86_64-linux.codex-package .#checks.x86_64-linux.host-package-contract --print-build-logs
```

No devShell API is assumed.

The final real-provider positive naming canary must use this exact static child
profile, existing serving identity and unchanged native transport, and obtain
an actual valid model result inside ten seconds. The old shared-daemon canary
is no longer representative. Logging choice/strict assertions remain pending;
fallback or a mock-provider pass cannot waive them. Refresh final package and
resource hashes/pins through their owners after review and verification.

No application edit, test, inference, Nix evaluation, config/cache change,
process launch/stop, Git operation, deployment or session mutation was performed
for this supplement. The coordinator owns acceptance and assignments.

## Prepared managed-child smoke boundary (2026-10-04)

The preceding static-runtime proposal has since been selected and implemented
in source, including the extracted `servePortalHTTP` cleanup path; this is a
source checkpoint, not packaged/native verification. The currently available
older ca/42/2e/f5 package does not contain that checkpoint. Final pins, package
and resource hashes remain coordinator-owned and pending. See the concrete
[managed-child smoke brief](managed-child-smoke-brief.md) for the proposed
fixture entries, exact serve argv, private inputs, commands and acceptance
observables. The brief is prepared; no fixture was launched or claimed to pass.

Use a disposable VM with a real systemd user manager and the eventual exact
assembled package. Runtime `nix/tests/host-module-idempotency.nix` establishes
the existing NixOS VM/user pattern but its fake router does not test this child.
A bounded session VM wrapper and tagged command-package native fixture are
still needed. Do not assume that a host user unit inherits the invoking
fixture's network namespace. The selected VM confines both systemd-launched
native processes and its synthetic mock provider to loopback, with a completed
negative control and unchanged denied counter. All homes/config/auth/provider
values are private and synthetic; no live serving state is mounted or copied.

Actual `main.go:newServeFlagSet/serve` and `server.go:New` support a private
workspace, existing private transition lock, private profile symlink and
authority/user-state directories while loading the real candidate package's
team catalog. The mandatory registration-marker path must be named
`registration.json` next to the ordinary Codex socket, but this admission path
does not read marker contents. Leave it absent; do not fabricate a registration
record or invoke host registration/lifecycle helpers. Parse the actual GET `/`
form for date/team/catalog digest and submit a fresh UUID request. The existing
`--dev-session` input can select a private fixed-failure helper to prevent real
session initialization after naming. This is a preparation/naming test, not a
successful creation or host-registration test. Preserve generation and package
validation rather than disabling them. Recheck these source conditions at the
final frozen head.

The packaged managed-unit cases cover one native child with two concurrent
naming slots, deterministic startup/loss fallback without ordinary-socket
routing, graceful MainPID TERM, and forced MainPID KILL followed by real cgroup
cleanup. Use the packaged KillMode=mixed/150-second stop policy, with a
documented fixture-only Restart=no to observe one lifetime. A separate real
ordinary native AppServer remains usable throughout. Its bounded private RPC
proxy proves absence of attempted naming routing, including attempts that fail
before provider inference. Capture native executable hash, PID start identity
and cgroup; parent exit or socket disappearance is not child-termination proof.

There is one precise owning-fixture extension: the unmodified packaged CLI
offers no supported external listener-close operation. Unlinking a bound UDS
does not cause HTTP Serve failure. Add a tagged real-native counterpart of
`TestNamingRuntimeHTTPExitKeepsChildForWorkerCleanup`, calling the existing
`servePortalHTTP` with its own listener and closing it only after an actual
naming provider POST. Require application worker cancellation while the child
is alive, then explicit child stop/join, plus ordinary continuity. This tests
the production function at reviewed source, and must not be labelled a forced
HTTP failure inside the packaged executable. No new product flag or fault
framework is justified. The companion packaged cases establish the process
and systemd boundary.

The prepared brief assigns only these finite fixture additions and their
manifest guards; implementation/review and long execution remain pending.
Native isolation, strict persistence assertions, the unresolved logging choice
and the unchanged-transport real-provider naming canary remain separate release
gates. A lifecycle smoke pass cannot waive them. The fixture uses the original
catalog/gpt-5.5/low and supported built-in HTTP fallback, changes no model or
55-key restriction, and adds no state/host migration contract. Retained 4ef/399
ancestry and forward-only recovery remain unchanged. Existing browser,
old-reader and unrelated host-migration evidence needs repetition only if its
owning behavior changes. No app/test changes, tests, process/network operations,
Git/pin/deployment or session mutations were performed for this supplement.

## Static-profile persistence diagnostic: ordinary background work (2026-10-04)

Scope: read-only assessment of provider `1be5ba65da7d2e2876804cb809b1fe398bdd50a7`
(code/tests equivalent to reviewed c8a9), runtime 1219d9a, and the pinned
0.160.0 source at
`/nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source/codex-rs`.
This is a proposed fixture correction for coordinator selection. No application
defect, isolation pass or logging-policy change is established by this analysis.
The independent managed-child fixture work is outside this supplement.

### Observed evidence and its limits

Bounded parsing of `automatic-session-slugs-static-profile-native-summary.json`
and its private synthetic log in `/tmp` confirms 38 phase records with fixed
deny counts 2→2 and no counter-unavailable or tool-schema diagnostic. The
dynamic-catalog control's zero inference is its expected negative result.
Five early errors name the same shell snapshot and four name
`memories_1.sqlite`; these are nine failed comparisons, not evidence of nine
distinct writes. `verifyPersistence` iterates a Go map and reports its first
mismatch, so alternating filenames do not establish an alternating write order.

The snapshot prefix is **not the recorded control root ID**: the root is
`01a10503-e1b4-7ec0-9051-b3fc367a290a`, whereas the named snapshot begins
`01a10503-e22f-7b43-b7f8-725d46e3e0cd`. The latter also matches none of the 35
nonempty utility ThreadIDs in the phase evidence. These are synthetic fixture
identities. The log does not retain whether that file disappeared or changed
contents, its writer PID, or the changed memory SQL rows. Do not call it a
control-root snapshot, a utility snapshot, or a confirmed consolidation snapshot
without that missing attribution.

`codex/ephemeral_integration_test.go:2816-2913` hashes ordinary files and compares
the complete logical `.dump` of goal/memory databases. A memory mismatch is not
merely an mtime/WAL/checkpoint difference, but it also does not prove the seeded
memory row changed: the dump includes job and migration tables. The same scan
checks utility markers/IDs before retaining comparison data. Later 28 bounded
diagnostics independently identify utility input/IDs in `logs_2.sqlite`, table
`logs`. That strict logging failure remains real and unresolved; attributing
other changes cannot waive it. Early absence of this diagnostic is not proof
that logging was disabled or that later content belongs only to later calls.

### Pinned source establishes an insufficient fixture completion barrier

Both fixture app-servers use exactly the same HOME/CODEX_HOME
(`ephemeral_integration_test.go:1181-1210`). The ordinary eligibility control
enables memories and starts a persistent root turn. `control:1871-1893` waits
only for that turn's completed status, then seeds the goal/memory rows and
takes the persistent baseline. Native turn completion does not join the
following separate work:

- `app-server/src/request_processors/turn_processor.rs:686-699` starts the
  memory startup pipeline after accepting an eligible started turn.
  `memories/write/src/start.rs:24-92` spawns it without a retained join handle.
  It skips ephemeral/MemoryTool-disabled/non-root sessions, but the ordinary
  control intentionally qualifies. Utility calls have both ephemeral mode
  and `features.memories=false`, so this entry does not launch their pipeline.
- The pipeline prunes before checking quota and later runs extraction and
  consolidation. `memories/write/src/phase1.rs:96-117` calls
  `state/src/runtime/memories.rs:403-435`, which deletes unselected stage-1 rows
  older than its cutoff using `COALESCE(last_usage,source_updated_at)`.
  The fixture's seed has `source_updated_at=1` and `generated_at=1`
  (`seedSensitiveStores:1936-1951`), so a still-pending ordinary prune can delete
  it. This is a concrete eligible writer, not proof that this run's seed was
  deleted. Global consolidation also writes `jobs` independently of model
  output (`state/src/runtime/memories.rs:1077-1147` and phase2 job completion).
- Consolidation can start a distinct internal MemoryConsolidation thread
  (`memories/write/src/runtime.rs:398-423`). Its config is ephemeral and disables
  recursive memory work, but clones the ordinary config and does not disable
  ShellSnapshot (`phase2.rs:294-322`; the feature defaults on in
  `features/src/lib.rs:1014-1019`). Its separate completion task shuts down and
  removes that agent, then finishes job/artifact accounting
  (`phase2.rs:376-441`, `runtime.rs:445-459`). This is a source-supported
  candidate for the third, non-utility ID, still unconfirmed for this run.
- `core/src/session/session.rs:1408-1429` enables or disables the snapshot
  builder by feature. The utility policy disables both shell-snapshot flags.
  Ordinary environment setup independently spawns its snapshot future
  (`environment_selection.rs:373-405`). `shell_snapshot.rs:258-327` names a file
  with the owning thread ID plus nonce and publishes it by rename;
  `ShellSnapshotFile::drop:528-536` removes it. Its separate stale cleanup
  (`1123-1181`) can remove snapshots lacking a rollout, excluding only the
  invoking active ID. These native temporary files are not immutable archives.

The shared home makes ordinary work visible to both daemons and the whole-home
oracle. Two daemons alone do not prove a shared-store bug. The inspected utility
gates do not start either ordinary pipeline; the current evidence cannot assign
the reported changes to a particular PID. Nor should the memory mismatch be
excused as generic SQLite maintenance: the memories DB has background
reclamation disabled (`state/src/sqlite.rs:81-88`), and the fixture compares
logical SQL. No blanket directory/table exclusion follows from this source.

### Smallest proposed correction: end eligibility writers before one baseline

Keep ordinary eligibility inference and all eight source/tool controls exactly
as they are. Add one explicit **fixture-only phase boundary before seeding the
sensitive SQL rows or running any utility leaf**:

1. Retain the completed ordinary root identity and its positive evidence; capture
   the existing fixed denied counter once at the current post-control boundary.
   Close the ordinary client, stop and positively join the fixture-owned native
   processes and any owned descendants. Reuse bounded fixture process ownership;
   a timeout must fail, not be swallowed by the present `stop()` helper. Do not
   treat thread completion/unsubscribe, two stable snapshots, or a sleep as a
   background-work join. No live serving process is involved.
2. Restart the same ordinary dynamic and utility static launch profiles against
   the same synthetic home/config/catalog. Establish readiness through their
   real private connections. Reopen the ordinary client with its same trusted
   options and use only `thread/read` on the retained root, with no resume,
   start or new ordinary turn during the persistence interval. Pinned
   `thread_processor.rs:2843-2909` reads an unloaded persisted thread without
   creating a live Codex session. Thus this continuity check does not restart
   the memory/snapshot pipeline. Fail if the retained control cannot be read.
3. Seed the exact existing goal/memory rows once, assert their bytes, then take
   the single immutable persistent baseline. No restore, reseed, deletion or
   rebaseline after a utility call. Preserve the seeded memory policy file and
   all marker/ID scans. The counter captured in step 1 must remain unchanged
   across restart and every later leaf; do not reset it to hide startup egress.

This keeps the production-representative same-home dual-daemon topology and
concurrent ordinary connection/read-generation checks, while separating the
already-proven ordinary inference controls from the utility mutation interval.
It makes no production config change and does not claim concurrent ordinary
writers must leave an entire serving home byte-identical. Merely giving the
utility a different home would change the represented deployment boundary and
is not the proposed remedy. Disabling ordinary memory eligibility, changing
seed timestamps to avoid retention, accepting changed rows, or ignoring
shell_snapshots/memory tables is also not proposed.

Add only bounded failure metadata needed to assess any remaining mismatch:
file present/absent and hash-changed flags, snapshot ID classification
(control-root/utility/other), changed SQL table names/counts, exact seeded-row
equality flags, and whether a job worker ID matches the known control. Keep
rows, memory text, prompts and raw IDs out of diagnostic output. Distinguish
missing files from modified bytes and avoid map-order-based conclusions.
These diagnostics must retain the original failures; they do not normalize or
relax comparisons. If positive process-tree quiescence cannot be established
with bounded existing fixture ownership, report that gap before adding scope.

Only `codex/ephemeral_integration_test.go` and focused fixture-helper tests need
an author assignment for this proposal. Preserve original utility deadlines,
binary/catalog/model, tool/dispatch eligibility, hidden-action rejection, fresh
MCP/catalog controls and strict logs marker gate. Quick verification includes
the registered tagged `TestEphemeralIntegrationSQLiteDiagnostics` and affected
ownership/diagnostic tests with explicit `-mod=readonly -race`; any new barrier
selector must be reported by its implementer. The unchanged full
`TestEphemeralProtocolIntegration` remains a post-review watcher gate, not a
check run by the architect. A later successful isolated comparison would test
this correction; it would not retroactively identify this run's writer.

No product invariant fix is justified yet. If the quiesced fixture still shows
a seed/file delta, retain failure and use the bounded row/ownership evidence to
choose a concrete next investigation. Logging consent remains unanswered and
independent. No native rerun, model/network execution, source edit, Git/pin,
deployment or lifecycle operation was performed for this investigation; only
this diagnostic design supplement was appended.

## Persistence barrier amendment: fixture PID-namespace ownership (2026-10-04)

The accepted barrier above requires this correction before implementation.
Author preflight in `/tmp/automatic-session-slugs-native-barrier-preflight-report.txt`
correctly stopped: pinned `core/src/shell_snapshot.rs:1081-1101` launches with
`ProcessMode::NewSession`, and `rmcp-client/src/stdio_server_launcher.rs:282-284`
uses NewGroup. Killing the two native leader groups or inspecting PPIDs cannot
prove that all writers stopped. This amendment selects a finite fixture-only
ownership boundary for coordinator acceptance; no source or native run changed.

**Supported design:** add `CLONE_NEWPID` to the already existing Go reexec's
`CLONE_NEWUSER | CLONE_NEWNET | CLONE_NEWNS` flags in
`codex/ephemeral_integration_test.go:101-125`. Keep the same UID/GID mappings,
private `/etc`, network rules, home, config, two native startup profiles and
in-process mock servers. The reexecuted Go test itself is namespace PID 1;
there is no separate init executable, service, controller or per-call runtime.
Do not invoke unshare inside the running multithreaded test to create this
boundary: the existing child clone/reexec is the supported Go interface.

Primary local evidence is Linux man-pages 6.18 under
`/nix/store/bf85kcgfb9mwnhwfvkdwfg9sy0lvl9cp-man-pages-6.18-man/share/man/`:
`man7/pid_namespaces.7.gz` sections “The namespace init process”, “Nesting PID
namespaces”, “Adoption of orphaned children”, and “/proc and PID namespaces”;
`man2/kill.2.gz` for PID -1; `man2/wait.2.gz` for ECHILD/WNOHANG/__WALL.
They establish that descendants cannot ascend to an ancestor PID namespace,
orphaned descendants are adopted by namespace init (possibly through a nearer
subreaper), signals use the caller's PID namespace, and init exit kills remaining
namespace members. `setsid`/new process groups do not alter membership. This
is kernel ownership, not a snapshot of a changing process tree.

The exact owning Go 1.26.7 source
`/nix/store/hfb2fkwkkr6jdcg2ggibvf1zablw7i57-go-1.26.7/share/go/src/`
passes Cloneflags to clone/clone3 (`syscall/exec_linux.go:303-343`), exposes
`syscall.WALL`/`WNOHANG` and `Wait4`, and gives each `exec.Cmd.Wait` its own
process-specific wait (`os/exec_unix.go:22-72`, `os/pidfd_linux.go:81-128`).
Wildcard reaping must therefore start **after** both existing direct Wait owners
finish; otherwise it could steal their exit status and produce ECHILD there.

### Guard and finite stop/join sequence

- The outer fixture records its PID-namespace identity and passes that fixed
  value through the private reexec environment. Before launching any native
  process or permitting a namespace-wide signal, the child requires its internal
  child marker, `Getpid()==1`, `Getppid()==0`, and a PID-namespace identity different
  from the captured outer identity. After the existing recursive MS_PRIVATE
  mount operation, mount a fresh proc instance over `/proc` with
  MS_NOSUID|MS_NODEV|MS_NOEXEC. Require `/proc/self` to resolve to `1` and
  `/proc/self/ns/pid` to match `/proc/1/ns/pid`. Store this successful validation
  in a private nonzero owner value; recheck PID identity at stop. Environment
  markers alone never authorize `kill(-1, ...)`. Missing/malformed identity,
  refused clone/mount or unsupported kernel/user-namespace capability fails the
  explicit test. No host fallback, alternate uncontained stop or escalation.
- Stop is a serial phase with no active utility call and no concurrent fixture
  subprocess starts. Fence the existing diagnostic generation under `h.mu`,
  then drain and hold `h.diagnosticMu` through the join. This waits the current
  bounded nft read and prevents queued diagnostic reads from starting. Existing
  synchronous ip/nft/sqlite helpers must have returned and completed their own
  Wait before entry. Do not run a counter read, snapshot, restart or SQL seed
  inside the kill/reap interval. In-process HTTP servers may remain; they are
  PID-1 goroutines, and fenced callbacks cannot launch external helpers.
- With the guard satisfied, send `syscall.Kill(-1, SIGKILL)`. In this private
  namespace this targets fixture descendants, excluding PID 1; it reaches
  detached sessions and groups. Accept ESRCH only as absence of a signal target,
  never as join success. Other signal errors fail. Do not use numeric host PIDs,
  process-name matching or a directory/tree scan to select victims.
- Await completion of both already-started native commands through their single
  existing Cmd.Wait owners. A deliberate SIGKILL ExitError is expected; missing
  completion, unexpected wait errors or ECHILD from those owners fails. Use a
  stored result plus closed completion channel, or equivalent cached completion,
  so startup readiness cannot consume the only completion value. Never call
  Cmd.Wait a second time and never add a general background wait(-1) reaper.
  Repeat the namespace-wide kill on bounded retry ticks while either direct
  wait is pending too; this closes a fork race or inherited output pipe without
  stealing either owner's wait status.
- Then drain adopted children with
  `syscall.Wait4(-1, &status, syscall.WNOHANG|syscall.WALL, nil)`. Reap positive
  PIDs; retry EINTR. Zero means children still exist, not completion. Repeat
  namespace-wide SIGKILL while draining so a descendant fork racing the first
  signal cannot survive. **ECHILD is the sole empty-domain success condition.**
  WALL includes clone children; omit WNOTHREAD so children adopted by any Go
  runtime thread remain waitable. Keep Go's normal SIGCHLD disposition; do not
  install SIG_IGN/SA_NOCLDWAIT. A bounded timer may pace nonblocking retries;
  elapsed time or stable samples never supply success.
- Use one fixed two-second stop deadline, covering both direct waits and orphan
  drain (no extension per loop), within the existing 180-second fixture budget.
  This replaces the two separately swallowed one-second waits. It changes no
  utility call deadline. On failure, abort the isolated test without restart,
  seeding or baseline capture; namespace-init termination supplies the kernel
  final containment boundary. The outer reexec owner still waits for that exact
  process and reports failure. Do not hide a failed join behind exit cleanup.

Once both direct waits and ECHILD are established, no descendant writer remains:
any surviving lineage would have a live or unreaped child of namespace init
(including a nearer subreaper) and prevent ECHILD. No new fixture child may start
until that predicate is reached. This is the missing positive boundary; native
leader exit alone remains insufficient. Reuse this guarded stop at the fixture's
existing restart/final-cleanup boundaries, without additional stop cycles.

After the one new post-eligibility barrier, retain the previously accepted
ordering: restart exact same profiles/home/config; reconnect ordinary with the
same options and persisted `thread/read` only; insert the unchanged SQL seeds
once; take one persistent baseline. The denied counter is captured at its
original post-control point and checked unchanged after stop/restart. No reset,
reseed, restore, directory/table exclusion, weakened marker/ID check or separate
utility home is introduced. This fixture namespace is not a product lifecycle
API, and it does not alter the independent managed-child VM fixture.

### Minimal author scope and checks

Limit implementation to the provider's existing tagged integration fixture and
its local helper tests: reexec flag/proc guard, the single guarded stop routine,
reliable existing Wait completion records, and the accepted baseline placement.
No PID registry, resident reaper service, general process-manager API or native
patch is needed. Pure quick cases must reject unguarded/non-PID1 use before any
signal, distinguish WNOHANG zero from ECHILD, fail timeout/wait errors, and verify
that wildcard reaping cannot run before both direct owners finish. Preserve the
existing diagnostic bounds/ownership tests and explicit `-mod=readonly -race`.

After commit and affected review, a finite non-model control inside the private
reexec must create two owned leader helpers, including a descendant using a new
session and an orphan after its immediate parent exits. Require positive helper
readiness, both direct Wait completions, orphan reaping and ECHILD while PID 1
survives; then demonstrate a second start/stop cycle. A deliberate prerequisite
failure must fail without native startup. This belongs to post-review namespace
verification, not an unguarded quick host test. Exact new selectors are the
author's report obligation. Then the unchanged full native fixture remains a
watcher gate with all original controls/assertions. A source-backed design is
not execution proof.

No remaining source/API gap is identified for this finite boundary. Actual
host support for creating the extra namespace and mounting proc remains a
fail-closed execution prerequisite. The observed snapshot/SQL writer remains
unattributed; this correction does not relabel that old run. The strict logging
gate and unanswered privacy question are unchanged. Only this design amendment
was written; no process/native/model/network operation, source edit, test,
Git/pin/deployment/session mutation or delegation was performed.
