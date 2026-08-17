# 2026-08-17-image-build-failures

## Repositories

- `vpsadminos`
  - branch: `2026-08-17-image-build-failures`
  - worktree: `worktrees/2026-08-17-image-build-failures/vpsadminos`
  - base: `origin/staging` at `563d08fb951b624078c3f1bf4e5b817c641be0be`

## Status

- All sixteen implementation commits, quick verification, and mandatory review
  are complete. The reviewed feature branch is pushed. RuboCop passed; the
  expensive integration workflows are externally blocked before checkout by
  an active GitHub Actions incident.

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
- vpsAdminOS commit series from base `563d08fb9` to head `37212611d`:
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

## Open questions

- None. The current musl stage3 archives still contain 1,508,934,142 bytes
  under `/opt/rust-bin-1.95.0`; the implemented temporary, dependency-checked
  Portage depclean avoids delaying the full workflow.

## Cleanup

- Keep the feature worktree until the branch is reviewed, pushed, tested, and
  integrated or explicitly abandoned.
