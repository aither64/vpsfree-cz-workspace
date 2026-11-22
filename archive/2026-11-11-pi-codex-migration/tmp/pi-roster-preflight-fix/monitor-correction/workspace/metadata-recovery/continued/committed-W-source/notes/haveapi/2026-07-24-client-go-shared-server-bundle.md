# Client integration tests need the Ruby server bundle

## Symptom

Running Ruby, Go, or JavaScript client integration specs in their component
shells can fail before the suite with `server did not start`. The test helpers
launch `servers/ruby/test_support/client_test_server.rb`, but component
environments can contain only the client dependencies.

## Cause

The shared Ruby test server has additional dependencies from
`servers/ruby/Gemfile`. The `client-go` shell also uses `clients/go/.gems` and
sets `RUBYOPT` to load the client bundle. An inline `BUNDLE_GEMFILE` alone is
insufficient while that `RUBYOPT=-rbundler/setup` is active.

## Workaround

Install the server bundle into the active component shell's gem home without
the preloaded client bundle, then run the client spec:

```sh
env -u RUBYOPT BUNDLE_GEMFILE=../../servers/ruby/Gemfile bundle install
BUNDLE_GEMFILE=Gemfile bundle exec rspec spec/integration/generator_spec.rb
```

For JavaScript, prepare `servers/ruby/Gemfile` in the top-level Ruby gem home
and run `npm test` from the default `nix develop` shell so the helper sees that
gem home.

## Verification

The focused Ruby association specs, JavaScript description-member specs, and
Go generated-client member-name spec all passed after preparing the appropriate
server bundle.

Related initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix`.
