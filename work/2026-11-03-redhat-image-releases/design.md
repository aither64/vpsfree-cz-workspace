# Red Hat-family releases and source identity in image tests

## Scope and evidence

Update release RPM references that differ from the live upstream listings.
The user subsequently approved the proposed source-identity correction with
"aha I see, implement your suggested solution and continue". The additional
bounded design below supersedes the original release-only scope for test-runner,
framework and channel files. Preserve the four release commits unchanged.
Repository: `vpsadminos`; feature branch: `2026-11-03-redhat-image-releases`;
worktree: `worktrees/2026-11-03-redhat-image-releases/vpsadminos`.
The inspected baseline is `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
The integration target is `origin/staging`: the lead confirmed the remote
symbolic HEAD with `git ls-remote --symref origin HEAD`. Earlier references to
`master` were an incorrect assumption, not the repository's current default.

On 2026-11-03, architect0 ran the documented read-only discovery command from
the feature worktree; it exited successfully:

```sh
ruby skills/update-redhat-family-image-releases/scripts/discover_release_updates.rb all
```

The current checkout contains 12 matching images. The initial bare-HEAD inventory
was older and lacked Fedora 45; the table below uses the fresh feature baseline.
Only four `RELEASE` lines need changing. No point versions change, and every
stable Fedora image is present on the live mirror, so none should be removed.

| Image | Current release RPM or shared Fedora value | Proposed value |
| --- | --- | --- |
| almalinux-8 | `almalinux-release-8.10-1.el8.x86_64.rpm` | unchanged |
| almalinux-9 | `almalinux-release-9.8-1.el9.x86_64.rpm` | unchanged |
| almalinux-10 | `almalinux-release-10.2-21.el10.x86_64.rpm` | unchanged |
| centos-9-stream | `centos-stream-release-9.0-36.el9.noarch.rpm` | `centos-stream-release-9.0-38.el9.noarch.rpm` |
| centos-10-stream | `centos-stream-release-10.0-21.el10.noarch.rpm` | `centos-stream-release-10.0-23.el10.noarch.rpm` |
| fedora-43 | `43-25` for all four release packages | unchanged |
| fedora-44 | `44-17` for all four release packages | unchanged |
| fedora-45 | `45-13` for all four release packages | unchanged |
| fedora-rawhide | `RAWHIDE_RELVER=46-0.1` for all four release packages | unchanged |
| rocky-8 | `rocky-release-8.10-1.14.el8.noarch.rpm` | unchanged |
| rocky-9 | `rocky-release-9.8-1.1.el9.noarch.rpm` | `rocky-release-9.8-1.2.el9.noarch.rpm` |
| rocky-10 | `rocky-release-10.2-1.1.el10.noarch.rpm` | `rocky-release-10.2-1.2.el10.noarch.rpm` |

The script read these package listings for the changed images:

- [CentOS Stream 9](https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/os/Packages/)
- [CentOS Stream 10](https://mirror.stream.centos.org/10-stream/BaseOS/x86_64/os/Packages/)
- [Rocky 9.8](https://ftp.linux.cz/pub/linux/rocky/9.8/BaseOS/x86_64/os/Packages/r/)
- [Rocky 10.2](https://ftp.linux.cz/pub/linux/rocky/10.2/BaseOS/x86_64/os/Packages/r/)

Unchanged-image evidence came from the same script using AlmaLinux's
`https://repo.almalinux.org/almalinux/<POINTVER>/BaseOS/x86_64/os/Packages/`
for 8.10, 9.8 and 10.2; Rocky's corresponding 8.10 listing; Fedora's
`http://ftp.fi.muni.cz/pub/linux/fedora/linux/releases/<RELVER>/Everything/x86_64/os/Packages/f/`
for 43, 44 and 45; and
`http://ftp.fi.muni.cz/pub/linux/fedora/linux/development/rawhide/Everything/x86_64/os/Packages/f/`.
Point-release selection came from the Rocky and AlmaLinux root listings.

