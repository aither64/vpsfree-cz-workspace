# Run vpsAdmin hooks and commits inside the Nix shell

Related initiative: `work/2026-06-15-vpsadmin-events`

## Symptom

Running `git commit` directly from the ambient shell invoked the installed
Overcommit hook, but RuboCop, PHP CS Fixer, gettext tools, and MariaDB were not
available. The hook correctly rejected the commit.

Running `nix develop .#webui -c webui/lang/scripts/locales-update` from the
repository root also failed because the WebUI shell changes its working
directory to `webui/`, producing a duplicated `webui/webui/` path.

## Workflow

- Run the complete hook suite as `nix develop -c overcommit --run`.
- Run the final `git commit` through `nix develop -c git commit ...` so the
  installed hook sees the same toolchain.
- Invoke WebUI locale scripts relative to the shell's working directory, for
  example `nix develop .#webui -c lang/scripts/locales-update`.

The repeated hook suite and commit-time hook both passed with this workflow.
