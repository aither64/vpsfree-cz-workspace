# Add an opt-in Pi backend alongside Codex

Package P, architect0, 2026-11-12. **Plan only: no implementation package is
assigned or released by this document.** K was completed, reported and accepted
before P. Session/environment and retained workspace-write access were verified;
unchanged required procedures and documentation skill were reused. Lead owns
allocation, acceptance, tracking and the user answer.

## Outcome and scope

Add Pi to the existing portal so the user can evaluate it in new, explicitly
selected development sessions. Keep every existing Codex session on its original
backend, fully writable and runnable with its current tools, queues, members,
terminal access, history and recovery. Do not change the new-session default.
Initially one backend owns an entire development session, including its retained
lead and members; a provider/model override does not change that backend.

The first useful milestone is a limited opt-in Pi session with manual chat,
streaming/history/reconnect, stop, process accounting and shared authentication
on a proven provider. It is not held behind every team feature or Daybreak
entitlement. Its unsupported operations are explicit; uncertain delivery stays
held and dependent automation stays disabled. Later milestones add the requested
team/reviewer/watcher workflows, member providers and finite fallback, optional
questions, Plan behavior and complete installed recovery checks.

Use the existing portal UI and a narrow host adapter. Do not build a general
agent server, emulate Codex App Server, rename/split repositories, or introduce
a generic scheduler/goal engine for native-feature parity. Existing naming and
other Codex-only control-plane utilities may remain behind their native adapter.
Pi-specific gaps are capability-gated, never successful no-ops or restrictions
on otherwise working legacy Codex.

**Deferred entirely:** conversation converter/import pipeline, export standard,
cross-backend handover, cutover framework, archive conversion, retirement
automation, legacy-daemon rehosting and default switching. Later conversion
should prefer the full representable conversation with originals/omissions
preserved; a summary is a fallback if full conversion proves too costly. That
preference adds only clean ownership/history boundaries now, not migration code.
Pi terminal attachment, an authentication broker/gateway and hard scratch quotas
are also outside this initial work.

## Source and repository ownership

The fixed investigated inputs are:

- **D, dev-workspace:** [`6587c4c1cedabee95bcc52f4667e7d33e3a82859`][D]. Owns
  runtime/session authority, CLI, teams, credentials, worker packaging and host
  orchestration.
- **C, codex-web:** [`dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`][C]. Owns reusable
  HTTP/browser conversation views and the unchanged public native Codex client.
- **Pi:** [`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`][Pi], inspected main source;
  not certification that all behavior ships in the observed v1.5.2 tag.

D continues to depend on C through its flake and Go module; C must not import D
or acquire site/team/host policy. Keep `C/codex/` public types and native APIs
compatible. Add a neutral conversation path with adaptation for existing
`Client`/`Target` callers; do not directly replace their Codex-typed signatures
and break embedding applications. No new repository is needed.

The accepted supporting briefs are [runtime/process plan](pi-runtime-plan.md),
[backend boundaries](backend-evolution-boundaries.md), and the
[exact source/check map](backend-integration-map.md). Provider, question and auth
details remain in [fallback](provider-fallback-evidence.md),
[questions/extensions](extension-and-question-evidence.md), and
[authentication](authentication-evidence.md). This main plan controls initial
scope, package ownership and milestones; subordinate package labels are not
additional assignments. [design.md](design.md) retains feasibility rationale.

Before later implementation, fetch/rebase in this initiative's own worktrees,
read changed repository guidance, and record the actual chosen base/head/input
graph. These source snapshots are evidence, not a claim about the deployed build.

## P0: finite decisions before dependent implementation

P0 is the first separately authorized implementation/prototype package, initially
timeboxed to 3–5 engineer-days. Use one disposable fixture, fake provider/auth
data and one lead/member pair in each of two sessions. Compare **SDK workers**
against **stock RPC workers plus a small reviewed first-party extension**, using
the same operations. Choose one production path and remove the unused probe
alternative from production packaging. No maintained Pi fork, monkey patch or
host-outbox-as-acceptance workaround is an acceptable hidden prerequisite.

P0 must deliver a short decision record and freeze the contracts its consumers
need, with two separate results:

