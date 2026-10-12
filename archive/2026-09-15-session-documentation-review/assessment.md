# Session and project documentation: assessment and proposal

Historical assessment of the baseline on 2026-09-15, before implementation.
The accepted [plan](plan.md) and current [state](state.md) supersede its proposed
rollout. In particular, the user chose a generic runtime skill and gradual
project-documentation updates as related work touches them.

## Recommendation

Make the agent responsible for maintaining useful documentation as part of each
change. Give it discretion over which documents to create and how much detail
they need. Preserve explanations in the repository that owns the behavior, with
session records linking to them.

The existing workspace has substantial written context. Decisions, compatibility
constraints, and rollout details are often present, but spread across plans,
state histories, review packets, and occasional runbooks. The improvement needed
is a reliable path from those working records into documentation that the next
developer or operator can find and use.

Keep `plan.md` and `state.md`. Make their roles narrower, and add a short
agent-owned documentation step to development and review. The current portal
already supports extra Markdown artifacts, so this can begin without a new
storage system or manifest schema.

## How it works today

| Location or mechanism | Existing responsibility | Limitation observed |
| --- | --- | --- |
| Workspace `AGENTS.md` | Requires plans to include decisions, compatibility, deployment ordering, and tests; requires useful commit rationale | Does not establish a consistent destination for accepted design decisions or a step that promotes session knowledge into project docs |
| `plan.md` | Intent, affected projects, approach, compatibility, deployment, decisions | Long initiatives retain earlier proposals and follow-ups alongside the final approach |
| `state.md` | Progress, branches, commands, results, blockers, cleanup | Often becomes a detailed chronological record; finding the present contract requires reading past superseded checkpoints |
| `notes/` | Reusable lessons from tooling failures and investigations | Its documented format is troubleshooting-oriented; architecture and operations have no equivalent workspace-wide authoring convention |
| Project docs | Existing architecture, reference, user, and operational documentation | Coverage and maintenance conventions vary across projects |
| Mandatory review | Already asks whether behavior changes update docs, man pages, migrations, and operations | Does not explicitly ask whether the important rationale escaped the session or whether a future task will find it |
| Portal artifacts | Built-in Plan and State, plus explicitly registered files | Provides session-level access; the inspected catalog has no project documentation index or semantic document roles |
| Archive | Preserves tracking and selected evidence, proves repository integration and lifecycle conditions | Its mechanical checks cannot determine whether the explanation of a feature is adequate |

The session helper's plan skeleton includes Goal, Affected repositories,
Approach, Compatibility and deployment, and Testing plan. It does not prompt for
decisions or documentation destinations. Its state skeleton includes Commands
run and Results, with no explicit distinction between current status and
historical evidence. Creation recovery checks for these exact headings, so
changing templates needs a compatibility check. [Runtime source][runtime]

### Evidence from this workspace

- In a filesystem snapshot excluding this assessment, 177 directories under
  `work/` and 21 under `archive/` contained `state.md`. Of these, 27 and four
  respectively exceeded 500 lines. The largest had 19,588 lines. These are
  directory counts, not assertions about valid lifecycle or portal registration.
  Length alone does not establish poor quality, but it makes state files costly
  as the main source of design context.
- The archived workspace-component initiative has an approximately 1,000-line
  state file, including a separate Compatibility decisions section and many
  superseded review checkpoints. It also has an assessment and review packets.
  There is useful rationale to preserve and make discoverable.
  [Session state][components-state]
- The cgroup device-fix plan explains the shared parent versus container-private
  boundary and why running state was left to heal at a controlled container
  restart. The project has cgroup and device documentation, but the two inspected
  pages do not explain that specific change and recovery decision. This is a
  candidate for a focused project-doc update; the session's earlier phase must
  be reconciled with its final implementation before reuse.
  [Plan][cgroup-plan], [cgroup documentation][cgroups],
  [device documentation][devices]
- There are good existing examples. The configuration repository has an indexed,
  release-specific password-recovery runbook with reviewed revisions, rollout
  order, mixed-version constraints, and rollback guidance. vpsAdminOS has recent
  documentation work on NFS cancellation and test-runner behavior. The
  assessment therefore does not support a blanket claim that projects have no
  documentation. [Recovery runbook][recovery], [configuration navigation][nav]
- Some routing instructions have drifted: the workspace names
  `vpsfree-kb-contracts/docs/webui-change-workflow.md`, while the inspected
  vpsAdmin `AGENTS.md` still points to `vpsadmin-kb-captures` for that workflow.
  A canonical document needs maintained links from its consumers.
  [Workspace rules][workspace-rules], [vpsAdmin rules][vpsadmin-rules]

