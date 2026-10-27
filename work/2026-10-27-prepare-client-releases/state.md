---
lifecycle: active
---

# 2026-10-27-prepare-client-releases

## Status

- Phase: release investigation and design. Session/environment identity verified.
- No integration, registry publication, tag push or infrastructure deployment yet.

## Phase checklist

- [x] Verify session and retained team access/settings.
- [ ] Confirm release versions, procedures and publisher requirements.
- [ ] Prepare committed releases and pass quick checks.
- [ ] Independent final review and required longer checks.
- [ ] HaveAPI publication and verification; manual client publication handoff.

## Backlog and owners

| Owner | Result and acceptance | Dependency/checks |
| --- | --- | --- |
| architect0 | design.md with exact package/version/publisher fields and execution boundaries | Repository guidance and registry evidence |
| implementer0 | HaveAPI release package, committed changes and quick-check evidence | Accepted design; mandatory hooks |
| implementer1 | vpsAdmin client artifact and exact manual publication instructions | Accepted design; confirmed generator/version |
| lead | Tracking, release text, acceptance, approvals and operator handoff | Implementer reports and independent review |
| reviewer0 | Independent final review, full history and migration conclusion | Complete committed deliverable and passing quick checks |

## Next actions

- Accept the architect's design, then assign the independent execution packages.

## Documentation

- [Plan](plan.md); architect will add design.md. Exact publication instructions
  and outcomes will be linked here when prepared.

## Repositories

- Expected: haveapi and the owner of vpsadmin-typescript-client (under inspection).
- No session worktrees registered yet.

## Commands run

- `dev-session current`: exact slug matched both environment markers and trusted
  thread binding for `/home/aither/workspace/ai/vpsfree.cz`.
- `dev-session team list ... --as-is`: architect0 and implementer0/1 ready with
  workspace_write access; retained reviewer0 read_only, all settings preserved.

## Results

## Open questions

- Existing release automation, exact vpsAdmin client version, and pending publisher
  account prerequisites are being investigated by architect0.

## Cleanup

- Preserve unrelated shared working-tree changes and leave this session open.
