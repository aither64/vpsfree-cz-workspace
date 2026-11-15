# Archive failure investigation and proposed repair

Packages A/A2, architect0, 2026-11-11. Investigation accepted; the user's later
"implement it" direction authorizes the bounded implementation below. A2
reconciles the brief against fetched upstream and releases sufficient design
boundaries for lead-assigned C and D. Recovery of the two named sessions remains
prepared only; no archive, stop, monitor resolution or deployment is authorized
by these packages.
Operational observations and exact receipt identities are in
[findings-runtime.md](findings-runtime.md). No application edits, lifecycle
retry, service stop, long checks or commits were performed by this package.

## Evidence and root causes

The selected profile and running portal use
`/nix/store/9hr3ppqzzwb12x51vwjasw8hq0ka7dab-dev-workspace-0.2.0`.
Its derivation
`/nix/store/laq7gxhg6cv91cyv873fskhcl9sx07xf-dev-workspace-0.2.0.drv`
identifies exact source
`/nix/store/pfnyfqh3z37g4dpqq3pw04qhdgg98d55-source` in `env.src`.
All source references below are relative to that immutable source. Canonical
bare repository HEAD differs; no Git revision is asserted for the installed
source or the package running at the November 3 failure.

### Preview: a terminal report incorrectly retains an external-work fence

The archive request for `2026-11-10-status-theme-responsive-preview` failed at
2026-11-11 13:30:18 UTC after three repair rounds without progress. Its sole
blocker names monitor `7648d2bf-a2b9-493e-8bcf-c1a69d8fc1a0` as retaining external
work. The monitor's terminal report is `failed`, exit 1, conclusion `cancelled`,
but its `stillRunning` field contains:

> none; observation session 68962 exited 1; GitHub run 42816255766 attempt 1 is terminal completed/cancelled

`portal/internal/monitoroperation/service.go:245` (`HasUnresolvedEffects`)
treats **any nonempty** terminal `stillRunning` value as unresolved effects.
`validateReport` at line 94 permits this combination.
`portal/internal/monitoroperation/lifecycle.go:142` rejects archival on that
fence before proving native quiescence. `libexec/dev-session:9404` calls it
from archive readiness; `libexec/workspace-archive-check.rb:53` returns the
failure as a conversation blocker. The preparation's three-round cutoff at
`portal/internal/web/archive_preparation.go:583` then makes it terminal.

This classification is proven by the exact persisted report and code. A fresh
GitHub read independently proves run 42816255766 attempt 1 and job 129830005698
are completed/cancelled at head `9958b0375eb4d7c655cdc505a76e46ec95301cd4`.
The utility has a recorded completed termination. The historical local tool
session 68962 and all possible operation-owned cells were **not independently
reconciled** in this investigation. Therefore the report-format defect is
proven, while unconditional permission to clear the existing fence is not.

### Release: transient session contention permanently fails preparation

The request for `2026-11-02-haveapi-vpsadmin-release` has remained failed at
attempt 1 since 2026-11-03 14:10:17 UTC. Its saved error is
`session is changing: resource temporarily unavailable`, after one accepted
repair delivery. This is before the archive worker started.

`portal/internal/web/archive_preparation.go:384` obtains a nonblocking shared
session lock. `portal/internal/session/authority.go:106` wraps flock contention
as that error. Preparation's error path at lines 426–433 writes `failed`;
the delivery loop only retries native unknown-send/transport errors, so session
contention falls through to failure. `active()` at line 81 excludes failed
preparations, and restart recovery at line 305 skips them. The ordinary browser
Retry endpoint is the path back into execution (`portal/internal/web/server.go:3474`).
This explains the persisted failure and the current lack of continuation. The
historical lock holder and exact historical executable remain unknown.

The preceding readiness result legitimately identified 2,712 unmanaged entries
under `haveapi-rust-source`; the saved 128 examples include `.editorconfig` and
`.git/` entries. `libexec/workspace-archive-check.rb:48` discovers canonical
worktrees with `clean: false`; `libexec/workspace-archive-cleanup.rb:629` refuses
loose files/symlinks outside recognized checkout roots. Explicit archival may
discard uncommitted content **inside verified checkouts**, but does not infer
ownership of arbitrary adjacent repository-like content. Fixing lock handling
alone does not establish that this request can finish. Its present layout and
whether its accepted repair already changed it were not inspected.

### Why services survived and timers did not help

Both records failed in `lead_fixing_blockers`. Neither has an archive journal,
cleanup sidecar, services-cleanup prelude, matching archive worker or pending
tracking-sync receipt. `portal/internal/web/server.go:3365` requires preparation
success before `runSupervisedArchive` can start. The worker is therefore not
the failed component in these cases.

Fresh CLI archival repeats readiness at `libexec/dev-session:2125`, then native
quiescence and inventory checks, before registered service cleanup at line 2193.
`libexec/workspace-session-services.rb:527` retires the frozen registered set;
lines 750–790 require settled jobs, terminal state, recursive cgroup emptiness
and transient-unit unload. Supporting-file removal follows verified cleanup.
The preview was correctly registered: at 18:44 UTC all 12 current registered
services were running with `cleanup: null`; port 4567 matched the registry,
systemd invocation and cgroup. No stop had been attempted.

Automatic archival resumes only its own operation records
(`libexec/workspace-auto-archive.rb`, `auto_archive_scan_session` and
`auto_archive_resume`); it does not adopt a failed explicit browser preparation.
Tracking-sync retries only tracking Git bookkeeping. Neither timer is a general
archive-request retry mechanism. The apparent retry promise therefore ends at
the preparation failure boundary.

## Smallest proposed changes

1. Keep a confirmed preparation active during transient lock contention. Handle
   typed `EAGAIN`/`EWOULDBLOCK` at admission, release all admission locks, record
   a visible waiting reason and retry with bounded, interruptible backoff under
   the **same** receipt, operation and repair-message identity. Do not consume
   repair/no-progress rounds while waiting. Existing active preparation states
   and restart recovery can provide durability without a new scheduler or
   persistent format. Recheck generation, exact target and cancellation on every
   admission. Retain permanent refusal for identity/content/ownership failures.
2. Validate newly accepted monitor reports: terminal `passed`/`failed` requires
   an omitted or empty `stillRunning`; actual unfinished or uncertain effects
   require `incomplete`. Put completed-work evidence in `detail`/`evidence`.
   Update the utility instructions and validation error to say this explicitly.
   Keep conservative fence semantics; do not parse English phrases such as
   `none` to authorize lifecycle changes.
3. Present hard blockers as an actionable hold on the accepted request, including
   the exact blocker, last check, required owner action and whether registered
   services are still running. Retain the three-round limit on model repair;
   avoid repeating unchanged repairs indefinitely. Distinguish waiting for
   session access from operator/evidence action, and preserve Retry/Cancel.

Preserve current shutdown ordering in this minimal fix. Service cleanup must
still precede supporting-file deletion, while unresolved external effects and
unproved ownership must not be bypassed to make Archive look successful. Moving
service shutdown ahead of all readiness checks could stop dependencies of work
whose effects are still unknown. Such early shutdown would need a separately
settled dependency/authorization contract; it is not required to fix either
proven defect. Show the pending cleanup plainly instead.

## Compatibility and proposed recovery

No database, network protocol, client generator, Terraform, NixOS node or
cluster-schema change is proposed. Existing archive modes, journal schemas,
sealed recovery contents, service identities and exact-final-head rules remain
unchanged. This is the user-profile application, not a system-pin deployment.

Monitor compatibility needs care: `validateOperation` calls `validateReport`
for retained events (`service.go:207`), and `AddEvent` currently validates before
checking exact replay (`service.go:129`). Do **not** simply tighten the shared
reader and make the offending historical record unreadable. Apply the stronger
invariant only to new event acceptance; continue reading and exactly replaying
old immutable reports under their original contract. Old reports keep their
fence until the existing evidence-resolution path succeeds. No rewritten event
or substring migration is needed. New preparation fields, if implementation
finds them necessary, require an explicit compatibility review because its
schema-1 reader rejects unknown fields; reuse existing active states first.

Recovery remains a proposal requiring explicit authority in the affected session:

- Preview: its own lead must account for the exact source, historical local
  session 68962 and every known operation-owned cell/session; then use the
  existing immutable monitor `resolve` acknowledgement with exact evidence and
  native quiescence proof. No blind resolution, event edit or rerun is needed.
  Retry the original accepted archive after the fence is legitimately resolved.
- Release: its owning lead checks whether the recorded unmanaged content still
  exists and proves its ownership/purpose. Preserve unknown contents; relocation
  outside the managed worktree group is safer than deletion. Placement inside a
  verified owning checkout is appropriate only when its explicit discard policy
  is intentional. Fresh readiness must pass before archival. Retry the same
  browser receipt, reconciling its already accepted repair delivery rather than
  sending a duplicate. Lock handling alone cannot clear content blockers.
- For both, success means verified retirement of all registered services, then
  ordinary tracking/worktree/runtime completion. No supporting files may be
  removed while shutdown is uncertain. Keep original receipts and recovery
  policy; never clear private files to force eligibility.

No deployment or package transition was prepared or performed. A future rollout
uses the selected package's coordination/recovery procedures, preserves retained
records, and verifies disposable archive/revive behavior before any authorized
recovery of these sessions. Forward recovery remains the installed package policy.

## A2: implementation release against fetched upstream

Identity and live same-session roster reverified. Implementation baseline:
`origin/master` = `6587c4c1cedabee95bcc52f4667e7d33e3a82859`, with canonical
repository `FETCH_HEAD` refreshed at 2026-11-11 19:54:49 UTC. Twenty relevant
files are byte-identical to the investigated immutable source: AGENTS/README,
preparation and tests, operation state/store, server/worker, session lock helper,
monitor service/launch/lifecycle, archive CLI/check/services, session/recovery
docs, monitoring skill and packaged archive lifecycle VM. No upstream drift
changes the root causes, interfaces or compatibility constraints above.

C and D have sufficient briefs for independent implementation; no unresolved
historical evidence blocks these code changes. Historical lock ownership,
unmanaged contents and monitor tool-session effects remain blockers to claiming
live recovery, not to fixing the proven contracts. Lead retains package
allocation, release acceptance and shared Git/check-output scheduling.

Settled implementation interfaces and invariants:

- C retries only positively typed lock contention at preparation admission.
  Preserve the existing active preparation state, receipt/attempt/journal/target
  identity and accepted repair delivery. Release locks before each interruptible
  wait; do not increment model-repair or no-progress counts. A restart resumes
  the same preparation; cancellation and changed target/generation stop further
  work. Do not convert every timeout/error into a retry or enroll old failed
  receipts by matching their English error text.
- C uses existing lifecycle and service projections for status. Label hard
  blockers as requiring attention, identify the blocked phase/action, and show
  that service cleanup has not started or is pending when supported by evidence.
  Unknown/unavailable service status must stay unknown. Reuse existing controls,
  styles and Services navigation; no new lifecycle journal or status framework.
  Keep the existing hard-blocker repair bound and the shutdown ordering above.
- D keeps original validation for retained reads and legacy event replay. Apply
  the stronger terminal-report invariant only when admitting a new event after
  proving no identical historical event already occupies its slot. Preserve
  source-result requirements, exact reporter/owner/epoch checks, immutability,
  conflict rejection and the conservative unresolved-effects fence. New terminal
  success/failure requires exactly empty/omitted `stillRunning`; whitespace or
  `none` prose is not an absence proof. Incomplete remains fenced even when its
  field is empty; existing evidence-bound resolution remains unchanged.
- No persisted schema change is needed for either package. If implementation
  discovers one is required, report the consequential change through the lead
  before writing a new format. Preserve predecessor readers and recovery policy.

Ownership is explicit: C owns archive preparation/status/UI and
`docs/session-archive-recovery.md`; D owns monitor implementation/tests,
`skills/dev-session-monitor/SKILL.md` and the monitor section of
`docs/dev-sessions.md`. Other shared documentation or fixtures require a
lead-owned edit window. C and D must not edit each other's files. Routine
clarification goes directly to architect0; consequential deviations and
ownership conflicts go through the lead. Neither package mutates live receipts.

## Released packages and acceptance

| Package / owner | Files and deliverable | Acceptance, checks and evidence |
| --- | --- | --- |
| C / implementer0 | `portal/internal/web/archive_preparation.go`, relevant operation/server/status/UI and focused tests; session lock helper only if necessary; archive recovery docs | Exact accepted request waits through transient contention, restarts and cancellation without duplicate repair or worker launch; hard blockers and pending/unknown service cleanup remain visible. Focused Go/browser tests cover contention before/after accepted repair, restart during wait, cancellation, changed target and three-round repair bound. |
| D / implementer1 | `portal/internal/monitoroperation/{service,launch}.go`, monitor report/store/lifecycle tests; monitoring skill and monitor section of session docs | Reject new terminal success/failure with nonempty `stillRunning`; accept terminal cancellation with empty field; preserve incomplete fences, persisted legacy reads/exact API retries, conflicting-slot rejection and evidence-bound resolution. Include the exact historical report shape. |
| E / lead assigns after C+D acceptance | Existing packaged lifecycle regression and verification evidence, no new framework | After committed changes, quick checks and independent review, use the runtime-owned watcher for existing `session-archive-lifecycle` VM and applicable package checks. Verify registered service descendants/unload before file removal, stop failure retaining files, preparation contention/restart and unrelated-session availability. Deployment and live recovery are separate authorization. |

Quick verification uses the repository's Nix environment, focused Go tests with
explicit `-mod=readonly`, and the existing browser harness for C's visible status
changes. Run the smallest regression that exercises each actual failure; then
the relevant package quick checks. Long/uncertain checks require the monitoring
skill and follow independent final review. Each implementer reports exact
base/head, changed files, commands/results/gaps and whole-branch/migration
provenance; no migrations are intended. The lead applies the user-facing writing
skill to UI/skill-facing prose as applicable before commit and owns final review.

No tests were executed by A/A2; investigation used source-to-runtime correlation,
and A2 checked source equality. Product docs accompany implementation. Routine
findings/design do not trigger automatic review. The lead owns tracking and
acceptance; A2 is ready for acceptance, with C and D safe to execute independently.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/).

## A4: sufficient paired-pin package for authorized aitherdev deployment

The A4/A5 heads below are retained checkpoints. **A8 supersedes the A7 wait with
sufficient G2/F2 briefs against settled defaults.** The built A6 pair must not
be activated. Lead owns mutation windows and execution release.

The user subsequently authorized deployment to aitherdev through
`vpsfree-cz-configuration`, with integration after verification. The complete
reviewed/published runtime is
`79700e46361543dbc399647a218671d7ad4b55e1`; final CI
`43101129602` attempt 1 passed at that exact head. Reuse its recorded independent
review and verification rather than repeat completed runtime development.

**F's initial mechanical pin preparation was released**, owned by implementer0.
**A5 settles the composition:** the user chose the default/removal route, so F
resumed unchanged and completed both commits. No deployed image/demo commits are
imported and no extension-master integration is in scope. Build/deployment still
follow the reviewed-source and ownership gates in rollout.md. Source/file
boundary: this session's workspace feature `flake.nix` direct nested runtime URL
and generated `flake.lock`; this session's configuration channel-owned generated
runtime lock change (plus only metadata generated by its normal confctl command).
No application edits, extension updates, Codex upgrades, provider changes or
machine mapping changes. Initial bases: workspace
`709195156084edb345ca1401cc61a2c564223d7d`; configuration
`dda57166bd8bb6d85a74decdd05a8810933bdecc`. Lead owns any integration/rebase change.

Settled F interfaces, execution and acceptance:

- Set `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` to exact runtime
  `79700e46361543dbc399647a218671d7ad4b55e1`, then generate the workspace lock with
  `nix flake update vpsfree-dev-workspace/dev-workspace` in its feature worktree.
- In the configuration Nix shell use
  `confctl inputs channel set --commit dev-workspace devWorkspace 79700e46361543dbc399647a218671d7ad4b55e1`.
  The channel role maps to input `devWorkspace`. Keep its generated commit
  message and declared Overcommit hooks; prepare environment/trust before commit.
