# Adding a new flake input with confctl

## Symptom

Running this for a newly declared input did update `flake.lock`, but created no
generated commit:

```sh
nix develop -c confctl inputs channel update --commit bun2nix
```

## Cause

Entering the dirty checkout's development shell evaluated `flake.nix` before
starting `confctl`. Nix added the newly declared input to `flake.lock` during
that evaluation. By the time `confctl` read the lock, it was already current,
so its change set was empty and `--commit` had nothing to commit.

## Workaround

First ensure the worktree lock still matches `HEAD`, then run an already built
`confctl` executable directly, without evaluating the dirty flake first:

```sh
/nix/store/...-confctl/bin/confctl inputs channel update --commit bun2nix
```

Use the actual store path supplied by the repository's development shell. Do
not hard-code the example path in scripts. Ensure the repository's hook
dependencies are available in the ambient environment before the direct
invocation, because the generated commit still runs Git hooks.

## Verification

The direct invocation generated commit `53bd859d` with the exact message
`inputs: update bun2nix to 5a39d717`. Overcommit's pre-commit and commit-message
hooks passed, and the resulting flake passed `nix flake check --no-build`.

Related initiative: `work/2026-07-16-codex-lb-update/`.