| Gate | Required evidence | Consequence |
| --- | --- | --- |
| Pilot-ready adapter | Supported session/tool/resource APIs; exact member identity; private history/settings roots; shared canonical auth-directory configuration; manual send/history/stream/stop and outcome mapping | Basic Pi work can proceed. Lost acknowledgements retain durable `Unknown`, visibly held with no automatic resend. Unsupported queue/team/fallback recovery remains disabled. |
| Automation-ready admission | Supported stable request identity and reconciliation at acceptance/acknowledgement/restart boundaries, without a maintained fork | Release only automation whose native acceptance/recovery proof passes. A host outbox proves intent, not Pi acceptance; arbitrary external tools never gain an exactly-once guarantee. |
| Launch-ready containment | Exact session cgroup and mount namespace, distinct loaded worker processes, required UID/groups/repository/Nix/tool access, shared fake auth directory/locks/replacement visibility and retained scratch | Required before any usable Pi worker launch. Unsupported isolation or tool access cannot be replaced silently with an unisolated worker. |

Try the rootless service route first. If it cannot retain required tool/user
semantics, report the precise failure and stop that route. One narrow
host-created namespace launcher is a conditional alternative for lead allocation;
it runs workers as the original UID and does not grant agents host mount
administration privileges. Do not expand into kernel, quota or sandbox research.

Test send before/after acceptance, lost reply, worker restart, queue intent and
tool intent/result boundaries. Record where `Accepted`, `NotSubmitted` or
`Unknown` can actually be established. An honest held Unknown is sufficient for
the explicitly limited pilot, but is not transparent automated recovery. If no
supported automation mechanism exists, report that blocker; do not quietly
declare full integration ready or start a new harness project. Reconsidering
experimental Pi Durable is a consequential substrate decision for lead/design
acceptance, not an automatic expansion of P0.

Also prove configuration separation: canonical auth is shared, while native
conversation/session files, mutable settings and per-member routing state are
private to their owners. Check SDK and RPC defaults, including whether a model
selection persists global defaults. A command-line flag or extension name alone
does not prove isolation. Daybreak-specific access is a separate route gate and
must not block an independently proven ordinary provider.

## Narrow contracts to implement

### Identity, authority and package fences

Use these internal concepts, not a new public protocol/export format:

```text
SessionRef       = trusted workspace + development-session slug
BackendBinding   = SessionRef + kind(codex|pi) + contract version
ConversationRef  = BackendBinding + retained lead/member address
                   + existing incarnation + native conversation identity
ExecutionHandle  = ConversationRef + current runtime generation
```

Validate known legacy records and normalize their backend to Codex **in memory**.
Do not bulk rewrite old authorities, rosters, manifests or receipts. New Pi
bindings use explicit versioned private state under the existing session runtime
authority; unknown versions/kinds and ambiguous bindings refuse. Extend package
capability fences so an older writer cannot overlook Pi state and create a
Codex authority for the same session. P0/authority work must name the exact new
schema/path and reader/writer fence before dependent mutation packages release.

Every request resolves opaque portal session/member IDs through trusted host
state and existing transition/runtime/roster locks. The browser/model cannot
choose native paths, sockets, credentials, sender identity or generations.
Backend capabilities describe support; authorization and execution admission
remain separate checks. The retained session's backend is immutable in this
initial delivery. Forks stay within their source backend; no cross-backend
transfer route is introduced.

Receipt identity binds backend, session/member incarnation, native conversation,
submission UUID, immutable payload digest, action and options. **Runtime
generation is dispatch evidence, not part of a fresh idempotency namespace.**
A restart must not make the same user operation look new. Keep old Codex
receipts and their native history proofs under the Codex adapter.

### Operations and outcomes

Introduce neutral internal views/settings/outcomes in C's conversation layer
and a small application lifecycle interface in D. Generic host/UI code must not
require `codex.*` DTOs or scattered `if pi` dispatch. Existing Codex optimizations
remain optional adapter-local behavior.