- Both old runtime selections are `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
  The initial fetched-base comparison preserved extension
  `0c7168f352f6d4f11c46368e702b9356d81012c6`, content hash
  `sha256-hhWrvLJFedS3B6Yd55gPcUQmyhChYMvxABg7yVRWGLw=`, all sibling input
  identities and semantic follows paths. That extension is older than the live
  profile; A5's explicit removal choice now accepts this selection. Inspect
  complete before/after locks,
  not only node names. No manual lock edits or incidental dependency cleanup.
- Run `bin/check-dev-workspace-deployment --workspace-root WORKSPACE_FEATURE_ROOT
  --configuration-root CONFIGURATION_FEATURE_ROOT` on the final pair; run
  declared hooks/format checks and focused pin/contract checks. Report exact
  commits, final diff, complete lock identities, quick results and hook evidence.
  Consolidate one final update per pin stream; whole-branch history remains
  reviewable even for mechanically generated changes.
- F owns both feature worktrees and their edit/commit windows; it does not touch
  shared master content, acquire claims, activate systems/profiles, merge, or
  mutate the two affected sessions. Architect0 owns this design and rollout.md;
  lead owns tracking, approval interpretation and final review/check scheduling.

Pin implementation is independent of the remaining operational dependencies:
build/copy artifacts, deployment gates and recovery evidence belong to the
[rollout record](rollout.md). Ordinary profile switch must preserve selected
generation and all pending-operation/monitor/guest-process refusals. Outstanding
source/poller effects recorded in state must be reconciled through their original
contract before any transition they block; no false resolution or lifecycle
cleanup is authorized here.

The composed user profile depends on workspace feature content as well as the
runtime/configuration commits. A5's lead assignment records the selected scope:
runtime, configuration and workspace `master` integration after verification.
No extension-master merge is included. No merge or machine claim is acquired
by A4/A5/F.

### A4 deployed-lineage evidence; A5 selected default route

Read-only provenance proves that the selected profile contains extension
`c1b421c1fe47d9cbe7a5d31ab67749c8826f4dfa`, not the fetched workspace base's
`0c7168f`. Offline evaluation of immutable workspace source
`/nix/store/qzil247mgz63nnq4l12gm3jwl31fgi8l-source` reproduces the exact selected
package derivation. The running system reports clean configuration revision
`799edd140a60b1f861bf7f1b30bcb495bf413129`. Fresh SSH remote-default checks and
canonical ancestry tests prove both feature heads are unintegrated:

- Configuration live-only range
  `3c088a4b71881b3649441ce3c4e92c71757708e6..799edd140a60b1f861bf7f1b30bcb495bf413129`
  contains two commits adding the development image repository and its images
  hostname. Default `dda57166bd8bb6d85a74decdd05a8810933bdecc` contains unrelated
  status, DNS and syslog changes; it does not deliberately remove/supersede the
  deployed feature.
- Extension live-only range
  `0c7168f352f6d4f11c46368e702b9356d81012c6..c1b421c1fe47d9cbe7a5d31ab67749c8826f4dfa`
  contains three commits adding the optional image demo, synthetic fixtures and
  schema-3 fixture support. Default `cdeb36a748acf1cd1ff1bab8fc8edce60966ec6f`
  adds review guidance and does not supersede those features.

The A4 preservation proposal was not selected. In the user turn relayed by lead
in A5, the user said: "it’s ok to remove it... the responsible session will work
after you and bring it back". The selected result is the default-based pair:
remove the host image front door/certificate-service configuration and optional
demo/fixture capability from this deployment, without importing either live
feature range. This does not authorize guest access, data resets, session
archive/retry/stop/resolve, or registered-service cleanup. Restoring the feature
belongs to the responsible session later, with its own deployment ownership.

Final F pair: configuration `8cb800aaa382c9d2f46532c7a5ad7d883546ef8f` on
`dda57166`, workspace `c96a15b5d2d935c2476c8da6216218b46d3a14cb` on `70919515`.
Both are clean; the final locks match the passing paired-check evidence. No
system/profile candidate has yet been built or activated by these packages.

A5's bounded static comparison of extension `0c7168f..c1b421c1` found only
optional demo Nix composition, explicit fixture helpers, tests and docs; its
flake change adds a test invocation. The schema-2/3 check belongs to
`dev-clusters/vpsadminos/lib/image-repository-history.rb:106`, an explicitly
invoked offline fixture helper, not a mandatory package-state reader. Provider
state/transition readers and generic lifecycle/monitor/service schemas are not
changed by this extension range. There is no demonstrated reader incompatibility
from omitting it. Ordinary `workspace-host switch` still validates candidate
cluster contracts/providers and retained state through supported admission
(`libexec/workspace-host:3046` at runtime `79700e4`); do not manually invoke its
internal helper or inspect peer guest data. `workspace-host status` and
`workspace-host maintenance status` are the smallest ordinary status checks;
they are observations, not substitutes for switch admission.

Exact graph hashes, final commands, deployment/recovery gates and minimum live
verification are in [rollout.md](rollout.md). No peer records/worktrees/transcripts
were accessed and no cross-session communication was used. A4/A5 perform no
application edits, builds, claims, merges or lifecycle actions.

## A6: sufficient mechanical refresh brief for G and dependent F

**G is sufficient to execute now**, owner implementer1, with lead release.
Owner/file boundary is this session's registered `dev-workspace` feature branch
and worktree, retaining the complete two-commit archive/monitor feature. No new
behavior, migration, input, contract or repository scope is authorized.

Fresh canonical runtime `master` is
`02881b401955ff0db71bb74f6fb84f6e475a7879`. The reviewed head
`79700e46361543dbc399647a218671d7ad4b55e1` is not its ancestor; common base is
`6587c4c1cedabee95bcc52f4667e7d33e3a82859`. The old feature range contains exactly
`3a0af7ad6b97ae4a3a7e38921beac8a2cdf9ff54` (new monitor reports) and `79700e4`
(archive contention/status). Upstream adds only `02881b4` (repository comparison
metadata loading). The only file changed by both ranges is
`portal/internal/web/static/app.js`: upstream changes repository-review asset
`v=9` to `v=10` near old line 4021, while our hunks are near old lines 904–927.
No overlapping behavior or schema/input change was found. A clean rebase is
expected, not asserted before execution.

G deliverable and stopping rule:

1. Preserve the exact old reviewed head/range with a retained ref. Confirm clean
   own worktree and fresh runtime default; refresh the entire two-commit series
   onto exact `02881b4`. Keep both features and upstream metadata behavior.
2. Record new exact base/head, `git range-diff` for
   `6587c4c1..79700e4` versus `02881b4..NEW_HEAD`, ordered stable patch IDs, final
   diff and unchanged runtime input/contract hashes. Preserve old CI/review
   evidence as old-head evidence. No intermediate pin or obsolete feature commit
   is required in the final range. There are no feature migrations.
3. Any conflict or manual behavior change stops for lead/design assessment;
   do not infer equivalence, discard upstream changes or expand the fix. The
   existing three-target integration approval covers a proven equivalent refresh.
4. Run repository Nix-environment quick checks: the accepted C focused archive/
   lifecycle selector, D's full `./internal/monitoroperation` tests with
   `-mod=readonly -count=1`, existing browser contract unit invocation with its
   actual pinned conversation module, `node --check` for the changed application
   script, and `git diff --check`. Use recorded working invocations in
   implementation-c.md/package-d-evidence.md. Check package history/docs and
   preserve the reviewed 60-second prearmed archive hydration assertion.
5. Report exact new head, equivalence, checks/gaps and complete history/migration
   conclusion to lead. Lead applies independent review/equivalence rules before
   long verification. Fresh CI on the new head must cover the existing fast
   checks (including upstream repository metadata/browser regressions) and
   archive/creation jobs under the unchanged workflow. Reuse prior diagnostics;
   do not claim old-head CI is a new-head result or add unrelated host tests.

**Dependent F refresh**, owner implementer0: independent read-only/preparation
may use fresh configuration `5dcde1ce5210a42e4499dbf1b6badbd1f0aa326c` and
workspace `42c76e8cb61e0d2063a3d25b4b448e66abee523f`. Wait for G's exact reviewed/
published final runtime revision before selecting it through the existing confctl
channel and direct nested workspace URL. Preserve extension `0c7168f`, all other
nodes/follows and current defaults. Regenerate locks normally; consolidate each
pin stream to one final update and repeat hooks/complete-graph/paired checks.
Old F `c96a15b5`/`8cb800aa` remain checkpoints and must not be deployed as-is.
F owns workspace/config edits; G owns runtime edits; no shared edit window exists.

Refreshed F completion report selects runtime
`43085d5d5ac1bfc8dbca48a809c2162acf8e0e74` in workspace
`7778d49bff929c9a0c36d7529b4bc1dda66f91c7` and configuration
`32b32945fb0ede6f4851b630924928e91a15bb8a`, on the A6 bases above. Each has one
final pin commit, clean worktree, unchanged sibling/follows graph and passing
paired checker. Exact lock hashes and review/build status are in rollout.md;
no build or activation is implied by source completion.

The live baseline has independently advanced to runtime `02881b4`, profile 232
and configuration `5dcde1ce`; it already selects extension `0c7168f`. The approved
default/removal product choice is unchanged, with no new image-feature import or
removal work. New live paths/graphs and old/new ranges are in rollout.md. No
build/claim/activation is authorized by A6; the lead resumes those later under
the existing rollout gates. No peer records, transcripts or worktrees are needed.

## A7: built candidate held for a concurrent live feature

R3/G accepted runtime `43085d5d`, R4/F accepted workspace `7778d49b` and config
`32b32945`; the lead reports their system build/copy and composed-profile build
completed. Fresh CI `43267182066` continues independently. A7 performs only
read-only canonical/live-metadata reconciliation and updates these records.

The live system now reports clean configuration
`f74dd69e590eb53e79743eed70ca9224e852b3af`, selecting runtime
`4dd6c7577c4e6c6f607f07c5227b553f17975cce`. Profile 233 selects that same runtime
and extension `0c7168f`. Fresh defaults remain runtime `02881b4`, config `5dcde1ce`,
workspace `42c76e8` and extension `cdeb36a`. Live `4dd6c757` is one feature commit
above `02881b4`, not its ancestor; our `43085d5d` and live `4dd6c757` diverge at
`02881b4`. Live config is one runtime-pin commit above `5dcde1ce`, also unmerged.

This is substantive new behavior: automatic repository overview/file line
counts, backed by an additive endpoint and existing comparison cache. It is not
equivalent deployment metadata. Only `portal/internal/web/static/app.js` is
changed by both feature ranges; live changes the repository-review asset URL
`v=10`→`v=11` near old 4021, separate from our archive-status hunks at 904–927.
Live/prepared runtime, claim, machine-claim, machine-policy and package descriptor
JSON are equal. Lock graphs differ only in the runtime node; the nine-node
runtime dependency graph is unchanged. These establish unchanged declared
compatibility, not content equivalence or permission to remove the new feature.

Lead's authoritative snapshot identifies held aitherdev claim
`faad7680-b349-4d27-8876-e23e5ab55893`, label "Deploy automatic repository line
counts", source `f74dd69e`. A7 does not duplicate ownership checks, contact that
session, inspect its data, or activate around its claim. The user's earlier
removal choice concerned the image/demo feature, not repository line counts.

Smallest safe next path: retain the completed artifacts and continue existing CI;
wait for the holder's verified deployment/default integration and release. Then
perform one bounded default/live check. If that feature becomes the settled
default, lead may release a mechanical refresh of our same two commits and
dependent pins, preserving it and the accepted archive behavior. Prove old/new
ranges and patch equivalence, rerun affected C/D/browser and paired-graph checks,
apply review/CI rules to the exact successor, and rebuild/copy only changed
artifacts. Any manual behavior conflict returns to lead. A7 itself releases no
rebase, import, new implementation, build or claim. No new product question is
needed merely to wait; dropping the new feature would require a separate scope
decision. Exact old/new source graphs, paths and holds are in rollout.md.

## A8: sufficient G2/F2 implementation brief

**G2 is sufficient for lead release now**, owner implementer1. Refresh the exact
two-commit runtime range `02881b401955ff0db71bb74f6fb84f6e475a7879..43085d5d5ac1bfc8dbca48a809c2162acf8e0e74`
onto settled default `db4b0fa62633b925e1917ec880737e1776f82cc8` in this session's
owned runtime worktree. Retain old refs/review/CI/build ranges, including original
`6587c4c1..79700e4`. Do not add behavior or change inputs/contracts/migrations.

The new default preserves automatic repository counts and adds `--full-index`
to immutable-blob Git diff. It is not literally merged/patch-identical `4dd6c757`,
but the current live system/profile now select exact `db4b0fa6`. Our `43085d5d`
is not its ancestor (common `02881b4`). Only shared changed file is `static/app.js`:
upstream asset `v=10`→`v=11` near 4021 versus our archive-status hunks near 904–927.
Declared state/claim/machine/package contracts and dependency graph are unchanged.

G2 preserves both archive/monitor patches, new baseline behavior, old reads/exact
replay and the reviewed 60-second prearmed browser assertion. Deliver exact
base/head, retained refs, whole-branch two-commit history, `range-diff`, ordered
stable patch IDs, upstream-delta comparison and explicit no-migration/unchanged
input-contract proof. **Any conflict or manual behavior change stops for lead**;
do not infer equivalence or drop upstream changes.

Quick checks use the declared Nix environment: accepted C archive/lifecycle
selector, D monitoroperation suite, existing browser contract unit invocation
with its pinned conversation module, application syntax and `git diff --check`.
Include existing repository Go tests for the new baseline's counts/blob-diff:
`go -C portal test -mod=readonly -count=1 ./internal/repository`. Use the monitor
skill for uncertain/long checks. No new framework or unrelated test expansion.

**F2 interfaces are sufficient**, owner implementer0. Configuration base
`55b83513b863c704c845e65e956b8230482f173e`; workspace base
`3bdad4b138a346482e98be906660f8526020835b`. Independent preparation can start;
final pinning waits only for G2's accepted/published exact runtime head. Own only
workspace direct nested runtime URL/generated lock and config's existing confctl
channel-generated lock/history. Preserve extension `0c7168f`, every sibling,
root/follows path and channel mapping. Regenerate through the existing commands;
one final pin commit per repository. Retain `7778d49b`/`32b32945` as build
checkpoints, not redundant final pin commits. Repeat hooks, full-graph semantic
comparison and paired checker. G2/F2 have disjoint repository ownership.

Minimum review/reuse: installed mandatory-change-review permits certified
mechanical refresh only with its schema-1 accepted-review receipt and independent
tree reconstruction/generated-pin verification; it excludes substantive baseline
changes, migrations, conflicts or unproved scope. New counts behavior is a real
baseline change from R3's `02881b4`: retain unchanged feature review evidence but
require applicable independent affected-lane composition/history review after
quick checks, without repeating unaffected review. Pure generated F2 pins may
skip standalone content review when proved mechanical; whole-branch history,
consolidation and deployment compatibility remain required.

CI `43267182066` passed fast/archive/creation at `43085d5d` at 17:49:18Z. Retain
it as exact-old-head evidence. Verification/artifact reuse separately requires
exact derivation **and input** identity, not patch IDs. After quick checks and
applicable review, satisfy final-head fast/archive/creation under the unchanged
workflow, reusing only specifically proven identical verification derivations.
Rebuild/copy changed final system/profile artifacts before fresh machine ownership.
No new product question, extension merge, source scope, lifecycle action or
automatic activation is added. Three approved master targets and ordinary
exact-final-head completion remain; lead owns mutation windows and execution.

## Bounded CI remediation: maintenance caller observes worker exit

**Sufficient for lead acceptance/release**, proposed owner implementer1. This is
a narrow runtime correction discovered by CI, not another mechanical rebase.
Owner/file boundary: `libexec/workspace-maintenance.rb` and
`test/workspace_host/maintenance_test.rb` in the owned runtime worktree. Preserve
all other feature/source/deployment decisions. No implementation begins on this
brief until lead releases it.

At reviewed runtime `e1c67dbee3188df9dc7c37fa1d1e724515530fea`,
`start_maintenance_switch` first inspects the operation and handles terminal
phases, then observes systemd ActiveState; any state other than active/activating
immediately raises the recovery-required error. The operation can complete and
the worker can exit between these reads. This race is demonstrated by source.
The same-operation CI evidence strongly supports that interleaving: journal
`/tmp/session-archival-ci-43280290315/maintenance-journal.txt:115` onward shows
worker 45178 finishing for `8403a093-2544-466a-aa72-a3834d3f651a` while caller
44607 exits 1 requiring recover at 19:00:57. Implementer reports the durable
operation complete/restoration/continuations settled and worker-success VM
assertion passed. The precise interleaving was not instrumented; a deterministic
fixture must reproduce it before claiming regression coverage.

Smallest change: after observing a stopped/non-active worker, perform one fresh
ordinary `inspect` of the **same operation UUID**, and reuse the existing
complete/cancelled handling before declaring recovery necessary. Complete still
prints that operation's candidate package and returns success. Cancelled retains
its existing cancellation versus source-recovered/not-applied messages. A fresh
nonterminal record still raises the existing recovery-required refusal. Preserve
ordinary inspection errors; do not infer success from service exit alone.

Invariants: one accepted operation, unchanged source/claim/profile/generation
admission, no new activation, worker restart, recover action, retry schedule,
deadline, journal/schema conversion or native-fence change. Terminal record
semantics remain authoritative as in the initial inspection path. Do not weaken
the VM assertion, lengthen its deadline, add sleeps, or rerun unchanged long CI
as a substitute for proving this race.

Acceptance/quick checks: use the existing maintenance host fixture to force an
initial nonterminal inspection, stopped-worker observation, then terminal
inspection. Demonstrate the complete case fails on old code and passes with the
fix. Also cover stopped+fresh-nonterminal refusal and fresh cancelled handling,
including the source-recovered outcome. Assert every inspection uses the original
UUID, with no extra prepare/start/recover/activation effects. Existing active/
activating polling and initial terminal paths stay intact. Run Nix-environment
Ruby syntax, deterministic cases, the relevant maintenance test subset and diff
checks before broader verification; monitor uncertain/long commands under policy.

Review/rollout: record this as a separate functional correction with exact final
history and no migrations, preserving prior e1 review/CI failure and reproduction
evidence. Lead applies affected independent host/compatibility review after quick
checks, before the necessary packaged creation/maintenance VM rerun and final-head
workflow. This changes runtime/package identity: downstream F pins and prepared
artifacts must select the accepted published successor, with their normal graph/
hook/pair checks and review policy. Old successful jobs remain exact-head evidence;
reuse requires actual verification derivation/input identity. No live maintenance
recovery, session lifecycle action, build or activation is authorized by this
design assessment. Lead owns release, dependent packages and execution windows.

Compatibility: retained maintenance operations keep their original source-package
owner and recovery contract. Installing a corrected target does not retroactively
replace an older caller or worker. A caller error must be reconciled against its
exact original operation/status before deciding what happened; this fix adds no
automatic recovery and grants no permission to invoke recovery on live state.

## A10: HaveAPI activation refusal after the authorized archive retry

**Diagnosis and supported-action guidance only; no implementation package.**
Source is installed runtime `eabb56a278bd8eb1759041467eaebfa6392ddcb2`.
The exact target is `2026-11-02-haveapi-vpsadmin-release`. Root owns lifecycle
execution; architect performed only source reads and the public recovery GET.

Current evidence supersedes the initial Rust-source findings. Root's completed
readiness command, recorded in
`/tmp/session-archival-live-retries-eabb56a2/haveapi-readiness-current.json`, reports
`ready:false`, 5/6 checks and 960 `unmanaged_entry` blockers under
`haveapi-ts-tools`; its 128 retained examples begin with `.editorconfig` and
`.git` entries. Their provenance/content was not inspected. This is a current
ownership/layout refusal, not proof that the earlier repair failed. Explicit
archived mode still does not authorize discarding entries outside verified owned
checkouts. Ordinary CLI archive cannot safely finish against this result.

Public `GET /api/sessions/2026-11-02-haveapi-vpsadmin-release/recovery` returned
`{"state":"idle","executionHeld":true}`. `recovery_input.go:26-100` separately
checks inactive native state, turns, pending input, queue, goal and managed pane;
this result does not say the lead is busy. `recovery.go:42-58` checks execution
permission against retained identity, active-thread membership and App Server
socket generation. An old terminal answer does not grant that permission.
The exact historical reason the hold arose was not established.

The ordering explains the immediate error: `archive_preparation.go:507-550`
first resumes a retained repair `MessageID`, checks `recoveryHeld` at line 522,
then reconciles the exact original delivery and accepted turn. Readiness runs
only afterward at line 613. Thus the refusal precedes reusing the old repair
result or checking current files. It preserves execution and receipt fences;
changing that ordering or making cold archival activate a lead would be a new
behavior change, not an already authorized operational retry.

Supported public activation is explicit input in the **target session**:

- For the current idle/held state, ordinary Send can carry a narrowly scoped
  request to repair the reported archive blockers, preserve unknown content,
  avoid normal development, and leave archival to the portal. Its public route
  is `POST /api/sessions/2026-11-02-haveapi-vpsadmin-release/message`, with JSON
  `message` and one stable UUID `clientUserMessageId`. Preserve the exact text
  and UUID for recovery; ordinary UI Send manages the receipt. The server derives
  the retained root from the exact slug; no caller-supplied native thread ID,
  member address, forged sender or roster access is needed. Existing pending
  original input may still refuse a fresh Send and must keep its own recovery.
- Public `POST /api/sessions/2026-11-02-haveapi-vpsadmin-release/continue` takes
  `{"requestId":"<one stable UUID>"}` and uses the same retained-root admission
  (`recovery.go:336-414,553-628`). With no queue or goal it adds the visible
  generic continuation prompt before activation. It is therefore broader than
  archive-only repair, not a load-only shortcut; the idle UI hides Continue.
- `dev-session resume … --as-is` / public `POST …/resume` restores access and
  leaves execution held (`recovery.go:305-334`); it is not the missing activation.

These are operator session actions, not `session_communication` between leads.
That distinction does not grant permission to send: the lead must obtain explicit
authorization to activate this exact held session, including the bounded repair
input, rather than treating “retry them” as a new activation instruction. No
cross-session communication grant or direct native-thread access is inferred.
The existing approval still covers the original requested archive/retry policy;
it does not cover arbitrary content removal, receipt edits or a new code change.

Activation alone is not a promised archive recovery. A fresh Send/Continue can
create a newer turn, while `archiveRepairComplete` at lines 118-155 requires the
original accepted repair turn to remain latest and successfully complete with
verified loaded idle activity. Preserve this refusal if encountered; do not clear
the pending message, substitute the new turn, or infer completion from idle alone.
After authorized owner repair, root must obtain fresh readiness and reconcile
the original operation through supported status/retry, retaining its policy and
receipt. Any further receipt mismatch returns to the lead for bounded diagnosis.
No code, tests, lifecycle actions, activation or peer communication were performed
for A10; no new implementation/review/build batch is proposed.

## A11: the retained archive receipt blocks cold activation

**Sufficient bounded route diagnosis; no implementation or lifecycle action.**
This supersedes A10's operational suggestion that ordinary Send can activate this
particular session while its failed archive receipt remains. The route and JSON
shape are valid, but their current admission contract refuses that combination.
Lead now records explicit user approval to reactivate, repair and archive, an
approved exact communication pair, and one pending bounded repair message. These
permissions do not waive receipt, retained identity or native execution checks.

Installed runtime remains `eabb56a278bd8eb1759041467eaebfa6392ddcb2`, pinning
codex-web `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`. Root's activation request
`82ac6186-a5b3-4dcc-85d6-a6782a2781e0` received JSON HTTP 404
`conversation is unavailable`; no accepted input is established. Preserve that
exact request/text, with no blind duplicate or replacement thread.

The legacy message endpoint is correctly rewritten by runtime
`portal/internal/web/server.go:1942-1954,2040-2052` to
`/codex/conversations/2026-11-02-haveapi-vpsadmin-release/message`.
`member_conversation.go:20-28` accepts the plain slug as the retained root; it
needs no namespace, `~lead`, native thread ID or extra JSON identity field.
Pinned codex-web `conversation/handler.go:299-322` deliberately maps resolver
errors and final native identity-verification errors to the same JSON 404 before
message handling. Body changes or using the canonical route cannot avoid the
same checks. The matching existing portal log is the only evidence that can
identify which predicate failed first for the historical POST; no log access
beyond the assigned public-metadata scope was taken.

There is nevertheless a **proven current admission conflict**. The exact public
operation GET retains failed archive receipt
`ea0c9a4c926561e2c6332b0067524685558fc69fa0d8434db6885a7fa60f1e75`,
attempt 2, phase `lead_fixing_blockers`, journal
`f07963fa25efbca58194f382210aaf3881210adf9525c0d1f142df0c37ae5a32`, root
`01a19e2e-3abc-7a82-a37a-0a68d376b1ae`; recovery GET still reports
`idle`/`executionHeld:true`. Cold Send calls `requireRetainedInputIdentity`
(`server.go:3986-3989`, `plan_delivery.go:143-170`), which calls
`RequireObservationReceipts` with empty archive coordinates. At
`observation_receipts.go:75-84`, any browser operation whose state is not
`complete` then refuses with `another browser operation reserves the session`.
Read-only idle classification does not run this same mutation receipt admission.

Public Continue also resolves a `message` mutation (`recovery.go:375-380`) and
hits this conflict; Resume is not execution activation. There is no supported
alternate route/request shape identified that both grants cold execution and
retains this failed archive receipt. Do not dismiss/cancel it, clear preparation,
forge archive coordinates, invoke a private helper or load the native thread to
work around the refusal. The smallest safe next dependency is lead reconciliation
of this source conflict with the exact logged error, then an explicit bounded
recovery/design decision. No new implementation package is released by A11.
Original latest-turn verification and the pending communication task remain
unchanged. The current 960 unmanaged-entry blockers still need owner repair;
this route diagnosis says nothing about their contents or provenance.

## A12: supported dismissal of this failed pre-journal reservation

**Supported recovery assessment; lead owns execution.** The supplied portal log
at 2026-11-12 20:53:55 confirms A11's exact error: `resolve conversation: another
browser operation reserves the session`. A11 established that the old receipt
cannot remain the active reservation during cold Send; it did not establish a
need for code changes. Normal public **Dismiss** is available for failed or
complete operations (`static/app.js:2144-2170`). With the exact user approval to
reactivate, repair and archive HaveAPI, this routine failed-operation control can
serve that authorized recovery without another approval or a private record edit.

For this exact failed attempt 2, first retain the full old public receipt,
target/root, archived policy, preparation summary, error and command outcomes in
the existing audit. Then the supported control is
`DELETE /api/sessions/2026-11-02-haveapi-vpsadmin-release/operation` with JSON
`{"receiptId":"ea0c9a4c926561e2c6332b0067524685558fc69fa0d8434db6885a7fa60f1e75"}`.
Success is HTTP 204, not evidence that archival succeeded. Reconcile an uncertain
response against public status before any subsequent action.

At installed eabb, `server.go:876-891,3593-3638` keeps transition/current-profile/
provider admission, reconciles the operation, requires failed or complete state,
then checks the exact current receipt and terminal state again under the operation
mutex. Active preparation is projected as running (`operation_state.go:396-399`)
and cannot be dismissed. `removeLifecycleOperationLocked:615-637` saves removal
of the current browser receipt and display snapshot; a failed archive's preparation
is retained. It does not alter journals, cleanup/prelude state, native submissions,
queued communication, goals, retained conversation identity or execution permission.

Guard limits matter: Dismiss is not a native-effects cancellation or universal
no-journal proof. Its handler does not reject every reconciliation error when an
existing receipt remains (`server.go:3602` tests `err != nil && !ok`). Therefore
the lead must preserve its independently verified failed/pre-journal/no-worker
conditions, not infer them from the currently stale public operation snapshot.
Fresh session details expose `pendingLifecycle` from ordinary validated inspection;
an explicit empty value proves no pending journal/prelude at that observation.
For precise metadata-only checks, all these canonical paths must yield **ENOENT**:

- `worktrees/.locks/2026-11-02-haveapi-vpsadmin-release.archive.json`
- `worktrees/.locks/2026-11-02-haveapi-vpsadmin-release.archive-cleanup.json`
- `worktrees/.locks/2026-11-02-haveapi-vpsadmin-release.services-cleanup.json`

Paths are relative to `/home/aither/workspace/ai/vpsfree.cz`; `.locks` itself must
be a real directory, not a symlink. Use `lstat`, without opening record contents;
any present entry, symlink or non-ENOENT error is not absence and requires ordinary
reconciliation. Source: `session/lifecycle.go:117-169,175-211`,
`session/service_cleanup.go:21-31`, `libexec/workspace-archive-cleanup.rb:150-152`.
No mutation is made atomic by a prior status check; subsequent normal admission
remains authoritative.

After confirmed Dismiss, retry the exact already authorized bounded activation
text/ID `82ac6186-a5b3-4dcc-85d6-a6782a2781e0` through ordinary Send. Its retained
identity, stopped-pane, native inactivity, queue/goal, original-input and uncertain
delivery checks remain (`recovery_input.go:137-198,215-243`); stop on a new refusal
instead of clearing evidence. Preserve the pending cross-session repair message.
Once owner repair and fresh readiness succeed, a **new ordinary Archive
confirmation**, same `archived` policy and exact retained target, creates a new
receipt. It does not retry or certify the old failed repair turn. New confirmation
still refuses an accepted journal (`server.go:3147-3187`).

The runtime does not retain an append-only history of dismissed browser receipts.
Failed preparation survives Dismiss but a new archive receipt replaces the
orphaned preparation (`archive_preparation.go:228-250`); preserve old available
audit before these steps. Native delivery records remain separate and untouched.
This distinction makes public Dismiss plus new confirmation different from
private evidence rewriting or pretending the old receipt succeeded. No code,
tests, native reads, Dismiss, activation or archival was performed by architect.

## A13: prepare this session by accounting for retained monitor effects

**Preparation only.** Development is paused for the user's requested portal-owned
archival preparation of `2026-11-11-session-archival-failures`. No archive, delete,
stop, cancellation, signal, infrastructure change, queued development or new
implementation/check is authorized by this package. Architect owns this appendix;
implementer0 gathers exact current evidence; the exact retained lead owns any
supported evidence-resolution action.

Installed runtime is still `eabb56a278bd8eb1759041467eaebfa6392ddcb2`. Its
`monitoroperation/service.go:248-264` treats a terminal `incomplete` report or any
nonempty terminal `stillRunning` as unresolved external effects, independently
of native idle state. No prose interpretation, elapsed age or later successful
run changes that result. `lifecycle.go:130-146` preserves the archive refusal.

For monitor `63e94315-36d3-4455-87d0-69f78f1e71ef` and the separately identified
same-source monitor beginning `8c0c1246`, evidence must account for all of:

- Exact frozen provider/repository/workflow/run **43095435241**, run attempt and
  full tested commit corresponding to `359636df`; fresh authoritative terminal
  run/job status, conclusion and timestamps. A different attempt or later run
  cannot settle this source.
- Original local poller tool session **33520**, PID **1773324**, its exact command
  and invocation identity, plus any known owned child/cell/tool-session effects.
  Prefer the original joined exit/terminal receipt. PID absence/reuse or CI
  completion alone is not exact invocation/effects proof. If the original handle
  cannot be joined, a replacement observation must positively account for that
  invocation and all known effects; record any remaining uncertainty as a blocker.
- Each monitor's own full operation UUID, retained utility/project/thread,
  immutable report and exact launch/delivery receipts. Shared CI evidence is
  reusable only for the identical frozen source tuple; it does not settle the
  other utility's local work or authorize resolving an abbreviated ID.

Only when that evidence is complete, the exact current lead can call ordinary
`monitor_operation` with `action:"resolve"`, the full `operationId`, one fresh
stable `resolutionId`, nonempty `detail` and `evidence`. Use a distinct resolution
for each unresolved operation. Evidence permits 1–16 nonempty strings of at most
1024 bytes; detail is at most 4096 bytes (`service.go:236-244`). Retry an uncertain
resolution only with the identical ID, detail and evidence; inspect its status
first. This is not a new report and must not change the historical test outcome.

`ResolveEffects` (`service.go:266-325`) rechecks exact lead/session incarnation,
locks the operation, reconciles its launch and requires native quiescence. The
runtime rejects unknown launch/lead-submission receipts and verifies exact native
utility identity, idle turns, prompts, queues and submissions
(`lifecycle.go:31-127`). It cannot inventory every code cell/tool process; that
is why independent poller/effects evidence remains required. Resolution records
one immutable proof, clears only the external-effects fence, and suppresses unsent
continuation delivery. It does not interrupt a command, wake a conversation,
archive a utility/session, edit the original report or settle another operation.
Accepted or submitting deliveries and other native fences keep their own proof.

If any named poller/cell is live, its identity is uncertain, or native/receipt
proof refuses, retain the blocker and report exactly what evidence or separately
authorized action is missing. Do not use cancellation, new monitoring, a rerun,
manual receipt edits or a terminal-outcome rewrite as substitutes. The current
operational proof belongs to implementer0's report; no terminal result or safe
resolution is claimed here until that evidence is supplied and assessed.

### A13 operational evidence assessment: remote source still unfinished

Implementer0's bounded Q report supplies the missing local evidence. Fresh GitHub
REST run, attempt-1 and jobs reads at **2026-11-12T21:50:57Z** succeeded, but the
exact run **43095435241**, attempt **1**, workflow **354263807**, tested head
`359636df` still reports **queued**, null conclusion and zero jobs. Its provider
created/started/updated timestamps remain 2026-11-11T20:20:24Z. Successful REST
commands prove a successful observation, not successful or terminal CI. Age and
zero jobs do not prove that the queued run has no future effects.

The original local poller is accounted for by a positive native terminal receipt:
`exec-b5e058f6-4f3b-4454-94b2-2471fbf3b1c1`, tool session **33520**, exact original
argv/cwd, status `failed`, exit **-1**, completed
**2026-11-11T21:03:56.170Z**. Its cause/signal is not recorded. Current PID
1773324 absence is supporting metadata, not the completion proof. This late
receipt follows utility63's task completion at 20:33:56.124Z and confirms why a
completed native turn alone was insufficient. Utility8c completed at 20:42:50.023Z.
Implementer0 accounted for all 47 outer calls and 26 native command terminal
receipts, with no known unjoined command after the late receipt; the second
monitor launched no additional long source. The exact tables belong to its
assigned `verification.md` appendix, not a duplicate inventory here.

The full second operation is `8c0c1246-5469-419b-aacd-a2e0f38e87d9`. Lead-supplied
status snapshots at `/tmp/session-archival-preparation-<operationId>-lead-status.json`
retain terminal `incomplete` and no resolution for both operations; 8c's terminal
report was synthesized after its turn completed. These immutable outcomes remain
unchanged. **Neither operation is presently safe to resolve:** the exact remote
source is still unfinished even though the known local effects are now accounted
for. The minimum remaining dependency is authoritative terminal status for that
same run/attempt. Cancellation would require separate explicit authorization for
that exact remote run, followed by terminal proof; no cancellation is authorized
or performed by this preparation package. No new code, verification run, native
read, lifecycle action or monitor mutation is needed for this conclusion.

## A14: separate archive safety from remote verification completion

**Proposal only; sufficient for product/scope decision, not implementation release.**
The user requests a process fix, not CI cancellation, implementation, deployment
or archival. This proposed contract supersedes A13's remote-terminal prerequisite
only after implementation and compatibility verification; installed eabb still
enforces the old rule. Remote CI should continue by default when its observing
session is archived. No additional product choice is needed for that default.

### Cause and smallest coherent change

Currently `HasUnresolvedEffects` conflates an incomplete verification outcome with
unsafe local work (`monitoroperation/service.go:248-264`). Archive requires that
combined predicate before quiescing the session (`lifecycle.go:130-179`,
`libexec/dev-session:9454-9470`). Revoke suppresses notification delivery but does
not stop observers (`lifecycle.go:207-239`). Consequently a queued remote run can
block even after its observer ended. Conversely, Q's poller33520 ended well after
its utility turn, so ignoring every CI monitor or trusting idle alone is unsafe.

Separate three durable facts under the existing monitor owner:

1. **Source observation:** exact provider/repository/workflow/run/attempt/commit,
   last observed remote status/conclusion/time, and whether local observation is
   attached or detached. Remote queued/running/unavailable status is information,
   not a session archive dependency. Detachment never means CI passed or stopped.
2. **Local observation safety:** launch/call ownership, local running/unknown/
   quiescent effects, original receipts and evidence coverage, plus durable
   observing → quiescing → detached state bound to the accepted archive identity.
3. **Historical result:** original report/events and accepted deliveries remain
   immutable, including `incomplete`. Do not rewrite `stillRunning`, parse English
   `none`, or repurpose old `Resolution` as proof that remote CI ended.

This applies to positively identified **observation of an existing remote run**,
not every `kind:ci` operation. Session-owned remote deployments, mutations and
resources retain their existing coordinator/resource-owner fences. Monitor
classification neither adopts nor releases those obligations. Arbitrary local
commands and unknown tool effects remain blocking even when their source is CI.

### Automatic archive behavior

For new read-only CI observation, use bounded direct polling inside the existing
monitor worker (`web/monitor.go:98-177`); freeze its exact source and restrict it
to read-only status requests. Do not launch an LLM-owned long `gh run watch` shell
or detached code cell for this mode. Keep other verification watchers unchanged.
The worker owns each request context and joins it on shutdown. No new daemon,
general scheduler, service registry or remote cancellation API is needed. Existing
registered-service shutdown remains the boundary for any already registered
local observer process; never adopt an arbitrary PID as such a service.

After an Archive confirmation is durably accepted and its target/admission are
verified, persist quiescing and suppress new observer requests and wakes through
existing revocation/delivery admission **before** requesting local shutdown.
Cancel/join only the owned read-only polling request, then save detached with
local proof and the remote source unchanged. This is cancellation of observation,
not of the GitHub run. For a retained native utility, keep exact project/thread,
launch/submission and idle proof (`monitoroperation/lifecycle.go:31-127`); an
interrupt response alone cannot prove its command sessions ended.

Read-only `archive-check` must remain read-only: distinguish an automatically
quiesceable observer from a hard unknown/local-effects blocker. The accepted
preparation/executor owns quiescence, then reruns authoritative readiness before
any supporting file/worktree removal. Both browser and ordinary CLI archive use
the same lifecycle assessment. Existing tracking, target, services, native,
coordination and resource checks still apply. The status should say that local
observation ended and remote CI continues, retaining its run link and last result.
If shutdown/proof is uncertain, leave preparation pending with the exact local
handle and reason; do not remove files or force a successful status.

### Legacy proof, restart and package compatibility

Use existing cold native identity/receipt observations as evidence, not an
assumed tool-process inventory. Structured native `CommandExecution` receipts
can settle exact calls such as33520; a terminal turn/activity-count cache cannot
substitute for complete late-call evidence. The selected monitor skill explicitly
states that native idle checks do not inventory every cell/tool session. Keep
unknown coverage fenced rather than inventing a generic process census.

For legacy63e94315 and8c0c1246, add a narrow exact-lead **local-observation
attestation** under ordinary monitor admission: bind each full monitor ID,
original source/owner, Q's full call/terminal-receipt evidence and explicit
observation-only classification; require current native/receipt proof. Record
local quiescence and remote detachment without changing either historical
incomplete report or requiring terminal GitHub status. Q's complete local proof
is sufficient input for this route, subject to runtime revalidation. It does not
justify a blanket migration of other old incomplete monitors.

Prefer one versioned auxiliary observer record owned by the existing monitor
store, leaving schema-1 operation/report bytes and exact report replay intact.
Publish a narrowly scoped observer-lifecycle capability. New packages read old
records conservatively; absent attestation means unknown, not detached. Extend
the existing source/candidate activation compatibility checks
(`libexec/workspace-host:3151-3169` and target activation) to require that capability
whenever auxiliary records exist. Initial upgrade can retain the old schema-1
reader contract; rollback to an incapable package must refuse before switching
or deleting evidence. No database migration, eager historical rewrite or silent
old-reader interpretation is permitted. Final field names/version and generated
contract edits belong to the implementation brief after approval.

Persist shutdown intent before effects. Retry/restart resumes the same monitor,
source and accepted archive identity, reconciles any in-flight request, and never
restarts a detached observer or the remote job. Late responses may retain a
matching source snapshot but cannot reopen observation or wake an archived lead.
Accepted/uncertain native deliveries retain their separate receipt recovery.
Revival does not silently reattach observation; doing so requires a new explicit
monitor request. A failed archive keeps the detached state and recovery evidence.

### Staged implementation and narrow acceptance

| Proposed owner/package | Files/interfaces and dependency | Acceptance |
| --- | --- | --- |
| Implementer1: monitor safety contract | `portal/internal/monitoroperation/{types,store,service,lifecycle,delivery}.go`, CLI monitor admission in `portal/cmd/workspace-portal`, runtime contract and package compatibility. Add local assessment/attestation; retain old report semantics. | Queued remote source plus proved local quiescence is archive-safe; live/unknown local effects, foreign ownership and unresolved native submissions refuse. Existing incomplete outcome/replay remains unchanged. |
| Implementer0: bounded observer and archive integration | After contract settlement: `portal/internal/web/monitor.go`, `archive_preparation.go`, `libexec/dev-session`, `workspace-archive-check.rb`, matching portal status and monitor/recovery docs/skill. Add direct read-only polling and accepted-operation quiescence. | Archive joins owned polling and suppresses wakes, then rechecks readiness before removal; no remote cancel, replacement job or normal-development turn. Preserve independent resource/deployment fences. |

Sequence shared contract/CLI edits and pin any codex-web change only if an actually
missing structured proof interface requires it; no Codex upgrade or generic tool
supervisor is part of this proposal. Minimum focused cases: queued and long-running
remote CI with ended local observation; live owned poll request joined; unknown
legacy cell or incomplete inventory refuses;33520-style late command completion;
same-source dual monitors with distinct local proof; restart before/after shutdown
and late response; exact retry/idempotence; accepted/unknown native delivery;
legacy schema/read/replay and incapable rollback; genuine resource-owner blocker.
An integration fixture must show archive completes with a still-queued remote run,
zero remote cancellation calls, no surviving local observer and no post-archive
wake. Use normal quick checks, committed independent review and only the affected
package/lifecycle integration verification if implementation is later authorized.
No tests, builds, source changes or live recovery actions were performed for A14.

## A15: sufficient implementation contract for monitor archive safety

**Ready for lead acceptance and package release.** User approved implementation;
this does not authorize live attestation, cancellation, archival, deployment or
claims. P0 establishes fresh canonical `origin/master` and clean feature HEAD at
`eabb56a278bd8eb1759041467eaebfa6392ddcb2`, with no A14 interface drift. Installed
`0s5dljmmfngj7ia2r9lfkxwydnfiz6b6` is unchanged. This section fixes A14's remaining
implementation choices; earlier investigation records remain historical evidence.

### Execution owner and public contract

- For a **new** `monitor_operation start` with valid `source.kind:"ci"` and
  provider `github`, runtime-owned bounded polling replaces the native Luna
  launch. It observes only the exact existing repository/workflow/run/attempt/
  commit. No thread/project, model turn, `gh run watch`, remote trigger, rerun or
  cancellation is created. Unsupported providers refuse explicitly; do not
  silently launch a native observer as fallback.
- Resolve an existing ID in both stores before choosing a driver. Same ID and
  exact original request digest replays its stored operation: existing schema-1
  CI monitors remain native. Changed request/source/driver is a conflict, never
  an implicit conversion. Local command sources and member-owned fallback keep
  the current native utility policy and catalog snapshot.
- `start`/`status` expose `executionOwner:"runtime-ci"|"native"`. Native replies
  preserve their current fields; direct replies expose common ID/owner/source,
  observer status and delivery events, with **no fictitious launch/thread**.
  Callers verify the acknowledged owner: runtime-ci requires durable registration,
  not a utility turn receipt. Exact lead ownership, session/incarnation and
  stable-request checks remain mandatory for start/status/cancel/attest.
- Existing `report` remains utility-only and cannot report a direct observer.
  Add `attest-local` to the existing monitor tool/CLI, carrying `operationId`,
  `attestationId`, `sourceDigest`, `nativeBindingDigest`, `evidence`, `detail` and
  `observationOnly:true`. It records local proof, **not** `ResolveEffects` or a
  terminal remote result. Existing `resolve` retains its old semantics. `cancel`
  continues to suppress unsent continuation; it is not remote cancellation.

### Record and persistence contract

Use `<monitor-store>/observers/<id>.json`, schema **1**, owned by the existing
monitor store. This is the sole direct-CI record; do not create an artificial
schema-1 native operation beside it. For a legacy attestation it is an auxiliary
record referring to the existing native operation. Strict decoder, duplicate-key
rejection, canonical ownership, bounded JSON (512 KiB), mode0600 and the existing
atomic temporary-write/fsync/rename/directory-fsync pattern apply.

Required fields and meaning:

| Field | Contract |
| --- | --- |
| `schema`, `id`, `workspace`, `owner` | `1`, existing valid operation ID, canonical workspace and existing exact `Owner` structure. Immutable. |
| `driver` | `direct-ci` or `legacy-native`. Immutable; never inferred from report prose. |
| `requestDigest`, `source`, `sourceDigest` | Existing canonical start-request digest and CI source; SHA256 of canonical source serialization. Immutable. Repository/workflow/run/attempt/commit validation reuses existing CI rules. |
| `createdAt`, `updatedAt`, `revision` | UTC timestamps, monotonically increasing revision for accepted record writes. |
| `phase` | `observing`, `quiescing`, `quiescent`, `detached`. Only direct-CI starts observing. No transition from detached back to observing. |
| `remote` | Optional last validated `{status,conclusion,observedAt,url}` snapshot. Missing means unknown; no snapshot or terminal conclusion is needed to detach. Exact source must match every response. |
| `poll` | Optional current bounded invocation `{id,ownerEpoch,state,startedAt,handle,finishedAt,exitStatus}`; state is `intent`, `running` or `joined`. `handle` is an exact runner receipt, not a bare PID. Retain the last receipt when joined. |
| `archive` | Optional accepted `{operationId,receiptId,targetId,mode}`; CLI may omit browser receipt. Mode/target are copied from validated ordinary lifecycle admission, never accepted as caller assertions alone. |
| `localProof` | Optional `{kind,at,evidence,detail,attestationId,leadThreadId,nativeBindingDigest}`. Kind `runtime-joined` or `legacy-attested`; attestation fields required only for legacy. Evidence/detail use existing resolution bounds. |
| `events` | Existing bounded `Event`/delivery representation for direct-CI only. Legacy events remain exclusively in their original operation; do not copy or rewrite them. |

One per-ID lock serializes lookup/create across native and observer stores.
Take existing session/generation admission before that lock. Legacy mutation order
is session → native operation lock → observer record; readers use the same order.
Atomic creation of the direct record is registration; no native side effects may
precede it. A duplicate native/direct ID is corruption and refuses, not precedence.
For legacy, `nativeBindingDigest` hashes canonical immutable owner/source/request,
launch project/thread/message/options/bootstrap identity and existing report bodies;
exclude mutable delivery status and lifecycle disposition. New/changed report or
identity invalidates old proof. Retain schema-1 validation, old request digests,
exact report replay and immutable outcome bytes unchanged.

Legacy attestation verifies the existing source is CI observation only, exact lead,
current native quiescence/known receipts, and nonempty evidence accounting for
every known local call/tool session. It is an explicit trusted-lead evidence act,
not an automatic parser or an assertion that the runtime enumerated all cells.
It writes phase quiescent. Same attestation ID and exact evidence/detail/bindings
is idempotent; any conflicting reuse or changed owner refuses. The Q evidence for
63e94315 and8c0c1246 is suitable input; runtime must revalidate before accepting.
Remote run43095435241 may remain queued and both old incomplete reports stay intact.

### Exported package interfaces

Owner1 supplies these interfaces in `monitoroperation`; names/signatures are the
shared implementation boundary (ordinary transport/DTO adapters may be private):

```go
type LocalSafety struct {
    State string // quiescent, quiesceable, blocked
    Reason string
    OperationIDs []string
}
type ArchiveAuthority struct {
    Slug, RootThreadID, OperationID, ReceiptID, TargetID, Mode string
}
// Read-only, no polling, loading, shutdown, attestation or record creation.
func (l Lifecycle) AssessLocalSafety(ctx context.Context, slug, root string) (LocalSafety, error)
func (s *Service) AttestLocalObservation(ctx context.Context, caller string, req LocalAttestationRequest) (ObserverRecord, error)
// Ordinary accepted lifecycle owner only; persists intent and fences dispatch.
func (l Lifecycle) BeginArchiveQuiescence(ctx context.Context, a ArchiveAuthority) error
// Returns pending local handles/refusals until all exact effects are joined.
func (l Lifecycle) CompleteArchiveQuiescence(ctx context.Context, a ArchiveAuthority) (LocalSafety, error)
type CIObserver interface {
    Poll(context.Context, Source) (CISnapshot, PollReceipt, error)
    Quiesce(context.Context, string /* operation ID */) (PollReceipt, error)
}
```

The portal worker receives the CI observer dependency. CLI/executor processes
request quiescence through the durable phase and read its published join proof;
they never reconstruct another process's cancellation handle or signal its PID.
An in-process controller can cancel immediately after intent is saved. Without
one, Complete returns pending until the owning worker joins its bounded request;
controller absence cannot be interpreted as no local work. Owner1 owns
registration/snapshot/result commit helpers under the same
store transaction; owner0 supplies the bounded runner implementation. Poll receipts
prove actual start/join or positively unsent; an error/timeout is not such proof.
The worker never edits files directly. Results are committed only for matching
ID/source/revision/phase; a late response cannot reopen detached observation.

`AssessLocalSafety` treats an attached, registered direct reader as quiesceable,
not a remote-result blocker. Legacy unresolved effects without valid local proof,
unknown tools, changed identity, unknown native submissions or active native work
are blocked. Valid legacy proof bypasses only the old combined external-effects
predicate for this observation; native receipt/idle checks still run. A real
deployment/resource mutation remains with its current coordinator/resource owner;
neither attestation nor CI status can waive those fences.

### Polling, delivery and accepted archive ordering

Use the existing monitor worker's bounded/fair passes. One poll per operation at
a time, 15-second minimum interval, existing per-item 5-second request budget;
no total CI deadline. Use the configured GitHub access context and a fixed read-only
run-attempt API query; no shell, arbitrary argv or provider mutation. The existing
bounded GH runner may be reused only with synchronous cancellation/join and exact
owned-call receipts. An in-flight intent is persisted before invoking it. If a
crash loses the execution receipt, retain unknown local effects and require exact
runner reconciliation; never assume a child died because the portal restarted.
No new general process supervisor, service or scheduler is permitted. If the
existing runner cannot furnish that ownership/join proof, stop the adapter package
for clarification rather than replacing it with a detached/native watcher.

A poll timeout/network/auth error retains the last source snapshot plus a bounded
diagnostic; it does not synthesize failed CI. A validated terminal source produces
one ordinary immutable terminal event (`success` → passed, other terminal
conclusions → failed). Creation and dispatch use existing event IDs, exact lead
settings, original-receipt reconciliation and held-session rules. Archive detachment
does not fabricate a successful terminal report or an unsolicited wake.

For an accepted archive: validate current generation/provider/target and resource
admission; call BeginArchiveQuiescence to save the exact archive binding and
quiescing intent; revoke future observer launch/poll/delivery; cancel/join only
the owned read-only request; then CompleteArchiveQuiescence repeats local/native
proof and saves detached. Persist before effects, and never hold a store lock while
waiting for a worker that needs that lock to commit. Recheck state under the lock
after joining. Existing accepted/submitting native deliveries are reconciled, not
deleted or declared canceled. Dismissal/replacement of an archive request cannot
reattach the observer; a new explicit monitor ID is required to observe again.

`archive-check` stays read-only. Add typed monitor-local readiness information to
its bounded JSON result as optional `monitorLocal:{state,reason,operationIds}`
using LocalSafety's values. Quiesceable keeps `ready:false` with a specific
`monitor_observation` blocker until joined; it is not a hard repair request.
Preserve existing fields/meaning for old consumers. Preparation does not increment
repair round/no-progress counters while waiting for this owned shutdown. The
accepted browser preparation must quiesce this monitor work before asking a lead
to repair unrelated blockers. CLI explicit archive invokes the same owner path.
Both then run the normal authoritative readiness checks before file removal.
No archive fast path, schema1 native-receipt waiver or resource cleanup bypass.

On restart, observing direct records may resume bounded reads only after exact
owner/generation/maintenance admission and reconciliation of any prior poll.
Quiescing records resume the same accepted archive binding; detached records
never poll or send. A recorded joined poll is replayable; an uncertain invocation
stays blocked. Revival does not reattach. Normal native monitor launch/delivery
recovery remains unchanged, including unknown submissions and stopped leads.

### Capability and rollout contract

Keep `monitorOperationStateSchema:1` and `monitorOperationPolicy:1` for unchanged
native records. Add **`monitorObserverStateSchema:1`** and
**`monitorObserverLifecyclePolicy:1`** to the runtime contract. Reading absent
observer state creates nothing. The first direct registration/attestation creates
the observer directory durably; any present/unreadable/malformed observer state
requires both capabilities in a selected target. No downgrade silently ignores it.

Source preflight and candidate activation must inventory this exact directory and
enforce the new capabilities before a switch/rollback can proceed. Existing
generation/maintenance exclusions fence new writes while old retained package
operations finish; do not allow an old recovery executor to bypass new obligations.
Initial upgrade from eabb is allowed with schema1 compatibility and no observer
state. Deploy the complete reader/writer/worker/CLI/skill unit before enabling any
new observer record. Once used, rollback is only to a package with both capabilities;
there is no destructive down-conversion, synthetic old Resolution or automatic
record deletion. Retain forward recovery and all original archive policy/journals.

The generic monitor skill and tool help must explicitly route new supported CI
observations to the acknowledged runtime owner without selecting Luna or demanding
a native launch receipt. Retained native operations, local commands, member-owned
checks and unsupported runtime fallback retain the existing watcher rules. Root
owns any required caller-policy wording in workspace instructions that otherwise
unconditionally mandates a Luna CI watcher; that narrow consistency edit is a
rollout prerequisite, not permission to alter retained member settings.

### Package ownership, acceptance and stopping conditions

| Package | Owner and exclusive files | Dependencies / required result |
| --- | --- | --- |
| P1 core | implementer1: `portal/internal/monitoroperation/`, monitor CLI/tool handlers in `portal/cmd/workspace-portal`, runtime-contract source/generated checks, `libexec/workspace-host` compatibility gate and its activation counterpart; monitor contract documentation in `docs/workspace-portal.md`. | Root accepts this brief. Export interfaces, dual-format ID ownership, direct registration, strict local attestation, event/delivery adaptation and capability enforcement. No poll adapter or archive caller edits. |
| P2 integration | implementer0: `portal/internal/web/monitor.go`, direct CI adapter/tests, `archive_preparation.go`, archive-check JSON adapter, `libexec/dev-session`, `libexec/workspace-archive-check.rb`, affected browser status/tests, archive recovery docs and generic monitoring skill/session guide. | P1 signatures settled; code may start against them after root release. Final compilation/verification depends on P1. Wire polling, typed readiness, accepted archive quiescence and truthful UI. |

P1 owns shared `portal/cmd/workspace-portal` edits, including P2's small dispatch
wiring by direct clarification; P2 owns `libexec/dev-session`. P1 introduces
typed readiness DTOs consumed by P2; no competing edits to monitor core/types.
Sequence index/commit/formatting windows. Root owns final caller-policy wording,
independent review and acceptance. No codex-web/package dependency upgrade is
required; a missing proof interface is a blocker to report, not scope to invent.

Quick checks after implementation: focused readonly-mode Go monitor/CLI/web tests,
Ruby syntax and relevant host/archive unit cases, browser syntax and focused
archive readiness fixture, contract-generation consistency, diff checks. Use the
repo Nix environment; uncertain/long checks use the installed watcher policy.
Stop on source/owner mismatch, unproved runner shutdown, unexpected schema scope
or basic fixture/type failure; fix the specific boundary before broad reruns.

Acceptance covers new CI start with **zero native launches**, same-ID legacy
native replay, queued/running/unavailable remote source with joined local observer,
native/live/unknown local effects and genuine resource blockers, exact33520 late
receipt, two same-source monitors with separate local proof, immutable legacy
incomplete reports, duplicate/cross-format IDs, accepted/unknown delivery,
restart at each registration/poll/quiesce write boundary, detached late response,
no wake after archive/revival, stale target and capability rollback refusal.
After committed independent review, run the affected packaged monitor/native and
archive lifecycle integration tests: complete archive while a fixture remote run
remains queued, zero remote mutation/cancel calls, no remaining local observer,
and unchanged resource/native/file-removal fences. Keep exact final-head evidence;
do not use a real stuck CI run or live session as a test fixture. No implementation,
checks or live recovery actions were performed by the architect for this brief.

### A15 runner-proof clarification accepted by lead

P2 may extend only the existing `portal/internal/processgroup/processgroup.go`
and its focused tests to expose a detailed owned execution result, preserving
the current `Run` contract for existing consumers. The repository runner's opaque
`CombinedOutput` is insufficient. Existing `processgroup.Run` owns `Start`, sets
a process group and waits synchronously, but its context-cancellation branch
discards the group-kill error and raw `Wait` result. A nonnil `ProcessState`
therefore cannot alone prove safe cleanup; `exec.ErrWaitDelay` can be hidden.

The detailed result must retain whether Start actually succeeded, whether Wait
returned, raw Wait error, group-cancellation error and incomplete pipe cleanup.
The fixed read-only GH adapter binds this result to the previously persisted
operation/poll ID, owner epoch, exact argv/source and live owned command handle.
No P1/core signature change or new supervisor/service is needed.

- **Unsent:** positive pre-start refusal or Start failure with no started command.
  Missing data after interruption is not proof of unsent execution.
- **Joined:** the exact started command has a terminal ProcessState and Wait
  returned, no incomplete pipe cleanup/ErrWaitDelay, and the original owned group
  is absent or equivalent helper-owned shutdown proof exists. Limit any absence
  check to that captured group and existing bounded cleanup budget. Nonzero exit
  or a proved local context-cancel shutdown may still be locally joined; neither
  establishes a terminal remote CI outcome.
- **Unknown:** started but no terminal receipt, masked/uncertain cleanup, remaining
  owned group, escaped pipe holder, ambiguous identity, or crash/lost in-memory
  handle. Persist the blocker; do not reconstruct a handle or signal by a saved
  PID, assume parent death killed children, or substitute a new watcher.

Only the original adapter/helper controls its live group. Do not add whole-host
process discovery, adopt other processes, or widen the command to arbitrary shell
execution. Root accepted this narrow P2 file-boundary addition; P1 and unrelated
integration remain independent. This addendum is source assessment only: no
helper edits, tests, prototype or runtime action by architect.

### A15 fresh CLI archive admission: accepted trusted-parent handoff

Canonical base `eabb56a278bd8eb1759041467eaebfa6392ddcb2` proves the fresh CLI
has accepted in-memory authority, but no persisted archive authority yet:

- `libexec/dev-session:10563` (`run_archive`) obtains interactive confirmation
  or validates the portal worker. `with_lifecycle_transition:10022` validates
  generation/provider under the shared transition lock.
- `archive:2093`, `with_lifecycle_access:8332` and
  `revalidate_lifecycle_access!:8405` capture and recheck the target/receipt/journal
  under creation and exclusive slug locks before marking the request admitted.
- Fresh explicit readiness at line 2125 precedes operation-ID allocation at
  2134, native quiescence at 2170, service prelude creation at 2195 and capture
  journal creation at 2208. Neither later artifact can prove this earlier action.
- `portal/cmd/workspace-portal/monitor.go:181` documents the lock-held Ruby
  caller, but its old retirement actions require an existing journal. Caller
  fields alone do not establish fresh accepted archive authority.

Do not move the capture journal/service prelude earlier, invent a browser receipt,
or weaken readiness/native capture. Browser preparation's accepted receipt and
admission remain independently usable. Existing journal recovery keeps its
original authority and policy.

Lead accepted a trusted handoff from the already confirmed, admitted high-level
CLI using the actual inherited exclusive slug-lock descriptor. The existing
precedent is `release_development_clusters!:7043`, which
passes `@held_slug_lock` with `DEV_SESSION_LIFECYCLE_LOCK_FD/PATH` and `pass_fds`.
That proves a reusable handoff mechanism, not a monitor authorization path already
implemented. An inherited lock proves lock ownership, not user confirmation by
itself; the high-level confirmed call chain must remain the only entry. The
handoff preserves target/root/generation/provider/resource admission and A15's
existing observer binding/restart rules without manufacturing a receipt.

**Owner and transport:** P2 wires `libexec/dev-session` after ordinary confirmation,
`with_lifecycle_access` admission, exact manifest/root/target validation and normal
coordination admission. Require the matching admitted archive request and actual
`@held_slug_lock` in EX mode. Use existing `CommandRunner.capture:409` with its
`env` and `pass_fds`, supplying `DEV_SESSION_LIFECYCLE_OPERATION=archive` and the
existing lock FD/path variables. Scope/IDs travel through the internal monitor
lifecycle adapter; supplied fields alone never authorize it. P1 owns that adapter
in `portal/cmd/workspace-portal/monitor.go`, its `AuthorizeArchive` wiring and
focused validation tests. Existing exported Begin/Complete signatures stay fixed.
The browser keeps its persisted receipt admission, without this CLI shortcut.

**Descriptor proof:** reuse the existing validation pattern in canonical extension
`767dfd587e346168e1443e65ccdb67ce748f3fe3`,
`dev-clusters/kb/lib/guards.rb:60` and `dev-clusters/lib/runtime.sh:698`:

1. Require a real inherited FD >= 3 and the canonical selected workspace's exact
   slug-lock path (configured runtime authority; existing CLI fallback only when
   that is the selected lock). Require an euid-owned mode0600 regular file, reject
   symlinks, and match the inherited FD's device/inode to a no-follow path open.
2. An independent open's shared nonblocking probe must fail with lock contention;
   success means no exclusive owner and refuses. Other errors also refuse.
3. Exclusive nonblocking flock on the inherited FD must succeed, proving it owns
   that exclusion rather than merely observing another owner's lock. Do not
   unlock or downgrade this shared open-file description in the child; close only
   its inherited reference when done. No PID or whole-host process discovery.

The caller's current generation/provider admission and exact target/root remain
required alongside this proof. The adapter verifies the current manifest/target
against the supplied binding, rejects conflicting lifecycle state, and cannot
turn a caller-supplied receipt into browser authority. This is the repository's
trusted-local-parent boundary, not protection against a malicious host operator.

**Pre-journal replay:** under admitted locks, select the archive binding before
allocating a fresh operation ID. A normal existing journal/prelude or accepted
browser receipt supplies its original ID/policy and must agree with observer
bindings. For fresh CLI, inspect only the current owner's observer records for
an existing accepted binding: exact workspace/slug/root, current version-2 target,
mode and operation ID must agree across affected records. Preserve its operation
ID and empty CLI receipt ID; a browser-bound record requires its real receipt
admission. Conflicts, changed incarnation/target, malformed records or uncertain
ownership refuse. Do not select the newest conflicting record or erase one.

With no existing binding, allocate one archive operation ID and persist it through
Begin's existing observer `archive` field before any quiescence effect. The private
adapter may select/replay this binding and return the selected authority to Ruby;
this requires no new exported core API or standalone authority record. Ruby uses
that same ID for the later normal archive journal/prelude. A crash after a partial
Begin or before its reply is recovered from the stored binding, including an
already detached record; repeat Begin/Complete idempotently without reattaching,
changing the remote outcome or claiming the archive itself succeeded. Native
unknown effects remain blockers. If no binding was durably written, no quiescence
effect may have started.

Pending quiescence unwinds creation/exclusive slug locks before an interruptible
bounded wait, so the original worker can publish its join. Retain the accepted
request in the current invocation; each reacquisition must revalidate its full
target/binding/current admission, not rely on the old `admitted` shortcut after
releasing locks. A process restart requires ordinary fresh confirmation/admission
and then reuses the exact durable binding. Readiness and native capture still run
before file removal; journal/prelude creation stays at its original boundary.

Focused acceptance: bare flags, missing/wrong/unheld/shared FD, foreign inode,
changed target/provider/generation and conflicting bindings refuse; exact inherited
owner succeeds. A crash between the first observer write and normal journal,
partial multi-record Begin, and lost reply reuse the original ID; no lock-held
wait deadlock, fabricated receipt, successful-archive claim or observer reattach.
P1/P2 retain their existing file ownership. No source edits, checks or runtime
actions were performed by architect for this mapping.

### A15 browser coordination admission clarification

Reuse the ordinary read-only archive check, not the coordination UI/cache or a
new resource API. At base eabb, `libexec/workspace-archive-check.rb:109` invokes
`require_lifecycle_idle!` and `require_lifecycle_capacity!`; their implementation
at `libexec/workspace-coordination.rb:545` maps the current owner incarnation and
checks active resource claims/jobs, uncertain deployment and admission capacity.
The later lifecycle journal binding remains the actual coordinator fence.

P2 runs that fresh check and immediate Begin in the same accepted preparation
admission callback. After releasing/reacquiring admission, refresh the check;
an earlier clean result is not a retained permit. Require valid, complete output
(`blockerCount == len(blockers)`): absence of a coordination blocker among the
first 128 examples does not prove that the final coordination check passed.
Coordination errors or incomplete/unknown evidence refuse quiescence actionably.
Re-admit and refresh for later Complete attempts, then run ordinary full readiness
after joining/detaching. Preserve the executor's independent coordination checks
and journal binding; this snapshot creates no new reservation or cleanup power.

Only the exact current worker's epoch/owned handle may reconcile a CLI projection
that cannot see that handle. Genuine unknown local effects remain blocked.
P2 owns this sequencing; P1's authorization callback accepts the admitted path,
not caller assertions. No new core signature, journal, framework or live action.

## A16: complete A14 delivery and MCP helper cutover

The source predicate below remains correct. A17 establishes a supported,
conditional recovery through the old resolution contract; it supersedes A16's
unsettled bootstrap dependency and A13's requirement that this observed CI end.

**Bootstrap hold, final bounded source check:** root reports complete candidate
`b9b408710e5c20ffa470afde10e4f7afc33919d2` committed with quick checks passing.
The policy-2 source/target contract comparison below is valid, but it is not
sufficient to admit our known old monitor state. Installed eabb
`portal/internal/monitoroperation/lifecycle.go:142` checks
`HasUnresolvedEffects(op)` unconditionally, before the `executionOnly` branch.
`service.go:249` returns true for a terminal `incomplete` report without a
Resolution, independently of native activity. `maintenance_monitor.go:44` rejects
unresolved inventory and line 49 calls `RequireIdle(..., false)`;
`maintenance_control.go:736` records `monitor-operation-unresolved` and line 826
refuses preparation when blockers exist. Thus known legacy 63/8 still block the
old source, despite Q's terminal local/native evidence. No remote CI query is
performed by this predicate; the old combined report semantics cause refusal.

Ordinary eabb-to-policy-2 maintenance is **not yet operationally feasible** for
this state. Existing `maintenanceProtocolOwner` at lines 110-146 routes even
prepare/recovery to the saved source package, and Ruby worker dispatch retains
that source owner. Invoking the target/candidate executable alone does not replace
this predicate. The remaining dependency is a separately accepted, supported
source-bound bootstrap/recovery path that can preserve the old immutable reports
while proving local safety; no such exception was established by A16. Do not run
the known-refusing switch, fake Resolution, rewrite records or force a restart.
Root must settle that dependency before activation; final independent review and
CI preparation may continue. This finding uses installed source and existing Q
facts only, with no repeated CI/process/native/monitor reads or mutation.

Only the final combined monitor core, worker, archive integration, caller policy
and corrected validations are a delivery candidate. Component
`269e2e92849f7920b59cb1817beee4fdd9fe0a17` is not a deployable A14 result.
Root accepts/releases implementation and the final published head; this brief
authorizes no live transition, observer write or session lifecycle action.

### Sufficient P1 cutover correction brief

**Decision:** advance the existing integer `livePackageSwitchPolicy` from **1 to
2**. Keep `workspaceReportingPolicy = 3`, its exact startup arguments/tool names,
native executable, schema-1 monitor data and retained reporting-policy-1/2/3
validation/replay unchanged. Policy 2 identifies the complete observer-aware MCP
tool/response surface and requires one normal daemon/helper cutover from policy 1.
Do not mark old launch provenance as policy 2 or normalize across this boundary.

Source proof at eabb: `libexec/workspace-host:2410` reads each package's live
policy and compares it with the executing host's own contract value. A mismatch
returns false; it is not a target-package rejection. `codex_restart_required?`
at 2389 and `registration_restart_required?` at 2394 turn that false result into
ordinary restart admission, including the original launch package. All references
to this policy in the installed runtime were checked; no separate source gate
requires a target value of 1. Source strict reporting validation at 1891/1913
continues accepting the unchanged policy-3 invocation, and its monitor-state
reader gate at 3162 remains satisfied. Bumping reporting policy to an unsupported
value would not provide this source-compatible path.

The target host compiled with policy 2 similarly rejects policy-1 launch evidence
for live preservation and performs its normal activation/reconciliation. Only an
actual restart publishes the target launch marker. Once both selected and launch
packages have policy 2, unchanged native/normalized invocation can again switch
live. Retained policy-1/2/3 reporting proofs remain readable; their live-package
epoch determines restart eligibility independently of their reporting format.

**Owner/files:** P1 owns `portal/internal/session/runtime-contract.json`, existing
generated contract assertions if required, focused
`test/workspace_host/live_switch_test.rb`,
`test/workspace_host/maintenance_test.rb` and corresponding source/target fixture
support. Update the existing switching/reporting sections of
`docs/workspace-portal.md` and `docs/workspace-updates.md` to explain this boundary.
No new host switch flag, journal, daemon, protocol or arbitrary restart helper.
Existing production host comparison should suffice; a contrary fixture/source
finding returns to root before extending behavior. P2 stays independent.

**Ordinary operation:** retain the claim-bound
`workspace-host switch --source FINAL_WORKSPACE_SOURCE` entry point. The existing
`libexec/workspace-maintenance.rb:251` uses the same restart predicate, preserves
source ownership/deadline/grants, and requires the existing target maintenance
contracts (schema 2, policy 2, held-completion 1). Thus an eabb source can admit
the candidate through its existing bounded maintenance flow. The ordinary idle
path still refuses active/unknown execution when maintenance is unavailable;
there is no forced service stop or alternate native launch. Recovery uses the
same saved operation/forward target, never a fresh operation to hide uncertainty.

**Focused proof before release:** exercise a frozen policy-1/eabb source executor
admitting a policy-2 candidate with identical native binary and policy-3 argv,
then the actual target activation path. Do not merely run a new host with both
fixtures inheriting its new default value. Prove maintenance/restart is selected,
busy/unknown ordinary admission refuses safely, target marker/helper is actually
replaced, and later 2-to-2 package-only updates preserve the new daemon. Preserve
old reporting-policy-1/2/3 and immutable schema-1 replay tests. Exercise interrupted
cutover and same-operation recovery without duplicate resumes or lost receipts.
After review, affected packaged/native verification must show the new helper's
response decoder works through the existing daemon-start transport. **S1/A32
supersedes the original A16/A20 attestation-field discriminator:** use the existing
retained native operation's successful `monitor_operation status` response with
`executionOwner:"native"`, schema1 and exact operation/workspace/owner/root.
Eabb/D's strict bare-Operation decoder rejects that remaining field; S1's retained
NativeStatus decoder accepts it. The original gate used `attest-local` and native
digests, now removed, as version evidence; preserve that historical rationale
without preserving the API. Unchanged input inventory alone is no version proof.
A freshly spawned standalone helper or a selected package path alone is not
proof that a retained conversation uses the new decoder. No live observer write,
attestation/start/cancel or new test mechanism is part of this replacement gate;
the A20 rollout procedure retains ordinary identity/generation/no-new-turn checks.

This brief is sufficient for root to release P1's bounded correction; F3 waits
for the complete corrected, reviewed, accepted and published runtime head.

### Sufficient dependent F3 paired-pin brief

Fresh SSH defaults at `2026-11-13T12:49:57Z`: runtime
`eabb56a278bd8eb1759041467eaebfa6392ddcb2`, configuration
`6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494`, workspace
`5e06283bc46670bdd922bdf04fd549ac2e27060d`, extension
`cdeb36a748acf1cd1ff1bab8fc8edce60966ec6f`. All are unchanged; live system/profile
and immutable graph hashes also match the prior proven deployment. See the A16
rollout checkpoint; no feature-preservation/product-choice question reopened.

F3 retains implementer0 as the proposed pin owner; root confirms capacity and
releases it after P2's existing package boundary. The owner updates only the normal paired inputs after
root supplies the accepted/reviewed/published **complete** runtime head. Config
starts at `6e9ed6fb`; workspace starts at the current own functional successor
`9be40723b9c982c02f9fb745556aedaebd3d15e4` of `5e06283b`. Preserve that caller-policy
commit's `AGENTS.md`, `docs/agent-instructions/verification.md` and
`docs/agent-teams.md` changes. It is functional content requiring final review,
not a disposable tracking or intermediate pin commit.

Configuration `flake.nix:134` still maps channel `dev-workspace`, role
`devWorkspace`, to input `devWorkspace`. In its declared Nix environment use
`confctl inputs channel set --commit dev-workspace devWorkspace FINAL_RUNTIME_SHA`;
preserve generated history/hooks. In the workspace feature change only the direct
`inputs.vpsfree-dev-workspace.inputs.dev-workspace.url`, then generate its lock
with `nix flake update vpsfree-dev-workspace/dev-workspace`. Retain one final pin
per stream; do not rewrite already integrated history or remove retention refs.

Preserve extension `0c7168f352f6d4f11c46368e702b9356d81012c6` and its `hhW...` NAR
hash, all other 34 workspace/63 config nodes, follows and root mappings, native
Codex/llm-agents and codex-web. No extension-master integration or feature import.
Record full before/after graphs and lock hashes, run the existing
`bin/check-dev-workspace-deployment --workspace-root PATH --configuration-root PATH`,
and report exact final heads, generated diffs/history and clean owned trees.
Unexpected transitive or source drift returns to root; do not silently broaden.

Build/copy, system/profile selection, actual MCP cutover, first observer use and
the three approved master integrations remain dependent on final review/checks
and root execution. A16 performs none of them. The source/target observer schema
and lifecycle capabilities must both be 1 before first new observer state;
installed eabb lacks them and cannot be a rollback target afterward. Keep old
schema-1 reports and remote queued outcomes unchanged. Recover the same forward
maintenance/package operation; never delete state or force a service to pass.

## A17: supported resolution of completed observation effects

**Sufficient contract finding; no implementation package needed.** The old exact-lead
`resolve` action can acknowledge the completed effects of these two observation-only
operations while explicitly retaining the independently existing queued CI and their
original `incomplete` outcomes. This is a source-scope interpretation supported by
the installed contract and Q's complete effects inventory, not by the permissiveness
of its evidence strings. Root owns acceptance and any action; A17 invokes nothing.

Controlling installed eabb guidance, under
`/nix/store/6sbb6vy4hiz957zndxc8amcc2r89f1wp-source`:

- `skills/dev-session-monitor/SKILL.md:32-34`: “The watcher owns a new local run.
  An existing run needs independently accessible status and logs; do not relaunch
  it to obtain a tool handle.” The supplied assignment and Q inventory establish
  that these utilities only observed the pre-existing run; chronology alone is
  not an ownership proof.
- The same skill at lines 65-74 permits immutable resolution after native and
  receipt proof and requires evidence to “account for the source command and
  every known operation-owned code cell or tool session.” Known uncertainty stays
  fenced. It does not require successful verification or make observation the
  owner of an independently running remote job.
- `docs/dev-sessions.md:264-283` says resolution “clears only the external-effects
  fence” and “changes no original source, outcome or receipt.” The skill's
  authoritative CI-conclusion requirement at lines 132-147 governs reporting
  `passed`/`failed`; neither report is being replaced or promoted by resolution.

Apply this only to `63e94315-36d3-4455-87d0-69f78f1e71ef` and
`8c0c1246-5469-419b-aacd-a2e0f38e87d9`, owned by this session's exact lead. Q in
[verification.md](verification.md#q-own-archive-preparation-monitor-evidence-2026-11-12)
accounts for all 47 outer calls and all 26 native command completions. In
particular, the original poller's exact producer receipt
`exec-b5e058f6-4f3b-4454-94b2-2471fbf3b1c1`, tool session `33520`, ended at
`2026-11-11T21:03:56.170Z`, failed/exit `-1`; the cause is unknown. This positive
receipt, rather than PID absence or an earlier idle turn, settles the local
invocation. The second utility launched no replacement long-running observer.

Resolution evidence must preserve the exact source tuple: `aither64/dev-workspace`,
run `43095435241`, attempt `1`, workflow `354263807`, head
`359636df4e38b3f8c4049eb7e894c3c5eeca2625`. Root's latest supplied evidence still
reports queued/null; ordinary and documented force-cancel each returned 409
“not been queued yet.” These are failed cancellation requests, not terminal
proof. Detail must say the obsolete observation has ended, remote CI remains
queued with no conclusion, and these utilities neither launched that remote run
nor owned a deployment/resource mutation. Original incomplete reports and their
source uncertainty remain unchanged. No blanket exemption for CI, English
`none` parsing, reassigned ownership or claim that all remote effects are harmless.

The existing runtime supplies additional mandatory guards:
`portal/internal/monitoroperation/service.go:266-325` revalidates exact lead/owner
under session and operation locks, requires `CheckResolution`, stores one immutable
resolution and cancels only eligible unsent delivery. It does not rewrite reports
or contact GitHub. `lifecycle.go:67-129` rejects unknown launch/submission receipts
and requires exact native thread quiescence. Q does not replace those fresh checks.
Any refusal or newly uncertain local/mutation effect stops this route; no private
edit, forced native action or conflicting resolution retry follows.

Root may use a separate stable `resolutionId` for each operation with bounded
nonempty evidence/detail, saving original public status and the returned audit.
An uncertain response is retried only with the identical ID and payload. Only
successful supported resolutions remove the old `HasUnresolvedEffects` predicate
for these records; all other maintenance, identity, ownership and receipt gates
remain. This uses the old schema-1 resolution, not a new observer attestation,
and needs no new MCP helper or auxiliary record before cutover.

This corrects A13's interpretation, also quoted in Q's historical conclusion,
that queued remote CI necessarily prevents resolution of completed observation
effects. Q's underlying facts and immutable outcomes remain intact. A16's ordinary
source-owned policy-2 maintenance and recovery then remain the proposed upgrade
path, subject to root's actual admission and final review/CI/deployment gates.
The reviewed `4f99` runtime and F3 pins `29075f2c` / `689753e0` are unchanged.
No policy-1 bridge or further bootstrap exploration is needed on this evidence.

## A18: configuration-only freshness refresh

**Sufficient brief; no runtime or workspace change.** Canonical configuration
`355e269f034422bb042f6c39fdab1725855b47e0` is one direct child of the prepared
base `6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494`. Its only changed path is
`.github/workflows/daily-update.yml` (8 additions, 6 deletions), commit
`ci: reuse the initial daily update shell`. It saves the initial Nix development
shell in a runner-temporary profile and reuses it for later workflow steps so
input updates cannot mix Ruby/native gems/hooks from different shells.

The old/new root trees are `eb16da10b23926463cb010740f7bce066eeb948a` and
`bf06206a618e4d1745f787f4b1371145b733c88b`. `flake.lock` is the same blob
`d9d60da6848ef9a34c5487e040ea0a8b78817d58`; `flake.nix` and all other tracked
files are unchanged. The identical cluster/modules/profiles/configs/packages/
overlays trees prove no aitherdev host configuration, runtime selection, input
graph, capability, native or persisted-state change in this upstream advance.
No potential live feature loss is exposed, so A18 needs no live metadata query.

Prepared configuration `5bb204005ab2790945410b715138bd3a820f8427` is one direct
child of old `6e9`, changing only the generated lock's `devWorkspace` revision,
NAR hash and lastModified. It selects accepted runtime
`1e5f566e4dc77a7d45d545b06bf345bdf5d82edc`,
`sha256-63McCeJCOYHQj0jjH20a18G6pwl2i4E81r1Ye46rQvA=`, timestamp `1794580865`.
This patch is disjoint from the upstream workflow change. Workspace
`14162a86a97ae70253200c2873c09cde4ea16d2b` and its exact caller policy `9be40723b`
remain unchanged; no runtime rebase or new runtime CI follows from this drift.

Root can release implementer0 for one bounded configuration-only replay after
reconciling the ongoing old-head build and granting its source window. Retain
the old `6e9..5bb` source/build/review receipts and head, then replay that one
unchanged generated pin onto exact `355e269f` using ordinary Git in the declared
Nix environment. Preserve upstream workflow bytes and generated commit history;
do not regenerate unrelated inputs or edit the workflow. Stop on a conflict,
unexpected base change, hook failure or any non-equivalent patch. No source
mutation is performed or released by A18 itself.

Acceptance is one pin commit above `355`, equal range-diff/patch and exact
prepared lock bytes (SHA256
`8e2d35e2fb004a853f0bd1aaf1acd34f1d74bc3442a0ea495b156bf6ddbdb4d7`), unchanged
63 sibling nodes/follows/native/extension, normal hooks and clean final history.
Repeat the ordinary paired checker against unchanged workspace `14162` and the
refreshed config. Update R11's exact base/head and mechanical-history disposition;
the already integrated upstream workflow is not new feature scope to reimplement
or independently redesign. Any substantive deviation returns to root for review.

Runtime review/CI and workspace profile/native checks retain their exact `1e5` /
`14162` scope and do not need reruns merely for this configuration advance.
Build `27006` remains evidence for `5bb` only; A18 neither polls nor interrupts it.
No refreshed system derivation has been evaluated here. Identical input locks do
not establish identical system derivations or configuration provenance: retain
the old result, then obtain the ordinary exact-final-config generation/build and
copy receipt. Reuse cached outputs only with actual derivation/input identity;
never relabel `5bb`'s embedded revision as the refreshed head. Existing deployment,
MCP cutover, recovery and three-target integration gates are unchanged.

## C5: threadless archive monitor response

**Sufficient bounded correction; P1 implements only after root releases source.**
At exact `1e5f566e4dc77a7d45d545b06bf345bdf5d82edc`, completed archive job
`131955004087` fails ordinary `2026-10-17-roundtrip` after the earlier observer
fixture creates the workspace monitor store. Existing log
`/tmp/session-archival-ci-43445868248/archive-failure.log:4941` reports
`monitor shutdown returned invalid output`; line 4985 retains an empty target
thread, ready 6/6 and `monitorLocal:{state:quiescent,operationIds:[]}`. No new
download, reproduction or runtime observation is needed for this source defect.

`portal/cmd/workspace-portal/monitor.go:272-282` proves both owned stores empty,
but returns success without stdout for threadless `begin-archive` and
`complete-archive`. Ruby `libexec/dev-session:1957-1990` requires the existing
JSON envelope and selected authority. Empty stdout is not that protocol. The
proposal to reuse the existing admitted adapter is sufficient; no new policy,
schema, authority record or lifecycle action is needed.

Keep `monitorAcceptedArchive` and core signatures unchanged. Route these two
actions through the actual adapter in `monitor_archive.go:167-227`, including
selected-generation proof, exact inherited admitted-parent EX descriptor when
there is no receipt, ordinary current target/root/journal selection, and
`web.ValidateMonitorArchiveAuthority` for the real browser receipt or CLI target.
The parent still owns confirmation, provider/resource admission and lock lifetime.
An empty caller flag alone must not establish threadlessness or admission.

Only after that validation, and a fresh successful empty list of **both** legacy
monitor operations and auxiliary observers for the exact slug, return the same
envelope as the nonempty-root adapter:

```json
{"authority":{"slug":"ACTUAL_SLUG","rootThreadId":"","operationId":"ACTUAL_64_HEX_ID","targetId":"ACTUAL_V2_TARGET","mode":"ACTUAL_ACCEPTED_MODE"},"local":{"state":"quiescent","operationIds":[]},"pending":false}
```

Include the actual `receiptId` when present, using the existing optional field.
Keep the genuine empty root, non-null empty operation array, and boolean false.
Preserve all existing scalar/ID validation: canonical selected operation/target,
bounded mode/receipt and exact journal/receipt consistency. Do not bypass those
checks merely because core Begin/Complete are skipped. Use existing authority
selection for any fresh CLI ID; Ruby retains the returned ID for Complete and
its later ordinary journal. Existing receipt/journal IDs are never replaced.

The narrow no-op branch must verify the retained manifest is actually normalized
threadless, reusing `session.RequireNormalizedThreadless` where needed, and
refuse any root mismatch, creation/conversation evidence, malformed/unreadable
store, retained operation or observer, or changed/conflicting admission. Existing
target identity explicitly represents absent root (`lifecycle_target.go:44-49`),
and `ObservationIdentity` also supports explicit absence. No synthetic native
root/client proof or fake `ArchiveAuthority` is required.

Keep `monitoroperation.validateArchive`'s real-root requirement unchanged
(`observer_validation.go:33-39`). With no records there is no core quiescence,
revocation, native call, detach, attestation or observer write to perform. This
is an admitted empty monitor result, not successful archival or permission to
skip subsequent Ruby threadless-runtime/readiness/cleanup/journal guards. A crash
before any ordinary journal and with no monitor record leaves no observer effect
to recover; ordinary admission applies again without inventing a persisted binding.

P1 owns `monitor.go`, `monitor_archive.go` and focused adapter/command regressions.
Cover valid threadless CLI-parent and real-browser-receipt Begin/Complete JSON,
same returned ID, retained records/errors refusing, and invalid generation,
descriptor, target/root/receipt refusing. Keep nonthreadless core rejection and
existing threadless readiness checks. Root coordinates source/index windows,
quick checks, affected final review and the exact final archive CI; the existing
roundtrip assertion remains intact. A18's configuration refresh will select this
eventual accepted runtime successor, not create another interim `1e5` pin.

## A19: sufficient F4 source release and host verification boundary

**Source brief settled; root may release F4 independently of later build/health
evidence.** Implementer0 retains F4 ownership. Configuration base is exactly
`454c94c4eb1315f74e23b2126187c2a27eb3868a`, preserving every integrated workflow,
Gemfile/gemset and input update. Workspace retains exact functional caller-policy
`9be40723b9c982c02f9fb745556aedaebd3d15e4` above master `5e06283b`; preserve its
three policy files. Both final pins select published, R12-reviewed runtime
`9678f71d44780d3c49130372e7944a770fc5e3b6`. No runtime rebase or additional
runtime CI is required by configuration-only baseline drift; root already owns
the exact-head CI. Old build `27006` is joined, per root's supplied receipt.

Retain old `6e9..5bb20400` / `5e..14162a86` heads and all exact-head receipts,
then use ordinary clean history consolidation and the existing generators for
one final pin per repository. Config uses its unchanged channel/role mapping:
`confctl inputs channel set --commit dev-workspace devWorkspace 9678f71d44780d3c49130372e7944a770fc5e3b6`.
Workspace changes only the direct nested runtime URL and runs
`nix flake update vpsfree-dev-workspace/dev-workspace`. Use the current declared
Nix/Bundler/hooks, not old installed gems; preserve generated commit history.

Canonical lock traversal proves config's runtime subtree has nine nodes, with
all eight dependencies identical to frozen workspace `14162`. Their root runtime
identities differ (config eabb, workspace 1e5); do not call the complete graphs
equal before both final pins. Runtime `1e5..9678` has byte-identical `flake.nix`
and `flake.lock`. Preserve those eight dependency identities/edges, configuration's
other 63 nodes **from new base 454**, workspace's other 34 nodes, root mappings,
follows, extension `0c7168f`/`hhW...`, native selection and caller policy. Do not
restore old `6e9` sibling inputs or update the independent root llm-agents to
match runtime's intentionally separate dependency.

Acceptance: clean exact final heads, one generated pin above config `454`, exact
`9be` then one workspace pin, whole-graph preservation against these respective
bases, matching final runtime NAR/revision and resolved nine-node graphs, normal
hooks and the existing paired checker. Stop on conflicts, unexpected dependency
changes or a newer baseline; return the concrete difference to root. Root owns
source windows, final mechanical history/review disposition and publication.
No source edits, ref changes or checks are performed by A19.

System evidence is separate: root stable nixpkgs and root llm-agents advanced,
so old system builds cannot establish the final host derivation or native
environment. Obtain final system generation/build/copy, scoped dry activation and
health evidence. The unchanged runtime dependencies do not establish equality of
system or profile outputs. R12/exact `9678` CI remain the runtime evidence; old
`1e5` successes remain historical and retain only their proven scope.

### A19 host and selection evidence

Config `355..454` contains seven integrated dependency commits; the earlier
`6e9..355` workflow-only change remains preserved. Host source, `flake.nix`,
AGENTS, provider/auth/network declarations and channel mappings are unchanged.
The nine changed lock nodes are `flake-parts_2`, `llm-agents_2`,
`nixpkgsProduction`, `nixpkgsStable`, `nixpkgsStaging`, `nixpkgsUnstable_2`,
`nixpkgs_5`, `vpsadminosOsStaging` and `vpsadminosStaging`. These are outside the
runtime subtree. Home-manager's revision is unchanged, but its followed stable
nixpkgs advances. Full lock SHA256 at `454` is
`2c71b5fb264bfeac6cf555576c7f63c86365d3b2ab0956f4e1260ca8215476cb`.

`cluster/cz.vpsfree/machines/aitherdev/module.nix:6-11` selects only nixos-stable,
home-manager, llm-agents and dev-workspace channels. `config.nix:14-21,105-106,224`
uses root stable pkgs for the system/home environment and root llm-agents for the
system Codex wrapper; `codex-ds` uses that same wrapper. These dependencies really
change, though no host behavior declaration was edited. Geminabox/ssh-exporter
updates are retained upstream packages, not newly enabled aitherdev services;
vpsAdminOS channels do not turn this standalone NixOS host into a node upgrade.
The root Gemfile update changes the config development/hooks environment, including
Overcommit 0.73 to 0.76; use its declared environment without bypassing hooks.

Managed native selection is separate. Runtime `9678:flake.nix:25-44` builds its
Codex from runtime-owned llm-agents `91ff550fe42d4dd51dcf8b6bad87a0134fe7f314`;
`nix/workspace-portal.nix:346` embeds that package under `libexec/codex`.
Configuration's root llm-agents now selects `860075d9`, independently. A new
system `codex` on PATH does not prove that the active managed daemon changed or
that the new helper schema is usable. No new system Codex version/derivation is
claimed before evaluation; record the actual output in the final build receipt.

The one permitted live metadata checkpoint still found both system links at
`/nix/store/vx0p926axyld6ih648184wbc63lqjj4w-nixos-system-aitherdev-26.05.20261026.718f670`,
clean config `6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494`, and selected profile
`/nix/store/0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`. No new live
lineage/product choice is exposed. Root performs final prepared system and
profile build/copy, dry activation and configured health checks, then the existing
authorized system-before-profile maintenance/cutover flow under fresh ownership.
Verify exact system/config provenance, SSH/router/HTTPS health, own retained
conversation/catalog/naming status, actual managed native/helper selection and
new tool surface before first observer write. Do not add other-host tests or
remote CI observation merely for these config inputs.

Retain both old and final system/profile generations and source/input graphs.
An ordinary package refusal or interrupted maintenance uses its existing saved
source-owned operation and recovery, without force or new operation IDs. Old
eabb is not a rollback reader once new observer state exists; retain the accepted
forward-compatible recovery rule and first-write gate. No new migration, schema
or product decision is introduced by this configuration reconciliation.

## A23 — source prepare refusal diagnostic boundary

The source-owned `eabb` prepare for `5d13febb-8cb8-488c-8c66-fd0e5ca9d683`
failed before an accepted operation was persisted. Root proved its directory
and journal absent, global maintenance status `none`, caller joined 1 and profile
still `0s5`. The worker launch follows successful prepare, so `recover` is not
a supported way to retry this unaccepted request. System deployment already
succeeded; machine ownership remains with root. Final source/pins stay frozen.

The exact failed predicate is unavailable: the controller maps unclassified
prepare errors to `identity-or-proof-refused` without retaining the underlying
error. Its possible inventory blockers are not proof of the observed cause;
known historical own monitor resolutions must not be repeated. See
[A23 in rollout.md](rollout.md#a23-prepare-refusal-no-accepted-operation-and-lost-diagnostic)
for exact source lines, persistence ordering and operational evidence.

No additional implementation package is released. If root assigns a diagnostic
correction, its minimum boundary is bounded allowlisted prepare-stage/reason
reporting through existing `ProofError` and `Response.reason`, preserving all
admission, ownership, native effects and persistence semantics. It must not emit
raw native/peer data, create an operation on refusal or imply that the old cause
was recovered. Candidate-only instrumentation cannot observe the old source's
prepare, which is explicitly routed back to its immutable package. No source
replacement, bridge, private helper, retry or force route is proposed by A23.

## A24 — sufficient source-compatible diagnostic repair brief

**Settled route; implementation requires root release.** Build a complete repair
`D = eabb56a278bd8eb1759041467eaebfa6392ddcb2 + one diagnostic commit` and select
its ordinary configured profile with `workspace-host switch --source D_WORKSPACE`
under the existing exact session/machine claim. Preserve the current maintenance
enablement; do not add `--enable-maintenance` to this first switch. D changes
diagnostics only: no A14 observer code, state/schema, native executable, reporting
tools/decoder, launch arguments, registration policy, capability or input changes.
It retains `livePackageSwitchPolicy=1`, reporting policy 3, registration policy 1
and maintenance schema 2 / policy 2 / held-completion policy 1.

### Why this ordinary path can precede the blocked census

At eabb, `libexec/workspace-host:626-649` invokes maintenance only when
`workspace-maintenance.rb:251-256,347-348` finds a required native restart.
`workspace-host:2129-2148,2389-2418` requires the same resolved native, storage,
launch policy, capacity and complete validated reporting invocation. Only the
package-dependent MCP executable path is normalized. Both packages and the
actual launch package must advertise live policy 1. D preserves every static
input to this predicate; ordinary admission still proves the actual markers.
The source may not be replaced merely by relabeling a policy-2 package as policy 1.

Target activation repeats that predicate (`workspace-host:1211-1241`); its
no-restart reconciliation refreshes registration inventory and clears matching
pending state without native census, quiescence or restart (`2320-2337`). The
immutable launch marker stays unchanged (`2080-2088`); portal/router restart and
normal host activation effects still occur. Preparation and activation retain
all lifecycle, creation, provider, cluster, claim and generation checks. A23's
absent operation provides no recovery authority and is not rewritten.

After successful selection, `preselection_session_package:2562-2565` and
`prepare_profile:706-714` bind a later ordinary final-target maintenance request
to D. `maintenance_control.go:109-145` then dispatches to D as its true source
owner. The final A14 target retains live policy 2 and its required native/helper
cutover; D does not make that step a live switch or weaken its census. Existing
source/target maintenance contracts admit this ordered transition. This is
source feasibility, not proof of the future candidate's actual activation.

### Narrow implementation and checks

One implementer, allocated by root, owns
`portal/cmd/workspace-portal/maintenance_control.go` and focused fixtures in
`maintenance_control_test.go` / `maintenance_inventory_test.go`; reuse the
existing monitor inventory fixture only if needed for its real blocker case.
Add a small explanation to `docs/workspace-updates.md`. No host, marker, MCP,
store format, admission or native behavior changes. A focused policy-3 variant
of the existing `test/workspace_host/live_switch_test.rb` fixture may establish
the exact composition transition without changing production host code.

Expose only program-selected, finite reason codes through existing `ProofError`
and `Response.reason`. Distinguish prepare target/identity validation, source
process/executable/socket capture, inventory acquisition and operation creation
failures. Within inventory, identify the existing exact refusal sites (ownership
ambiguity versus unavailable metadata/native proof) and the existing blocker
categories `monitor-operation-unresolved`, `retained-member-transition`, and
`unowned-loaded-writer`. Preserve all simultaneously observed blocker categories
in a bounded deterministic allowlisted reason; do not guess which one matters.
Preserve existing typed proof, cancellation and timeout reasons. Unknown errors
receive a fixed stage fallback, never `err.Error()` or substring-derived output.
No session/thread IDs, paths, native payloads or raw errors cross the boundary.
For D1's existing child inventory call, exact equality with the source constant
`ambiguous native child ownership` (`maintenance_pause.go:55-56` at eabb) may map
to the same fixed ownership-ambiguous reason in the owned caller. Other errors
and decorated/near-match text retain the stage fallback; preserve typed proof,
cancellation and timeout precedence. This requires no helper-file change.
Do not create a journal/receipt to retain a rejected preparation, add diagnostics
flags/private entry points, change accepted operation contents, or bypass a gate.

Quick checks in the declared Nix environment: focused maintenance Go tests
(`go -C portal test -mod=readonly ./cmd/workspace-portal -run 'TestMaintenance'`),
the affected Ruby live-switch tests and syntax where changed. Cover each
diagnostic branch, mixed blocker categories, raw-error sentinels/redaction,
unchanged typed/time-bound outcomes, and absence of operation/startup writes on
pre-creation refusal. Preserve existing partial-persistence recovery on an I/O
failure during Create; do not erase a successfully written operation. Prove
successful prepare behavior unchanged. The host fixture must
prove policy-1/reporting-3 package-path change preserves native/marker, skips
maintenance inventory and retains normal claim/forward-recovery behavior; a
policy-2 target must still take maintenance. Stop on any need to relax those
predicates or edit launch/contract machinery.

Before selecting D: complete quick checks, commit and independent affected
review, then ordinary exact-D package/required CI and the existing host
activation/live-switch acceptance. Build the actual configured D composition;
record its full graph, native path, contract and normalized registration equality.
Use existing retained source/derivation receipts only within proven scope; 9678
CI/builds do not validate D. No new model/session/observer/lifecycle smoke is
introduced. Root's bounded deployment proof is exact selected D, unchanged native
process/socket/launch marker, new inventory, portal/router health, retained own
conversation and no unresolved transition effects. Stop on unexpected restart
requirements. A preselection refusal leaves the predecessor; a failure after
selection retains D and its pending evidence for ordinary same-source forward
recovery (`workspace-host:793-816`, `docs/workspace-portal.md` live-switch section).

### Composition, source history and final delivery

Preserve frozen `9678` / config `72cb` / workspace `35bd` and all their exact-head
evidence. Prepare a separate ordinary matching D workspace/configuration input
pair with the normal nested runtime override, confctl channel generator and
paired checker. Preserve extension/native/follows and every unrelated input and
site contract; no direct generic-package substitution. The already deployed
system `72cb` remains selected during diagnosis. No procedure imposes an
unconditional second system deployment for an application-only profile change:
deployment guidance explicitly separates application profile and system
substrate. However, a matching temporary source pair is not proof of the live
system's derivation equality. Root must prove staged profile/host-contract
compatibility; if the actual candidate needs changed host configuration, stop
and return that concrete dependency instead of assuming compatibility. The
source `eabb..9678` production Nix modules are unchanged (the Nix delta is the
archive VM fixture); this supports the narrow route but does not certify a new
artifact's identity.

Root's explicit A24 history decision is to retain consumed D as a separate
logical source-owned checkpoint, then prepare the final A14 successor **atop D**
while preserving the reviewed 9678 checkpoint and patch evidence. D may become
the immutable recovery owner of the later operation and must remain available.
No automatic rewrite of frozen heads or merge occurs here. The successor needs
its own affected review, exact-head CI, refreshed final pins and artifacts, and
verified final deployment before the three approved integrations. Do not call
9678 an ancestor containing D or reuse its build identity. No migration is added;
D remains an old reader and cannot be selected after first A14 observer state.
Normal complete deployed-lineage and command-effect proof governs eventual
machine release. No new authority or product decision is introduced by this
diagnostic route; root owns release, execution and any newly exposed blocker.

## A25 — exact-D creation acceptance with the corrected test script

**Invocation superseded by A27; do not execute the A25 command below.** A25
incorrectly inferred the realized driver's interface from retrieved upstream
source without proving installed-source equality. Root's only attempt exited 2
at argument parsing before VM construction: qxz does not support `--test-script`.
V1's frozen corrected-script and original D VM/package proofs remain valid.
[A27](#a27--realized-driver-correction-and-public-config-route) supplies the
realized-source-backed replacement through the same driver's public `--config`.
The remainder of A25 records the historical proposed method, not acceptance.

Keep runtime
`b8329e32f1132fd947f4a9c803bf44e3ed9ce481` and its temporary `98b6`/`f312`
composition frozen. CI `43472027059/1` creation remains failed. C7's recorded
cause is the exact status-1 retained-start lock refusal before admission, not
a demonstrated maintenance/native defect. The separate acceptance below runs
the complete original D VM fixture with only C7's reviewed bounded helper/call
correction. Final F still needs its own normal exact-head CI and managed checks.

D locks nixpkgs to `f20cd90e28fe0403873f473b29e42662cd86e8c4`.
Its public [driver entry point](https://github.com/NixOS/nixpkgs/blob/f20cd90e28fe0403873f473b29e42662cd86e8c4/nixos/lib/test-driver/src/test_driver/__init__.py#L85)
accepts `--test-script`; lines 160-168 load the original configuration and
replace only its script path. The original wrapper retains its configuration,
and its output includes the rendered `test-script`; the test exposes the
ordinary `.driver` attribute ([driver.nix:98-109,229](https://github.com/NixOS/nixpkgs/blob/f20cd90e28fe0403873f473b29e42662cd86e8c4/nixos/lib/testing/driver.nix#L98)).
The [configuration](https://github.com/NixOS/nixpkgs/blob/f20cd90e28fe0403873f473b29e42662cd86e8c4/nixos/lib/testing/driver-configuration.nix#L60)
separately fixes VM start scripts, networks and timeout. The
[driver](https://github.com/NixOS/nixpkgs/blob/f20cd90e28fe0403873f473b29e42662cd86e8c4/nixos/lib/test-driver/src/test_driver/driver.py#L143)
uses those unchanged fields to construct machines and its timeout while reading
the selected script. No private helper or replacement VM configuration is needed.

### Inputs, provenance and root-owned execution

Use the clean exact-D source already retained by root. Realize or reuse its
original driver, not F's driver and not a newly edited D fixture. Preparation
may build missing original closure outputs; it must not change D's derivation
identity. Minimal ordinary command, for root's assigned verification owner:

```sh
A25_D_DRIVER=$(nix build --no-link --print-out-paths \
  "$A25_D_SOURCE#checks.x86_64-linux.session-creation.driver")
