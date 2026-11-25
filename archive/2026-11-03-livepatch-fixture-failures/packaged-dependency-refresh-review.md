# Packaged dependency refresh: final affected independent review

Final range: vpsfreecz/vpsadminos 2951a632c4254a44747a8da326e3dde897eaa0e2..e1751c917f216897292ab0b893727a6e5553a540.
Retained reviewed range: 54b4313404cea35b58ebb9df951ae75e27c44971..dc74bcdadef75f181934bad2178afb589c34644c.
Reviewer: retained reviewer0, gpt-6.1-sol/xhigh, review-purpose/read_only, unchanged settings.
Lanes: general, architecture/repetition, scope/proportionality and risk/compatibility, restricted to the actual packaged-baseline interaction, evidence reuse and complete final history.

## Findings and disposition

No new Blocking, Important or Advisory findings. The affected committed-review gate passes for publication and full exact-final-head CI.

This review does not establish new gem-byte/package realization, guest/runner closure equality, runtime success or merge readiness. The old cgroup-v1 boot cause remains unclassified and unwaived. The user's accepted full final-head CI/identity/semantic/recovery condition still gates vpsadminos/staging integration.

Reuse osvm-boot-evidence-review.md and the earlier review/reconciliation chain for the unchanged implementation. No unrelated twenty-file source audit was repeated.

## Actual packaged-input interaction

I independently confirmed that incoming canonical history contains one commit, 2951a632c4254a44747a8da326e3dde897eaa0e2, "os: update packaged gem dependencies". It changes only:
- os/packages/osctl-env-exec/Gemfile.lock.
- os/packages/osctl-env-exec/gemset.nix.

The paired +3/-3 update selects rake-compiler 1.3.3 instead of 1.3.2 and updates its gem source hash. Final feature history preserves those two canonical files exactly; it neither reverts them nor regenerates another dependency set.

The owning default.nix uses bundlerApp with this directory as gemdir. The unchanged tools/osctl-env-exec gemspec declares rake-compiler as a runtime dependency in its bootstrap environment, and the unchanged executable delegates to Process.exec(*ARGV). Thus this is a real packaged dependency, not evidence-free metadata or a dependency proven irrelevant merely by a small diff.

I inspected os/overlays/osctl.nix and os/packages/ruby-source-gem-config.nix. Source-backed local gems receive src = repoPath for the whole repository and then unpack/copy that source before selecting their gem directory. The changed package files therefore affect source inputs for ordinary packages such as osctl/osctld even when those gems' own Ruby files are identical. The osBundlerApp wrapper adds completion generation; it does not erase this broader source dependency.

Channel construction also copies os/ when enabled. The test base defaults channel registration off, while enabled QEMU/ISO paths may carry it. This is an additional conditional source-content path, not proof that every test guest uses that channel or executes the bootstrap command. No direct guest-module selection of osctl-env-exec was found in the inspected paths; that does not prove whole-guest input equality because the source-gem path already demonstrates a broader effect.

The refreshed commit also changes captured revision/source paths under the previously reviewed source-identity machinery. Whole guest/test closure equality and old-head runtime acceptance therefore cannot follow from unchanged feature blobs or root flake.lock.

## Host check reuse and evaluation limits

The actual host boundaries are distinct:
- The packaged runner uses test-runner/nix/Gemfile, runner-deps.lock and gemset.nix plus current local runner/OSVM/libosctl sources and native extension.
- The retained focused/full OSVM and shared integration specs use test-runner/Gemfile and Gemfile.lock under the recorded cached declared Ruby/native/Bundler environment.
- The incoming bootstrap bundle is os/packages/osctl-env-exec/Gemfile.lock and gemset.nix.

I independently checked that the exact loaded source/spec/framework paths and all those host-bundle inputs named in A's comparison are unchanged versus reviewed dc74. The full old/new tree delta is only the incoming bootstrap pair. I read the current execution-binding load receipt: Ruby 3.4.11 resolves to the same z30... store path, the native extension to the same givmi... store path, Bundler 4.0.23 and RSpec 3.13.6 are loaded, and Machine/MachineLog/CLI resolve to the current unchanged checkout sources with the same test-runner Gemfile/BUNDLE_PATH. No examples were executed by that binding check.

That supports retaining D's 81 focused/207 full OSVM and A's 99 integration successes within their existing exact source/execution-input scope. They remain earlier executions, not new-head suite or packaged-runner passes. The standalone source-version/channel-revision results likewise retain their unchanged owning code and locked-input scope. No automatic broad rerun or new verification framework is necessary merely to repeat these unchanged checks.

I inspected both fresh IFD-disabled evaluation receipts:
- The complete ten-field livepatch/SDK tuple is structurally identical to package-a-osvm-identity.json, including every drvPath/outputPath and module value. I independently compared the JSON objects.
- The four requested actual-head package fields are complete: osctlEnvExec, osctl, osctld and testRunner, each with drvPath/outputPath. Their evaluated outputs are respectively /nix/store/c3kb17cf3xmm40rkzh04kpnmb9xjvakg-osctl-env-exec-26.05.0, /nix/store/h9cvfm2qqrkpg08ji54bxb9y0i3bsx15-osctl, /nix/store/kivvmblmpzva7ankywjxk2c68q4mmwdk-osctld-26.05.0 and /nix/store/4vjr6gmfxb4ljsxg8q9mn126p2x3mqg6-test-runner. Full drv/output identities remain in package-a-2951-package-identity.json.

