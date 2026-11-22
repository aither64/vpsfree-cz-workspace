# Focused session Ruby checks need the aggregate entry point

Session tests under `test/dev_session/` share fixtures loaded by
`test/dev_session_test.rb`. Directly running an individual feature file can
leave NullTmux/ManagedTmux unavailable because their support is defined in the
lifecycle commands test. Use the aggregate entry point with Minitest `--name`
to select a feature while retaining fixture loading, for example:

```sh
ruby test/dev_session_test.rb --name "/creation|fork/"
```

The portal creation initiative used this path successfully for60 tests and624
assertions in the repository Nix environment. Related initiative:
`work/2026-10-02-portal-creation-performance/`.