cp "$A25_D_DRIVER/test-script" "$A25_EVIDENCE_DIR/test-script.d-original.py"
```

All variables select explicit absolute owned source/artifact paths; require one
driver output. Retain its derivation/output, embedded configuration and VM
start-script identities, and compare them with the original D fixture evidence
from the failed job. If the comparison cannot establish equality, stop before
execution and resolve the source/artifact mismatch; do not infer equality from
the application revision alone.

C7's owner prepares `A25_CORRECTED_SCRIPT` from that **D-rendered** script by
applying only the accepted helper and retained-start call delta. Save both script
hashes, the exact C7 commit/blob and complete rendered diff. Every original
ordered store-path reference, including D package, maintenance target, browser,
Python and native fixture dependencies, must remain identical. Do not render
the whole F script and substitute it: its interpolated package paths select F.
D's fixture at lines 160-175 already includes its original package and
maintenance target in the VM; lines 187-188 bind those exact paths in Python.
All later identity, client, native, maintenance/worker and recovery assertions
remain unchanged. Preserve the exact status/text match, one 20-second bound
and fatal handling of every other failure from accepted C7.

After C7 quick checks and required affected review, run once from a fresh owned
directory, with a separate existing output directory:

```sh
cd "$A25_RUN_DIR"
"$A25_D_DRIVER/bin/nixos-test-driver" \
  --test-script "$A25_CORRECTED_SCRIPT" \
  -o "$A25_OUTPUT_DIR" --junit-xml junit.xml
