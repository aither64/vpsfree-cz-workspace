# Team workload: current implementation brief

## Deployment preparation — 2026-11-04

**Settled route:** aitherdev system deployment is supported by
`vpsfree-cz-configuration`, but this policy-only feature needs the existing
workspace user-profile route. Configuration does not install or orchestrate
activation of this application. Its canonical
`docs/operations/codex-providers-aitherdev.md` explicitly permits application-only
`workspace-host switch --source PATH` without system activation (lines 54–59).
`cluster/cz.vpsfree/machines/aitherdev/config.nix` imports the host module;
`flake.nix` maps channel `dev-workspace`/role `devWorkspace` to that runtime.
No configuration source changes, channel updates or system build/deploy are
justified here. The user's route statement supplies no named-default merge
approval; this section releases preparation only, not activation.

Source evidence checked through canonical Git objects and read-only SSH refs:

- Original feature range remains
  `aa94433b2c41a17d54f8128b119e33f3289e93ba..4c958a01aeb79f40ca3658e4e759b184e6cf64d8`.
  Preserve its independent review, narrow-fix evidence and exact-head test results.
  Its four changed files are the catalog and three workflow/procedure documents.
- Workspace remote `master` was
  `12a3df65467c7c460cae5e0a3cd8dca60138288e`; configuration remote `master` was
  `f4069909b55fbed907cb658f350ec6a59f97e05a`. Both select runtime
  `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7`; workspace selects extension
  `f8da821e3c76e26e73aa9d89a712eab0e0faa319`. Refresh these refs during preparation.
- The old feature instead selects runtime `c2182254...` and extension `e4e7e95e...`.
  Current workspace master also supplies `machineIdentityConfig` and
  `config/machine-identity.nix`. Deploying the old source would omit these
  accepted changes. Preserve the current baseline rather than inventing an upgrade.
- Selected profile package:
  `/nix/store/myjy32qh6bd4avgym1awx180y29nvwz9-dev-workspace-0.2.0`;
  deriver `/nix/store/gh92nngdvvyynsqgh6b8l2r0rhcig426-dev-workspace-0.2.0.drv`;
  derivation source `/nix/store/4vkbjz025li2xrsyvhfqkgcnsyw462sd-source`.
  Installed coordination catalog digest is
  `sha256:0866876d14c76c8750bda045bcf18b39ac8324551eb379ffca8ecb2fe58d7048`.
  These identities do not by themselves prove the complete selected input graph.
  Capture and compare that graph with the prepared candidate before any switch.

**One complete package, implementer1:** mechanically refresh the existing workspace
feature onto fresh accepted workspace master, retaining the four-file feature
scope and all baseline inputs/machine identity. Record old/new full base/head
ranges, `git range-diff`/patch-equivalence and no-migration conclusions. Preserve
the old receipts; their successful checks do not certify a new input graph.
Apply existing review-equivalence/narrow-fix rules, returning material patch
changes to lead and the required reviewer. No new design gate is needed.

The same owner prepares an unchanged session-owned, registered
`vpsfree-cz-configuration` reference at the verified remote default only if one
is needed for composition checks and typed machine resolution. Do not use another
session's worktree or create a configuration change to obtain a deployment route.
Run `bin/check-dev-workspace-deployment --workspace-root WORKSPACE_FEATURE
--configuration-root CONFIGURATION_REFERENCE` against exact final locks. Compare
selected/candidate source/input graphs, native invocation, compatibility
descriptors and machine-identity bridge using immutable package/source metadata;
do not inspect peer private state to bypass ordinary switch checks.

Quick acceptance remains scoped diff/cleanliness, effective catalog length and
unchanged non-instruction contracts, existing instruction tests, link checks and
composition validation. Carry forward or rerun only the checks justified by
changed inputs under the existing review/verification rules; lead selects any
required packaged rerun. Preserve exact derivation/input evidence for reuse.
For candidate preparation, from the committed feature worktree use the existing
package export:

```sh
nix build --no-link --print-out-paths .#vpsfree-dev-workspace
```

Any required long/uncertain build/check uses the verification watcher under the
lead's existing workflow. This command builds only; record its exact output and
graph in the existing rollout/preparation receipt. No second implementation lane,
new tests, system build or runtime feature is needed. Completion is a concrete
candidate and compatibility/equivalence evidence for the lead's authorization
decision, not deployment success.

