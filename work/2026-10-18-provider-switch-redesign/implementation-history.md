---
lifecycle: active
---

# Provider switch redesign

Phase: isolated verification of supported root/direct-input threads. Two complete
independent review rounds finished; their narrow remediations are committed and
quick checks pass. Full native v2 child switching remains unresolved; the user's
scope question is unanswered. This is not complete or ready for deployment.
The live OpenAI workspace is unchanged. No deployment or merge is authorized.

## Phase checklist

- [x] Establish native session-local close/reopen mechanism and design.
- [x] Implement scoped automatic pause/resume, creation selection and progress.
- [x] Quick checks and complete committed deliverable; patch-equivalent rebase.
- [x] Independent final review and narrow finding remediation.
- [ ] Resolve native v2 child capability scope with the user.
- [ ] Isolated native integration, package checks, publication and CI.
- [ ] Explicit integration/deployment direction and any authorized rollout.

## Ownership and revisions

- Initiative: `2026-10-18-provider-switch-redesign`.
- Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
- Lead owns design/implementation. No native root/roster was created. Same-session
  `dev-session team list ... --as-is` confirms no valid lead thread; use the
  mandatory review standalone fallback, without inventing a team.
- Branch in both projects: `2026-10-18-provider-switch-redesign`.
- Worktrees: `worktrees/2026-10-18-provider-switch-redesign/{dev-workspace,codex-web}`.
- Initial tracking commit: `03778c16`.
- codex-web: base `5daae414ed9c1a1919242cf87d5b4af681284d0d`, published head
  `9e53d02f75caffcb925471d47b8f494f28ce136e`.
- dev-workspace: base `c1c620f` (current fetched origin/master), head
  `61830581487798af8170b307324e8a1b7da05913` (not yet published).
- dev-workspace series: `5ef93d9` dependency pin, `1aa036f` scoped runtime and
  backend, `6183058` browser controls/docs. Range-diff proved all three unchanged
  by the clean rebase from `9e66eb8` to `c1c620f`.
- No database migrations. Provider schema 1 is deployed and remains supported;
  schema 2 is introduced directly here. No intermediate schema-2 deployment or
  consumer boundary. One consolidated codex-web dependency stream.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-provider-switch-redesign/

## Implementation and rationale

See `design.md`. Native 0.163.0 loaded resume ignores provider overrides; last
unsubscribe has a 30-minute unload grace period. The isolated fake-provider probe
proved native archive/unarchive/cold-resume changes provider on the same thread
and preserves an exact queued submission. Native history archival does not
archive the development initiative. Probe: `native-capability-probe.py`.

Schema-2 exact-root session selections, creation-incarnation binding, durable
scoped stages, runtime locks and forward recovery keep unrelated sessions usable.
The worker quiesces affected terminals before capturing settings. It journals
native close/reopen/verification/continuation and restores original activity.
Existing queues and delivery identities remain intact. Pending native questions
or approvals can be canceled by interruption; continuation asks again rather than
answering them. Native descendants are discovered by ancestry, including children
spawned during close. Idle threads remain idle. Shared services keep running.

The browser/CLI supports optional new-session provider selection; omission
inherits the workspace default. Forks inherit the workspace default and may be
switched afterward. Session overrides survive workspace-default changes.
Private model-only servers cache per-provider models without loading threads.
Quota metrics do not gate switches. Progress is available before native scans,
with stage, exact thread, counts, elapsed time and safe reasons. Unknown stages,
inconsistent roots and replacement-session requests refuse.

Legacy schema-1 operations keep the deployed engine and snapshot semantics.
Retain old capability fields for upgrade admission; add scoped capabilities for
schema 2. Older packages cannot consume schema 2. No package upgrade or native
version change was executed. The old shared-start probe retries transient proc
EACCES/ENOENT within its existing deadline and still requires exact executable
and protocol proof.

## Quick verification

Repository Nix shells prepared successfully; no kernel builds. Logs:
`environment-{dev-workspace,codex-web}.log`. Both repositories declare no hook
framework; no hooks were bypassed. Formatting, Ruby/node syntax and diff checks
pass.

Passed focused checks in Nix with actual published dependency pins:

- codex-web lifecycle/request destination, conversation catalog and watch
  restoration tests.
- Go codexproviders/workspacecodex/scoped helper/provider/creation/preparation
  tests. Covers lost native close reply, invalid persisted stages/root scopes,
  exact-root replacement refusal and recovery fencing.
- Ruby scoped provider tests: 6 tests, 28 assertions; legacy provider tests:
  21 tests, 194 assertions; CLI provider tests through `test/dev_session_test.rb`:
  2 tests, 11 assertions.
- Provider browser tests: 8 passed. Shipped browser/new-session checks use their
  Go harness. Native integration tag compiles; native transition test not run yet.
- Creation receipt/preparation test proves provider survives restart/handoff
  and participates in accepted request identity.

Environment lessons: set `DEV_WORKSPACES_CODEX_PROVIDERS` to an absent fixture
path for unregistered test workspaces. Inside Nix use `TMPDIR=/tmp` to avoid
long Unix socket paths. Standalone codex_runtime tests miss shared ManagedTmux;
use the suite entry point with --name. browser_contract_test.cjs requires the
Go HTTP harness. These fixture/invocation errors were corrected, not accepted as
product failures. The ambient GOFLAGS requires explicit `-mod=readonly`.

## Review and remaining verification

High risk: native lifecycle, persisted state, permissions, protocol and
mixed-generation compatibility. All four mandatory-review lanes apply.
Installed catalog fallback: reviewer `gpt-6-astra`, `xhigh`, read_only; no nested
agents. Catalog digest at selection:
`ca26056cb57c0936f4430ceb0338f30fa147b73199eb1bc6caabd7c378e0edaf`.
Utility policy remains `gpt-6-luna`/low, operation lifetime.

Next: independent complete-branch review, fix findings, then a fresh utility runs
isolated native tests and packaged checks. Native goal restart, queued input,
settings/policies, idle and unrelated busy work require actual native evidence.
Review native late descendants, cold goal capture and interrupted recovery.
No integration, package selection, live switch or service restart during tests.
Publish feature branches and inspect CI; keep lifecycle active pending explicit
integration direction. No archive/delete/stop action is authorized.

## Documentation and incident references

Project behavior and recovery: dev-workspace `docs/codex-providers.md`,
`docs/dev-sessions.md`, `docs/workspace-portal.md` and README. Reusable extension
contracts: codex-web README. Main agent applied user-facing writing skills.
Deployment instructions are prepared guidance, not executed rollout evidence.
Prior incident: `work/2026-10-18-codex-subscription-switch/incident.md` and
`notes/dev-workspace/2026-10-18-provider-switch-idle-and-startup-failures.md`.

## Review findings and current remediation checkpoint

Reviewer /root/provider_final_review, gpt-6-astra/xhigh, all four lanes, read-only.
Original review: codex-web 5daae41..9e53d02; dev-workspace c1c620f..6183058.
History/stream conclusions accepted: no obsolete history; one consolidated
codex-web stream; no migrations. Original branches were not ready.

1. Blocking late children: now reconcile both unarchived and newly archived
   descendants to a fixed point. Fake native regression includes a child born
   during parent archive, including lost-close-reply recovery.
2. Blocking native v2 child ownership: native source confirms overrides ignored
   and direct input/settings/goals forbidden. Captured unsupported children
   currently refuse before any close. Async user question asks whether to extend
   native Codex or ship the explicit limitation; unanswered. No native update.
3. Blocking stale goal restoration: remove direct goal/set pause/reactivation.
   Cold native resume owns current durable goal state; continuation receipts
   apply only to interrupted non-goal work. Goal-owned intent prevents a stale
   ordinary continuation after completion. Completion-during-close tests pass.
   Actual native active-goal resume still needs integration proof.
