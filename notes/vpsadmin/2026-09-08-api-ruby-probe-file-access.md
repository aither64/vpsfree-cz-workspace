# Deployed API Ruby probes need service-user file access

`devcluster ssh ... services -- bash -s` runs as root, but
`vpsadmin-api-ruby SCRIPT` starts a transient systemd unit as `vpsadmin-api`.
A root-owned `mktemp` file at mode 0600 therefore fails with `LoadError:
cannot load such file`, even though the file exists and SSH can read it.

Keep the prepared script private to the intended runner: change its group to
`vpsadmin-api`, set mode 0640, run the wrapper, and remove the script with an
EXIT trap. Start Ruby probes with `require 'vpsadmin'`. Capture sensitive
results in process memory rather than tool output. This procedure successfully
read sanitized acceptance-fixture metadata from the running cluster.

Related initiative: `work/2026-08-18-vpsadmin-password-reset/`.