This is a sample of documentation quality, not a full audit of every project,
component README, generated manual, or published documentation site. Repository
sources were inspected at the fetched revisions listed below. vpsAdminOS was
assessed on `origin/staging`; its historical `origin/master` was excluded from
current-state conclusions.

## Give each kind of knowledge a home

| Knowledge | Recommended home | Maintenance rule |
| --- | --- | --- |
| Current intent, constraints, open design questions | Session `plan.md` | Update when the approach changes; link detailed designs and accepted decisions |
| Current implementation status and next action | Session `state.md` | Put a concise summary first; retain material evidence through links and a bounded history |
| How a subsystem works and why its important constraints exist | Existing project `doc/` or `docs/` tree | Update alongside the code; link from the project documentation entry point |
| A consequential choice among plausible alternatives | A short decision section, or a decision record in the owning project's docs | Record context, choice, actual alternatives, consequences, and when to reconsider; link a successor if superseded |
| Repeatable deployment, operation, diagnosis, or recovery | Owning project's operations docs; site-specific procedures in the configuration repository | Keep the procedure usable for the supported system and explicit about prerequisites and verification |
| One particular rollout and its execution evidence | Session `rollout.md` or a release-specific project runbook | State the applicable revisions and rollout status; link the reusable procedure |
| A cross-project contract | One document in the repository that owns the contract; workspace docs for workspace-level designs | Name participating projects and link from their relevant docs; keep one authoritative explanation |
| A development-environment troubleshooting lesson | Workspace `notes/<project>/` or `notes/cross-project/` | Keep a short searchable lesson; promote general project instructions into the project when useful |
| Member-facing guidance | Existing KB or product documentation workflow | Preserve current writing, contract, staging, and publication rules |

A decision record is a small document explaining why a consequential choice was
made. It need not become a file for every change. A few sentences beside a
subsystem description are enough when they preserve the reasoning. Use a
separate record when the decision affects multiple components, deployment,
persistence, security boundaries, or a tradeoff that someone is likely to revisit.

Respect existing layouts: vpsAdmin uses `doc/`, vpsAdminOS uses `docs/`, and confctl
also has generated manuals. Add to those structures before creating another one.
A small project can keep its documentation in its README. Each project should
have one obvious entry point that leads to its architecture and operational
material. A short pointer in `AGENTS.md` tells future agents where to begin.

Current design documentation should explain the supported behavior. Decision
records preserve the historical reason and its status. A release-specific
runbook must state its applicable versions; session state records whether that
rollout was prepared, executed, or verified. This prevents a plan for deployment
from being mistaken for evidence that production was updated.

Project docs should be understandable without this private coordination
workspace. Put the substantive explanation in the project, with local relative
links and relevant commits or tests. The session can link back to it. Internal
hostnames and site-specific deployment instructions belong in their owning site
repository or session, consistent with repository boundaries.

## Model-driven authoring

The model should decide what readers need from the meaning of the change. File
counts and fixed document bundles would encourage filler. These are useful
triggers for that judgment:

- A non-obvious invariant or a choice that a future refactor could accidentally
  undo needs an explanation of why it exists.
- A new subsystem, service boundary, or protocol needs an account of how the
  pieces interact and what each side assumes.
- A change to persistent data or supported version combinations needs a
  compatibility and migration explanation, including rollback limits.
- A deployment requiring ordered steps, downtime, a flag, repair, or manual
  verification needs an operator procedure before the deployment starts.
- A simple local fix may need only an existing-doc correction, a nearby code
  comment, or a useful commit body. A new document can be unnecessary.

The model should update relevant documentation without asking the user to choose
filenames or approve routine authoring. It should ask when the underlying
product or operational decision is unresolved. Writing a procedure does not
change the existing authorization required to execute it.

Capture rationale when the decision happens. Later reconstruction from code can
explain what the code does, but cannot reliably establish the original reasons.
Distinguish recorded decisions from inferred explanations, and name unresolved
questions. Do not invent rejected alternatives or describe an untested command
as verified.

### Proposed instruction

> Treat documentation as part of the change. Read the relevant project docs at
> the start, and create or update documentation when the work reveals knowledge
> that future developers or operators will need: purpose, design rationale,
> constraints, compatibility, deployment, verification, or recovery. Choose the
> smallest useful form and follow the project's existing layout. Preserve
> accepted rationale while it is available. Keep lasting project knowledge in
> the owning repository, and link it from the session and the project's docs
> entry point. Use session files for current intent, progress, and evidence.
> Before review and handoff, reconcile the docs with the delivered behavior and
> summarize what documentation changed, or briefly explain why none was needed.
> Mark proposals, historical decisions, inferred rationale, and unverified
> procedures accurately. Routine documentation work is part of the task.

