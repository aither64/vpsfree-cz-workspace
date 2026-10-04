# Utility implementation report

Session: `2026-10-03-automatic-session-slugs` · implementer0.
Status: utility unit committed after coordinator quick checks and main-context
prose review. Both owning worktrees and indexes are clean. No binary integration
or live inference has run. Ready for the coordinator's frontend handoff;
dependency publication/pins remain a later unit.

Committed heads before the coordinator-owned runtime rebase:

- codex-web: `ca0f3bc980ca99454d000761aeee37b4b9bbafc3`
  (`codex: run bounded ephemeral utility turns`), eight owned files.
- dev-workspace: `dd12036644a3c1cc540cd23e262734a14179e43f`
  (`portal: name sessions through the private utility client`), five owned files.

Backend commits remain `a90570e5868a033a9978c57bd6476278c03b165b` and
`c5472c4f520e4e92b1fc05bfb3184eb74bc9458b`. The coordinator's aggregate Ruby
entry-point correction is already folded into the latter; the old unpublished
head is superseded.

The actual deployed predecessor is published/unmerged
`4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4`, one descendant of origin/master
`924c0ec28c41dd8b56aaf17f2212b302ca614899`. It advances cluster transition
policy 2 to 3 and is already active in the serving profile. The coordinator
will rebase our clean unpublished runtime commits onto that exact revision;
the deployed commit must retain its SHA and must not be folded or rewritten.
Our runtime commit IDs will change. No rebase was performed by implementer0.
Inspection of the 924-to-4ef diff confirms only workspace-portal documentation,
workspace-host, runtime-contract.json and its profile-transition tests differ.
Upload, dev-session CLI and Go dependency sources are byte-identical, so the
exact-924 old-source upload fixture still represents this predecessor for its
tested boundary. This does not claim cluster-policy compatibility with policy 2.

## Completed files and contracts

| Repository | Files | Result |
| --- | --- | --- |
| codex-web | `codex/client.go`, `codex/ephemeral.go`, `codex/ephemeral_policy.json` | Additive public helper; private sink before ordinary admission; finite config/model/start/cleanup recipe |
| codex-web | `codex/ephemeral_test.go` | Eleven top-level fake-transport groups: policy/lifecycle, questions, identity, bounds, discovery, cancellation, disconnect and ordinary-client isolation |
| codex-web | `test/codex_protocol_contract.py`, `test/codex_ephemeral_config_contract.py` | Exact production call-site counts, consumed shapes and declared restriction-key/type validation |
| codex-web | `codex/ephemeral_integration_test.go` | Tagged exact-candidate fixture and fast tool-schema representation test; execution evidence pending |
| codex-web | `docs/reference.md` | Public API, provisioning, limits, errors, safe cleanup, operating assumptions and fixture prerequisites |
| dev-workspace | `portal/internal/web/server.go`, `portal/internal/web/session_namer.go`, `portal/internal/web/session_namer_test.go` | Normal trusted-socket adapter; injected seam preserved; five focused adapter groups |
| dev-workspace | `docs/session-preparations.md`, `docs/codex-package.md` | Private runtime naming, cancellation/cleanup, operator MCP procedure and exact-binary release boundary |

`RunEphemeralTurn` takes trusted private canonical absolute `Directory` and
separate empty regular mode-0600 `InstructionFile`, exact model/effort, explicit
instructions, UTF-8 text and bounded object schema. The application owns
provisioning/removal. It copies only socket/client identity and uses existing
transport without parent policy, roots, observers, activity, timers, ledger or
normal send/resume/history helpers. It bounds input/schema/output, frames,
aggregate bytes/envelopes, provisional events and model pagination. Errors have
static categories, preserving caller cancellation.

Actual server requests receive fixed `-32601` errors and fail the utility;
async question/delivery notifications immediately fail without an invented
response, normal UI admission or persistence. Success requires the turn/start
response identity, exact generation/thread/turn, successful completion and one
completed explicit final answer.

Safe cleanup retains one validated early same-generation/thread turn identity
solely for interruption after the one issued turn/start. Matching turn/started,
turn/completed or item started/completed may provide it when the reply is lost.
It cannot authorize success. Missing, foreign or contradictory identity cannot
authorize interruption. Cleanup interrupts the owned exact turn on failure,
unsubscribes the known thread and always closes within the original deadline,
with at most 250 ms of remaining cleanup budget. Unsubscribe alone does not
stop a running turn. No reconnect, adoption, blanket cancellation or persisted
thread lifecycle action is used.

The adapter uses exactly `gpt-6-luna`/`low`, fixed instructions/name schema and
the first 8192 raw UTF-8 bytes. It provisions an empty mode-0700 cwd outside the
workspace and a separate empty private override file, then removes only its
own scratch state after teardown. The existing worker owns the ten-second
whole budget, two-call workspace limit, deterministic fallback and generation
checks. Custom names/attachment-only requests bypass it; shutdown/generation
cancellation cannot commit fallback. No attachments/team/config options or
module/dependency pins/replace directives were added.

