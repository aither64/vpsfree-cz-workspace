# 2026-08-17-image-build-failures

## Repositories

- `vpsadminos`
  - branch: `2026-08-17-image-build-failures`
  - worktree: `worktrees/2026-08-17-image-build-failures/vpsadminos`
  - base: `origin/staging` at `563d08fb951b624078c3f1bf4e5b817c641be0be`
  - current integration target: `origin/staging` at
    `b6b57f4866c0cbc74210d8464390a824467a24c1`
  - integration branch: `2026-08-17-image-build-failures-integrate`
  - integration worktree:
    removed after the fast-forward integration
  - integration head: `b6b57f4866c0cbc74210d8464390a824467a24c1`
  - follow-up branch: `2026-08-17-image-build-failures-followup`
  - follow-up worktree:
    `worktrees/2026-08-17-image-build-failures/vpsadminos-followup`
  - follow-up head: `7f5a0a05b5bc9c4381a8f5fd380aa5bb473d385e`
  - Guix draft worktree:
    removed after its commits were copied to the follow-up branch

## Status

- The 18 verified non-Guix commits passed a fresh mandatory review and were
  fast-forwarded to `staging` at `b6b57f486` with normal commit messages and
  normal GitHub triggers. Runs `32125885812` (images), `32125885934` (CI), and
  `32125885869` (RuboCop) started from the integrated head. A clean follow-up
  branch now contains only unresolved work.

- The Arch failure has an exact reproduced root cause in the unchanged Ruby
  exporter. `Zlib::GzipWriter#close` runs while the `zfs send` child exits;
  Ruby's `SIGCHLD` can interrupt zlib 3.2.3 during `Z_FINISH`, whose interrupted
  retry condition incorrectly requires input to remain. The call can therefore
  return success after writing the CRC/size footer but before writing the final
  deflate block. The planned focused fix moves compression to an external
  `gzip` pipeline, checks both child statuses, and adds a producer-exit/signal
  regression. The final focused fix is committed at `1c8e5affd`; quick
  verification passes and its standalone mandatory review returned PASS with
  no findings.

- The final Guix rewrite is committed at `4ffd22c8b` and `7f5a0a05b`. It
  replaces Debian Guix 1.4 with `guix:latest`, resolves the newest authenticated
  default-branch revision with Guix CI pull substitutes at build time, performs
  one `guix time-machine ... system init`, and separately module-qualifies the
  delayed service binding. There is no maintained repository revision pin.
  Fast checks and hooks pass; the detector selects only Guix. A fresh final
  mandatory review returned PASS with no Blocking, Important, or Advisory
  findings. The continuation branch was updated with force-with-lease.

- The full follow-up review found one Important exporter lifecycle issue:
  Open3 starts `zfs send` before attempting the next pipeline process, so a
  missing gzip could strand the producer until garbage collection. The exporter
  now resolves gzip before starting the pipeline, and a regression proves the
  producer never starts when resolution fails. The fix is folded into the
  exporter commit; its focused reviewer follow-up passed.

- The focused follow-up review confirmed the lifecycle fix and returned PASS
  with no findings. The clean branch was pushed normally at `4e3a2d7da`.
  GitHub runs `32129561366` (Guix image), `32129561380` (CI), `32129561419`
  (RSpec), and `32129561518` (RuboCop) started without skip directives.
  These runs are on the superseded pinned-Guix head. After the final
  force-with-lease update, cancel only runs that are still queued or running on
  that old SHA.

- An independent supported-consumer audit found no missing runtime compressor.
  osctld declares `pkgs.gzip` directly. osctl-image and scheduled repository
  builds execute with the vpsAdminOS system path, where GNU gzip is a mandatory
  core package. Fetched vpsAdmin `origin/master` at `d8ce525fa`; it has no
  `Exporter::Zfs` or `ct_export` caller, so it needs no change. The standalone
  libosctl gem now records GNU gzip as a conditional
  requirement for gzip-compressed ZFS exports. The legacy OpenVZ converter is
  intentionally out of scope by user decision.

