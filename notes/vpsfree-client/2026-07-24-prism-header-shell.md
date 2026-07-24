# vpsfree-client shell cannot build current Prism

Initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix/`

## Symptom

Entering `nix-shell` resolves the current public dependency graph, including
`vpsadmin-client` 4.2.0 and `haveapi-client` 0.29.5, but Bundler fails while
building `prism` 1.9.0:

```text
prism.h is required
```

The shell hook does not abort the requested command, so a following
`bundle exec rake build` can still run and mask the failed dependency install.

## Cause

The legacy `shell.nix` uses the default Nixpkgs Ruby and an ad-hoc writable gem
home. That environment does not expose the headers needed to compile the
current Prism gem selected through ActiveSupport/Minitest.

## Workaround

Use a maintained repository Nix development shell with a complete Ruby native
extension toolchain for isolated registry-backed installation. Check the
shell-hook output explicitly; do not treat a successful later command as proof
that `bundle install` succeeded.

The related release artifact was built successfully and verified in the
vpsAdmin root Nix shell. Updating vpsfree-client's development shell remains a
separate maintenance task.
