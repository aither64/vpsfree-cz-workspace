# Retain candidates during long verification

A consuming workspace candidate passed a `nix build --no-link` and browser
checks, then its exact store path was absent after lengthy private history
setup. The parent confirmed the absence. The specific removal operation was
not established; an unrooted build does not retain its output through garbage
collection.

Re-realize the unchanged source using a private `--out-link`, and verify that
the link and build JSON select the original expected store path. This run
returned the identical candidate and repeated its package checks successfully.
Keep that GC root through verification and activation; creating it does not
select the application profile.

Place the link outside a guarded benchmark evidence directory whose inventory
is intentionally exact. Preserve earlier logs and failed setup evidence. Do not
change dependency pins, accept a substitute package, or activate early merely
to retain a build output.

A host configuration output also disappeared while the later checks ran. The
recorded derivation was absent too, so direct re-realisation could not rebuild
it. Use the owning configuration tool to reconstruct the build, then retain
the expected system output with `nix-store --realise <output> --add-root <link>`.
Keep its generation metadata and verify the output before deployment. The
specific removal operation remains unknown.

Related initiative: `work/2026-10-02-portal-creation-performance/`.