- The original 24-commit implementation is reviewed and pushed at
  `b0eeed852`. Final
  image run `32094157385` completed all 51 tests: 49 passed, Arch failed after
  a successful build because its exported gzip/ZFS stream was truncated, and
  Guix failed deterministically after both pulls succeeded because current
  Guix could not resolve the delayed `%ct-services` binding. The later Arch
  investigation identified and reproduced Ruby zlib's interrupted gzip
  finalization as the exact cause. The integration plan separates the 18
  verified commits from a clean follow-up branch for the exporter and Guix.
  Guix will self-host from the last published Guix image and dynamically
  select a CI-substitutable authenticated default-branch revision; no standing
  recovery builder will be kept.

- Historical implementation progress follows. The original sixteen
  implementation commits are reviewed and pushed.
  RuboCop and the main CI suite passed. Image workflow attempt 4 built and
  tested 48 of 51 images successfully. Two Slackware compatibility fixes and
  Guix failure-log diagnostics are committed, locally verified, and passed the
  follow-up mandatory review. The targeted workflow then passed both
  Slackwares and exposed Guix's exact Guile compatibility failure. An
  authenticated Guix 1.4 bridge is committed, locally verified, and passed
  mandatory review. Guix-only workflow run `32085757382` proved that bridge
  succeeds, then exposed an isolated channel-file compatibility issue. The
  two focused Guix follow-ups are committed and passed quick verification.
  Their full-series review found a separate partial chroot-mount failure and
  missing detector self-trigger. Both findings are fixed in three focused,
  hook-verified commits. A follow-up review found unsafe shared-mount cleanup
  and two direct callers that masked failures. The next review confirmed the
  mount barrier and Arch fix, but found OpenSUSE still disabled `errexit` by
  invoking its bootstrap in a conditional context and noted that a failed
  safety barrier could leave a mount in the reusable builder namespace. Both
  findings are fixed. The final fresh full-series review passed with no
  findings; the reviewed follow-up is ready to push for the 51-image workflow.

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
- `gh run download 32094157385 ...`
- Current-versus-prior Arch artifact comparison
- Guix pull/system-init boundary and upstream module-loader history analysis
- Public vpsAdminOS image index inspection for the latest Guix artifact
- `git fetch origin staging`
- Clean cherry-pick of the 18 non-Guix commits onto `7f50e2d43`
- Integration-tree Bash/Ruby syntax and common-helper regression
- Integration-tree 51-image detector matrix and `git diff --check`
- Integration-tree Nix image-repository evaluation
- Integration-tree `nix develop --command overcommit --run`
- Fast-forward push of integration head `b6b57f486` to `origin/staging`
- Removal of the temporary integration worktree and creation of the clean
  follow-up branch/worktree from integrated `origin/staging`
- Focused Ruby zlib producer-exit reproduction and signal stress test
- Focused libosctl exporter spec and targeted RuboCop
- Built the libosctl gem and inspected its GNU gzip requirement metadata
- Independent supported-consumer gzip PATH audit across current default refs
- Full follow-up-tree `nix develop --command overcommit --run`
- Force-with-lease update of the unmerged continuation branch to `7f5a0a05b`
- Cancellation of superseded old-head image and CI workflows
- Guix builder/image configuration resolution and Scheme parsing
- Mocked Guix time-machine success, status-42 failure, and build-log extraction
- Final follow-up detector run against integrated `origin/staging`
- Normal push of the new follow-up branch at `4e3a2d7da`
- Targeted analysis of the Guix and Slackware failure artifacts
- `nix develop --command overcommit --run`
- ShellCheck 0.11 through `nix shell nixpkgs#shellcheck`
- Official Guix and Guile history inspection in filtered temporary clones
- Targeted workflow run `32081719754` and artifact inspection
- Guix-only workflow run `32085757382` and artifact inspection
- Guix 1.4-style and isolated safe-binding channel-file evaluation
- Synthetic Guix bridge/rolling retry, status, profile activation, and version
  detection matrix
- Permanent common chroot helper regression covering setup, mount, chroot, and
  cleanup failure precedence
- Isolated real-mount propagation-barrier check and actual OpenSUSE/Arch caller
  failure checks
- Disposable image-runner mount-namespace argument, status, recursion, and
  teardown checks
