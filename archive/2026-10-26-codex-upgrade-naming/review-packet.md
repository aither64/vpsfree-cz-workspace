# Final review packet

## Recovery/manual-input correction: final affected review at b398a9a

This is the current final packet. All intended changes are committed; the lead
independently confirmed clean status, exact head/tree, full series/diffs and focused
check logs. Earlier packets below retain their original scope and authorization.

- Repository: git@github.com:aither64/dev-workspace.git, target master.
- Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-codex-upgrade-naming/dev-workspace.
- Full base: fffbd0d59fffc09667cb39878d9f7da8bdcd3806.
- Head: b398a9a5bd611260fc3f869c27db93cfc2a2e2d1.
- Tree: 7294ab4eb82b8e504b8d7871773ddcfc31cb6a1f.
- New delta from deployed352aa4c60457d682207b900fa5835dec82e5d064:25files,+1333/-195.
  Full branch:65files,+3262/-412. Compare actual scope with this growth first;
  focused tests and existing entrypoint coverage account for much of the delta.
- Fresh SSH fetch: default remainsfffbd0d5, feature remains352a. New head is local,
  unpublished. The six prior accepted commits remain exact ancestors, no rewrite.

Complete series:

```text
4161ed088bc7bd4a72533e3c4955d8e664728588 naming: adopt prompted Codex 0.164 with bounded recovery
33ccc148fd84bd0f58725d138a2f9b3f57f9dc3a codex: preserve cancellation during loaded retirement discovery
288194c8e33ade108cd2eabbf9afae5d50f7bfeb test: settle session bootstrap before archive worktree setup
4c6c72a5a6d0c1906080def4738d5eed7ffd1024 test: check reconciliation before admitting fresh creation
a2a38579a3d188fed6039c597c67aa0d0c49e745 workspace: separate transition quiescence from delivery uncertainty
352aa4c60457d682207b900fa5835dec82e5d064 workspace: isolate native compatibility preflight storage
b398a9a5bd611260fc3f869c27db93cfc2a2e2d1 portal: restore manual input without replaying saved work

```

The seventh unit is the coherent browser/server recovery correction, tests and
owning docs. No migration of any merge/release/deployment/external-use provenance
is introduced; optional fields extend the existing deferred settings file.
No obsolete approach, fixup history or repeated dependency stream is retained.
One client255 stream and unchanged nativeEA stream remain in the naming unit.
Independently verify these whole-history and migration conclusions. Prior exact
review and narrow-fix dispositions are in review-result.md.

Focused Nix checks passed: browser unit/composer/submission contracts (including
29 preparation cases), syntax and diff checks; Go recovery/cold/Plan and related
session/runtime-client batch web7.976s/session0.394s/workspacecodex0.972s. Final
changed-path checks for pending work, conflicting request before preparation and
explicit Plan identity passed4.075s/1.256s/4.166s. Logs: recovery-ui-quick.log,
recovery-ui-final-syntax.log and recovery-manual-quick/{go-final,go-pending,
go-binding,go-plan-final}.log. Runtime-report.md supplies owning command details
and earlier fixture/compile correction history. There is no declared hook
framework and no bypass. Full mounted Playwright remains intentionally unrun
until this review; browser syntax/unit success is not live UI acceptance.

User outcome: a session that was idle before runtime restoration opens without
recovery prompts. Dismissal leaves manual input and Plan/Default available. New
input must reach the server once or explain its blocker; completed-plan and
recovery actions must not compete. The existing CPU-tab waiting message needs an
explicit same-ID Resume sending action. The user approved implementation and
autonomous aitherdev deployment, but withdrew merge/release direction.

Acceptance covers quiet idle classification without GET side effects; positive
saved-work classification; draft/attachment/ID preservation; exact original
reconciliation without unknown replay; no activation of old queues/goals from
unrelated new input; mode confirmation before fresh dispatch; and same-epoch
permission publication only after accepted receipt. Inspect the complete browser
flow as well as direct server calls: the prior regression missed their mismatch.

