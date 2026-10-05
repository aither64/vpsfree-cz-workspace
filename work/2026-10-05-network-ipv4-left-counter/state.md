---
lifecycle: active
---

# Network availability and IPv4-left counter

## Status

Phase: investigation and proposal. No application changes or deployments.
Session identity verified against `dev-session current`, both environment markers,
and trusted thread binding. Architect `architect0` assigned design investigation;
saved access is workspace-write, purpose design, ready, Astra/xhigh.

## Phase checklist

- [x] Verify session identity and retained roster.
- [x] Establish proposal-only scope and affected repositories.
- [ ] Trace counters and allocation semantics; produce architect proposal.
- [ ] Consolidate findings and suggested solution for user.
- [ ] Implementation, local verification, independent review and deployment:
  future work if requested.

## Repositories and evidence

No feature branches or worktrees created or registered.
- vpsadmin default source: `b4ef8535a629ee8c9cd753afecdb05e0895d0eea`.
- vpsadmin-webui source: origin/main
  `aa2f60b89df65d2f987be48784ed42bab7010833`.
- Both index pages consume Cluster::PublicStats.ipv4_left.
- Backend currently counts unowned, unassigned rows in public_access IPv4
  networks, without a network enabled state or allocation-policy filtering.
- Separate frontend bare HEAD has no local main target; use existing origin/main
  read-only. No shared repository metadata was changed.

## Results and limits

Source inspection only. Production data and deployed revision not inspected.
Public/private exclusion currently relies on network role, not numeric CIDRs.
No tests run; no completed substantive implementation deliverable for final review.

## Next action

Integrate architect findings and recommend disabled-network semantics, counter
criteria, compatible rollout and meaningful verification.

## Documentation and cleanup

Plan and proposed design are session-owned planning records; project docs will
be updated with implementation if requested. Keep this session open. No cleanup.
