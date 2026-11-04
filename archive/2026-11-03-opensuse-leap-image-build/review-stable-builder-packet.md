# Stable-builder final review packet

Request remains Leap16.1 image support and repository config. User steering:
"can't we use leap16.0 as a builder?" Lead accepted dedicated stable Leap16.0
builder only for16.1, preserving older image builders. No other scope added.

Session2026-11-03-opensuse-leap-image-build; worktree
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-opensuse-leap-image-build/vpsadminos.
Read plan/state/design, implementation-result, original review-packet/review-result,
runtime-revision-diagnosis and candidate-checks. Those are session evidence,
not substantive project documentation deliverables.

Base dd188397abe37d0bc33f4c5dfb3605206ce5e326, final head
aa963dce42859ae4251cdfaded91920d67b3a46e, tree
d4a264295678a50eac25732074dc942e637850e4. One coherent commit, sixfiles+25/-1;
clean worktree and exact remote feature head confirmed. Feature branch same slug;
defaulttarget staging. No merge/deployment/publicimage publication authorized.

Original complete review f0e1656cd840cdd2c5180340241f798614fe23d1 passed all four
lanes with two advisories. Message-only fe9182dd2fb1ba627c30d54c39c1acd7b140df69
fixed message advisory with identical tree/patchID. Its actual runtime test then
failed bootstrap using old15.5builder: zypper solved226 packages, installedthrough
200, glibc2.40 exec=nil and systemd257 rpm.execute=nil; fatal libgio2.84.4 cpio
unpack ENOENT caused abort8. Failednative log preserved as
failed-leap-15.5-test-runner.log SHA256
1dae03c64a78ccd895a53a06de0d39feee657a349c05506f4a867e716e3ae929.
Retained read-only debug reached Pry but stdin closed, so no actual15.5RPMversion
was captured; do not claim measured version or proven cpio causal chain.

Architect first recommended existing Tumbleweed builder, but user preferred
stable16.0. Tumbleweed choice was never applied. Currentdelta adds dedicated
builders/opensuse-leap-16.0 config/setup and changes only new16.1 BUILDER ref.
Explicit16.0 avoids latest/stable circularity. Newbuilder uses published
opensuse/leap-16.0, setup is conventional no-op; target remains Leap16.1 OSS.
Newbuilder is a proposed fix for confirmed LuaAPI errors, not proof that cpio is
fixed; full targeted retest must have neither Lua errors nor cpio failure.
No helper, oldbuilder, oldimage, pin, lock, API, protocol or persistent state change.
Existing containers untouched, no coordinated fleet upgrade. Deployment order
and tag behavior from original review unchanged; old versions remain selectable.

Finalseries consolidated into one logical image-support commit, including caused
bootstrapfix and required matrix/config. Backup refs preserve originalreviewed
f0 and failedfe heads; no released/deployed/external consumers of these feature
revisions. No obsolete applied approaches, fixups or repeated update streams.
No migrations, hence no merged/released/deployed/externallyconsumed migration
lineage. Independently assess entire finalseries/diff and history conclusions.

Risk remains conservatively high (containeruserspace/bootstrap compatibility and
default image selection). Same retained reviewer0 gpt-6.1-sol/xhigh, nooverride.
Affected lanes: general (correctness/history), architecture (builder/target owner
boundary), scope (stable dedicated2filebuilder vs existingrolling choice), risk
(build/runtime compatibility and rollback). Read all four references and perform
real affected review before long retest; not a confirmation-only rerun.

Quick checks pass: bash -n all4new shellfiles, Nixparse bothNixfiles, diffcheck,
nativeparser confirms newbuilder opensuse/leap-16.0 and image opensuse/leap-16.1,
modes644, active Nixfmt/commitmsg hooks. Earlier full RuboCop/Nixfmt passed;
Ruby inputs unchanged, no repeat broadlint justified. New final revision config
sets exact head via documented VPSADMINOS_CONFIG to address baseline immutable
snapshot missing .git-revision (diagnosis records unchangedbaseline source and
full inputs). No test-runner source change. Newhead primary not yet run.