| Operation | Required behavior |
| --- | --- |
| Create / load | Retain requested backend/model/policy in the existing creation receipt before native creation. Retry the same creation identity; verify native conversation/member ownership before use. New Pi is explicit opt-in only. |
| Reconnect / watch | Rebind to the verified runtime generation; recover a current snapshot plus opaque cursor. Do not replay a send because an event stream disconnected. Stale events cannot authorize mutations. |
| Read / page history | Project typed message/tool/question/activity views with stable cursor/order and native provenance. Preserve native originals separately; display projection is not a new persisted universal transcript. |
| Send / steer | Record immutable intent before dispatch; return an evidenced acceptance receipt, positive pre-acceptance refusal, or Unknown. Steering reaches a safe backend boundary, not immediate shell preemption. |
| Queue / start / cancel | Preserve order, exact item identity, held state and dispatch proof. Queue acceptance and actual execution settings are distinct. Pilot advertises these unavailable until its selected mechanism is proved. |
| Interrupt / stop | Bind the exact current turn/worker/command handle. A requested abort is not verified process termination or reversal of external effects. Keep unresolved effects held. |
| Settings / models | Resolve trusted catalog/account references; persist requested and effective member policy. Serialize switches with dispatch and preserve settings on reload. Do not mutate another member or global native defaults. |
| Questions / decisions | Distinguish blocking approvals from optional ask-and-continue records. Validate exact request/revision/response identities and deliver through the same stable receipt boundary. |
| Outcome lookup | `Accepted` proves native acceptance, not task completion; `NotSubmitted` needs positive no-acceptance evidence; `Unknown` retains the original ID and holds further dispatch until reconciled. Missing history is not proof of no send. |

Keep history reading/projection separable from execution methods, native IDs and
source order retained, and backend-specific recovery behind its adapter. These
are the only current migration/removal seams; implement no converter, alternate
archive format or replacement reader now.

### Session runtime, workers and control plane

```text
shared portal/control plane
  -> Pi session supervisor [one owned cgroup + exact mount namespace]
       -> loaded lead worker -> local tools
       -> loaded member workers -> local tools
       -> registered temporary services
```

Prefer a supervisor subcommand in the existing Go binary with a private,
application-specific control channel. It owns ensure/inspect, worker load,
command/service start, cancel and resource observation. Native conversation
dispatch uses the selected SDK/RPC adapter. The portal never starts Pi tools
outside that supervisor. No process pool spans development sessions; dormant
members/history need no permanent worker. Do not add automatic session shutdown.

Persist launch intent and ownership outside scratch: session/backend/incarnation,
package/store identity, supervisor generation, boot and service invocation IDs,
cgroup, PID/start identity, observed namespace, scratch backing paths and live
worker/command/service handles. Reconcile lost launch replies under the original
operation ID. A replacement generation cannot admit work until the old invocation
is proven drained; unknown descendants hold recovery. Portal restart alone must
not kill the supervisor. Namespace inode/PID/path alone is not durable ownership.

Targeted worker/command cancellation uses handles and process-group/child
tracking, followed by exit verification. A single shared cgroup gives a
whole-session stop boundary, not reliable per-worker ownership of every
daemonized descendant. Ambiguous survivors remain pending; do not kill unrelated
members or report false completion. Whole-session drain occurs only through an
explicitly authorized existing lifecycle action and its recovery contract.

For new Pi temporary services, retain existing resource UUID, digest,
durable-before-launch intent and unknown-stop semantics, but launch inside the
supervisor. Current `systemd-run --user` sibling units do not share the exact
namespace. Old registrations keep their original systemd reader/stop path;
do not adopt or reinterpret existing services. Idle worker unloading must not
stop registered services or discard subscriptions, pending tools or receipts.

Use owned disk-backed `/tmp` and `/var/tmp` directories, consistently mounted
for the session incarnation. Keep the control socket and durable records outside
scratch. Crash/restart or unit-stop defaults must not erase recovery inputs;
backing-data removal stays with authorized cleanup. Expose timestamped cgroup
CPU, memory/peak/anon/cache/kernel, tasks and I/O, plus directory logical/allocated
usage. Directory telemetry is not a disk quota and misses open-unlinked files;
`df` on a bind mount describes the shared filesystem. Nix daemon/builders, remote
MCP/SSH/VM work and shared control-plane services are excluded costs.

