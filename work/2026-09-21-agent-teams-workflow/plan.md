# Real persistent Codex teams

## Goal

Replace the virtual managed-team implementation with independent persistent
Codex threads that can be controlled consistently from the portal and the
terminal. The initiative keeps the existing session tmux layout: one attached
lead conversation per development session. Specialist threads remain headless
until assigned work and retain their own history for the lifetime of the
session.

## Design

- `lead` is the permanent root thread and the only member resumed in the
  session's tmux `dev` pane. `dev-session attach <slug>` continues to attach
  that tmux session unchanged.
- Each other member has a real App Server thread and a stable compact address:
  `architect0`, `architect1`, `implementer0`, `reviewer0`, and custom-role
  equivalents. Addresses are never renumbered or reused.
- The portal and `dev-session team` use one package-owned team runtime and the
  same durable roster. There is no separate agent simulator, message broker,
  database, or background scheduler.
- `dev-session team assign --to architect0` submits a correlated App Server
  turn to that member. A member reports to `lead` through the same assignment
  command. There is no separate broker, queue, report, question, or progress
  protocol; a busy target uses App Server's ordinary turn/steer behavior.
- A new member receives a real configured thread but no model turn until its
  first assignment. Member model and reasoning-effort settings apply to its
  next turn; a single assignment may override them. Long builds and tests use
  a fresh Luna/low watcher utility and never appear in the roster.
- Team presets are editable starting points: `Solo — lead`, `Delivery — lead ·
  implementer0 · reviewer0`, and `Full team — lead · architect0 ·
  implementer0 · reviewer0`. UI labels use human-readable text without
  underscores.

## Phases

1. Complete — remove managed virtual-team restrictions and restore normal root
   conversation access. Existing virtual state is ignored while preserving the
   root conversation and tmux identity.
2. Complete — implement the shared roster/runtime and terminal commands:
   list, preset, add, configure, remove, and assign. Creation and fork reserve
   an address before thread creation and retain incomplete records for safe
   retirement; model and effort defaults are applied to the next assignment.
3. Complete — replace the creation-time virtual selection and session Team UI
   with formatted presets, roster controls, model/effort controls, add/remove
   actions, direct assignment, and roster-address-only transcript inspection.
4. Complete — synchronize fork, archive, revive, delete, and auto-archive
   with member threads. The root lifecycle journal retries the roster operation;
   the roster itself records member state. There is no separate member-operation
   journal or automatic repair of a failed App Server call.

## Compatibility and deployment

This is a forward-only aitherdev cutover. Existing virtual-team records have
no retained member value: keep only their root conversation and expose an
empty editable roster after upgrade. Do not preserve old selection, override,
or virtual-member state. The session filesystem, tracking records, worktrees,
tmux identity, root thread, and normal unmanaged lifecycle behavior remain
intact. The workspace application is deployed from its user profile; no
configuration-master integration or rollback support is required.

## Verification and review

- Test portal/CLI parity, root tmux attachment, roster-local assignment,
  addresses, model/effort defaults, removal, and incomplete-create recovery.
- Test full-team fork, archive/revive/delete, and auto-archive through the
  existing lifecycle suite.
- Exercise the public workspace alias in a browser: lead conversation access,
  `architect1` creation, delegation, activity, and result delivery.
- Use fresh Luna/low watchers for every long or uncertain build, test, or
  deployment operation. Run one consolidated Sol/xhigh review after all
  implementation phases, then integration and deployment checks.
