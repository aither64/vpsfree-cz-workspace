# Two-test repair: narrow affected test and history review

Current final head **d632caf4b6d617ee8495b8132332fc56a82bdfe5**, tree **884bc3eb0e9d758cc1025e1a12f5130eaa0c84d9**, is clean. Base **767dfd587e346168e1443e65ccdb67ce748f3fe3**. Previously reviewed/published head **3fdecfbbdd93f92754a0384d0134958c260cf619**, tree **4990ae5d719e4d7cdea8d207660ad26632fb4270**.

Repository/worktree/branch remain the existing owned vpsfree-dev-workspace-services-os package. The lead accepted reviewer0 native01a1912c all-four-lane HIGH review on767..3fdec, with no findings, coherent whole history and NO MIGRATIONS. This followup requests only the affected test assertions/fixtures and refreshed complete history; all implementation and documentation are byte-identical to that review.

[Exact reviewed-to-final diff](reviewed-to-final.diff) changes only **test/devcluster_commands_test.rb**, +4/-2 in two existing methods. All **111 other tracked path/mode/blob entries match3fdec**. The full final767..d632 range is one coherent commit, seven paths, with all105 outside-baseline entries equal. [Inventory and evidence bindings](inventory.json), [complete final history](history.txt), [full final diff](final.diff), [range comparison](range-diff.txt).

## Concrete findings and repair

The original normal flake check on3fdec exited1 after2275.687s. The full command suite ran48 tests/645 assertions with two failures, zero errors/skips. Its preceding status suite passed52/608. The fail-fast driver did not launch the installed checker or new real-services projection. This is not final-source package acceptance. [Original failure/effects](../postreview-failure.json).

1. `test_successful_start_keeps_build_environment_for_the_runner` compared every build variable with the runner environment. The reviewed implementation deliberately scopes exactly `VPSADMIN_DEVCLUSTER_APPLIED_CONFIG` and `VPSADMIN_DEVCLUSTER_UPDATE_TARGET` to the build. The repair compares every other environment field unchanged and explicitly asserts that **both** internal variables are absent from the runner. Existing source/config/network/readiness/stale-file/lock assertions remain.
2. `test_refresh_failure_is_not_reported_as_success` created no applied context for its update variant. The accepted target-proof guard correctly refused before the intended injected SSH failure. The fixture now prepares validated applied context **only for update**. Both start/update variants retain expected SSH exit23, exactly one SSH event and lock-release assertions.

No provider implementation, Nix projection, diagnostics, README, helper, shared/runtime/OSVM code, selector, credentials, dependency, state schema or public interface changed. No assertions were relaxed outside the two intended build-only environment fields, whose absence is checked explicitly.

## Actual affected quick checks

Normal declared tests environment (`nix develop .#checks.x86_64-linux.tests`), pinned Ruby3.4.9/Gem.default_dir, original runtime contract, CPU60–63/nice5/Nix1job2cores and the retained840-unavailable visible owner fallback.

Targeted original handle56075 exited0: **2 tests /25 assertions /zero failures/errors/skips**,70.749921s. Ruby syntax and git diff whitespace0. Existing hook framework remains absent, with no active hooks; ordinary `git commit --amend -F` completed0 without bypass. [Precommit/quick hash receipt](../test-repair-precommit.json). Raw log `/tmp/e0os-same-selector-checks-h61n8jq6/fix-quick.log` remains private0600 under0700, SHA256 bound in inventory.

No successful quick suite was rerun and no full command suite was repeated for this narrow repair. Final-source normal full flake/all48 plus installed-flake/runner check including the new real-services projection remain **held pending this review and lead release**. Exact unchanged derivations/inputs may use normal Nix cache reuse when execution resumes; no old source result is relabelled.

## History and recovery

Before amending, exact3fdec was preserved at `refs/heads/2026-10-24-vpsadmin-haveapi-upgrade-services-os-same-selector-recovery`. Oldacc remains at the separate applied-pin recovery ref and remote recovery branch. All original3fdec roots, publication proof, failed fullcheck/result/log and prior quick/review evidence remain intact. Remote feature still selects3fdec; **d632 is not published**. No remote operation occurred during repair.

Per explicit lead direction, the two test corrections were folded into the single final provider commit. The entire original commit message is byte-identical. There is no superseded applied-input pin, revert, fixup, repeated dependency/channel stream or separate test-fix commit in the final767..d632 history. **NO MIGRATIONS**: schema/envelope format and migration inventory are unchanged.

All original recorded owned PIDs1396504/1396508/1396563/1396590/1398241/1400751 are gone. Targeted56075 completed; no verification operation remains active. All roots/evidence are retained; no source/default/profile/consumer/live cluster action, VM/kernel build, storage collection/deletion or session lifecycle change occurred. The new source is reserved only for review findings. Lead owns the narrow retained reviewer0 test/history assignment, publication disposition and subsequent execution release; E1 must eventually bind the final published SHA.

[Previous complete design/context packet](prior-review-packet.md). Session stays open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