- Actionlint and detector self-change/full-matrix checks
- Official `actions/checkout` latest-release verification

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
- `origin/staging` advanced from the recorded base to `7f50e2d43` through the
  scheduled mechanical commit `flake: nixpkgs 02e08985a -> 0dd31db7e`. It does
  not overlap the image-script changes. The integration slice must be rebuilt
  and reviewed on this current target before fast-forwarding.
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
- Guix-only run `32085757382` authenticated and built the pinned bridge, then
  the bridge Guix rejected the rolling channel file before fetching it:
  isolated channel evaluation intentionally does not expose `use-modules`.
  Both Guix 1.4 and the isolated loader already provide the safe channel
  bindings, so the redundant import is removed from both channel files.
- The same run showed a nonfatal broken-pipe backtrace from probing
  `guix --version` through `head`. The probe now uses `sed`, which consumes the
  full output while selecting the first line.
- Both channel files evaluate successfully under the Guix 1.4 loader model and
  the bridge's exact isolated safe-binding set. Tests assert the inherited
  authentication introduction, canonical URL, exact bridge pin, and unpinned
  rolling channel.
- The synthetic pull matrix covers retry success and exhaustion for bridge and
  rolling pulls, exact failure status propagation, profile command
  re-resolution, diagnostics, private temporary-file cleanup, and version
  output with thousands of trailing lines.
- `mount-chroot` now checks every operation explicitly even when called from a
  conditional context, preserves the first setup failure, skips `chroot`, and
  cleans only filesystems mounted by that invocation. A recursive `/dev` clone
  is made private before unmount; if the safety barrier fails, detachment is
  deferred to namespace teardown. Every image action is re-executed in a
  disposable private mount namespace, so an undetachable bind cannot persist
  in or poison the reusable builder. The wrapper preserves normal process
  status and signal behavior and fails closed if `unshare` is unavailable. All
  current builder bases normally include util-linux; an unusually old or
  minimized persistent builder may need that package installed or recreation.
  OpenSUSE invokes its `set -e` bootstrap outside a conditional context and
  preserves bootstrap-over-cleanup precedence, while Arch exits immediately on
  chroot failure.
- The permanent regression verifies all helper stages, both direct callers,
  the first failing OpenSUSE `zypper` command, chroot-over-cleanup status
  precedence, namespace-wrapper arguments and recursion, and propagation and
  teardown behavior with real isolated mounts.
- Changes to the detector script now trigger the image workflow and select all
  51 concrete images. The workflow runs the common-helper regression before
  calculating its image matrix.
- Final image run `32094157385` exercised all 51 selected images at reviewed
  head `b0eeed852` in 23,186 seconds. Forty-nine images passed. RuboCop run
  `32094157381` passed at the same head.
- Arch run `32094157385` completed its bootstrap and configuration with
  `build_status=0`; both chroot calls and every new mount cleanup returned 0.
  Import then reported `gzip: stdin: unexpected end of file` and an incomplete
  ZFS stream from `rootfs/base.dat.gz`. The prior full run imported the same
  Arch 2026.08.01 bootstrap and passed all 15 runtime tests in 552 seconds.
  Mount namespace isolation ends before the Ruby exporter writes the archive,
  so the evidence does not support an Arch or branch regression. No
  Arch-specific change is planned. General atomic export validation is recorded
  in `notes/vpsadminos/2026-08-18-truncated-image-zfs-stream.md`.
- Guix ran for 4,847.74 seconds. Debian Guix 1.4 authenticated and built the
  pinned bridge, the bridge Guix authenticated and built floating commit
  `f2b9872`, and both pulls returned 0. `guix system init` then failed with
  `%ct-services: unbound variable`. Upstream commit `94ae360ab403` changed
  configuration loading to use fresh anonymous modules; the operating-system
  services field is delayed and can no longer resolve the custom binding
  imported into the original module. The binding must be module-qualified.
- The public image index currently has Guix `20260613` tagged both `latest`
  and `stable`; it contains Guix 1.5 and the running Guix daemon. The planned
  normal builder therefore uses `DISTNAME=guix`, `RELVER=latest`. It will run
  one exact authenticated revision through `guix time-machine`, selected only
  after channel substitutes exist. The Debian 1.4 builder, bridge, double pull,
  and version compatibility path will be removed.
- The user explicitly chose not to maintain a NixOS or other recovery builder.
  The last known-good dated Guix image remains available and can be selected
  manually for exceptional recovery.
