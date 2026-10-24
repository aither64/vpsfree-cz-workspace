# Native retry verification handoff

Status: prepared on 2026-10-22; no native tests executed for this brief.
Run only after intended source/fixture changes are committed, quick checks pass,
and final independent review findings are resolved or explicitly accepted.
Lead owns final heads and the matching dependency pin. This supplements
[design.md](design.md); it does not authorize deployment or modify Codex.

## Run-2 pinned source diagnosis and next-run gate

Run 2 is failed/incomplete; preserve
[its result](native-verification/run-2-3f2153a4/result.md). No native execution
was performed for this source diagnosis. The run retained no native status
tuple establishing B's timeout cause. Pinned source nevertheless proves a
material product predicate error: loaded terminal failures may stay
`systemError`, not literal `idle`. The accepted correction and source links
are in [design.md](design.md), **Native 0.163 loaded terminal status correction
(run 2)**. A owns `TurnState.IsLoadedFailedTurn(expectedTurnID)` and B consumes
it. Preserve exact error allowlisting and every queue, prompt, unresolved-send,
settings and lifecycle hold. After owners commit/quick-check the correction,
the same reviewer's affected general/architecture/risk lanes must complete
before native run 3. Use final A/B heads, not the failed run's source receipt.

Fresh `thread/start` does not guarantee materialized rollout/history before
the first user history. Native
[`thread/read:3013–3022`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L3013)
explicitly builds a loaded metadata-only response before persistence, and
[`6250–6286`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L6250)
defines pre-first-message history-unavailable errors. A's separately approved
test-only bootstrap establishes private fixture history using its existing
headless bootstrap path before the original input; no production cold-activation
behavior changes. Use the current subtest's testing handle and retain useful
failure diagnostics without dropping assertions.