4. Blocking creation admission race: shared creator admission and EX default
   snapshot/fence publication. An admitted-creator regression passes.
5. Important CLI catalog mismatch: new shared codexproviders.ReadModels and
   workspacecodex.ModelsForDirectory used by browser and CLI create/presets/
   team validation. A target-only Daybreak model test passes without any shared
   daemon. CLI fork default catalog path also routed through this boundary.
6. Important CLI journal gap: persist optional provider in original creation
   journal; omission on retry retains it, changed provider refuses. Regression
   reproduces the journal-before-binding window and passes.
7. Important plan creation: add provider control, request/draft/receipt transport
   and destination catalogs independent of source catalog. Synthetic shipped
   wiring test passes; endpoint test proves --provider reaches creation helper.

Current passed quick checks: scoped native fake tests (lost reply, late child,
completion interleavings), provider models, creation/preparation/plan Go checks,
legacy Ruby 21/194, scoped Ruby 7/33, CLI provider Ruby 3/14, provider browser 10.
New-session Playwright harness was skipped without PORTAL_BROWSER_TEST=1; do
not describe that as actual browser execution. Shipped-browser Go harness passes.

Remaining before long tests: reconcile docs, focused checks, native child/goal
limitations, commit and consolidate remediations, rerun affected review lanes
with same reviewer. Then isolated native and package checks via fresh utility.
Native source evidence: /nix/store/9is267xl3palxb615kk86qlli9nggkf9-source,
app-server thread_processor.rs 1722 (snapshot archive), 3991/4581 (v2 resume),
thread_input.rs 12 (direct input), thread_goal_processor.rs 323 (goal guard),
core/agent/control/spawn.rs 317/458 (stored child provider), ext/goal/runtime.rs
412 (restore durable active goals), ext/goal/extension.rs 165/196 (resume/idle).
No long command is running.

Remediation revisions (same base c1c620f): dependency 5ef93d9 unchanged; runtime
85bf6d899c0daa3d7e78297e3e3528a2101d2f21; browser
c547d754b2b883cddf4ef77c358793717e8771cf. Fixups were folded into owning commits.
The initial attempt to combine git --fixup with -F was rejected by Git without
creating a commit. Explicit fixup! messages through temporary files plus ordinary
-F commits and autosquash succeeded. No reset/stash or hook bypass was used.

The previous standalone review follow-up interface was unavailable. A fresh
read-only standalone native review uses the same installed Astra/xhigh policy,
all four lanes and the complete packet. Actual native header verified:
OpenAI Codex 0.163.0, gpt-6-astra, openai, approval never, sandbox read-only,
xhigh, ephemeral session 01a14f04-27a1-7b52-9d34-1bb1b2dba8dd.
Log review-remediation.log; final output review-remediation-result.md.
The reviewer may read source and native references but cannot edit/test/deploy.
Its command is currently running under parent tool session 49226.

## Second review reconciliation and final verification candidate

Second reviewer: fresh standalone read-only Astra/xhigh, native ephemeral ID
01a14f04-27a1-7b52-9d34-1bb1b2dba8dd, matching installed review policy. Full
report: review-remediation-result.md. The old reviewer identity could not be
resumed; the replacement reason and actual native header are retained above.
Review process is complete, not still running under session 49226.

- Blocking archived loaded descendants: preflight now includes loaded archived
  children and the native child capability guard. Inactive archived histories
  remain excluded. Reconciliation also considers loaded/recently interrupted
  archived histories. A retained archive marker is preserved on reopen; an
  already archived loaded thread is unarchived before archive so teardown
  actually runs. The focused archived-child guard regression passes.
- Important plan settings: newly accepted plan requests carry the server-owned
  destinationSettings marker. Schema-1 plan creation resolves the selected
  destination model independently. Older accepted receipts retain their original
  source-settings semantics, including when retried after upgrade. The marker
  does not change user request identity. Strict readers allow it only on plans.
  The endpoint regression uses different source/target models and proves the
  selected provider and settings reach the helper. This helper fixture does not
  emit a real creation completion proof and does not assert session readiness.
- Important restored draft catalogs: programmatic provider restoration reloads
  models. Shipped-wiring regression restores an explicit provider while a default
  response is held, proves that stale response cannot overwrite the target list,
  and then restores an inherited default selection. All 11 provider browser
  contracts pass.
- Advisory native goal evidence: add a separate queue-free active-goal root.
  The goal-bearing queued root remains as independent queue-preservation proof.

These changes directly implement the reviewer's requested narrow corrections;
mandatory-change-review step 9 applies. No new public/cross-project contract or
expanded supported boundary was introduced, so an additional reviewer turn is
not required merely to confirm them. The native v2 limitation remains a separate
unaccepted outcome limitation. The review explicitly permits isolated root
verification without claiming v2 support. No live tests or package selection.

Final consolidated dev-workspace candidate ab6c272ac78851f008ae9107c5c50a15192fe49c:
base c8f9a2bb0ef72a1c0ff0061bd9898df5df7dd5cb; commits b3e0d23 (pin),
4f87f25 (runtime/backend), ab6c272 (browser/docs). Clean rebase onto the new
upstream host reporting fix; range-diff proved all three patches unchanged.
Previous candidate de8724c/e14c89f and c547d75/85bf6d8 were superseded and remain
only as evidence. No migrations; no intermediate schema-2 deployed consumer.
Codex-web remains 5daae41..9e53d02, one published additive interface commit.

Verification policy re-resolved from the installed catalog digest
ca26056cb57c0936f4430ceb0338f30fa147b73199eb1bc6caabd7c378e0edaf:
verification_watcher gpt-6-luna/low, operation lifetime, native utility
verification_watcher-low.toml (dw_a040191becdc195dfbdb68dd182493e81271dde01bebaf9b).

## First isolated native run

Fresh Luna/low watcher /root/provider_verify_native_packages completed the exact
ab6c272/9e53d02 batch. Native exit 1, elapsed about 108 seconds. Native scoped
switch failed during switching with RPC -32600 thread not found. Legacy native
routing passed both directions in 46.75 seconds, preserving histories, settings
and model routing. Package checks were not reached due to the scripted && gate.
Evidence: native-integration.log and native-integration.exit; no running operation.

Source-backed cause: native goal/get on an unloaded thread uses the rollout
lookup that excludes archived histories (thread_goal_processor.rs:343). The
worker queried goals after native archive. Read goal state after cold reopening,
where native current-state restoration already applies. Late-descendant capture
reads while unarchived/loaded, then closes without a post-close query. No goal
mutations or replay were added. The fake native now rejects goal queries on
archived histories; all scoped quick checks pass and native-tag compilation
passes. Failure diagnostics now include scoped progress and a bounded synthetic
native log tail. This is a narrow correction within the reviewed goal-ownership
design; no additional review lane or public contract change.

Second verification candidate: dev-workspace b81c6f0b4b1db7d0d507ba5097a674871bb4c8f3,
base c8f9a2b, final commits b3e0d23, 1222b73, b81c6f0. Native lookup correction
folded into the runtime commit. Codex-web remains 9e53d02. Quick scoped checks,
compile-only native tag, formatting and diff checks pass. Next utility owns
isolated scoped-native rerun, package checks and an actual Playwright creation
settings test. Exact scripts retain separate logs/status; no deployment.

## Second verification batch

Fresh utility /root/provider_verify_second_batch (Luna/low) tested b81c6f0.
Actual Playwright TestNewSessionSettingsBrowser passed in 10.99 seconds (batch
42 seconds including tool preparation). Codex-web complete flake check passed
at 9e53d02, including 64 browser contracts. Its exact-SHA GitHub Check run also
passed: https://github.com/aither64/codex-web/actions/runs/39123540992 .

Scoped native failed reopening due to nil shell_environment_policy.set. The
isolated test invoked the Go helper directly and omitted the Ruby worker's
trusted environment injection (workspace-provider-sessions.rb:342). Fixed the
fixture to perform that injection. Test cleanup now force-reaps its disposable
native process group instead of waiting for graceful model request shutdown.
No production environment fallback or weaker checks were added.

