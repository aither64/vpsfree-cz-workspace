# Ruby 3.4 RuboCop installation in Nix shells

## Symptom

Exporter shell startup under Nixpkgs Ruby 3.4.9 ran `gem install rubocop`.
Prism 1.9.0 was downloaded with `include/prism.h`, but its native extension
failed to compile because the Nix compiler could not resolve that header.
Overcommit was installed, but its RuboCop hook then failed because no RuboCop
executable was available.

## Cause

The exporter shells installed their hook tooling imperatively into a local
`GEM_HOME`. The current RuboCop dependency chain includes a native Prism gem
that does not build correctly through this ad-hoc installation in the Nix Ruby
3.4 shell.

## Fix

Provide `rubyPackages.rubocop` through `buildInputs` and stop installing
RuboCop with `gem install`. Overcommit can continue to be installed locally;
its hook finds the Nix-provided RuboCop executable on `PATH`.

## Verification

Re-enter the shell, confirm `rubocop --version`, then run `overcommit --run`.

Related initiative: `work/2026-08-07-exporters-gem-update/`.
