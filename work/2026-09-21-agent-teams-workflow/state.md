---
lifecycle: active
---

# 2026-09-21-agent-teams-workflow

## Status

The direct-thread team transport is implemented and deployed on aitherdev.
A portal feedback follow-up is committed and pinned through the workspace
feature worktree but is not yet deployed: it adds counted preset labels, a live CLI command preview, stable
Add member/model selectors, collapsed removed members, timestamped member
messages, and full Codex conversations for ready members. It awaits downstream
one consolidated review rerun, packaged verification, and aitherdev switch.
The currently active package is
`/nix/store/wxh93a4fmmmp94dd6g11z0n6nfmvyppk-dev-workspace-0.2.0`.
Both read-only `architect2` and workspace-write `implementer1` delivered
reports through the installed `report_to_lead` tool to their own session's
lead; removed-member and wrong-session bindings were rejected. The final
Sol/xhigh review is resolved, the full packaged check and pinned Codex MCP
contract pass, and the portal is available at
`https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-21-agent-teams-workflow/`.
All retained roles default to GPT-6 Sol; only operation-scoped monitoring
uses GPT-6 Luna/low. The initiative stays `active` for user UI feedback and
later feature-branch integration. No session was archived or deleted.

Current feature heads: codex-web `d542e767310d`, generic dev-workspace
`c0217744b2c9`, vpsFree extension `0331b17bb2b3`, workspace configuration
`964fd340f8d5`. The first three are published over SSH; the workspace pin
remains local, pending review and deployment. None is integrated into master.

## Rollout log

Final portal feedback review (2026-09-23 local): the retained independent
reviewer reran General, Architecture, Scope and Risk at GPT-6 Sol/xhigh against
codex-web `d542e767`, generic `58fa8d5`, extension `160a868` and workspace
`a9767ac`. All first-review findings were resolved. Its sole new Important
General finding was the plan-to-new-session dialog's preset label missing the
total team size. Generic `c021774` changes that one label to match the main
creation form and adds a focused template test; the test passes. This direct
presentation fix adds no design or accepted boundary, so the mandatory review
procedure does not call for a reviewer rerun. Extension `0331b17` and
workspace `964fd34` pin that final generic head; both no-build flake checks
pass. Packaged and live checks remain pending.

Portal feedback review-remediation checkpoint (2026-09-23 local): the first
consolidated Sol/xhigh review (General, Architecture, Scope, Risk;
`review-portal-feedback-packet.md`, catalog digest `bc7e3a3c`) found three
Blocking issues and two lower-severity issues. The new codex-web head
`d542e767` persists nonempty turn options with the attempt and recovers them
for retry after a member setting change; old zero-option attempts retain their
wire form and old nonzero attempts without snapshots fail closed. The generic
series is now three focused commits: `e473547` (creation labels and CLI preview),
`55b44f6` (Team-tab refresh, saved effort, message presentation), and
`58fa8d5` (ready-member transcript/send and wrapper capability forwarding).
Its downstream extension and workspace pins are `160a868` and `a9767ac`.
Focused codex-web retry/queue tests, generic teamruntime/web tests and
JavaScript syntax, extension and workspace no-build flake checks, and diff
whitespace checks pass. The generic Go suite completed in 35.3 seconds.
The revised review packet calls for all four Sol/xhigh lanes to rerun on these
exact heads. Long packaged checks and the aitherdev switch are still pending.
No unrelated test session, cluster, or shared configuration master changed.

Portal feedback follow-up (2026-09-23 local): codex-web `bd8cb096f110`
rebinds the per-member policy before queued turns and is published on its
feature branch. Generic `ecddc8e` adds full member conversations and the
requested portal controls, pins that client, and has the new Go vendoring
hash. Focused codex-web queue and generic teamruntime/web suites pass; browser
JavaScript syntax and the CLI preview helper pass. A direct browser-suite
invocation lacks its required server URL and Playwright dependency, so the
packaged browser check remains for post-review verification. The next action
is to publish the generic branch, update extension and workspace pins, run one
consolidated review, then perform Luna-watched packaged checks and deployment.

The earlier entries below are chronological checkpoints; statements about work still
pending describe their point in time, not the current status above.

