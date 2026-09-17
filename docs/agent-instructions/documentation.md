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

Use these local destinations:

- Project behavior, design rationale, and accepted decisions belong in that
  project's documentation, understandable without this coordination workspace.
- Repeatable operations belong in separate project operations documentation;
  site-specific procedures belong in the configuration repository that owns the
  deployment. Generic runtime and extension docs link to their contracts
  without copying concrete host details.
- Supported upgrade instructions belong in the owning project's upgrade
  guidance, scoped to source/target versions or schema boundaries and retained
  while that path needs support. Do not invent release versions or hide guidance
  needed by other upgraders in private session records.
- Cross-project contracts have one authoritative home in the owning project;
  workspace-level designs belong in this workspace's documentation. Link the
  participating projects to that home.
- An individual rollout's plan, exact revisions, prepared steps, execution
  results and rollback preparation belong in a session rollout record or a
  dated record in the deployment repository. Temporary branch state, review
  fixtures and disposable database resets belong in session records.
- Reusable development-environment lessons belong in `notes/` under the existing
  convention. General project setup instructions should also reach project docs.
- Member-facing guidance follows the existing KB/product documentation and
  user-facing writing workflows below, including publication approvals.

Before mandatory review and handoff, reconcile documentation with the final
implementation and actual deployment evidence. Check placement as well as
completeness. Split mixed passages without burying feature contracts or losing
recovery requirements; application transaction rollback is feature behavior,
while reverting deployed software is an operational procedure. Identify changed
or checked docs, or briefly explain why no update was useful. Follow existing
layouts without requiring a fixed file bundle or a deployment heading on every
feature page. Writing instructions remains distinct from authorization to
execute them.
