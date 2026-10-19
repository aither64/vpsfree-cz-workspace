# Final review packet: automatic coordination storage cleanup

Read top-level AGENTS.md and its applicable routing procedures, each affected
repository AGENTS.md, ~/.codex/skills/mandatory-change-review/SKILL.md and all four
lane references: general, architecture, scope, risk. Review directly, read-only;
do not delegate or edit application code. The local operator is trusted as stated
in dev-workspace/AGENTS.md. Protect ordinary concurrency, ownership, recovery and
external inputs; do not invent a hostile-root security boundary.

## Requested outcome

The user asked what occupies aitherdev disk, then requested automatic cleanup of
workspace snapshots and coordination checkouts, and explicitly allowed tracking.
Read plan.md, design.md and state.md in this directory. No master integration or
production cleanup is authorized yet; the feature is prepared for review/rollout.
No retained reviewer/valid native lead thread exists for this initially external,
threadless session. Installed default lead_reviewed catalog selects Astra/xhigh
for this fresh independent reviewer; catalog ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376.

## Exact final branches and complete history

All paths are under /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-coordination-storage-cleanup/.

- dev-workspace: base 8385699aabcc2cfc74b585ca653a4658ff3eef75,
  head 957dc29fce880790f49921e59f6e5f88baa5e348.
  5cac3f8eda428f837b4789de1130704394022504: collect finished integration scratch
  and worker roots, tests, owning operations docs.
  957dc29fce880790f49921e59f6e5f88baa5e348: bound workspace profile generations,
  tests and owning operations docs. Profile-history policy is separately reviewable.
- workspace: base 92a9a8d3c88e91b81d7a752fc29d1b807ed9d02f,
  head e295c2200895d0d56bd9f8b3582fdce6d3eac451.
  One commit selecting the published exact runtime through its existing nested
  vpsfree-dev-workspace/dev-workspace input; extension and other nodes unchanged.
- vpsfree-cz-configuration: base 95a8b88d383c177fc65bf67d51c901a69c0b2847,
  head dd2d0b4f17e6ee2a1df614fe45f623c7dfe56262.
  One confctl-generated dev-workspace/devWorkspace channel pin to the same runtime.

Inspect each complete base-to-head series and diff. No superseded implementation
commits remain; no repeated dependency-update stream exists within either consumer
branch. Generated configuration commit text is intentionally retained verbatim.
There are no SQL/schema migrations; no migration has been merged, released,
deployed or externally consumed. Optional mutable integration-journal bookkeeping
is additive and is not a versioned SQL/schema migration. No feature is deployed.

## Contract and acceptance

Reuse the existing five-minute Collector, profile-transition exclusion, locks,
reference marking, process checks and Git worktree removal. Collect only known,
clean, detached completed integration scratch; preserve live dependencies, holds,
dirty/foreign/unknown layouts and unfinished runs. Before Git removal persist exact
pending path/common directory/head in additive payloadGcPending; retry even if the
directory has disappeared. Old source retention.json stays unchanged. Older
integration readers preserve this optional field and older collectors leave it
untouched. Keep journals, compact evidence and feature refs.

Collect only known worker-root UUID/digest layouts with idle notification locks
and services or completed/idle integrations. Pending notification payloads retain
their independent dependencies; the next dispatch roots its selected worker package.
Prune only recognized workspace Nix profile generations via nix-env, under the
existing transition exclusion and exact profile identity rechecks. Keep selected,
one predecessor, generations newer than a legacy rollback, and live package
references. Leave Codex generation roots, other user/system profiles and Nix store
path deletion to their owners. Runtime workspace rollback is already unsupported.
Removed disposable data cannot be restored by software rollback.

Non-goals: user feature-worktree deletion, VM/cluster/KB cleanup, Git history
rewrites, a new retention scheduler, or restructuring all archive content and
flake source boundaries. The measured multiplication remains relevant to live
work, but completed copies and stale package references must no longer leak.

## Quick verification

- Ruby syntax and git diff --check pass.
- Commit-one focused suite: 26 tests, 120 assertions, zero failures.
- Complete focused suite: 30 tests, 143 assertions, zero failures, about 25 seconds.
- A first fixture run was postponed by an unrelated real host preparation; fixture
  mode now excludes external preparers, matching existing systemd fixture isolation,
  with a separate test for the production preparation guard decision.
- Config checkout retried in its Nix environment after dependency setup; declared
  hooks are installed/signed and generated commit passed Nixfmt and commit hooks.
- Workspace and configuration semantic lock checks each change exactly one runtime
  node; both select 957dc29. Deployment contract is run before reviewer launch.

Long packaged checks/native profile exercise have deliberately not started yet.
Risk is high: destructive cleanup, profile retention and partial-operation recovery.
Use all four lanes and conclude explicitly on whole-branch history, migration
lineage, repeated update streams, compatibility and residual test gaps.

Return findings with severity, lane, file/line and concrete scenario, followed by
whole-branch conclusions. Save the report as review.md in this tracking directory.
