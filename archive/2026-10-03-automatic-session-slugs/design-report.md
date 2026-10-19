# Architect report

The independent runtime design is ready for implementation and was accepted
by the coordinator. [design.md](design.md) covers preparation/replay, exact team
snapshots, crash recovery, upload retention, allocation locks, receipt handoff,
browser drafts, compatibility and verification. The bounded utility supplement
is ready for implementation: public API, exact config/source evidence, private
request rejection, corpus changes and an exact-binary mock-provider fixture.
The restricted contract is confirmed by the user. The coordinator clarified
that serving-instance global policy is trusted and operator MCP reconfiguration
pauses naming through existing procedures. These are documented support limits,
not blockers. Exact-binary proof of the model-action boundary is still required.
The latest bounded clarification selects explicit `InstructionFile` input and
distinguishes async question notifications from request-ID-bearing question RPCs.
It does not change the accepted action-tool or trusted-operator boundary.

## Accepted clarifications

- Resolve and freeze exact settings from local installed policy at acceptance;
  validate live model availability in initialization. Preserve legacy caller
  validation, never substitute defaults, and report unavailable settings as a
  precise failed/retry state.
- Add the narrow CLI reservation guard under existing creation/slug locks.
  Ordinary CLI syntax/explicit names remain unchanged. Internal handoff requires
  the exact predetermined receipt ID, request, preset and deletion epoch.
- Recovery uses a newer package containing prior behavior. Never use
  `workspace-host rollback`, an earlier-generation switch or a system app pin.
- The user confirmed: "Keep model naming, disable tools that access files or
  networks, and reject questions immediately (recommended)." Pure clock may
  remain. Questions fail the utility before normal prompt admission; no UI,
  timers or auto-answer. No Codex patch/model bump or new production process
  framework is authorized. Project/workspace/team instruction injection stays
  disabled; global user instructions remain trusted serving-instance policy.
- Add required trusted `InstructionFile string` to `EphemeralTurnOptions`. One
  explicitly supplied empty private file serves both instruction/compact file
  overrides outside the private empty cwd. No hidden filename convention,
  arbitrary config input or provisioning framework.
- Async question notifications immediately fail the utility without UI admission
  or a fabricated RPC reply. JSON-RPC `-32601` applies only to a question request
  with a real outer request ID. The coordinator accepts both as the selected
  immediate-rejection behavior, followed by private teardown and fallback.
- Preserve the consumed runtime policy-3 predecessor and all four published
  extension commits through `399c3302` unchanged as exact ancestors;
  final dependency layers retain their complete nested closure/source behavior.
  This avoids a deployed-contract regression and does not grant integration
  approval or ownership of the predecessor's branch/records.

## Bounded implementation units

| Unit | Deliverable | Dependency / key evidence |
| --- | --- | --- |
| 1. Preparation storage/API | Separate strict v1 records; immutable input digest/full team snapshot; 512 unfinished and 10,000 reserved eventual mappings; status/retry API; tracked worker shutdown | Ready. Fault injection for intent/acceptance writes, duplicate IDs, limits, nonblocking acceptance and package-generation change |
| 2. Upload acceptance | Existing initial-submission fields encode a request-owned pending claim; staged intent → catalog pin → accepted record; transactional mutation exclusion and handoff | Ready. No upload schema extension. Old-source collector/delete/append/prepare fixtures, crash gaps and distinct-tab scope ownership |
| 3. Allocation/receipt handoff | Saved naming base; serialized suffix reservation; narrow CLI guard; supplied-ID receipt acceptance; mapping before receipt eviction | Ready with injected name generator. Exact-ID adversarial replay, concurrent CLI/portal creation, journals, epoch changes and missing-receipt crash recovery |
| 4. Browser/progress | Optional custom name; durable verified ID/snapshot; uncertain-response recovery; preparation page and safe redirects; preserve plan/fork flows | Ready. Extend existing browser contract and Playwright creation suites; include storage failure, catalog change, attachments, XSS and URL cases |
| 5. Ephemeral helper/naming adapter | Public generic helper, fixed restriction config, private pre-admission request sink, bounded lifecycle, exact model/effort, raw-text limit/fallback and binary fixture | Ready with the finite config/RPC recipe. Live naming requires exact-binary proof under the documented trusted-operator boundary |
| 6. Pins/documentation/rollout | codex-web → runtime preserving exact `4ef298b3` → extension preserving all four exact ancestors through `399c3302` → assembled package; complete lock/source diff, owning docs and canaries | Whole review includes inherited deployed ancestry; own extension diff against `399c3302` is pin-only. After quick checks, commits, mandatory review and watcher-run longer checks. No default-branch merge authorization |