## Checks and current evidence

Coordinator-owned checks passed in the prepared repository environments:

- Revised complete codex mock suite: package 7.777 s, exit 0, including all
  eleven helper groups after the early-ID cleanup correction. Log:
  `/tmp/automatic-session-slugs-utility-cleanup-go.log`.
- All five focused runtime adapter groups: wall 7.1 s, exit 0. Log:
  `/tmp/automatic-session-slugs-utility-cleanup-adapter.log`.
- Parent gofmt of the checked core Go subset; source hashes retained in
  `/tmp/automatic-session-slugs-utility-core.sha256`.
- Final updated protocol corpus, including the test-only hooks/list eligibility
  shape, is compatible with `/tmp/automatic-session-slugs-schema`; config
  validator passed 55 restrictions plus literal MCP enabled against the pinned
  config schema.
- Parent gofmt of the tagged fixture and compile-only `codex_integration`
  selector `^$`: exit 0, zero tests intentionally. This is compilation evidence.
- `TestEphemeralIntegrationToolSchemaShapes`: nonzero, all seven parser cases
  passed. It does not launch Codex or execute the binary integration fixture.
- Core source fingerprint unchanged; both application diffs whitespace-clean.
  Main-context prose review completed on reference/preparation/package docs and
  static errors; the coordinator's clarity edits are preserved in the commits.
- Hook preflight: no declared hook framework, core.hooksPath unset and only
  sample hooks in each canonical bare repository. No hooks bypassed. Commit
  messages came from temporary files, wrapped to 80 columns, via git commit -F.

Earlier corrected checks passed too (codex package 7.837 s, adapter 0.080 s),
but preceded the cleanup correction and are superseded above. The initial
unchanged socket-fixture failure was a long Nix TMPDIR path; `env TMPDIR=/tmp`
inside nix develop fixed it without source changes or skips. This member's Nix
daemon access fails at `/nix/var/nix/daemon-socket/socket` with `Operation not
permitted`; no ambient-tool workaround or sandbox bypass was used.

## Exact quick commands

Run from each owning worktree. Temporary GOWORK joins both assigned modules
until publication/pins; `-mod=readonly` overrides vendor GOFLAGS. Set TMPDIR
inside nix develop. Every Go selector below selects nonzero existing tests.
Core checks need no repeat absent a new edit or failed check.

```sh
# codex-web: all eleven fake helper groups, or the complete mock package
nix develop /tmp/automatic-session-slugs-codex-web-env -c \
  env TMPDIR=/tmp GOWORK=/tmp/automatic-session-slugs-local-go.work \
  go test -mod=readonly ./codex -run '^TestEphemeral' -count=1
nix develop /tmp/automatic-session-slugs-codex-web-env -c \
  env TMPDIR=/tmp GOWORK=/tmp/automatic-session-slugs-local-go.work \
  go test -mod=readonly ./codex -count=1

# dev-workspace: all five adapter groups
nix develop /tmp/automatic-session-slugs-runtime-env -c \
  env TMPDIR=/tmp GOWORK=/tmp/automatic-session-slugs-local-go.work \
  go -C portal test -mod=readonly ./internal/web \
  -run '^TestSessionNamingUtility' -count=1

# codex-web: compile tagged fixture; run only its fast schema parser
# This does not invoke TestEphemeralProtocolIntegration or Codex.
nix develop /tmp/automatic-session-slugs-codex-web-env -c \
  env TMPDIR=/tmp GOWORK=/tmp/automatic-session-slugs-local-go.work \
  go test -mod=readonly -tags=codex_integration ./codex \
  -run '^TestEphemeralIntegrationToolSchemaShapes$' -count=1

# codex-web: scanner/corpus and fixed config restrictions
nix develop /tmp/automatic-session-slugs-codex-web-env -c \
  python3 test/codex_protocol_contract.py --coverage-only codex/client.go
nix develop /tmp/automatic-session-slugs-codex-web-env -c \
  python3 test/codex_protocol_contract.py \
  /tmp/automatic-session-slugs-schema codex/client.go
nix develop /tmp/automatic-session-slugs-codex-web-env -c \
  python3 test/codex_ephemeral_config_contract.py \
  /nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source/codex-rs/core/config.schema.json
```

The temporary schema validates the unchanged selected source. Generate schemas
from the exact assembled candidate before release as well.

## Tagged fixture and prerequisites

Entry point: `codex/ephemeral_integration_test.go`,
`TestEphemeralProtocolIntegration`, tag `codex_integration`. It has not run;
execution waits for mandatory independent review. Explicit invocation fails
rather than skips without:

- Absolute executable `CODEX_EPHEMERAL_TEST_BINARY` and its exact reviewed
  `CODEX_EPHEMERAL_TEST_SHA256`.
- Absolute `CODEX_EPHEMERAL_TEST_SOURCE` for that candidate's `codex-rs`, with
  config schema and unchanged models.json. The fixture checks Luna low effort
  and original async-input/clock metadata.
- Absolute executables `CODEX_EPHEMERAL_TEST_IP`, `CODEX_EPHEMERAL_TEST_NFT`,
  `CODEX_EPHEMERAL_TEST_SQLITE`; Linux user/network/mount namespaces and private
  firewall/mount capability. The namespace probe is environment evidence only.

The fixture starts a disposable private app-server and built-in OpenAI Responses
provider path with synthetic credentials/mock endpoint. It retains provider,
model and catalog capabilities, including Luna's Responses Lite representation.
It inspects every actual top-level and developer additional_tools schema,
including the pinned plain-function namespace; action/custom/deferred/unknown
tools and duplicate catalogs fail. An ordinary control proves synthetic
instruction/skill/file/plugin/hook eligibility. User/plugin hooks use actual
hooks/list and normal trusted_hash state, without bypassing hook trust. Private
nftables permits only the mock inference endpoint.

Controls cover hostile dispatch/file/network canaries, async notification
rejection, separately labelled genuine request-ID question rejection, clock,
early events, cancellation/disconnect, stale/malformed/ambiguous completion,
discovery timeouts, a concurrent ordinary connection and fresh MCP inventory
between stopped calls. Lost-clock/lost-question modes drop turn/start replies
and hold a second real provider request open until actual cancellation; exact
interruption and observed provider cancellation are required, so natural
completion cannot hide an active turn.

Persistence checks use actual candidate-created goal/memory SQLite stores,
seed a valid paused goal/retained memory and require their dumps unchanged.
File/SQLite checks reject utility prompts, identities/rollouts, unexpected
files, hook/notify/MCP side effects and goal/memory mutations. Only inventoried
ordinary metadata/catalog cache is excluded. Provider requests remain bounded
synthetic test memory; no production prompt/credential is captured.

After review, a fresh coordinator watcher may explicitly run with all
prerequisite variables populated:

```sh
nix develop /tmp/automatic-session-slugs-codex-web-env -c \
  env TMPDIR=/tmp GOWORK=/tmp/automatic-session-slugs-local-go.work \
  go test -mod=readonly -tags=codex_integration ./codex \
  -run '^TestEphemeralProtocolIntegration$' -count=1 -timeout=180s
```

## Clarifications, gates and committed split

Required trusted InstructionFile and immediate async-notification failure were
accepted by the coordinator; -32601 applies only to actual server requests.
The coordinator-required early-ID cleanup fix is complete and revised checks
pass. No public API/config/model scope deviation remains. Global user policy
is trusted serving-instance policy. Operators pause/stop naming between MCP
changes using existing procedures. No administrator-race defense, global lease,
shared-home rewrite, Codex patch/model bump or production process framework was
added.

Remaining: coordinator-owned deployed-base rebase and resulting-head inventory;
mandatory review; exact-binary isolation fixture; frontend; final dependency
publication/pins/vendor hash and assembled package checks. Unsupported tools,
source eligibility, teardown or persistence
must fail the real release gate and be reported. Mock/schema success or fallback
cannot replace that evidence.

Committed focused split:

1. `codex: run bounded ephemeral utility turns` — all eight owned codex-web
   paths above. Explain additive trusted API, private pre-admission sink,
   restrictions/bounds, response-loss cleanup, existing-client compatibility,
   corpus/config checks and tagged fixture entry point without an execution claim.
2. `portal: name sessions through the private utility client` — the five owned
   dev-workspace paths above. Explain exact Luna/low/raw-text/private-file adapter,
   trusted-socket construction, retained seam, worker budget/fallback/generation
   behavior and operating/release boundary. No frontend or dependency pins.

Exactly the two utility commits above were authorized and made. No push,
default-branch integration, binary execution, rebase, deployment or session
lifecycle action was performed. Coordinator owns plan/state/portal updates.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/>

## Nonempty instruction-file correction: frozen handoff, 2026-10-04

This checkpoint supersedes the earlier empty-file contract in this report. The
accepted design supplement establishes that the pinned native loader reads both
files before override precedence and rejects empty trimmed content. It also
establishes that the empty inline compact prompt selects the file's contents;
this correction does not disable compaction. Previous check results above remain
historical evidence for their recorded inputs, not results for this correction.