Also cover a retained undismissed predecessor notice: ordinary mounted-page
refresh must replace waiting with idle without a click, preference mutation,
permission grant or automatic submission. The user explicitly reiterated this.
After a failed portal activation, later CLI/team/Continue/StartQueue operations
must honor the unresolved mode/request binding before any effects. Exact receipt
reconciliation may return without activation; settings-only records do not gain
this refusal. Inspect old-epoch bindings and accepted-receipt permission rules.

The owning component is dev-workspace, consuming unchanged client255. The runtime
uses existing transition/session/roster/message locks and deferred settings. The
supported boundary includes managed portal, CLI/team/scheduler and terminal
writers, plus bounded native inactivity checks. The local operator is trusted;
raw unmanaged native clients are outside the managed contract. No new client API,
native schema, vendor computation, canary, generic lock framework or new launcher
is requested. See design.md's approved section for exact fields and ordering.

Risk is HIGH because this affects persisted message identity, explicit execution
permission, mode ordering and recovery across runtime epochs. All four review
lanes apply. Reviewer0 remains the independent retained Sol/xhigh/read_only
reviewer; reverify identity/readiness before assignment and retain saved settings.
Start with scope/proportionality; internal design approval is not scope authority.

Retain the six accepted units through deployed352aa4c60457d682207b900fa5835dec82e5d064
and add one independently useful recovery correction. Review the full base-to-head
series and explicit migration/repeated-input conclusions, reusing prior accepted
unchanged behavior. Deployed consumer sources are configuration4a725 on3b85 and
workspacea834 on051; their final mechanical refresh follows runtime publication.
Published client255 and its exact vendor/native evidence remain unchanged.

Owning documentation changed: docs/workspace-portal.md#session-recovery-after-runtime-loss
and docs/dev-sessions.md's restore/manual-input guidance. Lead directly applied
vpsfree-user-facing-writing/humanizer-en to those passages and visible browser/Go
copy after technical facts settled. Individual rollout facts stay in rollout.md.

Focused quicks precede review. Long verification follows accepted findings: final
push CI, affected existing recovery-boot check, normal matched package/output
checks and authorized same-native rollout. Reuse unchanged successful checks only
with exact derivation/input proof. Current deployment is profile5slsx/native5rm5
and systemirpd; original external cutover exit history remains unproved. Preserve
held machine2ecc, exact deployed refs and forward recovery. No foreign session
private-state reads, live sends or lifecycle actions are authorized by review.

## Runtime deployment correction, final affected review at2095417a

This is the current packet; earlier packets below retain their original scope.
Requested outcome: complete the existing Codex0.164/naming upgrade and correct the
observed deployment refusal on an idle session's hidden unresolved send records.
The user explicitly rejected this condition blocking deployment. Preserve original
attempts, no-duplicate delivery, real activity checks, persistent state and forward
recovery. Deployment/verification then integration of the four registered masters
is authorized, but the review itself is read-only and authorizes no operation.

All intended runtime changes are committed; own worktree is clean. Lead confirmed
HEAD/tree, complete log, diffstat and ordinary range-diff; read focused Go/probe and
actual dependency logs. Owner0's [runtime report](runtime-report.md) contains exact
commands/results and prior evidence. [Design](design.md), [plan](plan.md),
[state](state.md) and [rollout](rollout.md) supply scope and deployment facts.

- Runtime repository: git@github.com:aither64/dev-workspace.git, target master.
  Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-codex-upgrade-naming/dev-workspace.
  Basefffbd0d59fffc09667cb39878d9f7da8bdcd3806; final2095417afc8030b5926236917483794fa236dce2;
  treed09053350fa93fa128bb9d802946ddc044c00534. Fresh SSH default remainsfff.
  Final source is unpublished pending this review; old remote feature12cf retained.
