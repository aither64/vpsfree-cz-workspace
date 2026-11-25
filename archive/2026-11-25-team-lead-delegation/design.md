# Full-team lead delegation: design and verification brief

Package D, architect0, 2026-11-25. Scope: workspace instructions only.
The contracts below are sufficient for packages I0 and I1; lead acceptance and
allocation remain required. Initial plan/state are lead-owned. No application,
runtime, scheduler, telemetry, roster, deployment or integration work is included.

## Goal and evidence boundary

Make Full-team leads coordinate, assess evidence and report progress without
silently repeating or retaining substantive specialist work. Improve the rules
at the points where existing delegation language is ambiguous; do not add a
second scheduling process or measure success by equal role clocks.

Investigation is bounded to `AGENTS.md`, `docs/agent-teams.md`, routed workspace
procedures, `config/agent-teams.nix`, the verified same-session roster and one
bounded evidence report from implementer2. No peer-session sampling by the
architect. Identity matched `dev-session current`, the complete environment pair
and the thread binding; the roster identifies architect0 as design-purpose with
workspace-write access.

The initial evidence report does not establish systematic dispatch delay or
duplication from elapsed clocks. These are concrete instruction ambiguities,
not a claim that every existing session violates ownership. Detailed sample
evidence belongs in implementer2's report, subject to its sensitivity checks.

| Current wording/location | Concrete gap to close |
| --- | --- |
| `AGENTS.md` and role guide repeatedly distinguish “application edits” from lead coordination | Substantive instruction/configuration changes, diagnosis, technical docs, check preparation and evidence assembly can be treated as lead chores despite their package ownership. Define substantive work by responsibility, not file extension. |
| Guide allows “brief scoping” and “acceptance inspection” while prohibiting duplicate investigation | No practical stopping condition separates useful spot inspection from a second investigation, full review or rerun of unchanged passing checks. |
| `leadRequirements` says “Inventory full base-to-head series/diff/migrations; consolidate…” for every lead | Imperative execution wording conflicts with implementers owning commits, evidence and fixes. Separate ensuring completeness from assembling or repairing the evidence/history in delegated modes. |
| Full-team prompt says “Own design only if none exists” | The referent is unclear: no design document, no completed design, or no design-purpose member. Make the exception depend on the verified roster and saved authority. |
| Small edits may use a direct lead brief | This relaxes the separate design-document requirement, not delegated execution ownership; state that explicitly. |
| “Coordinate checks/deployment/records” and no-duplication “while waiting” | Checks, failure diagnosis and follow-up evidence remain assigned work after a handoff too. Preserve lead-owned safety/approval actions while naming who prepares and diagnoses. |

## Operating contract

### Lead boundary and stopping rule

In Full-team mode, the lead owns user scope, priorities, package allocation,
acceptance decisions, compact tracking and reporting, necessary approvals and
safety/authority coordination. The architect owns substantive investigation,
design and verification planning. Implementation-purpose members own assigned
execution, including technical documentation/instructions, configuration,
diagnosis, tests, quick checks, evidence assembly, commits and follow-up fixes.
Use the existing package process and one executing package per implementer.

The lead may read enough source, status and supplied evidence to identify the
question, assign an owner, establish a release boundary or make an acceptance
decision. For acceptance, identify the criterion or concrete uncertainty being
checked, inspect the relevant supplied evidence and a targeted source/diff/result
sample where needed, then accept or return a specific gap to its owner. This
does not require a separate inspection document or per-command permission.

Stop lead inspection once the criterion is established or a gap needs substantive
investigation, reproduction, correction, broad source reading or repeated checks.
Send that work to the existing owner with the question and expected evidence.
Do not independently reproduce the specialist's investigation, repair its patch,
assemble the same evidence or rerun unchanged passing checks merely for personal
confidence. New contradictory evidence, changed inputs or a required unrun check
justify more work; name the reason and assign its execution. Acceptance is still
the lead's responsibility and never means trusting a completion claim blindly.

Before delegation, initial triage ends when the lead can state a bounded question,
deliverable, owner and acceptance condition. Technical uncertainty is a valid
investigation assignment; it does not require the lead to solve the problem
before assigning it. Release sufficient independent packages promptly under the
existing stable-contract rule. Do not invent work to occupy members or fragment
a narrow package across extra people.

