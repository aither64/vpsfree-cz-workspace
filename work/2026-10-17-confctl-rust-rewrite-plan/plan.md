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

2026-10-18 revision: use built-in runtime-kernel collection and netboot
inventory generation with opt-in typed Nix settings. Remove the proposed generic
extension framework, wire protocol, SDK and separate site executable. Architect0
completed and lead accepted the revised design; source inventories retain
historical observations and explicitly superseded mechanism recommendations.

The completed [design](design.md) is the implementation plan. Its recommended
sequence is:

1. Capture executable Ruby compatibility fixtures for all 29 core command
   actions, site commands/hooks and four helpers (M0).
2. Establish Rust command/domain types, supervised processes, events, timing and
   typed settings for built-in kernel/netboot features (M1).
3. Port Nix/input/state adapters, live presentation and the built-in features using
   independent file packages (M2).
4. Complete operations, remote helpers and vpsAdmin data generation (M3).
5. Switch packaging, documentation and GitHub format/lint/test workflows (M4).
6. Complete differential, PTY, mixed-version, VM and operator acceptance before
   preparing cutover with a retained rollback environment (M5).

The design defines dependencies, file boundaries and acceptance checks per
package. It recommends Tokio, Ratatui/Crossterm, clap, Serde and thiserror, with
toolchain/MSRV/license and inline-terminal validation before locking versions.

Architect-owned Rust design informed by two independent source inventories.
Use exact source revisions and distinguish observed behavior from proposals.
Deliver an implementation sequence with ownership boundaries, dependencies,
acceptance criteria, compatibility gates, and verification requirements.

| Owner | Result | Acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| implementer0 | `inventory-confctl.md` | Commands, observable results, TUI, Go elapsed-time semantics, tests and packaging anchored to sources | Read-only source inspection |
| implementer1 | `inventory-extensions.md` | Every site Ruby script mapped to behavior and migration requirements; historical mechanism proposals superseded | Read-only configuration and confctl inspection |
| architect0 | `design.md` | Idiomatic Rust architecture, maintained crate candidates, built-in kernel/netboot features, migration, CI and milestones | Both inventories; source reconciliation |
| lead | Plan/state, acceptance inspection, portal handoff | All user requirements traceable to concrete design and next actions | Architect report and evidence |

All three assigned source/design packages are complete and accepted by the lead
as a planning deliverable. Verification is source/artifact validation, not proof
that a Rust implementation passes the proposed checks.

## Decisions

- Rust replaces Ruby as the intended implementation language.
- CLI command meaning and result are compatibility requirements. Terminal
  appearance can change while retaining live output, progress, color and format.
- Adopt the useful Go elapsed-time behavior after documenting its exact contract.
- This request authorizes planning, not implementation or modification of the
  earlier Go initiative. Leave that initiative and all project refs unchanged.
- Revised direction: no user extension support. Core owns kernel collection and
  netboot inventory generation as ordinary domain services, with typed settings
  for opt-in automatic stages and output paths. No generic task/hook DSL.
- Proposed settings: `confctl.runtimeKernels.{enable,stateFile,refreshBeforeDeploy}`
  and `confctl.netbootInventory.{enable,outputFile}`. Both features default off;
  enabled paths are explicit relative strings. Keep the existing files and
  `runtime-kernels update` command; other sites gain no default probes/writes.
- This removes extension infrastructure, not feature maintenance. New custom
  behavior requires an ordinary confctl feature or separate tooling. Site
  migration/rollback pairs the tool pin, settings and script removal/restoration.
- Site migration covers `scripts/discover_netbootable.rb` and
  `scripts/runtime_kernels.rb`. Preserve generated `cluster/netbootable.nix`,
  mutable `configs/node/kernels.json` and the latter's pre-build update ordering.
  Independent Ruby service/tooling in the configuration repository is outside
  the confctl runtime removal scope.

## Compatibility and deployment

The design must cover persisted state and GC roots, CLI output and exit codes,
Nix evaluation/build interfaces, remote helpers and protocols, mixed-version
operation, site hook ordering and errors, deployment order and rollback. Record
inapplicable database/API/Terraform concerns explicitly. Avoid a fleet-wide
coordinated update unless evidence requires it. No deployment in this session.

## Documentation

- [Rust architecture and migration design](design.md): main implementation brief.
- [Core and Go behavior inventory](inventory-confctl.md): complete built-in route
  and option matrix, source anchors, timing and runtime verification gaps.
- [Site extension inventory](inventory-extensions.md): two-script migration map,
  ordering and state contracts, packaging and differential acceptance cases.

Readers are confctl developers and site operators preparing the rewrite.
The session design is the proposed implementation brief; evidence inventories
hold source details. Future supported contracts and upgrade instructions belong
in the owning repositories when implemented, not solely in these session notes.

## Testing plan

Planning validation checks source anchors, extension coverage, requirement
traceability, and phase acceptance criteria. Specify future unit, differential,
PTY, process-cancellation, built-in feature/configuration, Nix and VM checks plus GitHub
format/lint/test workflows. Do not run builds or integration tests for a plan.
Routine planning and investigation do not trigger mandatory final review.
