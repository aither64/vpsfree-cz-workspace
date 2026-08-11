# `pkgsStatic.runCommandCC` may omit the compiler

Initiative: `work/2026-08-09-kb-kvm-review`

Building a small static C test appliance with
`pkgs.pkgsStatic.runCommandCC` selected the musl target, but the builder failed
with `cc: command not found` before compilation.

Use `pkgs.pkgsStatic.stdenv.mkDerivation` with ordinary `buildPhase` and
`installPhase` hooks instead. Its `$CC` is the target compiler and produces the
expected static executable. Verify the result with `file` and `ldd` in addition
to the consuming derivation build.
