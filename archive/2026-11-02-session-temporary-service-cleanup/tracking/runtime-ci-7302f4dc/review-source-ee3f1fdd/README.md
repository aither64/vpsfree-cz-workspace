# Active review source snapshot

This temporary root retains exact runtime ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f
for the active independent review. Source, commits and pins are unchanged.

Exact-revision LOCAL Git flake metadata restored
`/nix/store/8ygzal9j12xj6x600ws7yrhgn1ijngx2-source`.
An independent `nix hash path` returns the originally recorded NAR
`sha256-5mDdLgLQl/XPjIs9Ey5l2UDxWwVKR/VWpNCQwEvqsiw=`.
All 672 committed file contents and Git modes match; the source has no extra files.
The manifest preserves each Git blob ID, SHA256, Git mode and actual store mode.
Nix store files are read-only; executable bits are compared to Git exactly.

The ordinary indirect GC root is the `source` symlink in this directory, created
with `nix-store --add-root ABSOLUTE_SOURCE_LINK --indirect --realise STORE_SOURCE`.
The argument was the already restored source store path, not a derivation.
No package or test was built. `roots.txt` confirms registration of this exact root.
`receipt.json` records complete commands, provenance and supporting checksums.

The earlier source disappearance is unexplained. The old metadata receipt did
not retain an explicit review GC root; that alone does not prove collection.

Keep this root while the active review needs the source. Once its owner retires
that evidence dependency, remove only this directory's `source` symlink using
ordinary `unlink`; normal Nix garbage collection may subsequently reclaim it.
Do not remove the Nix store source directly or change global GC policy. No root
retirement has been performed as part of this repair.
