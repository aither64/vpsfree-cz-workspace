# Final review packet

Request: add openSUSE Leap 16.1 container build script and image repository
configuration. Scope: vpsadminos only, target staging. Acceptance: conventional
new build/config, preserved older images, unique latest/stable tags for 16.1,
explicit cgroupAll/systemd matrix entry, valid/discoverable scripts, followed by
actual candidate image build/runtime test after review.

Session: 2026-11-03-opensuse-leap-image-build. Read plan.md, state.md, design.md
and implementation-result.md here. Worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-opensuse-leap-image-build/vpsadminos.

Base: dd188397abe37d0bc33f4c5dfb3605206ce5e326.
Head: f0e1656cd840cdd2c5180340241f798614fe23d1.
Tree: 05b7f416e90b321f7d9c81a21198ed8d5b1625a5.
Published feature branch: 2026-11-03-opensuse-leap-image-build, exact remote head
verified by implementer. No merge/deployment authorized or performed.

Risk classification: high, conservatively because this new userspace image
changes future default openSUSE container selection and must boot under host
cgroups and LXC/user namespaces. No host behavior, API, protocol, persistence or
schema change; no coordinated node upgrade required. All four lanes apply:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Reviewer: retained reviewer0, gpt-6.1-sol/xhigh, independent read-only purpose;
verified ready same-session, no settings override/fallback.

One coherent commit owns build files, repository registration and required test
matrix. No migrations (merged, released, deployed or externally consumed), no
superseded iterations, fixups, compatibility shims, dependency/channel/pin update
streams or generated changes. Assess these conclusions independently against
whole branch history and final diff. Full series/diff below.

Non-goals: site configs, pins, helper/builder refactors, new testing framework,
production image publication, merge/deployment. Existing Leap builder/helper
preserved; upstream 16.1 repository and bootstrap package availability verified,
including systemd 257.13 supporting proposed existing cgroup classification.
Build test still needs to prove actual compatibility. Latest/stable moves to
16.1; explicit 16.0 and 15.6 preserved. New script/source must reach builder
before activation of new repository job. Rolling back registration does not
modify existing containers.

Owning public image identity: opensuse/leap-16.1/x86_64/vpsadminos/minimal;
osctl-image consumes scripts, image-repository config schedules publication,
distribution matrix selects explicit image version for tests. Shared helper,
builder and interface contracts are unchanged. Check representative existing
Leap16.0 sources/config and test discovery behavior.

Docs checked: image-scripts/README.md, docs/container-images/creating.md,
docs/container-images/repositories.md and repository add-image-build-script skill.
No project prose change useful for conventional release addition; temporary
upstream, rollout assumptions and verification evidence live in design/state.

Quick checks passed: bash -n both new scripts; nix-instantiate --parse both changed
Nix files; git diff --check; full nix develop --command overcommit --run (Nixfmt
and RuboCop); installed commit hooks passed. Nix environment push succeeded.
Test discovery passed and found target image test plus three distro cases.
Raw discovery log also confirms both cgroups/mount-v1 and mount-v2 cases;
lead corrected the watcher's inaccurate no-match summary without rerunning.
See test-discovery-result.md. No long tests run yet. Planned primary test uses
retained disposable state to permit extraction/reuse of candidate for focused
checks; don't accept tests using public older latest as candidate coverage.

Report findings by severity with evidence, residual risks and explicit complete
history/no-migrations/update-stream conclusions. Stay read-only, no nested agents.

## Complete series

```text
commit f0e1656cd840cdd2c5180340241f798614fe23d1
Author: Jakub Skokan <jakub.skokan@havefun.cz>
Commit: Jakub Skokan <jakub.skokan@havefun.cz>

    image-scripts: add opensuse-leap-16.1
    
    Use the existing Leap builder and bootstrap sequence to build the new
    release without changing older image definitions. Make Leap 16.1 the
    default stable openSUSE image while preserving explicit version selection.
    
    Register the exact release in the distribution test matrix so its systemd
    and cgroup behavior can be verified independently of the latest tag.
```

## Final diff

```diff
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
