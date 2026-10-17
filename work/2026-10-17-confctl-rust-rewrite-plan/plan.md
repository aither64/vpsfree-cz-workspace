# 2026-10-17-confctl-rust-rewrite-plan

## Goal

In  session 2026-10-09-evaluate-confctl-rewrite-language, we are rewriting confctl to golang.

I'd like to rewrite it to rust instead. what I'm interested in:

- CLI commands must have the same meaning/result
- TUI should be similar, doesn't have to be exact. But preserve the live view, progress bars, colors and formatting.
- Use maintained dependencies where appropriate, e.g. terminal handling, progress bars, etc.
- Suggest a solution for user extensions, such as are in vpsfree-cz-configuration
- Use idiomatic rust, follow best practices. I choose rust for its robust type system, memory safety, etc.
- github workflows for running tests / code formatting
- I like the operation elapsed time improvement we're making in the golang version, that can be adopted

I'd like you to go over the project and create a plan to reimplement confctl and replace user scripts in vpsfree-cz-configuration with the new solution. Ruby code will be replaced with the new rust version.

## Affected repositories

- `confctl`: read-only investigation of Ruby implementation, Nix interfaces,
  tests, terminal behavior, and the Go experiment referenced by the user.
- `vpsfree-cz-configuration`: read-only investigation of site extensions and
  packaging; plan their replacement alongside the Rust implementation.
- This workspace: planning artifacts only. No application implementation,
  production operations, branch integration, or changes to the Go session.

## Approach

Architect-owned Rust design informed by two independent source inventories.
Use exact source revisions and distinguish observed behavior from proposals.
Deliver an implementation sequence with ownership boundaries, dependencies,
acceptance criteria, compatibility gates, and verification requirements.

| Owner | Result | Acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| implementer0 | `inventory-confctl.md` | Commands, observable results, TUI, Go elapsed-time semantics, tests and packaging anchored to sources | Read-only source inspection |
| implementer1 | `inventory-extensions.md` | Every site Ruby extension/hook mapped to behavior and migration requirements | Read-only configuration and confctl inspection |
| architect0 | `design.md` | Idiomatic Rust architecture, maintained crate candidates, extension protocol, migration, CI and milestones | Both inventories; source reconciliation |
| lead | Plan/state, acceptance inspection, portal handoff | All user requirements traceable to concrete design and next actions | Architect report and evidence |

## Decisions

- Rust replaces Ruby as the intended implementation language.
- CLI command meaning and result are compatibility requirements. Terminal
  appearance can change while retaining live output, progress, color and format.
- Adopt the useful Go elapsed-time behavior after documenting its exact contract.
- This request authorizes planning, not implementation or modification of the
  earlier Go initiative. Leave that initiative and all project refs unchanged.

## Compatibility and deployment

The design must cover persisted state and GC roots, CLI output and exit codes,
Nix evaluation/build interfaces, remote helpers and protocols, mixed-version
operation, site hook ordering and errors, deployment order and rollback. Record
inapplicable database/API/Terraform concerns explicitly. Avoid a fleet-wide
coordinated update unless evidence requires it. No deployment in this session.

## Documentation

Readers are confctl developers and site operators preparing the rewrite.
The session design is the proposed implementation brief; evidence inventories
hold source details. Future supported contracts and upgrade instructions belong
in the owning repositories when implemented, not solely in these session notes.

## Testing plan

Planning validation checks source anchors, extension coverage, requirement
traceability, and phase acceptance criteria. Specify future unit, differential,
PTY, process-cancellation, extension-contract, Nix and VM checks plus GitHub
format/lint/test workflows. Do not run builds or integration tests for a plan.
Routine planning and investigation do not trigger mandatory final review.
