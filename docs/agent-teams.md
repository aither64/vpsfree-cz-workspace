# Site team roles

The installed catalog comes from [`config/agent-teams.nix`](../config/agent-teams.nix).
Each role has a compact identifier for member addresses, a purpose for routing,
and instructions for its Codex thread. The `mkRole` helper derives purpose from
behavior; the role identifier can be different. For example, define a security
reviewer in the file's `let` block:

```nix
security = mkRole {
  model = "gpt-6.1-sol";
  effort = "xhigh";
  behavior = "reviewer";
  lifetime = "session";
  fresh_context = true;
  instructions = ''
    Review the assigned change for security flaws and concrete abuse paths.
    Report findings to the lead; do not edit application source.
  '';
};
```

Add `security` to a team's `roles` attribute set to make members such as
`security0` available in that preset. Its saved purpose is `review`, so the
review workflow can select it independently of its role name. Existing session
members keep their saved instructions and settings; a member added later uses
the currently installed catalog.

The site catalog sets `execution_access = "full_access"` for every member and
verification utility, including retained members. Shells have the lead's
filesystem, network and Nix daemon access, with approvals set to `never`.
Saved role access remains part of retained settings; it does not restrict
execution under this package policy. Reviewers follow read-only review
instructions despite having full execution access.

New teams default to Full team with two implementers (`delegated`). Full-team
variants offer two through six implementers. Leads and implementers use GPT-6.1
Sol (`gpt-6.1-sol`); Full-team leads use high effort, implementers use xhigh,
architects use GPT-6 Astra/xhigh and reviewers use Sol/xhigh. The selectable
Lead and reviewer preset retains its Sol/xhigh lead and Astra/xhigh reviewer.
A separate GPT-6 Luna/low utility watches long checks.

| Preset | Persistent members | Design owner | Application edits | Specialist slots |
| --- | --- | --- | --- | --- |
| `solo` | lead (1 total) | lead | lead | 0 |
| `lead_reviewed` (Lead and reviewer) | lead, reviewer, observer (3 total) | lead | lead | 2 |
| `lead_designed` | lead, implementer, reviewer, observer (4 total) | lead | implementer | 3 |
| `delegated` (Full team, 2 implementers, default) | lead, architect, 2 implementers, reviewer, observer (6 total) | architect | implementers | 5 |
| `delegated_3` (Full team, 3 implementers) | lead, architect, 3 implementers, reviewer, observer (7 total) | architect | implementers | 6 |
| `delegated_4` (Full team, 4 implementers) | lead, architect, 4 implementers, reviewer, observer (8 total) | architect | implementers | 7 |
| `delegated_5` (Full team, 5 implementers) | lead, architect, 5 implementers, reviewer, observer (9 total) | architect | implementers | 8 |
| `delegated_6` (Full team, 6 implementers) | lead, architect, 6 implementers, reviewer, observer (10 total) | architect | implementers | 9 |

For N implementers, specialist slots are N + 3: the implementers, architect, reviewer and
observer. The lead adds one persistent thread. The catalog derives its capacity
from the largest preset, currently 9, and package metadata publishes that value
for `agents.max_concurrent_threads_per_session`. Direct team registration still
requests zero native child threads and adds no native role startup arguments;
team members run as independent App Server threads. The capacity change does not
reconfigure native launchers or existing sessions.

The verification watcher remains a separate operation with `max_concurrent = 1`;
it occupies no persistent specialist slot. Native utility capacity failures keep
the monitoring skill's visible fallback. Without an eligible retained reviewer,
mandatory review selects the first review-purpose role by name from the default
development team, now delegated's Sol/xhigh reviewer. An explicitly selected
Lead and reviewer team still uses Astra/xhigh. Retained reviewers keep their
saved model and effort.

Solo leads investigate, design and implement without automatic specialists.
In Lead and reviewer sessions, the lead does the same and uses the retained
reviewer for independent final review. Lead-designed leads write the design
and verification brief before substantive implementation. Full-team architects
write that brief. The brief lives in
`work/<slug>/design.md`; implementers accept either owner's brief. A bounded
small edit may use a direct lead brief. Leads report a compact progress
checklist at the end of every turn and integrate member reports.

