# HaveAPI release versioning final review packet

Status: ready for final independent review. All intended changes are committed
and quick checks pass; longer integration checks and feature publication wait.

## Request and accepted boundary

The user reported master 0.30.0 despite published 0.31 releases, asked for an
investigation and solution, then corrected the version policy: master contains
the latest major/minor with patch zero, while release branches own patch versions.
The user subsequently said "implement it". Implement the accepted policy in
HaveAPI only; no default-branch integration or package publication is authorized.

Acceptance:

- All maintained master identities/constraints synchronize to 0.31.0; preserve
  published release branches/tags/packages. Restore missing release changelog
  entries and the released maintenance-fixture isolation fix.
- Prepare future major/minor versions on master before cutting haveapi-X.Y;
  subsequent patch version changes stay on the release branch.
- Release validation reads fresh remote master version, validates numeric X.Y.Z,
  requires patch zero and compares numeric major/minor pairs. Master 0.31.0 must
  permit candidate 0.31.2; stale 0.30.0 and master 0.31.1 must fail; higher
  major/minor master remains valid. Existing tag/source/branch checks remain.
- Actual master quick metadata checks, including detached CI, enforce patch zero;
  release branches still permit nonzero patches. VERSION-only changes trigger
  the relevant existing workflow.
- Preserve original tagged helpers/artifacts for recovery of existing releases.
  No retagging, rebuilding or republishing accepted versions. No new subsystem.

## Ownership and context

Session: 2026-10-28-release-versioning-audit.
Workspace: /home/aither/workspace/ai/vpsfree.cz.
HaveAPI worktree: worktrees/2026-10-28-release-versioning-audit/haveapi.
Feature branch: 2026-10-28-release-versioning-audit; target: origin/master.
Plan/state/design: work/2026-10-28-release-versioning-audit/.
Initial base: 2f5156262baaf137800c17a9321e617c2b5df1d5.
Author: retained implementer0; architect0 authored the brief.
Reviewer: retained reviewer0, gpt-6.1-sol/xhigh, read-only, independent.

Read workspace AGENTS.md, mandatory routing procedures, HaveAPI AGENTS.md and
its development/release instructions; read performance.md for the fixture port.
Use /home/aither/.codex/skills/mandatory-change-review/SKILL.md and all four lane
references: general, architecture/repetition, scope/proportionality,
risk/compatibility. Review directly; no nested reviewer/subagent.

Risk classified conservatively high because release validation gates irreversible
publication and must preserve accepted-release recovery. Implementation itself is
bounded, adds no publishing destination and performs no publication/deployment.
No runtime API/protocol, persistence, fleet configuration or consumer pins change.
HaveAPI owns release tooling and package identities. Its existing release CLI,
Makefile and GitHub workflow consume this validation; maintained language package
metadata consumes the coordinated version. This is no new cross-project API.

## Final series and evidence

Base: `2f5156262baaf137800c17a9321e617c2b5df1d5`.
Head: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
Complete series in dependency order:

1. `29fae9e00bdc0f340196cda953c5c7b2408aec21` — servers/ruby: isolate
   maintenance lineage test versions. Port released `c9124da1` with master's
   optional Rust constant setup retained; no runtime performance-contract change.
2. `ae909bef9ee27d01d5497f4b511e27b72f6dd60e` — version: synchronize
   master to 0.31.0. All 17 maintained metadata/constraint paths and restoration
   of previously released changelog sections; generated tracked JS version only.
3. `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0` — release: enforce master
   version policy. Validator, CLI, workflow, focused specs and owning release docs.

Final diff: `final.diff` next to this packet; 24 files, +375/-51. One consolidated
version-update stream; no action, external dependency or Nix input pin updates.
Fixture message was amended before finalization; no obsolete followup remains.
No migrations or new schema/compatibility paths exist. The fixture source commit
was previously released as part of v0.31.0; its port preserves the original
historical maintenance contract, not literal release-commit ancestry on master.
No new branch commit has been released, deployed or externally consumed.

Fresh fetch and remote proof still show master at the exact base; tracked
worktree is clean and exact comparison is saved through dev-session. Release
branch and v0.31.2 remain at `819bba5110e089465535ecd71ca2eb37a7d39caa`.

Detailed commands/results and hook evidence: `implementation-evidence.md`.
Dependency preparation succeeded. In the final 42-second quick batch:
65 metadata/policy examples and 18 lineage examples pass; four changed Ruby files
pass RuboCop; `make release-check` passes authored metadata and prepared inputs.
Committed `check-clean`, `check-clean --master` and `make release-check` also pass.
Logs: `final-quick.log`, `committed-check.log`; hook logs:
`fixture-amend.log`, `version-commit.log`, `policy-commit.log`.
The initial lineage NameError and its diagnosed optional-constant ordering cause
are retained in `lineage-quick.log`; the corrected run passed. No hook bypass.
Workflow YAML and VERSION path selection checked; imported action refs verified
against official current upstream versions, with no ref changes.

Documentation: `doc/agent-instructions/releases.md` owns the master-first
major/minor process, release-only patches, detached context, ref freshness and
original tagged recovery. Existing release notes are restored without editorial
changes. Lead applied user-facing-writing/English guidance to the restored notes,
new errors and policy prose and found no necessary wording changes.

Please record findings by severity and lane in `review.md` beside this packet,
with explicit whole-series obsolete-history, repeated-update and migration
conclusions. Residual checks: full release-tool suite and appropriate broader
server/performance checks/build-only CI follow your review. Do not launch long
checks yourself or mutate the repository.