Workspace package failed one Ruby fixture: the archive-recovery package-layout
copy list lacked the new workspace-provider-sessions.rb dependency. Production
Nix install already includes it. Added it to that fixture. Evidence retained in
native-scoped-2.log, package-dev-workspace.log, package-codex-web.log and their
.exit files. No kernel build occurred and no operations remain from that batch.
Only affected native/workspace-package checks will rerun; browser and codex-web
successes remain valid because their code and derivation inputs are unchanged.

Third verification candidate: dev-workspace 029b8fef38c317cdef3cc4d5bdd988ee9a44193a,
base c8f9a2b, commits b3e0d23, ee1917e, 029b8fe. Only native fixture environment/
cleanup and package-layout fixture dependency changed since b81c6f0. Focused
archive-recovery fixture passes (1 test / 3 assertions); native tag compiles.
These are narrow fixture repairs with no production behavior change. A fresh
Luna/low utility /root/provider_verify_corrected_fixtures owns exact scripts
verify-scoped-native-3.sh and verify-workspace-package-3.sh; separate logs/status.
The catalog digest remains ca26056cb57c0936f4430ceb0338f30fa147b73199eb1bc6caabd7c378e0edaf.

Both feature branches are now published. dev-workspace exact head
029b8fef38c317cdef3cc4d5bdd988ee9a44193a was pushed over SSH after fetching;
origin/master still c8f9a2b. GitHub Check run 39130422753 is queued for this exact
head: https://github.com/aither64/dev-workspace/actions/runs/39130422753 .
No PR, merge or deployment was requested or performed. A fresh CI utility will
own monitoring after the current verification utility has completed, preserving
the installed max-concurrent-one watcher policy.


# Continuation: compatibility, verification and final publication

---
lifecycle: active
---

# Provider switch redesign

Phase: final-head packaged and VM verification; native v2 scope awaits the user. Scoped routing, automatic
pause/resume, optional creation providers and immediate progress are implemented
and published. Two independent complete-branch review rounds finished; requested
narrow remediations are committed. Full native v2 child support remains
unresolved and the user's scope choice is unanswered. This is not complete or
ready to deploy. Live OpenAI routing and services remain untouched.

## Phase checklist

- [x] Design and scoped runtime/browser/CLI implementation.
- [x] Quick checks, full committed branch review and finding remediations.
- [x] Publish both feature branches, including compatibility corrections.
- [x] Codex-web complete package checks and exact-SHA CI.
- [x] Actual Playwright creation settings regression.
- [x] Corrected isolated native verification.
- [x] Workspace-package verification.
- [x] Focused retained-creation compatibility review and narrow remediations.
- [ ] Final-head package/CI proof and archive restart fixture verification.
- [ ] Resolve native v2 child support scope.
- [ ] Explicit integration/deployment direction and authorized rollout.

## Ownership and revisions

This conversation created initiative 2026-10-18-provider-switch-redesign from
/home/aither/workspace/ai/vpsfree.cz. No native lead or retained roster was
created. dev-session current finds none, and team list confirms no valid lead
thread; do not adopt another session. Lead owns design and application edits.
Only policy-authorized independent review and verification utilities delegated.

Both worktrees and feature branches use 2026-10-18-provider-switch-redesign:

- dev-workspace: worktrees/2026-10-18-provider-switch-redesign/dev-workspace,
  base c8f9a2bb0ef72a1c0ff0061bd9898df5df7dd5cb, published head
  2bfc504c44b34ebc235bbdb1dbfbde0da917d063. Four final commits: b3e0d23
  dependency pin, 3476f2c runtime/backend, 4e37ece browser/docs, 2bfc504
  archive restart verification race fix.
- codex-web: worktrees/2026-10-18-provider-switch-redesign/codex-web,
  base 5daae414ed9c1a1919242cf87d5b4af681284d0d, published head
  9e53d02f75caffcb925471d47b8f494f28ce136e. One additive interface commit.
- SSH remotes: git@github.com:aither64/{dev-workspace,codex-web}.git.
- Initial substantive tracking commit 03778c16; shared workspace stays on master.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-provider-switch-redesign/

No database migrations. Provider schema 2 is introduced directly; deployed
schema 1 and its operation engine remain supported. No intermediate schema-2
release, deployment or external consumer. All codex-web pins consistently select
9e53d02; one consolidated update stream. Remediations were folded into owning
commits. Rebase onto c8f9a2b was clean and range-diff proved patch equivalence.

## Supported implementation and unresolved boundary

Design and compatibility: design.md. Scoped switches retain exact histories,
queues/delivery identities, model/effort, permissions and session environments.
The worker closes and reopens only affected native threads and terminal clients;
shared services keep running. Native cold resume owns current durable goal state;
there is no goal/set replay. Interrupted non-goal work uses correlated continuation
receipts. Workspace defaults preserve explicit session selections.

Browser/CLI creation selects an optional provider and uses destination catalogs.
Original creation journals retain provider intent before root binding. Inherited
creators and default-switch inventory share an admission fence. Progress precedes
native scans and gives stage, exact thread, counts, elapsed time and safe reasons.
Private model-only servers avoid shared-daemon model catalog mismatches.

Native 0.163.0 v2 children reject direct input/settings mutations and restore
saved child providers despite parent/caller overrides. Preflight refuses these
children, including loaded archived children. Full switching of such sessions
needs a packaged native change. The pending user question asks whether to extend
native Codex or ship this explicit limitation; neither option is accepted yet.
Isolated root verification does not establish v2 or retained-direct-roster proof.
Do not live-switch, restart services, select packages or deploy during development.

## Review

High risk: native lifecycle, persisted state, permissions, protocol and mixed
versions. General, architecture, scope and risk lanes applied. No roster, so
installed default review-purpose fallback selected Astra/xhigh/read-only from
catalog ca26056cb57c0936f4430ceb0338f30fa147b73199eb1bc6caabd7c378e0edaf.
First reviewer /root/provider_final_review; replacement native ephemeral identity
01a14f04-27a1-7b52-9d34-1bb1b2dba8dd matched model/effort. Earlier reviewer
follow-up interface was unavailable, requiring that fresh standalone review.

First review identified late descendants, v2 limitations, stale goal activation,
creation admission, CLI catalogs/journals and plan creation. Second complete
review accepted whole-branch history/update consolidation and no migrations;
found archived-loaded child discovery, unmanaged plan destination settings,
restored draft catalogs and weak goal-fixture evidence. Report:
review-remediation-result.md. All requested narrow corrections are committed;
native v2 scope remains unresolved. Step 9 permits focused verification of these
fixes without another confirmation review; public/supported boundaries unchanged.

## Verification and current operations

Quick checks pass: scoped fake-native recovery/lost-reply/late-child/goal-completion
cases; loaded archived-child guard; creation/plan/provider models; legacy/scoped
Ruby and CLI provider subsets; 11 provider browser contracts; native-tag
compilation, formatting, syntax and diff checks. Detailed counts/commands and
superseded heads are in implementation-history.md.

First native run: legacy routing passed both directions; scoped operation exposed
an archived goal/get lookup failure. Fixed by querying current goal state only
after cold reopening. Fake-native regression now rejects archived goal lookups.
Second native run exposed a test-only omission of the Ruby worker's environment
injection. Workspace package exposed a package-layout fixture missing the new
helper dependency. Both fixtures corrected; focused fixture check passes (1/3).
Raw failed logs/status are retained. No acceptance based on blind reruns.

Actual TestNewSessionSettingsBrowser passed in 10.99 seconds at b81c6f0; source
browser/runtime unchanged since then. Codex-web flake check passed at 9e53d02,
including 64 browser contracts. Its CI passed:
https://github.com/aither64/codex-web/actions/runs/39123540992 .