Native status is the watch manager's loaded-state projection, not proof derived
from the existence of history or a live metadata response. Untracked status
defaults to `notLoaded` ([thread_status.rs:384–386](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/thread_status.rs#L384));
the reader combines it with live running state. No evidence shows a normal
subscribed terminal failure becomes cold: automatic unloading requires both
no subscriber and no active status
([thread_lifecycle.rs:59–83](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/app-server/src/request_processors/thread_lifecycle.rs#L59)).
Whatever its cause, observed `notLoaded` remains a refusal; do not infer loaded
authority from persisted turns or automatically resume.

The `/tmp` PATH-alias warning is a distinct fixture prerequisite. Release
native code rejects alias creation when CODEX_HOME is beneath the process temp
root ([arg0/src/lib.rs:309–324](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/arg0/src/lib.rs#L309)),
then expressly warns and continues (149–164). The omitted aliases are
`apply_patch`, `applypatch`, and `codex-linux-sandbox` (370–375); the sandbox
path falls back to the current executable (249–258). Thus the warning alone
does not prove command failure or explain the history/status errors. Harmless
shell fixtures must use their declared shell/tool dependencies, not assume
these aliases exist. Actual sandbox command success remains a required native
assertion; fallback compatibility cannot be inferred from a nonfatal warning.
Keep isolated private homes and synthetic provider credentials unchanged.

## Fixed fixture contract and ownership

Implementer0 owns A, including any shared test-only harness extraction. Preserve
the existing recovery fixture's behavior. Implementer1 owns B; use its existing
private native harness, without duplicating A's complete campaign.

| Fixture | Location and status at planning | Required evidence |
| --- | --- | --- |
| `TestPinnedCodexRecoveryRemainsColdUntilActivation` | A `codex/recovery_integration_test.go`, exists | Cold recovery, native queue FIFO/activation and native daemon restart |
| `TestNativeLiveSwitchReconnect` | B `portal/cmd/workspace-portal/live_switch_integration_test.go`, exists, tag `live_switch_integration` | Active lead/member reconnect, queue/report stable IDs, partial command/question history |
| `TestPinnedCodexFailedTurnRetryContract` | A `codex/continuation_integration_test.go`, required addition; no new build tag | Real terminal errors, continuation/settings/history, queue execution, uncertain receipt and busy boundary |
| `TestNativeTurnRetryController` | B `portal/cmd/workspace-portal`, now present; lead reports compile green (0.042s), tag `live_switch_integration`; native run pending | Managed failure -> automatic continuation; enrollment, opt-out, scheduled UUID/deadline retained across controller/client restart |

Use these exact top-level names. Before review, owners record the final named
subcases in the review packet and this handoff. Missing fixtures or skipped
cases are incomplete verification, even if `go test` returns zero. Exhaustive
quota/schedule/lifecycle matrices remain unit tests; B needs one focused real
controller flow plus these boundary assertions.

## Exact synthetic provider wire

Use HTTP 200, `Content-Type: text/event-stream`, followed by these complete SSE
records (a blank line after each data line). The provider emits synthetic
responses only; these messages never go to a production model or policy service.

```text
event: response.failed
data: {"type":"response.failed","sequence_number":3,"response":{"id":"resp_fixture_capacity","object":"response","created_at":1759771626,"status":"failed","background":false,"error":{"code":"server_is_overloaded","message":"Synthetic capacity fixture."},"incomplete_details":null}}

event: response.failed
data: {"type":"response.failed","sequence_number":3,"response":{"id":"resp_fixture_cyber","object":"response","created_at":1759771626,"status":"failed","background":false,"error":{"code":"cyber_policy","message":"Synthetic policy fixture."},"incomplete_details":null}}

```

These are alternative terminal responses, not two failures on one stream. A
preceding `response.created` may use the same response ID. Do not send an HTTP
503 or invent `server_overloaded`: that tests a different transport/error path.

Source-confirmed mapping at upstream **rust-v0.163.0**:

- [`codex-api/src/sse/responses.rs:414–417`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/codex-api/src/sse/responses.rs#L414): `response.failed` passes its `response` to `parse_failed_response`.
- [`responses_error.rs:56–58,87–89`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/codex-api/src/sse/responses_error.rs#L56): `cyber_policy` -> `ApiError::CyberPolicy`; `server_is_overloaded` -> `ApiError::ServerOverloaded`.
- [`responses.rs:1197–1208`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/codex-api/src/sse/responses.rs#L1197): upstream exact cyber SSE test asserts the policy error.
- Generated pinned schema `/tmp/codex-thread-retries-01630-schema/v2/ThreadTurnsListResponse.json`: public variants `cyberPolicy` and `serverOverloaded`.

The native fixture must assert the terminal **failed turn** and exact public
variant. Source mapping and generated schema do not establish an empirical
App Server result; this still awaits the post-review run. Keep returning the
same synthetic failure for that turn if native retries occur; do not silently
let an internal retry consume the next success step.

Configure the private custom provider as follows, substituting only the owned
loopback address. The test harness writes this private config, not the operator's
configuration.

```toml
model_provider = "fixture"
model = "gpt-5.5"
model_reasoning_effort = "low"

[model_providers.fixture]
name = "Synthetic retry fixture"
base_url = "http://127.0.0.1:PORT/v1"
wire_api = "responses"
requires_openai_auth = false
supports_websockets = false
request_max_retries = 0
stream_max_retries = 0
```

Both retry keys are provider-level fields and accept zero without a lower
clamp: [`model-provider-info/src/lib.rs:180–186,498–509`](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/model-provider-info/src/lib.rs#L498).
These are fixture-only settings; production native retry policy is unchanged.
Count provider requests and record any unexpected native retry. If a helper
uses a WebSocket-capable provider, return HTTP 426 for a valid Upgrade request
to exercise HTTP fallback, as the existing B harness does.

Launch only the pinned executable's `app-server --strict-config --listen
unix://<private-socket>`. Use fresh private 0700 HOME/CODEX_HOME/XDG/work/state
directories and an allowlisted child environment. No inherited login, provider
key, proxy, credential file, registered workspace socket or rollout directory.
Use no-auth custom provider for new cases. The existing B harness's literal
`OPENAI_API_KEY=synthetic-only` is dummy fixture data, never a real key.

## Assertions and concurrency boundary

A must cover both native error variants and nonempty visible continuation with
the exact design text and stable client ID. Assert one new input/receipt, no
`thread/resume`, steer or policy write, explicit model/effort/context unchanged,
and plan/default mode plus effective native policy preserved. Preserve partial
assistant/tool items and a deterministic harmless fixture side effect. Never
replay the original prompt or fabricate failure by editing the rollout.

Exercise native queue automatic execution using a known-empty additionalContext,
correlate exact client ID to actual executed turn, and compare `ReadTurnContext`
with actual execution settings even when enqueue defaults differ. Drop a
turn/start reply **after native acceptance** with a proxy/barrier, recreate the
client using the same ledger, and reconcile the same ID to exactly one input.

The managed busy case must deterministically contend at shared admission and
prove no fresh continuation/steer while a competing managed turn or queued work
wins. Lead accepted a required B composed regression using actual managed
`SendWithOptions`/`QueueWithPolicy` against actual `Controller.Step`, with the
authoritative fence and synthetic-wire barriers. Manual admission wins =>
zero automatic start/steer. Automatic dispatch owns the fence => manual input
cannot reach native until dispatch/receipt critical section ends, after which
ordinary explicit manual semantics apply. Unknown automatic outcome => manual
input remains held. Keep the existing cross-process and roster lock tests;
neither lock-only tests nor the native-direct diagnostic replace this composed
production-path proof. No second complete native campaign is needed for this
deterministic B regression. A newly exposed product defect goes to lead/design
before production edits.

A separate native-direct race places an independent native `turn/start`
between final preflight and automatic `turn/start` using a test-only proxy
barrier. Run 3 recorded nil RPC error, equal nonempty manual/continuation turn
IDs, latest same turn `inProgress`, and one provider request while held. Pinned
source confirms public `turn/start` implicitly steers input into an active
regular turn and may apply persistent settings; see the source links and
accepted disposition in [design.md](design.md), **Native direct-writer race
disposition (run 3, accepted)**. This was not a replacement or refusal.

Keep `native_direct_busy_race_compatibility`, asserting that exact pinned
observation only. After releasing the provider, require bounded eventual
history with both exact client IDs once each in the same completed turn,
unchanged earlier failed history, and no distinct replacement/interruption.
Record exact RPC replies, turn statuses, input IDs and provider request counts.
One provider request is asserted at the held point; pending input can require
further sampling after release. Refusal or changed semantics fail for explicit
reassessment, not an alternative success branch. Do not skip/delete the case
or count it as managed safety. Library `receipt.Steered == false` describes its
client path and is not proof against native implicit steering.

Public `TurnStartParams` has no expected-turn/status compare-and-start field;
`parentTurnId` and `rootTurnId` are ancestry metadata, not a precondition. The
supported product guarantee covers managed portal/CLI/retained-team admission
sharing the runtime fence. Unmanaged direct native writers do not participate.
The run-3 steering result was escalated and lead accepted it within this
unchanged boundary. Unexpected native behavior remains a failed compatibility
gate, not permission to patch Codex, add a fallback or broaden the guarantee.

The lost-reply fixture may use a bounded same-ID reconciliation poll because
native acceptance does not wait for history persistence. It must not resubmit.
A owns the strict native diagnostic, that narrow fixture correction and its
lasting reference documentation; B owns composed admission tests and its portal
documentation. Lead performs the main copy pass before commits. After all
intended corrections are committed and quick checks pass, the same reviewer's
affected general/architecture/risk lanes must complete before the next final
native campaign. The four passing A665 cases in run 3 are retained scoped
evidence, not a whole-gate pass. B's wrong-CWD run emitted no test events;
lead's corrected same-B731 batch completes that run independently. B source
stays frozen until lead confirms that batch has finished, then the owner may
edit its tests/docs. Use the final reported heads for subsequent verification;
historical execution identities elsewhere in this brief do not release a new
campaign. C remains held.

Lead explicitly accepted the matching settings-authority boundary: exact
historical execution context plus a saved successful managed loaded binding
and unchanged generation, under the common admission fence. Remove display
cache mode reads from dispatch authority. Pinned `ThreadReadResponse`/`Thread`
does not expose current loaded collaboration mode/access; `ThreadResumeResponse`
does but resume mutates and is forbidden here. `TurnStartParams` accepts mode
and access overrides, but adding them would change the approved no-policy-write
contract and would not provide compare-and-start. No such expansion is planned.
Unmanaged direct native writes may silently change settings and invalidate this
guarantee; detection of every external write is not claimed. Observed mismatch,
foreign/unidentified input, execution hold or changed binding/socket generation
fails closed. Native restart cannot inherit a presumed loaded binding.

B's minimal real flow: establish a managed authorized binding; enroll before a
new failure; drive the controller's injected clock to its next attempt; prove a
single neutral continuation and native receipt. Establish an existing failed
turn before enrollment and prove it stays manual. Opt-out or Stop before a due
attempt must prevent dispatch. Recreate the controller/client on the same
private durable state and show accepted/uncertain receipt correlation without
a second input. Use a portal/controller restart here, not a native restart as
a substitute. Existing recovery fixture separately checks native cold holds.

## Executable commands

Pinned binary:
`/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex`.
Wrapper SHA256: `dd356114c45b6b78617be9da9c21ab6d284a8d3c7de1e5a39abf45be2cabed8b`.
Underlying `libexec/codex/bin/codex` SHA256:
`5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5`.
Record actual version/hash again at execution. A has no exported devShell;
the matching B flake provides the Go shell used below. Lead freezes final
reviewed A/B heads and shell/input graph before handing off; current planning
observations were A `25f115ffc9f188d83452835b68376434887ff850`, B
`aac06297d91892dce5ae176572d4734e5068d0f7` plus ongoing edits.

For each command set these literal variables in that shell. `RUN` must be a new
owned directory, created with `umask 077; mkdir -p "$RUN"`; choose its final
unique run suffix in the watcher assignment. No command below has run yet.

```sh
A=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/codex-web
B=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace
NATIVE=/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex
RUN=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/native-verification/RUN_ID
```

Compile only before final review; no native test invocation:

```sh
# cwd: $A
nix develop "$B" -c go test -mod=readonly -c -o "$RUN/codex.test" ./codex
"$RUN/codex.test" -test.list '^TestPinnedCodex(RecoveryRemainsColdUntilActivation|FailedTurnRetryContract)$'

# cwd: $B/portal
nix develop "$B" -c go test -mod=readonly -tags=live_switch_integration -c -o "$RUN/portal.test" ./cmd/workspace-portal
"$RUN/portal.test" -test.list '^TestNative(LiveSwitchReconnect|TurnRetryController)$'
```

Both listed names must appear in each corresponding list. Native runs after
review, through a fresh verification watcher:

```sh
# cwd: $A
nix develop "$B" -c env CODEX_WEB_TEST_BINARY="$NATIVE" go test -mod=readonly ./codex -run '^TestPinnedCodex(RecoveryRemainsColdUntilActivation|FailedTurnRetryContract)$' -count=1 -json -timeout=5m >"$RUN/library.jsonl" 2>"$RUN/library.stderr"
result=$?
printf '%s\n' "$result" >"$RUN/library.exit"

# cwd: $B/portal
nix develop "$B" -c env LIVE_SWITCH_CODEX="$NATIVE" go test -mod=readonly -tags=live_switch_integration ./cmd/workspace-portal -run '^TestNative(LiveSwitchReconnect|TurnRetryController)$' -count=1 -json -timeout=5m >"$RUN/runtime.jsonl" 2>"$RUN/runtime.stderr"
result=$?
printf '%s\n' "$result" >"$RUN/runtime.exit"
```

Each command is a separately assessed operation; a later successful command
cannot overwrite its result. Existing fixtures have 60s/90s internal contexts;
new cases must have bounded scenario contexts fitting this five-minute package
deadline. Owners report a necessary timeout change before execution. No generic
quiet-build deadline applies to Nix environment preparation.

Required evidence: exit zero, each exact top-level name has a `pass` event,
every declared named subcase has a `pass` event, no selected `skip`/`fail`, and
no missing cases. Preserve complete `go test -json`, stderr and exit files.
Use `jq -c 'select(.Test != null and (.Action == "pass" or .Action == "skip"
or .Action == "fail")) | {Action,Test,Elapsed}'` on each JSONL for the concise
case inventory; compare it to the owners' fixed case manifest. A zero-match
regex and a missing-binary skip both fail this evidence gate.

Existing helpers remove private temp directories, so outer logs are essential.
New fixtures should log bounded native error/turn/receipt evidence on failure
and emit a concise scenario summary. If owners add retained artifacts, put only
synthetic native logs/RPC traces/result manifests beneath `$RUN`, without
credentials, unrelated prompts or private production paths. Record owned native
PID/exit and cleanup outcome; leave no orphan fixture process.

## Watcher handoff

Lead resolves a fresh utility from the retained catalog's
`utilities.verification_watcher`, with installed execution access, using
`~/.codex/skills/dev-session-monitor/SKILL.md`. Supply exact reviewed commits,
cwd, commands/environment, unique RUN, named case manifest and final input graph.
Use explicit full access as required by the skill. Watcher owns its commands,
complete logs and status; no source edits, diagnosis, retries, deployment or
nested delegation. No watcher has been launched by this planning package.

Report passed/failed/incomplete, both exit statuses, actual passing/skipped/missing
case inventory, heads/binary hash, duration, artifacts and remaining owned
processes. Stop/escalate on fixture access outside disposable paths, production
egress, foreign sockets or unexpected local kernel builds. Silence alone does
not authorize cancellation. Cleanup applies only to owned disposable fixture
processes/data, never the development session or registered services.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/>

## Final A case manifest (owner report; execution still pending)

Reviewed-candidate head d2d74f931cc50e39345c6c15931748062ee51951.
TestPinnedCodexFailedTurnRetryContract subcases:
- nonempty_continuation_default
- nonempty_continuation_plan
- exact_cyber_terminal
- automatic_queue_uses_execution_context
- lost_accepted_reply_recreated_client
- native_direct_busy_race_compatibility

Third logical commit changes tests only; no native execution before review.

## Final execution identities (lead verified)

A d2d74f931cc50e39345c6c15931748062ee51951; B e0fb1238bd17cc3b29cc7d59ddaa9784c89ef939; W e6c2008a8f1215265fb8ceef3081a202570c30c6; C 49397f0d8ec0c2c33a4e8a0285843445068fe0ca. All committed/published/clean and quickchecked. Original independent review plus affected reports resolve all findings; last2 test-only fixture corrections directly inspected under step9. Final pin graphs independently reconstructed, one pin commit each, only runtime node changes from61de; A/extension/edges preserved. Final C receipt c-repin-e0fb1238.json and final-pin-inspection.json. Earlier candidate IDs/placeholders in preparation prose are historical and superseded by this exact execution set. Native/full package gates now released; no deployment approval inferred from verification itself.
