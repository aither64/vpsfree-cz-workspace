# 2026-08-10-update-vpsadminos-consumers

## Status

- Initiative created from the verified `2026-08-08-dns-caa-record` shell
  without touching that session's worktrees.
- Published integration inputs:
  - vpsAdminOS `2026-08-09-test-vm-kernel-oops` / `67fcc1737`;
  - vpsAdmin `2026-08-09-test-vm-kernel-oops` / `8b883cfb5`;
  - vpsadminos-org-configuration `2026-08-09-test-vm-kernel-oops` /
    `3fd69cc`;
  - vpsfree-cz-configuration `2026-08-09-test-vm-kernel-oops` /
    `f25dc345`.
- Consumer inventory from current default branches:
  - direct vpsAdminOS input: `vpsadmin`, `confctl`;
  - followed through vpsAdmin: `terraform-provider-vpsadmin`,
    `vpsadmin-kb-captures`, `vpsfree-irc-bot`;
  - explicitly requested configuration channels:
    `vpsfree-cz-configuration`.
- All requested default branches are merged and published.
- All temporary worktrees have been removed. Feature branches remain locally
  and remotely as required.

## Repositories

- `vpsadminos`
  - integrated published branch `2026-08-09-test-vm-kernel-oops`;
  - default `staging`: `67fcc17372d175b036706a1459a8b471bfc225e0`.
- `vpsadmin`
  - integrated published branch `2026-08-09-test-vm-kernel-oops`;
  - default `master`: `8b883cfb5bcfba263b318f2064f314672bf9dcf2`.
- `confctl`
  - feature branch: `2026-08-10-update-vpsadminos-consumers`;
  - commit/default `master`:
    `6ed1715c27ed1aa6264e9e90213afedb3df7a25f`.
- `terraform-provider-vpsadmin`
  - feature branch: `2026-08-10-update-vpsadminos-consumers`;
  - commit/default `master`:
    `54537973a7ba1a873580e8375ff2355948411896`.
- `vpsadmin-kb-captures`
  - feature branch: `2026-08-10-update-vpsadminos-consumers`;
  - commit/default `master`:
    `b670cf0f780e11c8a92451418710c2811c227cfe`.
- `vpsfree-irc-bot`
  - feature branch: `2026-08-10-update-vpsadminos-consumers`;
  - commit/default `master`:
    `88906fd54b0fc8cf613fc2cec2fb930d8196d05a`.
- `vpsadminos-org-configuration`
  - integrated published branch `2026-08-09-test-vm-kernel-oops`;
  - default `master`: `3fd69cc49bc64f3fb5d2d7b447fab3e7467a2e3b`.
- `vpsfree-cz-configuration`
  - feature branch: `2026-08-10-update-vpsadminos-consumers`, based on the
    published runner4 DNS feature;
  - generated channel commit: `0944ad46a33b69538a2fdfd3f6898d384512e850`;
  - default `master`: `0944ad46a33b69538a2fdfd3f6898d384512e850`.

## Verification

- All eight remote default refs were read back and exactly match the heads
  listed above.
- `vpsadmin`, `confctl`, `terraform-provider-vpsadmin`,
  `vpsadmin-kb-captures`, and `vpsfree-irc-bot` resolve vpsAdminOS
  `67fcc17372d175b036706a1459a8b471bfc225e0` in `flake.lock`.
- Followed consumers were updated with
  `nix flake update vpsadmin/vpsadminos`; their vpsAdmin revisions remain
  unchanged. In particular, the capture contract stays on vpsAdmin
  `63c2c44f6` while its test framework advances independently.
- confctl and IRC-bot Overcommit hooks passed inside their Nix development
  shells. Terraform and capture repositories declare no hook framework for
  this lock-only commit. `git diff --check` passed throughout.
- vpsfree.cz channels were updated only with:
  `confctl inputs channel update --commit --no-editor '*' vpsadminos`.
  The generated commit message was retained unchanged. `confctl inputs channel
  ls` reports `os-staging`, `production`, and `staging` at `67fcc173`.
- Existing validation carried into the merged series:
  - AMD livepatch lifecycle passed on runner4;
  - vpsAdminOS build and generic full suite passed;
  - the prior Intel lifecycle passed, while the final identical Intel path was
    still queued behind runner2 at integration time;
  - runner4 and internal DNS `confctl build` checks passed before deployment;
  - vpsAdmin `services-up` passed all 27 examples on the preceding framework
    head; the final change affects only the AMD lifecycle assertion.
- Default-branch GitHub quick workflows:
  - vpsAdminOS RSpec and RuboCop passed;
  - vpsAdmin client, WebUI PHPUnit, i18n, and libnodectld specs passed;
  - confctl RSpec and RuboCop passed;
  - IRC-bot RSpec passed.
- All previously queued self-hosted default-branch workflows completed
  successfully: vpsAdminOS run `31400699936`, vpsAdmin run `31400740738`,
  confctl run `31402089240`, Terraform provider run `31402095774`, and IRC-bot
  run `31402220153`.
- The mandatory review was not repeated: new commits are dependency-only or
  generated lock/channel updates, and the merged vpsAdminOS code series had
  already completed standalone review with no findings.
- Worktree creation and ambient pushes in Overcommit repositories can return
  nonzero after creating the worktree or fast-forwarding it. Exact worktree
  state was verified, configurations were signed, and commits/pushes were run
  inside the relevant Nix shell. Existing durable notes cover these cases.

## Merge and cleanup

- Every default branch was fetched immediately before integration and every
  feature was a descendant of the current target. Integration used
  `git merge --ff-only` in fresh target-branch worktrees.
- All 13 initiative worktrees were removed after remote-ref verification.
  Forced removal was limited to `.bundle`/`.bin` per-worktree caches in three
  worktrees. Project data and branch refs were retained.
- No deployment command was run. The configuration merge records runner/DNS
  state already deployed by the user and advances source channels only.
