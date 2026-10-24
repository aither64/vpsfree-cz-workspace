# Composed verification and build result

Result: **incomplete**. All selected W/C checks, the composed workspace package, and the scoped confctl machine build succeeded. The required system build receipt command failed with exit 1, so processing stopped without retry. No activation, copy, deployment, or lifecycle action was performed. No owned process remains running.

## Source and coverage

- Session identity: `dev-session current` and both optional environment markers matched `2026-10-22-codex-thread-retries` at `/home/aither/workspace/ai/vpsfree.cz`.
- W `ebf6ab35c7754f9ac2e5474959259fdcef24a7c8`, tree `e46dfa5027a2e34cc083e6d41da78f7c60106d3e`; initial status clean.
- C `81d0e68c52762d3804e00e4c4ef99a421bafc05f`, tree `27b3b4425c9104269b5909a5d935eb94c6c954df`; initial status clean.
- W check inventory matched all four requested selectors; C matched all eight. Full flake metadata/lock graphs and selector-to-derivation/output maps are retained in this directory.
- Final-source deployment contract quick receipt was reusable from `c-repin-d819ad04.json` (exit 0 at the exact final W/C sources); it was not repeated.

## Operations

| Operation | Result | Elapsed |
| --- | --- | ---: |
| W/C Nix version and disk-space record | captured | recorded in `nix-version.*` and `space.*` |
| W `nix flake check --no-build --no-write-lock-file --print-build-logs` | pass, exit 0 | see `W-flake-check-no-build.elapsed` |
| C `nix flake check --no-build --no-write-lock-file --print-build-logs` | pass, exit 0 | see `C-flake-check-no-build.elapsed` |
| W selected check build (4 selectors) | pass, exit 0 | see `W-check-build.elapsed` |
| C selected check build (8 selectors) | pass, command exit 0 | see `C-check-build.elapsed` |
| Composed workspace profile package | pass, exit 0 | see `workspace-package.elapsed` |
| `CONFCTL_TTY=0 nix develop "$C" -c confctl --color never build --yes "$MACHINE"` from C | pass, exit 0 | see `confctl-build.elapsed` |
| Exact generation listing | pass, exit 0 | see `generation-list.elapsed` |
| Required Ruby system-build receipt | **failed, exit 1** | see `system-build-receipt.elapsed` |

The tool reported a login-shell `/etc/bash_logout: line 4: __ETC_BASHLOGOUT_SOURCED: unbound variable` message after C check command completion; the captured Nix command exit was 0 and all eight outputs were returned and rooted. This did not change the command result.

## Artifacts

- Complete per-command command, CWD, environment, stdout, stderr, exit, and elapsed receipts are retained under this RUN directory.
- Recursive derivation and output graph receipts and GC roots for the four W checks, eight C checks, and profile package are under `roots/` and the corresponding `*-receipt*` files.
- Profile package store path: see `workspace-package-path.txt`; output link: `workspace-package`.
- System generation: `2026-10-22--22-16-53` for `cz.vpsfree/machines/aitherdev`; generation metadata/listing, SHA256, resolved toplevel, and auto-rollback path are retained as `system-generation.json`, `system-generation.sha256`, `generation-list.*`, `system-toplevel.txt`, and `system-rollback.txt`. Toplevel and rollback outputs have roots under `roots/`.
- Ruby receipt failure evidence: `system-build-receipt.command`, `.cwd`, `.env`, `.stderr`, `.exit`, and `.elapsed`. Captured error: `mkConfigDevShell mode 'tools' requires ./Gemfile`; receipt JSON is empty.
- `C-pre-system-source.txt` records C HEAD, tree, status, and flake.lock SHA256 before the system build. The packet's end-of-source comparison was not reached after the receipt failure.

No failure diagnosis or retry was performed. Parent owns acceptance and any next action.
