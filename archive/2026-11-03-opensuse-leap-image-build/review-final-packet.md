# Final committed-series review packet

Prepared by implementer1 for lead assignment to the retained independent
reviewer. All intended application changes are committed and quick checks pass.
Long final-source checks have not been launched by implementer1.

## Request and acceptance

Fix openSUSE Leap image building with the existing shared builder, add 16.1,
and resolve the actual inactive systemd device-unit cause. The user rejected
an expected-failure extension. The accepted design is [Milestone 1](design.md)
and [Milestone 2](device-unit-design.md). No privilege/kernel/host change,
generic framework, public image publication or extra permanent test matrix is
part of this package.

The controlled original-AA experiment establishes missing udev processing and
normal boot plus dynamic-interface resolution. Final readiness additionally
requires rebuilt images, clean bootstrap/scriptlet evidence and the original
eth0/dummy assertions to pass against exact local candidate artifacts.

## Exact range and complete history

- Initiative: `2026-11-03-opensuse-leap-image-build`.
- Repository: `git@github.com:vpsfreecz/vpsadminos.git`, target `origin/staging`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-opensuse-leap-image-build/vpsadminos`.
- Base: `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
- Final head: `742eb30cb1a8b6766c85e915d26b0400e38244b1`.
- Final tree: `19f423e70ff439867d4bb27e8ed07b9c95fdb703`.
- Fresh SSH remote proof matches that feature head; staging remains at base.

| Commit | Logical ownership |
| --- | --- |
| `4c2a38bc02d1d10c208d478c01ec90057995825e` | Change only the shared Leap builder from 15.5 to 16.0. |
| `57871a8e3f8f429e86e3ad6abf16de99a44e9416` | Add 16.1 build/config, repository registration/latest move and explicit distribution coverage, using the shared builder. |
| `742eb30cb1a8b6766c85e915d26b0400e38244b1` | Explicit udev in the shared openSUSE helper, durable nearby rationale and removal of the device-unit expected-failure/conditional. |

Complete diff: seven files, +27/-14:
`image-scripts/builders/opensuse-leap/config.sh`,
`image-scripts/images/opensuse-leap-16.1/{build,config}.sh`,
`image-scripts/include/opensuse.sh`, `os/configs/image-repository.nix`,
`tests/distributions.nix`, `tests/suite/systemd/device-units.nix`.
Review the complete range, not only commit 3:

```sh
git log --reverse --format=fuller dd188397abe37d0bc33f4c5dfb3605206ce5e326..742eb30cb1a8b6766c85e915d26b0400e38244b1
git diff dd188397abe37d0bc33f4c5dfb3605206ce5e326 742eb30cb1a8b6766c85e915d26b0400e38244b1
```

