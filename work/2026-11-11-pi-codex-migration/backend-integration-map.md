# Initial Pi addition: source and check map (Package O)

Owner: implementer0, 2026-11-12. Planning evidence for architect0's
implementation plan; no implementation package is released here. Package D was
accepted and capacity confirmed before O. Identity/environment and retained
implementer0 workspace-write roster/access were reverified. Required unchanged
workspace procedures/documentation skill were reused; owning repository
instructions, manifests and CI were read at these accepted fixed heads:

- **D:** [dev-workspace `6587c4c1cedabee95bcc52f4667e7d33e3a82859`](https://github.com/aither64/dev-workspace/tree/6587c4c1cedabee95bcc52f4667e7d33e3a82859).
- **C:** [codex-web `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`](https://github.com/aither64/codex-web/tree/dd90fb4308ba85617ee2a4267cc835aa9a4f11ce).
- **Pi:** accepted capability evidence at `a22b888a58fe55b668cc45b80749ec88d4eb4ddc`; no new upstream research.

User scope controls this map: add/evaluate Pi **alongside working Codex now**;
one backend per development session, shared canonical native Pi credentials,
one Pi session supervisor/cgroup/exact mount namespace containing loaded
lead/member worker processes. Preserve the portal. No full Codex protocol
emulation, converter/import/export standard, cutover, archive conversion,
retirement tooling or legacy-daemon rehosting belongs in this initial plan.
Later full representable conversation conversion is a preference, not work here.
Architect0 owns contract choices; [backend evolution boundaries](backend-evolution-boundaries.md)
owns future separation rationale. This map does not add interface decisions.

## Smallest owning file groups

Paths use D/C aliases above; they identify touchpoints, not an instruction to
rewrite every listed file. Existing code references are inherited from accepted
[runtime evidence](current-runtime-evidence.md), with targeted source checks.

| Group | First touchpoints / purpose | Preserve / boundary and relevant existing checks |
| --- | --- | --- |
| Reusable conversation seam, **C** | `conversation/handler.go` (`Client`, `Target`, capabilities, optional providers), `mutation_lock.go`, `uploads.go`, `retry*.go`; needed neutral view/settings/question/receipt projections | Signatures currently use `codex.*`: changing them directly breaks embedding applications. Add the architect-selected neutral path and compatibility adaptation; keep existing `Client`/`Target` callers and optional interfaces working. `conversation/{handler,prompt_response,send_delivery,presentation}_test.go` guard authority, delivery and presentation. |
| Codex adapter stays native, **C + D** | C `codex/client.go`, `lifecycle.go`, `history_reader.go`, `thread_page.go`, `send_delivery.go`, `send_discovery.go`, `submission_{database,migration}.go`, `turn_state.go`; D `portal/internal/workspacecodex/` | Keep native transport/history/submission proof in C and workspace recovery/retirement policy in D's existing adapter. Pi does not implement native RPCs or reinterpret Codex receipts. Existing send-admission/reconciliation/history/lifecycle tests remain regressions, not code to delete. |
| Browser projection, **C + D** | C `conversation/assets/{conversation,sync,questions,uploads,retry,delivery_retry}.js`; D `portal/internal/web/static/{app,creation,codex-providers}.js`, templates | Preserve DOM/styles, HTTP authority and existing UI operations; adapt the neutral projected data/capability boundary. C conversation/sync/questions/retry browser contracts and D optional-question, settings, provider and plan browser contracts are the closest fixtures. Do not introduce Pi's picker or app UI. |
| Runtime composition, creation and authority, **D** | `portal/cmd/workspace-portal/main.go`; `portal/internal/web/server.go:60` (`codexController`/`Config`), `server.go:3875` resolver; web `creation.go`, `creation_store.go`, `cold_settings.go`, `recovery*.go`; session `manifest.go`, `authority.go`, `recovery.go`, `contract.go`, `runtime-contract.json`; `libexec/dev-session` | Current single `Config.Codex` and resolver are central dispatch seams. Route by trusted session backend/member mapping, never browser native paths. Deliberately version new authority/package capability state while preserving legacy Codex readers/recovery; no inferred migration. Existing creation/contention, authority, cold-settings and recovery tests target this. |
| Pi worker, session supervisor and registered services, **D** | Plausible new first-party `pi/` subtree for pinned worker/extension package and its tests; small Go host adapter under `portal/internal/` (names finalized by architect0). Existing `processgroup/`, `libexec/workspace-session-services.rb`, `portal/internal/session/{service_cleanup,lifecycle}.go`, `libexec/{dev-session,workspace-host}` are integration points | SDK versus stock RPC/extension remains the architect's supported-mechanism choice. Host owns supervisor/worker identity, admission/settled recovery and temporary-path leases. Current service helper launches sibling `app.slice` units: adapt the Pi launch path to inherited supervisor descendants, preserving registration/shutdown receipts. Existing service/lifecycle recovery tests plus new exact-namespace/cgroup checks are required; sibling units alone do not establish the requested boundary. |
| Settings, providers and credentials, **D** | `portal/internal/codexproviders/`, web `codex_providers.go`, `provider_models.go`, `provider_watches.go`; CLI `codex_provider*.go`; `libexec/workspace-{codex-providers,provider-admission,provider-sessions}.rb`; new Pi worker adapter | Retain Codex archive/unarchive strategy only on Codex route. Pi uses selected native model/provider primitives at the accepted boundary. Keep host catalogs/account UX and member settings, shared canonical Pi credential store/locking, explicit fallback and backend/provider distinction. Existing provider/cold-settings tests remain; new Pi fixtures must prove exact effective settings and failure policy. Do not build a new credential broker. |
| Teams, reports, reviewer/watcher and communication, **D** | `portal/internal/{agentteams,teamruntime,monitoroperation,communication,progressobserver}/`; CLI `team_mcp.go`, `monitor*.go`; web `monitor.go`, team stats; `nix/agent-teams.nix` | Roster/address/purpose/policy remains host-owned. Split native execution/caller projection from delivery policy; preserve retained reviewer settings, exact watcher receipt/settled proof, held-recipient and stable-ID semantics. Pi tools bind actual worker identity, not sender arguments. Existing `teamruntime/reporting_test.go`, monitor authority/delivery/native-repair tests, communication service tests, CLI MCP tests are closest seams. |
| Questions, Plan and turn retry, **D + C** | D web `plan_delivery.go`, plan handlers in `server.go`, `recovery_input.go`, `turn_retry*.go`; C `codex/{async_questions,prompt_response,continuation}.go` and generic question/retry views | Preserve host-owned async optional question/reply IDs and exact accepted Plan identity/delivery. Keep Codex continuation/context proof on Codex backend; implement Pi proof through its selected owner. No unconditional whole-native-interface generalization. D plan-decision/delivery/lifetime, optional-questions/required-question keyboard, retry-policy/idle tests define focused regressions. |
| Packaging and compatibility, **D consumes C** | `flake.nix`, `flake.lock`, `portal/go.{mod,sum}`, `nix/workspace-portal.nix`; `nix/systemd/workspace-{portal,codex}@.service`, `libexec/workspace-host`, session runtime contract; new Pi package/supervisor unit as needed | Keep Codex package/native launch, naming child and old session recovery usable. Package coherent Pi worker/extension/dependencies plus supervisor launcher; do not assume existing portal unit supplies the session namespace. Maintain C pin/Go pseudo-version/vendor hash consistency and new capability readers. Host configuration changes only if the chosen launcher requires them. |

**Repository direction/public compatibility:** D depends on C through both flake
and Go module pins. Reusable browser/HTTP projection belongs in C; Pi runtime,
session/team authority, supervisor, credentials and installed policy belong in D.
C must not import D or include site catalog/host details (both projects have
generic-source checks). Publish a tested C dependency before updating D pins;
no package/repository rename is needed to add a backend. Existing `codex/` public
types/native API and writable Codex sessions remain supported through the seam.

## Package release and parallel boundaries

These are allocation suggestions for the main plan, not new member assignments
or a separate prototype/approval gate. A released package needs settled relevant
authority, admission and namespace/credential contracts from architect0.
Architect2's boundary brief permits a narrower manual Pi capability surface
with automation disabled until its proofs exist; the full dependency map below
does not require broad automated parity before every useful Pi addition.

1. **Reusable seam:** C neutral projections/compatibility adaptation and existing
   Codex/browser regression fixtures. Can progress independently of Pi process
   implementation after the view/capability contract is settled.
2. **Pi owner + authority:** D worker/extension, supervisor and durable owner
   boundary together with session backend binding and creation integration.
   Settle admission/receipt and exact namespace/permission contracts before
   downstream execution packages rely on them; do not dispatch merely to fill
   parallel slots. A new subtree's pure tests can run alongside C seam work.
3. **Providers/host tools** and **teams/utility/communication** can be separate
   implementers after owner identity/settings/admission are available. Split
   worker extension files explicitly or use one extension owner; both touch
   caller-bound tool registration and must not concurrently edit it.
4. **Web/Plan/questions** builds on the neutral seam plus settled receipt and
   question policy. Packaging scaffolding can progress once the worker manifest
   and launcher contract are fixed; final package/VM acceptance depends on all
   paths, with fully editable/runnable Codex fixtures beside new Pi fixtures.

Lead should sequence short edits to `web/server.go`, CLI `main.go`,
`static/app.js`, `libexec/dev-session`, `workspace-host`, `runtime-contract.json`
and new worker composition/extension entrypoints. Separate fixtures by backend
and owner; do not share mutable test databases/homes. `flake.nix`/lock,
`go.mod`/sum/vendor hash updates have one dependency owner. Per-repository
index/commit/rebase windows remain exclusive even when source edits are disjoint;
C and D windows can be independent. Claims are only for later approved merges.

## Validation commands and intent (not executed)

Commands below come from fixed-head AGENTS, flakes, check phases and CI. Use
disposable fixtures, repository Nix tools and targeted cases first. This map
does not authorize running checks, logging in or invoking a model.

| Lane | Existing command / target | Purpose and boundary |
| --- | --- | --- |
| D focused Go/browser | In `portal/`, from D `nix develop`: `go test -mod=readonly ./internal/session ./internal/teamruntime ./internal/monitoroperation ./internal/communication ./internal/web ./cmd/workspace-portal` (narrow package/`-run` when appropriate); `node --check internal/web/static/app.js`; `node --test internal/web/optional_questions_browser_test.cjs internal/web/codex_providers_browser_test.cjs internal/web/read_cycle_browser_test.cjs` | Type/authority/delivery/question/settings/composer regressions. These commands exist; new Pi cases must test actual chosen contracts, not mirror adapter implementation. |
| D Ruby focused/exported | `ruby test/run_ruby_suite.rb dev_session_test.rb` or `workspace_host_test.rb`; exported shard targets `.#checks.x86_64-linux.ruby-dev_session-0` through `-3`, `ruby-workspace_host-0` | CLI creation/lifecycle/service/provider/package recovery. `nix/ruby-checks.nix` owns shard manifests/timings and aggregate unique coverage; a selected shard alone is not whole-suite proof. |
| C focused | Go root: `go test -mod=readonly ./codex ./conversation`; `node --test test/conversation_browser_contract_test.cjs test/sync_browser_contract_test.cjs test/questions_browser_contract_test.cjs test/delivery_retry_browser_contract_test.cjs`; `python3 test/codex_protocol_contract.py --coverage-only codex/client.go` | Preserve exported client/handler and generic browser behavior plus Codex call-site corpus coverage. C exports no devShell; use its package-derived environment (`nix develop .#packages.x86_64-linux.default`) or suitable pinned Nix tools, including Python jsonschema. |
| Existing packaged gates | Both repositories: `nix flake check --print-build-logs`; D CI first evaluates `nix flake check --no-build --print-build-logs`, then builds focused check attributes | C check phase runs corpus coverage, Go and browser contracts; D package runs Go/browser, pin consistency and aggregate Ruby. Keep these declared checks; new worker test/package commands must be specified by its selected manifest, not invented now. |
| D longer installed/VM | `nix build --no-link --print-build-logs .#checks.x86_64-linux.session-creation .#checks.x86_64-linux.session-archive-lifecycle .#checks.x86_64-linux.session-recovery-boot .#checks.x86_64-linux.host-module-idempotency` | Existing exact target names. CI creation/archive run on pushes; host/boot on master/manual dispatch; VM jobs require KVM. Extend disposable installed coverage for both backends, supervisor/namespace/services, restart/lost-ack, reports/watchers/questions and provider changes. |

Final substantive implementation: commit intended work and pass quick checks,
then mandatory independent review before long checks. Fresh monitoring utilities
own long/uncertain verification under the monitor skill. No live account/gateway
check or deployment is implied by these commands. Canonical bare repos have no
configured `core.hooksPath` or executable non-sample hooks at inspection; this is
not a hook waiver. Preserve any actual worktree/required hooks at execution.

Planning verification: owning file/test/flake/CI names inspected; no fetching,
feature branches/worktrees, application edits, builds/tests/prototypes, services,
credentials, model calls, deployment or lifecycle changes. Only this assigned
evidence file changed. Investigation/plan evidence does not trigger automatic
final review. Lead owns plan/state and architect0 owns implementation-plan/design.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
