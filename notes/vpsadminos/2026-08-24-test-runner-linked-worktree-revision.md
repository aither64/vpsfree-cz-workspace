# vpsAdminOS test runner loses revision in linked worktrees

## Symptom

Running the CI selection from a linked Git worktree can fail while evaluating
`zfs/block-cloning-corruption`:

```text
environment.etc."runit/services/channel-registration/run".source
error: cannot coerce null to a string: null
```

The failure occurs before a VM starts. Tests that leave
`os.channel-registration.enable` disabled are unaffected.

## Cause

The test runner resolves the repository with `builtins.getFlake` and passes its
plain store `outPath` to later test evaluations. That snapshot contains the
linked worktree's `.git` file, while `os/modules/misc/version.nix` only derives
the revision from a `.git` directory or `.git-revision`. The later path-flake
evaluation therefore sets `system.vpsadminos.revision` to null, and
`channel.nix` cannot interpolate it when building the local channel source.

A normal GitHub Actions checkout has a `.git` directory, so its snapshot
retains enough repository structure for revision discovery. In vpsAdminOS run
`32668034165`, the same `zfs/block-cloning-corruption` test passed in 115.43
seconds.

## Workaround and verification

Use the normal GitHub Actions run to validate channel-registration tests, or
run them locally from a normal clone rather than a linked worktree. Do not
treat this evaluation failure as a guest or kernel failure.

The durable fix is to preserve explicit source revision metadata when the test
runner creates its immutable repository snapshot instead of depending on the
shape of `.git`.

Related initiative:
`work/2026-08-23-vpsadmin-ci-failure/`.