Keep units in the existing packages; no new workflow framework. Implementation
owns source edits. The coordinator owns final visible-copy review, state and
portal artifact links, exact revision inventory and rollout.

## Deployed predecessor and review scope

The coordinator verified runtime default
`924c0ec28c41dd8b56aaf17f2212b302ca614899` is current, but shared pre-feature pins
consume runtime `4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4` through extension
`399c33023a568a8d7a21e4e4df52829628720a28`. Runtime `4ef298b3` is one published,
unmerged descendant: `runtime: require maintenance-aware cluster transition
policy`. It advances policy 2 to 3 while retaining schema 1; installed package
`zmwh78…` already declares policy 3. This is consumed ancestry, not stale refs.

Selected operation: once helper work is committed and runtime is clean, rebase
only our unpublished runtime feature commits onto exact `4ef298b3`, preserving
that commit unchanged. Coordinator/implementer owns the operation. Never fold,
rewrite or replace it or touch its owner's branch/records. Final review must
include `924c0ec2..final-head` with inherited deployed provenance and can also
show `4ef298b3..final-head` for our functional diff. No integration approval is
inferred. Codex-web's deployed/default base stays
`4c170393a96ed0a6ac2e43488d073f6fcab36132`; unrelated `FETCH_HEAD` beginning `7a`
is not a base.

The coordinator also verified extension default
`8f8d8ecf5031c40d3e4a4ee2e9425721fc035800` and the four published, unmerged
commits through deployed `399c33023a568a8d7a21e4e4df52829628720a28`.
Preserve all four exact SHAs unchanged as ancestors, oldest first:

| Extension commit | Subject |
| --- | --- |
| `5b2e9a4bb95bcf4070d62da33b219ed3c5a33f12` | flake: require the maintenance-aware runtime transition policy |
| `101d31264fb54cc39b2d0d9519a202d0705a7078` | vpsadmin: preserve stopped clusters through maintenance copy |
| `f50c92bf146c3f3d93a5293e0c005f5fdb3a26e2` | vpsadmin: preserve assignments in the development storage profile |
| `399c33023a568a8d7a21e4e4df52829628720a28` | vpsadmin: test retained services through interrupted maintenance |

Their 25 files/5,288 additions/67 deletions are already deployed behavior, not a
feature expansion. Correcting only the runtime pin on old extension `8f8d8ecf`
would still regress consumed source. Our extension branch is coordinator-verified
clean with no own commits; the coordinator selected fast-forwarding it to exact
`399c3302` before updating the runtime pin. No other owner's refs/records or
published predecessors may be rewritten. This report performs no branch action.

Final extension review includes `8f8d8ecf..final-head` with the complete consumed
four-commit lineage/provenance, plus `399c3302..final-head` for our intended
pin-only diff. Extension/root pins carry runtime `4ef298b3` plus our feature.
Preserve the complete nested dependency closure/source behavior and all
unrelated lock nodes. No integration or host mutation is authorized.

The coordinator verified fixture baseline `924c0ec2` and deployed `4ef298b3` are
byte-identical for the entire `portal/internal/uploads/` subtree,
`libexec/dev-session`, `portal/go.mod` and `portal/go.sum`. This is narrow
predecessor source equivalence, not whole-package equivalence or execution proof.
The old-reader fixture remains pending post-review execution.

### Final pin's host-migration applicability

**No new host-migration VM trigger for runtime
`51dca869fe50c20b6669d4770856fca0971fc9c2` and the prepared extension pin diff
against deployed `399c3302` plus `4ef298b3`.** Extension source is unchanged;
only `flake.nix`/`flake.lock` select that runtime and nested codex-web
`ca0f3bc980ca99454d000761aeee37b4b9bbafc3`. The full exported contract remains
unchanged (cluster schema 1/policy 3/authority policy 1). Source inspection also
establishes the private-state boundary; equal policy alone is not the reason.

- Extension `bin/vpsfree-dev-workspace-migrate` moves complete user-state trees
  (`migration_pairs:519`, `apply_moves:586`), fingerprinting relative paths,
  bytes and metadata recursively (`fingerprint:1940`). Its rewrite/validation
  inventory is authority JSON, registry and portal manifests
  (`rewrite_candidates:800`, `rewrite_path_allowed?:904`,
  `rewrite_machine_state:1029`), not portal-private JSON. New records therefore
  move unchanged with their parent; no record allowlist or rewrite limit applies.
