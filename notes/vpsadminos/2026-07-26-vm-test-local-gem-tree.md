# Local gem trees can pollute vpsadminOS VM builds

## Symptom

`./test-runner.sh test osctld/lifecycle` failed while building
`ruby3.4-osctld`, before the VM started. `gem build` reported that files
listed by a nested `bundler.gemspec` were missing.

## Cause

A package-local `osctld/.gems/` made for direct Bundler/RSpec runs was ignored
by Git, but still entered the local Nix source used to build the osctld gem.
Gem file discovery then treated specifications from the nested Bundler cache
as part of osctld. Checking only the repository root misses this cache.

## Workaround

Before running vpsadminOS VM tests from a worktree used for direct Ruby tests,
search the whole worktree and move generated `.gems/`, `.native/`, and
gem-local `tmp/` trees outside the repository. Keep their location if the
direct Ruby environment must be restored later. Do not rerun the VM test until
the source tree is free of generated package trees.

## Verification

The original failure was retained at
`/tmp/os-test-runner/os-test-osctld__lifecycle-000573c0/test-runner.log`.
The initiative retried the lifecycle VM after moving the generated directories.

Related initiative: `work/2026-07-24-ct-start-hang/`.