Docs: original image README/creating/repositories explain existing interfaces;
no new project prose useful for conventional builderdefinition. Session design
records rationale and actual failed rollout/test evidence separately.

Verification after review: original targeted image test with exact-revision config
and retained owned disks. Then candidate-backed six new matrix cases (network,
start/stop,/run,v1,v2,deviceunits). Public16.1 absent; stockCI's six cases fetch
public image and require authorized publication first. Changed-image workflow
onlybuilds/tests, neverpublishes, no crossworkflow dependency. Do not treat public
latest16.0 tests as candidate evidence; do not publish production for testing.

Report findings and explicit complete-history/no-migrations/streams conclusion;
read-only, no builds/nestedagents. Lead saves report to preserve readonly role.

## Full final series

```text
commit aa963dce42859ae4251cdfaded91920d67b3a46e
Author: Jakub Skokan <jakub.skokan@havefun.cz>
Commit: Jakub Skokan <jakub.skokan@havefun.cz>

    image-scripts: add opensuse-leap-16.1
    
    Use a dedicated stable Leap 16.0 builder for the new Leap 16.1 image.
    The older shared Leap 15.5 builder lacks Lua APIs required by the new
    package scriptlets. Keeping a separate versioned builder preserves
    existing image builds and keeps the target Leap repositories unchanged.
    
    Make Leap 16.1 the default stable openSUSE image while preserving older
    image definitions and explicit version selection. Register the exact
    release in the distribution test matrix so its systemd and cgroup
    behavior can be verified independently of the latest tag.
    
    Shell and Nix parsing, formatting and Ruby linting pass; image runtime
    retesting with the selected builder remains pending.
```

## Full final diff

```diff
diff --git a/image-scripts/builders/opensuse-leap-16.0/config.sh b/image-scripts/builders/opensuse-leap-16.0/config.sh
new file mode 100644
index 000000000..983a55cdc
--- /dev/null
+++ b/image-scripts/builders/opensuse-leap-16.0/config.sh
@@ -0,0 +1,2 @@
+DISTNAME=opensuse
+RELVER=leap-16.0
diff --git a/image-scripts/builders/opensuse-leap-16.0/setup.sh b/image-scripts/builders/opensuse-leap-16.0/setup.sh
new file mode 100644
index 000000000..397db75f0
--- /dev/null
+++ b/image-scripts/builders/opensuse-leap-16.0/setup.sh
@@ -0,0 +1 @@
+:
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
index 000000000..a2048acb9
--- /dev/null
+++ b/image-scripts/images/opensuse-leap-16.1/config.sh
@@ -0,0 +1,5 @@
+BUILDER=opensuse-leap-16.0
+SPIN=leap
+SPINVER=16.1
+RELVER=$SPIN-$SPINVER
+ARCH=x86_64
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
```

## Delta from failed/reviewed source

```diff
diff --git a/image-scripts/builders/opensuse-leap-16.0/config.sh b/image-scripts/builders/opensuse-leap-16.0/config.sh
new file mode 100644
index 000000000..983a55cdc
--- /dev/null
+++ b/image-scripts/builders/opensuse-leap-16.0/config.sh
@@ -0,0 +1,2 @@
+DISTNAME=opensuse
+RELVER=leap-16.0
diff --git a/image-scripts/builders/opensuse-leap-16.0/setup.sh b/image-scripts/builders/opensuse-leap-16.0/setup.sh
new file mode 100644
index 000000000..397db75f0
--- /dev/null
+++ b/image-scripts/builders/opensuse-leap-16.0/setup.sh
@@ -0,0 +1 @@
+:
diff --git a/image-scripts/images/opensuse-leap-16.1/config.sh b/image-scripts/images/opensuse-leap-16.1/config.sh
index 531649678..a2048acb9 100644
--- a/image-scripts/images/opensuse-leap-16.1/config.sh
+++ b/image-scripts/images/opensuse-leap-16.1/config.sh
@@ -1,4 +1,4 @@
-BUILDER=opensuse-leap
+BUILDER=opensuse-leap-16.0
 SPIN=leap
 SPINVER=16.1
 RELVER=$SPIN-$SPINVER
```
