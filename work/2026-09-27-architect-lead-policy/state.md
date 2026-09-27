---
lifecycle: active
---

# Current state

The new session and dedicated worktrees are ready. The architect's
[`design.md`](design.md) handoff is accepted; no project code or package has
changed yet. `dev-session current`
found no owned session in this shell, so this initiative was created
separately. The shared workspace checkout has unrelated dirty files; preserve
them and stage only this initiative's paths.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-27-architect-lead-policy/

## Phase checklist

- [x] Establish scope, compatibility, and deployment plan
- [x] Architect design and verification brief accepted
- [ ] Workspace policy, prompts, catalog, and docs committed
- [ ] Extension review skill committed and workspace pin updated
- [ ] Quick verification and whole-change independent review complete
- [ ] Longer checks and new-team smoke test complete
- [ ] User-profile package deployed and verified
- [ ] Explicit default-branch integration approval and merge

## Branches and worktrees

Branch: `2026-09-27-architect-lead-policy` in workspace and
`vpsfree-dev-workspace`.

- Workspace: `worktrees/2026-09-27-architect-lead-policy/workspace`
- Extension: `worktrees/2026-09-27-architect-lead-policy/vpsfree-dev-workspace`

The current workspace pin is extension `47d9d93cc2373f010a3e6963f76b1cb57bbc1240`;
the older `3f539b0f6f` commit would replace it with `dcb2762192` and so
cannot be used directly.

## Next action

Assign the workspace and extension edits to separate implementers. The
`lead_designed` key will remain for compatibility, but newly created teams
using it will include an architect. Solo remains investigation and discussion
only; it does not license lead-owned application edits.
