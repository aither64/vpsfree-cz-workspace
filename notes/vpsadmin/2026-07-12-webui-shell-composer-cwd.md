# WebUI dev shell changes Composer's working directory

Initiative: `work/2026-07-12-vpsadmin-kb-contract/`

Running `nix develop .#webui -c composer install --working-dir=webui` from a
vpsAdmin worktree failed because the WebUI shell hook changed the process
working directory to the per-user Composer directory before executing the
command. The relative `webui` path was therefore resolved outside the
repository.

Pass an absolute worktree path to `--working-dir`, or enter the shell and change
back to the worktree explicitly. The absolute-path invocation installed the
WebUI dependencies and the full 65-test PHPUnit suite then passed.