Fresh gpt-6-luna/low utility /root/provider_verify_corrected_fixtures owns the
corrected exact-029b8fe scoped-native and workspace package scripts, separate
logs/status: native-scoped-3.*, package-dev-workspace-3.*. No parallel parent
polling. Watcher catalog digest above; utility verification_watcher-low.toml,
operation lifetime, max concurrent one. Previous utilities completed. Browser
and unchanged codex-web checks are not repeated. No unexpected kernel build.

Dev-workspace exact-head CI run (monitor with a fresh utility after the current
one finishes): https://github.com/aither64/dev-workspace/actions/runs/39130422753 .

## Documentation, evidence and next action

Project explanations: dev-workspace docs/codex-providers.md, docs/dev-sessions.md,
docs/workspace-portal.md and README; codex-web README owns generic client contracts.
Main agent applied vpsfree-user-facing-writing/humanizer-en. Deployment guidance
is prepared documentation, not rollout evidence. Current scope: plan.md and
design.md. Full review packet: review-packet.md. Verification scope/scripts:
verification-brief.md. Detailed development history: implementation-history.md.

Next: collect corrected native/package results, diagnose any failures, then
monitor exact-head CI. Resolve native v2 scope before claiming the requested
outcome complete. No merge, deployment, PR, archive, deletion or stop authorization.
Retain branches and active lifecycle.


## Corrected-fixture batch result

Both checks completed with exit 1 at 029b8fe; all Ruby package shards passed
(including the repaired archive fixture). The native scoped switch reached
reopening/continuation in 3 seconds but its assertion compared native null versus
"default" service-tier spellings literally. Production already treats these as
the same default scheduling tier (providerTierMatches); use that established
semantic comparison in the test and retain exact checks for nondefault tiers.
Package Go tests failed only an obsolete source-text marker modelSelect.required
whose variable was renamed by grouped catalogs. Remove that brittle marker;
actual Playwright coverage still verifies concrete required model/effort choices.
No production edits for either result. Evidence: native-scoped-3.* and
package-dev-workspace-3.*. No operations remain; no kernel builds occurred.


Final test-assertion corrections committed and quick checks pass: native tag
compiles, shipped browser interaction check passes, gofmt/diff clean. Final
published dev-workspace head 777393773123007a679ad9da1d30f4183ed90b95, base
c8f9a2b, commits b3e0d23/548047d/7773937. Source behavior is unchanged since
b81c6f0; later changes repair test fixtures/assertions only. Feature history
remains three consolidated commits, no obsolete implementation or migrations.
Force-pushed with an explicit lease on 029b8fe after fetching; no default-branch
content changed. Superseded active CI runs for this branch will be canceled.

Current exact-head GitHub Check is run 39130750905 at 7773937:
https://github.com/aither64/dev-workspace/actions/runs/39130750905 .
Cancellation of superseded run 39130422753 was attempted after the force-push,
but GitHub returned HTTP 403 Resource not accessible by personal access token.
Do not retry with guessed credentials; the old run may finish and cannot serve
as final-head evidence. This is an API authorization limitation, not a failed
code check. No workflows from other branches were targeted.


Final monitoring fallback: the fresh delegation interface was unavailable in the
current turn. Announced the dev-session-monitor parent-monitoring fallback rather
than stalling verification or reusing a completed utility. Parent launched exact
7773937 native/package checks and watched CI run 39130750905. Independent logs
and statuses: native-scoped-4.*, package-dev-workspace-4.*, ci-final.*. Native and
package processes remain owned until completed; no live mutation or retries.


Final native scoped check passed at 7773937: four independent roots applied in
1.617790321 seconds without daemon restart; full test 2.67 seconds. Goal-only
and queued-goal work continued, queue remained one exact entry, ordinary active
work resumed, idle remained idle and unrelated busy work kept running. This is
an isolated fake-provider/native test, excluding terminal quiescing and provider
auth/health. It does not establish native v2 or retained direct-roster support.
Evidence: native-scoped-4.log and native-scoped-4.exit (0).
Reusable fixture lessons: notes/dev-workspace/2026-10-18-scoped-provider-native-fixtures.md.


Final workspace package passed at 7773937, status package-dev-workspace-4.exit=0.
Full Ruby shard manifest, ordinary Go suite and browser contracts passed; output
/nix/store/ib8i67lp2n77yznn9fgj07fdw4aqqs23-dev-workspace-0.2.0. No activation.
CI run 39130750905 remains in progress (fast and lifecycle archive VM jobs).
Only parent-owned CI watch session 46555 remains running; local package and
native operations are complete. No test data or Playwright GC root remains
from completed isolated checks. Raw evidence is retained under this initiative.


## CI failure investigated

Final-head run 39130750905: fast passed (8m30s), archive VM failed (8m11s), host
skipped by workflow policy. Downloaded ci-final-failure.log before any retry.
Failure is testScript line 133: an immediate assertion of running after portal
restart. Receipt identity was retained (line 132 passed); the worker was still
held in systemd start-pre. Existing lifecycle store deliberately restores running
receipts as paused until background worker reconciliation proves them. The same
unconditional assertion exists unchanged on base c8f9a2b; socket readiness does
not establish that asynchronous reconciliation has finished.

Correct the VM fixture to await the same receipt reaching running while the
pre-exec barrier remains held, with the actual response in assertion diagnostics
and the existing 60-second test wait convention. No application behavior or
weaker lifecycle proof is introduced. This directly corrects a verification race
inside the existing reviewed contract; it does not expand the supported boundary.
Native/package/browser source is unchanged and successful evidence is retained.
The initial nested-shell Python syntax invocation was malformed; corrected by
using a separate temporary checker script. No source defect was accepted.
No verification operations remain running from the failed CI batch.


Published follow-up 58d042195a7f60939325faf6617fb6b7dd2cfcc6 changes only the
archive VM fixture, in its own focused commit because it repairs a pre-existing
verification race. Nix parse, embedded Python compilation and diff checks pass.
The actual receipt response now accompanies failure diagnostics. This narrows
test scheduling assumptions without changing application/lifecycle contracts;
no additional production design or affected review lane was introduced.
Whole series remains four reviewable commits with one dependency stream and no
migrations or obsolete approaches. Native/runtime/browser inputs are unchanged
since their passing evidence. The new exact-head CI builds the package and VM,
so no redundant local whole-suite run is launched merely for this Nix fixture.

CI run 39131733420 at 58d0421 is owned by parent monitoring fallback:
https://github.com/aither64/dev-workspace/actions/runs/39131733420 .
Previous branch runs 39130750905 and 39130422753 are now completed failures;
there are no superseded active runs left to cancel. Raw new evidence:
ci-reconciled.log and ci-reconciled.exit. No live deployments or mutations.


## Final cross-reader compatibility correction

Finishing inspection found that valid_portal_managed_creation_request? in the
host rejected provider and destinationSettings, while the Go receipt reader
accepted them. This would reject later package transitions even for ready
managed/direct plan receipts. Also, an unmanaged destination-settings receipt can
exist before provider state adopts schema 2; older portals strictly reject its
new field, so package admission must require scoped capabilities for such retained
receipts too. These are actual format-consumer gaps, not hypothetical risks.

Implement the host reader rules and target capability check, sharing its existing
private directory boundary. Preserve legacy schema-1 inspection when new fields
are absent. Design addendum and project compatibility docs updated. This is a
persisted-state/package-admission contract correction beyond the narrow review
fixes; run the affected independent review lanes on the final committed delta
before its long verification. The previous standalone review was ephemeral and
cannot be resumed through the unavailable delegation interface; use a fresh
native read-only standalone reviewer with the installed Astra/xhigh policy and
record the actual header. All new root/native support questions remain pending.