- Runtime `web/operation_store.go:34`, `userstate/paths.go:11` and
  `web/preparation_store.go:58,94,110` keep full records and compact mappings
  under `<user-state-root>/portal/<workspace-id>/`. Workspace identity stays the
  checkout path; request/receipt IDs, slug, epoch and digests remain valid when
  their bytes are preserved. Frozen preset values reuse receipt schema 3's
  existing `directTeam`/`teamruntime.Preset`; existing receipt schemas do not change.
- `web/uploads.go:22` and `uploads/store.go:82,377,812,882,900` retain sibling
  `uploads/`, schema-1 catalog and existing file paths. The request claim uses
  existing initial-submission fields (`preparation:<id>`, pending, scope/file
  IDs), followed by existing slug/epoch/thread binding. Migration need not parse
  these new application ownership semantics. Existing authority lock inventory
  already covers creation/slug locks; stopped writers and transition exclusion
  remain required.

These paths are relative to extension `399c3302` and runtime `51dca869`; linked
sources and detailed reasoning are in [design.md](design.md#host-migration-applicability-for-runtime-51dca869).
This concludes generic preservation for the actual unchanged-namespace rollout,
not arbitrary relocation support: upload wire text already contains absolute
file paths at `4ef298b3`, and migration preserves it, existing receipt goals and
the new snapshots unchanged. This feature introduces no state-root move or new
rewrite requirement. The inherited extension lineage remains in whole-branch
review without becoming a new incoming host transition.

No migration test was run or claimed. Normal packaged Ruby migration/host-path
checks, feature compatibility and exact-binary isolation gates remain required;
independent review must assess this conclusion. Reassess any final diff that
changes the stated boundaries. Generation, holds, ownership and schema guards
remain enforced; this assessment authorizes no host mutation or integration.

## Utility decision evidence

Installed Codex 0.160.0 supports ephemeral threads and JSON output schema, but
the inspected public protocol/config does not expose its internal empty
`ToolPolicy.allowed_tools` ceiling. Bundled `gpt-6-luna` metadata advertises
async user-input and clock, and source tool construction adds those independently
of ordinary disabling flags. Empty dynamic tools/read-only/never approval do
not prove literal no tools.

The supported `model_catalog_json` path loads the shared models manager at
startup. Per-turn metadata overrides explicitly drop catalog replacement and
do not replace experimental tool capabilities. A per-thread catalog file is
therefore not a supported solution; no shared catalog rewrite, Codex source
patch or model-version change is authorized.

The restricted utility is now the confirmed contract. The supplement's table
maps the exact supported thread/config keys to source functions: empty execution
environments/roots/capabilities; explicit instructions/private cwd; disabled
shell/code execution, search/images, plugins/apps/skills, delegation, memory,
goals and hooks; `notify: []`; per-server MCP disablement; no sleep/update-plan
or ordinary input tool. Removed flags are explicitly excluded as evidence.

Use a private per-call client/connection with the event sink installed before
starting an ephemeral thread. The additive API remains
`Client.RunEphemeralTurn(ctx, EphemeralTurnOptions) (EphemeralTurnResult, error)`
with model, effort, instructions, input, output schema, trusted directory and
required trusted `InstructionFile`.
Never use persisted `Subscribe`/`Send`/`Resume` or copy parent client policies.

Pinned `RequestUserInputAsyncHandler` source emits `item/started` and
`item/completed` agent-message notifications with `delivery: "async"`, nonempty
`questions` and phase `final_answer`; it returns `accepted:true` internally.
There is no outer RPC request ID. Fail on the first matching notification before
answer/UI admission, send no reply, and never treat its item ID as an RPC ID.
The internal acceptance is not reversible; the selected contract is prompt
local failure, no UI/persistence and deterministic fallback.

The separate `EventMsg::RequestUserInput` path sends
`item/tool/requestUserInput` with a real outer request ID. Reject that request
with `-32601` and fixed text, then fail the utility. For both paths, latch failure
against later success, interrupt/unsubscribe within the existing deadline and
close the private connection. Existing `rejectUnsupported` is unsuitable because
it records notices and adds a timeout. Early notifications must not await turn
completion or the full timeout. A leak into ordinary UI/persistence or inability
to fail promptly is a material contract failure, not an accepted approximation.

Every new outgoing call site and consumed shape belongs in the existing exact
protocol corpus; validate restriction keys separately against the pinned config
schema. The adapter retains `gpt-6-luna`/`low`, first 8192 raw-text bytes at a
UTF-8 boundary, ten seconds including queue/connect/model lookup, two calls per
workspace and deterministic fallback. No second model attempt/substitution.

The coordinator resolved the two previously reported source limits by defining
the supported trust boundary. Record both in public helper docs and review:

- `AgentsMdManager::refresh` appends shared global user instructions independently
  of project byte limits and empty environments. Fresh roots inherit that
  provider; global AGENTS read errors can retain old text. The internal override
  is not public. Explicit base/developer instructions do not suppress it.
  Global policy is intentionally retained. Do not require its absence or rewrite
  global files/home. If it requests an action/question, the action-tool boundary
  and immediate rejection still apply.
- MCP tables merge and active threads can refresh from new global layers.
  Per-name disablement cannot exclude a newly added name. Empty/null maps and
  before/after config reads do not establish a config lease. Capture effective
  static config once at utility start and disable every configured name. Operator
  MCP changes must pause/stop naming through existing service/package procedures;
  fresh calls then recapture settings. Normal package changes stop workers and
  revalidate generation. No arbitrary concurrent administrator reconfiguration
  guarantee, config lease, global lock or process framework is required.

`model_instructions_file` and the compact-prompt file are also read despite
explicit base instructions. A supported application-owned empty private file
override covers these two paths independently of retained global user policy.
Pass its canonical absolute path as required `InstructionFile`, setting both
`model_instructions_file` and `experimental_compact_prompt_file` to that value.
The application provisions/owns it throughout the call/teardown; the helper
validates but does not provision/delete it. Require a zero-byte non-symlink regular
file, mode 0600/application-user ownership, in private mode-0700 state outside
cwd and project/workspace trees. Invalid input fails before connecting. One file
is simpler than two equivalent paths; descriptors/inline strings cannot directly
satisfy the server's path-valued settings. No broader provisioning API is needed.

Finite sequence: private initialize → one effective `config/read` for the private
cwd and `configRequirements/read` → bounded exact `model/list` → ephemeral
`thread/start` with the explicit restriction map/empty environments → one
`turn/start` → matching final completion → unsubscribe/close. Failures interrupt
only the exact known turn within the same deadline. The design includes exact
fields, full disabling-key table and consumed protocol shapes. No settings
refresh, normal persisted conversation API or parent policy is copied.

The fixture must use the exact candidate binary and unchanged model metadata,
with a representative provider capability path, synthetic global/project/skill/
hook/MCP sentinels and an ordinary concurrent conversation. Inspect actual
model-facing tools/instructions; inject forbidden tool calls and check canary
files, network/process counts and persistent stores. Assert global-policy
sentinel retention and workspace/team/skill sentinel exclusion. Check changed
MCP inventory between paused/stopped calls, not administrator reconfiguration
mid-call. A reduced mock provider would be a false proof. Unexpected model-facing
action tools in the supported configuration remain a real release failure.
Quick fake-transport checks precede independent review; only then does a watcher
run this tagged fixture. Live proof has not passed, and fallback alone is not
full model-naming feature completion.

Extend the corpus with async delivery/questions on both started/completed
agent-message notifications (no outer IDs), ordinary absent/null metadata, and
the distinct request-ID question/error-response shape. Quick tests cover the
required file's placement/type/size/permissions and both identical overrides.
The exact-binary fixture must prove prompt failure and clean teardown for both
question paths, with zero ordinary UI/prompt/timer/persistence leakage. Exercise
the metadata-driven async path under production restrictions; use a separately
labelled exact-binary control for the otherwise disabled ordinary request-input
path, sharing the same private handling. That control is not proof of the
production tool set and adds no public configuration escape hatch. Include
early notifications and misleading `final_answer`/JSON text. Source/schema
inspection and fake-transport checks are not isolation proof; this live gate
remains unexecuted and required before deployment.

## Main risks and compatibility limits

Do not adopt an equal-content receipt with a different ID. Persist slug/ID/epoch
before handoff, reserve across the write gap, and compact replay mappings before
receipt eviction. The final crash table has one row for frozen slug/ID with a
missing receipt and one distinct row for an installed receipt with a missing
handoff marker.

Old readers retain separate files and pending upload entries. Old CLI code
cannot enforce new reservations: newer recovery must detect and refuse its
conflicting destination. Safe preservation/conflict detection is the promised
compatibility boundary. Source shows old Delete rejects pending references;
old Prepare/Create can add competing records. Concrete baseline fixtures must
prove accepted file retention and safe refusal. No speculative claim of full
old-code concurrency exclusion is made.

## Verification commands

These commands are planned, not executed. Existing entry points were inspected;
new selectors remain implementation proposals until registered and confirmed.
`nix develop` selects the named package/check derivation's build
environment; neither repository exports an explicit devShell. Nix environment
realization/preflight may itself be long and belongs to a fresh watcher. Once
prepared, known quick focused checks can run inline. New test prefixes below
are part of the implementation brief and must not select zero tests.
Package-derived shells export `GOFLAGS=-mod=vendor`; source worktrees have no
vendor tree, so every source Go command explicitly uses `-mod=readonly`.
Packaged Nix checks remain unchanged. See the [Go module-mode note](../../notes/dev-workspace/2026-10-03-package-shell-go-modules.md).

From codex-web:

```sh
nix develop .#checks.x86_64-linux.default -c go test -mod=readonly ./codex -run '^TestEphemeral' -count=1
nix develop .#checks.x86_64-linux.default -c python3 test/codex_protocol_contract.py --coverage-only codex/client.go
```

From dev-workspace, before review with `PORTAL_BROWSER_TEST` unset:

```sh
nix develop .#packages.x86_64-linux.dev-workspace -c env -u PORTAL_BROWSER_TEST sh -c 'cd portal && go test -mod=readonly ./internal/web ./internal/uploads -run "^Test(SessionPreparation|SessionName|PreparationUpload)" -count=1'
nix develop .#packages.x86_64-linux.dev-workspace -c node --check portal/internal/web/static/app.js
nix develop .#packages.x86_64-linux.dev-workspace -c node --check portal/internal/web/static/creation.js
nix develop .#packages.x86_64-linux.dev-workspace -c env -u PORTAL_BROWSER_TEST sh -c 'cd portal && go test -mod=readonly ./internal/web -run "^TestShippedBrowserClientMatchesSessionAPI$" -count=1'
nix develop .#packages.x86_64-linux.dev-workspace -c ruby test/dev_session_test.rb --name '/portal_start_persists_receipt_bound|portal_creation_retry|preparation_reservation/'
git diff --check
```

The existing Node browser contract runs through
`TestShippedBrowserClientMatchesSessionAPI`, which supplies its HTTP fixture URL,
allowed origin and generated module path. Direct `node --test` without arguments
is not its normal entry point. `team_settings_browser_test.cjs` imports Playwright
and launches Chromium; its `TestQuestionBrowser` registration requires
`PORTAL_BROWSER_TEST=1` and belongs after mandatory review. The new pure
preparation Node suite runs only through its registered entry point; exact names
and selectors await the implementer's frontend report/registration barrier.
Do not count zero selected tests or a missing-Node skip as successful coverage.

After committed quick checks and mandatory independent review, fresh watchers
run `nix flake check --print-build-logs` in each affected repository, race checks
and `nix build --no-link --print-build-logs .#packages.x86_64-linux.default`
in the assembled workspace. Exact race, schema, browser and proposed
mock-provider entry commands with prerequisite tool variables are in the final
verification section of design.md. Browser integration uses the existing
`node test/creation_browser.cjs` with `CODEX_WEB_SOURCE`, `PLAYWRIGHT_MODULE`
and `CHROMIUM_EXECUTABLE` from the selected Nix environment. The existing live
team-settings selector, from `dev-workspace/portal` in the prepared Nix environment
with Node, Playwright modules and `PLAYWRIGHT_BROWSERS_PATH`, is also post-review:

```sh
PORTAL_BROWSER_TEST=1 go test -mod=readonly ./internal/web -run '^TestQuestionBrowser$/^team_settings_browser_test[.]cjs$' -count=1
```

Schema generation must use the exact candidate's bundled Codex, not an unrelated
ambient binary. These corrections change verification entry points and timing,
not the accepted feature behavior.

Proposed exact-binary fixture command, from codex-web in its prepared Nix
environment, after the fixture exists and independent review passes:

```sh
CODEX_EPHEMERAL_TEST_BINARY="$CODEX_BIN" go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeralProtocolIntegration$' -count=1
```

`CODEX_BIN` must be the reviewed assembled candidate's bundled executable.
The build tag separates this watcher-only integration test from quick checks;
the explicit integration invocation must fail on missing binary/prerequisites.

## Work performed and next action

Verified bound session identity, read required guidance and accepted records,
initially inspected the two clean origin/master-based application worktrees and
installed 0.160.0 source, and generated its experimental schema in temporary
storage. The bounded supplement used source/schema reads and edited only these
two design documents; it ran no tests or further schema-generation commands.
No application edits, commits, pushes, long checks, live inference or deployment.
Nix daemon access is denied in this architect thread; direct read-only source
inspection supplied the metadata evidence instead.

Coordinator: continue the owned implementation/review assignments, preserve the
consumed runtime and all four extension ancestors before final pins, and include
both default-to-final and deployed-to-final comparison ranges for runtime and
extension, plus predecessor provenance, in the review packet.
The finite utility recipe and global-source/operator clarification remain intact;
no product preference remains pending.
Unexpected action tools under the pinned configuration still block enablement.
Link these two design artifacts from the current state/portal manifest.
The session and refs remain open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/)

