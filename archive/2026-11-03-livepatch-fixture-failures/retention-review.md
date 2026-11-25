# Retention correction: independent committed review

Reviewer: reviewer0, retained gpt-6.1-sol/xhigh, review-purpose/read_only.
Final reviewed range: vpsfreecz/vpsadminos 742eb30cb1a8b6766c85e915d26b0400e38244b1 -> 48f2983e3cf6b5b72a21c254f744ad8e7d62a123.
Affected behavior: efc5f8fe87f7b0ddc09b5946047e1c231d23db67 -> 06d373facd86003a6c2d27604d553939f7ef3577, followed by the equivalent refresh to 48f2983e.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.

## Findings and disposition

No new Blocking, Important or Advisory findings in the retention correction or refreshed branch inventory. The affected final-review gate passes for proceeding to exact-head CI. Complete CI and runtime acceptance remain pending; the user's conditional merge approval remains unsatisfied.

Reuse final-review.md for the original dd188397..4fc0f375 substantive source review and review-reconciliation.md for its bounded R1/R2 remediation through efc5f8fe. I also inspected the actual six-path 4fc->efc delta and the small functional predicate/consumer corrections; it matches the recorded narrow fixes. I did not repeat the unaffected sixteen-file implementation review.

## Scope and proportionality

The accepted user outcome remains qualification of the current normal module, with nine useful semantic witnesses, exact predecessors/boot integrity and recovery. The new behavior delta is exactly one workflow file, +11/-1. Its local outlink and second existing profile-helper call directly address the demonstrated distribution failure. No server/config implementation, new helper interface, registry, persistent-state scheme or production recipe/input/pin change is introduced.

The elapsed evidence includes a queued CI build and a downstream failure roughly an hour after the copy; these are concrete preparation/delivery milestones, not grounds for expanding the correction. The present conventional use of existing Nix roots/profiles is proportionate. Additional retention infrastructure or optional hardening is unnecessary for this scoped fix.

## Evidence: observations and inference

I inspected the saved raw build and Intel logs and independently verified their SHA256:
- ci-41714748110-build-job.log: 84bab27b06c2e0ef63cb8558d6fe2ec39b7a246991f7e15858489260878098fb.
- ci-41714748110-intel-job.log: ca927242eda000fba4dfa6f6e2037f0494aca7145772858693796bdebc1ed263.

Old run 41714748110/attempt 1 is bound in the logs to tested head efc5f8fe87f7b0ddc09b5946047e1c231d23db67 and input-lock digest 604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa.

Build job 126191705303 built /nix/store/asfl9yry0hdavkhmv9ib8xcd4msknniz-livepatch-candidate-sites.drv, captured output /nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites, and reported normal producer /nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95 and module SHA256 7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f. The copy log explicitly includes the exact sites output at 22:05:43Z and the normal toplevel. The later successful profile step calls push-ci-generation only for BRANCH/BUILD_OUT.

Intel job 126236869931 has the same captured source/input/producer/module/sites values and fails at 23:06:56Z on nix-store --realise for aiqijl..., before the descriptor read, fixture preparation or VM. This is a distribution/preparation failure, not evidence that a runtime witness failed.

Saved public responses at 23:11:05Z show sites narinfo 404 with "No such path." and producer narinfo 200. These establish unavailability at that endpoint. Canonical proxy configuration also points that public cache to the int.cache nix-serve service. Its synthetic upstream-outage response has a different configured body, but these receipts still do not establish a server deletion journal or exact deployed configuration revision.

The old workflow demonstrably omitted a retention profile for an output outside BUILD_OUT's closure. GC of that unrooted output is consistent with the observed loss and canonical policy; the actual collector invocation/deletion timing remains an inference, not a proven event. The correction addresses the missing-root defect without claiming that inference as direct observation.

## Helper contract, identities, skips and failure semantics

I read the canonical cache owner source at vpsfreecz/vpsadminos-org-configuration f924aabd0a774d88d173419527215cf4b538168a, cluster/org.vpsadminos/int.cache/config.nix, and the relevant public proxy routing at the same revision.

push-ci-generation takes exactly branch plus one store path, derives basename(branch), and runs nix-env --set at /nix/var/nix/profiles/ci-BRANCH-profile. Its exit status is preserved. Canonical ci-gc recognizes that profile family, prunes generations/profiles using the existing policy and then collects unrooted paths. The new feature-branch profile receives the existing 90-day policy. This is inspection of canonical policy; the next live CI must prove the installed helper and retention path actually work.

Final .github/workflows/ci.yml:162-163 roots candidateSites locally with the ordinary run/attempt-specific outlink beneath RUNNER_TEMP while retaining its exact returned store path. Distinct run attempts use distinct local links. Existing digest/schema/source/input/producer checks still precede the dependent rows.

Final ci.yml:205-212 publishes the same captured LIVEPATCH_SITES_OUT after the existing SSH copy and normal profile call, using BRANCH-livepatch-sites. For this feature the resulting profiles are:
- ci-2026-11-03-livepatch-fixture-failures-profile.
- ci-2026-11-03-livepatch-fixture-failures-livepatch-sites-profile.

Both conform to the actual helper/GC naming contract. The basename behavior also keeps the two profiles distinct for nested branches. The new call roots metadata independently of BUILD_OUT; it does not switch a deployed system or broaden the helper's interface.

