# Dev-cluster graceful stop can time out

Initiative: `work/2026-07-13-security-advisory-automation`

## Symptom

`devcluster stop 2026-07-13-security-advisory-automation` waited for the normal
120-second shutdown window, then reported that the runner was killed after a
timeout. The runner log identified a graceful-stop timeout for the services
VM.

## Behavior and workaround

This is the tool's built-in fallback, not `devcluster reset`: it terminates the
runner, cleans socket processes, and removes the generated GC root while
leaving the cluster state directory and disk images intact. A subsequent
`devcluster start <slug> --topology single --network bridge` reused the disks,
rebuilt the GC root, and reached ready state.

Do not delete the state directory or use `reset` when the goal is to preserve
the database and VM disks across a reboot test.

## Verification

The restarted bridge-network cluster reached ready state. Its Node booted the
new kernel-evidence closure, nodectld published a complete schema-v2 report,
and the WebUI and API returned HTTP 200 using the dev-cluster CA.
