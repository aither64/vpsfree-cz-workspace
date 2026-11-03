# Local image-test evaluation failure: cause and proposed correction

Investigation only; source remains `3307df52ea5bf875e1d8a23318a64f569d8b3ebc`.
No application edits, CI actions or image retest. The metadata workaround path
was stopped on the lead's latest direction. No command or utility remains active.

## Proven local call chain

1. `test-runner/lib/test-runner/cli/command.rb:138-166` resolves the tested
   repository and replaces `TEST_RUNNER_REPO_ROOT` with its immutable source.
   `test-runner/nix/resolve-repository-source.nix:8` retains only
   `(builtins.getFlake (builtins.toString repoRoot)).outPath`.
2. `test-runner/nix/evaluate-tests.nix:16,81-107` reopens that source and resolves
   the image template. `tests/make-test.nix:104-128` imports `../os` directly.
   This path does not use the OS flake builder's source-identity module at
   `flake.nix:181-224`; the test framework exposes source paths and nixpkgs
   identity at `flake.nix:83-96`, but no equivalent vpsAdminOS source identity.
3. `os/modules/misc/version.nix:99-108` declares
   `system.vpsadminos.revision` as `nullOr str`. Its default reads a `.git`
   DIRECTORY, else `.git-revision`, else assigns `null`.
4. The failed source is `/nix/store/32fjrfl8xrvkl326xzyjrmnv5jxxmv1g-source`.
   Its `.git` is a linked-worktree pointer FILE containing
   `gitdir: /home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git/worktrees/vpsadminos2`;
   `.git-revision` is absent. Native module evaluation returned
   `revision=null`, `versionSuffix="pre-git"`.
5. `tests/suite/image-scripts/test.nix:34` enables channel registration.
   `os/modules/installer/cd-dvd/channel.nix:95` unconditionally interpolates
   `${config.system.vpsadminos.revision}` while writing `.git-revision`.
   The option is null, so evaluation fails before the VM/image can build.

`test-runner.sh:7` already exports `TEST_RUNNER_REPO_REV`, but the image template
uses it only for the later in-VM `OSCTL_IMAGE_VPSADMINOS_REV` command
(`tests/suite/image-scripts/test.nix:45-53`), not the host VM's revision option.
NIX_PATH is not the cause: the failed configuration uses the pinned nixpkgs at
`/nix/store/2xl4y8v0mpkqbvxdra2c0ci02w8mczyy-source`.

Baseline `dd188397abe37d0bc33f4c5dfb3605206ce5e326`, resolved as
`/nix/store/cgk63vdx1wjl4ybd53abkd5aqyzc7sfa-source`, also returned
`revision=null`, `versionSuffix="pre-git"` in native module evaluation. The
responsible files are unchanged in the release branch's four-line diff. This
supports the same pre-existing failure; no baseline image test was run.

## Smallest durable correction options, not implemented

- **Fix the nullable consumer:** emit `.git-revision` in `channel.nix` only when
  the revision is non-null, using `lib.optionalString`. This directly honors
  the existing option contract and avoids claiming an invented identity. It
  prevents this crash but leaves source identity unknown for these test VMs.
- **Preserve source identity through the framework:** retain verified revision
  and dirty-state metadata when resolving the original source, and pass it with
  the immutable snapshot into the existing OS metadata options. Reuse the
  flake builder's identity rules rather than inspecting live Git state from a
  snapshot. This restores provenance as well as preventing the null here, but
  needs a separate approved framework change and focused verification for
  ordinary checkouts, linked worktrees, dirty sources and Git-free snapshots.

Changing only `pathIsDirectory` to `pathExists` is insufficient: nixpkgs can
follow a worktree file, but its absolute pointer refers to mutable external
Git metadata. It would not reliably identify the retained snapshot and would
not support snapshots without `.git`.

CI's image workflow invokes the same runner (`.github/workflows/image-scripts.yml:131`),
so the snapshot/direct-import issue plausibly applies there. A normal checkout
starts with a `.git` directory, unlike this worktree. The actual failed CI
trace, revision, source form and effective configuration are still needed to
establish whether CI or the historical Fedora 45 run has this same cause.
The lead owns that evidence; no CI cause is claimed from local evidence alone.

## Preserved evidence and discontinued workaround

Original logs are unchanged:

- `image-tests.log`: SHA-256 `bd8a739d3d0b05d2021b47c80c17510a86f4ef2ff44d0022032d7d91b456d0df`.
- `/tmp/redhat-image-releases-2026-11-03/os-test-image-scripts__test__centos-10-stream-150f32eb/test-runner.log`:
  SHA-256 `68f0c8ab41b1c4ffc9b2962f63d9a4eaaeb5923f0e88a6c6ae0f2bef922f9c3b`.

The temporary native `VPSADMINOS_CONFIG` module
`/tmp/redhat-image-releases-2026-11-03-source-metadata.nix` sets revision to
`3307df52ea5bf875e1d8a23318a64f569d8b3ebc`, revisionDirty=false and
versionSuffix=".git.3307df5". Module-only evaluation confirmed those values.
This was a diagnostic override, not a durable fix or accepted verification.
Its SHA-256 is `d3f6313b7f870a8c460ef4f77d89eb28c586e565e7d23193568b33288039d3af`.

A bounded utility instantiated a JSON derivation, then exited 1 because an
extra positional `.` made it also look for worktree `default.nix`; the brief's
command punctuation caused that separate command error. Evidence remains at
`/tmp/redhat-image-releases-corrected-eval.{log,exit}`. It was not a successful
full check and will not be retried under the current investigation-only scope.
The utility finished; its brief overlap with the closing CI observer was
reported to the lead. No build or cancellation occurred.

Git/config writer authority is released to the lead. No tracking commit made.