### Authentication, settings and providers

Select native Pi shared credentials, not a new broker. All workers using one
account/grant see the same canonical writable credential **directory**, provider
key, lock sidecars and mutable replacement effects. Never copy credentials to
worker scratch or use file-only binds with independent adjacent locks. Keep
legacy Codex's rotating grant under its original authority; a Pi login/grant is
separate unless common ownership is explicitly proved. No auth attempt is
authorized by this plan.

Each worker receives explicit private native history/session and mutable settings
roots, plus immutable reviewed resource/catalog inputs. Only canonical auth is
shared. Workspace/session defaults and member overrides remain host-owned;
native model changes must not persist into global defaults. Member routing state
belongs to its own conversation/branch. P0 must prove supported configuration
for both history/settings privacy and auth sharing before selecting a worker.

Implement session default → member override → explicit finite provider/account/
model fallback chain. Capture policy revision, requested/effective thinking and
actual physical provider. Pi's native virtual-model router can select on retry,
but its retry classifier controls whether a retry starts. Verified structured
provider errors, text refusals and unknown failures are distinct. Use supported
native routing only where it meets the host contract; bound combined retry/hop
budgets, prevent cycles and keep the active route/reason visible. Preserve all
accepted prompt identities and completed/uncertain tool effects.

Daybreak's exact subscription/client/program/transport access is a per-route
acceptance item, not a prerequisite for ordinary Pi chat. Unsupported account or
model choices remain unavailable. Existing quota previews can remain host-owned;
do not fabricate Codex account/reset parity from token-cost data. Canonical auth
locking coordinates refresh but is not atomic with upstream rotation; failures
may require a real-browser reauthentication, including a hardware-key challenge.

### Host tools, teams, questions and Plan

Keep roster addresses/purposes, instructions, saved reviewer settings and access
policy host-owned. New Pi execution maps them to worker identities; bindings are
injected by the supervisor, never selected by tool arguments. Reuse existing
report/peer-message/communication policy and exact message IDs. Busy delivery,
eligible idle wakeup and held-recipient behavior need proved receipt semantics
before enabled. No automatic forwarding of every final answer is substituted
for explicit `report_to_lead`.

Pi reviewers remain independent assigned members. Fresh verification watchers
remain outside the persistent roster with the installed utility policy; use
the Pi execution adapter for their Pi-session launch/report/settlement proof.
Idle status alone proves neither command completion nor durable result delivery.
Preserve legacy Codex watcher/naming paths and package policies. Native-only
features without a supported Pi implementation are capability-gated; no new
generic scheduler or goal engine is included merely to mimic native Codex.

Optional question tooling commits a question ID/revision/caller binding before
publishing the existing choice/free-text card, then returns immediately. Later
authenticated answers have immutable response IDs and ordered corrections;
reconnect restores state independently of worker loading. Deliver to the exact
logical recipient through ordinary steer/follow-up/eligible idle dispatch, with
holds, branch/incarnation changes and late answers handled explicitly. Preselected
choices or elapsed time are not answers. Pi's in-memory blocking dialogs are
not a substitute; a host answer outbox still needs the native acceptance proof.

Preserve current Plan/Default workflow and accepted-plan identity/digest. Same-
backend implement-plan delivery must deduplicate across mode changes and retries.
Do not import the example's regex-based shell filter as a read-only guarantee;
map the current promised policy across enabled tools. Stronger isolation beyond
that contract is a separate decision. Keep answers as data, not slash commands.

Use a small first-party host-tool integration plus required official Pi built-ins.
Pin actual reviewed source/artifacts, coherent dependencies and catalogs; disable
floating executable-resource installs and silent omission of required tools.
Preserve intended skill/instruction discovery. Keep model catalog updates
controlled: a source pin alone does not freeze Pi runtime catalog overlays.
No external extension shopping or unreviewed package is needed.

## Work packages, release gates and sequencing

All owners below are **proposed retained members**, not current assignments.
Lead checks capacity, accepts the sufficient brief and releases each complete
package. An owner executes one package at a time. Architect0 owns contract
decisions; architect1 advises runtime constraints and architect2 identity
boundaries. The following is the single allocation table; M/N/O tables supply
evidence, not competing file ownership.

