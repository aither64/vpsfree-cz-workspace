# Source-identity baseline refresh: final affected independent review

Reviewed final range: vpsfreecz/vpsadminos 54b4313404cea35b58ebb9df951ae75e27c44971 -> ad8991fe6d48ec06fb7cf7d64f15af7578d37e7a.
Retained comparison: 742eb30cb1a8b6766c85e915d26b0400e38244b1 -> 5235bfd57c92bc05a25946937fe77f9803fe1c93.
Reviewer: reviewer0, gpt-6.1-sol/xhigh, review-purpose/read_only, unchanged settings.
Lanes: general, architecture/repetition, scope/proportionality and risk/compatibility, restricted to the affected source-capture/guest-metadata integration and final history.

## Findings and disposition

No new Blocking, Important or Advisory finding in the reviewed integration or final feature history. The affected committed-review gate passes.

This does not clear the known old-head native boot failure, satisfy final-head CI or authorize integration now. Reconcile the existing failure-handling/diagnostic plan before new CI, then require the complete exact-ad899 native and nine-row lifecycle results and their semantic/identity/recovery evidence. The user's conditional vpsadminos/staging merge gate remains unsatisfied.

Reuse final-review.md, review-reconciliation.md, retention-review.md, defined-symbol-review.md and defined-symbol-review-reconciliation.md for the unchanged implementation and prior requested fixes. I checked the retained DS1 reconciliation and actual current U/u predicate; the rejected uppercase-only approach is not retained in the current source. I did not repeat the unrelated sixteen-file implementation audit.

## Source capture through guest metadata

I inspected the actual incoming runner, Nix/framework and OS metadata implementation, surrounding invocation paths, the relevant specs and standalone evaluation cases. These changes are substantive integration context despite zero feature-path overlap.

RepositorySource captures the original repository commit before resolution, resolves one immutable Nix source under an invocation GC root, and compares that snapshot against the captured commit using a separate index. The comparison covers tracked changes and included untracked/ignored extras while excluding Git metadata. It does not use the caller's staged index as the snapshot identity or silently attribute a child source to an enclosing parent repository. Failure to establish the comparison yields unknown revision/dirty metadata. Later live HEAD/checkout changes do not retroactively change the captured source_info. Included extras may legitimately make a clean-index invocation's snapshot dirty.

Cli::Command scopes TEST_RUNNER_REPO_ROOT, TEST_RUNNER_SOURCE_INFO and any remapped VPSADMINOS_CONFIG around the whole invocation. The ensure path restores their prior values after normal completion or exception. NixCli's existing nix-instantiate/nix-build invocations inherit that environment. Both default/configured evaluation and the direct/batch path pass the provider framework through to tests/make-test.nix.

The sourceVersionModule takes captured metadata only when sourceInfo.sourcePath equals the OS provider's source.outPath. A foreign caller therefore retains the provider's own revision/dirty metadata rather than labeling a pinned provider with the caller's commit. The framework field is optional, so older providers remain accepted. Normal flake construction and test OS construction use the same owning source-version module; explicit module settings retain precedence.

The OS version fallback priority of 1100 remains weaker than captured mkDefault metadata at 1000 and ordinary explicit settings. Security evidence uses the authoritative configured revision when one exists; only the weaker legacy Git fallback expands its shortened display revision. Unknown and packaged-revision cases retain their documented fallback. The channel's nullable revision no longer produces an invalid unconditional revision write. The tests cover provider mismatch, captured dirty/unknown cases, explicit/null/short overrides, the actual test OS constructor, ordinary Git fallback and security evidence. Captured dirty=true and shortRev/version suffix are the baseline's explicit, tested representation; they do not imply a clean snapshot.

These metadata defaults affect guest/system derivations and version/security text. They do not establish guest closure equality across the refresh, and they cannot transfer old-head runtime results to ad899.

## Coexistence with once-captured livepatch identity

The feature's workflow remains byte-identical. It still captures current checkout HEAD, lock digest, exact normal producer/module, module SHA256 and sites once in the build job. Every dependent row validates source/lock/producer/module identity, realizes the exact captured outputs, rehashes the module and checks schema/module binding before discovery. Common/fragment consumers and guests retain their own module/sites checksum checks; released v5/v6 and fixed boot contracts remain separate.

TEST_RUNNER_SOURCE_INFO describes the source snapshot used for evaluation. It neither overwrites CAPTURED_SHA256/VPSADMINOS_LIVEPATCH_CORRECTED_SHA256 nor supplies the module-byte identity in place of those checks. A provider/snapshot version change can change guest metadata while the normal module and sites remain unchanged; the finite derivation/output receipt is appropriate evidence for that separation.

