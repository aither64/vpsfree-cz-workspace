# HaveAPI 0.30.2 backport and release

## Goal and scope

Backport all applicable improvements from HaveAPI master to the maintained 0.30
series and publish release 0.30.2. Only HaveAPI project code is in scope; no
consumer pin updates or production deployments are requested.

## Approach and ownership

- Architect0: inventory master versus 0.30, assess compatibility and release
  procedure, write design.md with implementation boundaries and verification.
- Implementer0: backport functional changes, tests and technical documentation
  from the approved design; own commits, checks and review fixes.
- Implementer1: independent release preparation/verification package identified
  by the architect; serialize overlapping edits and Git operations.
- Reviewer0: independent final committed-deliverable review after quick checks,
  including complete history and migration provenance, before long checks.
- Lead: tracking, acceptance, user-facing writing and release coordination.

## Compatibility and deployment

Preserve the 0.30 public contracts and component version compatibility. Assess
persisted state, schema/migrations, Ruby dependencies, API/client/CLI contracts,
mixed versions and rollback before implementation. No system deployment is
planned. Determine whether every master change can safely enter a patch release;
record adaptations or any material incompatibility rather than silently omitting it.

## Release and integration

The user explicitly requests release 0.30.2. Determine the canonical 0.30 branch,
version/tag/package workflow and publication prerequisites. Do not integrate
master or other default branches without explicit repository/target approval.
Prepare and review all release artifacts before publication. Preserve feature refs
and leave this session open.

## Documentation

Readers are maintainers and HaveAPI consumers. Keep release notes and lasting
behavior changes in HaveAPI documentation; design, coverage, commands, release
receipts and temporary verification evidence belong in this session.

## Verification

Follow HaveAPI instructions and Nix environment; retain hooks. Inventory complete
source changes and backport coverage. Run focused quick checks and package/version
checks, commit intended deliverables, run independent final review, then longer
supported tests and CI through a fresh utility watcher. Verify published refs and
package versions after authorized publication.
