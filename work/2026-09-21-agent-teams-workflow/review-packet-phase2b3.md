# Phase 2B.3 mandatory review packet

## Requested outcome

Activate creation of team-bound sessions from portal New, plan-to-new and the
direct CLI. Resolve the immutable selected team and catalog before creating the
root, publish retained state before the first turn, and retain launch evidence.
Old schema-1 sessions remain usable as unmanaged legacy sessions without a
migration. Managed lifecycle operations stay unavailable until their durable
dispatcher is implemented.

## Scope

- Initiative: `2026-09-21-agent-teams-workflow`.
- Owning implementation: `dev-workspace`, feature worktree
  `worktrees/2026-09-21-agent-teams-workflow/dev-workspace`.
- Reviewed range: `285e998f4aae703f1d6b639a7bf23f7e111a660c..f2754b8fdc5574ca4cc99eb5a98508fc185818fe`.
- Dependency: published `codex-web` feature head
  `52b8ca6e9ddf2175d1a9163996fa9073f9c1882d`, pinned in the generic Go and
  Nix inputs. No other repository has uncommitted implementation in this
  phase.

The single commit bundles portal, CLI, host and session behavior with their
tests, documentation and reproducibility pins because they implement one
crash-recoverable creation protocol; splitting them would leave a caller,
stored schema or pinned dependency without its required counterpart.

## Design and boundaries

- Managed creation uses a strict schema-2 receipt and retained team state;
  creation is bound to the current immutable catalog and chosen team.
- A managed root is published before the first initial-send attempt; replay and
  launch evidence are therefore recoverable after interruption.
- Schema-1 remains the supported legacy reader/recovery/conversation/lifecycle
  path. There is no offline migration, adoption, retasking or changed
  model/effort for an existing session.
- An unmanaged-source fork remains legacy; a managed-source fork and managed
  archive, revive, delete and automatic archive fail closed. Durable managed
  provenance/dispatch is deferred to Phase 2C.
- Aitherdev is the only deployment. It is a forward-only user-profile update;
  configuration/default-branch integration and deployment are not part of this
  review.

The durable rationale is in `plan.md` and
`design-phase2b3-managed-creation.md`; supported portal/host behavior is in
`dev-workspace/docs/workspace-portal.md`.

## Evidence before review

- Focused Go agent-team, session, portal-command and web packages passed.
- Stale-catalog HTTP boundary and Chromium creation acceptance passed.
- Final Ruby host suite passed: 91 runs, 512 assertions.
- Final Ruby dev-session suite passed: 325 runs, 3,514 assertions and 12
  intentional skips.
- Final pinned package build passed:
  `nix build .#packages.x86_64-linux.default --no-link`.

All long/uncertain checks were run and monitored by fresh Luna/low utilities.
Complete command and log evidence is in `verification-phase2b3.md`.

## Review classification and lanes

Risk is **high**: this changes persisted session/receipt schemas, starts Codex
threads, controls host package transitions and changes a browser/CLI contract.
Review at `xhigh` covers General, Architecture and repetition, Scope and
proportionality, and Risk and compatibility. The user prohibited gpt-6-astra,
so fresh independent reviewers use `gpt-5.6-sol` at `xhigh` instead.