## Accepted remediation design: R1 and R2

[review.md](review.md) records the completed independent review and two Important
findings. The coordinator accepted the bounded remediation and assigned
implementer0; implementation is active, while completed fixes, verification and
renewed review remain pending. Source traces describe reviewed predecessor
`edcfc18f2fdc3bdebfec7089e2bd79b2d9b918b1`, not current implementation line
numbers or evidence that active changes conform. Details and required cases are
in [design.md](design.md#accepted-remediation-design-r1-and-r2).
This reconciliation changes only these two documents; no tests were run.

1. **Published write versus durable acceptance.** `savePreparation` retains a
   renamed `running` record even when directory sync fails; admission then
   returns an error without launching a worker, while replay/retry merely
   returns that running record. Collector does not dispatch it; restart pauses
   it. Accepted repair: retain exact published identity plus bounded private
   unconfirmed-write and pending-dispatch bookkeeping; confirm required syncs
   before further state changes/success and consume `(ID, attempt)` dispatch
   exactly once. Identical POST repairs the same attempt/receipt instead of
   renaming or retry-incrementing it. Moving map assignment after sync alone
   would lose same-process knowledge of the published receipt. Also confirm a
   replayed upload claim after catalog rename/sync failure; unchanged catalog
   lookup alone is not durability proof. A fixed, ID-bound 503 persistence code
   permits frozen-body repair without a false accepted response. Collection
   aborts on unconfirmed state; mapping sync precedes receipt retirement.
   A later persistence error may stop an already dispatched worker. Once the
   write is confirmed, expose existing failed/paused explicit retry with the
   current receipt/attempt and preserved base/handoff; do not dispatch its
   naming attempt again or show a dead worker as running indefinitely. A
   progress-page retry that published an incremented attempt must recover the
   matching current token and pending launch or stopped outcome after I/O
   recovers, without remaining hidden behind GET 503/running. Keep the public
   contract within the bound 503 and existing status/retry semantics.
2. **Rejected browser draft.** The reviewed 409 covers both side-effect-free stale
   catalog validation and post-persistence failures; 404 cannot prove globally
   unused identity. Do not unlock/rewrite the old draft on either. Accepted
   alternative: offer explicit **Start a separate request** in a fresh no-opener
   tab, retaining original recovery and all original storage/files. New tab
   uses current catalog, new UUID and fresh scope; text copying, reattachment
   and submission are deliberate. Keep original text/settings and file selection
   accessible. Its body/ID/scope/files remain retained under normal contracts;
   the original may still finish. This is not replacement or cancellation.
   This makes the already documented separate-tab route discoverable without
   a rejection ledger or pretending a rejected HTTP call cancels other calls.

Real post-rename initial-admission and retry directory-sync fault regressions
are mandatory: repeated fault then healthy same-process recovery, exact
ID/receipt/attempt and one pending dispatch without unsafe acknowledgment.
Additional faults cover the changed catalog, mapping-retirement and stopped-
worker boundaries proportionately, including usable retry after later worker
I/O failure and current token recovery. Retain relevant collector/restart/
generation assertions; do not build exhaustive filesystem conformance tests.
Pure Node contracts cover stale/error/lost-response recovery and immutable old
bytes. Implement actual Playwright regressions during remediation and run them
only after renewed review. They must prove the separate tab gets fresh identity/scope/current catalog and leaves
the old attempt recoverable, including delayed acceptance. No arbitrary path
relocation, provider change, schema change or new filesystem framework is part
of this decision. Private bookkeeping and the bound 503 remain host-contract
compatible; the existing migration applicability decision is unchanged.

Coordinator owns tracking and reconciliation. Implementation, focused checks
and renewed independent review must finish before either finding is resolved
or readiness is claimed; architect remains idle.