- Whole series, in order:4161ed088bc7bd4a72533e3c4955d8e664728588 naming/raw164/final
  dependency selection;33ccc148fd84bd0f58725d138a2f9b3f57f9dc3a cancellation;
  288194c8e33ade108cd2eabbf9afae5d50f7bfeb archive fixture settlement;
  4c6c72a5a6d0c1906080def4738d5eed7ffd1024 reconciliation assertion ordering;
  6aacac71ec036ec76b0cbfc35ac230aa7e1659ed transition quiescence/drain/restoration
  and its required first-install naming prerequisite;
  2095417afc8030b5926236917483794fa236dce2 independent preflight isolation.
- Full diff40files,+1862/-212; affected12cf..2095 delta25files,+1064/-64, primarily
  regression coverage. Compare actual request and supported boundary with this
  growth before detailed review. No internal design alone expands authorization.
- Consolidation: [range-diff](runtime-quick/idle-range-diff.txt) pairs old units2–4
  exactly; unit1 differs only in final client/module/checksum/vendor selection;
  units5–6 are new. Autosquash preserved the final tree. One final client pin
  stream remains; llm-agents/native stream unchanged. Owner reports no obsolete
  approach, duplicate update stream or migration of any provenance. Independently
  conclude whole-branch history, repeated-stream disposition and no migrations.
  Before-idle-fix ref preserves exact12cf85e091b915f7d43f588c2d4f312173c60715.
- Dependency: accepted/published client255f0b4f74951ebbd0a5ab15eea7a3142be0ab93,
  tree593b8e0597d4a840ed490e1df393efb27c4b07da, base8b60554bc10c2a6bcbf9732a8b77ad959c317036.
  Reuse your completed client review; CI40486284856 passed. Runtime consumes
  v0.0.0-20261027100253-255f0b4f7495 and actual vendorHash
  sha256-r8pfbA22N3RNLZZDcbYNcpgPeU3fzSG+3Zvz+r4/TrQ=.
  One actual computation and successful final-hash build producedcabsc16q;
  exact derivation/input/output proof is in runtime-report and idle-vendor-*.
  No duplicate vendor/native generation is requested.

Acceptance and interfaces to assess:

- Host exclusive admission drains explicit sends through receipt completion;
  ordinary portal service stop closes background resume/auto-answer writers.
  Managed terminals still quiesce through the selected predecessor. Keep writers
  excluded from final observation through native cutover, including service
  configuration/reconciliation ordering. Ordinary same-native live switching stays.
- Cold unwatched ObserverOnly checks exact root/member identity, terminal history,
  known idle/notLoaded status, empty native queue and validated selected submission
  store. Malformed/active/waiting/unknown status, queue, retry/retirement ownership
  and invalid identity/store refuse. Archived identities keep their distinct proof.
  Preserve dormant prepared/submitting/unknown records and options/claims verbatim;
  never reconcile to accepted, discard or resend. Strict lifecycle checks remain.
- Preselection refusal restores prior-running portals and actually-quiesced
  terminals through the selected generation; incomplete restoration is visible.
  Postselection recovery remains forward-only. Existing claim/generation/state-root,
  lifecycle journal, cluster and retained-root contracts remain authoritative.
- Bootstrap uses existing same-native override/live-switch contract to select this
  same fixed candidate, then ordinary no-override external switch for0.164.
  Host ordinary-version mismatch suppresses every bundled naming invocation,
  including version probe, during stage1. Manual naming remains available then.
  No interleaved boot/user-manager/system-generation change or explicit reconcile;
  transient override is not a durable pin. Stage1 is not full native acceptance.
- Existing schema/version and both registration/compatibility native children use
  disposable cwd/home/SQLite/log directories and local-only marker. Preserve exact
  binary, args, validation/readiness, TERM/wait and parent ENV/cwd. No copied user
  credentials/config or administrator-policy bypass. Source possibility is not
  proof of past live storage damage. This separate unit fixes preselection startup.

