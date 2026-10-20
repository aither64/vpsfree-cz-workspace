---
lifecycle: active
---

# Kernel hang investigation

Current phase: provenance and read-only evidence collection. No source changes,
builds, deployments or confirmed causes.

## Phase checklist

- [x] Verify exact same-session identity and retained team access.
- [x] Assign architecture, patch inventory and central-log packages.
- [ ] Establish exact kernel/custom patch provenance and incident window.
- [ ] Complete independent source analysis of changed custom patches.
- [ ] Reconcile causal evidence and publish findings.

## Backlog

| Owner | Result | Acceptance / checks | Dependencies |
| --- | --- | --- | --- |
| architect0 | design.md and causal synthesis | Concrete source chain or verified failure; explicit uncertainty | Inventory and logs |
| implementer0 | patch-inventory.md | Exact refs, complete custom semantic delta | Canonical bare repositories |
| implementer1 | log-evidence.md | Bounded relevant excerpts, incident and kernel timeline | Read-only central log access |
| implementer2/3/4 | Independent source audit packages | Paths and triggers checked against both versions | Architect partition after inventory |
| lead | Reconciled findings and tracking | Assess all reports against user's confidence standard | All packages |

## Evidence and constraints

- dev-session current and both DEV_SESSION environment markers match
  2026-10-20-kernel-check at /home/aither/workspace/ai/vpsfree.cz.
- Same-session roster retained architect0, implementer0..4 and reviewer0;
  implementation members have saved workspace_write access.
- Central logs accessible as root@log.int.prg.vpsfree.cz; node24 directory:
  /var/log/remote/cz.vpsfree/nodes/prg/node24. Incident window pending.
- Read-only canonical repos: repos/vpsadminos.git, repos/linux.git; configuration
  may be consulted for deployment provenance. No feature branches/worktrees.
- No automatic final review for investigation/findings/evidence alone. No long
  tests planned. Any substantive deliverable or long test will use required gates.

## Next action

Obtain custom patch delta boundaries and incident window; assign independent
source paths to the three added implementers. Keep session open.
