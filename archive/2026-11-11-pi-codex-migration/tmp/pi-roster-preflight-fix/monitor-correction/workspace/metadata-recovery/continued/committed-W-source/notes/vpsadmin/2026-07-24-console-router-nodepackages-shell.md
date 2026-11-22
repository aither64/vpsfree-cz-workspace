# console-router shell references removed nodePackages

Initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix/`

## Symptom

`nix develop .#console-router` fails during evaluation with:

```text
nodePackages has been removed
```

## Cause

The console-router development shell still lists
`nodePackages.npm`, while the current pinned nixpkgs exposes npm/node tools
through top-level packages.

## Workaround

For a standalone JavaScript syntax check, use:

```sh
nix shell nixpkgs#nodejs --command node --check FILE
```

The HaveAPI 0.29.5 initiative used this fallback for both vendored client
files. The console-router shell definition still needs a separate maintenance
change.
