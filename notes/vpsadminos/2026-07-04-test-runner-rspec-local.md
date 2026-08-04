# test-runner RSpec Local Setup

Related initiative: `work/2026-07-04-test-runner-status/`.

When running `test-runner` specs from the repository root, add the spec
directory to Ruby's load path:

```sh
nix develop .#test-runner --command env TMPDIR=/tmp bundle exec rspec \
  -Itest-runner/spec test-runner/spec
```

Without `-Itest-runner/spec`, specs can fail before examples with
`cannot load such file -- spec_helper`.

The `test-runner` specs require `libosctl/native`. In a fresh worktree, build
the local native extension the same way as the RSpec workflow:

```sh
nix develop .#test-runner --command bash -lc \
  'cd libosctl/ext/libosctl && \
   ruby extconf.rb && make && cp native.so ../../lib/libosctl/native.so'
```

Do not use the test-runner bundle's `rake compile` for this step. That bundle
does not contain `rake-compiler`, so it fails with
`cannot load such file -- rake/extensiontask`.

The Nix shell may set `TMPDIR` to a private `/tmp/nix-shell.*` directory.
Set `TMPDIR=/tmp` inside the `nix develop --command` invocation when running
CLI specs that assert default state paths under `/tmp/os-test-runner`.