Initial transport checkpoint (2026-09-23 local): the final communication
path is now committed but not yet deployed. Generic runtime commit
`1529d96ddbc9` binds the one-member MCP policy on every assignment;
`81417a4` adds the package-owned `report_to_lead` helper and a host-locked
lead-root check. The helper verifies the exact ready roster member and thread
and passes report text through stdin across both CLI hops, never in process
arguments. Codex-web `2a228e70de42` reapplies the tool configuration on
member resume, including the internal pre-send resume. Focused Go, Ruby, and
protocol checks pass. Generic `04bb52a1f901` pins that client and the fresh
Go vendor hash `sha256-9OBydqLWyJUNin2ubEKRmKd669SSzwOGHWStdQi6Wqw=`;
its focused portal and runtime Go suites and no-build flake check pass. The
generic feature head is published over SSH. The final consolidated
Sol/xhigh review, Luna-watched package checks, and live member-to-lead
acceptance still outstanding. All retained team roles are GPT-6 Sol; the
operation-scoped watcher remains GPT-6 Luna/low. The stable session URL is
`https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-21-agent-teams-workflow/`.

Pinning checkpoint: vpsFree extension `08f576a8e8c4` is committed and
published over SSH, pointing at generic `04bb52a1f901`. Workspace
configuration `7db87792ccbb` pins the extension locally; its lock resolves
generic `04bb52a1f901` and codex-web `2a228e70de42`. Both no-build flake
checks pass, and both development-cluster providers remain in the extension.
All four project worktrees are clean at their intended heads. Review and
post-review acceptance are next; no new package is deployed yet.
The retained independent reviewer thread
`01a0cb4d-69fe-7bc3-a722-6ea267aa29b9` (catalog digest `bc7e3a3c`)
started the consolidated High-risk General/Architecture/Scope/Risk review at
GPT-6 Sol/xhigh in read-only mode against `review-transport-packet.md`.
Its verified runtime identity, model, effort and sandbox matched the packet.
The review completed with no Blocking finding, one Important forward-retry
gap across a package switch, and one Advisory shared-client guide issue
(`review-transport-result.md`). The Important gap is explicitly accepted for
this sole forward-only development host, with transcript inspection required
before any new-ID resend after an old uncertain assignment. The package
switch quiesces sessions; the user permits restarting idle sessions. Generic
documentation commit `b7883bee18fb` records the operator action. Codex-web
documentation commit `86aaa2e39062` corrects the fork binding rule. Both are
published over SSH; the downstream package pins intentionally stay on the
reviewed code heads `04bb52a` and `2a228e7`, since these later changes are
documentation-only. The reviewer need not rerun for those narrow corrections.
A fresh GPT-6 Luna/low watcher ran the opt-in pinned Codex 0.155.1
two-turn MCP contract on codex-web `86aaa2e39062`; the first-run log is
at `logs/pinned-mcp-contract-86aaa2e.log`. The full packaged check and live
aitherdev switch still await that result.
The first opt-in run failed before any model turn: its test supplied nil for
`shell_environment_policy.set`, and pinned Codex 0.155.1 requires a map.
Production teamruntime always creates a non-nil member environment. Test-only
codex-web `f699c58bcdcc` passes an empty map on start and resume; its quick
compile/server check passes. The failure log is
`logs/pinned-mcp-contract-86aaa2e.log`. A fresh Luna/low watcher will rerun
the contract at `f699c58`; no package pin changes are needed for this test
fixture correction.
The first `f699c58` rerun was not launched because its watcher assumed
`/usr/bin/time`; its log records wrapper exit 127. A fresh watcher ran the
exact test and exposed a second fixture issue: the host MCP test process did
not receive the probe's inherited environment, so it closed during the
required handshake (`logs/pinned-mcp-contract-f699c58-r2.log`). Test-only
codex-web `aba4f7315613` now passes probe identity through a test-binary
argument and private sentinel, matching the production helper's argument
binding pattern. Its quick compile/server check passed. A fresh Luna/low
watcher is running the opt-in contract at `aba4f73` while the workspace
packaged check continues. No downstream package code pin changed.
The full `nix flake check -L --show-trace` at workspace `7db87792ccbb`
passed under a fresh GPT-6 Luna/low watcher in about 3m36s
(`logs/final-packaged-check-7db8779.log`); it reported `all checks passed!`
and no unexpected kernel build. The `aba4f73` opt-in run reached a model
turn but its fixture treated a briefly empty post-send history as completed
(`logs/pinned-mcp-contract-aba4f73.log`). Test-only codex-web
`ef4cd581b1c0` waits for the returned turn ID to appear and finish before
declaring a missing MCP call. A fresh Luna/low watcher is running that
contract. Package behavior and downstream pins remain unchanged.
The opt-in two-turn pinned Codex 0.155.1 MCP contract passed at codex-web
`ef4cd581b1c0` under a fresh Luna/low watcher in about 15 seconds
(`logs/pinned-mcp-contract-ef4cd58.log`), proving host tool use before and
after reconnect/resume. The aitherdev profile switch from workspace
`7db87792ccbb` then succeeded to
`/nix/store/wxh93a4fmmmp94dd6g11z0n6nfmvyppk-dev-workspace-0.2.0`.
The profile reports Codex 0.155.0-compatible protocol, `dev-session validate`
passes 55 manifests, portal/router units are active, local portal GET `/`
returns 200, and the installed extension catalog contains both `vpsadmin`
and `vpsadminos` cluster providers. Existing sessions were quiesced and
terminal clients restarted; warnings concerned pre-existing unproven
worktrees outside this initiative, not a transition failure. On the test
session `2026-09-22-team-test-2`, installed CLI accepted assignments for
ready `architect2` and `implementer1` at Luna/low one-turn overrides; their
retained default settings remain Sol/xhigh. A fresh Luna/low watcher is
observing exact member-to-lead report markers. The stable session URL remains
`https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-21-agent-teams-workflow/`.
Live transport acceptance passed. The architect's assigned turn
`01a0cbea-d06d-7792-8eb7-508cc574fb90` and implementer's assigned turn
`01a0cbea-f83c-78b1-b105-2401ab828a03` each called the installed
`report_to_lead` MCP tool and received `Report sent to lead.` The test lead's
transcript contains the exact `architect2 bound report smoke 1102` and
`implementer1 bound report smoke 1202` user messages plus lead receipt
messages; both member turns completed. The Luna/low watcher observed these
without submitting or retrying messages. Direct installed-helper negative
checks for removed `architect1` and an `architect2` binding pointed at the
wrong session both returned `isError: true` before delivery; neither
negative marker appeared in the test lead transcript. The local portal index
returns 200, and its new-session form contains human-readable Full team and
Lead-designed team labels with concrete GPT-6 Sol values. The permanent
behavior and recovery notes are in generic `docs/workspace-portal.md` and
codex-web `docs/reference.md`; rollout evidence stays in this initiative.

