# I0: vpsAdminOS image build and test investigation

Investigation only, 2026-11-04. Owner: implementer0. No application edits,
builds, test runs, CI, deployment, fetch/push, worktrees, branches or commits.
Only this evidence file was written. Session identity matched `dev-session
current`, both environment variables, and the trusted thread binding.

Source: canonical bare `repos/vpsadminos.git`, explicit immutable revision
`2951a632c4254a44747a8da326e3dde897eaa0e2`, observed
`refs/remotes/origin/staging` and symbolic `refs/remotes/origin/HEAD` target.
No freshness against GitHub is claimed. `origin/master` is the obsolete
2023 revision `4658d40f8ca459194b578aa30b0f9bb344cd7ee2`; local
`refs/heads/staging` was `49636f902704ce6019a7a8ae47ec0b3ca6902f68` and was
not treated as the remote-default baseline. All file:line citations below
refer to the immutable remote-tracking revision above, not peer worktrees.

Read workspace AGENTS, sessions/documentation/projects/verification/git
procedures, agent-teams, documentation/handoff skills; repository AGENTS,
README, image-scripts README, docs/index, container-images creating and
repositories, and docs/os/testing. Source inspection used `git show`,
`git grep`, `git ls-tree`, `git symbolic-ref`, and `git for-each-ref`.

## Findings

The missing connection is between two existing flows. Image-script tests
already build and test their target locally. General distribution tests
independently download images from the public default repository; they do
not consume the local build. The local archives are created successfully but
remain inside a disposable test VM whose disk is then deleted. Existing VM,
file-sharing and repository tools cover most of the required primitives.

### Build and image-script tests

1. `.github/workflows/image-scripts.yml:15-28` triggers on image scripts,
   their workflow/helpers, and NixOS container code. `:31-64` builds the OS
   and populates its binary cache. This caches the OS closure, not container
   image archives.
2. `:66-97` detects changed images; `scripts/changed-image-scripts.rb:89-175`
   expands direct image changes, symlink/abstract images, changed builders,
   shared helpers, and NixOS-specific inputs. `:124-135` maps a builder change
   to images using that builder. Selection currently does not include
   changes only under `osctl-image`, image-test definitions, or runner code
   in this workflow's path filter. Main CI is a separate workflow.
3. `image-scripts.yml:99-131` runs on `self-hosted`, with fresh run-specific
   state and `--jobs auto`, selecting `image-scripts/test@{...}`. No
   dependency connects its resulting archives to the separate CI workflow's
   distribution consumers.
4. `test-runner.sh:7-19` passes source root/revision and builds/invokes the
   packaged runner. `tests/all-tests.nix:91-103,231-234` instantiates one
   image-script case per concrete image directory or symlink.
5. `tests/suite/image-scripts/test.nix:20-54` boots a vpsAdminOS VM, allocates
   24 GiB RAM, creates build/output ZFS datasets, shares the source tree as
   `hostOs`, and calls `osctl-image ... test --build-dataset
   tank/image-scripts/build --output-dir /tank/image-scripts/output IMAGE`.
   The command timeout is three hours. The output directory is on the VM's
   `tank` disk, not a host output mount.
6. `osctl-image/lib/osctl/image/operations/test/image.rb:30-41` builds if
   needed, then executes tests. `operations/image/build.rb:133-227` creates
   ZFS work/output datasets, binds scripts and work paths into a builder
   container, runs `image-scripts/bin/runner`, fixes file capabilities, and
   exports the result. `build.rb:295-305` copies the supplied source for
   NixOS builders and records its revision.
7. `operations/test/run.rb:40-69` creates a fresh test container from the
   local exported stream/archive. `:75-90` runs each image test in its Nix
   shell; `:93-99` deletes test containers unless failed retention was
   requested. The CLI test command exits nonzero on failing tests
   (`cli/image.rb:60-67`). The target image itself need not be public.

There is an explicit bootstrap dependency. `operations/builder/create.rb:30-37`
creates the builder container from an existing configured repository image,
then enables nesting, adds networking and runs setup (`:56-97`). At this
revision the builder config files under `image-scripts/builders/*/config.sh`
declare these distribution/version pairs at lines 1-2:

| Builder | Bootstrap image |
| --- | --- |
| almalinux-8 / almalinux-9 | almalinux:8 / almalinux:9 |
| devuan | devuan:5 |
| fedora | fedora:44 |
| guix | guix:latest |
| nixos | nixos:unstable |
| opensuse-leap | opensuse:leap-16.0 |
| opensuse-tumbleweed | opensuse:latest-tumbleweed |
| ubuntu | ubuntu:24.04 |

