# Installed checker wiring: narrow final test/history review

Clean final head **bd66db1e738b0021a2ec55c4bcbf92ad33b8eb30**, tree **8513c33abbb80be1dcabe53ada286e4709ed134b**, is directly above deployed **d632caf4b6d617ee8495b8132332fc56a82bdfe5**. Earlier reviewed/unpublished correction **b91815b8c116f27a5d04a843c21e982457c3e186** is preserved at local `refs/heads/2026-10-24-vpsadmin-haveapi-upgrade-services-os-config-export-reviewed-recovery`.

Lead accepted reviewer0 native01a191c2 all4/HIGH NO FINDINGS on767..b918, including full two-commit history and NO MIGRATIONS. That review remains valid for independently identical product/docs/command-test scope. This packet requests only the new smoke wiring/test correctness and refreshed complete history. [Previous full correction packet](../review-packet.md) and its original quick/failure evidence remain exactb918 records.

## Concrete coverage gap and remedy

After review, the release required the new config-export assertions to execute in the actual installed checker. Inspection found they existed only in `--projection-only`, which exited before normal five-argument execution. No claim of actual installed config-export acceptance was made, and no intermediateb918 publication or consumer pin occurred. Lead accepted the bounded test-only correction; A0 recorded it under “Installed-check coverage clarification (b918 follow-up)” in the final design section.

Only **test/devcluster_nix_smoke.rb** changes fromb918:31 insertions/12 deletions. [Exact delta](reviewed-to-final.diff). The existing Nix assertion expression/runner is now a single `check_projection_contract` function, called from raw quick mode and once from the normal packaged vpsAdmin branch. Normal execution reads the supplied package's actual provider `flake.nix`, `nix/test.nix` and `default-config.json`, the fixed VPSADMIN source and nixpkgs selected by fixed VPSADMINOS. It has no developer-source fallback. Raw quick retains its disposable provider copy and existing fixture default.

The one assertion body visibly emits `configExportAndGuestMount=true` and12 strict layout refusals, including config additions/removals, as well as lazy services, retained boot, selected targets and absent image preservation. No assertion body was duplicated. No public flag, helper behavior, schema, selector, runtime, guard or scenario matrix was added.

All **111 other tracked path/mode/blob entries equalb918**. Inventory separately binds the exact helper6lines/README, `projectUpdateConfig` owner flake, maintenance guards, `nix/test.nix` and commands-test blobs/hashes. No successful command/maintenance suite was repeated.

## Actual affected quick

Original58494 exited0 after **12.237706s** in the normal declared `nix develop .#checks.x86_64-linux.tests` shell, with CPU60–63/nice5/Nix1job2cores and retained840-unavailable visible owner fallback. Ruby syntax and `git diff --check` passed.

1. Raw `--projection-only` executed the shared Nix assertions and passed all advertised gates.
2. A bounded entry probe loaded the actual modified script through its ordinary five-argument path with the retained packaged provider/default and fixed app inputs. The same assertions passed with actual OS-selected nixpkgs. A private Ruby TracePoint checked the provider and VPSADMIN argument bindings, then intentionally unwound after successful assertion return, before unrelated long phases. Its assertion result emitted once; the nonlocal return emitted the stop marker twice. This is entry-path evidence, **not** a full installed-checker pass. No probe code was added to the repository.

The retained probe package is final-d632 tools3g3g; its assertion-consumed provider flake/test/default bytes remain unchanged. This proves the new call path and packaged input binding, not realization/acceptance of the final successor package. Parent will run the actual final `nix run .#devcluster-check` after review, where the normal branch has no probe and continues all existing checks.

[Inventory and exact quick/hash/effects bindings](inventory.json). Raw log/result/probe remain private0700/0600 under `/tmp/e0os-config-export-wiring-7e6m6o74`. Driver3956180/Nix3956228 have exited. Ordinary declared-shell `git commit --amend -F` completed0 with the complete original message preserved and no bypass; repository hook declaration/configuration is unchanged. The committed test delta equals the exact checked staged bytes.

## Complete history and boundary

[Full767..final diff](final.diff), [d632..final correction](correction.diff), [complete history](history.txt), [old/new range comparison](range-diff.txt).

The final767dfd587e346168e1443e65ccdb67ce748f3fe3..bd66 series is exactly two coherent commits: deployed d632 same-selector behavior, then the single config-export correction with its tests/docs. The unpublished correction was amended only for this test wiring. d632 was never amended. Exactb918, old3fdec and acc recovery refs/evidence remain intact; acc/3fdec are outside final ancestry. No repeated dependency/channel/input stream, revert or fixup remains. **NO MIGRATIONS**; schema/disk/recovery interfaces are unchanged. Require the reviewer's explicit whole-history conclusion.

Overall risk remains HIGH due to the existing retained-layout feature; this delta is bounded test wiring. Lead owns retained reviewer0 Sol/xhigh/read_only assignment and affected test/history disposition, reusing accepted all4b918 review only for exact unchanged scope.

**STOPPED for narrow final review.** Remote feature remains deployed d632 as independently observed over canonical SSH, default remains767, and no fetch/push/build campaign/activation/cluster/default/claim/GC/lifecycle action was performed during this correction. No final-source long result is claimed. Parent/E1 are held for the new final published SHA and subsequent actual0/0 package acceptance. All roots, refs, failures and session remain open; source remains reserved only for review findings.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