Committed compatibility review candidate cb29853284a965b1b77ab16c8fc9e4bcdf7186d5
(base c8f9a2b; b3e0d23/ad14862/9e155ca/cb29853). Compatibility fixes folded into
owning runtime/browser commits, VM fixture remains separate. Not pushed yet.
Same-session roster check still reports no valid native lead/roster. Fresh native
standalone review launched with explicit installed Astra/xhigh/read-only settings,
all four affected lanes, no nested agents/tests/edits. Tool session 96084 owns it;
review-compatibility.log and review-compatibility-result.md retain its evidence.
The existing CI watch session 85374 still owns run 39131733420 at 58d0421 only.
No long verification of the new compatibility delta before that review finishes.


Third review actual native header verified: OpenAI Codex 0.163.0, provider openai,
model gpt-6-astra, reasoning xhigh, approval never, sandbox read-only; ephemeral
native session 01a14f3c-1fe3-7510-9bb3-f7ca43f465ee. This is a standalone
review-purpose fallback under installed policy, not a retained team member.
The scope question was presented again with the now-concrete published and
verified root deliverable; no answer has arrived, so native v2 scope is unchanged.


CI 39131733420 passed at published 58d0421: fast 8m32s, archive lifecycle VM
10m51s, host skipped by policy. This verifies the diagnosed restart-fixture race
fix rather than a blind retry. Evidence ci-reconciled.log and exit 0. It does
not verify the later cb29853 receipt compatibility delta; final-head verification
remains pending independent review. Only review tool session 96084 is running.


Third review completed (actual identity above), complete report
review-compatibility-result.md. History/one pin stream/no migrations accepted.
Blocking: preparation snapshots persist provider before either provider state or
creation receipt exists. Extend the same scoped-capability admission to unfinished
session-preparations, with a valid paused snapshot regression in that exact window.
Completed mappings are compact and have no new fields. Important: the CLI creation
journal also persists provider through ready, but the host's separate journal
reader rejected it before skipping ready journals. Align its optional provider
validation and prove ready journals no longer block host lifecycle admission,
while invalid IDs still refuse. These directly requested bounded remediations
keep the reviewed capability design and do not require confirmation review under
step 9. No new schema or supported boundary. Quick checks follow, then consolidate
and perform final-head package/CI verification. Native v2 scope remains unanswered.


Third review remediations pass: 23 focused provider/creation host checks,
230 assertions, no failures; Ruby syntax and diff checks pass. Preparation
regression uses a paused frozen snapshot with correct digests and no receipt or
provider-state artifact, proving older-package refusal and compatible admission.
CLI regression proves ready provider journals pass host lifecycle inspection and
invalid IDs refuse. Current format consumers now cover preparation input/handoff,
portal receipts and the original CLI journal. Completed preparation mappings are
compact. Original native routing/Go/browser inputs remain unchanged.
The reviewer-requested narrow fixes were folded into the owning runtime/browser
commits without another confirmation review (step 9). No new schema/capability.
Next: push final exact head and monitor its packaged/VM checks. No long check is
running now; the previous CI and third review both completed.


Final consolidated compatibility head: 535b1f4ff791f4df866362a5a6c786488d983e84,
base c8f9a2b; commits b3e0d23 (pin), 3476f2c (runtime/backend), c18b055
(browser/docs), 535b1f4 (archive VM assertion). Complete history and final delta
remain consistent with independent review plus its requested narrow corrections:
one codex-web update stream, no obsolete approaches, no migrations. Codex-web
remains 9e53d02. No default-branch integration approval exists. Final native and
Go inputs match the passing root test; final Ruby/package checks are delegated
to the exact-head CI rather than duplicating another local whole suite.


Final candidate published with explicit lease on 58d0421 after fetching; target
master remains c8f9a2b. No superseded active CI runs remain. Exact-head Check
39133182387 at 535b1f4 is now monitored under the announced parent fallback:
https://github.com/aither64/dev-workspace/actions/runs/39133182387 .
Evidence: ci-compatibility-final.log and ci-compatibility-final.exit. It is the
only running verification operation. The third review identity completed; no
subagents remain assigned new work. Do not claim deployment readiness while
native v2 support remains unaccepted and this run is pending.


A final consumer check found the browser fork form still requested the source
session catalog although the reviewed fork contract and backend/CLI use the
workspace default. Corrected only that destination URL/group ownership: fork
models use the default catalog and never replace the source conversation's
catalog. Extended the shipped wiring regression to source/plan/fork catalogs;
the visible dialog now states default-provider inheritance. This is a narrow
consumer correction inside the reviewed shared-catalog/fork-default boundary,
without a new endpoint, provider selector or supported behavior. No separate
confirmation review is required for it. The current CI 39133182387 remains
owned and tests 535b1f4 only; it cannot certify this later browser delta.


Final browser consumer correction folded into its owning commit; published head
2bfc504c44b34ebc235bbdb1dbfbde0da917d063 (base c8f9a2b), commits
b3e0d23 / 3476f2c / 4e37ece / 2bfc504. Branch clean. Code interfaces, native
routing, migrations and dependency stream unchanged. All 11 provider browser
contracts, source/plan/fork destination catalogs, node syntax and focused Go
browser/plan checks pass. Explicit lease on 535b1f4 used after fetch.
Run 39133182387 still owns exact compatibility head 535b1f4, now superseded only
by browser catalog/copy fixes. GitHub cancellation rights remain unavailable
(403 documented earlier); preserve its result separately, not as final-head proof.
No additional runtime or model-choice investigation remains in this scope.
Await final-head CI and the pending native-v2 scope decision. No live mutation.


Exact final-head Check 39133675250 at 2bfc504 is monitored under the parent
fallback: https://github.com/aither64/dev-workspace/actions/runs/39133675250 .
Evidence ci-final-browser.log and ci-final-browser.exit. Compatibility run
39133182387 remains separately owned until completion or authorized cancellation;
its earlier state cannot certify the final browser delta. No source changes
remain planned. Native v2 scope is still a required unanswered user choice.


Exact final-head local proofs at 2bfc504 passed: native-scoped-final.exit=0 and
browser-settings-final.exit=0. The same isolated native goals/queues/idle/unrelated
work contract passes against the final embedded assets, and the actual Playwright
creation settings/draft/recovery regression passes against final shipped files.
These quick checks were repeated because browser/template inputs changed, rather
than claiming tree equivalence as final binary proof. The temporary Playwright
GC root was removed after completion; disposable native homes/processes were
reaped by the test. Native/browser tool sessions 79755/17130 are complete.
Only CI watches 71875 (final 2bfc504) and 18532 (superseded 535b1f4) remain.
Cancellation of 39133182387 was attempted for the new force-push and again
returned HTTP 403; neither token scope nor other branches were changed.


Compatibility CI 39133182387 completed successfully at 535b1f4. This is packaged
and VM proof for the reviewed retained-preparation/receipt/CLI-journal changes,
with final Ruby/host logic identical to 2bfc504. It is retained as scoped evidence,
not substituted for the pending final-browser exact-head run. Watch session
18532 completed; only final CI watch 71875 remains running.


## Checkpoint before final stock-Codex review

---
lifecycle: active
---

# Provider switch redesign

Phase: finalizing the stock-Codex implementation after the user's scope change.
The user rejected downstream Codex patches/rebuilds, then explicitly accepted
stopping temporary subagents. The native build is canceled; no build remains.
The patch, Nix override and unused custom protocol are removed from the tree.
No live deployment/default-branch integration occurred.

## Phase checklist

- [x] Per-session/default selection, creation options and immediate progress.
- [x] Replace in-place patch with stock archive/unarchive/resume for retained roots.
- [x] Remove child migration/refusal; native teardown may stop temporary children.
- [x] Focused stock-worker Go checks and eleven browser contracts pass.
- [ ] Consolidate/commit the final no-patch series and review changed lanes.
- [ ] Exact stock-binary roster/child/goal/queue/endpoint continuity proof.
- [ ] Relevant package checks and final publication/CI.
- [ ] Integration/deployment (not authorized; initiative stays active).