The implementation is deployed and ready for user portal feedback, but the
initiative remains `active`: the exact feature heads have not been rebased,
captured, and merged into their remote default branches. Do not archive or
delete the initiative. The next operator action is to inspect the Team tab
and new-session controls at the stable URL, report any UI changes desired,
then coordinate branch integration after feedback. The test session
`2026-09-22-team-test-2` remains active with its two ready members; no
cleanup of it was authorized in this turn.

Communication follow-up (2026-09-23 local): the live `architect2` and
`implementer1` assignments reached independent member threads, but neither
member sandbox can use `dev-session team assign` because it cannot open the
host transition lock; the read-only member also cannot connect to the shared
portal socket. A direct member-bound stdio MCP tool is the chosen correction,
not a broader shell sandbox or a shared socket grant. A temporary pinned
Codex 0.155.1 binary probe (`logs/mcp-probe-r4.log`) proved that a read-only
member discovered and successfully called a host-side tool when its single
report action was explicitly approved. The same thread lost that tool after
reconnect/resume without `config.mcp_servers`; the second turn's final answer
said the tool was unavailable. A member's first assignment and every later
pre-send resume must bind the exact member tool; start/fork cannot bind it
until the new thread ID exists. The first
probe lacked the existing headless bootstrap (`logs/mcp-probe.log`); the next
used a default approval mode that required an impossible interactive approval
(`logs/mcp-probe-r3.log`). These are probe setup results, not product
acceptance. Retained Sol implementation agents own the client policy, the
package-owned helper, and runtime binding. The codex-web policy and opt-in
pinned-binary contract are committed and published at `2a228e70de42`;
quick Go and protocol coverage checks passed. The generic runtime binding and
operator documentation are committed at `1529d96ddbc9`, with its focused Go
suite passing against the new client API. The host helper and exact-root CLI
guard remain in progress. No transport correction is deployed yet.

Current follow-up checkpoint (2026-09-23 local): pinned-binary verification
confirmed that a fresh Codex 0.155 thread omits project identity until its
first rollout, `thread/list` omits no-turn threads, and an acknowledged
`thread/delete` leaves `thread/read` reporting `thread not loaded`. The client
now materializes and verifies the exact project before member readiness; the
generic runtime no longer mistakes an empty project listing for confirmed
retirement. A lost deletion response still requires exact not-found proof,
otherwise the roster remains pending. The no-model pinned-binary contract
covers create/bootstrap/reconnect/fork/fresh delete and passes. This is a
forward-only aitherdev cutover, not a schema migration or coordinated node
update. The owning explanation is in generic `docs/workspace-portal.md`;
this binary-specific evidence is retained in this rollout record and tests.