## Interfaces, files and invariants

Each changed `build.sh` exports one release RPM URL consumed by
`image-scripts/include/redhat-family.sh`: bootstrap downloads and installs that
RPM into the new image root, then installs the distribution packages. Keep the
existing `${POINTVER}` interpolation, host, path, architecture and extension.
Change only `36` to `38`, `21` to `23`, and each Rocky `1.1` to `1.2` in the
respective `RELEASE` assignment.

Preserve `POINTVER`, `BASEURL`, `UPDATES`, builders, package lists and bootstrap
logic. AlmaLinux 8 retains its major-version repository URLs; CentOS retains
the major `-stream` paths. Fedora's four release references remain consistent.
The release packages need no shared-helper or workflow edits. The existing skill
already documents release updates; this record holds the dated inventory. The
approved framework correction below additionally needs focused tests and a short
explanation in the existing framework documentation.

## Implementation boundaries and dependencies

The lead accepted two independent family packages:

| Package | Owned files under `image-scripts/images/` | Acceptance and commits |
| --- | --- | --- |
| CentOS Stream | `centos-9-stream/build.sh`, `centos-10-stream/build.sh` | Exactly the two RPM suffix changes above; one commit per directory |
| Rocky | `rocky-9/build.sh`, `rocky-10/build.sh` | Exactly the two RPM suffix changes above; one commit per directory |

The packages have no source dependencies and may edit their disjoint files
concurrently. The shared worktree's Git/index operations must be serialized by
the lead; only the designated writer stages and commits at a time. Preserve
the other package's working changes. Each commit needs the repository hooks,
a scoped subject and explanation, and a temporary message file passed to
`git commit -F`. Four final commits are appropriate because the skill requires
one commit per changed image; do not combine them into family commits.

The architect owns this brief. Implementers own application edits, quick checks,
commits and diagnosis within their packages. Lead owns tracking commits, review,
long-test scheduling, publication and approved integration. A discovery result
that changes these four targets, or a failure needing shared-code edits, returns
to the lead before expanding the work.

## Compatibility, deployment and recovery

The four image names and major/point releases stay the same. This updates
bootstrap input packages for newly built container images; it does not mutate
running containers or the host. Persisted host state, database schemas, seeds,
migrations, APIs, generated clients, CLI contracts, protocols and NixOS module
options are unchanged. There are no migrations or mixed-version host coupling,
and no coordinated update of running nodes is required.

Per-image integration tests must establish that each new RPM remains usable by
the existing builder and runtime. No production image publication or machine
deployment is part of this request. Source rollback is a revert of the relevant
image commit; old RPM availability is not guaranteed once upstream removes it,
so a source revert alone may not restore a build. Existing image artifacts and
running containers remain unaffected. Future publication would follow its own
deployment procedure and retain known-good image artifacts for recovery.

## Verification and acceptance

Quick checks, before final independent review:

1. Compare the four new filenames with the successful upstream discovery above;
   inspect the final diff for exactly four changed `RELEASE` lines.
2. Run `bash -n` separately on all four changed `build.sh` files, followed by
   `git diff --check`, and satisfy repository commit hooks.
3. Confirm clean committed intended work, four image-specific commits plus the
   approved correction commits, and no obsolete approaches or migrations in the
   complete baseline-to-head series. Give this inventory to the final reviewer.

After the final committed-deliverable review passes, run every required image
integration test from the repository root through the prescribed verification
watcher:

```sh
nix develop .#test-runner -c bundle exec ./test-runner/bin/test-runner test image-scripts/test@centos-9-stream
nix develop .#test-runner -c bundle exec ./test-runner/bin/test-runner test image-scripts/test@centos-10-stream
nix develop .#test-runner -c bundle exec ./test-runner/bin/test-runner test image-scripts/test@rocky-9
nix develop .#test-runner -c bundle exec ./test-runner/bin/test-runner test image-scripts/test@rocky-10
```

