---
lifecycle: active
---

# Current state

## Initiative

- Slug: `2026-09-04-cgroup-v1-soft-delete-devices`
- Session created with `bin/dev-session start cgroup-v1-soft-delete-devices
  --no-attach --no-codex`.
- This process owns the slug by running initiative commands with
  `VPSFREE_DEV_SESSION_SLUG=2026-09-04-cgroup-v1-soft-delete-devices`.
- A separate managed initiative named `2026-09-04-cgv1-devices-bug` already
  existed without a matching environment variable; it is owned by another
  process and will not be touched.

## Scope

- Candidate repositories: `vpsadmin`, `vpsadminos`.
- Requested outcome: root-cause diagnosis only; no fix is currently authorized.
- Feature branches and worktrees: not yet created.

## Progress

- Confirmed that canonical bare repositories `repos/vpsadmin.git` and
  `repos/vpsadminos.git` exist.
- Recorded the supplied symptom: after a VPS is soft deleted on a cgroup v1
  node, `osctl healthcheck -a` can report configured character devices such as
  `10:200`, `10:229`, and `10:232` as not allowed in the container's devices
  cgroup.

## Commands and results

- `bin/dev-session current`: no current session because the inherited
  `VPSFREE_DEV_SESSION_SLUG` was unset.
- `git status --short --branch`: shared top-level checkout is on `master`, one
  commit ahead of `origin/master`, with numerous unrelated changes. Only this
  initiative's paths will be staged.
- `bin/dev-session list`: found the separately owned similar initiative.

## Open questions

- Which vpsAdmin soft-delete step changes device-policy inputs or container
  placement?
- Does osctld fail to reapply an unchanged effective device policy after a
  parent cgroup or ownership change?
- Which exact state and timing conditions explain why the symptom may not occur
  on every soft deletion?

## Cleanup

- No project worktrees or branches have been created yet.