For example, the new `opensuse-leap-16.1` target selects `opensuse-leap`
(`image-scripts/images/opensuse-leap-16.1/config.sh:1`), which bootstraps
16.0. It does not need an existing 16.1 image in order to build 16.1. These
are configured moving names/tags, not immutable bootstrap byte identities.

### Where a newly added distribution needs publication

`tests/distributions.nix:84-87` adds `opensuse:leap-16.1`; it is included in
cgroup-compatible/systemd/all sets (`:143,190,211`).
`tests/all-tests.nix:191-213` feeds distribution sets into routed-network,
start/stop and systemd tests. `tests/suite/dist-config/start-stop.nix:34-37`
calls `osctl ct new --distribution ... --version ...`; no local archive or
candidate repository is selected. The test has the `ci` tag (`:10`), whereas
the image-script template has no `ci` tag. Main CI selects `-t ci`
(`.github/workflows/ci.yml:223-245`). Merely registering both tests in
all-tests does not order or connect them.

Fresh pools create repository `default` at `https://images.vpsadminos.org`
(`osctld/lib/osctld/db/repositories.rb:5-16`). Therefore these consumers fail
until the target tuple exists in an enabled repository. More seriously, a
changed existing image can still pass these tests using the previous public
bytes. Passing image-script tests and general distribution tests does not
prove that the latter tested the candidate bytes.

### Exact artifact retention boundary

`operations/image/build.rb:74-83` computes the external archive filenames:
distribution/version/arch/vendor/variant plus `-archive.tar` and `-stream.tar`.
Archive format is omitted for images with additional datasets; the stream
always exists. `operations/image/export.rb:34-73` writes complete container
metadata/config/rootfs to those files. Build temporary datasets are removed
in an ensure (`build.rb:88-95,230-268`) **after** export; that cleanup does not
delete the output archive files.

The subsequent boundary loses them:

- `test-runner/lib/test-runner/test_evaluator.rb:764-780` stops/kills machines
  and calls `destroy` under the destructive option, which defaults on
  (`test-runner/man/man1/test-runner.1.md:165-168`).
- `osvm/lib/osvm/machine.rb:403-420` deletes its shared directory and managed
  disks. The image-script VM uses a 10 GiB managed disk
  (`tests/machines/vpsadminos/with-tank.nix:3-8`), containing the output ZFS
  dataset.
- CI uploads only logs/text on failure/cancellation
  (`image-scripts.yml:133-143`), not image archives. The composite uploader
  defaults to 14 days (`.github/actions/upload-test-logs/action.yml:21-24`).
- Final CI state cleanup removes run state after success/skipped tests or a
  successful failure-log upload; otherwise it preserves unpublished state
  (`.github/actions/cleanup-test-state/cleanup-test-state.bash:30-47`). That
  fallback does not resurrect VM disks already destroyed by the evaluator.

`--no-destructive` can retain disks for diagnosis; it is not an artifact
export contract. It also requires care with freshness because build caching
only checks whether a matching output filename exists
(`operations/image/build.rb:107-109`). A new reusable cache needs source and
input identity, not just those filenames.

## Existing reuse points

| Existing primitive | Source and implication |
| --- | --- |
| File transfer | `osvm/lib/osvm/machine.rb:717-727` exposes push/pull. `shared_dir.rb:62-67` returns a host path inside the VM's temporary shared directory; copy it into retained output **before** evaluator destruction. Returning the path alone is insufficient. |
| Extra shared filesystem | `machine.rb:177-180,877-892` starts virtiofsd for configured shared filesystems. The image test already mounts its source using this mechanism. A separate host output mount avoids copying archives from the VM disk. |
| Local image repository | `operations/image/deploy.rb:24-35` initializes a local repository and adds existing tar/ZFS outputs. `cli/image.rb:90-146` performs build/test/deploy. `docs/container-images/repositories.md` documents `osctl-repo local init/add/default` and serving over HTTP. No public publication is needed to construct a candidate repository. |
| Host-independent VM repository builder | `os/modules/services/misc/build-vpsadminos-container-image-repository/shared.nix:17-55,65-110` already runs a vpsAdminOS guest, with host `cacheDir`, `logDir`, `repoDir`, scripts and source shared via virtiofs. `options.nix:133-154` exposes retained host directories. This works as an architectural example without moving builds onto a privileged long-lived host. |
| Existing repository build coordinator | `os/modules/services/osctl/image-repository/build.rb:130-176` calls `osctl-image deploy` with build dataset, cache, selected images and tags. `:71-88` sets defaults, performs GC and calls postBuild. Concrete production publisher configuration is outside I0; the docs' rsync is an example, not deployment evidence. |
| Local HTTP-repository test fixture | `tests/suite/osctl/ct-image-fetch.nix:201-216` builds a repository from an exported container; `:219-240` starts its test server/adds a repository and explicitly selects it. The fixture proves local HTTP is already exercised, although its purpose-built flaky server should not become the candidate server. |
| Shared VM configuration | `tests/make-test.nix:112-120` includes common modules/base; `tests/configs/vpsadminos/base.nix:9-11` can load `os/configs/tests.nix`. Declarative `osctl.pools.<pool>.repositories` exists (`os/modules/osctl/pools.nix:63-67`); `repositories.nix:26-61` can replace the existing default's URL. Wait for repository configuration readiness, not merely pool active: the repository service itself starts after pool active (`:92-104`). |
| Runtime test configuration | `tests/make-test.nix:353-365` carries `--test-config` data into evaluator `test_config` (`test_evaluator.rb:93-95`). Current `tests/test-configs/ci.nix` configures docker/podman only. This can carry candidate URL and required tuples to a small consumer helper. No such image policy currently exists. |

