---
lifecycle: active
---

# Network availability and IPv4-left counter

## Status

Phase: implementation preparation (2026-10-06). User authorized the final plan.
No application changes or deployments yet.
Session identity verified against `dev-session current`, both environment markers,
and trusted thread binding. Architect `architect0` assigned design investigation;
saved access is workspace-write, purpose design, ready, Astra/xhigh.

## Phase checklist

- [x] Verify session identity and retained roster.
- [x] Establish proposal-only scope and affected repositories.
- [x] Trace counters and allocation semantics; produce architect proposal.
- [x] Consolidate findings and suggested solution for user.
- [ ] Reconcile architect brief and establish owned feature worktrees.
- [ ] Implement backend, both UIs and configuration channel pins.
- [ ] Quick checks, hooks and committed whole-branch inventory.
- [ ] Independent final review.
- [ ] Long verification and affected-host builds.
- [ ] Handoff verified branches; production activation/merges remain separate.

## Repositories and evidence

Owned worktrees now exist under worktrees/2026-10-05-network-ipv4-left-counter/:
- vpsadmin: branch 2026-10-05-network-ipv4-left-counter,
  base c4d9b50f4e74417ed37b5fe410cca3ec1addc24e.
- vpsadmin-webui: branch dev/network-enabled (repository branch exception),
  base 02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51; default main corrected in manifest.
- vpsfree-cz-configuration: branch 2026-10-05-network-ipv4-left-counter,
  base cde8451718d75929c931db63626b48f7de92fc4f.
V/config git worktree creation completed but post-checkout hooks failed (unsigned
Overcommit config in V; missing bundle in config). Helper recorded the worktrees;
setup must be repaired within Nix before any source commit. No hooks bypassed.
- vpsadmin default source: `b4ef8535a629ee8c9cd753afecdb05e0895d0eea`.
- vpsadmin-webui source: origin/main
  `aa2f60b89df65d2f987be48784ed42bab7010833`.
- Both index pages consume Cluster::PublicStats.ipv4_left.
- Backend currently counts unowned, unassigned rows in public_access IPv4
  networks, without a network enabled state or allocation-policy filtering.
- Counter also omits location selection policy, network purpose and IP resource
  reservations; these can further separate inventory from usable capacity. No
  IP cooldown column/predicate was found by architect inspection.
- Separate frontend bare HEAD has no local main target; use existing origin/main
  read-only. No shared repository metadata was changed.

## Results and limits

Source inspection only. Production data and deployed revision not inspected.
Public/private exclusion currently relies on network role, not numeric CIDRs.
Initial plan/state committed as `374d6611` on workspace master; unrelated
changes preserved and no declared workspace hook framework found.
No tests run; no completed substantive implementation deliverable for final review.

## Proposed solution and next action

See [architect proposal](design.md) for revision/path evidence, operation matrix,
concurrency/continuity boundaries, compatibility, rollout, acceptance criteria,
and a read-only per-network diagnostic query (prepared, not executed).

- Add Network.enabled NOT NULL default true; admin-only updates in both UIs.
- Enforce disabled state for new automatic/explicit allocations, detached-owned
  reuse, ownership transfers and owned registration. Retain visibility, existing
  service, release/rollback and trusted same-allocation continuity operations.
- Shared PublicStats count: unowned, unassigned, enabled public IPv4 inventory,
  unreserved; public/private classification uses Network.role only. Preserve allocation-row count;
  do not infer retirement from location/purpose/maintenance settings.
- Upgrade every allocator/writer before disabling pools. Older writer rollback
  ignores policy and is unsafe while disabled networks exist.

Next action: reconcile design with the accepted role-only decision and both
channel pins, then assign implementer0 from the verified roster, implement and
commit with quick checks,
then independent final review before longer verification. Before production
retirement, confirm deployed revision and per-network contributions read-only,
and obtain the explicit list of networks to disable.

Proposal accepted for presentation by lead after checking shared-counter/model
source evidence. No independent final review assigned: this is routine planning
and investigation, exempt from automatic review. No code, tests or deployment.

## Documentation and cleanup

Plan and [proposed design](design.md) are session-owned planning records; project docs will
be updated with implementation if requested. Keep this session open. No cleanup.

Stable session portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/

## 2026-10-06 resumption

Identity reverified with current from the bound session directory. Both shell
markers are absent; trusted thread binding exactly matches. A root-directory
current lookup initially returned no session; no mutation was made until resolved.
Retained roster unchanged; architect0 assigned brief reconciliation. Canonical
source fetches started; separate frontend origin lacks a fetch refspec, so main
is fetched explicitly into origin/main rather than changing shared settings.
Initial implementation planning refresh will be committed before source work.
