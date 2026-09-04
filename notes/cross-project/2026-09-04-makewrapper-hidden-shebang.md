# Patch shebangs before makeWrapper hides executables

Initiative: `work/2026-09-03-dev-session-portal/`

## Symptom

A packaged helper worked in development and its visible wrapper had a Nix
store Bash shebang, but NixOS activation failed with `env: bash: No such file or
directory` under its deliberately minimal `PATH`.

## Cause

`wrapProgram` moves the original executable to a hidden `.<name>-wrapped`
file. The standard shebang patching pass did not patch that hidden file, so its
portable `#!/usr/bin/env bash` or `#!/usr/bin/env ruby` shebang survived. The
visible wrapper adjusted `PATH`, but it did not include Bash for this helper.

## Fix and verification

Patch each installed helper's shebang before calling `wrapProgram`. Add an
install-time assertion that every hidden wrapped executable has a direct Nix
store interpreter, and exercise representative installed entry points with an
empty ambient `PATH` when practical.

Inspect the final installed output, not only source files or check-phase test
entry points. Tests run before wrapping do not cover this failure mode.
