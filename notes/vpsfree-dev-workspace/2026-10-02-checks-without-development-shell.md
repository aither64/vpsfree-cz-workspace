# Provider flake without a development shell

At provider revision `c56f981a`, `nix develop -c ...` fails before running the
command: the flake exports checks, an app and a named package, but no development
shell or default package. This is an interface mismatch, not a failed test or
commit hook.

Use the pinned input packages for short commands:

```sh
nix shell --inputs-from . nixpkgs#git -c git commit -F /tmp/message.txt
```

For focused Ruby checks, select the tools and environment used by the owning
`checks.x86_64-linux.tests` definition in `flake.nix`. Do not assume that
another repository's component shell exists here. Use the packaged checks for
the full suite after the required review.

The pinned Ruby shell can still discover user gems. A local Minitest 6.0.6
shadowed the bundled 5.25.4 and failed to load `minitest/mock` before any examples
ran. Isolate the bundled gems inside the pinned shell, before invoking tests:

```sh
unset RUBYOPT
provider_gems="$(ruby --disable=gems -rrubygems -e 'print Gem.default_dir')"
export GEM_HOME="$provider_gems" GEM_PATH="$provider_gems"
```

The loader then selected the Nix store's Minitest 5.25.4 with `minitest/mock`.
No gem installation or application change was needed. A refused loader is not
a failing test result; retain it separately from the actual example run.

The storage-profile runtime pin committed normally with the command above
after `nix develop` refused; no hook was bypassed and no commit was created by
the refused attempt. See [the session state](../../work/2026-09-23-storage-redesign/state.md).
