# vpsAdmin root shell resets package working directories

Initiative: `work/2026-07-13-security-advisory-automation`

Running `nix develop ../..#vpsadmin --command bundix -l` from a
`packages/<name>` directory does not regenerate that package. The root shell's
entry hook changes back to the repository root, so Bundix acts on the root
Gemfile and can create an unintended top-level `gemset.nix`.

Enter the root shell and change directory inside its command instead:

```sh
nix develop .#vpsadmin --command bash -lc '
  cd packages/api
  env -u GEM_HOME -u GEM_PATH -u RUBYLIB \
    -u BUNDLE_GEMFILE -u BUNDLE_PATH TMPDIR=/tmp bundix -l
  nixfmt gemset.nix
'
```

Delete the package lock first when reproducing the package-update task. This
regenerated the API, client, and download-mounter locks and gemsets with
HaveAPI 0.29.4; all three packages then built successfully.