- The user rejected a `skip-checks: true` integration trailer. All commits keep
  ordinary messages and the `staging` push will use normal GitHub triggers,
  even though shared runtime and detector changes schedule all 51 images.
- The user also rejected truncated-stream classification as an Arch root-cause
  explanation and requested integration first. The verified slice was merged
  before the exporter change. The subsequent investigation reproduced the
  exact Ruby zlib finalization race; no retry-only or Arch-specific workaround
  is planned.
- A fresh integration worktree was created from current `origin/staging`. The
  18 non-Guix commits cherry-picked cleanly in their original order. Excluding
  the six omitted Guix commits and the staging `flake.lock` update, its tree is
  byte-identical to reviewed feature head `b0eeed852`. Shell and Ruby syntax,
  the permanent common-helper regression, the 51-image detector matrix,
  `git diff --check`, the Nix image-repository evaluation, and full Overcommit
  all pass. A fresh standalone mandatory review returned PASS with no blocking,
  important, or advisory findings. The series was fast-forwarded to `staging`
  at `b6b57f486`, and the temporary integration worktree was removed.
- The failing gzip member retains the correct CRC and ISIZE footer for the
  complete input but lacks the final deflate block. The repository's exact
  `IO.popen`/32 KiB `GzipWriter` shape reproduced silent corruption after as
  few as two iterations. Without an exiting child it passed 1,000 iterations;
  reaping the producer before finalization also passed 1,000. An external gzip
  pipeline passed 1,000 producer-exit iterations and 50 signal-bombarded
  iterations. Ruby zlib 3.2.3 commit `c975060` retries interrupted work only
  while both input and output remain, although `Z_FINISH` must continue with
  zero input until `Z_STREAM_END`.
- Rewritten commit `1c8e5affd` replaces Ruby gzip finalization with an external
  pipeline, copies compressed output into the unchanged tar member, and
  reports every failed or signaled stage. Its spec exercises `zfs send` status
  23, `gzip` status 29, and six 1 MiB streams while repeatedly delivering real
  `SIGCHLD`; every decompressed byte is checked. A harness of the removed
  implementation corrupted 23 of 25 streams under the same signal loop, while
  the new example passed ten process-level repetitions covering 60 streams.
- Gzip executable resolution now happens before Open3 starts the producer. The
  missing-compressor regression raises `ENOENT` and verifies that the fake
  `zfs send` start marker is never created. The exporter spec now has twelve
  examples and passes on the rewritten head; full Overcommit passes again.
- The mandatory reviewer reproduced the original partial-pipeline lifecycle
  issue, then verified the preflight fix. Its follow-up verdict is PASS with no
  blocking, important, or advisory findings.
- The focused exporter mandatory review returned PASS with no blocking,
  important, or advisory findings. It independently verified the spec and the
  declarative vpsAdminOS gzip dependency. A later exhaustive audit confirmed
  every supported caller has gzip in its declared runtime environment. The
  user excluded the retired OpenVZ converter from further work.
- Rewritten commits `4ffd22c8b` and `7f5a0a05b` implement the Guix self-host
  and loader compatibility changes. `channels.scm` follows the authenticated
  default channel without a revision pin. A separate resolver chooses the
  newest revision with Guix CI pull substitutes and the build passes that
  validated commit to one time-machine invocation. Bash syntax, focused
  ShellCheck, Guile parsing, published-runtime resolution, mocked success and
  diagnostic failures, `git diff --check`, and full Overcommit pass.
- The edited workflow uses `actions/checkout@v7`; GitHub's official latest
  release is `v7.0.1`.
- vpsAdminOS commit series from base `563d08fb9` to head `b0eeed852`:
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
  - `5768d848d` image-scripts/guix: support isolated channel evaluation
  - `8be6a707a` image-scripts/guix: avoid a version probe broken pipe
  - `42bf2e131` image-scripts: fail closed on partial chroot mounts
  - `851d8c151` github: run common image helper regression
  - `b0eeed852` github: test image detector changes

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
- Full-series review through `8be6a707a`: **FAIL**. The two Guix commits had no
  finding, but the reviewer reproduced a blocking partial-mount failure masked
  by conditional-context `errexit` behavior in `common.sh`. The reviewer also
  reported that detector-only changes did not trigger the image workflow.