This text is proposed policy; it has not been installed in `AGENTS.md` or a skill.

## How it fits into a session

1. At planning, read the project's documentation entry point and relevant
   subsystem docs. Add a short Documentation section to `plan.md` identifying
   likely readers and destinations. Revise it as the work becomes clearer.
2. During implementation, record consequential decisions immediately. Update the
   relevant design or operator document as the behavior settles. Keep temporary
   reasoning in the session until it is accepted.
3. Before the existing mandatory review, commit the relevant project docs with
   the feature. Put documentation paths in the review packet. Ask the existing
   reviewers whether the final design and deployment consequences are explained,
   whether commands match the implementation, and whether the docs are findable.
4. At handoff, give `state.md` a short current summary, next actions, useful
   verification links, and documentation links. Distinguish preparation from
   deployment results. Move long command histories into supporting evidence
   when that makes state easier to read.
5. Before considering the initiative finished, ensure accepted knowledge has its
   durable home. Archive the session through the existing lifecycle process;
   the archive remains historical evidence. Documentation authoring belongs in
   the active work and existing review, before an automatic archive can occur.

Preserve the existing tracking commit cadence. Updating these documents does not
need a separate tracking commit for every decision or test. Keep evidence needed
to explain failures, rejected approaches, and review outcomes, but summarize
superseded checkpoints so a reader can identify the current result promptly.
A rough target of one or two screens for the current state summary can guide
writing; it should not become a parser limit or an enforced line count.

## A concrete example

For a device-isolation fix, a useful result could be:

- Update the existing cgroup architecture page with the invariant separating
  shared group/user state from a container's private enforcement state, and why
  changing one container must preserve siblings' access.
- Update the relevant recovery instructions with what a daemon restart repairs,
  what requires a container restart, and how an operator verifies recovery.
- Preserve the rationale for omitting automatic reconciliation in a short
  decision paragraph if it still describes the final supported behavior.
- Keep the exact tested revisions, rollout observations, and review evidence in
  the session, linked to those documents.

That gives the next developer enough context to assess a change without
reconstructing the initiative's full conversation and review history. The
specific explanation must be checked against the final code before committing;
this assessment has not performed that implementation audit.

## Implementation sequence

### First: authoring and ownership

Add the proposed responsibility to workspace policy, with an explicit pointer
to one canonical authoring workflow. The vpsFree extension already distributes
workspace skills and owns the review and handoff skills, so it is a practical
initial home for that workflow. Keep project paths and site ownership in the
consuming workspace and repository rules. If the workflow is later offered to
other workspaces, move its generic parts into dev-workspace and retain links
from the vpsFree extension.

Update review and handoff guidance with the few checks above. Add or repair
project documentation entry-point links as those projects are touched. Apply the
workflow to new work and consequential follow-ups. Backfill old decisions when
a related task needs them and evidence exists; avoid generating a bulk historical
story from code alone.

### Second: session defaults

In `dev-workspace`, add lightweight prompts for Decisions and Documentation to
the plan template. Encourage a current summary in state while preserving required
headings and lifecycle front matter. Update `docs/dev-sessions.md` to explain the
responsibilities and document destinations.

Verify creation, retained-tracking restart, fork recovery, and existing sessions.
The runtime currently validates template markers during creation reconciliation;
changing or removing those markers without compatibility handling could break
retries. An additive prompt is preferable to a new mandatory document schema.

### Third: discovery, if needed

Begin with a short documentation-links section in state and labeled entries in
`portal.yml` for useful session artifacts. Repository documentation remains in
its repository and is linked from the session; the current artifact path format
cannot directly register a file outside the tracking directory.

After trying this workflow on several real changes, consider a project-level
documentation index and portal search across document titles and content. Such
search should distinguish current project docs from historical session material.
This is an optional improvement to discovery. The present portal's Plan/State
plus registered-artifact view is sufficient to start authoring better docs.

If portal metadata later gains document roles or repository references, treat it
as a separate compatibility change: the current Ruby and Go manifest parsers
reject unknown keys. Specify old-reader behavior, test both readers and package
rollback, and preserve archived links. Do not silently change schema-1 manifests.

## How to judge the result

For the next few substantial changes, check whether someone unfamiliar with the
session can find answers to these questions from the project docs and handoff:

- What behavior does this provide, and why was this design chosen?
- Which constraints must a future change preserve?
- How is it deployed or upgraded, and which versions may run together?
- How can an operator verify it and recover from failure?
- Which instructions describe the supported system, and which record a past
  decision or a particular rollout?

