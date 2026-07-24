# Go client integration tests need the Ruby server bundle

## Symptom

Running a Go client integration spec in `nix develop .#client-go` failed before
the suite with `server did not start`. The test helper launches
`servers/ruby/test_support/client_test_server.rb`, but the Go client gem home
contained only the Go generator bundle.

## Cause

The `client-go` shell uses `clients/go/.gems` and sets `RUBYOPT` to load that
bundle. The shared Ruby test server has additional dependencies from
`servers/ruby/Gemfile`. An inline `BUNDLE_GEMFILE` alone is insufficient while
the shell's `RUBYOPT=-rbundler/setup` is active.

## Workaround

Install the server bundle into the Go shell's gem home without the preloaded
client bundle, then run the client spec:

```sh
env -u RUBYOPT BUNDLE_GEMFILE=../../servers/ruby/Gemfile bundle install
BUNDLE_GEMFILE=Gemfile bundle exec rspec spec/integration/generator_spec.rb
```

## Verification

The focused generated-client integration group completed with 7 examples and
no failures.

Related initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix`.