I inspected package-a-refresh-identity.json and independently checked that it contains exactly the ten requested fields, with drvPath/outputPath pairs for all derivation-valued entries rather than JSON-coerced path-only objects. Relevant exact identities include:
- Normal producer /nix/store/161r03nnqvqw9g2ar5kjsbz00zr7xydg-livepatch_7-6.12.95.drv -> /nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95.
- Sites /nix/store/asfl9yry0hdavkhmv9ib8xcd4msknniz-livepatch-candidate-sites.drv -> /nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites.
- Resolver /nix/store/3n2hckv25z7962vrifm8b9q9g5w2axdq-livepatch-probe-sites.drv -> /nix/store/5npsspqbs45rqvm3az8y0z7881668gy4-livepatch-probe-sites.
- Frozen boot/SDK /nix/store/hpjypr6g0sfaa3ygahvcmi5vgxb33b7m-linux-6.12.95-frozen-boot.drv -> /nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot and /nix/store/i1kpp81z029hdl4hyxzbm4sxni181yg0-linux-6.12.95-frozen-boot-dev.
The receipt retains the complete corrected symlink, siteChecks, configuration and compiler drv/output pairs as well.

Independent read-only hashes matched the packet:
- Realized module: 7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f.
- Resolver source: 7d81381c1faf9d9cd3b90422e4116fad0652829c7bb2df5689949b88b45682f8.
- Lock: 604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa.
- Realized sites: 093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1, schema 1, exactly nine records, matching the independently rehashed module.

Together with the retained exact artifact/input receipts and unchanged source, these support bounded reuse of the corresponding resolver/actual-ELF/SDK/helper checks. They do not prove unchanged whole guest/test closures, new-head substitution success or new-head runtime qualification.

## Verification and evidence limits

I inspected the saved fresh-ad899 checks: 99 examples/0 failures across RepositorySource, CLI command, prebuild_nix and livepatch_runtime_sites, plus successful source-version/channel-revision IFD-disabled evaluation checks and Nixfmt/RuboCop/whitespace checks. The source specs exercise actual immutable snapshots/private-index behavior and tiny source-symlink derivations; the metadata tests exercise the real constructor/options and precedence. These are useful scoped checks, not live guest results. I did not repeat their builds or run a new Nix evaluation.

The exact-5235 runtime receipts provide meaningful prior evidence:
- Fragment: corrected unique definition lookup, target at captured +0x3b6, native unlocked/unhashed versus current linked/locked state, nonzero observations and zero missed probes, successful removal.
- FUSE: original safe callee entry, exact configured caller returns, actual caller stack frames, held/count/argument/miss assertions, release/resume and transition/abort/close recovery.
- TCP: 232 accepted wide-value samples, UINT_MAX reordering, positive MSS, zero loss/misses and full 8388608-byte receiver comparison.

I preserved their limits. FUSE flag-clear is linked through the statically validated selected call after unlock; no dedicated unrelated-caller runtime negative or standalone reliable-unwinder return code is claimed. Fragment and main logs do not independently hash their boot images.

The separate frozen-.95 kernel-identity case supplies actual configured booted-image-path equality, notes byte equality, normal lifecycle checks and wrong-notes refusal. Its wrong-image negative also encounters missing readlink in the direct underlying-tool PATH, so it does not isolate image-mismatch refusal. I independently verified that both owning files are identical from old5235 to ad899:
- tests/suite/kernel/livepatch-kernel-identity.nix: blob 1036ac7a4b075324b9d79c72c5aadbd88f753054.
- os/modules/services/livepatches/default.nix: blob 936d937e6efd64e5ad9c963e5303f2559a4ad6cd.

The production guard still compares booted path and notes before management. Positive path/notes and wrong-notes evidence remain valid within that supported contract; an isolated wrong-image negative and independent main-guest image SHA are not invented. The existing control/PATH gap is a recorded residual verification limit, not a source-identity-refresh defect or grounds for an unrelated new framework. This review does not silently strengthen or weaken the original recovery/boot contract.

## Current CI and user decisions

The original 5235 run 41773470432 has seven recorded lifecycle row passes, with aged/fresh work unfinished at the assignment's evidence boundary. It is old-head evidence.