**Later activation, only after lead resolves authorization:** re-read the selected
`workspace-host coordination guide`. Acquire a separate schema-2 machine claim
for registered repository `vpsfree-cz-configuration`, selector
`cz.vpsfree/machines/aitherdev`, adapter `confctl`, after builds/copies are ready.
Verify its exact held binding with `coordination verify-machine`. The supported
ordinary activation command, with the prepared feature path and held claim, is:

```sh
DEV_SESSION_SLUG=2026-10-31-team-workload-parallelization \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
DEV_WORKSPACE_CLAIM_ID=CLAIM_UUID \
  workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-31-team-workload-parallelization/workspace
```

The normal helper owns transition admission, current-state checks and recovery.
Do not use a private activation helper or `--from-candidate` to bypass a refusal.
Same-native/launch-policy compatible updates can preserve running Codex threads;
otherwise ordinary idle-transition rules apply. Verify selected output/catalog,
portal/router health and conversation continuity, and confirm retained member
settings were not rewritten. New defaults affect future selections, not saved
prompts. Exact live system/profile and candidate store paths, source/input graphs,
machine mapping and final/deployed heads belong in the existing receipt.

Before profile selection, a refusal leaves preparation to be corrected without
forcing services. After selection, retain claim/journals/roots and retry the
ordinary switch on the same forward target; recovery is forward-only. Do not
roll back the workspace package or invoke lifecycle cleanup. Release a deployed
machine only after effects are verified and its complete feature lineage is
integrated into explicitly approved remote defaults; verify claim state before
and after release. No repository merge claim belongs to preparation or profile
activation. Workspace/master merge still needs separate explicit approval and
its short merge claim. No configuration merge is needed for an unchanged
reference already at remote default.

## Implementation authorized 2026-11-03

The user requested implementation after the investigation below. This brief
releases two bounded workspace-policy packages; the October findings remain
historical evidence, not claims about current peer-session behavior. The lead
accepted the file split and uses this session as the package-workflow pilot.

**Scope:** implement the operating conventions using existing prompts and docs.
No scheduler, aggregate API, new roles, roster reconfiguration, runtime edits,
dependency updates, deployment or integration. Implementers work in
`worktrees/2026-10-31-team-workload-parallelization/workspace`, branch
`2026-10-31-team-workload-parallelization`, actual initial base
`6383e8848c92c06a9d817f8109853b5b61305c89`. Shared session records stay here.