The existing test builds and tests the image inside a vpsAdminOS VM with the
working repository shared into the guest. Each VM requests 24 GiB memory, and
the image command has a three-hour timeout. Use a bounded batch that fits host
capacity; four simultaneous jobs are not required. The correction changes
test-runner, so use the documented local-code invocation shown above. Remove
the diagnostic metadata override from the test environment; exercise the fix.

Acceptance requires four individual successful results at the intended source
head, plus relevant pushed-branch CI and the independent whole-branch review.
Stop the batch for an unexpected local kernel build and investigate cache
availability; do not expand scope to kernel work. Investigate failed image
checks before retrying. Record exact source head, command, result and log path,
with derivation/input receipts if successful Nix evidence is reused. Unchanged
images need no additional integration runs for this four-line change.

The original four release edits are committed at
`3307df52ea5bf875e1d8a23318a64f569d8b3ebc`; local image evaluation exposed the
pre-existing failure described in [root-cause-report.md](root-cause-report.md)
and [verification-diagnosis.md](verification-diagnosis.md). The following is
implementation design, not a claim that the correction or image tests passed.
Integration remains the lead's operation after final verification and review.

## Approved source-identity correction

### Contract and minimal transport

Keep the existing immutable repository snapshot and invocation GC root. Add one
small metadata record to that existing RepositorySource lifetime: canonical
snapshot path, nullable revision, dirty flag when revision is known, and the
short revision needed by the existing suffix convention. Do not add a registry,
new runner, alternate snapshot system or configuration pin update.

Acquire the Git commit during source resolution, not later during evaluation.
Keep `(builtins.getFlake ...).outPath` as the content-selection mechanism:
changing to a Git fetch would silently drop untracked files currently included
by the path snapshot. Determine dirty state against the captured tree, not just
the original checkout's `git status`. A conventional implementation is a private
temporary Git index initialized from the captured commit, used read-only against
the immutable snapshot for tracked-file differences and extra files. Include
ignored/untracked files that the snapshot actually contains; exclude Git's own
metadata. This avoids reading or mutating the user's live index. Resolve linked
worktrees through Git's own repository discovery, and require the discovered
repository root to match the requested source root so a Git-free child directory
does not inherit an unrelated parent repository's identity.

A captured commit remains an immutable comparison baseline even if live HEAD
moves afterward: changed captured content must be marked dirty relative to that
commit. If a reliable commit cannot be obtained, represent identity as unknown;
never invent a clean revision. Git-free sources and existing packaged revision
files retain their supported fallback semantics. All Git/index temporaries stay
inside the invocation's existing cleanup lifetime; no application index writes.

Transport the record through the existing command environment as a scoped JSON
value, for example `TEST_RUNNER_SOURCE_INFO`, beside `TEST_RUNNER_REPO_ROOT`.
Set it once from RepositorySource and restore the caller's prior value in the
same ensure block. Do not use `TEST_RUNNER_REPO_REV` alone as provenance. The
record includes the exact immutable source path, and a consumer may use it only
when that path equals the vpsAdminOS provider's own source path. Absent metadata
retains existing behavior. Do not stamp the record into the captured source or
read mutable original Git metadata from Nix evaluation.

### Framework and module boundary

Factor the current `flakeVersionInfoModule` identity normalization into one small
shared helper or shared flake binding. Preserve its `rev`/`dirtyRev`, short-revision
suffix and `mkDefault` rules. Normal flake OS construction and the framework's
test OS construction both use it. Prefer an additive framework field exposing
the already bound version module, consumed conditionally by `tests/make-test.nix`.
The helper selects matching snapshot metadata first, otherwise the provider's
native flake metadata; an unknown identity does not manufacture revision fields.

Pass the existing full test framework through the native direct-test path in
`evaluate-tests.nix`, which currently imports the test library without it. Keep
legacy/direct-import fallbacks supported when the optional module is absent.
Preserve `mkTests`, `mkTestsMeta`, `makeTest`, `makeTemplate`, `makeTestLib`,
`sourcePath` and `sourceInputs` signatures. Preserve explicit module overrides,
alternate nixpkgs handling, and the current conditional nixpkgs-revision logic;
avoid introducing competing definitions of that option during factoring.