The earlier dedicated-builder approach was removed/consolidated before this
series; retained refs and old/new ranges are documented in
[Milestone 1's receipt](implementation-result.md). The builder update is one
logical update stream, with no repeated dependency/channel/lock update stream.
No WIP/fixup or obsolete intermediate implementation remains in the final range.
There are **no migrations**, so merged/released/deployed/externally consumed
migration provenance is empty. No final source image has been published or
deployed; AA was used only in disposable verification/diagnosis.

The final message amendment preserves published predecessor
`c856aa1b9939d048407ea72d434b087aed42c4af` at a backup ref and keeps the identical
tree. Full-range range-diff shows commits 1–2 identical, with only validation
prose added to commit 3. There was no source change or broad test rerun for that
message-only edit. This resolves the known commit-validation-prose advisory.

Require explicit independent conclusions about whole-branch history,
consolidation and migration lineage. Earlier review of AA does not replace this
final review.

## Evidence and compatibility

[Milestone 2 result](device-unit-result.md) contains accepted raw log hashes,
exact commands/results, warning explanations, source/check receipts and limits.
[Final verification preparation](final-checks-742eb30cb.md) binds source/input
identity, final revision modules and the bounded long-check plan.

The first discovery failed before test/VM execution because the session-only
8 GiB `mkForce` tied with an unrelated fixture's forced 4 GiB during metadata
enumeration. The old input/failure evidence is retained. Corrected
`final-verification-742eb30cb-v2.nix` uses priority 60, between ordinary 100 and
explicit `mkForce` 50, preserving forced fixture sizes while reducing normal
image guests to 8 GiB. Fresh watcher syntax/priority proof passed with
image8192/namespaces4096. Listing then failed because the previously inspected
unrooted source path was absent. [Input recovery](final-input-recovery-742eb30cb.md)
materialized the identical clean Git source/NAR, verified all files/modes with
no extras, and durably GC-rooted source and runner. The generated native
invocation avoids path retyping; fresh actual selector discovery is pending.
Product source, final head and reviewed diff are unchanged, so independent
product review can proceed.

Quick checks passed shell/Nix syntax, nixfmt, whitespace and full Overcommit
RuboCop/Nixfmt; active commit and commit-message hooks pass. The worktree is
clean. Final CI is pending, with current-head runs left untouched.

The shared helper actually serves Leap 15.6/16.0/16.1 and Tumbleweed. Existing
published images/containers are unchanged; rebuilt/new images gain udev and its
required dependency closure. Existing containers require a separately requested
package-manager install and restart. No host privilege, namespace, mount, device
policy, persisted host format, API or protocol changes occur. No coordinated
fleet upgrade is required. The shared builder cache must use fresh state because
builder identity/reuse does not encode the selected release.

Older public `opensuse/latest` archives are not retroactively fixed by the source
commit. Candidate-backed verification uses exact local rebuilt artifacts;
unqualified public-image CI may still see the older inactive-device behavior
until separately authorized image publication. Review that rollout distinction
without restoring an expected-failure workaround or inferring publication
authority.

The package rationale has a durable home beside EXTRAPKGS. Temporary experiment,
source, alias and rollout details remain in session records. No broader project
documentation was useful for the conventional package addition.

For the lead's mandatory review workflow, the requested lanes are general,
architecture/repetition, scope/proportionality and risk/compatibility. Treat the
shared image-builder and init/network behavior conservatively as high risk for
coverage selection. Use retained reviewer0's saved model/effort after a fresh
roster check; do not override its settings or let this packet assign itself.
No reviewer conclusion is pre-supplied by this packet.

## Full committed series and final diff

```text
commit 4c2a38bc02d1d10c208d478c01ec90057995825e
Author:     Jakub Skokan <jakub.skokan@havefun.cz>
AuthorDate: Tue Nov 3 20:37:47 2026 +0100
Commit:     Jakub Skokan <jakub.skokan@havefun.cz>
CommitDate: Tue Nov 3 20:37:47 2026 +0100

    image-scripts: use Leap 16.0 for Leap builds
    
    Upgrade the shared openSUSE Leap builder from 15.5 to explicit 16.0.
    The old RPM implementation lacks Lua APIs used by newer package
    scriptlets. This updates the build environment for existing Leap 15.6
    and 16.0 images and provides the tooling needed by the new 16.1 image.
    
    Keep the builder name and no-op setup unchanged. Existing managed
    builders are keyed by name, so an idle cached builder must be recreated
    to use the new release; reverting the config alone has the same caveat.
    
    Shell parsing and builder config resolution pass; native regression
    validation with fresh builders follows separately.

commit 57871a8e3f8f429e86e3ad6abf16de99a44e9416
Author:     Jakub Skokan <jakub.skokan@havefun.cz>
AuthorDate: Tue Nov 3 20:39:20 2026 +0100
Commit:     Jakub Skokan <jakub.skokan@havefun.cz>
CommitDate: Tue Nov 3 20:39:20 2026 +0100

    image-scripts: add opensuse-leap-16.1
    
    Build Leap 16.1 through the shared Leap builder while preserving the
    existing bootstrap and configuration sequence. Make it the default
    stable openSUSE image while retaining explicit older releases.
    
    Register the exact release for distribution and cgroup tests so it can
    be verified independently of the latest tag. Preserve the existing
    device-unit test behavior for separate compatibility investigation.
    
    Shell and Nix syntax and formatting checks pass; native image regression
    and final candidate checks follow separately.

commit 742eb30cb1a8b6766c85e915d26b0400e38244b1
Author:     Jakub Skokan <jakub.skokan@havefun.cz>
AuthorDate: Tue Nov 3 21:37:25 2026 +0100
Commit:     Jakub Skokan <jakub.skokan@havefun.cz>
CommitDate: Tue Nov 3 21:40:50 2026 +0100

    image-scripts: install udev in openSUSE images
    
    Install udev explicitly when bootstrapping openSUSE without recommended
    packages. systemd and libudev alone provide neither the event-processing
    daemon nor its units, leaving network device units inactive even though
    the interfaces exist. udev initializes and tags the devices for systemd
    on normal startup and when new interfaces are created.
    
    Remove the openSUSE device-unit test exception and use the same complete
    eth0 and dynamic dummy0 assertions for every distribution. Rebuilt
    images gain udev; existing containers need the package installed and a
    restart.
    
    A controlled udev install and clean restart activated eth0 and a new
    dummy interface. Shell/Nix syntax and Overcommit checks pass; rebuilt-
    image verification remains pending.
```

```diff
diff --git a/image-scripts/builders/opensuse-leap/config.sh b/image-scripts/builders/opensuse-leap/config.sh
index 6ae3ba689..983a55cdc 100644
--- a/image-scripts/builders/opensuse-leap/config.sh
+++ b/image-scripts/builders/opensuse-leap/config.sh
@@ -1,2 +1,2 @@
 DISTNAME=opensuse
-RELVER=leap-15.5
+RELVER=leap-16.0
diff --git a/image-scripts/images/opensuse-leap-16.1/build.sh b/image-scripts/images/opensuse-leap-16.1/build.sh
new file mode 100644
index 000000000..334b1935f
--- /dev/null
+++ b/image-scripts/images/opensuse-leap-16.1/build.sh
@@ -0,0 +1,9 @@
+. "$IMAGEDIR/config.sh"
+. "$INCLUDE/opensuse.sh"
+
+bootstrap
+configure-common
+
+configure-opensuse
+
+run-configure
diff --git a/image-scripts/images/opensuse-leap-16.1/config.sh b/image-scripts/images/opensuse-leap-16.1/config.sh
new file mode 100644
index 000000000..531649678
--- /dev/null
+++ b/image-scripts/images/opensuse-leap-16.1/config.sh
@@ -0,0 +1,5 @@
+BUILDER=opensuse-leap
+SPIN=leap
+SPINVER=16.1
+RELVER=$SPIN-$SPINVER
+ARCH=x86_64
diff --git a/image-scripts/include/opensuse.sh b/image-scripts/include/opensuse.sh
index 1eb883da9..68082f0a9 100644
--- a/image-scripts/include/opensuse.sh
+++ b/image-scripts/include/opensuse.sh
@@ -13,7 +13,9 @@ else
 	fail "unsupported spin"
 fi
 
-EXTRAPKGS='vim iproute2 iputils net-tools procps less psmisc timezone aaa_base-extras openssh curl ca-certificates ca-certificates-mozilla wicked hostname'
+# systemd device units need udev's network events. Install it explicitly because
+# the bootstrap excludes recommended packages.
+EXTRAPKGS='vim iproute2 iputils net-tools procps less psmisc timezone aaa_base-extras openssh curl ca-certificates ca-certificates-mozilla wicked hostname udev'
 
 ZYPPER="zypper -v --root=$INSTALL --non-interactive --gpg-auto-import-keys "
 
diff --git a/os/configs/image-repository.nix b/os/configs/image-repository.nix
index f94b75f46..eba7f6c7c 100644
--- a/os/configs/image-repository.nix
+++ b/os/configs/image-repository.nix
@@ -179,7 +179,8 @@
 
       opensuse = {
         "leap-15.6" = { };
-        "leap-16.0" = {
+        "leap-16.0" = { };
+        "leap-16.1" = {
           tags = [
             "latest"
             "stable"
diff --git a/tests/distributions.nix b/tests/distributions.nix
index 3dea9a40d..1e995b93b 100644
--- a/tests/distributions.nix
+++ b/tests/distributions.nix
@@ -81,6 +81,10 @@ let
       distribution = "opensuse";
       version = "latest";
     };
+    opensuse_leap_16_1 = {
+      distribution = "opensuse";
+      version = "leap-16.1";
+    };
     rocky_8 = {
       distribution = "rocky";
       version = "8";
@@ -136,6 +140,7 @@ in
     debian_stable
     devuan
     opensuse
+    opensuse_leap_16_1
     rocky_8
     rocky_9
     rocky_10
@@ -182,6 +187,7 @@ in
     nixos_stable
     nixos_unstable
     opensuse
+    opensuse_leap_16_1
     rocky_8
     rocky_9
     rocky_10
diff --git a/tests/suite/systemd/device-units.nix b/tests/suite/systemd/device-units.nix
index ce4e358bf..801b01151 100644
--- a/tests/suite/systemd/device-units.nix
+++ b/tests/suite/systemd/device-units.nix
@@ -16,16 +16,9 @@ import ../../make-test.nix (
     testScripts = builtins.listToAttrs (
       map (
         { distribution, version }:
-        let
-          expectFailure = distribution == "opensuse" && version == "latest";
-        in
         {
           name = "${distribution}-${version}";
           value = {
-            # These distributions do have the device unit, but it is inactive (dead) and so
-            # systemctl status returns non-zero exit status.
-            inherit expectFailure;
-
             script = ''
               machine.wait_for_osctl_pool("tank")
               machine.wait_until_online
@@ -39,10 +32,7 @@ import ../../make-test.nix (
                 "osctl ct start #{testct}",
               )
 
-              # Do not poll the known inactive openSUSE unit until the shell's
-              # protocol budget expires. Preserve its expected command failure
-              # and leave the worker shell usable by subsequent test scripts.
-              machine.${if expectFailure then "succeeds" else "wait_until_succeeds"}(
+              machine.wait_until_succeeds(
                 "osctl ct exec #{testct} systemctl status sys-devices-virtual-net-eth0.device",
                 timeout: 60
               )
```
