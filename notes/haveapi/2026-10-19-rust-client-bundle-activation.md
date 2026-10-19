# Rust client harnesses need explicit bundle activation

In the Rust generator session, plain `ruby clients/rust/spec/integration/run.rb`
failed before Cargo because setting `BUNDLE_GEMFILE` alone does not activate
Bundler. The generator depends on the sibling Ruby client as a path dependency;
an unrelated globally installed gem can hide the omission during local checks.
The runner now selects its component Gemfile and requires `bundler/setup` before
loading generator code. Its regression isolates the gem paths and verifies the
loaded client comes from the sibling checkout.

A separate server process needs its own bundle. Start it inside
`Bundler.with_unbundled_env`, select the server Gemfile and gem home, and avoid
restricting `GEM_PATH` to that gem home alone. The Nix Ruby distribution also
supplies gems in its default paths. Restricting GEM_PATH caused `net-pop` lookup
failure in the server probe and `rexml` lookup failure in commit hooks. Unsetting
GEM_PATH restored those defaults; no reinstall or hook bypass was needed.

The focused bundle-activation and fixture-contract checks passed 16 examples before
the real-server run. This repairs Ruby setup only; it does not establish that the
subsequent generated Rust fixture compiles or passes its protocol assertions.

Session: [Rust client generator](../../work/2026-10-18-rust-client-generator/state.md).
Related: [extracted-gem dependency paths](2026-10-12-extracted-gem-bundler-paths.md).
