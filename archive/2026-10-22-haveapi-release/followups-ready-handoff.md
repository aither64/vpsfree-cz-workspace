# Development follow-up ready

The six fixes are committed and pushed at
`090a188cb4ef3477324718627f4ae3415d1c0975` on
[2026-10-22-haveapi-release-followups](https://github.com/vpsfreecz/haveapi/tree/2026-10-22-haveapi-release-followups).
Independent review has no findings, all eight local verification phases pass,
and all seven exact-head CI runs succeed. The targeted npm, Rollup, Fiddle and
generated Rust naming warnings are absent from the full new CI build log.
Nix-runner and empty Git-fixture warnings remain visible.

Master and official0.30.0 source/refs/artifacts are unchanged; the publishing job
was skipped. No additional release or integration occurred. All commands ended
and source/index are clean. The session remains open, with the development
branch ready and awaiting any later explicit merge/release direction.

Use the fixed generator for a later vpsadmin-client regeneration before its
first crate publication; no new HaveAPI release is required for that source pin.
The downstream preparation and publication remain separately pending direction.

Evidence: [state](state.md), [review](followups-final-review.md),
[verification](followups-verification-handoff.md),
[final CI/proof](followups-final-ci-receipt.md),
[whole-job warning comparison](followups-ci-whole-job-warning-comparison.md).

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