The provider/root distinction is required compatibility, not optional hardening.
Read-only canonical inspection found vpsAdmin `origin/master`
`942c6eaed41331f823d8e0f670ed239e2b308440`, pinned to vpsAdminOS
`8e44a5124439b1f3048ffc56b1717614a5360358`. Its flake calls `mkTests` and
`mkTestsMeta`; its test wrapper calls `makeTest` and uses `sourcePath`, while
`all-tests.nix` calls `makeTestLib`. Those callers need no changes. A root
vpsAdmin snapshot's revision must never become the pinned vpsAdminOS guest
revision. The pinned provider retains its own source identity when paths differ.

### Independent nullable consumer

In `os/modules/installer/cd-dvd/channel.nix`, conditionally emit `.git-revision`
only when `config.system.vpsadminos.revision != null`. Retain known revisions
exactly; unknown means no generated revision file, not an empty or invented
revision. This honors the existing nullable option independently of the missing
framework provenance. It does not change image recipes or SSH tests.

### Packages and ownership

| Package | Files and deliverable | Dependencies |
| --- | --- | --- |
| Coupled identity package, implementer0 | `test-runner/lib/test-runner/repository_source.rb`, `cli/command.rb`, resolver/evaluator Nix helpers as needed, `flake.nix`, `tests/make-test.nix`, one small shared identity helper if useful, existing focused specs, `docs/os/test-framework-integration.md` | Own capture/transport/framework semantics together; preserve existing source-root lifecycle |
| Nullable channel package, implementer1 | `os/modules/installer/cd-dvd/channel.nix`, focused standalone Nix regression check | Independent source boundary; primary owner registers any shared flake check after receiving its interface |

The channel owner currently has sole Git/config writer and utility ownership.
The identity owner may edit disjoint files after the lead releases this brief,
but must wait for that ownership to transfer before Git writes or a fresh utility.
Keep correction commits separate from the four release commits and fold caused
follow-up fixes into their logical owner before final review. Lead owns final
review, long checks, publication, integration and tracking commits.

### Checks, compatibility and recovery

Extend the existing RepositorySource/command/Nix evaluation specs and existing
flake check conventions; no parallel test harness. Focused checks must cover:

- Ordinary clean checkout and linked worktree: same captured revision and
  truthful clean/dirty result under the unchanged path snapshot semantics.
- Tracked modifications plus included untracked/ignored files: bytes preserved
  and dirty state true; no live-index mutation.
- HEAD and files changed after capture: retained snapshot and metadata stay
  unchanged. Git-free input has no fabricated revision.
- Command success and exception: prior environment restored, existing GC-root
  and temporary-file cleanup retained.
- Matching provider accepts captured metadata; a different pinned provider
  retains its own identity. Exercise an external caller shaped like vpsAdmin,
  including a legacy framework without the new optional field.
- Both default and configured/direct test evaluation, explicit revision overrides,
  and normal flake OS version behavior. Channel-enabled evaluation succeeds with
  known and null revisions, with correct generated-file behavior.

Run focused Ruby checks in `nix develop .#test-runner`, formatting/hooks and
`git diff --check`. Use small Nix metadata/module evaluations for the identity
matrix rather than building full systems. Final independent review of all
committed changes precedes the four local-code image tests above and relevant
CI. Any uncertain-duration checks use the required single fresh utility slot.

This changes test provenance and generated channel source metadata, with no new
persisted application schema, API protocol or node coordination requirement.
Existing framework callers and old pinned providers continue to work; no
vpsAdmin pin bump or production deployment is part of this package. Rollback
reverts the two correction commits, restoring the original test limitation;
there is no state migration. Keep historical CI SSH evidence separate and do
not expand this fix into SSH timing or livepatch work.

## Resource setting for the four final image tests

