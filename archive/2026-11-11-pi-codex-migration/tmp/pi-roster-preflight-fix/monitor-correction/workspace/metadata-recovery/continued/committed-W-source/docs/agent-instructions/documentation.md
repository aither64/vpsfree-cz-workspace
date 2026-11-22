# Development documentation

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

## Documentation During Development

Use the generic `dev-session-documentation` skill for substantive development,
investigation, and operational work. It is supplied by dev-workspace at
`~/.codex/skills/dev-session-documentation/SKILL.md`; its canonical source and
human guide are in the generic runtime repository. The agent that owns the task
context maintains the documentation while decisions and evidence are available.

Read the relevant project docs at the start. Choose the smallest useful update
and maintain it with the implementation. Record consequential rationale,
constraints, supported version combinations, and applicable deployment,
verification, and recovery instructions. Follow the project's existing layout
and add an entry-point link when needed. Improve older material as related work
touches it; do not launch a historical backfill without a request.

Keep current intent and unresolved choices in `plan.md`. Put a concise current
summary, next actions, documentation links, and verification evidence in
`state.md`; link detailed history and artifacts. Follow the existing tracking
commit cadence and lifecycle rules.

Apply the generic skill's placement rules across all repositories: classify
material by applicability, useful lifetime and owner. Feature explanations
describe the system at the documented revision. Keep individual rollout
checklists and temporary branch state in operational/session records, even when
they contain no dates or revision hashes. Preserve lasting compatibility and
failure semantics with their owning component; link procedures to them.

The generic skill owns the [directory and README convention](https://github.com/aither64/dev-workspace/blob/master/skills/dev-session-documentation/SKILL.md#directory-and-readme-convention).
Use its tree for new material and retain existing subsystem equivalents. The
README stays an entry point for purpose, basic start and grouped links; keep
specialist details in their linked homes. Create directories only when needed.
Apply these site mappings without copying the generic contract:

| Material | Local authoritative home |
| --- | --- |
| Project behavior, rationale, accepted decisions and product tasks | Owning project docs, understandable without this workspace. vpsAdminOS keeps `docs/os/`, `docs/osctld/`, `docs/user-guide/` and `docs/containers/` as existing reference/how-to homes. Configuration reference may use `configs/<component>/README.md` and linked topic pages. |
| Repeatable deployment, diagnosis, operations and recovery | Owning project's `docs/operations/<service-or-task>.md` or existing equivalent. Concrete site procedures belong in the configuration repository that owns the deployment; generic runtime and extension docs link to the contract without copying host details. |
| Supported upgrades | Owning project's `docs/operations/upgrades/<from>-to-<to>.md` or existing equivalent, scoped to actual source/target releases or state boundaries. |
| Cross-project contracts and workspace designs | One authoritative home in the owning project, linked by consumers; workspace-level designs in this workspace's `docs/`. |
| Current intent, choices, status and evidence; individual rollout plans, exact revisions, results and rollback preparation | Shared `work/<slug>/{plan,state,design}.md` and linked records such as `work/<slug>/rollout.md`. Temporary branch state, review fixtures and disposable database resets stay here. |
| Reusable development-environment lessons | `notes/<project>/<yyyy-mm-dd-topic>.md`, or `notes/cross-project/` for shared lessons. General project setup also belongs in project docs. |
| Member-facing guidance | Existing KB/product documentation and [user-facing writing workflow](knowledge-base.md), including publication approvals. |

The [configuration repository's rules](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/master/AGENTS.md#commit--pull-request-guidelines)
prohibit deployment receipts, per-release test reports, screenshots, browser
traces and generated test output in tracked files. Do not recreate
`docs/operations/releases/` or move those artifacts to another tracked directory.
Use session rollout records for individual execution evidence there; the generic
optional `docs/deployments/` destination does not apply. Preserve reusable
configuration and operations guidance in that repository.

Retain a supported upgrade until the owning maintainer explicitly retires the
path with evidence covering old persisted state, backup restoration and rollback.
When retirement evidence is unknown, preserve the instructions and mark
applicability unresolved. Finishing one rollout does not retire its supported
upgrade or recovery path.

Before mandatory review and handoff, reconcile documentation with the final
implementation and actual deployment evidence. Check placement as well as
completeness. Split mixed passages without burying feature contracts or losing
recovery requirements; application transaction rollback is feature behavior,
while reverting deployed software is an operational procedure. Identify changed
or checked docs, or briefly explain why no update was useful. Follow existing
layouts without requiring a fixed file bundle or a deployment heading on every
feature page. Writing instructions remains distinct from authorization to
execute them.

Moves preserve prerequisites, failure/partial-success conditions, compatibility
restrictions, data-loss warnings and recovery steps. Keep old anchors or short
forwarding links where callers may depend on them. Include the compact topic →
reader/class → authoritative path/link → evidence or unresolved applicability
inventory in the existing review packet; the mandatory-review workflow owns the
independent placement and preservation judgment. An optional
[editor package](../agent-teams.md#optional-documentation-editor-package) follows
existing technical ownership, main-agent writing and review boundaries.

Archive records retain Markdown explanations and portal.yml manifests. Keep raw
logs, downloaded artifacts and build output untracked during active work; Archive
deletes those files. Commit project changes before archiving, because checkout
files and index state are not backed up. Shared tracking remains in the main
workspace; feature workspace checkouts omit work/ and archive/.

## Versions in documentation

Follow the [vpsFree.cz writing skill's workflow](https://github.com/vpsfreecz/dev-workspace/blob/master/skills/vpsfree-user-facing-writing/SKILL.md#workflow)
for version guidance in documentation prose, installation snippets and links.
