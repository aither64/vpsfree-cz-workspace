# Loading a fetched source as a flake

During `work/2026-10-12-streamline-vpsadminos-config-imports`, historical guest
fixtures fetched exact nixpkgs revisions and NAR hashes with `builtins.fetchTree`.
`builtins.getFlake "path:${source.outPath}"` then refused the locator because the
interpolated string retained its Nix store reference context.

For this verified immutable source, pass a context-free locator:
`builtins.getFlake (builtins.unsafeDiscardStringContext "path:${source.outPath}")`.
The fetchTree revision and NAR hash remain the source identity and integrity
check; clearing the locator context does not change which source was fetched.
Read Nix's string-context and getFlake documentation before applying this to a
new boundary. Do not discard context from derivation dependencies generally.

The fixture was corrected and syntax-checked. Multi-release behavioral
verification is recorded in the initiative state and verification logs.