```

Do not pass interactive, retained-machine-state, custom-config or debug options.
Use the original configured global timeout and all original assertions; no
subtest omission. The public script override does not rerun Nix's script lint
or type checks, so old D driver-build success cannot validate the corrected
harness. Bind C7's focused helper regression and syntax/type/lint evidence to
the same Python delta before this run; any F-rendered validation reuse needs
the documented store-literal-only difference proof. Root assigns the normal
long-check watcher and keeps source/fixture ownership separate from the active
configured-D batch. A25 launches nothing.

Acceptance is exit 0 with the full original creation scenario/assertion set
completed against the proven D VM/package, plus the separate C7 harness receipt.
Retain failure output and stop on timeout, another error, changed store paths or
uncertain command/VM effects; no automatic rerun or further tolerance widening.
Report a separate exact-D packaged creation acceptance result, never a successful
D CI run or a successful original D check derivation. No extra host VM, production
package rebuild for a fixture-only commit, new D pin or authority change is needed.

## A26 — sufficient F7 configuration base refresh

**Settled; root releases F7.** Fresh canonical SSH fetch confirms configuration
master `07a85cae5fdb4525e4ce2cca28a05a0888be8e0c`, one commit above prescribed
`454c94c4eb1315f74e23b2126187c2a27eb3868a`. The sole changed path is
`.github/workflows/daily-update.yml`: its `CONFCTL_FLAKE` changes from
`822c0e35dbe2549111912f539116b4225dfd3035` to
`ff5e017780a35fb97b549db2a51b570193867c3b` to scope automated update messages.
No workflow commands/flags, flake inputs, development toolchain or host declarations
change. Preserve this integrated workflow commit; no audit or upgrade of that
independent tool is part of F7.

Both bases have lock blob `0ee97248e566f8f6a5f76202b696bd420557632c`, SHA256
`2c71b5fb264bfeac6cf555576c7f63c86365d3b2ab0956f4e1260ca8215476cb`; all 64 nodes,
root mappings and follows are identical. The aitherdev subtree is unchanged at
`0a8a09cec1e27be4182ed1fc3f2ed0eebbd19710`, and the entire `modules` tree at
`c4b0e7043abd9c63c343da0729f967205a8a79c7`. AGENTS and flake.nix are unchanged.
Thus the A19/A21 host/native independence evidence remains applicable: root
stable `ac588ef1` and llm-agents `860075d9` are unchanged; no new stock or managed
Codex choice arises. The configuration runtime node is still eabb before our
pin. Runtime eabb, D b832 and final `084dcd6d88ccd18e24561364732774805db1b178`
have identical flake.nix and flake.lock blobs, preserving the eight dependency
nodes beneath that runtime root. This source result requires no live checkpoint.

Implementer0's existing F7 owns the ordinary generated final configuration pin
above **07a**, selecting root-accepted published runtime **084dcd6d88ccd18e24561364732774805db1b178**.
Use the unchanged declared Nix environment and
`confctl inputs channel set --commit dev-workspace devWorkspace REV`; preserve
the other 63 baseline nodes and mappings. Workspace stays on its already settled
base/caller-policy history with one final nested runtime pin and its other 34
nodes, extension and follows unchanged. Run the existing paired checker and
ordinary hooks; retain one final pin per stream. Configuration-only workflow
drift does not require a runtime/workspace rebase, new native scope or additional
runtime CI. The already required exact-084 CI and managed acceptance remain.

Preserve owned `72cb`/`35bd` and prepared `6d`/`b285` refs/evidence under root's
mutation windows. D source b832, diagnostic `98b6`/`f312`, their managed/native
receipts and the original D creation driver remain frozen; no retargeting or
rebuild of that pair. No changes to those sources or refs occur in A26.

Final artifact acceptance still binds the actual final config/workspace heads,
complete graphs and system/profile derivations. Workflow/tree equality is not
permission to relabel an older build: apply existing derivation/input receipt
reuse only where proven, otherwise perform the normal final scoped build/copy,
dry activation and health/selection/recovery gates. The actual deployed
`72cb`/`jma`, stock 0.167.2/provider success and selected `0s5` are root-supplied
historical/current evidence, not new reads. No new host change, migration,
product decision or extra verification matrix is introduced. Stop if canonical
base advances again or generation changes any node beyond the intended runtime.

## A27 — realized driver correction and public config route

**Sufficient static route; root releases execution.** Root's tool `4804` joined
exit 2, rejecting A25's `--test-script` before VM start. This is an A25
verification-design error, not a D application or VM result. Preserve that log,
V1's accepted artifacts and failed original D CI/check result. No VM run has been
performed by A27.

The actual chain is
`/nix/store/qxzvycghgz7034rdfkj1lbpbl6mkjkmj-nixos-test-driver-dev-workspace-session-creation/bin/nixos-test-driver`
→ its wrapped symlink →
`/nix/store/gxf3q4fva317n39j307wc4dhwg4ryqma-nixos-test-driver-1.1`.
The outer derivation `l45cvcppp0r1cfgb6dzmp9zmdrm8bj82` explicitly depends on
driver derivation `4dw5qw5n56j8m5bifv853qqv1rd34d4l`, whose output is gxf and
source is `/nix/store/s2p0s0lclav9fbrm84mkm8n4kchd4sf4-src`. Its
`test_driver/__init__.py` and gxf's installed Python module are byte-identical:
SHA256 `be3f8e47865a0fdb076380ea380da0d28e3496f990c051a31b525478bf6d6750`.
The installed entrypoint adds that exact package to its import path. Its parser
defines `--config` at lines 82-90, no `--test-script`, parses at line 136, and
loads `args.config` at lines 165-166. A25's retrieved upstream body did not prove
this packaged API; no upstream/cache/build fault is inferred from the mismatch.

The same qxz public wrapper supplies its default `--config` **before** `"$@"`.
The selected Python 3.13.15 `argparse.py:941-975` uses ordinary `_StoreAction`,
which assigns the supplied value; a later explicit `--config` selects the copy.
No alternate launcher, direct Python module call or wrapper/store edit is needed.
Installed `driver.py:39-51,151-170,184-201` loads the configuration and script,
preserving the configured VM start command and timeout.

The original configuration is
`/nix/store/10ywv4i58wjmv5272q7117ryhygfppsd-driverConfiguration.json`, SHA256
`ea6ca98cd89de9f5096a04942d1d45b0916bafbbdbc69fad2e1b87bf15c3c88e`.
Its six fields are: empty containers, SSH backdoor false, timeout 3600, VLANs
`[1]`, original test script `0vj9kxr1hffa1q2h3kn6skmbbqaxsp2s-test-script`, and
the sole machine's start script
`/nix/store/zz6c3crdh5xs1d1aid72lglqch9wgf1j-nixos-vm/bin/run-machine-vm`.
Copy that public test configuration, changing **only** `test_script` to frozen
`/tmp/session-archival-d-creation-acceptance/test-script.d-c7.py`, SHA256
`d165e94e7c592f79bd556113fbbc72c3a37a615522fb1d1bee9cfd1477ed008b`.
Preserve every other parsed field exactly, including any additional field if the
actual original differs; stop on that discrepancy rather than reconstructing it.

Minimal preparation and invocation for root's assigned owner, not executed here:

```sh
jq --arg script "$A27_V1_SCRIPT" '.test_script = $script' \
  "$A27_ORIGINAL_CONFIG" > "$A27_CONFIG_COPY"
cd "$A27_FRESH_RUN_DIR"
"$A27_ORIGINAL_DRIVER/bin/nixos-test-driver" \
  --config "$A27_CONFIG_COPY" -o "$A27_EXISTING_OUTPUT_DIR" \
  --junit-xml junit.xml
```

Bind the variables to the exact paths above and separate absolute owned output
paths. Before execution, root's preparation must record both config hashes and
prove their sole semantic difference is `test_script`; retain V1 script hash,
complete diff, original store references and all 221 unchanged assertions. Do
not re-render, edit or revalidate a different V1 script, alter global timeout,
VM configuration, packages or native/worker assertions, or pass retained-state,
interactive/debug flags. The successful V1 checks retain only their recorded
scope. This changes one public test input, not production state or authority.

Run the complete scenario once under the existing verification ownership and
timeout, subject to root release. Stop on any mismatch, failure or uncertain
effect; no retry probe or new driver/package build is justified by this interface
correction. Success remains separate exact-D acceptance with the accepted C7
harness, never a manufactured D CI/check-derivation pass. Final F keeps its normal
fresh CI/managed gates. A27 read exact immutable source/derivation/public artifacts
and amended these records only; it performed no driver, VM, build or live action.

## A28 — configuration advancement and unchanged feature publication

**Sufficient classification; no automatic refresh.** Fresh canonical SSH fetch
confirms master `7d9807e021e6106d628c021da45f5f55077b2e9c`. Above accepted
`07a85cae5fdb4525e4ce2cca28a05a0888be8e0c` it contains exactly:

- `0e66bd37ec51d5997a126e381fef68cc31438cba`: update locked confctl to ff5e0177.
- `7d9807e021e6106d628c021da45f5f55077b2e9c`: use that locked tool from the
  existing development shell in daily updates instead of an independent
  `CONFCTL_FLAKE`; one shell invocation also gains `--accept-flake-config`.

Only `.github/workflows/daily-update.yml` and `flake.lock` change. Four lock
nodes change: `confctl` (`7bee58a5` → `ff5e0177`), its `vpsadminos`
(`6f9b2c75` → `67fcc173`), and that dependency's `nixpkgs_2`
(`bd0ff2d3` → `8b8c811c`) and `nixpkgsUnstable` (`9ae611a4` → `f13ff45a`).
The root unstable input is the distinct unchanged `nixpkgsUnstable_2` node.
All aitherdev channel inputs, host declarations, native selections and runtime
nine-node subgraph remain unchanged; no Codex upgrade or runtime/workspace rebase
follows. The new lock blob is `227fb5faf3def96663292443b9dc4f87ebebdc94`, SHA256
`08212976733a03e5b879c86c0e0c38823257d2a1106e96dad3ccf57d013958c1`.
Aitherdev tree `0a8a09ce...` and modules tree `c4b0e704...` remain as in A26;
AGENTS and flake.nix are unchanged.

This is **not workflow-only**. `flake.nix:151-154` calls
`confctl.lib.mkConfctlOutputs`, and `:164-172` calls `mkConfigDevShell`.
The confctl input range changes those library/tool paths and generation code,
not just the latest message-scoping patch. This exposes a real evaluation/tool
dependency, though it does not prove changed aitherdev runtime behavior. Do not
waive that distinction or launch an unrelated upstream audit. The normal final
configuration generation/evaluation and artifact evidence must settle its actual
effect when the feature is refreshed.

**Publication need not wait for that refresh.** The Git procedure requires a
fresh fetch and rebasing when appropriate; it does not require every published
feature to contain the latest default. Root may publish unchanged exact
`e7bbb3b1b7bf6f2c80f205b0c37a1ac2d207c1ab` after the ordinary clean-head and
expected-remote-`72cb` lease checks. Its existing review and build/copy evidence
continue to describe e7, including generation `2026-11-13--19-50-57` and system
`3b5sdpdq7jaa9xcd8mibzs6nl7wpp3ap...`; this is not integration readiness or a new
artifact identity. No feature push, rebase or live action was done by A28.

For approved integration, prepare **one** refresh of the final configuration
pin onto the then-fresh default outside the short merge claim. Preserve e7 and
the exact old/new base/head ranges; retain the single runtime-084 update and all
new default nodes. Establish reconstruction/pin patch equivalence, whole-branch
history and no-migration evidence under the existing review procedure. Its
mechanical-review reuse rule cannot be inferred solely from identical feature
patch IDs when the evaluator baseline changed; root owns the bounded affected
review/reuse disposition. Runtime/workspace and frozen D need no new heads for
this configuration movement alone.

Retain the current exact system build, rather than rebuilding serial intermediate
pins for publication. A later final head must bind its actual derivation and
inputs before verification reuse is claimed. If the evaluator/host outcome
changes substantively, use a newly verified deployment; if independent evidence
establishes an equivalent successor, preserve that deployed-lineage proof and do
not call nonancestor e7 literally merged. New default movement does not invalidate
the old artifact, nor does the old artifact prove the new output. No claim release
or completion is inferred. Root decides the final preparation/activation order;
no additional live, native or CI inventory is needed for this classification.


## A29 — original-D V2 creation failure: browser hydration boundary

Sufficient diagnosis, 2026-11-13; no source/check/VM/live action by architect.
Root's V2 tool59795 joined1; driver cleanup/SIGTERM followed the assertion
failure, not a proved cause of it. Original D CI and V2 creation acceptance remain
failed. Final084 green CI and managed eleven-case acceptance are separate proof.

**Exact evidence.** `/tmp/session-archival-d-creation-acceptance/v2-vm-run.log`
SHA256 `095cd65337ce030652486abd72466db0fa89d3047f7cc25e6cae83cfabd79943`
(276588 bytes), structured error at line1558; compact fields were read from the
matching captured `v2-acceptance-output/creation-evidence/creation-evidence/`
`browser-failure.json`, `nginx-timing.jsonl`, and `post-failure-passive.json`.
JUnit names three preceding passed subtests and the failing automatic-naming,
inherited-primary, sensitive-team, notifications-off case. Failure is before
maintenance: `creation_acceptance_browser.cjs:185` waiting30s for visible
`CREATION_REPLY_`. Creation receipt is ready, attempt1, exact root
`01a1d64c-1d8b-77a1-9e95-9fb44c5cb3d3`, slug
`2026-11-13-accepted-session`; browser has that identity and no pageerror.

| Captured UTC event | Meaning |
| --- | --- |
| 19:04:49.885 canonical document200 | Server-rendered identity arrived; not proof the browser controller mounted. |
| 19:04:53.924–19:05:15.618 conversation/nested imports and later reset/provider imports | Startup dependency loading consumed most of the locator's budget. Timing does not identify CPU/load/lock ownership. |
| 19:05:16.101 initial thread/page request | First hydration read began about22s into the30s transcript wait. |
| 19:05:23.781 events200;23.886 initial page aborted;23.921 replacement page started | Consistent with the shipped first-stream-open supersession path below. |
| 19:05:24.212 assertion failure | Snapshot had not been applied; UI CONNECTING/Loading conversation. |
| 19:05:24.291 and25.675 nginx thread/page200 | Both server responses completed after the assertion; first request6.305s, replacement1.384s. No browser-applied payload is established by these status codes. |
| 19:05:36.625 native read completed;37.019 public portal read completed | Same exact root idle, completed turn, one initial message and one expected reply. Portal200 took0.393s. This proves later availability, not the exact earlier completion time. |

All captured nginx500s are `/favicon.ico`; they do not explain transcript
hydration. Model capture contains eight primary requests with overload/retryAdvice
false, but the later exact native/public reads are the relevant reply proof.
Postfailure storage sample has about3.76GB available and4% inode use; no storage
exhaustion is demonstrated. Do not convert these facts into a claim of a healthy
browser or a diagnosed host-performance problem.

**Source correlation.** D `b8329e32` has the same browser helper, app.js and
codex-web pin as eabb and final084 for this path. Its
`test/creation_acceptance_browser.cjs:168–185` waits for canonical URL and a
server-rendered nonempty body threadId, then starts the reply locator wait.
`portal/internal/web/static/app.js:1523,1853,1869` awaits conversation and other
imports before controller initialization. Pinned codex-web `dd90fb4308ba`
`conversation/assets/sync.js:258–260` opens the event stream and schedules an
initial snapshot; `:152–161` deliberately cancels the active snapshot on stream
open and schedules another. `:89–139` prevents superseded results from applying;
`portal/internal/web/static/app.js:7093–7124` is the actual portal integration:
it reads the transcript page and calls its own `renderThread` only for the
current sync result. The generic `mountConversation` in codex-web is not the
portal mounting path. This predicts the observed cancellation/order,
but no captured JS callback trace uniquely identifies the cancellation event.
The artifacts prove an initial-browser-hydration deadline miss, not a missing
creation result, wrong identity, maintenance regression, or indefinitely stuck
controller. Attribution of the startup/request delays remains unknown.

**Smallest next proof, before retry/change.** Use the existing pinned
`test/sync_browser_contract_test.cjs` fixture (`Clock`, controlled promises and
`Source`, lines6–54) for a seconds-scale focused case: start a pending initial
read, emit first stream-open, require its signal aborted and exactly one fresh
same-identity read; fulfill the replacement with the expected reply, require one
current apply/connected result, then fulfill the old read and require no stale
apply. No real30s sleep, VM, model call or new harness/framework is needed. This
proves the concrete supersession behavior; it does not reproduce or excuse the
unattributed host delay. Existing tests cover stalled/read recovery, but do not
substitute for this exact pending-read/first-open ordering.

Root owns whether a narrow test-harness correction is appropriate after that
proof. Any correction must distinguish server-rendered body readiness from real
successful hydration, preserve exact identity, transcript and follow-up
assertions, and fail on actual unsuccessful hydration. An unmodified VM retry,
blind timeout increase, browser refresh, synthetic reply, or weakening of native/
maintenance assertions is not justified here. No production fix is established
by this evidence. Preserve D/V1/V2 artifacts and frozen source/pair identities;
a later successful targeted proof alone is not full packaged creation acceptance.


## A30 — exact-D acceptance through a reviewed hydration fixture correction

Sufficient bounded brief, subject to root release. C8's accepted pinned dd90
controlled-promise test proves first-open cancellation, one replacement/current
apply, no stale overwrite and no timers. It does not prove historical browser
hydration, HTTP identity or a host-load cause. No production defect is established.

**Decision.** The original driver's public test-input override can execute a
corrected helper against exact D without rebuilding D. However, an untracked
operational-only correction cannot bypass the existing final-review gate:
`mandatory-change-review/SKILL.md` Purpose and Main Agent steps1–3 explicitly
include substantive tests and require committed changes and quick checks before
final review/long integration. The smallest compliant route is one lasting
fixture-only correction, then copying those exact reviewed helper bytes into
the disposable D guest. This supersedes A30's initial provisional report that an
uncommitted operational variant alone would suffice. No browser/runtime/Codex
upgrade or performance project is needed.

Retain084 and its green CI/managed results as exact checkpoints. A new final
source head receives normal affected review/fresh-head CI and actual derivation/
input comparison before artifact reuse; a test-only diff does not establish
store-output equality. Root decides subsequent pins/build preparation. Original
D package, VM, configuration, native and maintenance targets stay frozen.

**Actual boundary and correction.** The portal uses
`portal/internal/web/static/app.js:7093–7124` (`createConversationSync`), not the
generic codex-web `mountConversation`. Its `renderThread:5427–5525` applies the
current snapshot; `appendMessage:5175` assigns `data-transcript-entry-key`, with
entries inserted at5238–5261/5265–5322. The template's body/threadId, Connecting
badge and Loading-conversation placeholder exist before hydration. The connection
notice is initially hidden and hidden during its warning grace, so its visibility
is not a readiness API.

In `test/creation_acceptance_browser.cjs`, keep ordinary ready polling, canonical
redirect and all identity assertions, but establish genuine hydration before the
existing reply wait:

- The ready creation/preparation receipt supplies the exact final slug, **not a
  threadId**. After ready, use one supported GET
  `/api/sessions/<exact-ready-slug>/details` within the same remaining180s budget.
  Its `currentTarget` must be nonnull with matching slug, location `work`,
  archived false and nonempty threadId; retain its targetId as well. This is the
  expected root for both body and browser-transcript checks. It is identity
  evidence only, never hydration evidence. Missing/changed/failed target refuses.
  Do not replace expected identity with whatever the document reports.
- Passively observe a completed successful browser GET for exact target
  `/api/sessions/<slug>/thread` or `/thread/page`, parse the response and require
  its threadId to equal the expected root and its entries to be an array.
  Arm observation before navigation/admission, retaining early completion until
  final receipt identity is known. Reuse the existing request observation
  boundary; the rolling80-entry diagnostic ring is not the readiness authority.
- Require actual visible entries under
  `#transcript-entries [data-transcript-entry-key]` on the exact canonical
  document, correlating an actual returned fixture entry/marker with the rendered
  row. Preserve new/fork/plan semantics. Body-only readiness, a parsed HTTP body
  without rendering, a different/source thread and synthetic DOM do not qualify.
- Share the existing180s creation-ready budget across ready polling and hydration
  as one absolute deadline started at `usable()` entry. Never renew it on retry,
  SSE open or navigation. Once hydrated, keep the existing30s reply assertion,
  follow-up exchange, initial-count/settings/notification/root/reload checks and
  original driver global3600s unchanged.