At reviewed head `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`, an 8 GiB
guest is an acceptable resource-only verification environment for
`centos-9-stream`, `centos-10-stream`, `rocky-9` and `rocky-10`.
Use the normal local-code test-runner command with a recorded
`VPSADMINOS_CONFIG` module that selects the image suite by its existing dataset
marker and changes only guest memory:

```nix
{ config, lib, ... }:
lib.mkIf
  (lib.hasAttrByPath [ "boot" "zfs" "pools" "tank" "datasets" "image-scripts/build" ] config)
{
  boot.qemu.memory = lib.mkForce (8 * 1024);
}
```

The earlier global `mkForce` conflicted with an unrelated fixture's
`mkForce 4096` during full metadata evaluation, before any VM was scheduled.
The conditional module avoids that conflict without raising override priority.
At the inspected head, the marker occurs only in
`tests/suite/image-scripts/test.nix`; it is independent of QEMU memory and is
safe to use as the predicate. Non-image fixtures retain their own allocations.
The selector applies to image-suite metadata, including unselected image
templates; the execution filter must remain exactly the four named tests.
This does not qualify other distributions at 8 GiB.

Before launching the batch, require the normal full metadata/list evaluation
to pass with this module and confirm all four selected tests declare 8192 MiB
RAM/shared memory. Preserve evidence that the formerly conflicting non-image
fixture keeps 4096 MiB. Keep the module temporary and record its final hash;
do not change application source, scheduling reserves or override priority.

This conclusion follows the inspected contracts, not a measured memory peak:

- `os/modules/system/boot/qemu.nix:285` defaults to 8192 MiB and permits
  integer allocations greater than 256 MiB. The image-test template's 24 GiB
  is a generic allocation, not an asserted per-distribution minimum. Its
  introducing commit `da621027b5225192eea59533b508e49934a48596` records only
  the increase, without explaining the reason; do not attribute it to NixOS
  without evidence.
- All four images use the AlmaLinux 9 builder. Its setup installs packages
  with DNF; the Red Hat bootstrap installs RPMs and the core package group.
  Their recipes, builder setup, builder creation and image-test code declare
  no minimum above 8 GiB or fixed container memory reservation requiring 24 GiB.
- Image subtests run sequentially within each test VM. The common
  `nixos_rebuild` subtest explicitly skips non-NixOS images. The generic
  template also serves NixOS, but this invocation executes only these four images.

Use `--jobs 2` as a ceiling. Two active guests request 16 GiB RAM and 16 GiB
shared memory in total, plus unchanged host reserves (8 GiB for each resource)
and existing CPU admission. Confirm generated resource metadata is 8192 MiB
RAM/shared memory per test and native admission fits current host/cgroup and
`/dev/shm` capacity after peer use. The stated 47 GiB shared-memory total is
not proof of current free capacity. Retain memory/shared-memory overcommit 1.0;
do not allow the runner's documented oversized-alone fallback to bypass a
failed capacity check. Run one at a time or wait if two do not fit.

Record the override's exact path, contents/hash, final source head, normal
command, generated JSON/resource metadata and system/kernel/input paths with
the test results. Only the memory/resource values should change relative to
the intended test configuration; confirm source, kernel, scripts, assertions,
boot parameters and timeouts remain the intended ones. Do not reuse the cached
diagnostic launch, which bypassed the source's GC-root lifetime. The normal
Command/RepositorySource invocation keeps the shared source rooted for the batch.

This does not establish an 8 GiB minimum, predict faster boot, or resolve the
earlier slow-boot warnings. The longer 24 GiB diagnostic reached login; its
later checkout error was traced to GC of the unrooted diagnostic source, not
an image or kernel defect. No kernel/security/host changes are proposed.
An OOM or failed assertion at 8 GiB remains a failure to investigate; preserve
its evidence rather than treating a rerun as validation. Acceptance still
requires all four complete image tests to pass, explicitly recorded at 8 GiB,
and the remaining review/CI/integration requirements. No verification success
at 24 GiB may be inferred from the 8 GiB results.