The committed current heads are codex-web `0f59be164036`, generic
`98fc2b2c99fc`, vpsFree extension `a24bbee2bc84`, and workspace
`100eca5b2760`. The first three are published over SSH; the workspace head
is local. Codex `go test ./codex` and its pinned-binary contract pass.
Generic teamruntime/agentteams/web/CLI Go tests pass, and generic, extension
and workspace `nix flake check --no-build --show-trace` pass. A fresh Luna/low
watcher obtained the exact generic Go vendor hash
`sha256-F6ZN8CczBN8FdVQig7poppGz/MRCI8ZGH8iZYJfCIdA=` from the
expected fake-hash build (`logs/final-vendor-hash-0f59.log`); it is pinned in
generic `98fc2b2`. Codex-web CI at current head passed (35801027999);
generic CI 35801230254 and extension CI 35801288391 also passed at exact
heads under a fresh Luna/low watcher (`logs/final-ci-98fc-a24b.log`). The
retained independent GPT-6 Sol/xhigh reviewer completed the required narrow
four-lane High-risk follow-up on the committed binary fixes
(`review-pinned-binary-result.md`): no Blocking or Important findings, one
Advisory. Its public `IsThreadNotFound` helper can classify a raw -32001
error for a different ID, but the current runtime receives the ID-bound
`ReadThreadMetadata` wrapper, so the current retirement path is correct. We
accept this non-blocking API-hardening follow-up for later rather than repin
four projects and rebuild for an unexploited call path; no broad reviewer
rerun is warranted. The earlier broad four-lane review found no findings.
The deployed
aitherdev profile was switched after a Luna/low-watched full packaged check
passed at workspace `100eca5b` in about three minutes
(`logs/final-packaged-check-100eca.log`). The active package is
`/nix/store/fbxbng2h8ffdsvz7avkm990d9z8yc9rh-dev-workspace-0.2.0`;
`dev-session validate` checked 55 manifests, portal/router services are
active, and local portal socket requests for the index and two session pages
return 200. Public HTTPS correctly challenges unauthenticated probes with
401 (the host uses an internal CA, so default curl trust fails before `-k`).
Browser-authenticated feedback and final branch integration remain. The
stable session URL is
`https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-21-agent-teams-workflow/`.

Live acceptance is incomplete: `dev-session team add` created ready Sol/xhigh
`architect2` and `implementer1` in the existing `2026-09-22-team-test-2`
session, and assignments reached both member threads. The portal showed
their transcripts and team controls, with the new-session page showing
human-readable presets and concrete Sol role defaults. However neither
member could report back through the instructed CLI. Both read-only and
workspace-write Codex shell sandboxes reject opening the shared
`/home/aither/.local/state/dev-workspaces/transition.lock` with EROFS;
`DEV_SESSION_SLUG` was also absent from their shell environment. The
architect's sandbox could not connect to the portal Unix socket either.
The members' final answers remain visible in their portal transcripts, but
there is no working member-to-lead delivery yet. The failed smoke-test
messages are not considered delivered; do not retry them under a new ID as
if they were confirmed. A focused communication-transport correction is
required before completion. The two test members are idle and retained for
follow-up; no unrelated session records were edited manually.

Latest checkpoint (2026-09-23 local): the headless-rollout correction is
committed at codex-web `aee1a8d5d2f8`, generic runtime `462c55e77bad`,
vpsFree extension `59d47baf4888`, and workspace `cad7349ce3a3`.
Codex-web, generic and extension heads are published; the workspace feature
head remains local. The previous project-registration profile is still live,
not this new fix. At that previous deployment, focused client/runtime tests,
portal compilation, pinned protocol shapes, all three repository CI runs,
and a Luna/low-watched packaged `nix flake check` passed; the latter took
221 seconds and is logged at `logs/final-project-flake.log`. An independent
GPT-6 Sol/xhigh narrow follow-up of all four commit ranges found no findings
(`review-project-registration-result.md`). The aitherdev profile currently uses
`/nix/store/bdcyyrg6bm8rsbf36di39sqjlaqpf341-dev-workspace-0.2.0`;
`dev-session validate` checked 56 manifests and local index/test-session
portal requests return HTTP 200.