An aborted initial read is not success; await only its ordinary replacement
within that deadline. Matching HTTP errors, malformed/wrong-root payloads,
missing rendered hydration and expiry fail with compact phase evidence. Do not
force refresh, alter SSE behavior, inject replies, introduce an application
readiness API or increase the reply timeout. Stop/report if the existing passive
observer cannot faithfully bind the exact response and render.

C9 source clarification: `creation_store.go:81–95` and preparation status do
not publish a root. The existing details route at `server.go:2135–2137` returns
`currentTarget` at1531–1534. `lifecycle_target.go:74–91,134–140` freshly finds the
session and projects `summary.Codex.ThreadID`; that path is also present in D.
This works for new, fork and plan final slugs without a production/API change.
Keep the existing fork/plan root-different-from-source assertion. The additional
public identity read does not replace the passively observed browser hydration
read or add a new deadline; A30's earlier receipt-root attribution is corrected.

**Package/file ownership.** After root release, implementer2 owns only
`test/creation_acceptance_browser.cjs` and its narrow focused test under `test/`
(or the existing browser-contract test location), using the actual helper logic.
Root supplies the normal source/index/commit window; F8/J2 remain independent.
Root's C9 boundary clarification additionally assigns exactly one existing
checkPhase line in `nix/workspace-portal.nix`:
`node --test ../test/creation_acceptance_browser_test.cjs`. This wires the actual
helper regression into packaged fast checks from the existing portal module root;
verify its syntax/CWD without expanding the check batch. No other Nix change.
No production JS, codex-web, package contracts, Nix VM configuration or lifecycle
behavior changes. Preserve all existing assertions; sequence any shared file
with its assigned owner. Commit after quick proof and obtain the ordinary narrow
independent final review before the long D run.

**Seconds-scale gates.** Prove early response is retained, aborted-read then
valid replacement works, and body-only/wrong URL/wrong root/non200/malformed/no
render/expired shared deadline cannot pass. Require no timers/listeners after
success or failure. Test the actual helper boundary, not a copied algorithm;
reuse C8 only for its accepted sync scope. Run JS syntax and the existing pinned
Python parser/type/lint preparation against the actual driver interface, plus
full assertion and source/store-reference diffs. No VM retry is justified before
these pass and the correction is reviewed.

**Exact-D execution adapter.** Derive the operational helper from D's immutable
`/nix/store/047aiz4b5x6n2vri45lmk92hdzg51hmv-creation_acceptance_browser.cjs`
plus only the reviewed correction. Retain its original hash, corrected hash and
complete diff. The realized gxf driver's public
`machine.copy_from_host(source, target)` (`test_driver/machine/__init__.py:687–715`)
can copy it after guest startup and before the first browser invocation to an
ordinary dedicated guest `/tmp/` path; require readable permissions and matching
digest. In the derived V1 script change only `browser()`'s Node script argument
to that helper path, preserving original Node/Playwright/Chromium/user/environment.
Explicitly record this one additional harness-file substitution; do not claim
all executed test files are original. Preserve V1's accepted C7 changes, all
production/store/maintenance/native references and every scenario/assertion.

Use A27's same qxz public `--config COPY -o OUTPUT --junit-xml junit.xml` command;
only config.test_script changes. No alternate launcher, immutable store edit,
wrapper/VM/package build or retained VM state. Root releases one full fresh run
under existing ownership and3600s budget, stopping on failure/uncertainty without
automatic retry. Only a full pass establishes separate exact-D packaged
acceptance with the named reviewed harness. Original D CI, V2 and original test
derivation stay failed historical results. No action is executed by this brief.


## A31 — scope-freeze triage and the inferred old-D creation gate

Bounded assessment only; no new package, source/fixture change, check, probe,
retry, VM, CI query or live action. Exact current session/environment matched.
Root retains acceptance and execution authority.

**Retained failure cause.** Root's D VM invocation9163 joined1. Absolute
`/tmp/session-archival-c9-adapter/vm.log` is270181 bytes, SHA256
`f5404e00169c6751a2a7b1adac420c95c59d875659029dd7f21a344becf0423e`.
The first three named scenarios passed, including C9's explicit-session helper.
Automatic naming failed before hydration/maintenance: request
`b9d6af7e-3671-4f4d-ab3d-c03f84a11459` started20:14:18.000799Z and was failed/
stopped by18.058691Z; the browser observed that failure at20:14:26.263Z.
Captured `namingResponses` is empty.

The same restarted portal PID4907 logged `session naming provider configuration
unavailable` at20:13:07 (log1476/1628), then naming `utility_error category=server`
in11ms at20:14:18 (1541/1635). D `naming_runtime.go:85–88` returns from the
naming-owner goroutine on that provider-argument error, before launching its
private app-server at90–96. The goroutine removes its private directory on exit.
`namingProviderArguments:106–124` runs the existing `workspace-host provider
native-args fixture` with a5s bound, discards stderr and folds execution/nonzero/
overflow and JSON-shape failures into that log. Later `session_name.go:108–110,
139–140` maps the ephemeral server error to the recorded category. This is a
proved startup failure boundary consistent with the later missing naming server;
the exact subprocess cause is not retained. No evidence selects timeout, lock
contention, bad configuration, CPU load or provider outage. Do not introduce a
new diagnostic patch or retry to discover it during the freeze.

**Mandatory rule versus our plan.** No inspected applicable instruction names a
full old-D creation-VM pass as a prerequisite for this diagnostic-only policy1
selection. A24's `ordinary exact-D package/required CI` and the A25–A30 full-run
acceptance requirement were our verification-plan choice. They may be narrowed
by root's explicit applicability decision; failed results must remain failed.
This does not claim complete D packaged-suite acceptance.

The actual workspace verification rule is: “Keep the selected package unchanged
until the candidate passes review and applicable checks.” It separately requires
postdeployment portal health, naming and conversation continuity before calling
the runtime usable. Runtime AGENTS documents the full-suite command and focused
checks; it does not state that every historical CI job must be green before every
compatible diagnostic selection. Installed `docs/workspace-portal.md:1046–1076`
supports active-thread policy1 switching only with matching native executable,
launch policy/arguments/capacity, complete validated invocations and ordinary
lifecycle/creation/authority/transition fences. Its portal/router restart and
immutable native-marker behavior remain mandatory. `docs/workspace-updates.md:
193–195` requires actual Ruby worker/systemd/profile verification for the
native-changing maintenance operations described there; a nonmaintenance live
selection does not invoke that worker.

On root's accepted exact-D package checkPhase, native-monitor/LiveSwitchReconnect
79.358s, actual Ruby policy1 transition111 assertions, fast/archive CI, affected
review and G/J2 composition/host compatibility evidence, there is a supported
basis to **attempt the ordinary compatible D selection**, without another old-D
creation run. No result is reused as a different head/derivation, and the failed
full suite is explicitly retained. Root must record that narrower applicability
disposition; this assessment itself executes or approves nothing.

**Real residual risk and stopping boundary.** The live path restarts the portal,
so the unexplained naming-provider-argument startup failure could recur. Native/
argv/marker guards cannot establish naming usability. Retain ordinary selected
D/unchanged native-marker/socket/registration, portal/router, own conversation
and naming-health verification before calling the runtime usable. Unexpected
native restart, admission refusal or uncertain effects stops for the existing
source-owned recovery, with machine retention intact. Old5d13 has no accepted
journal/recovery authority. Final DA64 CI and final delivery acceptance remain
separate root-owned obligations. Do not expand into naming, browser performance,
Codex changes or fresh default classification; scope freeze remains active.

## A32 — necessity audit of DA64 (assessment only; delivery frozen)

**Subsequent acceptance/release.** Lead reports the user's explicit “proceed”
direction and accepts this assessment as the sufficient S1 brief for exactly two
cuts: remove redundant legacy attestation and remove threadless Begin/Complete
authority handling while preserving strict ownership/refusal checks. Implementer1
owns the complete primary-source reduction, index/amend, focused checks and
affected docs. Preserve consumed D and the DA64 checkpoint. Policy2 and the MCP
transport remain; no CLI-only redesign or creation-harness revert is released.
The assessment below is retained as historical rationale. Root owns acceptance
and subsequent delivery; architect0 remains available for exact clarification,
with no further audit or operational work assigned.

**Conclusion: the complete 6,053-line addition is not necessary for the requested
archive behavior.** A17 established an existing recovery that makes the new
legacy attestation API redundant. Threadless archive callers also acquired an
unnecessary mutation/authority round trip. Remove those two branches if the user
chooses reduction; retain the local observer safety mechanism. This is a cut
assessment, not authorization or an implementation release.

Exact inspected range: `eabb56a278bd8eb1759041467eaebfa6392ddcb2` →
`da64cf0999bd876836658c9f14b11f9f4b1ff60e`. The consumed diagnostic parent
`b8329e32f1132fd947f4a9c803bf44e3ed9ce481` is retained unchanged. Counts below
are added lines, including comments/blanks, not net savings or a claim that tests
do not matter. These disjoint file groups reconcile the supplied totals:

| Current area | Implementation + | Tests + | Disposition |
| --- | ---: | ---: | --- |
| Observer types/store/service/validation/lifecycle/delivery | 1,474 | 802 | Required direct-observer core; remove legacy branch below |
| Existing worker, bounded GH adapter, owned process-group result | 486 | 451 | Required local command ownership/join proof |
| CLI/browser archive admission and readiness, archive VM coverage | 741 | 843 | Required rooted path; remove threadless mutation branch |
| MCP adapter/ACK | 27 | 71 | Required for the selected MCP interface; attestation fields removable |
| Maintenance observer inventory | 14 | 0 | Required to avoid ignoring new local effects |
| Capability/rollback/contract and switch coverage | 47 | 186 | Observer capability required; helper cutover conditional below |
| Already consumed D diagnostic | 51 | 336 | Preserve exact history and behavior |
| General creation harness and checkPhase wiring | 1 | 248 | Separate scope choice; not the archive mechanism |

The other 275 additions are docs/skill text (15 belong to D). Totals are
2,841 implementation + 2,937 tests + 275 docs = 6,053 additions, 187 deletions.

**Concrete cuts, without a replacement framework:**

- **Remove `attest-local`, `legacy-native` auxiliary records and their native
  binding API.** At DA64, `observer_service.go:184–239`,
  `observer_types.go:75–84,94–111`, `observer_lifecycle.go:19–40` and
  `observer_validation.go:187–191` alone contain **111** added lines. Removing
  their CLI/MCP/status/validation/store branches and fields is approximately
  **200–260 implementation lines**, plus the exact **62-line** legacy-attestation
  test (`observer_test.go:115–176`) and related docs/assertions. No necessary
  supported consumer was found. Eabb `service.go:266–325` already authenticates
  the exact lead/incarnation, invokes `CheckResolution`/native quiescence, retains
  uncertain delivery, and records an immutable resolution without changing the
  original report. A17 proves that truthful observation-only local completion
  does not assert remote CI completion. Keep that supported recovery for 63/8
  and other old native records; no blanket CI exemption. Remove exported
  `NativeBindingDigest` and legacy status digest fields; **keep direct poll/source
  binding** (`SourceDigest` currently also binds actual GH responses), same-ID
  native replay and strict cross-format collision refusal.
- **Remove threadless Begin/Complete, not rooted archive authority.** The new
  Ruby caller currently enters it merely because the workspace-wide monitor
  directory exists (`libexec/dev-session:1918–1992`). For an empty retained root,
  use the ordinary strict `require-idle` reader, checking **both** native and
  observer stores, then continue the original archive checks. Do this under the
  already admitted EX slug lock/current generation; a missing root with owned
  records or unreadable state still refuses. Registration requires a real root
  and the same session lock, so it cannot race this admitted empty-root path.
  Remove approximately **30 implementation lines** of special routing/DTO
  handling and the **292-line** threadless-only test/helper block
  `monitor_archive_test.go:228–519`, replacing it with small caller/no-owned and
  contradictory-owned refusal coverage. Keep typed read-only readiness, rooted
  parent-FD/browser-receipt validation, retry binding, readiness before removal,
  and delete/revoke protections. Do not generalize this into skipping checks for
  rooted records or trusting mere directory absence as ownership proof.

Those cuts identify roughly **230–290 implementation + 354 test additions**
before smaller replacement coverage and documentation cleanup. They do not
justify promising a tiny patch or removing the whole 278-line authority adapter.

**Helper restart is not an automatic third cut.** Removing attestation restores
the old MCP *input* action/property surface; `executionOwner` is output, not an
input addition. However eabb `team_mcp.go:192–204` uses
`DisallowUnknownFields`, and `monitor_mcp.go:75–86` accepts only `Operation` ACKs.
DA64 adds native ACK fields and returns `ObserverRecord` for direct CI. The stable
profile dispatch (`team_mcp.go:117–121`) reaches the new CLI but leaves that old
decoder running. Old archived-owner status fallback also reads only the native
store (`monitor.go`, `monitorCaller`). Thus deleting only the policy2 marker would
break actual start/status/recovery consumers. Keeping MCP-managed direct CI
requires the corrected helper and ordinary cutover even after attestation removal.
Do not manufacture a native launch or repurpose schema1 fields to fake compatibility.

A **CLI-only new direct-observer interface**, with old MCP/native actions and ACKs
unchanged, could instead be a smaller product boundary, but it changes the approved
caller/skill/recovery interface and requires actual compatibility proof. It is a
lead/user scope choice, not an established safe deletion. Policy2-only test
anchors currently include the 70-line switch case, 41 added native-integration
lines and 17-line contract case; some assertions need replacement if the MCP
interface stays. The 26-line policy1 fixture is also used by consumed D coverage:
do not delete it blindly. Observer-state rollback capability remains necessary
with either public transport.

The general creation harness fixes (248 test additions plus one checkPhase line)
are likewise independently useful, not necessary archive product behavior. They
may be separated if scope is narrowed, but reverting them restores known harness
failures; neither final-head acceptance nor failed D results can be waived or
relabeled. No new run or harness workaround is proposed here.

**Smallest retained functional shape:** one existing-worker bounded read-only CI
poller; durable exact source/request/owner and poll intent; actual start/wait/pipe
join evidence; persistent accepted-archive fence; ordinary CLI/browser admission
and idempotent join/detach; immutable result/uncertain-delivery handling; no wakes
after detach; strict legacy native recovery through existing `resolve`; capability
checks before new state and against rollback. Remote queued CI does not block an
otherwise proven local join. Unknown local handles, native submissions and real
resource/mutation ownership still block. These are actual current consumers, not
extra assurance to justify every line of their present implementation.

Root reports D selected with original native/marker retained and portal/naming
healthy; DA64 observer/attestation state has **never** been written live. Therefore
dropping the unreleased legacy auxiliary branch needs no live migration on this
rollout; retain old schema1 readers and exact D lineage. Current DA64 checks remain
evidence for DA64 only. Any later reduction needs its own affected review/checks
and exact final artifacts, after explicit direction. No source, test, ref, pin,
CI, native or lifecycle action was performed for this audit. Capacity available.

## A33 — settled final configuration base for reduced runtime734

**Sufficient owner0 pin brief; root releases execution.** One canonical SSH fetch
observed configuration master `08d68a85f24a95b70b2d806f995f04b236e4d89a`.
Use that exact observed base for this preparation, not parked `d067` or another
refetch loop. Accepted `7d9807e021e6106d628c021da45f5f55077b2e9c` is its ancestor.
The five integrated commits are `e71d14d0` (vpsadminStaging), `d0674cc6`
(vpsadminServices), `1e0ecca5` (vpsadminosProduction), `1a948a87`
(vpsadminProduction), and `08d68a85` (node25.prg OOM thresholds). Only
`flake.lock` and `cluster/cz.vpsfree/nodes/prg/node25/config.nix` change.

All 64 lock nodes remain present. The changed nodes are vpsadminStaging,
vpsadminServices and vpsadminProduction → `2d0946c4e699aa61092228d8a7cb275477ee46d0`;
vpsadminosProduction → `c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`; and its
exclusive `impermanence_3` child → `fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2`.
Root input edges/follows are unchanged. Node25 alone adds `restart_hits=4` and
`load_multiplier=1.5`. Preserve all these already integrated changes.

**Affected-host boundary.** Aitherdev selects only nixos-stable, home-manager,
llm-agents and dev-workspace (`aitherdev/module.nix:7–12`); none of their selected
nodes changes. Its tree remains `0a8a09cec1e27be4182ed1fc3f2ed0eebbd19710`, modules
tree `c4b0e7043abd9c63c343da0729f967205a8a79c7`. AGENTS, flake.nix, Gemfile.lock,
confctl and its evaluator/development-shell inputs are identical to7d. Unlike
A28, this advancement introduces no demonstrated aitherdev/tool interface or
native selection change. It does not authorize deploying other hosts. Source
equality is not proof of final system-output equality: configuration revision
and complete input provenance still change. No live metadata was queried.

The existing configuration runtime closure (eabb plus eight dependencies) is
identical across7d→08d. Its resolved eight dependencies equal workspace
`327d044377126b7e8eb962344a339c6993e2f631`'s runtime dependencies; graph-local node
names were resolved before comparison. Published/reviewed reduced runtime
`734a85fea42c8f8276e6b037196c24cf8903cd12` has byte-identical flake.nix/flake.lock
toDA64. Keep that exact runtime, its dependencies and consumed D ancestry;
configuration movement requires no runtime rebase, feature change or additional
runtime CI. The08d lock SHA256 is
`d6a45cb62482eb2f321d551595325da1b44b1095284abe2acf6f4af57f487877`.

**Smallest final source/check boundary.** Owner0 uses the unchanged normal
`confctl inputs channel set --commit dev-workspace devWorkspace 734a85fea42c8f8276e6b037196c24cf8903cd12`
in the declared Nix environment, retaining one final runtime-pin commit above08d.
Preserve all other63 configuration nodes, host edits and follows. Independently
update the workspace's existing direct nested runtime to the same734; preserve
workspace327's caller policy9be, extension0c and all34 sibling nodes/follows.
Retain earlier final/D checkpoint refs and receipts; do not rewrite consumed D.

Required quick evidence is normal generator/hooks, full semantic graph/pin
comparison, paired deployment checker, and the existing F8 single-aitherdev
evaluation with IFD disabled: assert NixOS, target172.16.106.40, four channels,
exact runtime734, then force the selected `toplevel.drvPath`. Reuse its established
expression with only the expected revision changed; no new matrix or other-host
evaluation. Final config/profile evidence must bind exact head/clean status,
generation, complete input graph, actual derivation/output and successful
build/copy, followed by the existing deployment/health/recovery gates.

For source-review reuse, the existing certified-equivalence path is appropriate
only once its independent certificate binds old/new exact ranges, reconstruction
or installed pin proof, reviewed734, preserved siblings and no-migration/history
conclusion. This classification is not that certificate and grants no artifact
equivalence. Functional/conflicting pin changes require affected review; no broad
re-review of unrelated integrated node25/vpsAdmin work follows. Later default
movement belongs to the final integration freshness/lineage check, not serial
intermediate repins/builds. This brief changes no feature/ref/worktree, runs no
evaluation/test/build, and supplies no activation or integration action.

## A34 — D prepare refusal: exact predicate and own-session diagnostic route

**Source-only result, sufficient for E1.** Selected source is consumed
`b8329e32f1132fd947f4a9c803bf44e3ed9ce481` (D22x). Root's switch42666 returned
`prepare-inventory-blocked:monitor-operation-unresolved`; proposed operation
`a1adc0d3-4914-44fa-b9a7-219d9df70021/operation.json` is absent. This is a
pre-acceptance inventory refusal, not an accepted operation to recover.

At D `maintenance_control.go:722–765`, inventory visits **every** nonarchived,
rooted session whose socket matches each registered service. Any error from
`maintenanceMonitorInventory` becomes this category; the allowlisted classifier
at`:257–267` deliberately discards IDs/raw causes. Therefore the category does
not prove which session/monitor blocked or that a remote CI result is missing.
The exact helper (`maintenance_monitor.go:18–50`) can refuse for:

- store/inventory/identity read failure or an ambiguous/different retained owner;
- archiving, uncertain thread creation/bootstrap, or a submitting delivery
  (`service.go:514–551`, `Inventory.Unresolved`);
- `RequireIdle(...,false)` external effects, uncertain receipt, or failed actual
  native identity/quiescence proof (`lifecycle.go:130–180`).

`HasUnresolvedEffects` (`service.go:248–263`) clears with an existing resolution;
otherwise a terminal report blocks only for `incomplete` or nonempty
`stillRunning`. A completed terminal report supersedes earlier escalation.
“Passed”, “failed”, a cached termination time or an idle parent alone is not the
whole predicate. No supplied operation is newly classified by this source read.

**Smallest ordinary E1 read:** from the verified bound session and selected D,
run `dev-session archive-check 2026-11-11-session-archival-failures --as-is --json`.
Retain its own receipt and return only relevant `conversation` blocker ID/reason.
The public read-only readiness path's conversation stage calls
`ensure_archive_conversations_ready!` → `sync_monitor_lifecycle!('require-idle')`
(`libexec/workspace-archive-check.rb:53–68`, `libexec/dev-session:1907–1919,9401–9409`).
Root/state/socket are derived by the normal owner, not supplied as invented lead
authority. It can return `monitor ID retains external work` or
`monitor ID is not quiescent: REASON`. This is not an archive request.

The underlying `workspace-portal monitor-lifecycle require-idle` accepts
`--workspace`, `--user-state-root`, `--session-slug`, `--root-thread-id`, `--socket`
and has a30s bound, but is explicitly an internal Ruby-owner subcommand with
syntactic flags rather than independent session admission (`monitor.go:181–240`).
Do not bypass its public caller for this diagnosis. `require-execution-idle`
is a different predicate and is not a replacement for maintenance's full proof.

The proof issues no native resume/load/send/cancel/archive: it reads retained
identity and turns, requests/queue and submission evidence. Pinned codex-web
`dd90fb43:codex/client.go:4411–4448,4451–4479,4778…` supplies the read calls;
workspace `archive_proof.go:217–252` supplies archived/active branching.
Ordinary ledger/transport bookkeeping is not evidence of a new native action.

**Limits and stop:** owner/receipt/read errors may lack an ID; own admission can
fail earlier, and readiness output has a128-blocker cap. Store.List validates
workspace entries before filtering the requested slug (`store.go:261–295`), so
a generic store error is not attributable to this session. Do not manually read
all JSON files to find another owner. An own pass also cannot exclude the
maintenance helper's additional identity/inventory checks or another session's
blocker. Return that precise gap to root, without a peer census. Root owns any
exact-lead status/resolution and the evidence decision under existing A17;
unknown effects stay fenced and no new attestation API is proposed. Source/head/
pin/artifacts remain frozen. Architect ran no diagnostic/native/live operation;
routine route message sent to E1, then investigation stopped.

## A35 — maintenance-only gates after E1's own conversation pass

**Sufficient source-only determination; no new operation released.** E1's
single public archive-check passed conversation (5/6, sole coordination blocker).
D `maintenance_monitor.go` adds the following before the same full idle proof:

| Extra gate | Evidence needed from existing own metadata |
| --- | --- |
| `IdentityFor` (`authority.go:25–44`) | Session nonarchived/nonterminal, nonempty root, creation state not `creating`, no pending lifecycle, valid tracking-directory observation identity |
| `SameOwner` (`service.go:38–40`) | Exact `owner.slug`, `owner.rootThreadId`, `owner.incarnation`, `owner.socket` against that identity/service socket; origin turn, socket epoch, provider and runtime schema are **not** compared |
| `Store.Inventory` (`service.go:514–551`) | Across nonarchived own records, unique nonempty native `launch.threadId`/`projectId`; no disposition `archiving`; no `createAttempted` without thread; no `bootstrapAttempted` without receipt except `canceled-unsent`/`unsubmitted`; no event delivery status `submitting` |
| Five-second helper bound | Not established by saved status or E1's separate30s proof; the original error/timing would be needed to attribute expiration |

Existing saved6d/63/etc status DTOs contain the owner/launch/disposition/event
fields above. Existing own public details provides `observationIdentity`,
`currentTarget` and `pendingLifecycle`. Its observationIdentity is exactly the
incarnation digest used by IdentityFor (`session/observation.go:24–45`), distinct
from lifecycle targetId. The known root/socket and own active tracking/creation
metadata complete that comparison. These receipts prove only their named IDs
at their observation time, not absence of other own operations.

Successful exact-lead **recovery status is not sufficient IdentityFor proof**:
`monitor.go:132–155,375…` replaces callbacks with `monitorRecoveryOwner`, which
deliberately permits matching pending archive/delete work. It still checks exact
root/socket/incarnation. Status may reconcile existing metadata/receipts; do not
make fresh calls as a substitute for comparing the already saved DTOs.

After `Inventory` and `List` succeed, zero own operations **or all own operations
already disposition=archived** returns before IdentityFor and full idle proof
(`maintenance_monitor.go:18–33`). Store.List validates workspace records before
slug filtering, so a malformed shared entry can refuse even this short circuit.
E1's pass gives useful later read evidence, not a reconstruction of the earlier
failed snapshot or its timing.

**Existing route limit.** D exposes exact-ID monitor `status`, not a lead monitor
listing; empty-ID status resolves a registered utility. `dev-session list` lists
session/worktree/tmux rows, not monitor admissions. `/api/index-status` exposes
session observationIdentity/archived/pendingLifecycle metadata, not monitor
Inventory reasons. No inspected public own-scoped endpoint returns the missing
maintenance helper result. Do not fabricate maintenance-control requests or
call private lifecycle flags to obtain it.

**Minimum additional administrative scope, if root chooses to obtain authority:**
one bounded metadata projection of D's central workspace monitor store:

`/home/aither/.local/state/dev-workspaces/monitor-operations/8a2a555cb2f65b336ae8727305f7aaaac277dbdf66f266adde8c8af18bf12836/<ID>.json`

Read only regular bounded records and retain/output this allowlist: file ID/read
validity; schema/workspace; owner slug/rootThreadId/incarnation/socket;
disposition; launch state/projectId/threadId/createAttempted/bootstrapAttempted,
receipt-present/turnId/queuedSubmissionId; event ID and delivery status/receipt
turnId; resolution-present and terminal outcome/stillRunning-present boolean.
No source argv, brief, envelope, report/evidence text, tool output, credentials,
roster or conversation contents. Group the returned administrative fields by
owner to expose uncertain identities/receipts and retained-record counts.

If comparison needs current session identity, the existing `/api/index-status`
projection of only slug/observationIdentity/archived/pendingLifecycle is the
corresponding public administrative surface, with its freshness/error flags.
It is not a substitute for terminal/creation checks or native quiescence. Do not
fetch peer details (which also render roster/repository sections), tracking
content or native threads under this limited proposal. Stop on the first exact
static owner/ID/reason; any additional owner-specific proof needs separately
bounded authority. This is a concrete permission scope for root to assess, not
permission inferred from deployment approval and not a newly implemented tool.

Even a clean complete projection cannot localize a transient five-second/native
proof failure. The refused operation was never saved, and D maps the original
helper error to the category without retaining its ID/reason. That is the precise
remaining evidence gap if static metadata gives no blocker; no timeout/load or
foreign-owner cause follows. Root owns scope and any supported A17 resolution.
Architect read source only, changed this note only, and stopped; no live/native/
peer reads, retries, mutations or new diagnostic subsystem.

## A36 — existing owner-side exact-turn history and executor-proof limits

**Access correction after peer interface evidence:** the RPC schema facts below
do **not** establish an executable installed reader for a monitor utility.
One bounded source pass confirms **no supported exposed utility-history route
established** in D22x/b832 or reviewed734. D's `main.go:833–918` thread command
has observe/activity metadata readers, no history/items action. Its monitor MCP
has only start/report/status/cancel/resolve (`monitor_mcp.go:14–37`);734 adds no
history action. Authenticated HTTP uses the conversation resolver
(`server.go:529–534,3877…`): the no-address target is the retained lead; an
address must resolve through `readyConversationMember` to a ready roster member.
It has no monitor-utility ownership branch or arbitrary utility-thread override.
734 leaves that resolver unchanged. Therefore the earlier “owning lead may use
its existing passive App Server connection” wording is schema-level guidance,
**not a confirmed CLI/MCP/HTTP invocation**. Peer messages
`0de9fd24-4fca-42c8-b15a-35232a8d5c33` and
`986635ba-80b9-46d2-8e91-771caa703990` supplied this access gap.
No raw-socket/new-client/private-file fallback, proxy retry or new implementation
is proposed. Missing producer evidence remains fenced. Root owns the next
decision; this clarification inspected source only and stops here.

**Confirmed RPC schema; not an exposed invocation or complete executor ledger.** Runtime734
retains pinned codex-web `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`/Codex0.165.
It adds no per-tool inventory API. These existing wire shapes bind the original
operation's `launch.threadId` and `launch.receipt.turnId` (not monitor ID/root ID);
the access correction above limits their operational applicability:

```json
{"method":"thread/read","params":{"threadId":"UTILITY_THREAD_ID","includeTurns":false}}
{"method":"thread/items/list","params":{"threadId":"UTILITY_THREAD_ID","turnId":"ORIGINAL_TURN_ID","limit":32,"sortDirection":"asc"}}
```

`includeTurns:false` is confirmed by `codex/thread_page.go:249`, not an inferred
flag. If original-turn metadata must be located/checked, the existing request is
`thread/turns/list` with `{threadId,limit:20,sortDirection:"desc",itemsView:"notLoaded"}`.
Use each response's exact `nextCursor` on the same method/identity until absent
or null. Items response `data` entries are `{turnId,item}`. Require the expected
thread/cwd/project binding, exact turn ID, nonempty item IDs, no repeated
IDs/cursors and complete pages. A truncated/error page is a gap, not zero tools.
Pinned `test/codex_protocol_contract.py:235–240,336–338,750–775` binds these shapes;
`thread_page.go:381–415` validates pagination, and `history_reader.go:25–41`
confines passive history to these read methods. No resume/load/prompt/new server
is required or authorized here.

Raw items can expose retained `commandExecution` status/exitCode/aggregatedOutput
and other represented tool-call results. Preserve original IDs and any returned
executor handles; don't infer omitted handles or replace source statuses with
turn status. The command item contract is exercised at protocol-test`:628–636`;
the client renders command/tool output at `client.go:4514–4543`. Neither the
rendered transcript nor full pagination promises every raw outer
`functions.exec` call/output or nested executor session. Outer completion can
leave a yielded nested command running; a wait/poll result containing a handle
is not its join receipt. Background effects require their actual owned producer
evidence as well.

**What Q actually proved:** our `verification.md:306–341` matched47 raw outer
call/output pairs (no yielded outer cell left) and26 explicit native command
terminal receipts. Poller33520 had22 `write_stdin` observation returns, followed
only later by exact original `CommandExecution` terminal evidence at21:03:56.170Z,
exit-1, after the utility turn had ended. Q read the owner's exact local rollout;
it did not obtain completeness from a monitor-status DTO or remote CI success.

The public `Thread.path` property is intentionally nullable; the pinned client
uses a validated nonnull local path for its own persistent history metadata
(`protocol-contract.py:899…`, `client.go:4360…`, `thread_page.go:256–265`). It is
an owner-local source pointer, **not** cross-session file authority or a new raw
executor API. If public items omit required responses, only the peer owner under
its own existing scope can correlate its exact original rollout/call IDs/late
producer receipts as Q did. We do not read that file. Null/missing history or
missing producer responses remains an explicit evidence gap.

An original still-owned tool context may use its ordinary nonterminating
`functions.wait` on a returned running cell ID, or empty-input `write_stdin` on
its original exec session, to obtain the original result. Those are executor
tool calls, not passive history reads; they are not part of this source-only
assessment. A recorded numeric handle is not portable authority, and a lost or
closed handle must not be recreated or polled from an invented caller context.
No supported App Server reattachment/receipt-lookup RPC for those lost tool
handles was established in the inspected pinned adapters/contracts.

Stop at the first missing known call/result/producer join. Keep the incomplete
report immutable and the local-effects fence until the exact lead has all known
local/native proof for existing A17 ResolveEffects. CI success, synthetic empty
stillRunning and native turn completion do not supply it. No peer data, native
API/tool, CI, test, source or lifecycle action was accessed/executed by architect.

## A37 — owner-local producer evidence before existing resolution

**Sufficient next action; no implementation proposed.** Peer message
`5b38c3df` corrects the evidence state: its native rollout is **uninspected**,
not proved missing. The owner can locate and read that exact utility's retained
rollout under its own authority, as Q did. A36's absence of an exposed
CLI/MCP/HTTP utility-history reader remains true; it does not establish absence
of this owner-local evidence. We do not read or search the peer's native store.
Frozen734, consumed D/b832, pins, deployment and original reports remain intact.

**Controlling contract.** D `skills/dev-session-monitor/SKILL.md:64–84` says:
“Resolution evidence must account for the source command and every known
operation-owned code cell or tool session.” It also says: “Keep known uncertainty
fenced; an idle turn or the source command's exit does not settle those effects.”
`docs/dev-sessions.md:264–282` separates this evidence from the automated native
thread/turn, prompt, queue and submission proof. Thus current quiescence cannot
substitute for unaccounted known handles; an unrelated-history audit or remote CI
completion is not an additional resolution predicate. No narrower interpretation
licenses ignoring the uninspected original utility evidence.

**Exact owner-only lookup.** D `libexec/workspace-host:3765–3779` derives native
`CODEX_HOME` from the registered workspace, not the caller's ambient home:
`<workspace-host state>/codex-homes/<registry name>`. Q established this service's
root as `/home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz`.
Pinned codex-web dd90 `codex/activity_lineage.go:181–223` searches only its
`sessions` and `archived_sessions` directories for exact UUID suffix, skips
symlinks, bounds discovery and rejects duplicate matches. The owner can use this
filename-only command after confirming that same registered native home; it
opens no other rollout contents and must not be run here against peer history:

```sh
find -P /home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/sessions \
  /home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/archived_sessions \
  -type f -name '*-01a1d81c-1350-78a0-b6b8-ab8e63bd3dfd.jsonl' -print
```

An absent search directory is an explicit inventory fact, not an empty-history
proof. Require one unambiguous match, a regular no-follow file and first-line
`type=session_meta`, `payload.id=01a1d81c-1350-78a0-b6b8-ab8e63bd3dfd` and
`payload.cwd` matching the owner's retained utility launch. Require exact
`turn_context.payload.turn_id=01a1d81c-1ce3-74b0-b103-d723ff449e18` (and matching
task-start identity where retained). These are pinned reader checks, not guessed
filename authority: `activity_lineage.go:80–115`, `turn_context.go:37–110`.
Do not follow unexpected fork/history-base references into other identities.
Snapshot size/file identity and retain parse/truncation/change errors; incomplete
or changing evidence cannot prove an empty tool inventory. D's ordinary
`thread observe` does not expose `Thread.path` (`observation.go:33–45`), so it is
not a substitute path-discovery command.

**Bound the read and correlate effects.** The owner reads only that original
turn's calls/results and later records linked to its exact known call, command,
cell or session identities. Pair outer calls with outputs; preserve every
returned yielded-cell/nested executor handle. A poll returning the same handle
is not a completion receipt. Correlate terminal producer records to original
invocation identity/argv/cwd; account separately for any explicitly launched
background effects. Do not stop at `task_complete`: Q's33520 producer terminal
record arrived later, with exact command ID, process ID, times and exit status
(`verification.md:306–341`). Preserve failure/-1/unknown cause as recorded; PID
absence, turn termination and remote CI success do not replace these receipts.
Return a compact evidence inventory/gap list to the owning lead, not raw prompts,
credentials or unrelated transcript. No universal guarantee that every executor
receipt was persisted follows from this lookup.