Refreshed evidence: identity/current and both environment markers match this
session. The relevant catalog, team guide, session and verification guidance
were unchanged from October at inspected shared HEAD `c9e05e119...`; worktree
creation fetched the newer base above. The runtime pin is now
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79`, whose portal guide still documents
peer CLI messages and busy-target steering. No generic runtime change is needed.
Current lead prompts evaluate to 4,063 bytes (Full team) and 4,002
(Lead-designed), against the existing 4,096-byte maximum. Worktree `AGENTS.md`
has 16,356 bytes against 16,384. Consolidate rather than append; retain every
existing authority and safety contract.

## Settled behavior and interfaces

`docs/agent-teams.md` is the authoritative detailed workflow. Catalog prompts
give compact role-specific instructions; existing routed procedures link to
the workflow instead of repeating a new checklist everywhere.

- A complete package includes owner, deliverable/files, dependencies, acceptance,
  checks and evidence. Implementers own diagnosis through fixes, quick checks,
  commits and review preparation: exact revisions, changed scope, results/gaps
  and history/migration provenance. A lead may give an existing implementer a
  bounded evidence-assembly package; the lead retains acceptance, final packet
  completeness and invocation of independent review under its skill.
- Routine architect/implementer clarification uses existing same-session peer
  messages. Scope, consequential design changes, overlapping ownership and
  approval-bound operations still go through the lead. Preserve sender binding,
  stable IDs/exact retries and explicit `report_to_lead` completion/blocker reports.
- Independent investigation may begin with bounded questions/evidence limits.
  Implementation may begin once its sufficient brief is in `design.md`, relevant
  interfaces/invariants/compatibility/recovery are settled, dependencies are
  satisfied or safely independent, and file/resource ownership is explicit.
  Unrelated unsettled global design need not delay that package. No new approval
  ceremony or excuse to postpone authentication/data-integrity prerequisites.
- Each implementer executes one package at a time. `ready` is initialized roster
  state, not availability. The previous execution must be reported for acceptance
  or explicitly parked with blocker/owner before allocating the next, with
  capacity confirmed. Busy delivery steers the current turn; it is not a next-task
  queue. Distinguish current-package clarification from new work; no automatic
  pull, polling, queue or wake-up mechanism is implied.
- Parallelize disjoint edits and independent checks in the same repository.
  Sequence overlapping edits, index/commit/rebase actions and shared generated
  outputs/fixtures. The lead names owner/order for short mutation windows rather
  than relaying each command. Preserve unrelated changes and hook requirements;
  repository claims remain for approved default-branch merges only.
- Keep one compact package table in existing plan/state with owner, dependencies,
  status/blocker and evidence. Record meaningful transitions: contract ready,
  assigned, started, reviewable, accepted. Unknown timestamps stay unknown;
  use available reports without extra per-command documents or commits. Assess
  milestone and dispatch/acceptance delays, rework/conflicts and required checks;
  do not target equal role clocks, sum overlapping durations or add instrumentation.

## Independent packages and acceptance

| Package/owner | Exclusive file boundary | Completion evidence |
| --- | --- | --- |
| A — implementer0 | `config/agent-teams.nix`; only necessary existing `agent-team-policy` assertion wording in `flake.nix` | Compact effective prompts implement the applicable behavior above. Preserve Solo/Lead-and-reviewer ownership, Full-team/Lead-designed distinction, schema, roles/counts, model/effort/access, observer, lifecycle and all review/approval contracts. All effective role prompts remain within 4,096 bytes. |
| B — implementer1 | `docs/agent-teams.md`; minimal reconciliation/pointers in `docs/agent-instructions/sessions.md` and `docs/agent-instructions/verification.md`; `AGENTS.md` only if an existing passage needs replacement/consolidation; narrowly necessary existing assertions in `test/agent_instructions_test.rb` | One discoverable workflow covers package release, message/capacity semantics, evidence ownership, concurrency and compact timeline. Explain retained-prompt effects and preserve mandatory review timing, role boundaries and approval rules. Avoid expanding the nearly full core instructions. |

Both packages depend only on this settled brief and the prepared worktree, and
may edit concurrently. Lead sequences commits/index operations, beginning with
A then B unless a reported readiness change warrants a new sequence. Neither
package owns the other's files. Routine clarification may go directly to
architect0 or the other implementer; material deviations return to the lead.
Architect owns only this design record; lead owns plan/state and user reporting.

## Checks, compatibility and completion

Quick checks: each implementer runs `git diff --check` on its diff and inspects
scope against the brief. A evaluates the raw Nix catalog, checks effective
prompt byte lengths and verifies unchanged non-instruction policy fields;
do not enlarge limits to pass. B runs existing `test/agent_instructions_test.rb`
with Ruby from the repository's Nix environment and checks changed links/examples.
Preserve or minimally reconcile existing wording assertions when meaning stays
the same; do not add tests mirroring the new prose. Required hooks still run.

After both committed packages and quick checks, lead runs mandatory independent
final review of the full base-to-head series/diff, including an explicit
no-migrations conclusion. Then run focused packaged checks
`checks.x86_64-linux.agent-instructions` and
`checks.x86_64-linux.agent-team-policy` as applicable, through the monitoring
skill for uncertain/long builds. No broad runtime/lifecycle suite or deployment
is justified by prompt/documentation-only changes. Check duration, dependency
builds or failures may require reassessment, not an expanded subsystem project.

Catalog changes affect future selections only after a separately authorized
package deployment; retained sessions/forks keep their saved prompts/settings.
Workspace guidance may apply as it is read, but must not be presented as silently
updating retained developer instructions. This session can use explicit bounded
assignments within its saved roles. No persistent schema/API/protocol/migration
or rollback compatibility changes result. Recovery is an ordinary feature edit
or later reviewed corrective prompt update, with existing submission/recovery
contracts intact; this brief authorizes no package switch or session lifecycle
action. Finish as a reviewed, checked, published feature branch awaiting explicit
integration direction; implementation alone does not mean deployed or active.

## Historical investigation — 2026-10-31

Architect findings, 2026-10-31. Advice only; no application changes, roster
changes, deployment or lifecycle actions are proposed for execution in this task.

## Conclusion and evidence boundary

More useful parallelism is possible with the existing team and transport. Start
by giving members complete packages, releasing safely independent work earlier,
and reducing routine routing through the lead. Do not add implementers or build
a scheduler until a measured pilot shows those changes address actual delays.

The architecture concentrates dispatch, acceptance, tracking, overlapping-edit/Git
coordination and approval-bound work in the lead. That concentration is
demonstrated; its contribution to the user's observed imbalance is unverified.
The lead found 116 unarchived sessions in the authoritative global overview,
which exposes neither workload clocks nor current execution state. A lead
working longer than each individual member is not itself a bottleneck: members
have different phase responsibilities, and their work can overlap.

Evidence:

- [Session overview](session-overview.md): aggregate observation and privacy limits.
- [Transport findings](transport-findings.md): implementer0's canonical-source
  analysis and successful installed peer-message submission receipts.
- [Measurement findings](measurement-findings.md): implementer1's clock semantics,
  coverage limits and measurement proposal.
- Workspace `config/agent-teams.nix`, `docs/agent-teams.md` and
  `docs/agent-instructions/verification.md`, inspected at workspace HEAD
  `4737ef1449278f2b8d9b8398178008cfe401fb3c`.
- Generic runtime reference: canonical Git objects at the workspace pin
  `6f54d0c7fdb974705c120b3c1ef5372f5897d544`, especially
  `docs/dev-sessions.md:414-459` and `docs/workspace-portal.md:1457-1617`.
  Bare local master was older. The installed CLI path is recorded in transport
  findings; exact installed source/daemon identity was not independently proven.

No peer records, transcripts, worktrees or rosters were inspected. Session and
environment identity matched the trusted binding before this work.

## What exists and where it can concentrate work

| Demonstrated capability or rule | Implication; hypotheses still needing measurement |
| --- | --- |
| Full teams have independent persistent threads, 2–6 implementer presets, architect-owned design and end-to-end implementer packages. | More configured slots are not the first remedy. Idle execution capacity matters only when safe runnable work exists. |
| Same-session peer messaging already works. Submissions serialize under identity/lifecycle locks; model execution is independent. | Routine clarification need not pass twice through the lead. Submission locks are not demonstrated to dominate elapsed delivery time. |
| Roster `ready` means initialized; busy assignments steer the existing turn. | It does not prove availability or create an independent next-package queue. Stacking assignments can disrupt ownership and focus. |
| Reports are explicit; completed turns are not automatically forwarded. The inspected assignment path has no package/dependency scheduler. | Package state and dispatch remain manual; forgotten reports or slow acceptance could delay work, but were not measured in other sessions. |
| Current prompts already require complete-package delegation, including dependent implementation and follow-up fixes. | More exhortations to delegate may add little. Inspect actual package boundaries and retained policy before blaming missing instructions. |
| Lead/member prompts survive catalog changes and forks; only recognized stock observer prompts refresh automatically. | Older sessions may follow older role boundaries. That is a possible explanation, not an inspected fact about any peer session. |
| Final review follows the completed committed deliverable and quick checks; long verification follows review. | Low reviewer utilization early is expected. Using the reviewer as an early implementation worker would compromise its purpose and does not remove the final gate. |

## Immediate operating model: pilot with existing capabilities

Keep one compact package table in the session's existing plan/state. Each entry
needs owner, deliverable/files, dependencies, acceptance/checks, status and next
report. Link the design brief and evidence instead of duplicating them. Use
blocked, ready to assign, executing, ready for acceptance and accepted as
human-maintained states; these are proposed conventions, not runtime features.

| Owner | Complete responsibility | Escalation boundary |
| --- | --- | --- |
| Lead | User scope/priorities, package allocation, acceptance, concise tracking/user updates, approvals and coordinated integration/deployment. | Product decisions and consequential cross-package changes; no duplicate specialist investigation while waiting. |
| Architect | Cross-cutting invariants, dependency graph, package briefs and design updates; routine technical clarification directly with assigned implementers. | Route consequential design revisions through the lead; do not widen scope or silently release dependent work. |
| Implementer | Diagnosis, assigned source, tests, technical docs, quick checks, commits and follow-up fixes; package evidence and review-packet material. | Report blockers promptly; ask architect about contract ambiguity and lead about ownership/scope. One active execution package at a time. |
| Independent reviewer | Final scope, correctness, whole-branch history/migration and evidence review under the mandatory-review skill. | Remains independent and read-only; idle time before final review is normal. |
| Verification utility | Launch/watch authorized long or uncertain checks through the monitoring skill, with compact result/escalation. | No diagnosis, source fixes, approvals or deployment authority. Package owner handles failures. |

Assignments should name permitted same-session peers and label messages as
`clarification/current package` or `next package`. Send a next package only
after the prior package has an explicit disposition and capacity is confirmed;
do not use busy-target steering as an implicit backlog. Send decision/blocker
reports promptly and one compact completion report with exact revision, checks,
remaining gaps and next dependency. Avoid per-command requests and acknowledgments.

Implementers prepare their changed-file inventory, exact heads, check results,
known limitations and migration provenance. One existing implementer can assemble
the repository review material as a bounded package; this is not a new team role.
The lead checks completeness and invokes required review, retaining scope and
acceptance responsibility. Review findings return to the owning implementer.
This reduces clerical reconstruction without outsourcing independent review.

## Release work when its own prerequisites are settled

Parallel investigation can start while the architect resolves the global design.
This task used two such packages: transport/dispatch analysis and measurement/
observer analysis, with disjoint evidence files and a common canonical source pin.
They needed questions, evidence limits and acceptance criteria, not settled
implementation contracts. The lead independently handled the permitted overview.

For implementation, a package may start before every unrelated design decision
is settled only when `design.md` already contains its sufficient brief:

1. Its files/interfaces, supported behavior and acceptance/checks are defined.
2. Relevant cross-cutting invariants, including authority, data integrity and
   recovery, are settled; unresolved decisions cannot invalidate this package.
3. Dependencies are satisfied or demonstrably independent, and conflicting files
   and shared Git/build resources have an owner and sequence.

The architect records what is settled and what remains blocked. The lead accepts
that boundary. Do not substitute provisional stubs or postpone authentication,
schema compatibility or recovery solely to keep members busy. Serial dependency
work remains delegated to an implementer; it need not return to lead execution.

For a shared repository, parallelize disjoint source edits and independent
read-only analysis/checks. Serialize overlapping edits, index/commit/rebase
operations and operations sharing generated outputs or mutable fixtures. The
lead sets a Git sequence and exclusive owner for each brief mutation window,
instead of relaying every command. Do not serialize all work merely because it
shares a repository, and do not solve contention with broad resets/stashes.
Repository merge claims remain limited to approved default-branch integration;
they are not feature-work scheduling locks.

## Priorities and measurement

1. **Pilot the operating model first.** Use the existing roster and current
   instructions in a participating session under its own authority. Record
   contract-ready, assigned, first activity, reviewable and accepted timestamps
   for a small set of comparable milestones; explain blocked intervals and the
   dependency that releases them. Measure ready-to-start and reviewable-to-accepted
   delay separately from necessary design, execution and verification.
2. **Check retained-policy applicability.** New catalog text does not repair
   older sessions automatically. Make applicable package assignments concrete
   within saved role authority. Any actual prompt/roster reconfiguration requires
   explicit user direction and preserved custom settings/history.
3. **Add small visibility improvements only if gaps recur.** Candidate work is
   clearer initialized/working/package-available terminology and a view of the
   existing package table. A global aggregate metric API would be new capability,
   with explicit privacy, coverage and freshness semantics.
4. **Consider a durable ready queue only after measured dispatch delay.** If safe
   work repeatedly waits for a busy lead, design package ownership, dependency
   release, completion acknowledgment and explicit steer-versus-next semantics.
   Reuse existing delivery; do not build another peer bus or weaken identity locks.

Pilot success means shorter milestone elapsed time and less avoidable
ready-to-start/acceptance delay without higher rework, missing checks, ownership
conflicts or premature contract changes. Count necessary waits honestly. Observe
whether lead touches per accepted package fall; do not optimize for equal role
clocks, message count, output size or maximum simultaneous agents. Compare phases
and comparable scope, with coverage/unclassified intervals shown. Never sum
overlapping member clocks as elapsed time or claim speedup without a baseline.

## Compatibility, recovery and acceptance

This advice changes no persisted formats, APIs, model settings, roster policy,
deployment state or recovery contract. The initial pilot is an operating
convention using existing files and tools. Revert that convention by returning
to explicit lead dispatch; reconcile current owners and uncertain submissions
first. Ordinary exact-final-head review/integration, merge approval, machine
ownership and lifecycle rules remain intact.

A later runtime task ledger would require a separate approved design: additive
state/version semantics, old-reader behavior, idempotent claims/submissions,
restart recovery, stale/uncertain result handling, held/stopped session behavior,
and compatibility with package transitions. Older supported packages must not
silently launch duplicate work. Do not add a second automatic lifecycle or
deployment authority. Rollout would follow normal independent review and the
selected package's coordination/deployment procedure; no rollout is prepared here.

This investigation is accepted when capabilities and hypotheses are separated,
the lead has the evidence limits and prioritized operating model, and each
recommendation preserves role authority and safe concurrency. Quick verification
is reconciliation against the two member reports, current policy and cited
canonical source; no application tests or automatic review are required for
routine findings. Longer checks are the proposed in-session pilot, not work
performed or authorized by this report.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-31-team-workload-parallelization/>.
