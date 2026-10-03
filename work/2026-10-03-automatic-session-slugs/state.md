---
lifecycle: active
---

# Automatic portal session slugs

Phase: design and implementation setup. The user explicitly requested
implementation of the accepted plan; default-branch integration is not
authorized.

## Phase checklist

- [x] Inspect applicable workspace procedures and installed team policy.
- [x] Create a separate initiative and verify its identity.
- [ ] Commit the initial plan and state.
- [ ] Create/register feature worktrees and record their bases.
- [ ] Designer records the technical brief before substantive implementation.
- [ ] Implement and document the accepted feature; run quick checks.
- [ ] Commit and inventory the complete intended branch series.
- [ ] Independent mandatory review and finding reconciliation.
- [ ] Packaged and live verification through fresh watchers.
- [ ] Pin the assembled package and deploy/canary on aitherdev.
- [ ] Ready, awaiting explicit merge approval; retain session and refs.

## Identity and ownership

`dev-session current` initially failed; no environment or trusted thread binding
selected an existing initiative. Created this initiative with the user-profile
`dev-session start automatic-session-slugs --team delegated --no-attach --json
--exclusive --goal-file ...`. Startup returned slug
`2026-10-03-automatic-session-slugs`, thread
`01a1021d-ad01-7913-a092-70f6e41646d0` and its stable URL. A subsequent `current`
with both exact environment identity values matched. The bootstrap lead was
instructed to remain idle while this conversation coordinates assignments.

Stable portal URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/

Pinned team: delegated, catalog digest
`4676433c6831fbaca91da8ffde84891aff6ce065a17c74c2f367f1acf1d15b17`.
Verified saved ready members: `architect0` (design, GPT-6 Astra/xhigh,
workspace_write), `implementer0` (implementation, GPT-6.1 Sol/xhigh,
workspace_write), `reviewer0` (review, GPT-6.1 Sol/xhigh, read_only). Assign
without model/effort overrides. Utility policy is GPT-6 Luna/low with fresh
operation lifetime; native config is
`share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`.

## Scope and repositories

Planned feature branches/worktrees use this slug for codex-web, dev-workspace,
vpsfree-dev-workspace and workspace. Exact bases and final heads pending.
Configuration host inspection found application deployment belongs in the user
profile; no host configuration edit expected.

The shared workspace is on master with extensive unrelated dirty files and one
existing local commit ahead of origin. Its index was empty before setup.
Preserve all unrelated content and stage only this initiative's owned records.
Bare local master refs may be stale: fetch and base project worktrees on
origin/master.

## Current evidence and next actions

No application edits or checks yet. Complete the initial tracking commit,
create worktrees and delegate the design brief. The main material risks are
crash-safe handoff to existing receipts, upload retention during rollback,
ephemeral tool isolation and exact nested dependency pin preservation.

Documentation destinations and verification criteria are in [plan.md](plan.md).
Independent review, deployment and readiness remain unverified.