- Follow-up commits explicitly preserve and clean partial mount failures, add
  permanent regression coverage, run it in the workflow, and make detector
  changes trigger and conservatively select all concrete images.
- Follow-up review through the first chroot fix: **FAIL**. It reproduced
  recursive `/dev` unmount propagation when `make-rslave` failed and confirmed
  OpenSUSE and Arch could still mask helper failures.
- The chroot commit was rewritten before push to establish a private
  propagation barrier, defer unsafe detachment, preserve both direct-caller
  failures, and cover these paths with mocked and isolated real-mount tests.
- Follow-up review through `b728eeab5`: **FAIL**. It confirmed the private
  barrier and Arch propagation, but reproduced OpenSUSE continuing after its
  first failing `zypper` command because `do_bootstrap` was called on the left
  of `||`. It also found that an undetachable bind would outlive the build in
  the persistent builder namespace.
- The unpublished chroot and regression commits were rewritten again.
  OpenSUSE now captures a standalone `do_bootstrap` invocation, the regression
  uses the actual bootstrap with a first-command failure, and image actions run
  under `unshare` in a disposable private mount namespace. Quick syntax,
  ShellCheck, focused regression, `git diff --check`, and full Overcommit checks
  pass.
- Final fresh full-series review through `b0eeed852`: **PASS** with no Blocking,
  Important, or Advisory findings. The reviewer independently ran the real
  mount branch, focused helper and detector matrices, Fedora discovery, Nix
  repository evaluation, syntax/diff checks, and Overcommit. The required
  residual coverage is the intentionally deferred 51-image workflow, including
  real `unshare` permission in every builder and the final Guix rolling pull.
- Final fresh follow-up review through `7f5a0a05b`: **PASS** with no Blocking,
  Important, or Advisory findings. It independently reran the exporter spec,
  confirmed executable availability and gem metadata, checked the dynamic Guix
  resolver and authentication semantics, and repeated syntax, Scheme, diff,
  and hook checks. Residual integration coverage is the targeted Guix image
  build, import, and runtime test.

## GitHub Actions

- Pushed branch `2026-08-17-image-build-failures` and its clean worktree are at
  reviewed head `b0eeed852`.
- Final full-matrix runs:
  - RuboCop passed:
    https://github.com/vpsfreecz/vpsadminos/actions/runs/32094157381
  - Image workflow completed 49/51 successfully:
    https://github.com/vpsfreecz/vpsadminos/actions/runs/32094157385
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
    failed after 1 hour 8 minutes on reviewed commit `97bbf2d13`. The bridge
    authenticated, built, and activated successfully; all three rolling pull
    attempts then failed deterministically on the redundant `use-modules`
    form before any rolling channel fetch.
  - The next push includes a shared `common.sh` correction and detector logic,
    so the selector intentionally expands to all 51 concrete images. The Guix
    result remains independently identifiable within that resource-aware run.
  - Run `32094157385` completed after 6 hours 28 minutes. Its artifact was
    downloaded before classifying Arch as a truncated export and Guix as a
    post-pull module-scope incompatibility.
  - The `staging` integration push will use ordinary commit messages and
    normal workflow triggers. The detector will therefore schedule all 51
    images again. No commit-message skip directive will be used.
  - Final continuation head `7f5a0a05b` started runs `32132207935` (changed
    images), `32132207974` (CI), `32132207952` (RSpec), and `32132208000`
    (RuboCop). Superseded old-head runs `32129561366` and `32129561380` were
    cancelled after the force-with-lease update; completed old-head RSpec and
    RuboCop runs were left intact.

## Decisions and remaining work

- The current musl stage3 archives still contain 1,508,934,142 bytes under
  `/opt/rust-bin-1.95.0`; the implemented temporary, dependency-checked Portage
  depclean passed both musl image jobs.
- Integrate the reviewed non-Guix slice on current `origin/staging`, after quick
  verification and a fresh mandatory review, without repeating the 51-image
  workflow.
- Monitor the final follow-up workflows. Confirm the image detector selects
  only Guix, inspect any failure artifact, and inspect the successful artifact
  before integration.
- Fast-forward the exporter and Guix follow-up into current `staging` only
  after targeted workflows pass.

## Cleanup

- Keep the feature worktree until the branch is reviewed, pushed, tested, and
  integrated or explicitly abandoned.