The first package switch refused the existing `team-test-2` roster because
its failed `architect0` reservation lacked a confirmed idle thread. A
read-only `project/read` against the installed 0.155 App Server proved that
exact synthetic project was missing (`-32602`, exact `project not found:
<id>`), consistent with the pre-allocation `thread/start` failure. Under
the roster operation and file locks, the lead copied the original private
roster to `2026-09-22-team-test-2.json.pre-project-reconcile-20260923`, then
cleared only that proved-failed `createAttempted` flag. The installed
`dev-session team remove` command retired the three unstarted test members,
preserving their addresses. The second normal switch passed its idle check;
no unrelated session records were changed.

Live `dev-session team add` then created `architect1` with a registered UUID
project and a ready thread. The first assignment, message ID
`c6f2dd9e-80cc-47a5-aa2b-bfd0e27b9b47`, failed before confirmed delivery:
App Server reported `no rollout found` when the send path resumed the fresh
headless thread. A read-only team idle check also failed for this unused
thread with `missing source rollout`. Further read-only checks showed the
exact thread is `notLoaded`, with zero turns, zero queued submissions, and no
rollout file. Under both roster locks, the lead backed up the private roster
to `2026-09-22-team-test-2.json.pre-unmaterialized-retire-20260923` and
retired only this unusable test member at roster revision 12. The normal
`team require-idle` check now passes; the empty metadata-only Codex thread
remains outside the active roster. The committed fix uses create-time
`thread/inject_items`, which persists a developer initialization item without
a model turn, plus exact-marker and guarded unused-member lifecycle recovery.
It is not yet deployed. Do not retry the failed assignment with a new ID.
Browser-authenticated conversation access and full live team behavior remain
open.

The headless fix and exact downstream pins are committed at the four heads
above. Focused codex-web tests and generic teamruntime/agentteams/web/CLI Go
tests passed; Go formatting and diff checks passed. Generic, extension and
workspace `nix flake check --no-build --show-trace` passed. The generic
package build first rejected the stale vendored revision, then a fresh
Luna/low watcher obtained the exact new vendor hash; it is pinned in the
generic commit. The full package build, opt-in pinned-binary no-model
start/inject/disconnect/fork contract, CI, deployment and live first-assignment
acceptance remain next, after the focused Sol/xhigh change review. The first
CI runs at codex-web `aee1a8d` (35798208375), generic `462c55e` (35798586156)
and extension `59d47ba` (35798669315) all failed the same protocol-corpus
coverage check: the new `thread/inject_items`/`thread/delete` call sites and
an additional `thread/read` were not represented, and the static call regex
does not accept underscores. The failed logs were inspected before any rerun;
the downstream failures cascade from the codex-web source check. A focused
corpus correction passed local coverage-only and pinned-schema validation, and
is committed in codex-web `7cbb426a4dd4`. The retained independent Sol/xhigh
review of the preceding four committed implementation heads found no Blocking,
Important or Advisory findings (`review-headless-result.md`). It confirmed the
bootstrap method against pinned Codex source but left the opt-in binary test
and live assignment as verification gaps. The test-only corpus fix does not
alter that reviewed behavior; no broad rerun is warranted by the review
workflow. The current review packet is `review-packet.md`. Site defaults remain GPT-6 Sol for
retained roles and GPT-6 Luna/low for watchers; Terra is not active.

The independent review used a separate read-only Codex CLI thread because
native collaboration spawning and retained-reviewer follow-up both refused
with the agent thread limit. The reviewer identity was
`01a0cb4d-69fe-7bc3-a722-6ea267aa29b9`, model GPT-6 Sol, effort xhigh;
the packet is `review-packet.md`. The monitoring utility likewise uses a
fresh one-operation Codex CLI thread at GPT-6 Luna/low because the native
watcher spawn was unavailable. This fallback changes neither role policy nor
the review outcome.

## Earlier checkpoints

