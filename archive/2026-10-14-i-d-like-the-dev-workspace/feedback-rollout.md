# Notification feedback rollout

Status: exact final feedback revision activated; native diagnostics complete. Firefox display acceptance failed with correlated UnknownError; physical macOS acceptance pending.

The user requested menu placement, button spacing, removal of the top session
status row, and working notifications in Firefox on macOS. The missing physical
notification remains unresolved. The new Test path records evidence needed to
identify its failing boundary; it does not prove that macOS will display it.

## Source and supported predecessor

Original reviewed runtime (preserved evidence): `a5e41580d6dbeae9cbb468c707c22106f159066c`.
Current frozen candidate: `4ed9af55127743b7564cb4dd01d10c9f7fee5120`.
Amended delivery commit: `012f6184faa62b7d476555058f1473adcd908528`.
Refresh correction passed its affected committed review and exact final verification.
Delivery commit: `43c6461e3f5ce900f72df7b2aa9593584884b04e`.
Menu/spacing commit: `867682c3df251fbe6941ff9a667539ae1af790ec`.
Final workspace `750ab33c92d7b01e44152420ee5d2ab4c9493826`; configuration `c90e56d5dd0e1ae3da1bf192ca88ab34b2f788a7`.

Deployed predecessor runtime: `6e1d9a191724d376cad2a71f234f0e4d1c01f36f`;
workspace `0a9d232e74209da2c2f53358e5f2807f34074055`;
configuration `45fa9962df83b9bec65523ae6ee7d19b63bb03ea`.
Preserve deployed private notification state, receipts, integration journals,
subscriptions, keys, outbox and cleanup obligations. Recovery stays forward
through a compatible package. Old worker payloads remain version 1; optional
browser result fields require no database upgrade.

The original machine/profile jobs succeeded and remain terminal evidence.
The new ordered activation jobs both succeeded/applied under reservation
`1956d2a0-992b-4b4f-9b0f-9db804769d82`, retained in `deployed_review`.
No uncertain attempt may be replaced or replayed.

## Gates and evidence

- [x] Requested source changes committed; quick checks pass.
- [x] Exact inventory and patches preserved in delivery-feedback-inventory.md.
- [x] Independent final affected review completed.
- [x] Fix two Important correlation findings and one Advisory resume race; direct lead verification.
- [x] Actual Chromium/Firefox template/layout fixture at exact4ed passed21s.
  First exact5a run failed during Enable; feedback-5a-browser.log/status retained.
  Architect found refresh-ownership gap; bounded source correction committed.
  Its affected review passed with no findings; fresh4ed run passed.
- [x] Applicable packaged checks, complete recovery coverage and exact-head CI.
- [x] Publish reviewed runtime source4ed9af55.
- [x] Consolidate one final runtime selection per consumer.
- [x] Exact lock composition/history review and deployment-contract checker.
- [x] Fresh machine/profile preparation with exact evidence and retained user direction.
- [x] New ordered machine then profile jobs submitted under the existing reservation.
- [x] Ordered activation completed and verified; exact jobs/receipts in feedback-4ed-activation-verified.json.
- [x] Independent live selected application/system identity checks.
- [x] Native-run served-asset fences matched.
- [x] New native diagnostic probe and cleanup complete; see acceptance-4ed9af55.md/json.
- [ ] Firefox display acceptance: exact receipt succeeded, display rejected UnknownError.
- [ ] Physical Firefox/macOS appearance and real click acceptance.

Original deployment direction remains: “ok, proceed until it is implemented &
verified. you can also deploy aitherdev using vpsfree-cz-configuration.”
This supplies neither default-branch integration nor reservation release or
session lifecycle approval.

The native probe must use the shipped Test button, capture its descriptor and
match all four fields to post-display outcomes. Keep provider acceptance,
worker receipt, display API outcome, browser record, physical appearance and
click as separate evidence. Linux automation does not prove macOS appearance.
Preserve the earlier failed checks and native results without causal inference.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/

Final native outcome and cleanup are recorded in acceptance-4ed9af55.md/json.
Architect0’s firefox-display-assessment.md found no evidenced application defect;
Firefox/macOS shipped Test outcome is the next discriminating evidence. Coordinator675
has no unsettled jobs; reservation revision6 remains deployed_review.