Owning runtime docs: workspace-portal.md for transition/compensation/bootstrap and
probe isolation; codex-package.md for naming prerequisite; retained
session-preparations.md for original naming contract. Lead applied the contextual
writing pass. Individual rollout facts remain in rollout.md. Consumers are
workspace-host -> selected dev-session -> portal root/team cold helpers -> codex-web;
configuration imports host module, workspace/extension composes the user package.
Current consumers are configuration62cbee/base530efc and workspace14afb/base051c8;
their future mechanical pins await final runtime publication and matched checking.
The deployed system62c/bbai includes old runtime12cf, while candidate14afb/5ah was
never selected. New runtime is substantive, not a patch-equivalent deployed
successor: new matched outputs/deployment verification are required before release.

Quick checks pass in Nix: actual published-pin Go transition/naming/member/HTTP
batch(.966/.164/.298/.322s), tagged compile only(.047s), strict selected-store CLI
(.128s), host47/349 plus startup/compensation7/55, CLI restoration3/15, native
preflight fake subprocess1/100(1.917s), pin/corpus/diff checks. No hook framework
is declared and no bypass used. Exact logs are listed in runtime-report.md.
Synthetic tests and retained native source evidence do not claim live rollout
acceptance. After review: one existing two-attribute host VM command, normal exact
final branch CI, matched final system/profile builds and staged live verification.
No added native/schema/provider/canary campaign or workflow dispatch.

Overall risk HIGH: persisted delivery records, service/process exclusion,
public commands, deployment ordering and mixed-native storage. Reviewer0 is
retained Sol/xhigh/read_only, thread01a179a3-a347-7753-b3df-3f3df5c02748; live
roster37 checked ready and independent. Cover all four affected lanes: general,
architecture/repetition, scope/proportionality and risk/compatibility, with explicit
whole-series and migration conclusions. Read mandatory-change-review and all four
lane references. Preserve accepted prior lanes where unchanged; inspect the new
behavior directly. No nested agents, live/private-state reads, tests/builds,
source/Git mutations, deployment or integration. Report concrete findings and
residual verification limits; do not treat the design as automatic acceptance.

## Client observer queue-read correction, ready for affected review

Requested outcome: an actually inactive native thread must not block compatible
package deployment solely because it retains unresolved delivery records. The
runtime needs a cold observer that verifies an empty native queue without loading
or mutating the thread. Its test exposed ObserverOnly denying the existing
read-only ListQueue operation. Scope is one allowlist entry and regression, not a
new client API, receipt reconciliation, schema, dependency or catalog change.
Runtime implementation remains uncommitted and is explicitly outside this client
review; it will receive a separate final affected review after exact pin generation.

- Repository: aither64/codex-web, target master, own worktree under this session.
- Complete base/head: 8b60554bc10c2a6bcbf9732a8b77ad959c317036 to
  255f0b4f74951ebbd0a5ab15eea7a3142be0ab93, clean tree
  593b8e0597d4a840ed490e1df393efb27c4b07da.
- Affected delta: previously accepted02533a152223416f159bac2578e88bcbe653f247
  to255f0b4f, codex/client.go plus codex/observer_test.go, +103/-1.
- Complete series:643898a4 safe native retries;ccd2ce58 prompted0.164;
  ab60a81b capacity classification;02533a15 state fixture;255f0b4f observer queue
  read. First four units retain previous acceptance. No obsolete approach,
  repeated dependency stream, migration or deployed client revision in this range.
  Exact025 ref preserved. Inspect the whole history/disposition independently.
- Quicks: Nix go test -mod=readonly ./codex -run '^TestObserver' -count=1
  -timeout=45s -v passes five tests/0.169s; request corpus --coverage-only passes;
  diff check passes. [Log](client-observer-queue-quick.log), [report](client-report.md).
- Expected permission: only thread/queue/list added to existing observer read
  allowlist. Pagination preserves IDs/order/text; incoming requests receive no
  answer/rejection; no implicit resume/settings writes; explicit mutations remain
  denied. Native source inspection proves this method reads unloaded nonarchived
  metadata/queue without resume; existing state06 reads a queue and asserts the
  thread stays unloaded. No fresh native execution is claimed.
