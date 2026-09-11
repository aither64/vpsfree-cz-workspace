# Stable provider dispatch closes SSH stdin

Related initiative: `work/2026-09-11-devcluster-packaging-investigation/`.

On generic runtime bcbaf825, `vpsadminos-devcluster ssh <slug> node1 -- bash -s
< script.sh` exits successfully without executing the script. The host dispatcher
calls `system_env!`, implemented with `Open3.capture3` and no stdin_data, so its
provider subprocess sees EOF. Direct command arguments work. For a noninteractive
script, invoke the stable helper with argv `[..., '--', 'bash', '-c',
Shellwords.escape(script)]` (Python shlex.quote is equivalent); OpenSSH joins those
arguments into a remote shell command. Verified real osctl create/start/stop and
marker checks through this path. The generic runtime is intentionally unchanged
in the packaging repair; forwarding stdin/TTY belongs to a separate runtime fix.
