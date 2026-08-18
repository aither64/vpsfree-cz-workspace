# 2026-08-17-image-build-failures

## Repositories

- `vpsadminos`
  - branch: `2026-08-17-image-build-failures`
  - worktree: `worktrees/2026-08-17-image-build-failures/vpsadminos`
  - base: `origin/staging` at `563d08fb951b624078c3f1bf4e5b817c641be0be`

## Status

- The original sixteen implementation commits are reviewed and pushed.
  RuboCop and the main CI suite passed. Image workflow attempt 4 built and
  tested 48 of 51 images successfully. Two Slackware compatibility fixes and
  Guix failure-log diagnostics are committed, locally verified, and passed the
  follow-up mandatory review. The targeted workflow then passed both
  Slackwares and exposed Guix's exact Guile compatibility failure. An
  authenticated Guix 1.4 bridge is committed, locally verified, and passed
  mandatory review. Guix-only workflow run `32085757382` is now in progress
  on the exact reviewed commit.

## Commands run

- `bin/dev-session current`
- `bin/dev-session worktree add 2026-08-17-image-build-failures vpsadminos --as-is --branch 2026-08-17-image-build-failures --base origin/staging`
- `git commit -F /tmp/vpsadminos-image-build-commit-msg` (blocked by
  Overcommit because ambient PATH did not contain RuboCop)
- `ruby skills/update-redhat-family-image-releases/scripts/discover_release_updates.rb fedora`
- `nix eval --impure --raw --file tests/nixos-container-image-repository-eval.nix`
- `nix develop --command overcommit --run`
- Changed-image detection against `origin/staging...HEAD`
- Metadata-only exact package resolution against Slackware 15.0 and current
- Synthetic image runner failure propagation using an isolated temporary copy
- `gh run view 32037034898 ...`
- `gh run download 32037034898 ...`
- Targeted analysis of the Guix and Slackware failure artifacts
- `nix develop --command overcommit --run`
- ShellCheck 0.11 through `nix shell nixpkgs#shellcheck`
- Official Guix and Guile history inspection in filtered temporary clones
- Targeted workflow run `32081719754` and artifact inspection

## Results

- Active session slug and environment match.
- Canonical vpsAdminOS remote uses SSH.
- Worktree created from the latest fetched `origin/staging`.
- Overcommit is installed and active in the canonical bare repository. Final
  commits must run through `nix develop --command git commit ...` so all hook
  tools are available.
- Fedora discovery reports Fedora 43 suffix 25, Fedora 44 suffix 17, and
  Rawhide 46-0.1 current; Fedora 42 is absent.
- Fedora 42 is absent from script discovery and the repository configuration;
  the shared Fedora builder reports release 44.
- The Nix image-repository evaluation succeeds.
- Common chroot failure/cleanup status precedence passed a stubbed shell test.
- All 90 declared packages resolve exactly once with one checksum on both
  Slackware 15.0 and current. Metadata indexing takes about 0.2 seconds and
  resolving all packages about 1.5 seconds per release.
- Bash syntax, Ruby syntax/RuboCop, Scheme parsing, `git diff --check`, Nix
  evaluation, and the full Overcommit run pass.
- Isolated synthetic build scripts verify both runner paths: an explicit status
  37 is propagated unchanged, and `set -e` exits on a failing command with
  status 1. Neither failure writes `container.yml`.
- The temporary Gentoo musl workaround uses Portage to depclean `rust-bin`,
  verifies that its package and payload data are gone, and is marked for
  removal once refreshed musl stage3 archives stop shipping it.
- CI change detection selects all 51 concrete images for the shared runner and
  `common.sh` changes, including the consumers omitted by the first review;
  abstract templates and Fedora 42 are excluded.
- The latest fetched `origin/staging` remains at the recorded base and is an
  ancestor of the feature branch.
- Main CI run `32037034981` attempt 3 passed its system build, core test suite,
  AMD livepatch, and Intel livepatch jobs. RuboCop run `32037034986` passed.
- Image run `32037034898` attempt 4 passed 48 of all 51 selected concrete
  images. Fedora 43, Fedora 44, Fedora Rawhide, and both Gentoo musl variants
  passed. Only Guix, Slackware 15.0, and Slackware current failed.