**Resolution and stopping condition.** If the owner accounts for the original
observation command and all known cells/sessions/background effects, its exact
lead can submit the existing stable-ID `resolve` with truthful bounded evidence
and detail. D `monitoroperation/service.go:266–325` rechecks current owner under
the session lock, exact operation/root ownership, launch reconciliation and
native quiescence/receipt proof. It records an immutable resolution, cancels only
unsent delivery and preserves source, reports and accepted/submitting receipts;
identical replay succeeds and conflicting evidence refuses. This does not claim
the synthetic incomplete outcome succeeded or that remote CI ended because a
local observer ended. The existing original executor context, if still owned
and available, may obtain a missing original result through its ordinary wait;
a handle is not transferable authority for another thread. Missing or ambiguous
known completion remains a precise blocker. A new thin history client would
only expose retained public items and cannot reconstruct omitted producer
receipts or prove lost executor completion; it is not needed before this owner
lookup and is not released by A37.

Acceptance is the owner's exact identity/header/turn proof, complete bounded
known-effects inventory and the existing resolver's native guards, preserving
all old evidence. No code, schema, migration, package switch, check or new API is
needed for this next step. Architect performed canonical source/own-record reads
and this documentation only; root owns communication and any operational action.

## A38 — one owner-side empty-input read of original executor handle

**Sufficient action; correction to A36/A37 access inference.** The declared
`write_stdin` interface accepts an “existing unified exec session” by `session_id`;
empty `chars` “polls without writing.” Its arguments are session ID, characters,
wait duration and output bound. It has no caller/thread argument or stated
same-originating-thread-only restriction. The earlier original-context wording
must not be treated as a demonstrated API prohibition. Neither the definition
nor Q proves that handles are globally portable or survive executor loss. The
supported next step is one normal owner-authorized read, allowing the executor
to enforce its actual scope; no utility activation/reattachment is established
as a prerequisite.

Lead-supplied evidence binds operation `a8c49117-6d98-4afd-9b5d-15afe4132919`,
utility `01a1d74b-2c77-79a1-984f-0c5f7ada0667`, original turn
`01a1d74b-3675-76e0-b039-354de57a1c2e`: stable1078-line owner rollout,
211 paired outer calls,32 launches/31 terminal receipts. Only session99295 is
unresolved. Its last call `call_956cec0a3fbe4a5686409edf113991bd` at line1042 and
result1044 still return99295, with no later receipt through EOF1078. These are
owner findings supplied by the lead, not independently read peer evidence.

The exact owning lead, under the existing task authority and retained original
command/session provenance, may invoke its normal available tool once:

```json
{"session_id":99295,"chars":"","yield_time_ms":5000,"max_output_tokens":2000}
```

Await the call and retain the structured result, not just printed output. This
does not send input, signal, create a command, reopen a thread or change a native
turn. It may consume buffered output, so keep that receipt. Do not impersonate
the utility, supply an invented caller, guess another handle, or poll this peer
handle from our session. The known ID and owner authority justify the attempt;
they do not guarantee that this executor context still retains the session.

If it returns terminal `exit_code`, correlate the result with the retained exact
invocation and reject conflicting identity/output. A matched terminal result can
close99295's command gap; any separately known background effect still needs its
own proof. Preserve actual failure/exit status and the original incomplete
monitor outcome. If it returns `session_id`/running, no terminal status, unknown
session/context refusal, or conflicting evidence, stop and retain that precise
gap. A lookup refusal or empty output is not completion. No repeated poll,
replacement execution, utility resume or new client is authorized by this brief.
Existing exact-lead ResolveEffects remains conditional on complete known-effects
evidence and its unchanged native/identity/receipt guards.

This is a declared-tool-contract assessment, not an assertion about uninspected
executor internals. No supported utility resume/join mechanism or product change
is needed before trying this ordinary read. Architect did not call99295 or read
peer files/native/process state; source734/D, deployment and all receipts remain
unchanged. Root owns communication and the operational decision.

## A39 — actual executor scope and remaining recovery boundary

**A38 outcome and correction.** Owner's one read returned `Unknown process id
99295`; it produced no terminal receipt. Actual native source establishes that
the manager belongs to the invoking native Session. The owning lead's tool does
not select the utility's manager by numeric ID. A38's permissible diagnostic
attempt therefore did not test the original manager. Preserve that failed read
and all original211 paired calls/31 other terminal commands; only the original
`gh run watch 43528601963 --exit-status` call
`call_78784388a337495bb0a86a631d6184ab`/session99295 remains unresolved. These are
lead/owner-supplied facts, not peer evidence read by architect.

**Pinned-source basis.** Selected2rq's retained Nix derivations lead through
codex94pabr to `openai/codex` tag `rust-v0.165.0`, expected source NAR
`sha256-b9PpwNQeZsJIN4wbGA3FLfWAKd2EDMN5E/zj/Y62/vk=`. The public annotated tag
`e374836b2728d9b7aa981c2902649e640a2edaa8` peels to
`360319d8dee62d87e2d59fc0c21805d79519cfed`. Source lines below were read from that
release; its collected NAR was not rebuilt or independently rehashed. Retained
native patch targets daemon package installation; postPatch adds a Rust recursion
limit, neither alters executor semantics. No live process/binary epoch was read.

- [Tool dispatch](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/handlers/unified_exec.rs#L25)
  selects `invocation.session.services.unified_exec_manager`. Numeric IDs are
  not a cross-thread lookup interface.
- [Manager construction](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/session/session.rs#L1768)
  creates a new manager for a new Session. Its process map starts empty
  (`unified_exec/mod.rs:147–177`), with no rollout-to-handle restoration.
- [Manager lookup/lifetime](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/unified_exec/process_manager.rs#L1859)
  reports unknown when that map lacks the ID. IDs can be reused after removal.
  Removal also occurs during cleanup/pruning, not exclusively after a collected
  completion. Listing returns only non-exited entries and original call ID,
  command and cwd. Hence unknown/empty listing is not an original join receipt.
- [Shutdown](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/session/handlers.rs#L276)
  calls manager termination. [Local process teardown](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/utils/pty/src/process.rs#L205)
  attempts kill, ignores its result, aborts I/O and detaches the waiter. This is
  not an acknowledged join. A retired/recreated context or native epoch change
  therefore does not positively prove99295 quiescent. No force-clean/terminate
  response is substituted for producer completion.

**Smallest concrete next capability, not released implementation.** Native0.165
already exposes experimental `thread/backgroundTerminals/list` with
`{threadId,cursor?,limit?}`. Its
[handler](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/request_processors/thread_processor.rs#L2558)
uses `get_thread` only (`load_thread:1019–1033`), refusing an unloaded thread;
it does not cold-resume it. Read every returned page for the exact utility
`01a1d74b-2c77-79a1-984f-0c5f7ada0667`. Require one matching row with
`processId="99295"`, original `itemId`, exact command and original cwd. This is
an existing public wire method, **not an established installed D CLI/MCP/HTTP
command**: the bounded D/dd90 source scan found no adapter for it. No raw socket
or new standalone native server is recommended.

If root releases a correction, its first sufficient boundary is a thin,
read-only exact-owner operator adapter to that existing method through the
registered connection. Bind operation/current lead/root/incarnation, saved
utility project/cwd/bootstrap/original launch receipt and current native service
identity; accept an operation ID, never arbitrary peer thread IDs. Reuse existing
owner admission and client transport; no monitor-store schema change, automatic
resolution, resume, new command or general history interface. Refuse unsupported
native capability, unloaded/changed context, bad pages and identity mismatch;
report a missing row as unavailable proof. Focused acceptance: cross-owner
refusal, exact full tuple, no-load behavior and missing/changed/reused-ID refusal.
This read can locate a surviving original handle; it cannot recreate a lost one.

**Conditional join and D guards.** A new turn on the same still-loaded utility
can use its existing manager; release `thread/resume` first checks for that
existing object, whereas cold resume creates new state. Do not cold-resume or
create a replacement to recover99295. D `monitoroperation/lifecycle.go:69–130`
does not compare latest turn ID with the immutable launch turn. With a launch
receipt, `launch.go:174…` preserves it; bootstrap validation checks the original
single metadata/marker, not unchanged prompt history (`headless.go:98–176`).
Current turn, prompts, queue and submission proof still must pass
(`codex/client.go:4427…`). Thus one properly receipted same-utility recovery turn
would not intrinsically strand resolution, but is a separate consequential
action, not currently released or exposed by monitor status/start replay.

Only after positively matching the live original manager/entry may root release
such a bounded join through existing accepted-send/receipt machinery: one stable
request, original thread/settings/bootstrap retained, only empty-input poll,
no command launch or repeated old terminal report. Preserve native service
continuity and recheck the original tuple before accepting its result; manager
loss/recreation or uncertain submission stops recovery. Terminal producer
evidence plus all known effects and ordinary ResolveEffects checks remains the
acceptance condition. No-row/unloaded cannot be repaired by a new reader or a
teardown assumption; it requires separately established original producer/OS
ownership and completion evidence. No new authority to stop or resolve follows
from this brief. Architect stops at this bounded access correction: no source
edits, tests, native calls, peer reads, process inspection or live mutation.

### A39/M2 — sufficient one-off read-driver brief (root-selected boundary)

**Current acceptance correction:** the private-passivity/inner-call amendment
below supersedes this draft's ordinary-client selection and its use of the outer
call ID as the expected native item ID. No live execution relies on those two
earlier assumptions.

Root selects a private operational driver, **not an installed adapter or product
change**, superseding that possible packaging in A39 above. Owner implementer2;
owned files only `/tmp/session-archival-utility-99295/M2/` source, binary and
provenance/quick-proof artifacts. No repository edits, runtime/pin stream or
deployment. Root inspects source and proof, then shares the exact hash/invocation
with the owning lead; only that owner executes it. No turn/start, resume, unload,
terminal termination, helper fallback or resolution is included.

**Inputs and transport.** Reuse M1's actual pinned dd90 Go client, module/toolchain
and connect-only `NewWithOptions`/`Ensure`/`Request` path. Use its fixed registered
socket `/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock`,30-second whole
operation context and ordinary Close. `ObserverOnly` must not be set: dd90's
allowlist excludes this read method; instead make the driver's method allowlist
literal. Initialization already advertises experimental API support
(`client.go:1058`). M1's transport inspection and compile environment are reusable
within those exact inputs, but its old binary/hash/compilation is not M2 proof.

Fix operation `a8c49117-6d98-4afd-9b5d-15afe4132919`, utility
`01a1d74b-2c77-79a1-984f-0c5f7ada0667`, original turn
`01a1d74b-3675-76e0-b039-354de57a1c2e`, call
`call_78784388a337495bb0a86a631d6184ab`, process string `99295` and command
`gh run watch 43528601963 --repo vpsfreecz/vpsadmin --exit-status` in the driver.
No arbitrary target flags. The earlier A39 shorthand remains historical; this
exact literal supersedes it for M2.
Require owner-supplied `--expected-root`, `--expected-cwd` and
`--expected-project` from its existing exact public monitor/launch evidence;
do not infer peer root/project/slug or use this session's cwd. Expected cwd must
be the canonical immediate `work/<owner-slug>` path under the fixed workspace
`/home/aither/workspace/ai/vpsfree.cz`. Owner execution precondition is current
operation owner/root/incarnation/socket and launch binding still matching that
saved evidence; flags alone do not establish ownership. The driver performs only
exact-root and exact-utility cold metadata/turn reads plus the terminal-list RPC,
never roster/session enumeration or monitor MCP calls.

Require root metadata ID/cwd match. Require utility metadata ID/cwd/project,
source `vscode`, empty fork parent; before/after cold `ReadTurnState` must retain
the fixed original latestTurnId with a terminal status and loaded `idle` or
`systemError`. `notLoaded`, active/new turn or identity change is a diagnostic
stop. Preserve caller-supplied identity provenance and the safe observed fields;
do not claim those reads establish a historical native epoch. Where inspecting
the fixed socket metadata, retain before/after device/inode consistency only;
do not inspect native processes or infer manager continuity from that alone.

**Exact public wire shape.** Release360319d8
`app-server-protocol/src/protocol/v2/thread.rs:1243–1277` defines:

```text
thread/backgroundTerminals/list
params: {threadId: string, cursor?: string|null, limit?: uint32|null}
response: {
  data: [{itemId: string, processId: string, command: string, cwd: string,
          osPid: uint32|null, cpuPercent: number|null, rssKb: uint64|null}],
  nextCursor: string|null
}
```

The current native implementation sets all three metrics null; they are not
process-identity proof. Decode required `data`/row strings distinctly from missing
or null, validate optional metrics types, and keep processId as a string.
Use `limit:32`, no initial cursor; echo each nonempty returned cursor exactly.
Bound to4 pages/128 entries and the single deadline. Repeated/nonadvancing
cursors, duplicate item/process IDs, malformed fields, exceeded bounds or changed
before/after identity make the result incomplete, never empty. Native pagination
uses ascending numeric process IDs with no fixed maximum;32/4 are conservative
driver bounds, not invented native guarantees
(`thread_processor.rs:6842–6867`). Compare the entire fixed call/process/command/
cwd tuple with exactly one row. A same numeric ID with any different field is
`identity-conflict`; do not normalize or fuzzy-match the shell command. If the
owner's saved literal command differs, return that discrepancy to root before
compilation/execution rather than weakening the match.

**Output and limits.** Exclusive-create0600 JSON, source/provenance0600 and
binary0700, like M1. Output timestamps, fixed/expected identity, projected
before/after metadata, page/count/completeness, exact matching row (if any), and
structured stage/outcome. Never retain raw thread/history, previews,
TerminalFailure.message, instructions, environment, credentials or unrelated
row commands. Use safe error categories/native numeric error code where
available, not raw server text. Distinguish `matched`, `not-listed`,
`identity-conflict`, `not-loaded`, `changed`, `incomplete` and `rpc-failed`.
Even `matched` is read evidence only; no-row/unloaded is **not** completion.
No output may declare effects resolved or authorize another native call.

**Focused acceptance and stopping.** Reuse M1's reviewed transport source and
exact dd90 inputs; inspect the new method/arguments and decode/guard code.
Compile M2 once in the same declared Nix environment with readonly module/offline
dependencies, record exact argv/input hashes/build metadata and new binary hash.
Small offline response cases cover exact match, wrong call/cwd/project, absent/
null data, duplicate/cursor loop, bounded pagination and notLoaded/identity
change; no live server/proxy/daemon or full package suite. All compilation and
proof effects must join before root inspection. These private diagnostic
artifacts follow the existing M1 evidence boundary: no instruction requires
promoting this bounded read-only operational artifact into shipped product or a
new runtime commit. A scope change into a reusable product interface would need
separate release/review. No next action is released by preparing M2; root decides
only after the owning peer returns its exact result.

**M2 exact-owner clarification (peer provenance
`cbd2b28a-38b1-4e19-88ea-b742f19b0c4d`).** Keep the required expectation flags,
but now restrict their values to the supplied owner root
`01a18d34-3f9e-7883-bcf8-ca3a000bbff3`, utility project
`01a1d74b-2c38-7c51-b342-98d510cdf310` and cwd
`/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy`.
These replace unknown owner inputs; they do not grant cross-session access.
Loaded idle/systemError plus terminal fixed-original-turn applies **only to the
utility**. The root may be active: check root ID/cwd and unchanged before/after
ReadTurnState thread identity/latestTurnId/status without requiring root idle or
terminal. Compare safe selected fields, not error-message/transcript content.

Native commit360319d8 establishes exact command representation:
`tools/handlers/unified_exec/exec_command.rs:243` clones `args.cmd` into
`hook_command`; shell argv is constructed separately at279–282; request400–404
carries the former. `unified_exec/process_manager.rs:1262–1269` stores it and
`:1876–1890` emits that value as `row.command`. Thus M2 compares the full literal
including `--repo`, with no shell-wrapper removal or fuzzy normalization. A
PreToolUse rewrite can change the accepted literal; a conflicting row is evidence
to report, not permission to adjust the guard. For a row carrying the fixed
call/process, retain its bounded candidate tuple privately with mismatch fields;
do not emit other row commands or raw errors. With dd90's unexported RPC error
code, safe stage/categories alone are sufficient; no raw-message parsing or
invented numeric-code accessor. These are source-only clarifications; architect
has completed its rollout edits and implementer2 may append its final M2 receipt
in the agreed exclusive window.

## A40 — conditional same-loaded-utility continuation; no action release

**Applicability and actual remaining boundary.** M2 remains read-only. A40 is
inapplicable if M2 finds no exact tuple, an unloaded thread, changed identity or
any incomplete/error result. Positive M2 is necessary but not sufficient. Pinned
dd90 has one suitable existing receipt-aware public SDK call, **only for an
exact failed original native turn**:

```go
client.ContinueFailedTurn(ctx, utility, recoveryText, stableID,
    actionContext, originalTurn, codex.TurnOptions{})
```

`codex/continuation.go:8–127` never resumes, steers, changes policy or starts queued
work. It double-checks loaded idle/systemError, exact latest failed turn, prompts,
queue and known submissions, then uses the ordinary durable send ledger.
M2's completed/interrupted statuses do not qualify; synthetic monitor incomplete
does not establish native failure. Generic `SendWithOptions` is unsuitable
because it calls `resumeThreadWithPolicy` (`client.go:5471…`). No installed
D CLI/MCP/HTTP invocation for this utility continuation was established. A
separate one-off M3 would be the operational artifact boundary if all predicates
below become satisfied; it must never add mutation to M2.

**Native call and persistence.** With empty options the SDK's request is
`turn/start` with `{threadId,input:[{type:"text",text:recoveryText}],
clientUserMessageId:stableID}` and no model/effort/instructions override.
Native360319d8 `app-server/src/request_processors/turn_processor.rs:377–391,525–543`
looks up the existing `Arc<CodexThread>` and checks direct-input/provider
admission. It does not cold-load/resume a missing thread. A turn on that same
loaded Session reuses its executor manager; recreating the Session creates an
empty manager. Original launch receipt and bootstrap marker must never be
rewritten or reissued. D's resolution does not require latestTurnId to remain
the launch turn, but all new submissions, current native activity and effects
must be accounted for as established in A39.

**Same-manager limitation must not be hidden.** `ContinueFailedTurn` explicitly
requires the application to hold its existing shared admission fence and exclude
other native clients: the protocol has no compare-and-start. The ordinary SDK
`requestWithAdmission` calls `Ensure`, which may reconnect, and does not pass a
fixed expected connection generation (`client.go:1122–1178`). Its exported
`ObserverGeneration`/`FreezeObserverWrites` support ObserverOnly clients, which
cannot submit `turn/start` (`observer_events.go:127–145`). Therefore this public
SDK alone does **not** meet A40's strict requirement to refuse submission across
manager loss/recreation. Socket-inode checks or post-send status cannot be
promoted to that missing admission guarantee. Root must establish an existing
ordinary owner/admission and connection-continuity boundary before releasing
M3; none is invented here. This is the first sufficient source stopping point,
not a request to redesign transport or weaken the requirement.

**Conditional M3 contract if that boundary is established.** It stays a separate
private operational driver using actual dd90 and the registered connection, with
the fixed M2 owner/workspace/project/utility/original-turn/call/process/command/
cwd tuple. Inside the accepted ordinary owner execution/admission window, repeat
the full loaded-row match and effective settings/authority checks immediately
before calling the SDK. Preserve settings, original marker and immutable monitor
outcome. Any native disappearance, fresh manager, competing writer or uncertain
identity refuses and retains the fence. No fallback to ordinary Send/resume,
new command, new watcher, new native process or direct raw request is allowed.

Use one root/owner-approved stable UUID and exact recovery text/action context;
bind original turn, command/call identity and settings digest into the action
context. Reuse the deployed submission store through public SDK configuration,
not M1's default legacy file: D `main.go:57–85` selects
`<stateRoot>/submissions/<sha256(socket)>.sqlite`, the corresponding `.json`
import path and original socket-adjacent legacy import path. Derive the registered
state root under owner authority; no direct record editing, isolated replacement
ledger or silently repeated initialization. `ContinueFailedTurn` owns prepared,
submitting and accepted states and the native receipt. On uncertainty stop;
`ReconcileSendWithOptions` with unchanged identities is the supported read/recovery
path, not another submit or a new ID. Direct `Request` plus `PrepareSend` cannot
replace this: preparation alone does not record the actual submitting transition.

The visible follow-up permits exactly one awaited empty-input `write_stdin` for
session99295 (`chars:""`, wait5000ms, bounded output), then returning its receipt.
It forbids `exec_command`, signals/nonempty input, further polling, new watcher,
changed old monitor reports and development work. A new turn is not itself proof
of the old command's completion. Require the matched original producer result,
all new outer-cell/tool receipts, accepted new turn receipt and final native
quiescence before the owning lead considers existing ResolveEffects. Unknown or
running remains truthful; neither remote CI status nor the failed probe is
rewritten. No terminal report is resubmitted to an occupied immutable slot.

Root owns the later decision after M2 and peer authority. No M3 implementation or
execution is released by this conditional brief. Preparing a one-off driver from
existing public APIs would not itself require runtime/pin changes, but those APIs
have not yet discharged the strict connection/admission gap above. Architect
performed source reads and this design amendment only; rollout remains reserved
for implementer2's M2 appendix. No peer data, model/native call, tests or mutation.

### M2 acceptance amendment — passive incoming handling and inner call identity

Peer `df0adf62-04a5-4d94-b0db-544a9df7c79a` correctly identified an omitted write
path in the ordinary pinned client. dd90 `client.go:1416–1430` processes
server-initiated requests; unsupported requests reach `rejectUnsupported`, which
writes a JSON-RPC error directly through `writeOn` (`:1650–1680`), outside M2's
outgoing-method gate. No native attachment/routing proof was established that
makes such a request impossible. An outgoing allowlist alone cannot justify the
read-only claim.

**Root-selected artifact correction:** make a private
copy of exact dd90 under the existing M2 artifact directory, add only
`thread/backgroundTerminals/list` to the existing ObserverOnly read allowlist
(`client.go:1132`), and set the main M2 client to `ObserverOnly:true`. Keep the
incoming handler byte-identical: its ObserverOnly branch precedes normalization
and rejection, broadcasts locally and continues without answering. Keep the cold
history reader passive, all target/pagination/output guards, and no watch/resume
or callback-registration path. The existing native list is get-thread-only, so
this exact addition allows a read, not a lifecycle operation. No public option
was found that independently suppresses those replies in ordinary mode.

This is a deliberately disclosed derivative operational dependency, not stock
dd90 and not a new product version. Record upstream revision/tree, exact one-line
diff, private module replacement, full source/dependency/binary hashes and new
compile receipt. Do not edit the shared module cache, canonical repository,
runtime checkout, pins or installed package. Root inspects the exact private
diff and source proof before sharing execution instructions. Focused offline
checks must include an unsupported incoming server request producing **no**
reply while the exact background-list read is admitted, plus rejection of a
write/lifecycle method. Reuse existing client fixtures where possible; no native
server, live socket or transport reimplementation. Architect has not applied
this patch. Root owns the implementer2 preparation release and execution decision;
all previous artifacts remain retained with their original limitations.

**Independent item-ID correction:** native360319d8
`core/src/tools/code_mode/delegate.rs:323` generates a new inner tool call ID;
`:224–228` dispatches that ID to the nested tool.
`tools/handlers/unified_exec/exec_command.rs:176–182` passes it into
UnifiedExecContext; `unified_exec/process_manager.rs:1262–1269,1876–1890` stores
it and emits it as `itemId`. Therefore the supplied outer
`call_78784388a337495bb0a86a631d6184ab` is source-call provenance, **not** a proved
expected row.itemId. Retain the outer ID as historical provenance and any observed
inner ID as current native metadata, with their different meanings. Do not
generate an inner ID, strip a prefix or promote an observed candidate into
independent historical proof.

**Root's consequential read boundary:** a pre-known inner item ID is not required
for this authorized fixed-owner metadata discovery. M2 may read the existing
loaded exact utility's terminal metadata under all fixed root/project/workspace/
utility/original-turn guards. Privately retain only rows for known process99295;
discard every other row. Check the exact full command and cwd without fuzzy or
substring matching. A unique consistent tuple is reported only as `candidate`,
with `observedItemId`; conflicts remain `candidate-conflict` plus explicit
mismatch fields. Missing, malformed, duplicate or incomplete results keep their
existing diagnostic categories. Do not emit `matched`, `authenticatedOriginal`,
completion or resolution. No native contract requires a pre-known item ID to
perform this read, and no additional privacy/authority risk was identified within
this fixed authorized owner target and restricted output.

This disclosure supersedes the earlier M2 full-match outcome wording, not the
original-artifact history. Before any recovery mutation, the owner must establish
the independently retained original native command ID or separately source-proven
full history uniqueness/manager binding. A current candidate cannot supply its
own historical authentication. A40 stays unreleased: candidate-only M2 output
does not prove original-manager continuity, completion or permission to start a
turn. No recovery mutation, arbitrary target or weaker ownership inference is
authorized by root's read-only classification.

Routine source facts and the execution hold were sent to implementer2 and root.
Rollout appendix ownership remains with implementer2. These source corrections
add no peer access, live call, lifecycle action or change to frozen734/D.

### A39/M2 socket alias correction — accepted existing contract

Root accepted peer-owned evidence `291b674e` and superseded the proposed expanded
alias/target helper. The fixed registered socket path is a normal symlink;
an `Lstat` socket-type check rejects that supported registration. Peer inspection
reports its target is a UID1000 socket, mode0600, dev64769/ino18744292 with
ctime1794148953681548376, matching the saved a8 native epoch. This is supplied
owner evidence, not an architect live lookup. The cited D contract is
`portal/internal/session/recovery.go:222–234`: `unix.Stat` follows the registered
path, requires `S_IFSOCK`, and uses boot/dev/ino/ctime authority;
`monitoroperation/authority.go:84–88` consumes that identity.

The accepted correction is solely `os.Lstat` → `os.Stat` in the peer's private
driver copy. Retain the fixed path, existing target identity/stability checks,
passive transport and candidate-only RPC/output guards. Root assigned the peer
the new hash, warm build, offline alias/changed-target cases and affected review
before its own single read. No second artifact or alias-fingerprint framework
will be prepared here. Prior artifacts and receipts remain unchanged;
implementer2 stays parked with capacity available. This correction grants no
recovery mutation or completion inference and changes no runtime, repository,
pin or installed package. Architect records this decision only; no additional
investigation, patch, build, live lookup or driver execution is assigned.

## A41 — reconcile current local effects without inventing a historical exit

**Sufficient contract conclusion.** An original exit receipt is the preferred
proof, but it is not the exclusive evidence permitted by D's existing resolve
contract. The controlling skill requires evidence to “account for the source
command and every known operation-owned code cell or tool session”; it forbids
leaving known effects uncertain. D `docs/dev-sessions.md:264–282` separates that
acknowledgement from the immutable outcome. `monitoroperation/service.go:266–325`
checks the exact lead/current owner, reconciles launch, invokes native proof and
saves immutable evidence; `lifecycle.go:69–130` requires known launch/delivery
receipts and current native quiescence. Neither requires the old command's exit
code. A complete, positively bounded current-effects reconciliation can therefore
support resolve while retaining `incomplete` and an unknown historical exit.
This corrects any earlier reading of A37–A39 as requiring a producer receipt
exclusively; it does not weaken their known-effects accounting requirement.

**Supplied evidence, not new architect observations.** Peer M2 `030286ce` exited2
at `before/not-loaded`, before pagination, with exact original completed turn and
unchanged native socket epoch. It supplies no process result. A40's same-loaded-
manager continuation is inapplicable. Owner inventory accounts for 211 paired
outer calls and 32 native launches, 31 terminal. The sole remaining invocation
is session99295, exact command `gh run watch 43528601963 --repo vpsfreecz/vpsadmin
--exit-status` in the retained OOM session cwd. An explicit inventory of returned
yielded-cell handles must also establish no unjoined cell that could still spawn
work; pairing an outer call with a response alone does not establish that.

**Actual backend boundary.** Native360319d8
`tools/handlers/unified_exec/exec_command.rs:253–281,400–409` selects the turn's
environment/shell and records the command. `unified_exec.rs:133–157` applies the
configured login-shell default when no override is supplied; the literal command
alone does not prove absence of shell/hook wrappers. In
`unified_exec/process_manager.rs:1359–1402`, remote environments **or a shell
snapshot** use the selected execution backend; only the remaining branch calls
local `codex_sandboxing::spawn_process` (`:1459–1473`). Thus a local-looking cwd
does not alone prove the original OS domain. The owner must bind the actual local
backend/namespace, shell and effective command from its retained launch/config
and already inspected source. Account for any actual wrapper/background launch;
do not invent hypothetical effects, but do not assert arbitrary wrappers harmless.
The literal GH watch observes an existing run and grants no remote cancellation
or resource-mutation ownership. Native teardown still ignores kill errors and
does not await the waiter (`utils/pty/src/process.rs:219–269`), so unloading is not
the missing proof.

**Smallest owner-side route: one bounded standard OS metadata reconciliation.**
No new client, product primitive or cold resume is needed to try this route.
Root first agrees its exact administrative read scope with the owner. Use the
known native/execution service's ordinary `systemctl --user show` metadata
(`MainPID`, `ControlGroup`, `InvocationID`, start timestamp) and its actual local
execution domain; do not assume the native unit contains a separate backend.
Read only process metadata needed to cover that domain, including surviving
descendants after reparenting. For numeric OS PIDs, permitted fields are UID,
`/proc/<pid>/stat` state/PPID/pgrp/session/start ticks, `cgroup`, and candidate-only
`exe`, `cwd`, NUL-delimited `cmdline`. Session99295 is not an OS PID. No environ,
memory, credentials, unrelated command dump or peer project/history reads.

Bind candidates to the original start interval, actual creator/execution domain,
UID, executable, full argv and cwd, plus the already complete invocation history.
Do not use a current-parent-only walk: an orphan may have been reparented. A
negative result is sufficient only when the owner establishes that this is the
complete surviving domain for the known shell/command and any children, with no
unaccounted remote backend, detached work, pending cell or remaining producer.
Record scan coverage/errors and repeat identity checks at its end; unreadable,
changing or ambiguously excluded candidates keep the fence. Repeated empty
`pgrep` or PID absence does not establish this coverage. If the scoped domain
cannot cover surviving children, report that exact boundary rather than widening
the read silently or asserting completion.

If an exact owned process is alive, retain the fence and its `(boot,PID,start)`
identity. An identity-checked pidfd can observe its later exit without signals;
non-parent observation need not recover the historical exit code and is not
`waitpid` ownership. Account for its children separately. No interruption is
released here. If the complete bounded domain contains no executable work for
this invocation, and no remaining cell/queue/native submission can create it,
the combined evidence establishes **current local quiescence**, even though the
historical exit status remains unknown. Ordinary resolve then repeats its native
and receipt guards under its existing locks; no claim of joined original output,
successful CI, manager-teardown success or recovered exit is permitted.

**Acceptance and stop.** The exact owner may use existing stable-ID resolve only
after accepting the complete inventory, actual backend/domain binding, bounded
current OS proof and unchanged ordinary native/receipt guards. Detail must say
which current effects were reconciled, when and how, and explicitly retain the
original incomplete outcome and missing exit receipt. Remote CI is independent.
The missing fact presently is owner evidence of the actual execution domain and
its current known effects, not a proved need for a new API. This brief authorizes
no read or mutation by architect, no signals, re-entry, retry, lifecycle action
or package change. Lead owns the administrative read release and subsequent
resolution decision; frozen734/D and deployment evidence remain unchanged.

### A41 clarification — actual default selector and local snapshot backend

Peer `26094ef7` need not recover a missing rollout-header field. D
`monitoroperation/launch.go:107–108` supplies only session shell-environment
variables to dd90 `StartThreadWithSettings`. dd90 `client.go:3730–3759` serializes
cwd/config/settings/project, not native `environments`; its launch `turn/start`
at `:5545–5567` also omits that field. Native360319d8
`thread_processor.rs:1502–1505` therefore uses the manager's default environment
requests. `turn_processor.rs:738–746` preserves them when no override is supplied.
An exec command without `environment_id` selects the primary ready environment
(`core/src/tools/handlers/mod.rs:163–205`). This is inheritance, not a hardcoded
local guarantee.

The actual selector is constructed once for the daemon in
`app-server/src/lib.rs:638–647`. Ordinary startup uses
`EnvironmentManager::from_codex_home`; `exec-server/src/environment.rs:198–207`
gives a configured Noise environment precedence, otherwise reads
`CODEX_HOME/environments.toml`. The exact managed path is
`/home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/environments.toml`
(D `workspace-host:3765–3779`). Its top-level `default`, `include_local` and
configured environment IDs determine the available selections
(`environment_toml.rs:76–102,234–275`). With no explicit default and local enabled,
the default is local; with no file, `CODEX_EXEC_SERVER_URL` unset/empty selects
local, `none` disables execution and another value selects remote
(`environment_provider.rs:72–122`). Noise selectors take precedence over either.
The managed unit and D `run_codex:1769–1787` do not force this selector: its
`codex_environment` preserves inherited environment values while replacing the
registered storage paths. Model-provider `-c` arguments are unrelated.

**Minimal owner fact:** establish the daemon-startup selector as **local-only**
from that one configuration path and the applicable inherited-selector presence
in retained launch/service configuration. Project only file presence,
`default`, `include_local`, configured IDs, and whether the URL/Noise selectors
were effective; no URLs, programs/args, tokens, provider credentials or
`/proc/environ` read is requested. Noise's deciding names are
`CODEX_EXEC_SERVER_NOISE_REGISTRY_URL`, `CODEX_EXEC_SERVER_NOISE_ENVIRONMENT_ID`
and `CODEX_EXEC_SERVER_NOISE_AUTH_TOKEN`; only absence/presence is relevant.
Current configuration alone is not historical startup proof if it changed.
If additional environments were configured/added, report their bounded identity
set rather than inferring local-only from `default=local`: startup includes
configured IDs after the default (`environment.rs:385–402`), and primary uses
the first ready environment (`environment_selection.rs:1279–1280`). This is the
concrete remaining owner configuration predicate, not a demand for richer headers
or an unbounded remote inventory.

Once local-only is established, both possible executor branches are local by
construction. `Environment::local` (`environment.rs:788–805`) binds
`LocalProcess::with_local_runtime_paths`, with no remote client. Even when the
shell-snapshot branch calls `get_exec_backend`, this same in-process backend
prepares the snapshot then invokes `codex_sandboxing::spawn_process`
(`local_process.rs:380–434`). It does not launch or select a separate remote
exec-server. Therefore absence of the historical shellSnapshot flag does not
block a host-local OS-domain reconciliation. This source result narrows A41's
earlier backend caveat; shell/known-child effects and the complete current-effects
proof still apply. Architect read canonical/public source only and stops here;
root owns the bounded owner configuration check and all operational decisions.

### A41 clarification — redacted shared-daemon selector projection

Noise is possible in the ordinary app-server entrypoint; it requires no special
CLI flag. Native360319d8 `environment.rs:641–685` reads these exact activation
keys from the daemon environment:

- `CODEX_EXEC_SERVER_NOISE_REGISTRY_URL`
- `CODEX_EXEC_SERVER_NOISE_ENVIRONMENT_ID`
- `CODEX_EXEC_SERVER_NOISE_AUTH_TOKEN`

Each is obtained with `std::env::var(...).ok()`, trimmed, and discarded if empty.
All three effectively absent means no Noise; all three nonempty constructs the
Noise configuration, subject to validation; a partial set fails initialization.
`CODEX_EXEC_SERVER_NOISE_CHATGPT_ACCOUNT_ID` is optional context, does not activate
Noise and need not be read for this proof. The auth-key literal is defined in
`protocol/src/shell_environment.rs:9`. Both `from_codex_home` and `from_env`
perform this check first. `--ignore-user-config`, if actually selected, skips
the TOML file but does not disable these environment selectors.

The complete minimal environment projection is those three keys plus
`CODEX_EXEC_SERVER_URL`. Emit only per-key `unset`, `trim-empty`, `nonempty`
for Noise; URL uses `unset`, `trim-empty`, case-insensitive `none`, or `other`.
Unexpected encoding/duplicate-key ambiguity is a structured unknown, never a raw
value. No URL, token, account ID, length/hash of a secret or other environment
value belongs in output or retained evidence. Prefer original launch/service
metadata that covers the effective inherited startup environment; a current
systemd manager configuration alone is not the old process environment.

If retained metadata is insufficient, root may separately authorize a redacted
read of **its shared registered native service**, not the peer utility process.
This explicitly extends the earlier A41 no-environ scope. Bind before and after
to supplied PID1309145/start75094898/exe2rq, registered unit/boot identity and full
socket target epoch; refuse any change. `/proc/<pid>/environ` has no key-selecting
kernel interface: an in-memory parser necessarily reads its NUL-delimited bytes,
discards nonallowlisted fields and emits only the four classifications. Do not
describe that as reading only four kernel fields, use a shell environment dump,
or retain raw bytes. No such read is performed or released by architect.

The single file is the registered native home's `environments.toml`, not the
peer session config. Its schema is top-level optional `default:string`, optional
`include_local:bool` (defaults true), and `[[environments]]` tables with `id:string`.
`default` is Rust-trimmed before matching: `" local "` selects built-in local,
`"LOCAL"` does not, whitespace-only is invalid, and trimmed `none` is
case-insensitive disabled. Omission is distinct from an empty string. Table IDs
must already equal their trimmed form; exact `local` and case-insensitive `none`
are reserved and forbidden there (`environment_toml.rs:248–307`). Both top-level
and environment-table unknown keys refuse parsing; retain that unknown result.
Project only those fields/IDs and file presence; do not copy table transport,
`auth_bearer_token`, `env`, program/args or other content. Unknown fields/parse
errors must remain diagnostic without raw input. Native
`environment_toml.rs:234–245,331–351` reads it into the startup provider snapshot;
`app-server/src/lib.rs:638–649` constructs one shared manager. Ordinary new
threads use that manager, not a per-thread reread of the file. Separate explicit
environment registration can change the available set, so known such changes
must be accounted for rather than attributed to a file reread.

For an existing file, bind its current identity and nanosecond mtime/ctime before
and after projection to the same daemon start/boot clock basis. Pre-start times
with no known replacement/restore/config change support the ordinary trusted-local
unchanged-file inference; timestamps alone are not a retained startup snapshot.
Any later timestamp/change leaves startup applicability unproved and calls for
the retained version or exact owner configuration history. Current ENOENT alone
does not prove startup ENOENT. Do not equate a source-package timestamp or socket
ctime with the configuration load time. These limits concern evidence provenance,
not a new product gate or permission to inspect broader configuration. Stop once
the bounded startup selector is established; no backend inventory is added.

### A41/S2 result — residual historical configuration assertion

Root reports frozen probe6b22/result3fd9a7ce exited0 silently, with before/after
PID/start/exe/boot/socket identity checks passing and all four startup selectors
unset. The fixed TOML path is absent now; its parent timestamps are post-start.
These supplied facts establish no Noise/URL override, but do not establish the
TOML state when this same daemon initialized its environment manager. No process
domain, completion or resolution claim follows from S2 alone.

No already-exposed passive D/dd90 reader of that manager's startup selection was
established. dd90 `codex/client.go:524–537` ThreadMetadata and D
`workspacecodex/observation.go:33–45` ThreadObservation expose identity/activity,
not this environment-manager configuration; the examined installed CLI/MCP/web
adapters contain no environment-list/read route. A generic SDK Request method
does not establish an executable supported invocation within the no-new-client
boundary. Do not add a probe, transport, build or reader to close this residual.

The precise remaining operator assertion is: **at initialization of the bound
PID1309145/start75094898 native epoch, the registered
`codex-homes/vpsfree-cz/environments.toml` was absent, or its then-effective
contents configured only local execution.** The owning operator may establish
that from retained configuration/deployment history or direct knowledge of its
administration; preserve the evidence basis and any known subsequent explicit
environment change. Current absence, later parent timestamps, cwd/full-access
headers and successful CI cannot substitute for that assertion. If the operator
cannot establish it, retain this specific historical uncertainty and stop;
neither another selector nor a generic inventory is proposed. Architect performs
no shared/peer startup metadata or native read and remains available.

### A41 startup-log clarification — no affirmative selector event

The bounded source check found no deterministic positive startup record of
local-only fallback or loaded TOML default/configured IDs. Native360319d8
`environment.rs:198–240,288–371`, `environment_bootstrap.rs:41–61`,
`environment_provider.rs:72–115` and `environment_toml.rs:234–245,331–351`
construct/return the snapshot without logging that choice. The immediate caller
`app-server/src/lib.rs:638–650` constructs the manager silently. Its later generic
process-start metric (`:664`, `core/src/otel_init.rs:100–105`) receives no
environment selection. Local `start_connecting` returns immediately
(`environment.rs:1101–1104`); individual readiness/remote-failure events cannot
certify the full startup set. D's `workspace-host:1772–1787` records registration
and execs native, not the environment snapshot.

There is therefore no suitable affirmative event/target/level in this chain to
request from retained logs. Binding a generic startup record to the original
PID/boot/start would not supply its missing selection fields. Absence of any log
proves nothing about configuration. The precise historical operator assertion
above remains; no journal, telemetry, SQLite, shared-file or peer-data scan is
proposed or performed. Investigation stops at this source result.

### A41 final executor-log alternative — conditional positive evidence exists

This is separate from the silent environment constructor above. Native360319d8
`exec-server/src/process_telemetry.rs:32–75` emits INFO events on
`codex_otel.log_only`: `codex.exec_server.process_start` and
`codex.exec_server.process_exit`. Fields retain launch-time `conversation.id`,
`tool.call_id`, optional launch trace/span and executor registration, sandbox type,
exit code and termination-requested state. They omit turn, scoped handle99295,
argv and cwd; controller-supplied correlation is not itself authorization.
`local_process.rs:380–499` emits Start after actual local spawn and running-entry
insertion. Exit at `:1068,1126–1132` follows its exit receiver, but **-1 can mean
wait failure or closed channel**, not a proved joined process. Successful pipe/PTY
waits supply the actual exit code (`utils/pty/src/pipe.rs:271–290`,
`pty.rs:432–447`). Kill requests, drop, errors and missing events remain insufficient.

An original-invocation binding needs the owned source/history and native inner
call identity, not the outer functions.exec call. The INFO
`unified_exec.exec_command` span records conversation, original turn, native call
and `unified_exec_process_id` (`core/src/unified_exec/process_manager.rs:507–518`).
Its `codex.unified_exec.process_start_requested` event (`:1379–1386`, target
`codex_otel.trace_safe`) links the backend `process.id=99295-UUID`; it proves only
a request. A lifecycle event must correlate to that original invocation before
use. Remote executors emit the same event names: positive local-spawn proof also
requires original managed-native/local-emitter provenance, never event name,
handle alone, absent registration or a later candidate.

There is an existing, conditional retained source: enabled `RUST_LOG` records
reach text or `LOG_FORMAT=json` stderr, with enabled span NEW/CLOSE records
(`app-server/src/lib.rs:178–180,728–768`). The managed daemon routes this through
its existing `pid_file.with_extension("stderr.log")`
(`app-server-daemon/src/lib.rs:302–313`). Retention is lossy and bounded: current
1MiB, previous tail256KiB, queue64, maximum record16KiB
(`backend/stderr_log.rs:18–22,39–43,165–181`). The native SQLite log layer explicitly
excludes both event targets (`state/src/log_db.rs:74–75`); do not direct a logdb
scan for them. No owner-only per-command retained reader was established.

A suitably retained, epoch-bound original exit event without the synthetic -1
ambiguity can supply missing command-terminal evidence alongside the already
accounted effects; an authenticated original local-spawn event can establish the
invocation's execution domain for the bounded A41 current-effects reconciliation.
Neither availability nor such correlation has been observed. Any projection of
the shared managed log requires a separate root/owner operational-read decision,
restricted to the original utility/turn/call/handle and bound daemon epoch; it is
not permission for a global log or peer-content read. Disabled, missing, pruned
or insufficiently bound events prove nothing. Original INCOMPLETE/unknown outcome
is preserved. No logs, databases, process metadata or peer records were read;
source investigation stops here without a new reader or implementation package.

## A42 — exact active-utility steer through a private SDK entry

**Sufficient source-only brief; preparation/execution not released.** No installed
exact-owner utility-steer invocation was established. D's monitor request decoder
(`portal/cmd/workspace-portal/monitor.go:33–82`) admits start/report/resolve/status/
cancel, not steering. Existing conversation/team authorization does not turn a
monitor utility into a retained member. dd90's exported `SendWithOptions`
(`codex/client.go:5421–5567`) calls `resumeThreadWithPolicy` before deciding between
steer and start. It therefore cannot satisfy this request. `ContinueFailedTurn`
starts a new turn and is also unsuitable. `PrepareSend` plus generic `Request`
would omit the durable submission claim. The missing capability is one narrow
SDK entry, not a missing native protocol or a new product service.

**Existing native contract.** Native360319d8 accepts:

```json
{"threadId":"EXACT_UTILITY","expectedTurnId":"EXACT_ACTIVE_TURN",
 "clientUserMessageId":"ONE_STABLE_ID",
 "input":[{"type":"text","text":"OWNER_APPROVED_DRAIN_INSTRUCTION"}]}
