---
lifecycle: active
---

# Provider switch redesign

Phase: investigation and design. The current live workspace remains on OpenAI.

## Phase checklist

- [x] Read workspace procedure routes and affected repository instructions.
- [x] Create a separate initiative without a new native conversation/team.
- [ ] Establish native session-local transition mechanism and record design.
- [ ] Implement automatic pause/resume, per-session and creation selection.
- [ ] Complete quick checks and committed deliverable.
- [ ] Independent final review, isolated integration checks, publication.
- [ ] Explicit integration/deployment direction and any authorized rollout.

## Ownership and locations

- Initiative: `2026-10-18-provider-switch-redesign`.
- Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
- No native roster; lead owns application investigation/design/edits.
- Worktrees and feature branches: not created yet.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-provider-switch-redesign/

## Evidence and constraints

The prior incident is recorded in
`work/2026-10-18-codex-subscription-switch/incident.md` and
`notes/dev-workspace/2026-10-18-provider-switch-idle-and-startup-failures.md`.
Loaded native resume ignores provider overrides; settings/update lacks a
provider field. Establish safe per-session unloading before choosing a design.
Preserve the working OpenAI routing and portal; do not use production-wide
switches or daemon restarts as tests. Many unrelated shared changes exist and
must remain untouched.

Next action: create the dev-workspace worktree and inspect native unload,
provider admission, runtime activity and session creation integration.
