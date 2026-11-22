# Use the repository shell for hook-enabled pushes

In the NixOS container import initiative, an ambient git push stopped at the
Overcommit configuration signature gate even though the preceding hook-enabled
commit had passed in the declared shell. The repository configuration was
unchanged. Running the same push through nix develop with the retained
result/config-imports-dev-shell profile passed all hooks and published the
feature revision. No signature check or hook was disabled.

Use the declared repository environment for commits and pushes. Keep its ignored
result directory present before asking Nix to create a profile beneath it; the
profile roots the tools during long sessions. A missing result directory caused
an earlier shell setup to fail after downloads, before any tests ran.

Evidence: work/2026-10-12-streamline-vpsadminos-config-imports/state.md and
vpsadminos-feature-push.log. This note records observed environment dependence;
the exact difference in ambient Overcommit configuration merging was not traced.
