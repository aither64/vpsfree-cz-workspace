# Test-runner specs in a fresh vpsAdminOS worktree

## Symptom

Focused test-runner specs in a fresh worktree can fail while loading with
`cannot load such file -- libosctl/native`. The native extension is a local
build artifact and is not present in a new checkout.

Using the `libosctl` Bundler environment may also fail when a shared
`/tmp/dev-ruby-gems` contains gems from another shell, with Bundler reporting
that an exception status code is already registered.

## Workaround

Compile the extension directly in the test-runner shell and expose its build
directory to the spec process:

```sh
nix develop .#test-runner --command bash -c \
  'cd libosctl/ext/libosctl && ruby extconf.rb && make'
nix develop .#test-runner --command env \
  RUBYLIB="$PWD/libosctl/ext" bundle exec rspec -Itest-runner/spec TESTS...
```

This avoids the shared Bundler directory and does not copy generated files
into tracked source paths. The disposable worktree can be removed normally
afterward.

## Verification

The retry-classifier and evaluator specs passed all 50 examples after using
this setup. Related initiative:
`work/2026-09-02-kb-runtime-reliability/state.md`.