Capture and lifecycle matrix guards remain identical: test_suite != zfs-full and no test_pattern. If LIVEPATCH_SITES_OUT is absent or empty, only the ordinary profile is published. The existing nine-row matrix and dependent captured sites path are unchanged.

GitHub's Bash -e step semantics propagate either SSH/helper failure. I independently exercised the exact extracted final publication script in memory with an ssh shell-function stub: failure on call 1 exits 47 after one call; failure on call 2 exits 47 after two calls; both success completes after two calls; absent sites completes after one. No SSH command, filesystem mutation or remote operation occurred. A partial publication can leave the ordinary profile updated or an uploaded output unrooted, but a failed build does not release successful dependent verification rows. No forced rollback or hidden success path is added.

## Verification and remaining acceptance

I inspected the actual disposable nineteen-control harness and its saved final-run log, rather than treating the count as a live cache test. It extracts the workflow scripts and uses real checksums/Nix JSON/assertions, while Nix builds, realization and SSH are stubbed. It verifies capture identities, negative identity/schema cases, distinct run-attempt outlinks, exact profile arguments, absent/empty skips and nested branch names. Those controls support the shell contract; they do not prove Nix GC root registration, remote nix-env profile creation or downstream substitution. The saved final Nixfmt/RuboCop hook log passes. I independently ran final-range git diff --check.

The old build log now supplies actual candidateSites package-realization evidence for its exact asfl9/aiqijl inputs, closing the earlier old-head packaging uncertainty. It supplies no refreshed-head cache-retention or guest result. A's fresh IFD-disabled evaluation reports unchanged qi47/module/asfl9/aiqijl identities; I did not rerun Nix evaluation or claim a new build. My independent blob/history/lock-path inspection confirms the refresh does not alter feature files, lockfiles, kernel or fixture inputs.

Required next evidence is a fresh run bound to exact final head 48f2983e3cf6b5b72a21c254f744ad8e7d62a123: successful profile publication and actual sites substitution on downstream runners, native suite and all nine lifecycle rows with required FUSE/TCP/other semantic, identity, data-integrity, health and recovery evidence. Old-head successful checks may inform diagnosis; failed old run 41714748110 cannot satisfy complete-CI acceptance. No live profile, GC journal, replacement CI or runtime proof was invented here.

The new invariant is explained beside its owning workflow code. The individual failed-attempt evidence and diagnosis appropriately remain in ci-sites-retention-failure.md and session records. Existing project testing documentation is unchanged by this retention-only correction; another product documentation mechanism is unnecessary.

## Final whole-branch history, equivalence and migrations

Independently verified:
- HEAD = 48f2983e3cf6b5b72a21c254f744ad8e7d62a123.
- HEAD^ and merge base with the final baseline = 742eb30cb1a8b6766c85e915d26b0400e38244b1.
- Complete final range contains exactly one commit, "tests/livepatch: qualify current module probe sites", 16 files +2157/-180.
- efc5f8fe -> 06d373fa is only .github/workflows/ci.yml, +11/-1.
- range-diff dd188397..06d373fa versus 742eb30c..48f2983e reports equality.
- Both feature patches have stable patch ID eb6c27981a4cb0e38498f77fb4e5a92856cbc212.
- All sixteen feature blobs and the original commit message are byte-identical between 06d373fa and 48f2983e.
- Incoming baseline contains exactly three canonical openSUSE commits and seven paths, with no feature-path, fixture/kernel or lock overlap. These upstream changes remain their canonical history; they require normal fresh baseline CI.
- Local reviewed 4fc0f375, tested efc5f8fe and pre-refresh 06d373fa backup refs retain their exact objects. They are provenance refs outside the final feature series.

The retention correction and R1/R2 follow-ups are folded into the owning unmerged test feature commit. This is a coherent internal artifact-qualification contract. No obsolete unmerged approach, fixup/tidy residue or transitional source implementation remains in the final branch.

No repeated dependency/channel/input/pin/lock/generated-artifact update streams exist in the final feature series; none require consolidation or an intermediate-consumer exception.

No migrations. There is no database/schema/production persisted-format or protocol migration, deployed intermediate, externally consumed intermediate schema or migration lineage to preserve. Normal production inputs, boot/predecessor identities and mixed-version contracts remain unchanged; no coordinated fleet update is required.

## Identity and handoff

dev-session current from the assigned directory matches 2026-11-03-livepatch-fixture-failures. Both DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE are absent; trusted thread-bound developer instructions explicitly bind this session and /home/aither/workspace/ai/vpsfree.cz. Fresh roster confirms reviewer0/thread 01a1a24e-920c-7b82-9fff-7754d1f947ab, gpt-6.1-sol/xhigh, review/read_only, ready. Settings and independence were retained; no nested reviewer was launched. Mandatory skill and all four lane references were read, with applicable workspace/repository guidance.

Final source/index/nonignored-untracked status is clean. I remained read-only: no session/source writes, builds, VMs, retries, cancellation, fetch/push, merge, deployment or lifecycle action. This complete report is delivered through report_to_lead for root to save as retention-review.md.

Review complete; next action is lead-owned exact-head CI and evidence reconciliation. The user's conditional vpsadminos/staging integration approval still requires complete CI success. Session remains open.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