### Repository selection and candidate correctness

`osctld/lib/osctld/utils/container.rb:7-17` restricts an explicit
`--repository` to one repository; otherwise it enumerates all enabled pool
repositories. `:75-90` returns the first successful tuple, continuing on
both image absence and repository unavailability. Repository lists preserve
insertion order (`db/list.rb:42-57`); default is loaded first
(`pool.rb:759-770`). Simply adding a candidate repository after public default
therefore does not override existing public tuples. Repointing default and
adding public fallback has the opposite issue: a broken/missing candidate
can silently use public bytes.

There is no existing per-tuple CLI override for all raw test commands.
`osvm/lib/osvm/vpsadminos_machine.rb:9-11` provides a JSON wrapper only;
existing tests issue `machine.succeeds("osctl ct new ...")` directly. The
CLI exposes `--repository` (`osctl/lib/osctl/cli/app.rb:667`) without an
environment default. Targeted tests must adopt an explicit repository option
or a small shared helper. Avoid intercepting arbitrary shell command text.

## Concrete suggestions, smallest first

1. Retain the existing VM build boundary and export successful local outputs
   into an explicit host directory before machine destruction. Use the
   current extra shared-filesystem mechanism, or pull and immediately copy
   files outside `shared-dir`. Add explicit CI archive artifacts and a clear
   retention policy. Keep archive hashes, full image tuple, source revision
   and relevant build inputs beside them.
2. Initialize a candidate local repository from those exact tested files
   using existing osctl-repo tooling. A job-local HTTP endpoint or another
   VM can serve it. Explicitly sequence candidate production before targeted
   distribution consumers; current independent workflows do not provide this.
3. Start with affected consumer tests: pass candidate URL plus required
   tuples through test configuration, register the candidate, and select
   `--repository candidate` for exactly those tuples. Assert required tuple
   availability and artifact identity and fail when missing. Keep ordinary
   public defaults for unaffected/bootstrap tuples. This requires bounded
   consumer edits; the current runner has no transparent strict tuple policy.
   A global candidate-only default is viable for a scoped test batch whose
   entire dependency set is available in that repository.
4. Do not introduce a complete public-repository mirror or fallback proxy
   for this first slice. A merged index alone is not established as sufficient
   to redirect unchanged payloads to another origin; implementer2 owns the
   repository layout/consumer analysis. Generic multi-repository fallback is
   unsuitable evidence for candidate acceptance.
5. Keep publication a separate consuming operation over tested bytes; do not
   rebuild after approval and assume byte equivalence. Existing repository
   build/deploy primitives can be reused, but their current partial-build
   and postBuild behavior needs explicit acceptance semantics before serving
   as a release gate (`build.rb:178-203,227-233` logs failures and continues).

## Runner requirements and limits of this evidence

Source supports these requirements: Linux/Nix toolchain and substituted or
built vpsAdminOS closures; usable QEMU/KVM with host CPU exposure
(`tests/make-test.nix:52-55`, `osvm/lib/osvm/vpsadminos_machine.rb:162-175`);
virtiofsd; writable sparse disk/state and archive storage; Internet access
for bootstrap images and distro package downloads; 24 GiB guest memory per
image VM and adequate shared memory (make-test.nix:330-341 budgets guest RAM
as shm). `--jobs auto` budgets CPU/RAM/shm, not build/download/archive disk
capacity; docs/os/testing notes that an oversized test can still run alone.

The VM supplies ZFS/LXC and guest-root mount/chroot/container privileges.
It does not require a native vpsAdminOS runner host or justify privileged
native image builds. KVM access and virtiofs prerequisites still need the
runner's permissions/device support. These are source-derived requirements,
not a claim that every current self-hosted runner is configured correctly.
This first pass did not inspect runner host configuration, actual KVM device
access, disk free space, CI history/artifact byte sizes, upstream package
availability, production publication configuration, or runtime performance.
No runtime checks were authorized or performed.

Session portal: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/>.
