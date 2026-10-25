# Combined server and Rust bundle readiness

The dependency closure is ready for exact reviewed HaveAPI
`67fcd34ba506264a5c7ee2e8e18a88d221c6f469`, tree
`80804b1c0c3ed33fc4b086673dbc3618a789cd4f`. This is session verification setup,
not a product dependency or release change. The real mount probe is a separately
authorized application check; dependency activation did not run it.

The manifest evaluates the owning server Gemfile and adds its own local Rust gem,
Fiddle1.1.8 and tomlrb2.0.5. The final lock SHA-256 is
`eb9c5f9fcbadc88ebdb7f0b5f6c6abc7c7e5efdcc96ea6eb0e5e2f138693af29`.
All95 external records retain qualified versions, dependency edges, platforms and
checksums;86 apply to this host and nine foreign SQLite platform records remain
in the lock. The server's mime-types-data3.2026.1020 is preserved. All three local
project versions are0.30.0 and resolve to the same owning worktree.

Original archives were verified before installation. Racc1.8.1's original archive
came from the exact selected Ruby's read-only cache under the lead's narrow grant;
no installed native gems were copied. The new own gem home is beneath
`<worktree>/.bundle/profiles-server-rust-mount/gems`. GEM_PATH includes only that
home and the selected Ruby default directory. Ruby3.4.11 and Bundler4.0.23 are
bound to the retained declared environment and full native derivation graph.
Nondefault Fiddle1.1.8 loads from the new own home.

Two failed setup receipts remain intact. The first stopped before dependency
installation because the server gemspec source's relative serialization differed
from a physically identical absolute PATH entry. The granted retry built native
dependencies, then stopped at final frozen lock comparison. Bundler's native
frozen serializer changed only the order of the server and Ruby-client PATH
blocks. `final-serialization/semantic-proof.json` proves every locked record,
requirement, platform and checksum unchanged. No resolver, network or installation
ran in that last correction. Its frozen check and third-party activation passed
in3.25 seconds; see `final-serialization/result.json` and the raw activation log.
Source775 files,166 installation inputs,five other locks,47 dist files and eight
generated server docs remained exact.

Use the accepted caller's source/input guards and a fresh evidence child for the
actual probe. `with_bundle.py` clears inherited Ruby/Bundler settings and restores
only this verified environment:

```sh
python3 -B /absolute/session/client-example-profiles-rust-mount/with_bundle.py -- \
  /nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby \
  -rbundler/setup /absolute/session/client-example-profiles-rust-mount/probe.rb
```

Set `HAVEAPI_REPO_ROOT`, fresh `HAVEAPI_RUST_MOUNT_EVIDENCE`,
`HAVEAPI_RUST_MOUNT_MODE=full`, `HAVEAPI_RUST_MOUNT_EXPECTED_VERSION=0.30.0`, and
inert `HAVEAPI_RUST_MOUNT_FORMATTER_VERSION=rustfmt 1.10.0`. The evidence directory
must not exist; its parent must exist within this session. A later version-subset
requires actual prepared matching project versions and newly bound local lock
metadata; this0.30.0 receipt is not fresh0.30.1 evidence.

No root, native home, failed receipt or original artifact is removed by this
handoff. Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
