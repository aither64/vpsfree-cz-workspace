# Test helpers in Nix build sandboxes

## Symptom

A Ruby test-generated executable passed locally but failed in a Nix package
`checkPhase` with `Errno::ENOENT`, even though the helper file existed and was
executable.

## Cause

The helper used `#!/usr/bin/env ruby`. Nix build sandboxes do not provide the
ambient `/usr/bin/env` path, so the kernel reported the script itself as
unavailable.

## Workaround and verification

When a test already knows the Ruby interpreter, invoke the generated script as
`[RbConfig.ruby, script]`. Reserve shebang execution for helpers whose
interpreter path is supplied from the Nix closure. The workspace portal package
build exposed this in `test_stop_quiesces_terminal_before_the_authoritative_idle_check`.

Related initiative: `work/2026-09-03-dev-session-portal/`.