New paths below are proposed and must be recorded once P0 selects the worker:
`D/pi-runtime/`, `D/portal/internal/agentbackend/`,
`D/portal/internal/piruntime/`, and `C/conversation/backend*.go`.

| Package / proposed owner | Deliverable and owned files | Dependencies / release status | Acceptance evidence |
| --- | --- | --- | --- |
| P0 / implementer1, architect0 accepts decisions | Disposable fixtures/decision record; selected worker API, launch route, identity/outcome/settings/auth contracts | Ready to allocate only after implementation/prototype authorization; no production work released now | Separate Pilot/Automation/Launch results, crash-boundary matrix, exact pins; supported mechanism or explicit blocker; bounded stopping condition |
| P1 neutral seam / implementer0 | C `conversation/handler.go`, neutral view/operation files and compatibility adapter; targeted C browser/tests; native C `codex/` behavior retained | Can release when neutral contract above is settled; independent of Daybreak and host launcher | Existing public callers compile; existing Codex HTTP/browser behavior/authorization/receipts preserved; generic layer consumes neutral types |
| P2 host authority and integration / implementer2 | D `portal/internal/agentbackend/`, `session/{authority,recovery,contract,runtime-contract.json}`, creation/resolver paths and central composition | Identity/version/receipt contract settled; execution paths depend on P0/P3. Owner retains central integration windows through pilot/parity assembly | Known legacy records unchanged; explicit Pi creation/old-writer fencing; no cross-backend routing; wrong member/epoch refusals; original IDs survive restart |
| P3 supervisor and worker / implementer1 after P0 | D `portal/internal/piruntime/`, `portal/cmd/workspace-portal/pi_runtime.go`, `pi-runtime/` core/entrypoint, Pi unit, `workspace-host` Pi launcher and Pi service execution path | Pilot and Launch gates plus P2 authority. Automation subpath remains blocked until its gate | Manual stream/history/stop; separate member workers, exact namespace/cgroup, private settings/history/shared fake auth, scratch/restart/service ownership, truthful Unknown |
| P4 provider/account routing / implementer5 | D provider/catalog/model adapters, `pi-runtime/src/providers/` and provider fixtures; existing Codex provider implementation unchanged | P0 worker settings/auth contracts and P2 binding; ordinary route independent of unproved Daybreak; automatic fallback needs Automation gate | Member-local overrides, finite visible routing, actual account/model/thinking proof, canonical auth locking; no global persistence/cross-member mutation; unavailable routes honest |
| P5 team/reviewer/watcher / implementer3 | D `agentteams`, `teamruntime`, `monitoroperation`, `communication`, `progressobserver` execution adapters; `pi-runtime/src/host-tools/reporting*` | P2/P3 identity and Automation gate; P4 model validation for assigned roles | Exact caller/report/launch receipts; busy/idle/held delivery; retained reviewer policy; fresh watcher result/stop/restart proof; legacy contracts pass |
| P6 questions/Plan/UI / implementer4 | New D web question/plan modules, C question/view projections after P1, `pi-runtime/src/host-tools/questions*`; browser fixtures | Neutral types/question policy can be prepared independently; live answers/Plan dispatch require proved admission and P2/P3 | Ask-and-continue, late/corrected/retried replies, reconnect/holds/staleness; accepted-plan dedup; existing Codex UX unchanged |
| P7 packaging/checks/docs / implementer0 after P1 accepted | D C-dependency pins, `flake.nix`/lock, `portal/go.mod`/sum, vendor hash, `nix/workspace-portal.nix`, worker derivation/check wiring; maintained D/C docs with technical owners | Scaffolding after selected manifest/launch contract; final checks after intended packages complete | Reproducible coherent runtime/catalog/extension inputs; installed dual-backend compatibility; exact revisions/check matrix and review packet |
| H0 conditional host support / implementer2 after central conflict window | D host module and only necessary aitherdev configuration paths in configuration repo | Only if rootless route fails and lead accepts/allocates bounded host route; separate repository/deployment scope | Original UID/tool semantics plus exact namespace; no agent mount privilege; compatible package/recovery evidence |