### Diagnosis, checks and evidence

The package owner diagnoses failures, prepares and executes applicable quick
checks, provides commands/results and revisions, and repairs findings. A bounded
evidence-assembly package may go to an existing implementer after capacity is
confirmed; its output includes the base/head range, changed files, check scope,
gaps and history/migration provenance. The lead checks completeness and routes
independent final review; it does not recreate the packet's underlying analysis.

Long or uncertain verification retains the monitor skill's existing execution
and observation ownership. Watchers do not diagnose, modify, retry or deploy.
The appropriate implementation/design owner handles an observed failure and
proposes the next check; the lead coordinates dependencies and acceptance. No
new utility, monitoring loop, timing collector or runtime operation is required.

Preserve lead-owned authority-sensitive actions: approval interpretation,
repository/machine coordination, freshness and ownership checks, and drivers
that also approve, submit, integrate or activate operations. Preparing build,
test, review and rollout evidence can be delegated within its authorized package;
delegation does not transfer approval authority or permit claims to be held while
waiting. Required context-dependent user-facing writing stays with the main
agent/lead under its skill. Routine plan/state edits remain with the lead.

### Exceptions and retained compatibility

| Mode or condition | Preserved behavior |
| --- | --- |
| Solo | Lead investigates, designs and implements; no automatic specialists. Required independent review and verification utilities remain separate. |
| Lead and reviewer | Lead investigates, designs and implements; retained reviewer performs independent final review. |
| Lead-designed | Lead owns substantive design; implementers own execution, diagnosis and evidence. Acceptance stopping rules do not prohibit the lead's actual design role. |
| Full-team | Design-purpose member owns substantive investigation/design; implementation-purpose members own execution. |
| Verified roster genuinely lacks the relevant purpose | Existing lead fallback may apply within saved instructions; an absent file or pending deliverable does not establish this exception. |
| Relevant member busy, unready, blocked or inaccessible | Resolve or explicitly park the dependency; it is not absence and does not authorize takeover. No new/replacement member without explicit user direction. |
| Bounded small edit with direct lead brief | May omit separate design.md; the selected mode's execution ownership remains unchanged. |

Shared workspace guidance applies when read. Catalog prompt changes affect future
selections only after a separately authorized package deployment. Existing members
retain saved model, effort, access and instructions; do not rewrite their snapshots
or reconfigure the roster. Use bounded assignments within saved role authority.
If an actual saved instruction conflicts with a new task, surface that conflict
to the lead for resolution rather than silently changing settings or taking over.
Preserve the already documented stock-observer refresh behavior and its custom
instruction exception; no refresh mechanism changes belong here.

### Observation from existing evidence

The observer may flag a lead repeating assigned investigation/checks, retaining
substantive work that fits an available authorized package, or holding a settled
package without a dependency. It must identify the concrete work, ownership and
missing reason from existing assignments, reports, transcripts or diffs. Account
for acceptance inspection, mode-specific lead duties, approval/safety actions,
user-facing writing and actual blockers. Larger lead clocks, idle implementers
or roster `ready` alone prove neither duplication nor available capacity. Suggest
a bounded handoff or justification under the existing concern workflow; no new
gate, reassignment power, roster mutation or data collector.

## Package boundaries and release

Feature root supplied by lead:
`worktrees/2026-11-25-team-lead-delegation/workspace`.
The architect edits only this shared `design.md`.

