# Architect handoff, lead status, and final branch review

## Goal and owners

Adapt the instruction fixes from workspace commits `04b0e5c682` and
`3f539b0f6f`, and extension commit `dcb2762192`, without regressing the
currently selected workspace package. New full teams use an architect on
`gpt-6-astra/xhigh` to establish the design and verification steps for
substantive work. The lead orchestrates and reports progress; implementers
make application edits. Keep workspace `AGENTS.md` and retained-role initial
instructions consistent.

Affected projects: this coordination workspace and `vpsfree-dev-workspace`.
The generic `dev-workspace`, `codex-web`, and `vpsfree-cz-configuration` are
consumers or conditional deployment paths, not planned code changes.

Readers: future session leads, architects, implementers, reviewers, and the
operator deploying the user-profile workspace package. Lasting role policy
belongs in workspace `AGENTS.md` and `docs/agent-teams.md`; the reviewer
procedure belongs in the extension skill. This initiative's current checklist
belongs in `state.md`.

## Approach

1. Architect records a concrete design and verification brief for this
   initiative. For future substantive team tasks, an architect writes a brief
   under `work/<slug>/design.md`; the lead assigns implementers from it and
   resolves design gaps with the architect. Small bounded edits go directly
   to an implementer. Architect may edit assigned design documents and
   prototypes, while the lead may maintain coordination records but does not
   take over application edits.
2. Adapt `04b0e5c682` into workspace policy, team instructions, and git and
   verification procedures. Require compact end-of-every-turn status with
   current phase, done, remaining, blockers, and next action. Keep a live
   phase checklist in `state.md`, updated at phase changes rather than
   committed every turn. Require a final independent, whole-branch review
   with migration provenance before claiming readiness.
3. Adapt `dcb2762192` in the extension mandatory-review skill. Preserve the
   current package baseline; `3f539b0f6f` contains a stale pin and must not
   be applied as-is. Pin a new extension revision after review and focused
   verification.
4. Set the new architect role (internally `designer`) to
   `gpt-6-astra/xhigh`, retaining the documented `high` simple-design option.
   Keep lead, implementer, reviewer, and Luna watcher defaults unchanged.
   Keep the `lead_designed` preset key but give new instances an architect-led
   topology; retain `solo` for discussion and investigation, not application
   editing. Update catalog assertions and preset descriptions.

## Compatibility and deployment

No persisted schema, API, CLI, protocol, database, generated system option,
or migration change is planned. New catalog defaults apply to new members;
retained members keep their frozen prompts, model, and effort. Existing
sessions are not migrated. The review-skill and workspace-policy text can be
rolled out together through the user-profile workspace package. A rollback to
an older package is not promised for newly created Astra members; this is a
development-only workspace and the chosen deployment path moves forward.
Keep the current runtime pin and verify the new extension revision contains
it. If aitherdev system configuration changes become necessary, use a
`vpsfree-cz-configuration` feature worktree and deploy that branch using
`confctl`; do not put the workspace application in system configuration.
Neither deployment nor verification grants default-branch merge approval.

## Verification and integration

- Compare `AGENTS.md`, the catalog's initial role instructions, and reviewer
  skill for contradictory responsibilities and status/review requirements.
- Evaluate the generated catalog, including architect Astra/xhigh, Sol and
  Luna defaults, model inventory, and first-message prompt behavior.
- Run quick repository checks, then mandatory review of all intended commits
  and the complete feature series. Use a fresh Luna/low watcher for long or
  uncertain checks and deployment waits.
- Build and deploy the user-profile package, then smoke-test a new team and
  its design-to-implementation handoff without altering existing sessions.
- Keep branches active until explicit approval names the repositories and
  default branches to integrate.