- Both Slackware jobs completed the hardened download, checksum, package
  resolution, and deterministic install stages. The freshly installed
  `slackpkg` was already current, so its first upgrade returned documented
  no-op status 20. The new configuration failure propagation exposed this
  benign status. Upgrade commands now accept only statuses 0 and 20; every
  other status and all update/configuration commands remain fail-fast.
- Guix reached the canonical repository, authenticated channel commit
  `53d0ba4`, and failed identically on all three attempts while Debian Guix
  1.4.0-9 compiled `module-import-compiled.drv`. The runner had ample memory
  and disk, with no OOM, ENOSPC, or network evidence. The referenced Guix
  derivation log was destroyed with the builder before artifact collection.
  Pull output is now captured privately and referenced plain/compressed build
  logs are emitted before retries and final exit so the next run can expose
  the exact Guile exception without changing retry or success behavior.
- Follow-up change detection from the pushed head selects exactly
  `guix,slackware-15.0,slackware-current`.
- Targeted image run `32081719754` passed Slackware 15.0 in 842 seconds and
  Slackware current in 736 seconds. Guix remained the only failure.
- The emitted Guix derivation log identifies `spawn: unbound variable` while
  compiling `(guix ui)`. Official sources confirm Guix 1.4's self-build uses
  Guile 3.0.8, `spawn` was added in Guile 3.0.9, and Guix commit `a6094158`
  first references it. Commit `a6094158` has sole parent `6c03bb1d`, which
  does not reference `spawn` and whose self-build selects Guile 3.0.11.
- Guix 1.4 now performs an authenticated pull to `6c03bb1d` before the normal
  unpinned rolling pull. The bridge is skipped for newer Guix versions and is
  marked for removal when the Debian builder moves beyond Guix 1.4.
- vpsAdminOS commit series from base `563d08fb9` to head `97bbf2d13`:
  - `219d09ae6` github: fix concrete image change detection
  - `4b9866571` github: detect image builder changes
  - `1cabaee99` image-scripts: update Fedora builder to 44
  - `675335039` image-scripts, image-repository: remove fedora-42
  - `417e15190` image-scripts: fail on HTTP errors downloading release RPMs
  - `f7829e999` image-scripts: update fedora-rawhide release to 46-0.1
  - `a6b0031ae` image-scripts: preserve chroot configuration failures
  - `389f2239c` image-scripts: share Slackware image bootstrap
  - `4fb129568` image-scripts/slackware: fail on configuration errors
  - `e49eaa480` image-scripts/slackware: make downloads atomic and retried
  - `77723fe6e` image-scripts/slackware: resolve exact package metadata
  - `9c6d05de9` image-scripts/slackware: fail closed during package install
  - `d478c7e50` image-scripts: use the canonical Guix channel
  - `18e626751` image-scripts/guix: retry channel pulls
  - `fc799d081` image-scripts/gentoo: depclean temporary Rust toolchain
  - `37212611d` github: test shared image runtime changes
  - `f560a84` image-scripts/slackware: accept empty upgrades
  - `34e44b7b9` image-scripts/guix: emit failed pull build logs
  - `97bbf2d13` image-scripts/guix: bridge pulls from Guix 1.4

## Mandatory review

- First completed review: **FAIL**.
- Blocking findings:
  - `image-scripts/bin/runner` overwrote sourced build-script failures;
  - CI omitted indirect consumers of `common.sh` and runner changes;
  - Slackware configuration handling and Guix retries were combined with
    independently reviewable changes.
- Follow-up:
  - failure propagation is now part of the common helper commit and passed an
    end-to-end synthetic runner check;
  - shared runtime changes select all concrete images;
  - Slackware configuration, Slackware package bootstrap, Guix channel, and
    Guix retry changes are separate commits.
- Second completed review: **FAIL**.
- Blocking findings:
  - sourcing the build script on the left side of `||` disabled `set -e` inside
    sourced scripts;
  - the Slackware package hardening commit still combined transport, metadata,
    and installation behavior.