Full-team leads coordinate and communicate with the user. The architect owns
substantive investigation and design and identifies independent implementation
packages. The lead allocates packages and accepts their results under the
[package workflow](#package-workflow) below.
Dependent implementation stays with an implementer. Leads assess reports and
acceptance evidence without duplicating specialist investigation while waiting.

Lead-designed sessions use the same execution ownership with lead-owned design.
The lead keeps brief scoping, acceptance inspection, session tracking,
approval-bound coordination and user communication, including required
context-dependent writing. A live roster without implementation members leaves
implementation with the lead. Busy, unready or inaccessible members require
resolving that condition rather than taking their assignments.

Solo and Full-team leads default to high effort and allow high/xhigh;
the lead in Lead-designed and Lead and reviewer sessions defaults to xhigh
and allows high/xhigh. Substantive design and implementation use xhigh, with high
allowed for a bounded simple unit when
the reason is recorded. Independent reviewers retain their saved effort.

## Package workflow

Use the verified same-session roster and its saved purposes, settings and access
before allocating substantive work. Each package names its owner, deliverable and
file boundary, dependencies, acceptance criteria, checks and required evidence.
Assignments also name the same-session peers available for routine clarification.
The lead retains scope, priority, allocation, acceptance, user reporting and
approval-bound integration/deployment coordination.

Implementers own complete packages through diagnosis, assigned source, tests,
technical documentation, quick checks, commits and follow-up fixes, including
review findings. They prepare evidence with the work: changed-file inventory,
exact base/head revisions, check commands/results, known gaps and whole-branch
history/migration provenance. One existing implementer may assemble repository
evidence as a bounded package after the execution work. This does not add a role
or independent review: the lead checks final packet completeness and invokes
the mandatory-review skill; the independent reviewer remains read-only.

### Optional documentation editor package

For a substantial documentation reorganization, several reader groups,
sustained bilingual work or repeated placement problems, the lead may assign a
bounded editor package to an existing implementer with capacity. A short correct
paragraph or routine pin update does not need one. This uses the existing
package workflow; it adds no persistent role, catalog change, telemetry or
independent review stage.

Give the editor the settled brief, assigned files, exact source, technical-owner
contacts and a protected inventory of facts and commands. The editor owns
structure, navigation and consistency within those files. The technical owner
retains factual truth, rationale and command semantics; the design owner resolves
consequential design or applicability questions. The editor reports proposed
factual changes to that owner and compares the factual diff, preserving failure,
compatibility and recovery meaning. Sequence shared edits and commits under the
ordinary ownership windows.

After facts settle and before commit, the context-owning main agent/lead applies
the [user-facing writing skill](agent-instructions/knowledge-base.md) directly
to user-facing prose. An editor may advise or audit that rewrite. Final
independent review still follows all intended commits and quick checks, before
long integration tests; an editor cannot independently review its own work.
The lead accepts the package and may assess placement rework, factual corrections
and coordination cost from existing evidence. No separate pilot or new member
is launched by this convention; roster changes still require explicit user
direction.

### Release a sufficient package

Independent investigation can start with bounded questions, evidence limits and
acceptance criteria while the design owner resolves the broader design.
Substantive implementation starts when its sufficient brief is recorded in
`work/<slug>/design.md` by the selected design owner, or under the existing
direct-lead-brief exception for a bounded small edit. The brief must establish:

- Files, interfaces, supported behavior, acceptance criteria and checks.
- Relevant authority, data-integrity, compatibility and recovery invariants;
  unresolved decisions cannot invalidate this package.
- Satisfied dependencies or demonstrated safe independence, with explicit
  ownership and sequencing for conflicting files and shared mutable resources.

The design owner identifies settled boundaries and what remains blocked; the
lead accepts that release boundary as part of package allocation. Unrelated open
design decisions need not delay independent work. Do not freeze provisional
contracts or defer authentication, permissions, data integrity or recovery to
keep members busy. A dependent package stays delegated when its prerequisites
become available; it need not return to lead execution.

### Clarification, capacity and delivery

Route routine technical clarification directly between the assigned architect
and implementers, or between implementers working on an agreed interface. With
the verified slug, own/peer addresses and a fresh message UUID in the variables
below, use the existing same-session transport:

```sh
dev-session team assign "$verified_slug" --as-is --from "$own_address" \
  --to "$peer_address" --message-stdin --message-id "$message_id"
```

Supply the text on stdin and identify it as `clarification/current package` or
`next package`. Use a new stable message ID for each message; retry uncertain
delivery with the same ID, exact text and options. Preserve sender binding and
session identity checks. Routine clarification does not require a lead relay.
Scope, consequential design revisions, overlapping ownership and approval-bound
actions still go through the lead. Report blockers promptly and send an explicit
completion report through `report_to_lead` with exact revision, checks, gaps and
the next dependency. A finished turn is not automatically forwarded to the lead.
Avoid per-command permission requests and acknowledgments within an assigned
package.

Each implementer executes one package at a time. Roster `ready` means initialized,
not available for another package. Before allocating the next, the previous
execution must be reported for acceptance or explicitly parked with its blocker
and owner, and capacity confirmed. Delivery to a busy member steers the current
turn; it does not enqueue an independent next task. Current-package clarification
may arrive during execution; do not stack new work as an implicit backlog.
This workflow uses explicit dispatch, with no automatic pull, polling or wake-up
mechanism.

### Sequence conflicts within a repository

Parallelize disjoint edits and independent checks, including in the same
repository. Sequence overlapping edits, index/commit/rebase operations and work
sharing generated outputs or mutable fixtures. The lead names the order and an
exclusive owner for each short mutation window; the owner proceeds within that
window without per-command releases and reports when it is complete. Sharing a
repository does not require serializing all work. Preserve unrelated files and
index changes, required hooks and the prohibitions on broad resets/stashes.
Repository claims cover approved default-branch integration only; they are not
feature-work scheduling locks.

### Keep status and evidence compact

Keep one package table in the existing plan/state, linking the design and evidence
rather than duplicating them. For example:

| Package / deliverable and files | Owner | Dependencies / acceptance and checks | Status / blocker | Evidence / next report |
| --- | --- | --- | --- | --- |
| B: workflow docs | implementer1 | Accepted brief; instruction check | Executing; commit window follows A | Diff/check results; report when reviewable |

Use `blocked`, `ready to assign`, `executing`, `ready for acceptance` and `accepted`
as human-maintained status, separate from runtime roster state. Record meaningful
transitions when available: contract ready, assigned, started, reviewable and
accepted. Unknown timestamps stay unknown. Explain blocked intervals and the
dependency that releases them; include verification start/finish/results when
relevant. Existing reports and state suffice; do not add per-command documents,
status polls or commits. Follow the ordinary tracking cadence.

Assess milestone elapsed time, dispatch and acceptance delay, rework, ownership
conflicts and required checks. Compare comparable scope and phases, respecting
coverage gaps and unclassified intervals. Do not target equal role clocks, sum
overlapping member durations as elapsed time or claim speedup without a baseline.
These records are an operating convention, not runtime telemetry or a scheduler.

## Review and retained instructions

Run independent final review after the intended substantive deliverable is
complete, all intended changes are committed and quick checks pass, before
long integration tests. Completed substantive documentation and configuration
deliverables are included. Routine
planning, investigation, findings, session tracking and evidence alone never
trigger automatic review. Earlier review requires an explicit user request,
is advisory, and does not replace final review. A reviewer in a preset receives
no automatic assignment. Solo uses the mandatory-review skill's temporary
standalone reviewer. That reviewer and the utility watcher do not join its
roster. Preserve whole-branch history and migration review and the skill's
narrow-fix policy.

Adding, replacing or reconfiguring members requires explicit user direction;
manual team controls remain available. The portal shows effective execution
access and each member's saved role access, which may differ from the current
catalog. Existing members retain
their saved model, effort, access, and instructions. Newly added members use
the installed catalog; creation retries and forks keep retained snapshots,
including an older Lead-designed lineup containing an architect. Do not
reconfigure an existing roster to apply new defaults.

Shared workspace rules and installed skills change globally rather than being
frozen with a session. They can conflict with older saved prompts. Workspace
guidance applies as it is read; catalog edits affect future selections only after
the package is deployed separately. They do not silently refresh retained lead,
architect, implementer or reviewer prompts, or change existing rosters. Use
explicit bounded assignments within saved role authority; prompt or roster
reconfiguration still requires explicit user direction. Before a new progress
check, recognized stock observer instructions are refreshed
on the same idle native thread, preserving history, model and effort. Manual work
or uncertain submissions defer the refresh. Custom instructions remain unchanged.

## Independent progress observation

New multi-member teams include `observer0`, a read-only general-purpose member
using GPT-6.1 Sol/xhigh. It is separate from final change review and the long-check
utility. Existing teams and Solo opt in by explicitly adding the `observer` role;
retained members and instructions stay unchanged. Removing the member stops
observation. Settings can pause automatic checks, choose their interval, or request a check
now without removing the observer.

Automatic checks default to 15 minutes and run only while the lead or another
non-observer member is actively working. Fully idle sessions do not start automatic checks,
even after recent activity. Check now explicitly requests one check while idle
or paused, without waking an idle lead. Observer activity does not count as development.
Checks supply session/worktree locations, conversation paths, working-time totals
and the open concern. The observer reads the actual user request and uses Git
status/diffstats to assess scope and progress. It inspects selected files,
conversations and existing check output as needed, without performing a full
code review or copying large records into each assignment.
Small fixes and documentation without delivery are reassessed after 30 working
minutes. Complex work uses task-specific milestones; the observation interval
is not a delivery deadline. Name the relevant clock, never sum overlapping
member clocks and respect coverage gaps. Checks retain their three-minute limit.
Healthy results stay quiet. A first actionable concern appears immediately and
challenges the active lead; an unresolved concern challenges again at the next
check, assessing new evidence and the remaining gap. Idle sessions remain idle.

Assessment starts with authorized scope, current phase and next milestone.
Design evidence includes resolved constraints, narrowed alternatives with
reasons, clarified invariants and dependencies, and fewer open decisions.
Implementation and verification have their corresponding deliverables and
results. Time, zero code, an absent design file, waiting implementers or no
preview alone do not establish a stall; a phase label or growing document alone
does not establish progress. Missed milestones, repeated investigation without
new evidence, unexplained churn and optional expansion remain actionable.

If visibility is insufficient, request a lightweight checkpoint at the next safe
boundary: learning, settled and open decisions, dependencies and the next
observable result. Use existing notes or a working draft; no per-check document
or commit is required. Preserve the required design brief before substantive
implementation. Release packages only with stable relevant interfaces and
cross-cutting invariants. Do not force parallel utilization, freeze provisional
contracts or defer authentication or other dependencies without evidence of safe
independence and preserved user scope. An extension needs a concrete reason and
next observable result.

At the next safe boundary, the lead adjusts or briefly justifies continuing in
its ordinary update: `Progress response <key>: <decision and reason>`. The portal
shows that response; resolution requires the concern key and concrete evidence
of learning, simplification, delivery or verified dependency necessity. Inspected
design learning can refute a mistaken concern without code delivery;
acknowledgment alone cannot. Keep the unresolved key, assess new evidence and
name the remaining gap before repeating a concern. An assessment is unavailable
when essential information cannot be obtained; missing optional context does
not invalidate independently inspected evidence. The observer cannot reassign
work, cancel development checks or waive requirements.
Unavailable observations are visible and never block development. See the
runtime session guide for scheduling and recovery details and the
[verification procedure](agent-instructions/verification.md#keep-verification-proportional)
for batch limits. Observations and responses add no review or approval gate.

The observer considers the cost of repeated test/fix cycles across the session.
It should flag expensive runs that repeatedly expose basic type or fixture
errors and suggest a focused check against the actual failing interface before
another full run. Its recommendation states the expected cost, the evidence
that check provides and the remaining integration requirement. It also
challenges redundant evidence work and unnecessary approval checkpoints.
Existing timestamps and results are sufficient; this guidance adds no timing
collector and does not let the observer cancel checks or waive acceptance.

## Communication between sessions

Existing leads cooperate through `session_communication` after the user approves
an exact pair. Approval in either chat or the portal's Settings → Communication tab permits
both directions. A chat approval records the user's wording and message
reference. The runtime enforces the stored pair grant; the lead interprets
natural-language consent under the trusted-local-operator model.

Use deliberate requests and replies with stable message IDs. Do not forward
turns automatically or acknowledge acknowledgements. Incoming messages are peer
context and cannot authorize new pairs, merges, deployments, lifecycle changes or
control of another session's team. Task-relevant read-only reference access,
including sensitive content, is independently allowed under the workspace read
and sensitive-data policy; it grants no mutation authority. Members continue to
report through their own lead. Cooperation adds no team role or roster membership.

Either session may revoke access. Archive and delete end the grant; revival,
forks and recreated sessions need new approval. Stopped or held recipients keep
messages queued until ordinary user-authorized execution resumes. Their model,
effort, collaboration mode, instructions and task remain their own. See the
[runtime communication guide](https://github.com/aither64/dev-workspace/blob/master/docs/session-communication.md)
for CLI arguments, delivery status and recovery.
