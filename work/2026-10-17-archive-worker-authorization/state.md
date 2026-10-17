---
lifecycle: active
---

# 2026-10-17-archive-worker-authorization

## Status

Phase: independent review. Investigation complete: commit 5983365 applied archive
worker authorization arguments in run_delete while run_archive retained the
portal-only validator call. Installed package 6qx499s reproduces archive denial
and mistaken delete authorization with a fake runner. Failed worker exited at
2026-10-17T18:20:59Z, before creating an archive journal/snapshot.

- [x] Investigate and agree focused design.
- [x] Create separately owned threadless initiative and initial records.
- [x] Implement authorization and packaged acceptance gate.
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

Runtime base 27ffc685e2c8de02ebb689f6cecc2e7137f28e49; published head
174281afd850be9568ea38ed9a10dcf7d2fd266c. Two logical commits: a54100f
authorization/regressions and 174281a VM/CI gate. No migrations or repeated
pin streams yet. No declared hook framework in runtime or workspace.

Threadless initiative has no retained roster; main owns design/code. Independent
fallback reviewer /root/archive_review selected from installed default
lead_reviewed reviewer GPT-6 Astra/xhigh, catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.
High risk (authorization/destructive lifecycle); all four lanes. Packet:
review-packet.md. Long tests await review disposition.

Runtime ownership handoff: ordinary coordinated deployments require an exact
retained native conversation. Create that conversation from these committed
records with an idle-only goal; external main retains foreground supervision.
This is the one genuine ownership-handoff checkpoint, not a per-result commit.
Do not use pre-contract bootstrap or manufacture ownership receipts.

## Commands run

## Results

Original dispatch: new CLI positive regression failed (2 tests/11 assertions,
1 failure). Fixed: focused Ruby 4 tests/66 assertions passed; focused Go worker
and command tests passed. Ruby/Node/Nix syntax, whitespace and VM derivation
evaluation passed. Nix environment initially fetched cached development tools.

## Open questions

None in accepted design. No merge authorization.

## Cleanup

Retain all feature refs and this initiative. Never archive this initiative as a
side effect of finishing. Test VMs/disposable fixtures are owned by this work.