- Consumers: runtime workspacecodex package-transition helper, currently tested
  with a disposable modfile override only. Final runtime flake+Go pins/checksum
  and vendorHash must consume reviewed published255; ordinary observer consumers
  gain this read permission. No automatic retry or original receipt changes.
- Docs: existing ObserverOnly read-only contract remains; runtime operational
  explanation lives in pending docs/workspace-portal.md and docs/codex-package.md.
  No separate client guide rewrite is useful for one existing read method.
- Risk high at the overall transition/observer boundary. Retained reviewer0,
  Sol/xhigh/read_only, thread01a179a3-a347-7753-b3df-3f3df5c02748 verified roster37.
  Apply general, architecture/repetition, scope/proportionality, risk/compatibility
  affected lanes. No fallback/model override; preserve earlier review results.
- Non-goals: no new API/storage format/framework, native/schema/browser campaign,
  force-idle, receipt acceptance/deletion/replay, private foreign reads, deployment
  or integration by reviewer. User's no-canary and forward-recovery limits remain.


Current follow-up: the user requested correction of deployment refusal caused by
hidden durable send attempts on an idle session. That runtime change is being
designed and has not received final review. The accepted 12cf upgrade and previous
exact ranges below remain historical evidence; their acceptance does not cover
the new package-transition behavior. The next affected review must cover writer
exclusion (including async resume/answers), preserved original attempts, native
activity checks, selected-predecessor deployment path and refusal compensation.
No client API/storage migration or expanded recovery framework is intended.
The final packet will bind committed corrected source and focused check results
before assigning reviewer0. System62c is already deployed; app14afb/5ah never
selected. Preserve that intermediate deployed lineage explicitly.

Current refresh packet is appended below; the original packet and exact ranges
remain historical evidence. Current deployment/integration authorization and
prerequisite acceptance are recorded in state.md.

All intended changes are committed and quick checks pass. User requests the
smallest deferred Codex0.164/client025/naming patch on current defaults, preserving
newer observer and already merged UI/capacity work. No integration, physical
activation or session lifecycle action is authorized. Review is independent and
read-only, with all four mandatory-change-review lanes.

## Scope and sources

