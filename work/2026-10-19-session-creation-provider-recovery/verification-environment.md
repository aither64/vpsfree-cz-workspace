# Verification environment correction

The first whole Go suite on 3c0b459 stopped with exit 1; its browser command did
not run. The full original log and JSON result are retained. No rerun is accepted
without explaining both observed causes:

- Recovery tests bind Unix sockets below Go's t.TempDir. Nix develop set TMPDIR
  to `/tmp/nix-shell.5ajCgx`; combined test/subtest names produced socket paths
  beyond Linux's Unix address limit, and bind returned invalid argument. Set
  TMPDIR=/tmp for the test process after entering the shell, preserving short
  paths as in packaged sandbox execution.
- Naming-runtime lifecycle fixtures build an unmanaged portal with no workspace
  name. The live host's `/etc/dev-workspaces/codex-providers.json` was visible
  through codexproviders.CatalogPath, so initialization tried to read provider
  state with an empty workspace identity. The Nix sandbox has no such catalog.
  Set DEV_WORKSPACES_CODEX_PROVIDERS to an explicitly nonexistent path beneath
  this initiative for local verification. Tests requiring providers install their
  own catalog with t.Setenv and remain covered. No live configuration is changed.

No production failure is attributed to these fixture/environment errors. Focused
provider-contract tests had already passed. The corrected whole suite and actual
browser test will run under a fresh verification utility. Package verification
still runs in the declared Nix sandbox and is not replaced by this local check.

Existing workspace notes independently document the same environment causes:
`notes/dev-workspace/2026-10-14-go-web-tests-host-provider-catalog.md`,
`notes/dev-workspace/2026-10-15-source-fixture-provider-catalog.md` and
`notes/codex-web/2026-10-03-nix-shell-unix-socket-paths.md`. The corrected command
uses their documented isolation; no source change or test omission was needed.