Final implementation checkpoint (2026-09-22): all intended direct-team code,
site composition and policy changes are committed in clean feature worktrees
and published over SSH. The feature heads are codex-web `1635ea2b2348`,
generic dev-workspace `59c4ba30fd49`, vpsFree extension `e36a0dd0f7b6`, and
workspace `bd67be5ff2ac`. The earlier virtual-team implementation and its
branch-only compatibility surface were removed; each downstream consumer has
one final dependency pin. The exact final heads and acceptance contract are
in `review-packet.md`. The first consolidated Sol/xhigh review's blocking
findings were addressed in these commits. The retained reviewer completed a
full-lane final-tree review at earlier generic head `8781448` and reported
two Blocking and five Important findings: idle-member lifecycle transitions,
deleted roster retention, assignment/roster races, browser retry identity
loss after reload, fork member addressing, incomplete-source fork effects,
and obsolete virtual resolver CLI. Generic `7310b52` addressed all seven. A
Sol/xhigh risk follow-up found two remaining Important issues: browser
assignments could proceed without durable retry storage, and forced deletion
could stop at an active team member. Generic `b4ef59e` fails closed on storage
errors and adds bounded, identity-checked member retirement. The retained
reviewer confirmed those fixes but found one remaining Important retry gap:
App Server rejects a second `thread/archive` if the first archive succeeded
but the roster update was lost. Generic `59c4ba3` reconciles the exact
archived thread ID and session directory and persists the roster on retry.
The retained Sol/xhigh reviewer found no remaining Blocking, Important or
Advisory issue in the final risk rerun. A fresh Luna/low watcher is running the
packaged flake check before deployment.
The reviewer identity is
retained at catalog digest
`bc7e3a3c`, model GPT-6 Sol, effort xhigh.

Quick verification at the final heads passed: codex-web client tests; generic
`GOFLAGS=-mod=mod go test ./internal/teamruntime ./internal/agentteams
./internal/web ./cmd/workspace-portal` under the portal Nix shell; Ruby
`test/dev_session/agent_team_creation_test.rb` (8 runs, 49 assertions) and
`test/workspace_host/agent_team_registration_test.rb` (19 runs, 91 assertions);
browser JavaScript syntax; `git diff --check`; extension and workspace
`nix flake check --no-build --show-trace`. The generic Git pagination fixture
now disables background maintenance and passed twice. Generic CI at `e3fa01f`
failed the `generic-source` check because generic documentation named the
vpsFree site; it was made site-neutral. CI at `8781448` found a Go vendor-hash
mismatch, fixed in `b257024`; CI at that head then exposed an obsolete
`require_unmanaged_agent_team!` auto-archive call. It was removed in
`7310b52`, and the focused automatic-archive subset passed (12 runs, 263
assertions). Generic CI at `7310b52` and extension CI at `ed80c2c` passed.
Focused Go teamruntime/agentteams/web/CLI packages, browser syntax, three
direct-team lifecycle Ruby tests (15 assertions), and flake evaluations passed
at final pins. Generic and extension final-head CI plus the packaged flake
check passed. The new profile is installed, but
team creation failed its first live member start as detailed below. Existing
root conversations are preserved; browser-authenticated acceptance remains
necessary for the previous "Conversation access denied" symptom.

The older checkpoints below document the path to this final design, not the
current package state.

Deployment checkpoint (2026-09-23 local): the final packaged flake check passed
at workspace `bd67be5` under a fresh GPT-6 Luna/low watcher; its full log is
`logs/final-flake.log`. Generic final-head CI passed. The aitherdev user
profile switched successfully to
`/nix/store/jf6jdq41rqn9gym0cfphj0vzkqkmixvb-dev-workspace-0.2.0`;
router and portal are active, and `dev-session validate` checked 56 manifests.
The new-session page exposes the Sol presets and concrete lead settings; the
vpsAdmin and vpsAdminOS cluster commands are installed. Local router requests
for the existing `2026-09-22-team-test-2` root thread, Team, and activity APIs
return HTTP 200. Applying the Full team preset in that session then failed on
the first `architect0` start: App Server reports `project not found` for the
deterministic member project ID. Its roster correctly retains an attempted
`creating` member with no thread ID and must not be blindly retried. The
member-start contract is under investigation; this deployed profile is not
yet accepted for creating teams.
The corrective implementation uses App Server `project/create` with the
existing session-and-address hash as an idempotency key and stores the returned
UUID in the roster before `thread/start`. Focused client and runtime tests plus
the pinned 0.155 protocol corpus pass in the feature worktrees. The installed
profile's old direct-team validator cannot read a new UUID roster after a
member starts, so rollback to that generation would require manual roster
repair; the user explicitly chose a forward-only cutover on this sole host.