Read [plan](plan.md), [architect design](design.md), [state](state.md),
[client evidence](client-report.md), [runtime report](runtime-report.md),
[configuration report](configuration-report.md)
and [standard checks](standard-verification-plan.md). Worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-codex-upgrade-naming/`.
Read each affected repository's AGENTS.md. Workspace procedure paths are under
`/home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/`.

The source session remains open and untouched. Its final focused UI release is
already merged; preserved ec93/ca8 refs supply only remaining units. No whole-tree
replay or old consumer lock is used. Current observer settings, interval, Check
now, evidence and resolution fields must survive unchanged.

| Repository | Base | Final head |
| --- | --- | --- |
| codex-web | 8b60554bc10c2a6bcbf9732a8b77ad959c317036 | 02533a152223416f159bac2578e88bcbe653f247 |
| dev-workspace | 7e6d7c9cdb3388ab7abc720c034c15c21afbd686 | 391d3a3d45f301a5e9afb6e1c72781598a7e0dd6 |
| vpsfree-cz-configuration | 880a6253f8d6cc1368e633f936b174792e86bff7 | 9155be82dcaf96740d4b324dfcd6b4245979e500 |
| workspace | 978a2f280185f3ae114c2db13130f13e6976b159 | 3751c6d76da6258157edc31b307eb0f944386942 |

Read the complete base-to-head series and final diff in each worktree. Client
series:643898a4 safe native retry proof,ccd2ce58 prompted0.164 API,ab60a81b exact
capacity classifier,02533a15 disposable state-upgrade fixture. Source801 naming
work is imported content, not a literal ancestor. Exact025 source/history is
preserved; native tests and prior independent review have scoped reuse evidence.

Runtime series:a45f73d33d3f9e18a70fd63986aeb79d6598c52e naming/dependency,
391d3a3d45f301a5e9afb6e1c72781598a7e0dd6 retirement cancellation. Naming unit
bundles the API adoption with matching native/client/module/vendor/catalog version
selection and its tests/docs because it must run with that supported pair.
Retirement cancellation is separately reviewable. Runtime total24 files,+792/-151.
Only the small private registry/environment fixture correction is taken fromca8;
its receipt/manifest/VM/real-canary framework and unrelated archive/creation
diagnostics are excluded. Already merged UI/capacity code is untouched.

Each consumer has one final runtime selection stream. No superseded dependency
pin commits are intended. No new migrations: existing SQLite schemas/readers,
creation/archive journals and observer schema1 remain. None of this session's
feature heads has been deployed or integrated; old refs and deployment records
are preserved. Independently conclude whole-branch history, repeated-stream
consolidation and migration lineage, including explicit no-migrations outcome.

Configuration9155be82 is one generated lock-only `inputs: set devWorkspace to
391d3a3d` commit. Normal confctl channel command and hooks passed; generated
message unchanged. Semantic diff changes runtime, client025, runtime llm-agentsea188
and its nested nixpkgsf20; root system llm-agentsea188 and every sibling/edge remain.

Workspace3751c6d76 is one two-file pin,16+/15-, on current shared tracking
master978a2f280. Published feature3751/defaultc00fa4b3b confirmed over SSH. Its
four changed nodes match configuration, all other nodes/edges and extension767
preserved. Existing bin/check-dev-workspace-deployment passed against final
workspace3751/config9155/runtime391d3a3d. No hook framework declared. Both consumer
worktrees are clean; no substantive consumer behavior change or new project docs.

## Contracts, risk and non-goals

Risk is high: public protocol/client support, native persistent-state upgrade,
cross-project packaging, cancellation/recovery and eventual activation ordering.
Apply general, architecture/repetition, scope/proportionality and risk/compatibility
lanes from /home/aither/.codex/skills/mandatory-change-review/SKILL.md.
Retained reviewer0 is independent Sol/xhigh/read_only, live roster37; no fallback.

codex-web owns public strict0.163 `RunEphemeralTurn` and prompted0.164
`RunPromptedEphemeralTurn`. Runtime's session namer is the prompted consumer.
Naming uses Luna/low, bounded raw request/prompt/JSON, a30-second operation budget,
two slots, native retry ownership and at most one proven safe fresh attempt.
Failures pause before reservation and retain manual recovery. Prompt restrictions
do not guarantee tool isolation; preserve that explicit support boundary.

Native launch/group/service ownership is unchanged except accepted0.164 version.
Keep packaging helper and raw native hashd2af1cd0... from llm-agentsea188d2.
System configuration selects the matching runtime helper and its already0.164
system input. Workspace owns application profile selection separately. No unrelated
graph/policy/catalog update is intended. Future activation requires idle native
transition, system before application and forward recovery; cold old-reader
success does not establish safe downgrade or mixed writers.

The user explicitly rejects real naming canary/account gates and credential
search/copy. The two owning-guide paragraphs describe real canary as optional,
separately authorized validation and report synthetic coverage honestly. No policy
framework or client-only documentation commit. The lead directly applied the
user-facing writing skill to runtime's three existing guides.

## Verification

Client unchanged025 automatic Check40385717557 passed83s. Prior exact native
results are documented in client-report: scoped00–05 reuse, actual025 stage06
upgrade/restart/fork/receipts/queue/messages/offline old-reader cold-read PASS.
Raw artifacts later became unavailable; surviving Markdown and lead's first-hand
tool transcript are attributed, not represented as new runs or restored receipts.

Runtime focused startup/naming/preparation/observer/retirement tests passed,
including recovery/cancellation/collection exclusion. Tagged managed fixture
compiled without execution. Pin/protocol coverage, syntax/format/whitespace passed.
Ruby reservation7 runs/28 assertions and live-switch6 runs/93 assertions passed.
Incidental test-command errors (missing time binary, ambient runtime flag, direct
Ruby shard without aggregate loader) were corrected without product changes;
successful checks were retained. Final runtime report supplies command/log detail.

Automatic final-runtime Check40387489791 started at391d3a3d. It runs the existing
package/fast, session-creation and session-archive-lifecycle jobs; host skips on
feature branches. No final success is yet claimed. Long local final consumer
builds wait for this review. No bespoke managed-naming VM/native-retirement or
extra browser campaign; no real inference. Acceptance ends at final required
CI plus ordinary composed-profile/system outputs, pending explicit approvals.

The profile build batch also runs one ordinary final `goModules --rebuild`.
The vendor generator consumes current source/test imports, so unchanged module
pins alone cannot transfer the old ec93/jmj vendor proof to the newer observer
composition. Record only the normal derivation/output/result; no broad rebuild,
hash-discovery round or source inventory is needed. Architect's design records
this boundary and owner2 owns that step.


## Combined prerequisite refresh, 2026-10-27

All three user-named initiatives have merged their work; owner3 recorded exact
remote evidence and the user confirmed archive's complete scope. User authorizes
this initiative's deploy, verify, then four-repository master integration. This
review authorizes no physical action; application activation still needs the
supported external-shell idle handoff. No lifecycle action is authorized.

Review the complete refreshed runtime range
fffbd0d59fffc09667cb39878d9f7da8bdcd3806..12cf85e091b915f7d43f588c2d4f312173c60715
against the retained reviewed old range
7e6d7c9cdb3388ab7abc720c034c15c21afbd686..096062879a74b24204e8162620c3f98b8e05bc62.
Local source is committed and clean, awaiting affected review before push.
The final diff is26files +807/-157. Four units remain:
1b6b2e0e naming/dependencies,56908082 retirement cancellation,f7738a10 archive
setup ordering,12cf85e0 creation receipt assertion ordering. No repeated pin
stream, obsolete unit or new migration is reported. None of our candidates has
been deployed. Client025 remains exact, clean/published, default8b605 unchanged;
its independent review and CI remain applicable. Consumer pin replacements are
mechanical and will follow accepted runtime publication.

The actual conflict was nix/tests/session-archive-lifecycle.nix. Resolution
retains upstream --user-state-root on require-idle and our existing native idle,
persisted retry-policy and bounded shared-flock barriers before registration.
All three other commits compare equal in runtime-quick/refresh-range-diff.txt.
Do not call the entire range literally patch-identical: context changed for the
fixture. Review the surrounding new archive-permission and readonly-cache tests,
CPU retry-idle/cache and shutdown changes, and title-notification baseline for
preservation and interactions with our existing client/naming/cancellation code.
Architect's current amendment in design.md scopes these boundaries. Upstream
production CPU/title/permission files are reported byte-identical to default.

Quick checks passed: main0.726s,workspacecodex0.064s,web38.057s (naming,
preparation/admission/receipt/progress plus settled-retry/cache regressions),
Ruby archive permissions7tests/146assertions,Node75tests, pin checks and
Nix/embedded Python syntax. Logs are runtime-quick/refresh-main-retirement.log,
refresh-web.log and refresh-ruby-browser-contract.log. No long local builds,
VMs, native replay or new CI has been launched.

Risk remains high due to existing protocol/state and deployment boundaries.
Use retained reviewer0 Sol/xhigh/read_only for affected general,
architecture/repetition and risk/compatibility lanes. Original scope/proportionality
conclusion remains unless the actual refreshed patch reveals new scope. Inspect
complete history/consolidation/migration lineage explicitly. Preserve exact old
review and evidence; do not create a certificate framework. Architect supports
reusing actual1a vendor proof because incoming imports are stdlib/local/already
used client packages and vendoring hooks/module/build selection are unchanged;
assess that bounded rationale, never relabel old execution as a new run.
