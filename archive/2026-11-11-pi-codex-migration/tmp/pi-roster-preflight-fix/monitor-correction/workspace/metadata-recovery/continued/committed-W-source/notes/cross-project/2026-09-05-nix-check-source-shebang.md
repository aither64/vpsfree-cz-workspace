# Source helpers in Nix package checks

Related initiative: `work/2026-09-03-dev-session-portal`

`nix build` can report `fork/exec <helper>: no such file or directory` even
when the helper exists in the unpacked source. A source script with
`#!/usr/bin/env bash` cannot start in the Nix build sandbox because
`/usr/bin/env` is absent.

Patch source-script shebangs before a package check that executes them. This is
separate from patching or wrapping the installed copy in `postInstall`.

An installed-helper smoke test must also create any workspace path it passes
through `VPSFREE_DEVCLUSTER_WORKSPACE`. The helper resolves that directory
before it parses `--help`.

A full `nix build .#workspace-portal --no-link -L` passed after both fixtures
were added, including the source helper contracts and installed empty-`PATH`
checks.
