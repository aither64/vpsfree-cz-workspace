---
lifecycle: active
---

# 2026-10-17-confctl-rust-rewrite-plan

## Status

- Phase: planning delivered. Both inventories and the Rust implementation design
  are complete and accepted. Session remains open for follow-up.
- No application implementation, application tests, independent review,
  deployment or integration occurred. No feature branches were created.
- Identity verified by `dev-session current` and both environment markers.
- Retained Full-team roster verified; architect and implementers have saved
  workspace-write access. Reviewer remains unassigned for this planning task.

## Phase checklist

- [x] Scope and ownership established.
- [x] Ruby/Go behavior and site extension inventories completed.
  - [x] Site inventory complete and accepted as source evidence.
  - [x] Core/Go inventory complete and accepted as source evidence.
- [x] Rust architecture and extension migration design completed.
- [x] Lead acceptance inspection and planning handoff completed.

## Next actions

- Future implementation starts with M0: executable Ruby parity fixtures for 29
  built-in actions, site hooks/command and four helpers. Then follow M1–M5 in
  the design; this turn fulfills the planning request only.
- No blockers to the planning deliverable. Material implementation risks are
  parser/exit quirks, inline PTY behavior, vpsAdmin authentication parity and
  mixed-version helper/rollback behavior. Each has an explicit acceptance gate.

## Documentation

- [Completed architecture and migration plan](design.md), owned by architect0.
- [Core and Go behavior inventory](inventory-confctl.md), owned by implementer0;
  complete 29-route/option matrix, behavior, timing, helpers, packaging and test
  inventory accepted. Exact execution behavior still needs future fixtures.
- [Completed site extension inventory](inventory-extensions.md), owned by
  implementer1. Includes script/API mapping, hook ordering, packaging boundary
  and differential acceptance scenarios; source inspection only.

## Repositories

- Canonical `repos/confctl.git` and `repos/vpsfree-cz-configuration.git` are
  read-only inputs. No feature worktrees or branches created or registered.
- Earlier Go session is a read-only historical reference explicitly requested
  by the user; no work is transferred or altered there.

## Commands run

- `dev-session current`; environment identity check; retained team list and
  assignments via `dev-session team assign --message-stdin`.
- Read workspace routing, session, project, Git, lifecycle, documentation,
  verification and commit procedures and documentation/handoff skills.

## Results

- Investigation packages assigned to both retained implementers; architect
  owns design. No implementation, builds, independent review or deployment.
- Initial scope checkpoint committed as `1cdb0062`; shared workspace declares
  no hook framework and has no active hooks. Unrelated changes preserved.
- Architect proposed executable extensions, typed events, one process/terminal
  owner and preservation of existing on-disk and remote contracts; accepted as
  directions for the plan, subject to inventory reconciliation.
- Team report tool is absent. Architect's CLI reporting fallback was denied on
  the out-of-workspace transition lock under saved workspace-write access.
  Resolved for this task through assigned in-workspace artifacts read and relayed
  by lead. Source/design writes and session identity remain available; retained
  member settings were not changed.
- Site inventory complete: exactly two confctl user scripts at configuration
  `3ae43f560ec7c0e6400322a5777118232dcdb26b`. Its confctl pin is
  `7bee58a52372b95c2198ce3f2a719807a3c2c66b`; local confctl master is
  `cc40679d267165aecfa569128438bb55fe910268`. These local immutable anchors do
  not assert deployed or latest remote status. Critical requirements relayed to
  architect: pre-evaluation kernel update, live PWD/root association, nonfatal
  host failures, explicit/hooked selection differences and preserved files.
- Core inventory complete: 29 built-in action leaves, negative/alias/default
  options, command results, terminal/prompt behavior, state, all four Ruby
  helpers, package/tests/workflow inventory and Go timing golden contract.
  Go reference `009ca80cfca39634fc72e38b4002108a94194796` is published,
  unmerged and not deployed per its historical state; no verification reused
  as current-session runtime proof.
- Architect completed protocol/dependency/CI/milestone sections and reconciled
  both inventories. Lead accepted all requested areas: full CLI results,
  similar live TUI/progress/colors, maintained dependencies, site extensions,
  idiomatic Rust, GitHub checks, Go timing, full Ruby runtime/helper removal and
  compatibility/recovery. Planning uncertainties are explicit future gates.
- Mandatory final review not triggered: this is routine planning and source
  investigation only, with no implemented substantive deliverable or project
  documentation/configuration changes. Reviewer remains unassigned.
- Artifact validation checked source commit existence, local links, required
  topic coverage, completion markers, whitespace and portal registration. No
  runtime, crate build, package closure or production validation is claimed.

## Open questions

- Exact GLI errors/exit codes/parser edge cases need future executable fixtures.
  Source inventory is evidence for the plan, not runtime parity validation.
- Ratatui inline/scrollback/resize behavior and crate toolchain compatibility
  require an early Rust implementation spike before committing to UI internals.

## Cleanup

- No lifecycle action requested. Leave session open and preserve all refs.
- Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-17-confctl-rust-rewrite-plan/
- Evidence/source scratch copies under this session's `/tmp` prefix were not
  used as worktrees and contain no owned running test processes.
