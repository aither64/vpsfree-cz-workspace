# system/install needs revision metadata in linked worktrees

## Command and symptom

Running `./test-runner.sh test system/install` from a linked vpsadminos Git
worktree failed during Nix evaluation, before VM startup, with
`cannot coerce null to a string: null`. The full trace pointed to interpolation
of `config.system.vpsadminos.revision` in
`os/modules/installer/cd-dvd/channel.nix`.

## Cause

`os/modules/misc/version.nix` detects a development checkout with
`pathIsDirectory <repo>/.git`. A linked worktree has a `.git` file, not a
directory, and its flake source does not contain `.git-revision`, so the
revision becomes null. GitHub Actions uses a normal checkout with a `.git`
directory and does not hit this failure.

## Workaround and verification

Supply the exact tested commit through a temporary Nix module and run with the
CI test config:

```nix
{ ... }:
{
  system.vpsadminos.revision = "<full-commit-id>";
  system.vpsadminos.versionSuffix = ".git.<short-commit-id>";
}
```

```sh
VPSADMINOS_CONFIG=/tmp/exact-revision.nix \
  ./test-runner.sh test --test-config tests/test-configs/ci.nix system/install
```

This workaround was verified for commit `173ebb60552fa5e42ab444b4bca37d64b85f2ee1`:
all six examples and the `system/install` test passed. See
`work/2026-07-21-system-install-failure/`.