The lead's subsequent D verification update refines native-only run 41811208607: cpu-view-cgroups-v1, memory-view-cgroups-v1 and tmpfs-cgroups-v1 time out in the before hook while waiting for osctl pool tank/boot on one shared cgroup-v1 guest, 1200 seconds each. No CPU, memory or tmpfs functional assertion ran. The console shows only SeaBIOS/Booting ROM; no stage 1/2 or shell. Same-head prior cgroup-v1 success and the cgroup-v2 guest's 6.18.49 boot do not classify the underlying failure. There is no supported claim of flakiness, resource cause or functional regression. D owns the minimal diagnostic/failure-handling plan before another CI run; this review does not duplicate that investigation or clear the failure.

The same update records actual old5235 passes for all six earlier explicit Leap16.1 scripts and latest device units, including latest eth0 active. This closes the old-head selected-image gap within those observed results. It does not qualify ad899. The user's temporary six-script missing-image exception never waived the separate latest-device-unit failure or any new cause; the current shared boot failure has no waiver.

After failure handling is ready, exact-ad899 full CI must establish native plus all nine lifecycle rows and required semantic, artifact, boot and recovery evidence. Passing this source review alone cannot satisfy that condition or authorize merging now.

## Scope, ownership and proportionality

The accepted outcome remains current normal-producer qualification, without a Nixpkgs freeze, blind whole-file repinning or historical-only witness lane. The feature patch has no change in this refresh. Incoming canonical metadata behavior is real integration context; equal patch IDs alone would have been insufficient to accept it.

The smallest completion path is the existing focused integration checks and retained identity tuple, diagnosis/handling of the actual shared-guest boot failure, then fresh exact-head full CI. The already-running/queued old checks and mutable external image timing are verification milestones, not reasons to add a general metadata or instrumentation framework. No optional hardening or new product mechanism is recommended.

Source-version behavior has its owning documentation at docs/os/test-framework-integration.md; the feature contract remains in docs/os/testing.md. Individual rollout, old-head CI and diagnostic evidence appropriately remain in session records. No feature documentation rewrite is needed for a patch-equivalent refresh.

There is no new production API/protocol/persisted-state migration or coordinated fleet update in this feature integration. The added canonical provider metadata field is optional, retains legacy provider behavior and respects explicit overrides; no downstream pin update is required by this feature patch.

## Whole-branch history, consolidation and migrations

Independently verified complete old and new series:
- Old 742eb30cb1a8b6766c85e915d26b0400e38244b1..5235bfd57c92bc05a25946937fe77f9803fe1c93.
- New 54b4313404cea35b58ebb9df951ae75e27c44971..ad8991fe6d48ec06fb7cf7d64f15af7578d37e7a.
- New HEAD^ and merge base equal exact54b; complete feature range contains one commit, "tests/livepatch: qualify current module probe sites", sixteen paths +2270/-183.
- Range-diff reports equality; both stable patch IDs are 317857127604b13d7f79a3d294ee39efe97b3379.
- All sixteen exact file modes/blobs and raw commit-message bytes match across refresh. Independent message SHA256 is 620322a1820f2a1f3527d677f6d54be378985dc870dc8e1e31a03d7d978f1fcd.
- Incoming canonical base consists of six commits/eighteen paths, with no feature overlap or lock update. Four RPM updates plus unknown-channel/source-identity commits remain their existing canonical merged history; this review does not rewrite or consolidate that baseline.
- The tested-5235bfd5 local backup retains exact5235; earlier reviewed/tested/rejected refs remain provenance outside the final series.
- Final source/index/nonignored-untracked status was clean at exactad899; final-range git diff --check passes.

No obsolete unmerged feature approach, fixup/tidy residue or transitional source iteration remains. Prior R1/R2, retention and DS1 remediations are folded into the owning feature commit.

No repeated dependency/channel/input/pin/lock/generated update streams exist in the final feature series. No retained intermediate boundary or consolidation exception is needed.

No migrations. There is no feature database/schema/protocol/persisted-format migration, deployed intermediate or externally consumed intermediate schema; migration lineage is empty.

## Identity and handoff

dev-session current matched 2026-11-03-livepatch-fixture-failures. Both DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE were absent; trusted thread-bound developer instructions explicitly bind this slug and /home/aither/workspace/ai/vpsfree.cz. Fresh roster verified reviewer0/thread 01a1a24e-920c-7b82-9fff-7754d1f947ab, gpt-6.1-sol/xhigh, review/read_only, ready.

Mandatory skill/all four lane references and unchanged procedures were reused from this continuous context as permitted. Repository AGENTS.md was read; changed workspace verification/project guidance at 08ec23ca5 was read. No model/effort override, nested reviewer or other-session access.

I remained read-only: no source/session writes, builds, VMs, CI polling/retry/cancel, fetch/push, merge, deployment or lifecycle action. Complete report delivered via report_to_lead for root to save as source-identity-refresh-review.md. Session remains open.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
