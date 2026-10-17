---
lifecycle: active
---

# 2026-10-17-archive-worker-authorization

## Status

Phase: implementation. Investigation complete: commit 5983365 applied archive
worker authorization arguments in run_delete while run_archive retained the
portal-only validator call. Installed package 6qx499s reproduces archive denial
and mistaken delete authorization with a fake runner. Failed worker exited at
2026-10-17T18:20:59Z, before creating an archive journal/snapshot.

- [x] Investigate and agree focused design.
- [x] Create separately owned threadless initiative and initial records.
- [ ] Implement authorization and packaged acceptance gate.
- [ ] Quick checks and committed independent whole-branch review.
- [ ] Packaged/CI acceptance.
- [ ] Align pins and deploy through coordinator.
- [ ] Deployed disposable acceptance and reported archive retry.
- [ ] Ready, awaiting explicit merge approval.

## Next actions

## Documentation

## Repositories

Intended feature branch: 2026-10-17-archive-worker-authorization in dev-workspace,
workspace and vpsfree-cz-configuration. Shared workspace remains master.

## Commands run

## Results

## Open questions

None in accepted design. No merge authorization.

## Cleanup

Retain all feature refs and this initiative. Never archive this initiative as a
side effect of finishing. Test VMs/disposable fixtures are owned by this work.