| Package / owner | Deliverable and files | Dependencies, acceptance and evidence |
| --- | --- | --- |
| I0 / implementer0 | Instruction docs: `AGENTS.md`, `docs/agent-teams.md`; targeted consistency changes in `docs/agent-instructions/verification.md` only where needed | This sufficient brief and lead allocation. Put the detailed contract in the role guide; keep AGENTS and verification concise pointers/compatible summaries. Cover substantive non-code work, triage/acceptance stopping conditions, small-brief exception, owner-routed failure/evidence work, modes/retained compatibility and evidence-based observer checks. Preserve existing anchors and mandatory safety/review requirements. Report exact changed scope, revision, checks and scenario results. |
| I1 / implementer1 | Catalog prompt strings in `config/agent-teams.nix` | This sufficient brief and lead allocation; independent of I0 prose. Clarify Full-team design fallback, delegated work coverage and acceptance boundary. Replace common imperative evidence/history execution with mode-compatible accountability, and keep delegated execution details in `delegatedRequirements`. Add compact observer duplication guidance. Adjust implementer/designer prompt only if needed for this contract. Preserve all non-instruction values and all four mode distinctions. Report evaluated-catalog invariants, revision, checks and scenario results. |
| E / implementer2 | Existing bounded evidence report, under lead's assigned file ownership | Already independently assigned. Evidence can refine examples; it is not a blocker to I0/I1 and does not authorize additional sampling or broad empirical claims. |
| Acceptance / lead | Plan/state, allocation/capacity, Git mutation windows, complete review packet and review invocation | Compare I0/I1 output against this contract and reconcile mismatches by returning specific gaps to their owners. Lead accepts package release and results. No automatic implementation assignment from this design. |

I0 and I1 may edit disjoint files concurrently. Lead sequences their Git
index/commit windows and any shared formatter outputs. Assigned architect and
implementers clarify wording directly using verified addresses and stable message
IDs. Scope changes, consequential contract changes and ownership conflicts go to
the lead. No further files are implicitly assigned.

## Acceptance and checks

Use existing repository hooks and declared environment. No behavior test harness
or brittle exact-prompt snapshot is needed for this instruction-only change.

Quick checks, owned by each implementer for its files:

- `git diff --check`; required formatting/hooks, preserving unrelated paths.
- I0: verify touched links/anchors and read the factual diff for lost ownership,
  compatibility, approval, monitoring, review or lifecycle requirements.
- I1: parse/evaluate the standalone catalog (`nix-instantiate --eval --strict
  --json config/agent-teams.nix` or the repository's equivalent). Compare old/new
  evaluated structures after removing only instruction-string fields: schema,
  presets, members/purposes, model/effort/access, capacity, routing, utility and
  lifecycle policy must be identical. Catalog digest changes from text are expected.
- Both: perform a compact semantic scenario check against the changed text:
  Full-team unclear diagnosis is delegated; completed package with missing
  evidence returns to owner; unchanged passing checks are not repeated without
  a reason; busy member is not treated as absent; small edit still follows mode
  ownership; Solo and Lead and reviewer still implement; Lead-designed still
  designs; lead safety actions and required writing remain lead-owned; retained
  prompts are not silently refreshed; observer requires concrete duplication
  evidence and respects legitimate lead duties.

The lead invokes mandatory independent final review only after intended
instruction/catalog commits and quick checks. Reviewer receives the whole branch,
this brief, scenario evidence and explicit no-migration provenance. Routine
package-D planning/evidence does not itself trigger review. No long runtime or
integration test is proposed: no runtime behavior, state format or interface is
changed. Any required repository check discovered by implementers remains
applicable, with long/uncertain execution following the existing monitor skill.

## Compatibility, deployment and recovery

No database, persisted state, API/CLI/protocol, generated client, Nix module option,
runtime scheduling or backend-neutral interface change. No catalog schema or
policy change. Existing sessions and mixed old/new saved prompts remain supported
under the retained-settings rule above.

This initiative prepares source instructions and catalog text only. It does not
select a package, deploy, merge, reconfigure a team or close a session. A later
authorized integration makes shared guidance available; catalog rollout is a
separate package deployment under its applicable procedures. Do not claim current
members adopted new prompt strings merely because a feature branch exists.

Recovery is a reviewed source correction/revert through the ordinary repository
process, and, if a later rollout occurs, its existing package rollback procedure.
No data migration, roster rewrite or lifecycle cleanup is necessary or authorized.
Source rollback cannot undo saved instructions already selected by newly created
members; retain their snapshots and use supported explicit configuration only
with user direction.

## Settled and remaining

Settled: I0/I1 ownership, operating boundaries, mode exceptions, retained-prompt
compatibility, checks and no-runtime/no-deployment scope. Ready for lead acceptance
and allocation without waiting for E's final detail. Remaining: implementation,
semantic reconciliation, quick checks, independent review and separate delivery
decisions. Evidence samples may refine rationale but cannot add a new mechanism
or expand scope without lead resolution.