- Follow-up:
  - the runner now sources the script as a standalone command and immediately
    captures its status; both explicit-status and `set -e` synthetic cases
    pass;
  - Slackware atomic downloads, exact metadata resolution, and deterministic
    failure-aware installation are separate commits; the final file remains
    byte-identical to the previously verified result.
- Third completed review: **PASS** with no Blocking, Important, or Advisory
  findings.
- Residual integration coverage is intentionally delegated to GitHub Actions:
  all 51 selected image builds, including Guix pull, Gentoo depclean and size,
  and Slackware bootstrap and configuration.
- Follow-up review of commits `f560a84d1` and `34e44b7b9`: **PASS** with no
  Blocking, Important, or Advisory findings. The reviewer confirmed the
  Slackpkg status handling is limited to upgrade operations, Guix preserves
  pull/retry outcomes, and keeping both focused follow-ups separate improves
  reviewability.
- Mandatory review of Guix bridge commit `97bbf2d13`: **PASS** with no
  Blocking, Important, or Advisory findings. The reviewer confirmed the
  authenticated pin, 1.4-only selection, profile activation, unpinned final
  pull, and final-image channel handling.

## GitHub Actions

- Pushed branch `2026-08-17-image-build-failures` at `37212611d`.
- Active runs:
  - RuboCop: https://github.com/vpsfreecz/vpsadminos/actions/runs/32037034986
  - CI: https://github.com/vpsfreecz/vpsadminos/actions/runs/32037034981
  - Build and test changed container images:
    https://github.com/vpsfreecz/vpsadminos/actions/runs/32037034898
- First attempts:
  - RuboCop passed.
  - CI and the image workflow failed during runner setup before checkout.
    Both self-hosted runners received HTTP 429 from `codeload.github.com` on
    all three attempts to download `actions/checkout@v7`; no repository code
    or image job ran.
  - Failed logs were inspected and confirm the common external rate-limit
    cause. Both failed jobs were rerun with the same head SHA.
  - The immediate second attempts failed identically during action download;
    wait for the codeload rate limit to clear before another attempt.
  - A third image-workflow attempt after a short cooldown also failed at the
    same pre-checkout point.
  - GitHub Status reports an active incident affecting Actions, API requests,
    and webhooks since 2026-08-17 13:40 UTC, which matches the timing and
    symptoms: https://www.githubstatus.com/incidents/zkxwbgr0cnmx
  - Do not change checkout logic for this external outage; monitor the incident
    and rerun after recovery.
  - The incident remained active through 2026-08-17 14:20 UTC. No image or CI
    test command ran in any failed attempt.
  - After GitHub marked Actions operational, the user requested new retries.
    Image workflow attempt 4 and CI attempt 3 both passed checkout and began
    their Nix build steps at approximately 2026-08-17 19:18 UTC.
  - CI attempt 3 and RuboCop completed successfully.
  - Image workflow attempt 4 completed after about 3 hours 47 minutes. It
    passed 48 of 51 images; artifact `os-test-logs-32037034898` was downloaded
    and the three failures were investigated before preparing fixes.
  - The next push changes only Guix and the two concrete Slackware images, so
    change detection should run those three image tests rather than all 51.
  - Targeted run https://github.com/vpsfreecz/vpsadminos/actions/runs/32081719754
    passed both Slackware variants and failed only Guix. The new diagnostics
    successfully preserved the inner derivation log before builder cleanup.
  - The next push changes only Guix files, so change detection should select
    only `image-scripts/test@guix`.
  - Guix-only run https://github.com/vpsfreecz/vpsadminos/actions/runs/32085757382
    started on reviewed commit `97bbf2d13`.

## Open questions

- The current musl stage3 archives still contain 1,508,934,142 bytes under
  `/opt/rust-bin-1.95.0`; the implemented temporary, dependency-checked Portage
  depclean passed both musl image jobs.
- The Guix 1.4 authenticated bridge has synthetic coverage but still requires
  a real image build to validate substitute, network, and two-stage pull
  behavior.

## Cleanup

- Keep the feature worktree until the branch is reviewed, pushed, tested, and
  integrated or explicitly abandoned.
