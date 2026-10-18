# Quick checks at final compatibility revision

Runtime 79da0bb5eafd5b8e7cd4e32a02dc5a16da6116f6; workspace 524ba50b692a00b5119f4a35f194de67026737b0; configuration 35eeeddcfbcdf192c3cb2d0576ba364d38f9c6f4.

- Runtime focused pending manual/schema-2 retained compatibility: 3 runs, 33 assertions, zero failures/errors/skips (2.44s), Nix development shell.
- Go agentteams TestLoadInstalled: passed in 0.058s, -mod=readonly.
- Pinned nixfmt 1.4.0 --check passed on both changed Nix files. Runtime flake has no formatter output; nixfmt absent in dev shell, so used nix shell --inputs-from . nixpkgs#nixfmt.
- Ruby syntax and diff whitespace checks passed. No declared hook framework in runtime or workspace. Configuration Overcommit Nixfmt and commit-message hooks passed; generated width warning retained unchanged as required.
- Workspace/configuration composition contract passed at same final runtime; only dev-workspace/devWorkspace lock nodes changed from respective default branches. compat-pin-proof.json records this.
- Actual installed predecessor Store accepts unchanged schema-1 metadata with new sidecar and pending manual journal, journal unchanged. Metadata-2 negative control refuses: compatibility-predecessor-probe.json.

No superseded in-progress CI runs remain on this branch; older runs completed. New run 39014378649 started at exact final runtime.