## Ownership and exact revisions

Initiative created by this conversation: 2026-10-18-provider-switch-redesign,
workspace /home/aither/workspace/ai/vpsfree.cz. No native lead or retained roster
was created; current finds none and team list confirms no valid lead thread.
Do not adopt another session. Lead owns design/application work. Only policy-
authorized review and verification utilities were delegated.

Both worktrees/branches use 2026-10-18-provider-switch-redesign:

- dev-workspace worktree worktrees/2026-10-18-provider-switch-redesign/dev-workspace;
  base c8f9a2bb0ef72a1c0ff0061bd9898df5df7dd5cb; previous published head
  2bfc504c44b34ebc235bbdb1dbfbde0da917d063. Consolidated local head
  b64afb065570036ccc6e0c762dcd79e18554b622: b3e0d23 pin, 5473efe native,
  0f899c2 worker, cf77e9c browser, b64afb0 archive VM fixture. Pending narrow
  native import/pending-input correction and regression fixture are in the tree.
- codex-web worktree worktrees/2026-10-18-provider-switch-redesign/codex-web;
  base 5daae414ed9c1a1919242cf87d5b4af681284d0d; clean published head
  9e53d02f75caffcb925471d47b8f494f28ce136e, one additive interface commit.
- SSH remotes git@github.com:aither64/{dev-workspace,codex-web}.git.
- Shared coordination checkout remains master; initial tracking commit 03778c16.
  Current tracking/evidence remains in the working tree under the normal cadence.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-provider-switch-redesign/

No migrations. Schema 2 is introduced directly while deployed schema-1 state and
its engine remain supported. No intermediate schema-2 release/deployment/external
consumer. One consolidated codex-web dependency stream selects 9e53d02. Requested
fixes folded into owning commits; the existing VM timing-race fix remains a
separate reviewable commit. No obsolete approaches or redundant pin history.
Feature refs retained; no PR, merge, archive, deletion or session stop.

## Implementation and supported boundary

Design/compatibility brief: design.md. Provider switches reserve only affected
session authorities and terminal clients; shared native/portal services continue.
Native updates keep histories, queues, goals and the parent agent tree alive.
Only the exact journaled old-provider source turn is replaced; ordinary work
continues with correlated receipts, while native goal/queue scheduling retains
ownership. The scoped archive prototype was removed; genuine deployed schema-1
workspace-wide recovery remains supported. Existing temporary children keep their
old provider and active turn, while new children inherit the switched parent.

Provider selection at creation survives drafts, preparations, original CLI
journals and exact-root binding. Destination catalogs serve new/plan creation;
forks use the workspace default catalog, separate from the source session.
Source/target settings and retained ownership remain validated. Creation
admission prevents a default switch from missing an admitted new root.
Progress precedes native scans, with stage, thread, counts, elapsed time and safe
reasons; quota display does not gate switching. No global idle/ledger scan.

The host reads every new provider-bearing format: preparation snapshot/handoff,
portal receipts, and CLI creation journal. Retained preparations/receipts require
scoped package capabilities before activation, even before provider state exists.
Legacy schema-1 records without new fields retain their prior inspection policy.

## Previous baseline verification

These checks covered the previous archive-based scoped prototype. Its temporary
data was cleaned up. New in-place checks and a native compile are now underway;
the previous successes do not establish the refined behavior.

- Native scoped test at exact 2bfc504 passed: four independent roots applied in
  1.618088611 seconds without daemon restart; full test 2.73s. Ordinary work and
  two goals (one queue-free) resumed; exact queued entry survived; idle work
  stayed idle and unrelated busy work continued. Fake providers, no real model
  inference/subscription used by these tests. Excludes terminal quiescing and
  provider auth/health. Does not prove v2 or retained direct-team roster behavior.
- Actual Playwright TestNewSessionSettingsBrowser at exact 2bfc504 passed in
  9.47s. Eleven provider browser contracts pass, including source/plan/fork
  catalogs and saved-provider restoration versus an outstanding default reply.
- Focused provider/creation host checks: 23 runs / 230 assertions pass. Covers
  pre-receipt preparations, completed CLI journals, strict invalid fields and
  incompatible target refusal. Formatting, syntax, Nix/VM Python parse pass.
- Final exact-head CI 39133675250 passed at 2bfc504: fast/package/focused checks
  8m34s; packaged browser archive/recovery/revival VM 8m41s. Host job skipped by
  declared feature-branch policy. URL:
  https://github.com/aither64/dev-workspace/actions/runs/39133675250
- Compatibility CI 39133182387 passed at 535b1f4; archive-race correction CI
  39131733420 passed at 58d0421. Superseded runs are complete. Cancellation was
  attempted while needed, but token lacked rights (HTTP 403); no scopes changed.
- Codex-web full flake check and exact-head CI passed at 9e53d02:
  https://github.com/aither64/codex-web/actions/runs/39123540992

Details and raw evidence: verification-result.md, implementation-history.md,
per-run logs/statuses. Failed runs were diagnosed before corrections/retries:
archived goal lookup, missing fixture environment/helper, default-tier spelling,
obsolete source marker, and asynchronous receipt reconciliation after restart.

## Review

High risk, all four lanes: general, architecture, scope, risk/compatibility.
No retained roster; installed catalog fallback Astra/xhigh/read-only selected.
Catalog digest ca26056cb57c0936f4430ceb0338f30fa147b73199eb1bc6caabd7c378e0edaf.

1. /root/provider_final_review reviewed the full initial branches and native
   source. Late children, v2 limits, stale goal activation, creation admission,
   CLI catalog/journal and plan-creation findings accounted for.
2. Native standalone review 01a14f04-27a1-7b52-9d34-1bb1b2dba8dd verified actual
   OpenAI Astra/xhigh/read-only settings. Corrected loaded archived descendants,
   unmanaged destination settings and restored draft catalogs; added queue-free
   goal proof. Report review-remediation-result.md.
3. Native standalone review 01a14f3c-1fe3-7510-9bb3-f7ca43f465ee verified the same
   settings and reviewed retained-creation/package admission. Blocking preparation
   window and Important CLI-journal reader findings fixed with focused regressions.
   Report review-compatibility-result.md. Whole history, one pin stream and no
   migrations accepted. Requested narrow corrections use skill step 9 without
   another confirmation review; later fork catalog correction stays within the
   reviewed destination-catalog/default-fork contract.

Replacement reason: earlier follow-up interface unavailable; standalone review
was ephemeral/unresumable. Reviewers remained independent/read-only. Long checks
used fresh installed-policy Luna/low utilities; when the current tool interface
lacked fresh delegation, the announced parent-monitoring fallback owned exact
commands/runs. All handles completed and final-head proof is preserved.

## Documentation and next action

Owning docs: dev-workspace docs/codex-providers.md, docs/dev-sessions.md,
docs/workspace-portal.md and README; codex-web README owns reusable contracts.
Main agent applied user-facing writing/humanizer guidance. Prepared deployment
instructions are not rollout evidence. Reusable lessons:
notes/dev-workspace/2026-10-18-scoped-provider-native-fixtures.md.

The user answered the scope question: temporary subagents may finish on the old
provider as long as all retained team members switch. Do not ask that choice
again or treat it as acceptance of the current blanket v2 refusal. Read-only
native source inspection confirms thread/archive closes the entire spawn tree;
v2 metadata restoration does not itself resume interrupted delegated turns.
Simply ignoring child provider mismatch would not preserve their work.

The user then explicitly instructed "proceed with implementation". The lead
implemented the additive experimental native thread/modelProvider/update and
retained-only worker. It persists future routing and interrupts only the exact
old source turn, using native replacement semantics to preserve goals and the
agent tree. Provider-specific model metadata follows future turns. Old temporary
children remain on their captured provider; new children inherit the target.
The scoped archive prototype and its fixtures were never deployed, released or
externally consumed, so they were removed rather than kept as an unused recovery
engine. Genuine deployed schema-1 workspace-wide recovery remains unchanged.

