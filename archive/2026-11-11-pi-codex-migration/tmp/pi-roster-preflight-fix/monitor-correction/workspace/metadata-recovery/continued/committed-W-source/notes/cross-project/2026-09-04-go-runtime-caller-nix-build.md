# Go test fixture paths in Nix builds

Related initiative: `work/2026-09-03-dev-session-portal`

## Symptom

A Go test found repository fixtures in a normal worktree but failed in
`buildGoModule` with an empty fixture glob. The source archive contained the
files.

## Cause

The test derived the repository root from the filename returned by
`runtime.Caller`. Nix's Go build uses trimmed source paths, so that filename is
not a stable absolute path inside the builder.

## Fix

Resolve repository fixtures relative to the test process working directory.
Go runs a package's tests with that package directory as the working directory,
which remains stable when compiler source paths are trimmed.

## Verification

The package-local Go suite and the exact `buildGoModule` derivation both pass.
