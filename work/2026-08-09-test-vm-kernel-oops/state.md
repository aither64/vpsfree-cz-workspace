# 2026-08-09-test-vm-kernel-oops

## Repositories

- `vpsadminos`
  - branch: `2026-08-09-test-vm-kernel-oops`
  - worktree: `worktrees/2026-08-09-test-vm-kernel-oops/vpsadminos`
  - current base: `origin/staging` / `579737ac9`
  - current head: `cf1994bfb`
- `vpsadmin`
  - branch: `2026-08-09-test-vm-kernel-oops`
  - worktree: `worktrees/2026-08-09-test-vm-kernel-oops/vpsadmin`
  - current base: `origin/master` / `a0e2c7af4`
  - current head: `5ceadff4b`
- `vpsadminos-org-configuration`
  - branch: `2026-08-09-test-vm-kernel-oops`
  - worktree:
    `worktrees/2026-08-09-test-vm-kernel-oops/vpsadminos-org-configuration`
  - base: `origin/master` / `10330b7a2`
  - head: `3fd69cc`
- `vpsfree-cz-configuration`
  - branch: `2026-08-09-test-vm-kernel-oops`
  - worktree:
    `worktrees/2026-08-09-test-vm-kernel-oops/vpsfree-cz-configuration`
  - base: `origin/master` / `8888cc735`
  - head: `f25dc345`

## Status

- The Linux 6.18 guest-kernel detector and udev serialization implementation
  is complete and was previously reviewed by a standalone agent.
- The vpsAdminOS branch was rebased onto current `origin/staging`; its rewritten
  detector commits are `651aa87bc` and `8e3d6db57`.
- The lifecycle candidate checksum was removed because current module bytes
  follow the current locked kernel/toolchain inputs. Historical predecessor
  checksums remain.
- Lifecycle CI now selects the existing `vpsAdminOS runners` group using
  `intel-kvm` and `amd-livepatch`. Existing runners 1-3 are unchanged.
- `gh-runner4.int.vpsadminos.org` is configured at `172.16.4.31` without
  default GitHub labels and with only `amd-livepatch`.
- VPS 30102 is operational inventory only; the user will place it on an AMD
  production node and provision its runner secret before activation.
- Internal DNS contains the runner4 A record with zone serial `2026081001`.
- Obsolete CI run `31324312195` is cancelled. Its AMD job was permanently
  queued for the retired `self-hosted,Linux,X64,amd-kvm` selector.
- Current vpsAdminOS CI run `31380014093` is waiting only for AMD job
  `93428443248`. Current vpsAdmin integration run `31380971998` is still
  active.
- All four feature branches are published. The vpsAdmin pin was rebuilt from
  current `origin/master` with the repository helper after publishing the
  final vpsAdminOS SHA.

## Commits

- vpsAdminOS:
  - `651aa87bc tests: serialize NixOS udev workers`
  - `8e3d6db57 tests: fail on guest kernel failures`
  - `cf38f27a7 tests/kernel: stop hashing livepatch candidates`
  - `cf1994bfb ci: reserve AMD runner for livepatch checks`
- vpsadminos-org-configuration:
  - `3fd69cc cluster: add dedicated AMD livepatch runner`
- vpsfree-cz-configuration:
  - `f25dc345 internal-dns: add gh-runner4.int.vpsadminos.org`
- vpsAdmin:
  - `5ceadff4b flake: vpsadminos 837baf040 -> cf1994bfb`

## Verification

- Earlier implementation verification:
  - focused osvm specs: 47 examples, 0 failures;
  - focused test-runner specs: 18 examples, 0 failures;
  - full osvm specs: 108 examples, 0 failures;
  - full test-runner specs: 182 examples, 0 failures;
  - RuboCop passed on the changed Ruby files;
  - evaluated NixOS test VM parameters contain both
    `rd.udev.children_max=1` and `udev.children_max=1`;
  - crashdump integration passed all three scripts with expected panic
    allowances;
  - `kernel/module-autoload` passed all 16 examples;
  - vpsAdmin `services-up` passed all 27 examples;
  - GitHub RSpec, RuboCop, client, libnodectld, WebUI PHPUnit, and i18n checks
    passed on the previously published heads.
- Current follow-up quick verification:
  - vpsAdminOS Nix formatting and `git diff --check` passed;
  - `actionlint` passed while ignoring only its unknown-custom-label diagnostic
    for `amd-livepatch` and the pre-existing `intel-kvm`;
  - no `candidateSha256` or `CANDIDATE_SHA256` references remain;
  - runner configuration Nix formatting passed;
  - `confctl ls` lists `org.vpsadminos/int.gh-runner4`;
  - `named-checkzone` loaded serial `2026081001` successfully, with only the
    repository's expected `@fqdn@` warning;
  - Overcommit hooks are installed and passed all four follow-up commits.
  - `confctl build -y org.vpsadminos/int.gh-runner4` built generation
    `2026-08-10--12-33-03` successfully;
  - `confctl build -y -t internal-dns` built both internal nameservers in
    generation `2026-08-10--12-33-54` successfully.
  - the final vpsAdmin `services-up` VM integration test passed all 27
    examples against vpsAdminOS `cf1994bfb` in 453.15 seconds;
  - vpsAdminOS RSpec and RuboCop Actions passed on `cf1994bfb`;
  - the Intel livepatch lifecycle job and the generic full suite passed on
    `cf1994bfb`; the AMD lifecycle job is correctly queued for runner4;
  - the generic suite ran on runner1 and completed its test-state cleanup step
    successfully;
  - vpsAdmin RuboCop, WebUI PHPUnit, migration specs, client specs, i18n,
    libnodectld, and all 26 topic-parallel API shards passed on `5ceadff4b`;
    its selected integration-test workflow remains in progress with no failure
    reported. Comparable successful runs take several hours.
  - repository job metadata confirms the Intel lifecycle job ran on runner2
    with `intel-kvm`, the generic suite ran on runner1 with `self-hosted`, and
    the unassigned AMD job requests only `amd-livepatch`;
  - organization-wide runner inventory could not be read because the active
    GitHub token lacks the required Actions administration scope. Repository
    job metadata remains sufficient to verify current workflow routing.
- The root filesystem reached the non-root reserve while another session built
  a KVM initrd. Removing only this initiative's caches was insufficient; after
  that active build completed, standard `nix-store --gc` removed unreferenced
  cache paths and restored 261 GiB free. No project data was removed.

## Review and rollout

- Mandatory follow-up change review completed with no Blocking, Important, or
  Advisory findings. It confirmed the checksum policy, runner routing,
  unchanged runners 1-3, additive DNS/configuration, compatibility assumptions,
  and commit split.
- Residual review gaps are hardware and registration preflight, the AMD half
  of dual-vendor CI, AMD QEMU cleanup, host KVM/SVM log inspection, and the
  terminal result of the still-running vpsAdmin selected integration tests.
- Next: preflight and activate runner4 after the user places VPS 30102 on an
  AMD node and provisions its runner secret. Then monitor the AMD lifecycle
  job through cleanup and inspect the host node's KVM/SVM log.
- Before runner activation, verify `AuthenticAMD`, `svm`, `npt`, `nrip_save`,
  usable `/dev/kvm`, and no IP conflict inside VPS 30102.
- After the first AMD lifecycle run, verify runner/QEMU cleanup and inspect the
  host node for KVM/SVM faults.

## Cleanup

- Worktrees remain active until validation, default-branch integration, and
  deployment are complete.
- Feature branches must be retained after merge.