**Integration and pin ownership:** implementer2 exclusively integrates changes
to D `portal/internal/web/server.go`, CLI `main.go`, `static/app.js`,
`libexec/dev-session` and `session/runtime-contract.json`. Other packages expose
module APIs and pass required integration changes to that owner. Implementer1
owns `workspace-host`, supervisor/service launch changes and worker entrypoint;
provider/question/reporting subtrees are disjoint, and their registration is
sequenced through that entrypoint owner. Implementer0 alone updates C→D flake/Go/
vendor pins and package manifests after module requirements settle. Sequence
the Pi unit/launcher versus final packaging edits, and P6's C edits after P1's
interface window. Do not allow concurrent edits to these shared files.

All implementers own their package tests, technical docs, commits, source/check
evidence and review fixes. Use private fixture homes/databases/sockets; no shared
mutable test state. Per-repository index/commit/rebase windows are exclusive even
when source edits are disjoint. C and D windows can be independent. Publish C's
tested feature dependency before updating D pins; do not reverse dependencies.
Repository claims are for separately approved default-branch integration only.

## Finite milestones and done criteria

1. **Contracts and P0 result:** record selected worker/launch approach, precise
   identity/schema/old-writer fence and operation outcomes. Release P1 and safely
   independent modules once their relevant contracts settle; do not wait for
   unrelated account access. A failed critical gate has a concrete owner/result.
2. **Usable opt-in pilot:** P1/P2/P3 plus the minimum proven P4 path expose
   explicit limited Pi creation, manual chat/history/reconnect/stop and resource
   accounting. Prefer an explicitly selected Solo pilot until team execution is
   proved; never silently downgrade a requested roster. Codex default and all
   existing sessions remain unchanged. Unknown sends stay held. Review and
   applicable installed checks precede any separately authorized pilot deployment.
3. **Requested workflow coverage:** Automation gate then P4/P5/P6 enable proved
   member routing/fallback, teams/reviewer/watcher, queues, optional questions
   and Plan. Unsupported routes/features remain explicit. A missing Daybreak
   entitlement blocks that route, not successful independent capabilities.
4. **Initial integration ready:** all intended changes committed, quick checks,
   independent final review and required long/installed checks passed; both
   backends preserve their recovery contracts. Document supported Pi capabilities,
   unresolved optional routes and operational recovery. This is readiness for
   explicitly scoped deployment/integration, not automatic authorization.

The initial delivery is done only when the agreed Pi capability set works in
opt-in sessions and legacy Codex regression/installed checks pass, with no
unresolved required review/recovery work. A pilot is a usable milestone, not a
claim that all initial integration work is complete. No migration/removal/default
switch is part of these done criteria.

## Verification and delivery sequence

No command below was run in this planning package. Start with targeted fixtures
against actual selected APIs; stop broad runs on a failing contract. Quick checks
run before final review; long/uncertain builds, integration and CI waits use fresh
verification utilities under the monitor skill. No live credentials are needed
for namespace/refresh-lock fixtures.

| Lane | Existing command or future focused evidence |
| --- | --- |
| C quick | In its package-derived Nix environment (`nix develop .#packages.x86_64-linux.default`; C has no devShell), `go test -mod=readonly ./codex ./conversation`; `node --test test/conversation_browser_contract_test.cjs test/sync_browser_contract_test.cjs test/questions_browser_contract_test.cjs test/delivery_retry_browser_contract_test.cjs`; `python3 test/codex_protocol_contract.py --coverage-only codex/client.go` |
| D quick | From D `nix develop`, in `portal/`: `go test -mod=readonly ./internal/session ./internal/teamruntime ./internal/monitoroperation ./internal/communication ./internal/web ./cmd/workspace-portal`; target relevant `-run` cases first. `node --check internal/web/static/app.js`; `node --test internal/web/optional_questions_browser_test.cjs internal/web/codex_providers_browser_test.cjs internal/web/read_cycle_browser_test.cjs` |
| D CLI/service | From D Nix environment: `ruby test/run_ruby_suite.rb dev_session_test.rb` and `ruby test/run_ruby_suite.rb workspace_host_test.rb`. Existing exports include `.#checks.x86_64-linux.ruby-dev_session-0` through `-3`, and `ruby-workspace_host-0`; aggregate unique coverage is required for whole-suite claims |
| New worker/contracts | Add selected worker's type/unit commands to its pinned manifest/Nix check before release; do not invent commands for an unchosen substrate. Fixture cases: legacy-default/unknown-version routing, stable receipt across restart, exact auth-directory lock/replacement with private settings/history, capability refusal, stale worker/tool/question handles |
| Packaged checks | Both repositories: `nix flake check --print-build-logs`. D's existing evaluation gate: `nix flake check --no-build --print-build-logs`. Do not treat a pin-consistency or compilation pass as runtime acceptance |
| Longer installed/KVM | From D: `nix build --no-link --print-build-logs .#checks.x86_64-linux.session-creation .#checks.x86_64-linux.session-archive-lifecycle .#checks.x86_64-linux.session-recovery-boot .#checks.x86_64-linux.host-module-idempotency` |

