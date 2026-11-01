# Configuration export: focused committed review packet

Exact clean head **b91815b8c116f27a5d04a843c21e982457c3e186**, tree **77f4eca2dadbad020223f01b135b361e829836d8**, directly follows deployed **d632caf4b6d617ee8495b8132332fc56a82bdfe5**. Repository `git@github.com:vpsfreecz/dev-workspace.git`, own branch `2026-10-24-vpsadmin-haveapi-upgrade-services-os`, worktree `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-dev-workspace-services-os`.

This is the lead-authorized correction to A0's final [design section](../../design.md), “2026-10-31: retained-start refusal from a newly detected configuration export” at line5778. Parent accepted the fixed policy and the user confirmed “okay okay, let's keep it as it is. proceed with your fix.” The requested review is narrow product/test/compatibility assessment of d632..b918 plus explicit complete767..b918 history/consolidation/migration conclusions. No new architecture campaign is requested.

## Failure and correction

The ordinary retained start17669 refused before launch because a newly present optional configuration checkout automatically requested a `sharedFileSystems.config` export. A0's offline comparison found exactly that absent-to-present field in all four actual guest descriptors; every other nonpayload field matched after the existing OS/host projection. Lead reports d632/consumer35510cb already deployed as aitherdev profile217/ns0. No claim about config.json byte changes is made; no preimage exists. E3 owns actual cluster effects and later operations.

The six-line helper correction keeps `config_source_path` empty only when a validated, nonempty retained context has no `config` export in **every** descriptor. It executes before `nix_common_env`. Fresh/null context retains ordinary checkout detection. If any descriptor records the export, ordinary current-path selection and exact strict guards still apply. Malformed JSON propagates jq failure before Nix. No public selector, state schema or mount transition is added.

Both host share and guest `/mnt/configuration` declarations already depend on that argument in `nix/test.nix`; that file remains byte-identical. `projectUpdateConfig`, `compatible_configuration!`, `machine_layout`, target proof/pending semantics and the same OS checkout/local-staging selector are also unchanged. Missing/retargeted/mixed existing exports still refuse. Other automatically selected mounts keep their existing behavior.

## Scope and complete history

[Inventory](inventory.json), [d632..b918 correction](delta.diff), [767..b918 full diff](final.diff), [complete history](history.txt), [old/new range comparison](range-diff.txt).

The correction touches exactly four files: provider helper, its README, existing commands tests and existing Nix-smoke test. All **108 other tracked path/mode/blob entries equal d632**. The full selected767dfd587e346168e1443e65ccdb67ce748f3fe3..b918 series contains exactly two coherent behavior commits across seven paths; all **105 outside entries equal767**:

1. d632 introduces the reviewed same-OS-selector behavior and remains the supported deployed predecessor. Its actual profile217/consumer355 boundary must remain recoverable; this correction does not rewrite it.
2. b918 introduces only absent configuration-export preservation with its tests and explanation. These are one behavior and are committed together.

No dependency/channel/lock or generated-input stream changed in the correction. Superseded acc/3fdec are not ancestors of the final series; their named recovery refs and prior roots/evidence remain intact. There is no revert, fixup or obsolete applied-input pin stream. **NO MIGRATIONS**: no envelope schema, disk format, migration file or recovery contract changed. The reviewer must independently confirm the full history and migration conclusion.

## Focused quick evidence

Declared `nix develop .#checks.x86_64-linux.tests`, pinned Ruby3.4.9/Gem.default_dir and baseline Ruby verbosity, CPU60–63/nice5/Nix1job2cores. The retained840-unavailable visible original-owner monitor fallback was used without bootstrap. All recorded driver/Nix process identities have exited. Raw logs/results stay0700/0600 outside portal under `/tmp/e0os-config-export-374ji3hq`; inventory binds their hashes and exact original handles.

- Original34641 exited1/13.163s before commands tests: the new raw-source Nix fixture lacked packaging-generated default-config.json. The fixture now uses a disposable copy of the actual provider plus existing `test/fixtures/vpsadmin-config.json`, matching normal packaging; product source did not broaden.
- Original34728 exited1/251.765s:5 tests/53 assertions/2 failures/0 errors/skips. Fresh creation, malformed context and existing matching exports **passed**. The Nix fixture **passed** actual absent/present host-share and service/node guest-mount gates, lazy services, retained boot, selected targets, absent `rootDisk.image` and12 strict layout refusals, including config add/remove and another mount mutation. This passing scope is reused unchanged, not called a green five-test run.
- Its two failures were new fixtures: all-target coverage omitted configured DNS descriptors, and refusal coverage guessed stderr suppressed by the inherited stub's `$VERBOSE=nil`. The all-target fixture now supplies both DNS descriptors. Refusals require nonzero exit, exact selected source/build context, byte-identical applied envelope, no run/copy/activate/SSH and released locks; diagnostics did not change.
- Affected original71166 exited0/335.102s: **3 tests/93 assertions/0 failures/errors/skips** (test time328.190109s). The corrected late-checkout matrix passed boot/services/node/all/same-target retry; all six start/services missing/retargeted/mixed variants passed; the existing retained-start other-layout refusal and unapplied-payload regression also passed. Successful unchanged cases/Nix proof were not repeated.
- Ruby syntax for both test files, Bash helper syntax and `git diff --check` passed. Ordinary `git commit -F` in the declared environment completed0. This repository declares no hook framework, core.hooksPath or active nonsample hook; no hook was bypassed. The committed delta exactly equals the staged checked bytes.

## Compatibility and documentation

No public CLI/environment interface, persisted schema or mount layout transition changes. Rollback can read the same stored state; old d632 may again refuse a retained absent-export cluster when the checkout exists, which is the original safe refusal. Current exports still require exact path equality. No coordinated machine update or kernel replacement is promised.

The provider owns this automatic selection; the workspace package's provider wrapper and portal retained-start/update commands consume it. Existing consumer355 selects deployed d632. Parent/E1 will separately pin a reviewed/published successor and perform applicable package preparation/activation; no consumer or configuration worktree was edited here. Root/operator trust assumptions remain those in local AGENTS; no generic runtime or OSVM contract changed.

README's nine-line paragraph uses the parent's exact final wording after its required user-facing-writing/humanizer pass. It explains fresh detection, retained absence, strict existing-export paths and that these commands provide no attachment transition. No new diagnostic was added.

## Review and execution boundary

Overall **HIGH** risk because retained host/guest layout and persistent-disk compatibility are involved. Lead owns retained reviewer0 (`gpt-6.1-sol`/xhigh/read_only), its assignment and acceptance. Use the mandatory-change-review skill and affected general, architecture/repetition, scope/proportionality and risk/compatibility lanes, retaining earlier d632 implementation review only at exact unchanged scope.

**STOPPED for independent final review.** No new remote mutation, long flake/installed checker, manual full commands suite, consumer pin, activation, cluster query/start/update/retry, claim, default integration, export transition, kernel/VM build, GC or lifecycle action occurred. Prior final-d6320/0 remains proof of that source only. After review, parent will release final-source ordinary checks/publication and E1 pin. Own source is reserved only for review findings; all historical roots/refs/evidence and the session remain open.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/)
