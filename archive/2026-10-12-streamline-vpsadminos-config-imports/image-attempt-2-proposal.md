# Image test metadata proposal

This proposal executes no test and changes no repository source. It supplies
verified host metadata through existing public configuration interfaces.

Final source: `7e79afd4690ff5abac2554fd2a02ba8e8c97c0b1`, tree
`613cc6046198119575728cd7f745a1c86f6a5ab6`, clean published feature worktree.
The first attempt used `/nix/store/bnahikd1zf4271n989bqwz9m2pgj7jv2-source`.
All 2371 tracked files, executable flags and symlink targets in that snapshot
match the clean final source checkout. No feature diff touches the runner,
make-test, raw OS evaluator, version module, channel module or kernel selection.
Those paths are identical to initial base `1150e37b`.

The failure occurs before VM boot: channel.nix interpolates
`system.vpsadminos.revision` into its generated .git-revision write. The snapshot
contains a .git **file** (a worktree gitdir pointer), while version.nix requires
.git to be a directory. It has no .git-revision file, so its revision is null.
This is baseline behavior rather than a guest selector or runtime finding.

`image-host-metadata.nix` supplies the verified full source revision and
`revisionDirty = false`. The latter is truthful for the proven clean source;
it does not claim the test machine is an unmodified production configuration.
The proposed suffix `.git.7e79afd46` uses this repository's current Git short
abbreviation. Raw version.nix's own directory-Git fallback takes seven
characters (`.git.7e79afd`); the flake wrapper uses self.shortRev or a seven-char
fallback. The explicit nine-char suffix is a valid accurate label, not a claim
that the raw module truncates to nine. Either accurate prefix leaves kernel
settings unchanged, but choosing a different label changes host derivation names.

A template test without --test-config uses flake.tests, explicitly defined with
configuration = null. Setting VPSADMINOS_CONFIG alone therefore cannot fix
image-scripts/test@... evaluation. Supply `image-test-config.nix`, which returns
the unchanged default empty framework object. This public runner option selects
testFramework.mkTests/mkTestsMeta and forwards the imported VPSADMINOS_CONFIG
through make-template, make-test and os/default.nix. Both files live outside the
source worktree, so the source snapshot and guest lock revision stay unchanged.

The existing test-runner.sh computes TEST_RUNNER_REPO_REV from final Git HEAD.
RepositorySource changes TEST_RUNNER_REPO_ROOT to its immutable snapshot while
leaving that revision intact. The image test's osctl-image command exports it as
OSCTL_IMAGE_VPSADMINOS_REV. The existing image builder copies that snapshot,
writes .vpsadminos-git-rev before removing .git, and flake.nix uses that recorded
SHA to generate the guest lock. The host metadata module changes none of those
paths. Verify the next generated test JSON still names the exact source snapshot
and includes the full SHA in OSCTL_IMAGE_VPSADMINOS_REV before accepting a run.

The module sets no boot/kernel or enableUnstable options. Stable host kernel
selection remains 6.12.109, with its existing Linux/ZFS inputs and configuration.
Host channel derivations, os-release/security evidence, squashfs and toplevel
will gain the revision/label and may need rebuilding or substitutions. The
kernel derivation should remain unchanged; stop unexpected kernel builds under
the usual cache policy. No new guest input, lock, release or stateVersion is set.

Proposed first-case command, to be launched only by the lead's authorized
watcher/fallback from the vpsadminos worktree:

```sh
VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/image-host-metadata.nix \
  ./test-runner.sh test \
  --test-config /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/image-test-config.nix \
  --state-dir /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos/result/config-imports-image-tests \
  --fresh --jobs 1 image-scripts/test@nixos-26.05
```

After the first case reaches real guest verification, use the same module,
empty test config and explicit state directory for the remaining three image
cases. Retain attempt-1 state/logs; no /tmp cleanup is proposed. This source
trace establishes the intended evaluation path; no Nix evaluation or runtime
rerun was performed in this investigation.