```

Method `turn/steer` returns `{"turnId":"EXACT_ACTIVE_TURN"}`.
`app-server-protocol/src/protocol/v2/turn.rs:317–352` defines these fields;
`turn_processor.rs:1045–1160` uses get-thread-only lookup, direct-input/provider
admission and an expected-turn precondition. Native
`core/src/session/turn_input.rs:843–928` checks the active regular turn under its
lock and appends pending input to that same turn. Missing/wrong/non-steerable
turn refuses. It neither cold-loads nor starts a replacement turn.

**Private derivative boundary.** A separately reviewed owner-controlled
operational artifact may add a single method inside a private copy of pinned
dd90, for example:

```go
func (c *Client) SteerActiveTurnConnected(ctx context.Context,
    threadID, text, clientID, actionContext, expectedTurnID string,
    expectedGeneration uint64) (SendReceipt, error)
```

This is a proposed private addition, not an already-exported method. The wrapper
fixes the owner's exact operation/root/incarnation/workspace/utility/project/cwd/
active-turn tuple and authorized drain text; no arbitrary target or method input.
The owner verifies its explicit action authority and fresh exact session/monitor
binding; the applicability clarification below defines the executable guards.
Bind the registered package/native service/socket epoch before use;
bind the connected SDK generation separately. Use the existing application
submission SQLite store and import paths (D `main.go:57–85`), never a fresh
isolated ledger or direct ledger writes. Preserve original monitor receipts.

Use a dedicated `ObserverOnly:true` client with no watches, implicit resume or
request-answering callback. Its existing incoming no-answer behavior stays intact.
After an explicit connect-only `Ensure`, capture nonzero ready
`ObserverGeneration`; never recapture it to recover a disconnect. The new private
method is a deliberately disclosed, exact steering exception using
`requestConnectedAdmission`, not an expansion of generic Request's allowlist and
not a repurposing of the frozen read-only M2 artifact. No native method other than
the fixed steer can be emitted by this entry.

**Reuse the existing ledger and writer, in this order.** Hold
`queueUpdateLock(threadID)`; normalize fixed empty `TurnOptions`; read the exact
attempt with `sendAttemptWithOptions` and reject a queue attempt, conflicting
identity/options or an existing non-steered attempt. Bind expected turn and owner
generation identity into the immutable actionContext. An accepted attempt returns
only its exact expected-turn/client-ID/Steered receipt. A submitting attempt is
read-reconciled only, never sent again. An absent/prepared attempt requires current
loaded active identity and `ActiveTurnID == expectedTurnID`, unchanged owner
admission, and known other submissions (`requireSubmissionAttemptsExcept`); refuse
unrelated queued work without starting or deleting it. Record preparation through
`recordSendAttemptWithOptions(..., steered=true, TurnOptions{})` if absent, then
repeat the active-turn check.

Call only `requestConnectedAdmission(ctx, expectedGeneration, "turn/steer", ...)`.
Its admission callback invokes existing `claimSendSubmissionExact(..., true)` and
retains the claim ID. That transition atomically changes prepared to submitting
under the existing durable store before the native write. The helper rejects
changed/not-ready connections without `Ensure`; `writeOfferAdmission` repeats
connection/generation and context checks under the writer lock
(`client.go:1151–1197,1282–1336`). No resume/start/interrupt, policy change, queue
start or reconnect fallback exists. Native expectedTurnId closes the active-turn
race at admission, independently of the earlier read.

On a matching native response, use `finishAcceptedSend` to persist the accepted
receipt with exact turn/client ID and `Steered:true`. An unknown/mismatched response
or post-write transport failure stays submitting/unknown unless bounded exact
history proves acceptance. Reuse `sentByClientID`/`waitForSentByClientID`, but check
the expected turn **before** marking accepted; do not blindly accept a matching
text/client ID on another turn. Existing accepted receipts are checked likewise.
Use the SDK's existing provably-unwritten and typed explicit-refusal restoration
helpers/claim handling; do not invent an error-string classifier. A before-claim
refusal is unsent; an uncertain write is not. No automatic retry, new stable ID,
idle-start fallback or second steer. Later explicit recovery may only reconcile
the unchanged identity; preserve uncertainty if history cannot establish it.
The existing SDK's bounded two-second post-error reconciliation is sufficient;
it is not permission for an ongoing polling loop or an automatic resend.

**What reaches the utility.** Accepted steering appends model-visible pending
input to its original active turn. It is not a `thread/queue` item waiting for a
new turn, but consumption still depends on that turn reaching input processing.
It does not preempt a blocked tool call, execute `functions.wait` itself, or prove
the cell ended. The owner's text may instruct that exact utility to terminate
its own known cell7 with `functions.wait(cell_id:7, terminate:true)`, await the
actual result and account for every known poll/tool session. No other caller may
guess or operate on its handle. Terminating a cell does not by itself prove all
nested commands ended. Require the accepted steer receipt, actual utility
consumption/action receipts, all remaining effects accounting and final ordinary
native quiescence before considering existing resolve. If the utility never
consumes accepted input, retain pending/unknown work; no interrupt or new-turn
fallback is authorized by this design. Monitor cancel alone does not stop it.

**Narrow acceptance for any later owner preparation.** Offline cases must cover
exact active acceptance, ended/wrong turn with zero start/resume calls, generation
change/disconnect, concurrent exact claim, lost reply with no resend, wrong-turn
history refusal, queue/identity conflict, and no answers to unsolicited native
requests. Record the exact private SDK delta/source/binary provenance; no installed
product/API/runtime/pin/CI stream changes. Existing internals support this contract
without a new ledger, transport or authority framework. Root accepts/releases any
preparation separately; the peer alone adopts and executes under its user's
local-observation stop authority. A41's historical configuration question remains
separate. Architect performed source/design only and stops here.

### A42/S3 refinement — bind reused reads before Ensure

Implementer2's source finding is correct: `ActiveTurnID` (`client.go:5962`),
`nextThreadItems` (`:2464`) and `ListQueue` use generic Request. Checking only the
final steer generation leaves those helpers able to call Ensure. The smallest
accepted private seam is one unexported, typed context scope, created only by the
new entry, carrying the exact client pointer, nonzero captured generation and
utility thread ID. No default client behavior or context-free call changes.

In `requestWithAdmission`, retain the existing ObserverOnly allowlist and insert
this scope check immediately before Ensure. A present scope must have the correct
type, owning client, nonzero generation, `admit == nil`, one of `thread/read`,
`thread/turns/list`, `thread/items/list`, `thread/queue/list`, and the exact
`threadId` parameter. Otherwise refuse; never fall through to Ensure. Valid
scoped reads call `requestConnectedAdmission` with that generation and nil
admission. No generic mutating-method allowance is added. The new entry requires
ObserverOnly mode and **no separate HistoryReader**, so every reused history/
queue helper follows this same client path. Capture/validate the ready generation
before deriving the scope; zero, mismatch or a disconnected client refuses.
All preflight and reconciliation reads retain that scope. A bounded post-error
reconciliation context may remove cancellation and add its existing two-second
deadline, but must preserve the same scope (for example WithTimeout over
WithoutCancel); a new Background context must not lose it. No failed read can
replace the captured generation. Final steering continues to call the existing
generation-bound admission helper directly with its real ledger claim callback.

**Restore without the generic wrong-turn acceptance path.** Do not call
`restoreUnwrittenSendOutcome` or `unwrittenSendOutcome` from this entry: both can
reach generic `reconcileSend`, which may mark history accepted before checking the
expected turn (`send_delivery.go:17–43`). For a claimed write proved unwritten or
an existing typed explicit refusal, reuse `restoreRejectedSendClaim` with its
actual nonempty claim; retain its SQLite claim-identity guard. Then reread the
exact atomic queue/attempt state with `sendStateWithOptions`. Return known-unsent
only for the same prepared (or genuinely never-prepared absent) identity with no
queue; preserve the existing typed error/retryability distinction, without any
automatic retry. Any concurrent accepted/submitting state takes the entry's
exact-turn reconciliation path. That path uses existing history readers, validates
turn/client ID before `finishAcceptedSend`, and retains unknown on mismatch or
missing evidence. Restoration failure cannot be discarded as proof of no send.
Original options/context/expected-turn identity stays immutable throughout.

**Listener-free offline proof boundary.** Existing acceptance fixtures use a
Unix WebSocket listener, outside this preparation scope. A test-only Go overlay
may replace solely `requestConnectedAdmission` at the wire boundary with an
in-memory recorder. Run the actual new entry, new scoped Request branch and real
SQLite preparation/claim/acceptance/restoration against it. The fake must invoke
the supplied admission callback in the simulated write order and record method,
generation and exact turn parameters. Preserve production source separately;
compile that derivative without the overlay and record exact source/overlay/test
hashes. No runtime injection option, listener, native process or production
transport change is added. Cases prove entry decisions, scoped-read forwarding,
real ledger transitions, concurrent claim behavior and refusal/unknown recovery;
they do **not** prove real socket I/O or native acceptance. Source comparison
must separately show the actual generation-checking writer and incoming no-answer
paths unchanged. Existing review must retain that evidence limit. This is the
minimum offline preparation boundary, not a live-check waiver or peer execution
release; root retains release/acceptance and the peer retains adoption/action.

### A42/S3 applicability — no unspecified external lock prerequisite

The private steer does **not** require the caller to hold an unexposed session
admission lock or runtime package-transition lock across its SDK call. Earlier
“ordinary owner admission”/“real admission fence” wording must not be interpreted
as such a prerequisite. A40's `ContinueFailedTurn` has a different condition:
dd90 `continuation.go:8–14,67–70` requires shared application exclusion because
native has no compare-and-start. A42 performs no start/resume; native
`turn_input.rs:843–928` checks the exact current regular turn while holding its
active-turn lock. Importing A40's stronger exclusion requirement here was an
inference, not a demonstrated steering requirement.

The actual caller checks are executable now: verify its own `dev-session current`
and trusted session/environment binding; obtain its exact-lead
`monitor_operation {action:"status",id:EXACT_OPERATION}` proof and match the saved
root/incarnation/utility/project/cwd plus the owner's explicit local-drain
authorization. Pin the registered native identity/socket epoch and fixed target;
then use S3's already specified loaded/exact-active-turn and same-connection
preflight. Status establishes the current ownership evidence; it is not a lock
or a permission manufactured by passing IDs. This is the existing trusted-local
operator boundary, not a new multi-tenant authentication API.

The enforced send admission is S3's closed exact-target scoped-read path,
ObserverOnly incoming no-answer behavior, local queue-update lock, existing
SQLite exact-identity submission claim, and the SDK's connection/generation
checks at admission and writer acquisition (`client.go:1151–1197,1282–1336`).
Native then applies direct-input/provider checks and expectedTurnId atomically.
The scoped ObserverOnly path is intentionally sufficient for this application
send; no second owner-external guard command or new lock is required. SDK
connection generation is not a workspace package-generation lock, and fresh
package/native metadata must not be described as holding one.

If the turn ends or changes before admission, steer refuses rather than starting
another. A restart/disconnect retains the uncertain ledger outcome and cannot
redirect the write onto a new connection. If accepted input is never consumed,
its receipt remains acceptance only and all effects stay accounted separately.
An ordinary archive still faces unresolved-monitor and active-native/receipt
checks (D `monitoroperation/lifecycle.go:135–183`); this artifact changes none of
them. A concurrently authorized native/lifecycle interruption is handled as a
refusal or uncertain/result-not-consumed case, not a reason to cold-load or retry.
No lifecycle/transition permission is inferred. Thus no missing executable
runtime exclusion blocks S3 preparation or its later owner adoption on this
point; actual artifact review and explicit peer execution remain separate.

Only this consequential design clarification is changed here. Architect performs
no live action; rollout remains in implementer2's appendix window.

## A43 — use the retained root's existing MCP status tool for cutover proof

**Sufficient substitution; no new artifact.** After the ordinary accepted final
profile/policy2 maintenance, restoration, generation and current-root checks,
the actual retained lead `01a1cbe7-f37c-7173-9e5c-e28ff5b96e9f` can invoke its
already-exposed native tool once:

```javascript
await tools.mcp__team_reporting__monitor_operation({
  action: "status",
  id: "63e94315-36d3-4455-87d0-69f78f1e71ef"
})
```

The field is **id**, not operationId. D/734 `monitor.go:65–82` decodes status
strictly as action/id; operationId belongs to resolve and would make this status
request invalid. Supply no caller/thread/_meta argument and do not invoke from
architect or another member. Availability of a similarly named tool elsewhere
is not proof of this retained root route.

**Actual decoder path.** Native invokes the registered `team_reporting` server's
tools/call handler (`team_mcp.go:250–299`). `monitor_mcp.go:38–72` extracts native
`_meta.threadId`, resolves the actual owner, and uses its stable-profile dev-session
invocation with bound workspace/root and expected monitor caller. Caller extraction
is `team_mcp.go:367–399`; exact lead/recovery ownership is `monitor.go:412–462`.
Registration pins the helper executable in `agentteams/registration.go:78–91`;
the host wrapper supplies current generation/socket authority
(`team_mcp.go:146–174`). This is the real retained helper, not the HTTP frontend
or a standalone helper invocation. The new CLI's NativeStatus contains
`executionOwner:"native"` (`observer_service.go:15–26`); the retained helper must
decode that response before returning it. Old D `monitor_mcp.go:75–86` decodes
bare Operation with `DisallowUnknownFields` (`team_mcp.go:192–204`) and cannot
return this successful ACK. 734's native branch accepts it at
`monitor_mcp.go:92–97`. Thus the direct tool exercises the same decisive decoder
boundary A20 intended, without M1's ordinary-client incoming-reply risk.

**Interpretation.** Retain the raw CallToolResult. Require `isError:false` and its
single text content item; parse that text as JSON, not the whole MCP envelope.
Require schema1, exact operation ID/workspace, owner slug/root matching this
session and `executionOwner:"native"`. Match the existing source/report/resolution
to the retained record; historical operation fields are not rewritten to the new
native epoch. Any error text, malformed/wrong ACK or missing original receipt
leaves the cutover proof incomplete. `teamMCPToolResult` explicitly returns the
isError/content wrapper (`team_mcp.go:207–209`). Tool availability alone is not
success, and a direct CLI status would bypass the decoder under test.

The call occurs within the already-restored exact root's current native turn;
its native tool metadata plus the ACK owner checks establish caller identity.
The retained operation already has a launch receipt, so reconcileLaunch returns
without loading/submitting (`launch.go:174–182`). This status path starts no root
turn, utility or observer. Preserve the existing restoration/current-root evidence
and ordinary tool receipt; no additional before/after SDK client is needed to
demonstrate a new turn was not requested. Do not infer global inactivity or that
no unrelated concurrent event occurred. This supersedes M1 invocation and optional
custom inventory reads, not the ordinary transition/generation guards. Keep all
M1 artifacts and compile receipts unexecuted with their historical limitations.
Architect invoked no status/native call; root alone performs the post-cutover
read. No production/review/pin change or additional implementation is needed.

## A44 — executor-log file applicability correction; no read package

**Accepted source-only stopping result.** A41 correctly identifies conditional
executor telemetry, but its managed-file retention path is not established for
this workspace launch. Native360319d8 `cli/src/main.rs:612–614` defines the hidden
`--managed-daemon` boolean; `:1294–1300` calls `maintain_stderr_log` only when that
flag is true and the transport is UnixSocket. Calling the registered workspace
service “managed” does not establish this native launch mode. D b8329e32
`libexec/workspace-host:1772–1787` execs global plan/provider/storage arguments
followed by `app-server --listen unix://<registered socket>`, without that flag.
The specifically inspected own records preserve native PID1309145/start75094898,
exe2rq and unchanged argv/socket identity; they do not supply affirmative
native managed-daemon mode or the original native `pid_file` identity. No wider
record search or new observation is authorized or needed for this stopping result.

The source formula is conditional, not a discovered path: a proved native
`P.pid` gives current `P.stderr.log`, and its retained tail is
`P.stderr.log.previous` (`app-server-daemon/src/lib.rs:302–313` and
`backend/stderr_log.rs:197–222`). Never read the temporary file. The choice between
`daemon.pid` and legacy `app-server.pid` depends on native package-root/artifact
state (`lib.rs:351–368`, `managed_install.rs:20–55`); do not guess either basename,
probe both, or treat an unrelated existing file as this daemon's log.

This supersedes the A41 inference that these two managed files constitute an
established retained-reader route for the actual registered process. Event
definitions and their correlation/exit-code limits remain true; actual emission,
retention and file applicability remain unproved. No parser, read/projection
artifact, shared-log access or alternative journal/storage investigation is
released. Root has held the proposed read and informed the user that no files
will be read on these facts. The historical startup-configuration operator fact
remains pending; the separate804 owner's stop decision is independent. Original
inventory and INCOMPLETE/unknown outcome remain immutable. Only this design note
changed; architect stops with capacity available.

## A45 — authorized local termination versus enforced package admission

**Sufficient bounded source result.** The user now authorizes ending the remaining
a8/99295 and8045 **local observations**. This does not authorize remote-CI
cancellation, session lifecycle changes, a shared-native kill, false terminal
reports or rewriting original monitor records. No action was performed here.

The cutover block is enforced by selected D, not an extra design precaution.
D `libexec/workspace-host:2389–2419` requires source, target and actual launch
packages to satisfy its live policy1 comparison. Frozen734 advertises policy2;
an identical native executable does not admit the live path. Ordinary switch
therefore enters `workspace-maintenance.rb:251–256,347–378`, whose source-owned
prepare precedes worker launch/activation. `maintenance_control.go:722–765`
inventories all rooted, nonarchived sessions on the registered native socket.
`maintenance_monitor.go:18–50` checks ownership/inventory and full
`RequireIdle(...,false)`; `monitoroperation/lifecycle.go:142` rejects unresolved
effects before its native proof. No remote-CI request occurs in this predicate.

Public switch options (`workspace-host:652–660`) expose source/from-candidate,
maintenance enablement and pause timeout, not a force/skip-monitor exception.
Candidate entry retains these checks. A longer timeout, omission of
`--enable-maintenance`, or administrative intent cannot bypass the policy
mismatch. Relabeling734, changing a profile link directly or using a different
package as protocol owner would not be the supported compatible live path.
There is no supported final734-selection command established that retains these
unresolved records without satisfying D's existing guard.

**Literal-stop audit boundary (S4).** `docs/dev-sessions.md:274` and
`monitoroperation/service.go:476–513` make monitor Cancel continuation intent
only; it sends no utility/cell signal. Public monitor CLI accepts
start/report/status/cancel/resolve (`libexec/dev-session:10465`). Resolve records
evidence, not termination. Generic dd90 `Client.Interrupt:5949` uses
Request/Ensure and lacks this operation/utility/generation binding; the installed
browser interrupt route admits roots or ready roster members, not monitor
utilities. It is not an administrative utility-drain route. S4 found no complete
existing exposed per-monitor stop/drain command. Do not fabricate one.

**Concrete next-action boundary.** For8045, its owning lead can first supply the
exact public monitor launch thread/receipt and current active-turn identity,
plus the already-owned executor/cell handle. If still active, the existing A42
SDK entry can send an exact-turn request for that utility to end its own local
observation and account its tool results; its previous fixed638b/cell7 caller
must not be applied unchanged to8045. This is cooperative steering, not enforced
termination, and needs a separately scoped owner invocation. For a8, the accepted
notLoaded result excludes that route. Existing metadata has no OS PID for99295
(an executor-scoped handle), so there is no honest `kill 99295` or native resume
command to offer. An administrator may terminate a positively identified local
process under the new authority, but exact current process/owner provenance and
an observed stop/join are still needed; no such process is established by this
source check. Its absent original manager supplies neither a kill target nor
completion evidence.

Root therefore has a concrete cooperative route conditional on8045's active
owner binding, and a precise missing administrative execution target/receipt for
a8. Neither calls for more historical startup/configuration/log searches. Any
additional administrative drain capability or scoped process-identification
action requires root's explicit release; it is not silently supplied by this
brief. Original INCOMPLETE/unknown outcome stays immutable. Supported evidence
resolution may follow actual local-effect reconciliation; no false resolution,
profile retry or new implementation package is released here. Sources/pins and
rollout remain unchanged. Investigation stops with capacity available.

## A46 — fixed56e configuration baseline; one preserved runtime734 pin

**Sufficient configuration preparation brief; root releases implementation.**
Freeze the already observed `56e6bb4ccddfa32ed1d4d701962d0d4aa80be100`.
Its objects were present in the canonical configuration repository: no fetch,
default re-observation or feature/ref/worktree mutation was needed. Approved
`08d68a85f24a95b70b2d806f995f04b236e4d89a` is its ancestor. Exactly three commits
change only `flake.lock`: `0ede318f` updates nixpkgsProduction/Stable/Staging,
`60008ccd` updates vpsadminosOsStaging/Staging, and `56e6bb4c` updates llm-agents.
All64 nodes and every input edge/original/follows remain; only six locked objects
change. Preserve these integrated updates, not the old08d siblings.

Aitherdev's unchanged `module.nix:7–12` selects nixos-stable, home-manager,
llm-agents and dev-workspace. Its system nixpkgsStable advances ac588ef to
`f1e5c356f35d07e7b71a6b5e6c9338e0b029e0c0`; root llm-agents_2 advances860075d9 to
`ee05b5abb7c7f4af84a5ad5420f8a6e662774f2b`. Thus system packages, the stock Codex
wrapper input (`config.nix:14–21`) and declared development-shell packages are
affected. The new stock native version/output is unmeasured; do not infer one.
The two vpsAdminOS staging nodes advance to068200a4 but are not aitherdev channels.
Host tree remains `0a8a09cec1e27be4182ed1fc3f2ed0eebbd19710`; modules, AGENTS,
flake.nix/channel mapping, Gemfile.lock and confctlff5e source are unchanged.
Confctl's interface is unchanged, but its nixpkgs-backed tools must be exercised
in the declared new-base environment rather than assumed identical.

The independent devWorkspace input remains eabb before our pin. Its complete
eight dependencies are byte-identical to08d and resolve to the same locked
identities as workspace `f538a05db64f9cb9e6dcbeec42bf8a82af0bb0e7`: codex-webdd90,
runtime llm-agents91ff, both runtime nixpkgs nodes, bun2nix, flake-parts, systems
and treefmt-nix. This is not the changed root llm-agents input. Managed runtime734,
its native/package contract, workspace caller policy9be and extension selection
need no refresh, rebase or new runtime CI due to this configuration movement.

Deployed config `a67a69097346731880c7eed80c1b55f429c912d3` is exactly one generated
devWorkspace-only3+/3- pin above08d, selecting
`734a85fea42c8f8276e6b037196c24cf8903cd12` /
`sha256-3ZBvjhPjr8wBF/58ObIVcYJwceqpe0S9+V+uq9zIKxw=`. Prepare ONE equivalent
final pin above fixed56e using the existing declared-environment command
`confctl inputs channel set --commit dev-workspace devWorkspace 734a85fea42c8f8276e6b037196c24cf8903cd12`.
Preserve all63 new-base siblings, follows and the eight runtime dependencies;
retain deployeda67/D refs and original receipts. The56e lock SHA256 is
`3e119fc9a74fe3d957cc803a8b08d653a701517bdf027bb1a2ef5f298f62917e`.

Minimum preparation evidence: normal generator/hooks; one-pin history and exact
old08d..a67/new56e..final comparison; complete semantic sibling/runtime graph
proof; existing paired deployment checker; and the existing single-aitherdev
`nix eval --json --no-write-lock-file --option allow-import-from-derivation false
.#confctl --apply <retained assertions>` in the declared environment. Assert
NixOS,172.16.106.40,the four channels and exact734; force only that system's
toplevel.drvPath. Stop on generator/tool or interface failure, not an unrelated
host audit. Independent certified pin/range/graph equivalence can establish the
deployed **feature lineage** once the actual final head exists; this assessment
is not its certificate and a nonancestor a67 must not be called literally merged.
It cannot establish whole-system derivation/output equality across the changed
host inputs. Any deployment of the refreshed system requires its exact final
derivation/build/copy and existing host/stock-provider health evidence; olda67
receipts remain evidence only for a67. Integration-lineage assessment must keep
that distinction and does not itself order another deployment or Codex upgrade.
No new local migration or product choice is introduced by the pin. H7 runtime/
workspace preparation is independent. Later default drift belongs to root's
integration freshness check; do not chase another baseline here. No evaluation,
check, build, live query, source pin or claim was performed. A46 stops with
capacity available; rollout was not edited.

## A47 — native public environment metadata exists, but not the missing snapshot