Focused Go tests pass (0.231s at that checkpoint); fixtures compile with the
native integration tag. New integration covers an actual saved direct-team
member plus old/new v2 children, queue/goal continuity and stable roster/policies.
It has not run yet. First native build failed on a missing Op::kind match arm;
the exact error was diagnosed and fixed. Evidence: native-live-build.{log,exit}.
Second native compile failed after ~25 minutes on the nonexistent
codex_protocol::error::CodexResult import. Corrected to Result as CodexResult.
Evidence: native-live-build-2.{log,exit}. Neither earlier build kept its failed
build directory. Third build uses --keep-failed, owned by fresh Luna/low utility
/root/provider_native_build_live_3 executing build-native-live-3.sh on patch
SHA256 27c528264b2ca4458ea116b50cedb86086e767e57fa8d0368eeb7b17c3ff2ba8.
Native inspection also found normal abort clears accepted unsampled input.
The narrow provider replacement now records that input through the native input
pipeline before clearing turn state. The actual-native fixture steers a unique
client-ID prompt into a plain busy turn and requires exactly one history entry.
This correction is not yet compiled or executed; focused worker tests pass.

Independent final review is running in resumable native session
01a14fa1-fc33-7fb2-97bd-93f01a2946bc with verified openai/Astra/xhigh/read-only
settings. Exact committed review head is b64afb0; packet/log are
review-inplace-packet.md and review-inplace.log. The pending import/input fix
requires reconciliation with its findings and affected-lane followup if needed.
Current installed utility/reviewer catalog digest is
bd3278a2715ea7377f94f9a2ef011b9c7cf0897994477222aa8f9760b7f59146;
watcher Luna/low and fallback reviewer Astra/xhigh remain unchanged. Rustfmt
1.95.0 is pinned from that Nix input. Scratch source edits live under
/tmp/provider-native-20261018.dmkzzfzq; only the generated owning-repo patch is
deliverable. No immutable store source or live native runtime was modified.

Next action: finish native compile, commit the input-preservation correction,
reconcile the running review, then exact-native and relevant package verification.
Keep lifecycle active and branches intact; merge/deployment approval is absent.

## User-directed removal of native patch

User: "are you patching codex? I don't want that, I don't want to keep rebuilding
it... what are we going to lose when we won't patch?" Followed by: "let the
subagents be stopped, it's not that important". This authorizes native tree
interruption during scoped provider switches and rejects the custom patch.

Parent canceled exact Nix PID 3704375 with SIGINT; watcher confirmed build 3
exited 1 after ~92 seconds, ending "interrupted by the user". It is canceled,
not a compiler failure, and produced no usable runtime. Builds 1/2 failed on
compiler errors as recorded. No patched native runtime was activated.

Final review report review-inplace-result.md is anchored to b64afb0. It found
Blocking retained-client routing, nested submission-loop callbacks, accepted
steering loss and crash recovery; Important reserved-turn/provider-catalog
races; Advisory stale archive prose. Its native-specific findings are resolved
by removing that implementation completely, not by asserting its correctness.
The stock worker always cold-resumes retained roots before continuing; native
metadata and actual per-thread HTTP endpoints will be checked. Its normal
interrupt semantics do not guarantee private unsampled native buffers; running
tools/questions and delegated child work can be canceled. Durable histories,
queue entries and goal ownership remain native-owned. Record this boundary
without reintroducing native patches or speculative buffer recovery.

Reused the former tested stock transition but deleted all child inventory,
provider migration, late-child reconciliation and blanket v2 refusal. The new
fixture contains a real retained roster member, a stopped v2 child, new child
inheritance and per-thread target HTTP requests. It compiles; native execution
awaits the relevant final review. Focused Go stock recovery passes in 0.688s;
eleven provider browser contracts pass. No native build is needed.


## Checkpoint before final stock-Codex handoff

---
lifecycle: active
---

# Provider switch redesign

Phase: implementation, quick checks, independent review and exact stock-native
verification complete. Both final feature heads are published; application
package/VM CI remains running. The user rejected a downstream Codex patch and
accepted temporary subagent stops. No native patch or build override remains.
No live activation, provider switch, deployment or merge occurred.

## Phase checklist

- [x] Session/default selection, optional creation selection and immediate progress.
- [x] Stock archive/resume transitions for every retained lead/member.
- [x] Remove child migration/refusal and all native patch/build changes.
- [x] Quick Go recovery checks, tagged compilation and eleven browser contracts.
- [x] Independent final review: no Blocking or Important findings; Advisory fixed.
- [x] Exact stock-native roster/child/goal/queue/per-thread endpoint proof.
- [x] Publish final feature heads; rebased shared-client CI passes.
- [ ] Final application package and archive/recovery/revival VM CI.
- [ ] Integration/deployment (not authorized; initiative remains active).

## Ownership and current branches

Initiative created by this conversation: 2026-10-18-provider-switch-redesign,
workspace /home/aither/workspace/ai/vpsfree.cz. It has no native lead or roster:
current finds none and team list confirms no valid lead. Do not create a
replacement or adopt another initiative. Lead owns design/application work;
only mandatory independent review and verification utilities were delegated.

Both worktrees/branches use the initiative slug:

- dev-workspace: worktrees/2026-10-18-provider-switch-redesign/dev-workspace.
  Base 705301228f726bcc9c5e0b516abc03f6f6c995cf. Clean published final head
  2b96a3f44569fd9f5e5bba01e1c2c94a3f2a8fe8. Complete cleaned series:
  6261dc0 dependency pin, d99f468 stock scoped backend, 3fce1c8 browser/docs,
  2b96a3f existing archive-VM reconciliation assertion.
- codex-web: worktrees/2026-10-18-provider-switch-redesign/codex-web.
  Base 56ec377d81e86951865068e1905b7726cff33ddd. Clean published final head
  c064ce09cfcea8d8af6bf676635a53cd823f772c (one additive interface commit).
- SSH remotes: git@github.com:aither64/{dev-workspace,codex-web}.git. Exact
  remote feature refs verified after final push. Default branches untouched.
- Shared coordination checkout remains master; initial tracking 03778c16.
  Tracking/evidence stays uncommitted under the usual daily/handoff cadence.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-provider-switch-redesign/

No migrations. Schema 2 is introduced directly; genuine deployed schema-1
workspace operations retain their engine. No intermediate scoped/native patch
was released, deployed or externally consumed. One consolidated codex-web pin
stream selects c064ce0 across URL/lock/Go checksums/vendor hash. No obsolete
native implementation, child engine or redundant pin history remains. Native
assembly/release selection/package tests/docs match upstream. Feature refs
retained; no PR, merge, archive, delete or session stop.

## Accepted implementation

See design.md and plan.md. The user's latest instruction accepts temporary
subagent stops and rejects downstream Codex patch maintenance. Use the unchanged
selected upstream native binary. Archive/unarchive closes and reopens only the
retained roots; native tree teardown can stop their children. Do not inventory,
migrate, reopen or verify temporary children. New children inherit the target.

Preserve thread IDs, persisted histories, durable native queue entries, model,
effort, policies, instructions, member environments and current native goal
ownership. Normal interruption can cancel running tools/dialogs and unsampled
native buffers; do not claim lossless hot migration or restored delegated work.
Correlated ordinary continuations inspect prior results before retrying actions.
Unrelated sessions, shared daemon/portal/tmux and clusters remain running.

Workspace defaults preserve explicit selections. Provider-specific catalogs
serve session/creation pickers and validation. Selection survives drafts,
preparations, CLI journals and exact-root binding. Scoped authorities/package
locks and creation admission retain concurrency/recovery protection. Progress
appears before inventory/auth/model checks with bounded concrete reasons. No
workspace-wide idle/ledger wait or child scan gates a scoped transition.

