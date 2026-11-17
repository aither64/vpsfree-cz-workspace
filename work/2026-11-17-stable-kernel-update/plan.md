# Stable kernel update process and Linux 6.12.118

## Goal and scope

Create a reusable skill/process in vpsadminos for adding or replacing stable
kernels. Use it to carry the complete 6.12.117 downstream patch stack onto
upstream 6.12.118. Resolve every rebase conflict and prove preservation of every
patch, including any upstream-equivalent changes. Tune the process using the
actual execution. Repositories: vpsadminos and its Linux downstream source.

## Approach and decisions

Architect owns investigation and design.md. Implementers own the process and
kernel port packages, quick checks, commits, evidence and review fixes. Create
the process before using it for the port. Lead coordinates tracking, acceptance,
independent final review and publishing feature branches. Do not integrate any
remote default branch or deploy without separate explicit direction.

## Compatibility and recovery

Preserve the previous kernel and existing supported paths until conventions and
scope are verified. Account for all patch layers, source refs, kernel config,
ZFS compatibility and package hashes. No database or service protocol change is
intended. Record add/replace behavior, mixed-version operation, deployment and
rollback implications in design. No coordinated fleet update is intended.

## Documentation and readers

Kernel maintainers and coding agents need a discoverable process in vpsadminos,
with exact invariants and conflict handling. Execution-specific revisions,
correspondence evidence and results remain in this session's records.

## Verification

Inventory complete old and new downstream ranges. Check one-to-one patch
correspondence, independently inspect conflict resolutions and upstreamed
patches, and verify packaging/configuration/source hashes. Validate the skill
and any helpers, run repository hooks and quick checks, then independent final
review of committed changes before longer build/integration checks. Bound checks
by the risk they establish and use a watcher for uncertain/long verification.