No comparable old four-package receipt was invented or evaluated here. These evaluations establish evaluability and record required identities; they do not fetch/verify the new gem, build the applications or certify their behavior. Required new outputs and guest/runner behavior belong to final-head CI.

The ten-field equality supports the respective prior artifact-specific module/sites/resolver/control/boot/SDK/compiler checks, not all guest closures. A's fresh receipt also retains module SHA 7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f and sites SHA 093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1 with schema/module binding intact.

Independent file hashes match:
- flake.lock: 604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa.
- test-runner/Gemfile.lock: 10cc972d84899008e01de673d812f14827493520037b64e22ab7f30f3356a744.
- Bootstrap Gemfile.lock: ac8e1776934597c74396d83042ad3475a00b52d1c7346163bad3d090319bcc90.
- Bootstrap gemset.nix: 0fa12b236bf9581cbb4396ef9604b3713eca4672544637036db55600020ebc68.

I inspected the current declared Bundler Diff-hook pass. Both original messages retain their earlier hook proof plus normal enabled rebase-hook provenance. My final-range whitespace check passed. I ran no evaluation, build, suite, VM or binding-load command.

## Scope, architecture and compatibility

The actual user outcome remains current normal-module qualification with nine meaningful current-build witnesses, exact predecessors/boot and recovery, without a freeze, blind allowlist repin or historical-only witness lane. This refresh adds no feature mechanism or source change. The separate bootstrap recipe and existing shared source-gem owner explain the new baseline's effects without inventing another interface or compatibility layer.

The bounded comparison, actual-head evaluation receipts, explicitly scoped host-check reuse and final-head build/runtime requirement are proportionate. Repeating the unrelated implementation audit, regenerating gems or building a new local dependency project is unnecessary. The mechanical refresh preserves supported interfaces; no feature API/protocol/persisted-state migration or coordinated fleet update is introduced. This is not an assertion that the new upstream gem's behavior has already been tested.

Existing project behavior documentation remains accurate because the feature body is unchanged. Refresh/evaluation/CI provenance appropriately remains in package-a-result.md, design/implementation-plan, verification-launch.md and the linked receipts. No new product documentation mechanism is needed.

## Complete final history, equivalence and migration conclusion

Independently verified the complete final two-purpose series:
1. 8169b8189c29f471b2ecf27a33b6f71dbde5e70e — tests/livepatch: qualify current module probe sites.
2. e1751c917f216897292ab0b893727a6e5553a540 — osvm: record bounded host evidence for boot failures.

The final first parent is exact2951; e175's parent is exact8169; merge base is exact2951. The range contains exactly two commits, twenty paths +2923/-184.

Both range-diff rows compare equal to 54b..dc74. I independently verified ordered patch IDs and raw messages:
- ad899 -> 8169: patch ID 317857127604b13d7f79a3d294ee39efe97b3379; raw message SHA256 620322a1820f2a1f3527d677f6d54be378985dc870dc8e1e31a03d7d978f1fcd.
- dc74 -> e175: patch ID 35e735aa81029cac8e6e960ff15a8a94a2ef0cc7; raw message SHA256 9e8ae232e2fcb389129930fb0c269044c5fd718d430581997bc25af852c8dada.

All twenty feature path modes/blobs and their complete inventory equal the reviewed old range. The complete dc74-to-e175 tree delta equals exactly the two incoming canonical bootstrap files; both match canonical2951. The reviewed-dc74bcda local backup retains exactdc74. Earlier refs and detached5235 remain provenance outside the feature series; none were removed or published by this reviewer.

The two commit purposes remain independently meaningful: qualification plus bounded pre-shell host evidence. No obsolete feature approach, fixup/tidy residue or transitional implementation remains.

No repeated dependency/channel/input/pin/lock/generated update stream occurs in the unmerged feature series. The already canonical dependency commit is baseline history, not a feature update to fold, consolidate or rewrite.

No migrations. No feature database/schema/production persisted-format/protocol migration, deployed intermediate or externally consumed transitional schema is introduced; migration lineage is empty.

Final HEAD and clean source/index/nonignored-untracked status matched e175 at inspection. No rebase conflict or changed feature content was found.

## Remaining gates, identity and handoff

This review permits the planned publication and full exact-e175 native plus all nine lifecycle CI, including required artifact/boot identity, FUSE/TCP/fragment and other semantic witnesses and recovery. It does not authorize merging before accepted complete success. The packaged lock/source-path and captured revision changes make that fresh verification material.

Old5235 run 41773470432 remains observer-owned old-head evidence. Native41811208607's shared cgroup-v1 firmware-only boot failure remains unclassified and unwaived. New OSVM observation supplies future facts; it does not explain that stall. Old5235 updated-image/device passes also remain bounded to their own inputs. Any actual new failure requires evidence-based handling, not a blind retry or retrospective cause claim.

Identity was reverified first: dev-session current matched 2026-11-03-livepatch-fixture-failures; both environment markers were absent; trusted thread-bound instructions bind that exact slug and /home/aither/workspace/ai/vpsfree.cz. Live roster confirms reviewer0/thread 01a1a24e-920c-7b82-9fff-7754d1f947ab, gpt-6.1-sol/xhigh, review/read_only, ready. No setting overrides or nested reviewers. Applied the mandatory skill/all four references and unchanged current-context workspace/repository guidance; current guidance remains 4d58b5877.

I remained read-only: no source/session writes, evaluation/build/VM, Git mutation, CI polling/retry/cancel/fetch, push/merge/deploy/service/lifecycle action. Complete report delivered via report_to_lead for root to save as packaged-dependency-refresh-review.md. Session remains open.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