Extend disposable installed scenarios, not the live workspace: two distinct Pi
session namespaces/cgroups; lead/member/tools/service inheritance; fake shared
auth but private native settings/history; foreground and detached child cancel;
ambiguous-survivor hold; portal/supervisor restart; scratch preservation and
open-unlinked usage caveat; lost create/send/service/report/answer acknowledgement;
duplicate/corrected questions; queued settings and provider change; ordinary
Codex follow-up/tools/queue/member operation beside Pi. Verify Pi archive/revive
and explicit shutdown only in authorized fixtures, preserving old registration
and lifecycle-journal behavior. Report actual source/package/unit/generation
identities and remaining Unknown outcomes.

Mandatory final review starts only after **all intended changes for the completed
substantive deliverable** are committed and quick checks pass, before long
integration checks. Intermediate package completion alone does not trigger it.
Earlier advisory review requires an explicit user request and cannot replace
final review. A separately scoped, completed pilot may receive its own final
review before deployment. Final branch readiness still requires review of the
complete exact base/head series, interactions, consolidated history and migration
conclusion (including no legacy conversion); prior pilot review is not blanket
acceptance. No reviewer is assigned by this plan. Preserve repository hooks and
use published feature branches, not automatic PRs.

Before any authorized deployment, read the selected package coordination and
deployment procedures; prepare builds, immutable source/input graphs, store
paths and recovery outside machine ownership waits. Keep forward-only package
recovery: a corrected compatible package may disable new Pi creation while
retaining Pi state readers/reconciliation and unchanged Codex execution. Never
downgrade past a state fence or delete receipts to recover. If H0 is required,
apply the reviewed host prerequisite before dependent user-profile activation;
otherwise avoid host configuration changes. Verify old Codex and opt-in Pi after
activation. Deployment and repository integration need their separate explicit
scope; no default switch or session lifecycle action is inferred from completion.

## Effort and remaining release blockers

P0's initial 3–5 day timebox produces a technical decision and usable-pilot path,
not guaranteed full automated parity. The earlier 6–12 week one-engineer estimate
was a narrower feasibility baseline; the session containment, questions and
member fallback additions are not independently priced. Re-estimate after P0
selects the supported mechanism and host route, using the actual package diff.
Parallel modules can shorten elapsed time after contracts settle; no automatic
two-person speedup or precise new total is asserted.

Not yet release-ready: supported automated admission/reconciliation; exact
namespace setup with required tool permissions; concrete versioned Pi binding
and old-writer fence; supported SDK/RPC private settings/history plus shared-auth
configuration; and route-specific account/model/error proof. Only dependent
work waits on each blocker. Native error categories, OAuth/client access and
Daybreak are not inferred from catalog labels. No broker, migration platform,
retirement framework or further source inventory is needed to finish this plan.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

[D]: https://github.com/aither64/dev-workspace/tree/6587c4c1cedabee95bcc52f4667e7d33e3a82859
[C]: https://github.com/aither64/codex-web/tree/dd90fb4308ba85617ee2a4267cc835aa9a4f11ce
[Pi]: https://github.com/earendil-works/pi/tree/a22b888a58fe55b668cc45b80749ec88d4eb4ddc