Current checkpoint (2026-09-22): the consolidated Sol/xhigh review found
blocking gaps in schema-3 creation proof, per-member instruction/sandbox
policy, ambiguous member start retries, retained virtual dispatch, and
repeated package pins. Focused fixes are in progress across the generic
runtime and a new codex-web client head `1635ea2b2348`, which is published
and pinned in the generic feature worktree. The team runtime is adding
session-local project identity and fail-closed retry reconciliation; the
portal and CLI now carry stable assignment retry IDs. The retired virtual
dispatcher and its UI are being removed under the forward-only cutover.
Generic documentation and role controls are being reconciled to the final
design. These uncommitted fixes are not yet deployed or reviewed. Do not use
new team creation on the currently deployed profile until the corrected
schema-3 proof and member policy are installed.

The prior virtual managed-team implementation reached a deployed feedback
candidate but failed its intended portal interaction: the user receives
"Conversation access denied" and the controls do not represent real agents.
The user has explicitly replaced that design. Its old immutable catalog,
virtual member ledger, selection transitions, and managed dispatch are now
superseded work, not a foundation to extend.

The replacement retains the root App Server conversation and the existing tmux
session per initiative. It creates independent persistent member threads and
uses direct correlated App Server turns as the team transport. `lead` remains
the attached terminal conversation; specialist members use compact stable
addresses such as `architect0` and are headless until assigned work.

The earlier direct-runtime slice was committed on
`2026-09-21-agent-teams-workflow` in the `dev-workspace` feature worktree at
`269799d` (`teams: preserve roster and lifecycle invariants`), following
`f597c1d` (`teams: use independent Codex member threads`). It supplied the
direct roster, portal Team tab, terminal commands, roster-address-only member
transcript reader, and root lifecycle synchronization. The legacy managed
access gate was disabled so old virtual state no longer denied a root
conversation. Its creation-time selection gap is being closed below.

Quick verification passed under a fresh Luna/low watcher:

- `nix develop -c bash -lc 'cd portal && GOFLAGS=-mod=mod go test
  ./internal/teamruntime ./internal/web && node --check internal/web/static/app.js
  && cd .. && ruby test/dev_session_test.rb'`
- Go packages and browser syntax passed; Ruby result: 332 runs, 3694
  assertions, 0 failures, 0 errors, 0 skips.

The repository's normal vendored Go invocation remains blocked before
compilation by an existing vendor metadata mismatch with `portal/go.mod`;
focused verification deliberately uses Go module mode. The consolidated
Sol/xhigh review covered general, architecture, scope, and
risk/compatibility lanes. It found and the lead corrected: lost roster data in
the automatic Team refresh; removed members being revived or forked as active;
team mutations racing lifecycle transitions; report sender attribution; preset
reapplication adding duplicate members; public retention of the retired
selection flags; and inaccurate busy-member documentation. The fixes stay
within the reviewed direct-thread contract. Post-fix focused verification passed
with the same zero-failure result. Packaged `nix flake check --print-build-logs`
also passed under a fresh Luna/low watcher; the complete log is
`logs/direct-team-flake-retry.log`. VM boot logs were expected and no unexpected
local kernel build occurred. The aitherdev user profile was switched from this
exact worktree successfully. The switch initially refused two stopped stale
vpsAdmin development clusters, so their exact disposable states were reset:
`2026-08-18-vpsadmin-password-reset` and
`2026-09-09-ip-release-mechanism`. The new router and portal service are
active; `dev-session validate` validated 55 manifests and the stable portal URL
returns its expected Basic Auth challenge. No configuration pin change is
planned.

The first deployed profile start exposed the deployment error: the generic
package has no `vpsadmin` or `vpsadminos` providers, so the portal rejected the
workspace declaration and crash-looped. Emptying the provider list in the
shared root made the portal serve again, but removed cluster capability and
also left the extension-owned writing, review, and handoff skills unavailable.
This is a temporary, uncommitted repair, not an accepted final configuration.
The correct package is the vpsFree extension wrapper around the feature generic
runtime. Its provider and skill catalog must be restored through the package
chain before final UI writing or review.

User feedback on 2026-09-22 established that the implementation is incomplete:
new-session team selection is explicitly rejected by `resolveManagedCreation`,
the Add member form is rendered in both test sessions but has not been proven
operational through a live mutation, and creation's blank model/effort fields
resolve to the live catalog default (GPT-6-Astra/medium). The requested outcome
is explicit site settings with no hidden default, a real team selected before
the first lead turn, editable members, and restored clusters. The revised plan
records four remaining phases rather than treating the earlier deployment as
completion.