Use missing or misleading answers to improve the authoring workflow. A growing
number of Markdown files is not a useful success measure.

## Source references

Workspace policy and notes were read from the shared checkout. Sample session
files can change as their owning sessions continue; the observations above are
from this assessment's snapshot. Project links below pin the inspected commits.

[runtime]: https://github.com/aither64/dev-workspace/blob/227bcfc1b989407582d3b022f8b388ac29972c16/libexec/dev-session
[components-state]: /home/aither/workspace/ai/vpsfree.cz/archive/2026-09-09-workspace-components/state.md:895
[cgroup-plan]: /home/aither/workspace/ai/vpsfree.cz/archive/2026-09-05-cgroup-v1-shared-device-fix/plan.md:23
[cgroups]: https://github.com/vpsfreecz/vpsadminos/blob/d4012a7234bc849bb9253efabf229e73011437c3/docs/osctld/cgroups.md
[devices]: https://github.com/vpsfreecz/vpsadminos/blob/d4012a7234bc849bb9253efabf229e73011437c3/docs/containers/devices.md
[recovery]: https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/b792c50e3baa17a73989dda1129cb17ba0e63587/docs/operations/vpsadmin-password-recovery-deployment.md
[nav]: https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/b792c50e3baa17a73989dda1129cb17ba0e63587/mkdocs.yml
[workspace-rules]: /home/aither/workspace/ai/vpsfree.cz/AGENTS.md
[vpsadmin-rules]: https://github.com/vpsfreecz/vpsadmin/blob/c38839d5be62e9d40d055b23a84844e2037ba4db/AGENTS.md

Additional inspected sources:

- [dev-workspace/docs/dev-sessions.md](https://github.com/aither64/dev-workspace/blob/227bcfc1b989407582d3b022f8b388ac29972c16/docs/dev-sessions.md)
- [dev-workspace/docs/workspace-portal.md](https://github.com/aither64/dev-workspace/blob/227bcfc1b989407582d3b022f8b388ac29972c16/docs/workspace-portal.md)
- [dev-workspace/portal/internal/session/manifest.go](https://github.com/aither64/dev-workspace/blob/227bcfc1b989407582d3b022f8b388ac29972c16/portal/internal/session/manifest.go)
- [dev-workspace/portal/internal/web/templates/details.html](https://github.com/aither64/dev-workspace/blob/227bcfc1b989407582d3b022f8b388ac29972c16/portal/internal/web/templates/details.html)
- [vpsfree-dev-workspace/skills/mandatory-change-review/references/general-review.md](https://github.com/vpsfreecz/dev-workspace/blob/08d691cfd239260ce5bf7c269a44a49ce8de41e7/skills/mandatory-change-review/references/general-review.md)
- [vpsfree-dev-workspace/skills/dev-session-handoff/SKILL.md](https://github.com/vpsfreecz/dev-workspace/blob/08d691cfd239260ce5bf7c269a44a49ce8de41e7/skills/dev-session-handoff/SKILL.md)
- [vpsadmin/doc/index.mdwn](https://github.com/vpsfreecz/vpsadmin/blob/c38839d5be62e9d40d055b23a84844e2037ba4db/doc/index.mdwn)
- [vpsadmin/doc/transactions.mdwn](https://github.com/vpsfreecz/vpsadmin/blob/c38839d5be62e9d40d055b23a84844e2037ba4db/doc/transactions.mdwn)
- [vpsadminos/AGENTS.md](https://github.com/vpsfreecz/vpsadminos/blob/d4012a7234bc849bb9253efabf229e73011437c3/AGENTS.md)
- [confctl/AGENTS.md](https://github.com/vpsfreecz/confctl/blob/6ed1715c27ed1aa6264e9e90213afedb3df7a25f/AGENTS.md)
- [Workspace notes conventions](/home/aither/workspace/ai/vpsfree.cz/notes/README.md)

| Repository | Inspected branch | Revision |
| --- | --- | --- |
| dev-workspace | master | `227bcfc1b989407582d3b022f8b388ac29972c16` |
| vpsfree-dev-workspace | master | `08d691cfd239260ce5bf7c269a44a49ce8de41e7` |
| vpsadmin | master | `c38839d5be62e9d40d055b23a84844e2037ba4db` |
| vpsadminos | staging | `d4012a7234bc849bb9253efabf229e73011437c3` |
| confctl | master | `6ed1715c27ed1aa6264e9e90213afedb3df7a25f` |
| vpsfree-cz-configuration | master | `b792c50e3baa17a73989dda1129cb17ba0e63587` |
