# Scoped final revision review brief

The independent final all-lane review covered base1b56616 through18d8b486;
its requested fixes were directly inspected/tested and folded into3be154b5.
See review-report.md and branch-inventory.md for complete reviewed lineage.

Local full integration at3be154b5 passed auto_rollback3/3 and carrier/deploy8/8.
Netboot/deploy_flakes failed before assertions at bare `nix flake lock`, before
fixture Git init. These same commands exist at the v3 baseline; modern declared
Nix discovers git+file:///tmp. Explicit-path operational smoke already passed.

The intended additional delta is exactly two fixture lock commands in
`tests/suite/carrier/netboot.nix` and `tests/suite/deploy/base.nix`: use
`['nix', 'flake', 'lock', "path:#{conf_dir}"]`, preserving placement, chdir,
copied-lock behavior, Git initialization/commits, all tests/assertions and
runtime/boot/deployment interfaces. No helper/framework/new design is added.

General lane is affected by the committed fixture source-discovery correction.
Prior architecture/scope/risk conclusions remain; no public/persisted-state
boundary or protocol changes. Flag any contrary evidence. This is an additional
post-review verification correction, rather than a rubber-stamp rerun of the
three earlier requested fixes. Reviewer0 retained gpt-6.1-sol/xhigh/read_only.

Final committed head/series, two-line delta and quick evidence will be inserted
before assigning review. Long failed-suite retries follow this revision gate.
No migrations; unchanged v3 JSON/roots/recovery contracts. No merge/deployment.

## Committed revision and quick checks

Base1b56616eff41e760327f3a0dbed8875e4aa9dbec, head`cc40679d267165aecfa569128438bb55fe910268`.
Final tree08f33e1fe5613f7634ba69b38535fb3c35a3c0c9, identical checked pre-fold tree.
Clean source/index, whitespace clean; only2fixture commands changed from3be.
Parent fullRSpec66/0 (22.83s),95-file RuboCop0; member two-file nixfmt and
extracted Ruby syntax passed, direct hashes unchanged, active hooks passed.

Complete final series:

```text
d72ff27a9b589ed0d2b0532db70f4e1b96b7373d Make confctl runtime exclusively flake-based
72eb424c430182c0563b3ecb7d4e5869a5c2721d Remove Nix pin evaluation and expose flake module options
85bb8717ca25aa84a01fb6f5ef4ce43e3283a5fb Make the flake example the sole configuration fixture
9d63ab4f30929043b8695225c0128029b188a985 Drop software-pin-only dependencies and CI setup
cc40679d267165aecfa569128438bb55fe910268 Document flake-only operation and preserved recovery state
```

Final complete diff: confctl-final.diff. Added delta: fixture-remediation.diff.
Whole5-unit fold: fixture-remediation.range-diff; units1/2 exactsame,4/5
patch-identical; unit3 owns2lines plus final rationale. No fixup/transitional
commit remains. No migrations or new intermediate state format. Published3be
contains unchanged v3 flake state contract; no merge/release/live deployment
by this session. Newhead unpublished pending review. External consumption of
public3be is unknown and no incompatible schema/path is being rewritten.