The generic runtime now has creation-time direct teams committed on the
initiative branch: `cabd41b` adds schema-3 creation receipts, an immutable
catalog snapshot, root-plus-member initialization before the lead's first
request, CLI `start --team` and catalog-backed `team preset`, with retry tests;
`0344cd9` adds portal team choices, visible concrete lead settings, roster
retry/configuration controls and direct-team documentation; `5976ea0` aligns
examples and projection fixtures with the revised GPT-6 Sol policy, and
`1c3580b` names the GPT-6 Luna watcher in the guides; `0b31336`
requires a live-validated model/effort pair for CLI member add/configure. Quick
Ruby syntax and focused tests passed (17 runs, 191 assertions); a fresh
watcher passed the Go web, teamruntime and CLI packages, and focused
portal/runtime tests and browser JavaScript syntax passed after the UI commit.
Full integration and live acceptance are still outstanding.

`224ee32` makes CLI `team list` resolve the same installed site catalog as
portal creation instead of advertising retired generic presets. Focused Go
command tests, Ruby syntax and `git diff --check` passed; it was pushed over
SSH. The initial extension package-metadata check failed because it expected
only the five site skills, while composition correctly includes the generic
documentation and monitor skills too. A subset assertion is committed in the
extension worktree; the final package checks passed against the final generic
pin.

The user selected GPT-6 Sol for all retained team roles, keeping their
existing high/xhigh efforts, and GPT-6 Luna/low for the operation-scoped
watcher. The live portal App Server catalog confirms both exact model IDs and
required efforts. The workspace feature worktree owns that policy change and
pins generic `224ee32` through extension `0d72b8c`. GPT-6 Astra must not be
selected automatically. The composed package was deployed to the aitherdev
user profile at `/nix/store/dzlsx1gzdlpzib26864gxg12fav6vx69-dev-workspace-0.2.0`.
The workspace feature branch was then cleanly rebased onto current shared
master; its review head is `e670d519` (same package-relevant source as the
deployed `b2a0b909`).

The fresh Luna/low final package check passed: extension `package-metadata`
and workspace `cluster-provider-composition` both exited 0 at generic
`224ee32`, extension `0d72b8c`, workspace `b2a0b909` before the rebase. The
live switch exited 0; package metadata has both cluster providers and the
review, handoff, writing and monitor skills installed. The shared root
provider declaration was restored from `[]` to `vpsadmin`/`vpsadminos` and
the portal service restarted. Router and portal are active; the existing
`2026-09-22-team-test-2` conversation and team endpoints both return HTTP 200
over the portal Unix socket. Browser-authenticated acceptance is still open.
`dev-session team list` returns the site's Full team, Lead-designed team and
Solo presets with concrete Sol model/effort settings.

Generic final-head CI run `35777328340` failed in unchanged
`TestReviewCommitPaginationAndRootDiff` while making empty Git commits
(`fatal: could not parse HEAD`). The fixture does not disable background Git
maintenance whereas comparable fixtures do. Earlier final-phase generic runs
passed. The evidence and possible fixture-only remedy are in
`notes/vpsfree-dev-workspace/2026-09-22-review-pagination-git-maintenance.md`;
no blind rerun or fixture change was made before review. Extension CI final
head was still running at the last snapshot.

## Current implementation scope

- `dev-workspace` is the primary implementation repository.
- `codex-web` is updated only if its public client must expose a generated
  App Server operation needed by the new direct-thread runtime.
- `vpsfree-dev-workspace` is updated only for needed vpsFree.cz session/team
  instructions. No configuration repository code change is planned.

## Decisions

- The portal and terminal share one team runtime and roster; neither is a
  secondary or simulated interface.
- There is no external bus, SQLite store, or daemon. App Server turns are the
  task/result transport, and existing send-ledger recovery is reused.
- Existing virtual team state is reset at the forward-only aitherdev cutover.
  Root conversations, worktrees, tracking, and tmux sessions are retained.
- Long verification always uses a fresh GPT-6 Luna/low watcher and is not a member.
- Implement all phases before a single consolidated GPT-6 Sol/xhigh review. Do not
  request review for intermediate commits or phases.

## Next actions

1. Complete the focused unmaterialized-thread correction and its narrow
   independent review and checks. Reconcile the unused `architect1` under
   the lifecycle contract before the next package switch, preserving the
   failed assignment's exact message ID.
2. Perform live portal and CLI acceptance, including creation, member
   configuration, tmux attachment and representative lifecycle/cluster paths.
   Verify the browser-authenticated conversation path with the user.
3. Capture comparisons, integrate reviewed feature heads fast-forward-only,
   preserve branches, and update tracking/handoff. Do not archive this session
   without an explicit request.