Provider base: `23d1aaa67574c849b933178400058f46d53ef3e1`. Runtime base:
`d05e75270a9bed417d07e9be8bc082c906f6846a`. All eight application files are
uncommitted and frozen for coordinator formatting, checks and prose review:

- codex-web: `codex/ephemeral.go`, `codex/ephemeral_test.go`,
  `codex/ephemeral_integration_test.go`, `codex/ephemeral_policy.json`,
  `docs/reference.md`.
- dev-workspace: `portal/internal/web/session_namer.go`,
  `portal/internal/web/session_namer_test.go`, `docs/session-preparations.md`.

The provider exports the exact accepted `EphemeralInstructionFileContent` string.
Before connecting, the validator retains the canonical path, private placement,
ownership, regular mode-0600 single-link checks, requires the exact length and
reads at most constant length plus one byte to compare exact bytes. The adapter
writes the provider constant once to a unique `instructions.txt` outside its
empty cwd. Both config file overrides remain; explicit base/developer text,
empty inline compact prompt, model/effort, fixed restrictions, budgets, teardown,
worker ownership and fallback are unchanged. No legacy empty-file fallback is
provided. Empty-file callers of the unreleased API update with their dependency.

Focused source tests cover ten invalid file-content/path cases before connection,
successful exact-byte provisioning and unchanged teardown bytes, both override
paths and unchanged explicit instructions. The adapter checks exact path, bytes,
owner/mode/single link, empty cwd, unchanged deadline, distinct per-call scratch
paths and cleanup on success, failure and cancellation.

The tagged fixture now records at most 48 private phase samples, always retaining
the final post-teardown sample. Known RPC methods map to fixed phase names;
errors retain only their numeric code and a fixed category, including recognized
empty model/compact file errors. Arbitrary messages, error data, parameters and
raw model requests are excluded from this evidence. Samples cover handshake,
configuration, model lookup, thread/turn ownership, native provider upgrade/POST,
synthetic tool dispatch and teardown with provider counts and unchanged nft deny
counters. Counter reads have a bounded diagnostic context. The existing final
deny comparison remains exact; no counter or baseline reset was added. Samples
locate changes in time and do not prove which concurrent native task sent a
packet. The full 36-leaf native matrix and HTTP-fallback coverage limit remain.
Baseline/early-event provider controls also require explicit utility instructions
in the actual decoded request. Five pure diagnostic cases include the category,
bounded storage and final-sample checks.

Only `git diff --check` was run here; both owning worktrees passed. No Go tests,
formatting, Nix launch, native/browser execution, commits or pin changes were run.
Within the public non-test Go corpus, only `ephemeral.go` differs from deployed
`ca0f3bc`; policy changes are exactly the two example path values. The other
public client/transport files remain byte-identical. Native model/catalog/binary
guards and metadata are unchanged. No actual native RPC cause or isolation pass
is claimed. Denied-egress attribution remains unresolved pending real phase
evidence. No analytics, MCP, provider or capability setup change was made.

Pending coordinator quick commands, from the owning repository roots:

```sh
nix develop /tmp/automatic-session-slugs-codex-web-env -c \
  env TMPDIR=/tmp GOWORK=off go test -mod=readonly ./codex \
  -run '^TestEphemeral' -count=1
nix develop /tmp/automatic-session-slugs-codex-web-env -c \
  env TMPDIR=/tmp GOWORK=off go test -mod=readonly -tags=codex_integration \
  ./codex -run '^TestEphemeralIntegration(ControlRequest|HTTPFallbackResponder|DiagnosticBounds|RPCDiagnostics|ToolSchemaShapes)$' \
  -count=1
```

These selectors name 12 non-tagged provider groups and five tagged pure groups.
The tagged command compiles, but does not execute, the native integration entry.
The runtime command requires a coordinator-prepared temporary module/sum copy
with a local provider replace; nothing is committed to module or pin files:

```sh
nix develop /tmp/automatic-session-slugs-runtime-env -c \
  env TMPDIR=/tmp GOWORK=off go -C portal test -mod=readonly \
  -modfile=/tmp/automatic-session-slugs-instruction-file.mod ./internal/web \
  -run '^TestSessionNamingUtility' -count=1
```

This selector names five adapter groups. From codex-web, pending schema checks
use the exact candidate-generated schema directory and pinned config schema:

```sh
python3 test/codex_protocol_contract.py \
  /tmp/automatic-session-slugs-schema codex/client.go
python3 test/codex_ephemeral_config_contract.py \
  /nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source/codex-rs/core/config.schema.json
```

Suggested focused split: provider contract/tests/policy/reference and private
fixture diagnostics together; consuming adapter/tests/preparation docs together.
Coordinator owns final prose, checks, commit authorization, dependency/resource
refresh and related reviewer0 rerun before the next native release attempt. The
session and refs remain open; unrelated browser/race/compatibility/VM evidence
was not repeated.
