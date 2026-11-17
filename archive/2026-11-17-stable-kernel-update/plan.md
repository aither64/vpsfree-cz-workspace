# Stable kernel update process and Linux 6.12.118

## Goal and scope

Create a reusable skill/process in vpsadminos for adding or replacing stable
kernels. Use it to carry the complete 6.12.117 downstream patch stack onto
upstream 6.12.118. Resolve every rebase conflict and prove preservation of every
patch, including any upstream-equivalent changes. Tune the process using the
actual execution. The reusable process dynamically derives the complete patch
range from the latest applicable previous kernel, with no fixed patch list.
Updating the applicable stable/unstable selector and checking its resolved
identity are required parts of the process. Repositories: vpsadminos and its Linux downstream source.

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

## Accepted design and delivery boundary

See [design](design.md) and the single package table in [state](state.md).
P was committed first, then K began using it. R follows complete source/accounting.
All intended changes and quick checks precede mandatory final independent review.
Long checks target stable identity explicitly; no broad kernel test glob can
substitute for target coverage. No fixed patch list is part of the process.

## User-approved publication convention and integration

After CI passed, user authorized merging the work. OS integration target remains
staging. User clarified Linux is never merged and approved
`vpsadminos-<upstream-version>` branches, no automatic downstream tags, full
commit/archive pins. Final vpsadminos-6.12.118 now verified on the same source.
D3 adds the owning OS publication instruction plus a narrowly scoped workspace
Linux delivery exception, preserving other-repository merge rules and runtime
recovery/lifecycle boundaries. No runtime/schema/ledger change or session closure.
D3-OS and D3-W are independently owned/disjoint edits, checked and committed
before affected documentation review. Source/kernel inputs unchanged; reuse exact
CI receipts only within proven scope after clean OS rebase over unrelated exporter
baseline42baba6117bebcde3d04555a71377381df197925. Workspace policy changes stay
on its feature branch until explicit workspace-master integration approval.

## User addition: three configuration channels and merge

User requests vpsadminos update in vpsfree-cz-configuration for staging,
os-staging and production, then explicitly says "and merge it". Affected
repository defaultmaster integration approved; no deployment. Use confctl
channel-owned role updates only, preserve generated changelog messages and
expected transitive locks, all unrelated pins. Routine channel update requires
no new configuration docs/receipts. D4 architect mapping/check brief precedes
C4 implementer0 channel mutations; independent hook setup may proceed.
Merge preparation/checks/history review as appropriate outside claim; final
fresh target/ff-only/hooks/SSHpush/proof under one short repository claim.
Evidence in session C4-evidence.md, not tracked config-repo reports.

C4 delivered and merged as `15e3b9af` after graph/source/inventory checks and
independent history review. Fresh remote master proof and released claim are in
[integration](integration.md). No deployment requested or performed.