## Verification

Current quick proof (tree 2f32354a283f36aa99e9540bf829db7040e25d8f): focused
stock recovery worker checks pass (~0.65s); tagged native fixture compiles;
eleven browser provider contracts pass. git diff --check passes. Consolidation
preserved this exact tree. Native assembly, its tests and package docs are
identical to the base; there is no added native patch or compilation dependency.

New fixture contains a real retained member and v2 child, verifies child
interruption and saved history, new-child inheritance, per-retained-thread HTTP
target requests, stable roster/policy, native goal/queue continuity, idle state
and unrelated busy work. It has not executed on the final head yet.

Earlier stock-prototype evidence is retained separately: native four-root switch
~1.62s, actual Playwright creation ~9.47s, Ruby provider/creation 23 runs/230
assertions, CI 39133675250 (fast/package and archive VM) passed at 2bfc504.
https://github.com/aither64/dev-workspace/actions/runs/39133675250
These do not prove the new retained-member/v2-child fixture. Codex-web full
flake check and exact-head CI passed at unchanged 9e53d02:
https://github.com/aither64/codex-web/actions/runs/39123540992

Full old evidence and diagnosed failures: verification-result.md,
implementation-history.md and per-run logs/statuses. Native builds 1/2 failed
on compiler errors in the abandoned patch. Build 3 was deliberately canceled
with SIGINT at exact Nix PID 3704375 after the user rejected native rebuilding;
watcher confirmed exit 1 ~92s, no output/runtime and no running build. It is a
canceled attempt, not a compiler result.

## Independent review

High risk, all four lanes, installed default fallback Astra/xhigh/read-only;
no retained roster exists. Current catalog digest:
bd3278a2715ea7377f94f9a2ef011b9c7cf0897994477222aa8f9760b7f59146.
Resumable native reviewer 01a14fa1-fc33-7fb2-97bd-93f01a2946bc has verified
openai/Astra/xhigh/read-only settings. Retain it for related revisions.

review-inplace-result.md reviewed b64afb0 and unchanged codex-web head. It found
Blocking old inference-client routing, nested submission-loop deadlock, accepted
steering loss and cold crash recovery; Important reservation/catalog races;
Advisory stale archive prose. Its native-specific findings are resolved by
complete removal of the custom runtime. The stock native interruption boundary
is explicit; crash recovery cold-resumes retained roots before continuation.
Do not claim the rejected native implementation passed review or execution.

Changed-lane final review must inspect the stock strategy and cleaned complete
series, test coverage and accepted interruption boundary. Previous successful
reviews of the stock prototype are useful context, not its replacement.

## Documentation and next action

Owning docs: dev-workspace docs/codex-providers.md, docs/dev-sessions.md,
docs/workspace-portal.md and README; unchanged docs/codex-package.md describes
assembly; codex-web README owns reusable contracts. Main agent applied writing
and humanizer guidance to the revised child-interruption prose and dialog.
No rollout record exists because activation/deployment is not authorized.
Reusable fixture lessons: notes/dev-workspace/2026-10-18-scoped-provider-native-fixtures.md.

Next: finish changed-lane review; resolve findings; run exact stock-native and
relevant packaged checks through fresh Luna/low utility; publish consolidated
feature branch and monitor exact CI. No merge/deployment permission is implied.

## Rebased final stock candidate

Upstream advanced to dev-workspace 7053012 and codex-web 56ec377 (package-wide
execution policy). Rebased both features preserving it. Codex-web final c064ce0
is published; only README adjacency conflicted, both paragraphs retained. Its
code range-diff is equivalent and focused routing/settings tests pass. Runtime
final head 33072104068a7348028141d9bf04a6d190030ea4:

6261dc05c315eefffae83b5052bce1c3f7eac616 deps: pin codex-web session lifecycle interfaces
9dd91f20a269b052a0c53631552c64b60d6c1870 providers: switch retained session threads with stock Codex
86516ce939ad93fa6f285f1b63df2214d58e621a portal: expose session providers and immediate switch progress
33072104068a7348028141d9bf04a6d190030ea4 tests: await archive worker reconciliation after portal restart


The pin commit selects c064ce0 consistently; computed Go vendor NAR hash
sha256-xPhBkdvGlncxAlQPJqBmetL9AEU6A2SMjmrErV4114M=. One stream remains.
No native/package assembly changes were introduced. Earlier stock review was
interrupted for this rebase. It reported a Blocking partial-close intent loss
and Important stale goal ownership; both now fixed with focused regressions
(1.44s), folded into backend. Native fixture compiles with baseline-required
unmanaged package metadata. Final same-identity review uses
review-stock-final-prompt.txt; all worktrees clean.

## Final review accepted for isolated verification

review-stock-final-result.md completed all four lanes at 3307210 / c064ce0 with
no Blocking or Important findings. One Advisory requested binding the new-child
HTTP routing assertion to its actual thread ID. The lead made exactly that
test-only change, compiled the tagged fixture and folded it into backend.
Final dev-workspace head 125179050626c98f61342c0abb9440c10e720ed2; no production
code, contract or design changed after review. Skill step 9 permits focused
verification without another confirmation review. Complete cleaned history, one
pin stream, no obsolete native/child engine and no migrations were accepted.
Next: isolated exact-stock native run through a fresh verification utility.

Stock native attempt 1 failed before switching (1.34s): the manually prepared
read-only implementer fixture lacked Purpose and had incompatible access.
Production retained-policy validation correctly refused it. Corrected the
fixture to a complete reviewer0/review/read_only role, retaining the same idle
member scenario. Evidence native-stock-1.{log,exit}; no blind rerun or runtime
change. Published 1251790 triggered CI 39143658528 while native ran; after the
fixture-only followup publish, cancel this superseded run if still active.

## Stock native proof and final publication

The corrected exact-head fixture passed at
2b96a3f44569fd9f5e5bba01e1c2c94a3f2a8fe8. Native switch phase measured
2.613495962s; full Go test 4.042s (wrapper ~12s including environment setup).
It proves every retained lead/member target inference, stopped old v2 child
and readable history, new child identity-bound target inference, unchanged
roster/policy, preserved goals and queued entry (1 before/after), idle and
unrelated work, and unchanged shared daemon. Fake providers only; excludes
provider authentication/health and terminal quiescing. No live routing changed.
Evidence native-stock-final.{log,exit}; utility /root/provider_verify_stock_native_2.
Both post-review changes were narrow fixture corrections (Advisory child-ID
assertion and complete saved reviewer-role policy), folded into backend; no
production/contract changes require another reviewer confirmation under step 9.

Final dev-workspace branch published with exact-head force-with-lease from
1251790 to 2b96a3f. Final CI 39143904845 is in progress:
https://github.com/aither64/dev-workspace/actions/runs/39143904845
Superseded same-branch 39143658528 at 1251790 was still active. Parent tried
canceling it after verifying the head mismatch; GitHub returned HTTP 403,
Resource not accessible by personal access token. No token scopes were changed.
The exact current-head run continues independently. Shared-client final CI
39142745669 at c064ce0 already passed. No local package check duplicates CI.

Fresh standalone CI utility verified native identity
01a14fc9-f55f-7c22-948a-e96d4817a195, openai/gpt-6-luna/low, danger-full-access,
approval never. It owns only run 39143904845 via watch-stock-ci.sh. Parent
does not poll the same CI logs. Logs/status will be ci-stock-final.*.

Removed owned abandoned native scratch /tmp/provider-native-20261018.dmkzzfzq
(including its temporary formatter/build links) and disposable Go-vendor trees
/tmp/provider-stock-vendor-20261018 and /tmp/provider-switch-vendor.kGghj9.
No Nix store paths, live processes/services, worktrees or feature refs removed.
Native fixture homes clean themselves after both failure and success.
