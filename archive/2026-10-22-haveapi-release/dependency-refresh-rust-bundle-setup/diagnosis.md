# Prism setup diagnosis

The parsed `nix print-dev-env` session script retained derivation-only
`NIX_ENFORCE_PURITY=1`, with `NIX_BUILD_TOP` and temporary directory variables
set to `/build`. The selected Nix GCC wrapper removes absolute include paths
outside the store and permitted build/temporary directories. That removes the
exact `/home/.../clients/rust/.gems/gems/prism-1.9.0/include` argument shown in
the failed mkmf command. The compiler therefore reports missing `prism.h`.

The header is present. All150 payload files match the cached original gem. The
local Prism headers, including generated ast/version and extension headers,
are present; the compiler error is at prism.h itself, not a nested include. The
one official RubyGems metadata GET returned HTTP200 and SHA256
`7b530c6a9f92c24300014919c9dcbc055bf4cdf51ec30aed099b06cd6674ef85`, identical
to the cache and committed lock checksum. No payload or version change is needed.

Read-only reconstruction used the unchanged frozen flake/lock and the original
script import semantics. The failed script did not persist a separate full
environment snapshot. Its selected Ruby store path matches the old component's
successful mkmf log; the old component also has the same Rust lock and exact
Prism payload SHA. Its absolute include check succeeded. Historical mkmf names
only `gcc`, so complete wrapper/input identity is not asserted or reused as
verification. The retained R1 frozen setup reports success with the same lock,
but installed only Fiddle in that step. Downstream Ruby3.3.10 setup and CI
version strings are not treated as equivalent tool evidence.

The smallest correction is session-only `NIX_ENFORCE_PURITY=0` scoped to the
frozen bundle install. The root flake already uses that precise accommodation
for Prism headers in a local gem home. Keep the declared Ruby/compiler, exact
Bundler4.0.23, frozen lock, own partial bundle and native identity guards. No
include override, source/flake/config/lock edit, upgrade or native borrowing is
required. Recovery needs its own granted operation and distinct evidence.

No install, compiler probe, retry or source/lock mutation ran during diagnosis.
See diagnosis.json, prism-payload-inspection.json, prism-official-observation.json,
declared-build-environment.json and the two copied mkmf logs. Original failure
evidence remains unchanged. Release0.30.1 remains held.