Pinned360319d8 exposes experimental `environment/status` with `{environmentId: EXACT_ID}` and response `{status: ready|pending|disconnected|unknown,error?:string}` (`protocol/common.rs:1257–1263`, `v2/environment.rs:97–140`). Dispatch uses the same EnvironmentManager as the thread manager (`message_processor.rs:591–592,1248–1249`; `request_processors/environment_processor.rs:79–99`). Its contract does not start/recover environments; an already-ready remote is queried over its existing connection. Ready conflates local and connected remote and this method does not enumerate IDs/default/provider. `environment/info` calls `force_info` and returns shell/cwd, so is not a passive substitute. Public `thread/read {threadId: EXACT,includeTurns:false}` can expose current **loaded** `thread.environments`, primary first, with `{environmentId,cwd,runtimeWorkspaceRoots}` (`v2/thread_data.rs:207–212`, `v2/environment.rs:10–31`). Its callee uses `get_thread(...).ok()` and stored metadata, not resume/start (`thread_processor.rs:3047–3114`); unloaded constructors return null (`:6605–6608`, `thread_summary.rs:261–264`), while loaded metadata maps current config selections (`:6798–6803`). These existing experimental-native fields require ordinary connection/capability admission and supply no new owner authority. No public environment dispatch reads the complete current startup-manager provider/default-ID snapshot, and current loaded selection is not original-command history. Thus a8's accepted notLoaded state leaves the precise original99295 domain gap; neither a local-status query nor another thread's selection settles it. No API/client/action was released or executed, no further factual search is proposed, and build/integration work remains independent. A47 source check stops; capacity available.

## A48 — selected D honors resolution; aggregate failure loses the cause

Selected profile resolves22x45q9snm46qw95c1zjsbavifv9fki9. Its previously certified
actual source `/nix/store/882d9278smpacf3czxzc0wliggx03a9f-source` was read directly:
service.go, lifecycle.go and maintenance_monitor.go equal canonical b832 bytes.
`HasUnresolvedEffects` is byte-identical in D and734: a nonnil Resolution returns
false before terminal incomplete/stillRunning classification. Thus a8's reported
22f4 resolution, if present on the same record read by D, cannot fail that
predicate. Resolution does not bypass known receipts, exact identity or
ProveQuiescent. No state/native read was duplicated; E6's210-record static pass
does not establish those remaining proofs or identify the actual failed gate.

The5s timeout is **per session helper call**, not one deadline for all210 native
operations (`maintenance_monitor.go:18`; `maintenance_control.go:751–764`). It
covers Inventory, another List, IdentityFor/SameOwner and that session's full
RequireIdle. Each List reads/validates the central directory before filtering,
checking context per entry (`store.go:261–295`), so global metadata is reread;
native proof covers the matching session's retained operations. Deadline expiry
can produce the aggregate category because every helper error is replaced with
`monitor-operation-unresolved`. Record count alone cannot prove expiry. The
underlying error/ID is not retained: inventory returns before Store.Create
(`maintenance_control.go:444–447`), and `:763–764` discards the helper error.

Existing exact-owner status returns Operation metadata and possible launch
reconciliation (`service.go:428–473`), not a quiescence result. The smallest public
diagnostic remains `dev-session archive-check <OWN_EXACT_SLUG> --as-is --json`:
its conversation stage calls RequireIdle and reports
`monitor <ID> is not quiescent: <reason>` on ProveQuiescent failure. All readiness
stages execute even after an earlier failure (`workspace-archive-check.rb:23–30`);
inspect the conversation result, not overall ready alone. This read publishes no
archive intent. It uses30s and lacks maintenance's extra identity/inventory gates
(`monitor.go:226–233`), so success cannot exclude D's5s expiry or another session's
failure. Known-receipt/store errors can also lack an ID. Internal monitor-lifecycle
flags are not a public administrative bypass. No existing public global route
returns the discarded prepare cause or exact ID; another owner's native check
requires its own authority/root decision. No repeated switch, census, native
query, diagnostic client or code change was performed. Source investigation
stops at this exact exposure gap; capacity available.

## A49 — prepare remains source-owned; smallest diagnostic correction

The selected D operations/update guidance was read. Public
`workspace-host maintenance` exposes status, startup-status, cancel, recover and
recover-startup, not an inventory diagnostic (`workspace-maintenance.rb:48–71`).
`docs/workspace-updates.md` explicitly says a pre-Create refusal saves no
operation/startup receipt and deliberately omits identities/raw errors from its
reason. Status/recover cannot recover the missing explanation for1620bc16.
No new owner requests, checks or repeated switch are proposed.

**p71 is not a prepare override.** `--from-candidate` initially calls the candidate
Ruby/portal executable, but `prepare_profile` records the actually selected
`preselection_session_package` as SourcePackage (`workspace-host:710,2562–2565`).
`maintenanceProtocolOwner` uses that request identity and execs the saved source
helper **before** decoding/handling prepare (`maintenance_control.go:72–89,109–145`).
Thus p71's public switch still invokes D's admission. The documented candidate
recover-startup exception requires an existing startup selection and no full
operation directory; it neither creates a new prepare owner nor applies to this
pre-Create refusal. Private helper invocation, a fabricated SourcePackage or
profile-link replacement is not a sanctioned route.

**Minimum capability correction, requiring root release:** preserve an
allowlisted typed stage/reason from the existing monitor check through the
existing prepare Response.reason, instead of replacing every error with the
aggregate category. Distinguish deadline/cancellation, store/inventory, owner
identity, known receipts and native-quiescence failure at their actual call
boundaries. Never output raw SDK error, prompt, path or transcript. The minimum
diagnostic can retain the current no-ID policy; an exact monitor UUID would
localize a per-record failure but changes that documented response policy and
needs root's explicit bounded metadata-output decision. This is propagation in
the existing `maintenance_monitor.go` / `maintenance_control.go` path (with a
small typed lifecycle error only if needed to preserve its gate), focused
classification/unchanged-refusal tests and update-guide explanation. It changes
no predicate, timeout, state/schema, native/MCP invocation, journal or authority.

A complete policy1/reporting3 D diagnostic successor can use the already proven
ordinary compatible live-selection path, preserving consumed D and actual
native/registration proofs. Once genuinely selected, that source owns the next
ordinary final734 preparation. This requires normal preparation/review/package
selection approval; it is not released or executed here. No new reader, probe
command, generic diagnostic service or compatibility bypass is necessary.
Do not infer that a longer timeout is the repair before the actual reason exists.

**Inherited session environment hypothesis:** the per-session check is an
in-process Go function, not a dev-session subprocess. It receives explicit
summary workspace/slug/socket. `IdentityFor:25–44` calls
`session.Find:363–386`, `PendingLifecycle:117…` and
`ObservationIdentity:24–45`, all using those explicit identities; this seam does
not read DEV_SESSION_SLUG/WORKSPACE. `newTransitionClient` receives explicit
workspace/state-root/socket (`main.go:53…`). The root's inherited slug therefore
does not establish the proposed foreign-session rejection. Owner conversation
passes still do not identify the discarded maintenance cause. No native/state/
log/API query or code change was performed. A49 stops with capacity available;
root owns any corrective implementation release and subsequent execution.

## A50 — released source-D diagnostic successor

**Settled implementation brief.** Root accepts the user's deployment/resolution
direction as authority for this necessary diagnostic correction and explicitly
chooses sanitized **monitor UUID and recorded owner slug**, where known. Owner:
implementer2, sole source/test/doc/index/commit ownership in a fresh owned runtime
worktree based exactly on consumed D
`b8329e32f1132fd947f4a9c803bf44e3ed9ce481`. Produce one logical diagnostic commit
above D; do not rewrite/reuse D or modify frozen734, workspace32 or config86.
Root controls any overlapping Git windows and later publication/selection.

**Files and contract.** Limit edits to
`portal/cmd/workspace-portal/maintenance_monitor.go`,
`maintenance_control.go`, their focused tests,
`portal/internal/monitoroperation/lifecycle.go` plus a minimal typed-error
definition/test if necessary, and `docs/workspace-updates.md`. Reuse the existing
prepare response's `reason` string; no new endpoint, request/response schema,
reader, ledger, service or diagnostic store. At actual failing boundaries retain
typed fixed stage/category and the exact known record identity. Stages distinguish
inventory/store, owner identity/match, receipt proof and native project/thread/
bootstrap/archive-state/idle proof. Categories distinguish deadline, cancellation,
invalid/uncertain state, identity mismatch and unavailable proof; use a small
fixed enum derived from those existing branches, never raw error text.

Keep the existing aggregate category ordering/prefix. When that same aggregate
refusal is returned, append one bounded diagnostic for its first observed monitor
failure, e.g. `;monitor-stage=...;monitor-category=...;monitor-id=...;owner-slug=...`.
Do not return early, reorder work or mask a higher-priority existing refusal.
Use `unknown` when identity is unavailable. Emit only a canonical valid monitor
UUID and the existing validated, bounded ASCII owner slug; malformed/unexpected
values must not pass through. Bound the entire reason to1024bytes without
truncating identifiers into different identities. No raw native/error message,
argv, report, path, credential or transcript may reach this projection. A tiny
typed error can carry these fields across packages and preserve its underlying
cause with Unwrap so `errors.Is` still identifies deadline/cancellation. Preserve
existing Error text/behavior for non-diagnostic callers wherever applicable.
Diagnostically exposing an identity grants no authority over its record.

All admission predicates, timeout values/scope, iteration/decision ordering,
native calls, state writes and protocol ownership remain unchanged. Policy1,
reporting3, native binary/argv, schemas, capabilities and MCP inputs/decoder remain
byte-identical to D. No diagnosis is assumed: in particular, do not widen5s,
resolve an operation or classify inherited DEV_SESSION variables as causal.
Documentation must explicitly narrow the former no-ID rule: the existing
source-owned operator prepare refusal may expose the sanitized runtime UUID/
recorded owner slug and fixed gate/category; it still excludes private content.

**Acceptance and evidence.** Focused existing prepare/inventory tests plus new
cases must prove unchanged refusals/success/ordering, valid and unknown identity
projection, malformed/control-character/oversized identity exclusion, raw-error
redaction and preserved deadline/cancellation classification. Verify the Ruby
consumer can print the existing schema1 refused response with the extended
reason. Run only relevant declared-environment quick checks/hooks; stop/report
behavior or scope conflicts, not expand to a broad suite. Record exact base/head,
diffstat, commands/results, unchanged contracts/native/inputs and no-migration
conclusion, then independent affected review before longer acceptance/selection.

**Delivery and lineage.** Root may prepare a normal composed policy1 diagnostic
profile and select it through the existing compatible live-switch workflow after
required artifact/review/claim proofs; no private helper or link edit. Only the
actually selected successor then owns a later ordinary final734 preparation.
Retain consumed D and the diagnostic checkpoint as a separate source-owned
consumed stream. **Implementer2 owns BOTH committed source ranges for ONE final
review packet before long builds:** exact b832→D-diagnostic and exact
`734a85fea42c8f8276e6b037196c24cf8903cd12`→final-diagnostic. Keep both original
heads untouched. The final successor must contain the same substantive diagnostic
correction; it is not optional or removable as a supposedly temporary feature.
Map the same typed gate/category and sanitized identity projection onto the
final helper's existing observer-aware `AssessLocalSafety` path without replacing
it with D's RequireIdle path or changing observer admission. The final-only
`portal/internal/monitoroperation/observer_lifecycle.go` is within owner2's scope
solely for carrying this diagnostic through that existing call seam. Its existing
LocalSafety declaration in `observer_types.go` may gain only the transient
`Diagnostic *DiagnosticError` field tagged `json:"-"`, needed because blocked
results otherwise return nil error and discard the typed proof. Preserve all existing State/Reason/
OperationIDs wire values and semantics. No new persisted or public API field.
Stop/report any behavioral conflict instead of adapting a guard.

The packet binds both exact ranges, same-correction mapping and unavoidable
call-seam differences, quick results, unchanged D policy1/reporting3 versus final
policy2, unchanged native/inputs/schemas, and whole-history/no-migration
conclusions. The source-owned D diagnostic must have integrated final lineage;
do not claim a nonancestor checkpoint literally merged or certify its removal
as equivalent. Root controls publication, selections and approved merges; owner0
alone prepares the matching generated pairs after frozen/review-ready source
release. Each changed final head needs its corresponding exact pin/artifact/
verification evidence. Never rewrite master, claim old734 includes the correction
or relabel old artifacts. The existing refusal remains safe on interruption and
no pre-Create operation is invented. This brief releases source work only; no
live selection, pins, claims or lifecycle action by architect or implementer2.
Architect stops; routine exact clarification remains available.

Projection clarification: a pre-record store/IdentityFor failure has no known
recorded owner. Emit `monitor-id=unknown;owner-slug=unknown`; do not select an
arbitrary record or substitute the inspected summary slug for a recorded owner.
Only the actual failing record supplies those identity fields. Canonical
lowercase dashed36 UUIDs are admitted; other fixture/store-ID representations
remain unknown rather than being transformed into an apparent exact identity.

### A50 execution note — the requesting root is a maintenance participant

The unchanged ordinary maintenance path has no requester exemption: a loaded
retained root with an inProgress turn is captured with sourceTurn and stable
noticeId/continuationId (`maintenance_control.go:744–850`). Root launches the
authorized mutation, retains its accepted UUID/source/candidate/claim and own
checkpoint, then honors the pause notice. Prepare/Create precedes the independent
`workspace-maintenance@UUID.service`; the original CLI subsequently follows status
(`workspace-maintenance.rb:347–408`). Native shutdown may lose its exec handle.
Keep caller exit unknown unless independently received; worker completion is not
a fabricated caller exit receipt.

After restoration, use `workspace-host maintenance status UUID` for that exact
operation; status without UUID can identify an active operation if its identity
was genuinely lost. Verify source/candidate, phase complete/outcome updated,
continuationsSettled and restoration.completed. The own participant retains the
exact root/sourceTurn/continuationId and accepted disposition; explicit Stop
suppression is not resumed execution. No continuationTurnId exists in this public
operation DTO: the existing sender reconciles its stable ID, and the actual
restored root turn is separate runtime evidence. `startup-status UUID` applies
to a matching startup selection; pending/none or another UUID cannot replace full
operation completion. Required recovery uses `workspace-host maintenance recover
UUID` with the SAME source-owned operation, not a fresh switch or private helper.

A new registered active watcher can itself fail monitor admission; a native
child is paused/interrupted with its owner and cannot observe across source
shutdown, while an unowned loaded writer can refuse admission. Accepted
maintenance holds new work. Do not add a watcher to this cutover. The durable
source-owned worker and visible direct-lead bounded follow provide the ordinary
mutation-wait contract; the monitor skill permits parent fallback when required
delegation/transferable observation is unavailable. This does not convert a lost
tool handle into completion or waive effects reconciliation. The compatible D52
live selection and later full policy2 cutover keep their distinct receipts.
No session Stop/archive/delete/cleanup, new client or live action is authorized
by this note. Root alone executes and reconciles; architect stops.

**Shortest staged route confirmed:** after the ordinary D52-owned full cutover
to the already verified p71/runtime734 completes, ee's diagnostic-only policy2
successor can use ordinary compatible live selection. The predicate is not
hardcoded1:734 `workspace-host:2417` compares each package against the executing
runtime's policy value2. Predecessor, target and actual launch-marker package must
all satisfy2, with identical resolved native and validated registration semantics
(`:2389–2398`, path-only helper normalization`:2136–2148`). Then
`maintenance_switch_required?:251–256` returns false and does not run the global
maintenance monitor census. Ordinary generation/lifecycle/provider/claim and
activation guards remain. Root's sequence is D52 compatible selection, exactp71
full maintenance and retained-root/helper/health proof, then separately verified
ee compatible selection and final diagnostic lineage/integration before release.
Owner0's clean historical32 evaluation must reproduce exact existingp71 or stop;
no old artifact relabeling or automatic rebuild. This route does not make p71 the
final diagnostic deliverable, claim D52 literally merged, or waive ee's exact
final artifacts/deployment/lineage. No action was executed by architect.

### A51 — exact native-project refusal is a passive-client allowlist defect

Root's D52 attempt `cb506412-248e-4e14-868b-2ac915e88f90` refused before
Create at `native-project/unavailable-proof` for own monitor
`092de5fd-a83d-4a60-948a-008d54f96fc0`. Its supplied public status retains an
exact launch receipt and terminal PASSED report; no resolution is needed to
replace that outcome. No additional cell accounting or native lookup was run.

The unchanged source seam proves the immediate cause: maintenance constructs
`newTransitionClient` (`maintenance_control.go:740`; `main.go:52–79`), setting
ObserverOnly. `Lifecycle.State` first calls ReadProject (`lifecycle.go:35`),
before thread metadata or bootstrap/quiescence proof. Pinned codex-web
`dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`, `codex/client.go:497–504`, sends
`project/read` through Request. Its ObserverOnly allowlist at `:1130–1136`
omits that method and rejects it locally **before Ensure or native transmission**.
The runtime embeds that SDK client and has no ReadProject override.

Ordinary archive-check uses `newCodexClient`, with ObserverOnly false
(`monitor.go:221–236`). Both paths call RequireIdle with executionOnly=false,
then the same State proof; the failure precedes any archived-thread choice.
ReadProject has only projectId, no includeArchived flag. Thus prior conversation
PASS and maintenance refusal are compatible; this evidence does not establish
a missing, archived or mismatched native project.

No supported retry, resolve, project mutation or private helper repairs this
client restriction. The minimum correction is to admit the existing read-only
project/read operation in the passive SDK contract, retaining ObserverOnly's
incoming no-answer behavior and all identity/quiescence checks. Lead must settle
the normal reviewed source/dependency counterpart and compatible source selection
before another full attempt; this finding releases no code or live action.
Passing that gate does not certify later gates. Existing reports, refused UUID,
consumed D/D52 and final source/artifact evidence remain unchanged. Source-only
investigation is sufficient and stopped; architect capacity available.

**SDK1 release — lead accepted A51.** Implementer2 owns the normal codex-web
provider correction in `codex/client.go` plus focused existing/new SDK tests,
and its ordinary dependency counterparts in the D52 and final-ee runtime
streams. The only added passive method is `project/read`; leave ObserverOnly,
incoming no-answer behavior, native project identity validation, timeouts,
schemas, policies and all mutation refusals unchanged. No vendoring, private
cache patch or new client/endpoint. Read each repository's instructions first.

Owner2 observes canonical codex-web/master once and records its exact base. If
that source has materially advanced or already fixes this omission, report the
input fact before adopting unrelated changes. Use the normal SDK feature branch
and declared dependency update path. Consumer scope is only existing SDK pin
manifests/locks and required generated dependency hashes, plus a focused real
transition-client regression if needed; no native/input upgrades or catalog/
protocol project. Preserve consumed D52/e9 and earlier D references exactly.
Unconsumed, unmerged final-ee/f53/d038 work may consolidate its new dependency
pin stream without rewriting master or relabeling old artifacts.

Acceptance: a real ObserverOnly ReadProject reaches the existing read request
with exact projectId and retains response-identity validation; project mutations
and thread mutations remain refused, and incoming native requests still receive
no answer. Exercise the actual passive-client path that mocks previously missed.
First compile the changed SDK and both real consumers; run their narrowly
affected SDK/passive-client and maintenance proof checks in declared environments,
then commit all intended changes for ONE affected final review covering the SDK
and both consumer ranges. Preserve normal exact-head package/CI/native acceptance
requirements; unchanged earlier evidence is historical, not new artifact proof.
Root selects the smallest affected packaged acceptance after review; no extra
conformance matrix. The correction has no persisted-state migration and does not
prove subsequent maintenance gates. Recovery remains ordinary source-owned
compatible selection followed by the normal full operation; an unchanged source
will continue refusing safely. No live action is released to owner2 here.

Root owns publication/selection and final integration decisions. Existing three
repository merge approvals do not include codex-web/master: seek that explicit
approval only when the concrete reviewed SDK fix is ready. Feature preparation
and authorized deployment preparation continue. No new investigation or packet
is required for this settled boundary; report the first compiling milestone and
exact source/pin evidence, then proceed under root's existing delivery ownership.

### A52 — adopt the published bounded maintenance recovery repair

Sufficient REC1 brief; implementer2 owns source adoption, focused checks, normal
hooks/commits and equivalence evidence. Root owns accepted live recovery, package
selection, pins and integration. No architect/implementer live action is released.
Identity/roster and applicable procedures were reread. Only canonical Git objects
and deliberately supplied peer evidence were inspected, not peer records/state.

Freeze the fetched repair branch `2026-11-14-maintenance-pause-recovery` at
`147bbdbd0de193d26c9342fb80c54e97d45cc812`. Its exact ancestry is D base
`e32d0bd497dbd69fd3a8cd07bfb477d7cb44d3f3` →
`5b02b56c70ed4ab6fbdfc3b0d0292b6d6ef6a62d` →
`0bc9dfc4d6670f1610ef3ea4eff2a8b089958b41` →147. Prefer fast-forwarding
our D feature to those exact existing commits, retaining consumed e32 and all
earlier refs. Do not recreate equivalent D commits unnecessarily. Transplant the
same complete repair onto final `3492365c3a3e12b18418919964844089d560dc1b`,
retaining that checkpoint. One logical final adoption commit may consolidate the
three imported deltas while recording the exact upstream range; do not rewrite
external refs or claim nonancestor commits literally merged.

Owned files are the published 12-path range: `docs/workspace-updates.md`,
`libexec/{workspace-host,workspace-maintenance.rb}`, and under
`portal/cmd/workspace-portal/`, `maintenance_control.go`, `maintenance_pause.go`,
`maintenance_cutover.go`, `maintenance_notice_cleanup.go`, their existing pause
test plus the three new pause/recovery/continuation regression test files; also
`test/workspace_host/maintenance_test.rb`. The four changed Go production files
and Ruby maintenance implementation are byte-identical between e32 and349 before
adoption. All production hunks apply unchanged. Final's Ruby test top insertion
needs only placement beside its existing observer test/header; preserve those
tests, policy2 documentation and observer-state rollback guards in workspace-host.
Do not replace entire differing files. No SDK/native/input/schema/policy change.

Keep the repair's exact invariants: reuse the validated cancellation bit only
while the atomically replaced journal's identity/mode/size/mtime stay unchanged;
replacement requires full validation and cancellation remains visible between
requests. Existing activation permission is added once, with original Stop and
stable submission authority. Pause failure before cutover attempts ordinary
source cancellation/restoration and still reports update failure. Uncertainty
retains its fence. Each continuation pass has its existing repaired 30-second
bound plus separate five-second local result bookkeeping; accepted and unknown
same-ID submissions survive timeout/retry without duplicate sends.

Retain the explicit recover-cancel entry exactly: exact-source build/executor,
worker exclusion and generation/profile-token checks, schema2 cancellation
already requested, unchanged selected original source, no cutover/shutdown/
activation/source-recovery boundary, cancellation action allowlist only. It keeps
the original operation owner, target, claim, participants and submission IDs;
it does not select the repair or authorize another operation. Existing schema1
routing and rollback formats stay unchanged. Root's reported b468 cancellation
and source restoration are operational evidence owned by root, not a new action
or independently observed fact here. A fresh switch requires its accepted
terminal restoration; do not replay repaired cancellation as a deployment.

Review reuse is bounded by deliberately supplied message
`9248f1c3-24f7-4096-a651-e5177f08e069`: standalone Sol/xhigh/read-only
`/root/maintenance_review`, catalog SHA
`527918949048890e311178d620a30706d74abd3d5f4687335112aca4d4966a0c`,
all four lanes on b832→`ca4dd59c023f2a6fa22fe64c0a65c4512fd99ce4`,
then the reported Important continuation fix through
`e9f1b0020c1f2f95f2103ad9c1468e9235e30b88` and narrow admission-order
fix through0bc. Preserve those supplied findings, remediation/check receipts
and no-migration/history conclusions; do not imply review of transplant changes.
147 changes only one test: the expired prior deadline and real 30-second recovery
allowance replace the artificial short budget. Production is identical to0bc.

Owner2 records exact old/new ranges, production blob equality, patch/range
mapping and the sole test-context adaptation; preserve final's preexisting
observer behavior. Reuse certified unchanged review scope; root owns the narrow
equivalence/affected-difference acceptance, not a new blanket review campaign.
First compile both consumers, then run changed maintenance cancellation/cache/
continuation tests and the ordinary Ruby maintenance fixture in the declared
Nix environment, with explicit Go `-mod=readonly`. Include invalid journal
replacement, source/phase refusal, Stop/stable-ID replay, timeout/one-send,
pre-cutover pause-failure restoration and the actual 30-second inventory test.
External quick/package results apply only to their exact heads; our final
transplant requires its own affected checks and exact package/input evidence.
Root selects remaining mandatory packaged/native acceptance after review reuse
is established. No unrelated suite, new recovery mechanism or private helper.

Shortest delivery: preserve/reconcile the root-owned original operation; prepare
the repaired D source and final counterpart together; verify/pin ordinary exact
artifacts; root uses compatible repaired-source selection before another full
policy2 transition. Keep all old artifacts historical and the repaired D feature
in final deployed/integrated lineage. Stop/report any semantic conflict or failed
equivalence rather than weakening a guard. This settles the implementation
boundary; architect capacity available for routine clarification.

**A52 shorter execution route:** the repaired policy1 D source may select the
complete repaired final policy2 package directly. The earlier p71 step was an
available staging option, not a required intermediate format or business outcome.
No A50/A52 contract requires it. Retain p71 as historical/fallback evidence only;
it cannot substitute for the new final head's checks or artifact identity.

The final target must have its accepted source/review-equivalence, exact composed
profile and matching configuration/system graphs, CI and packaged/native checks,
build/copy/provenance and required system deployment established first. Preserve
maintenance schema2/policy2/held-completion1, reporting3, native registration and
all source/target capability checks, including observer rollback contracts.
Finish the original operation's restoration and retain its audit. The fresh full
operation remains owned by the selected repaired D source through activation and
recovery; it targets the exact final artifact without replacing SourcePackage or
reusing an older operation's target/authority. Policy1→2 still requires ordinary
maintenance/native restart, captured participants, stable continuation IDs and
retained-root helper/health proof before success. Final target activation also
enforces its own guards; repaired source and target do not bypass admission.

One member-owned verification batch may publish the completed D composition
artifact early, then finish the final managed build/native cases and system build.
Root may ordinarily select that verified D repair while the watcher continues
only if the actual policy1-compatible native invocation/launch-marker checks and
normal generation/claim/lifecycle guards pass. This is separate from full
cutover: every batch command, watcher/local effect and delivery must be joined or
truthfully reconciled before that attempt, and source monitor admission must
pass normally. Keep exact early-artifact and final-batch receipts distinct.
This removes one activation, changes no contract and needs no new review merely
for route selection. Root owns all execution; no architect live action occurred.

### A53 — registered final heads and the historical D creation failure

Source/ref-only checkpoint; no live/CI/log read, check or mutation. The own portal
manifest registers runtime main734, diagnostics b832, D1=147 and finaldiag
`1b5cebfecceb204ecf5670f5532715fb74f7a1a8`. Canonical ancestry proves main
`734a85fea42c8f8276e6b037196c24cf8903cd12` and diagnostics
`b8329e32f1132fd947f4a9c803bf44e3ed9ce481` already ancestors of1b5.
Only D1 `147bbdbd0de193d26c9342fb80c54e97d45cc812` is nonancestor.
The accepted reconstruction55262543 proves feature containment, not literal
integration of147 and not deployment of the new final artifact.

The smallest ordinary consolidation is therefore D1-only. After actual final
verification/deployment and settlement of the original D-owned operation and
effects, preserve147 and any required consumed predecessors under exact own
retained/public checkpoint refs, with remote proof. Retain required package
roots and any still-required original source checkout identity; a checkpoint
ref alone cannot replace an unfinished operation's source-path contract.
Then update the clean own unmerged D1 feature branch to the same accepted
canonical final head, using the ordinary owned-worktree procedure and an exact
expected-old force lease for its feature publication. Do not delete refs,
unregister repositories, rewrite master, change another session's branch, reset
unrelated work or claim the old147 object became an ancestor. The existing Git
procedure permits unmerged feature-history consolidation while requiring consumed
source retention (`git.md:184–214`); this is no completion exception.

No update of already-contained main734/b832 is required. Keep all registrations
and honest old/new comparison/equivalence receipts. Refresh final comparisons
and ordinary history checks, then integrate the accepted final lineage into the
approved remote default under its normal claim/hooks/SSH verification. Completion
requires each registered final head actually reachable from its remote default,
plus all other repositories and obligations complete (`sessions.md:118–120`).
Do not mark the initiative complete or release the machine merely because D1's
ref moved. Root owns the ordering and exact remote observations; no action here.

The reported D147 creation failure does **not** describe an unchanged final
call site. e32 and147 have `nix/tests/session-creation.nix` blob
`37a6ac37041a0dcd0c84c5a36651e239b1974baa`; final1b5 has
`af30d9d1a2555ab7bbe208a8c07def45f9967822`. The final line1330 already calls
`session_source(package, record["slug"], start=True)` instead of the one-shot
user() invocation. The helper at198–234 retries only exact status1/busy text for
that slug under the existing20s admission ceiling, and preserves all identity/
permission/client assertions. This correction is already in main734's accepted
feature history; it is not a new proposed change. D147's failed CI stays failed
and its peer-supplied cause remains attributed to that source/run. Await root's
actual current final43654242384 result; neither edit nor rerun based on the old
D failure, and do not infer success from source comparison. The unfinished
final build has no output proof here; withdrawn predicted paths remain unproved.
Both decisions are sufficient; architect stops with capacity available.

### A54 — ACT1 durable adoption of activation-forward recovery

Sufficient source brief for implementer2, subject to lead release. Own current
and roster were verified; both environment identity variables are absent after
cutover, and current from the trusted bound session directory matches the binding.
Required unchanged procedures were reused, repository guidance and the affected
workspace-update guide read. Inspection used only canonical public objects.

Adopt the exact single repair range
`147bbdbd0de193d26c9342fb80c54e97d45cc812` →
`fbea38eb2f035fbfccf6c4e1d2e1ad6e9f3c9262` onto merged final
`1b5cebfecceb204ecf5670f5532715fb74f7a1a8` as one ordinary successor commit.
Do not rewrite merged1b5 or consumed147/fbea, recreate D deployment, or claim
fbea literally merged when documenting an equivalent transplant. Keep exact
source/equivalence and recovery references. This is eight files only:
`libexec/workspace-{coordination-claims,coordination-host,coordination,host,maintenance}.rb`
except that the executable is `libexec/workspace-host` without `.rb`,
`test/coordination_claims_test.rb`, `test/workspace_host/maintenance_test.rb`,
and `docs/workspace-updates.md`. No Go, SDK, native, input, schema or policy change.

All three coordination implementation files, workspace-maintenance.rb and
coordination_claims_test.rb are byte-identical between147 and1b5 before adoption.
The remaining baseline differences are final's observer rollback guard,
policy2 documentation and observer-policy test. Apply the repair hunks unchanged
and preserve those differences; do not replace whole files. Prove the complete
eight-file range mapping and production equivalence, with only necessary
context placement recorded. Any behavior conflict returns to lead.

The changed contract is narrow: ordinary owner/claim checks default to native
proof. Only `maintenance_retained_claim?` permits the intentionally stopped
native to be absent for an exact nonterminal schema2 cutover with saved shutdown,
operation/profile/source/target/environment identities and original profile
token, or the exact authorized/pending target startup stage. The coordination
engine still verifies retained incarnation, unfenced owner, held physical claim
and current machine mapping. No user flag provides a general native-proof bypass.
Target startup grants and links precede starting only target native units; its
native-dependent activation check follows socket readiness. Portal work remains
held through continuation/client restoration. Keep Stop, stable IDs and all
observer-state rollback/ownership fences.

Retain the public `maintenance recover-activation UUID --source SOURCE
--from-candidate` path and its exact build/executor admission. It takes the
original worker/generation locks and requires recorded shutdown and forward
activation intent, exact candidate/native/plans, source configuration/protocol,
claim and profile identity. Partial profile selection retries the same original
grants and target; terminal, incomplete-shutdown, source-recovery or changed
identity refuses. It never selects the repair executor or rewrites SourcePackage,
the prepared target or journal. A failed admission before worker claim must not
manufacture a recovery mutation. Schema1 routing and existing schema2 fields stay
unchanged; older source packages retain ownership of their accepted operations.

Checks are the affected Ruby syntax and ordinary fixture entry points in the
declared Nix environment: exact retained-claim/no-native case and ordinary native
refusal; changed schema/owner/incarnation/fence/token/target denial; pending
selection replay; granted-native-before-activation ordering with no portal start;
original forward recovery and refusal cases. Preserve the existing observer
policy test and broader maintenance invariants. Use `test/workspace_host_test.rb`
with the affected filter, not the unsupported direct maintenance-test invocation.
Owner supplies committed exact head, full range/production mapping and focused
results. Root supplies the deliberately shared external review/remediation
provenance and accepts reuse for that exact scope; no new review campaign or
peer-record access. New configured artifacts still need their actual head/input
and required package evidence; prior results are not relabeled.

Root reports old operation `4a7c4f9b-9d1f-439c-9db3-1d05ee60cd7a`
complete/revision38/updated, source255c→targetslkr, continuationsSettled and
restoration.completed true, plus successful retained native MCP status. Preserve
those original receipts and distinguish worker completion from any uncertain
caller effects; do not invoke recovery again for that terminal operation.
This report is supplied operational evidence, not a new architect observation.
Once the configured successor is built/copied and verified, the existing
policy2→2 same-native compatible `workspace-host switch --source SOURCE` is
the intended route, subject to actual invocation/marker, generation, lifecycle,
claim and observer compatibility checks. No new full maintenance census or
restart is needed when that ordinary predicate passes; do not force the path if
it refuses. Root owns final deployment, health/retained-root continuity, approved
integration, complete feature lineage and machine release. Source design stops
here with capacity available; no live action is authorized by this appendix.

**A54 generated/deployment and evidence-reuse boundary (ACT2):** the normal
single config devWorkspace pin must match the successor workspace nested runtime.
`bin/check-dev-workspace-deployment:26–35` compares exact locked identities;
Ruby-only changes do not exempt that alignment. Preserve all eight runtime
dependencies and every baseline sibling/follows edge. Evaluate and bind the new
configuration/system derivation: exact old6ha output equality permits reuse of
that actual receipt; otherwise realize the real new output. When the only output
changes are configuration/input metadata and all module-dependent services,
stock/native/tool outputs are identical, ordinary metadata-only realization,
copy and deployment can reuse those cached unchanged closures. Do not relabel
old6ha as the new configuration from source similarity or prescribe a broad
system rebuild/test suite. Root accepts the exact resulting graph/output proof.

The retained11-case run is specifically `TestNativeMonitorOperation` (own
REC2 managed recipe). Its source at1b5 uses the candidate's portal MCP/CLI,
runtime contract, installed catalog and selected native executable; it does not
execute the changed Ruby host/coordination orchestration. Its coverage can be
reused when the complete Go/SDK/native/test-fixture inputs, installed catalog/
contracts, actual portal ELF, wrapper targets and executable dependencies are
equal and independently bound to the actual new composed artifact. Record the
original76.615s run as historical and the new input-equivalence evidence
separately; do not claim it ran against the new output. Equal Go sources or an
ELF alone are insufficient. Missing equality keeps only the affected proof open.

Minimum remaining correction acceptance is affected Ruby syntax, ordinary
coordination/maintenance fixtures (including the existing observer-policy case),
the actual new configured package result and the repository's normal exact-head
fast/archive/creation CI. These cover changed Ruby behavior; unchanged native
coverage is not its substitute. No new review campaign, standalone native11 rerun,
global census or full-maintenance test is added merely for this correction.
Root owns deliberately shared review provenance in
`/tmp/session-archival-deploy-recovery/act1-shared-review.json`, old complete4a
effects, normal compatible activation and bounded health/continuity verification.
No new live investigation, pin, evaluation or build was run by architect.
