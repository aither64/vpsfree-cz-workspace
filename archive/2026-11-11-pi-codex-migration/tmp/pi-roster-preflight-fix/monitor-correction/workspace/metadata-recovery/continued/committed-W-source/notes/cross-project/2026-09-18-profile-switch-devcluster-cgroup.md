# Workspace profile switches can terminate development clusters

## Observation

During the `2026-09-18-codex-0-155-update` profile switch, systemd stopped
`workspace-codex@vpsfree-cz.service` to replace Codex 0.154.0 with 0.155.0.
The service cgroup contained an unrelated long-running vpsAdmin development
cluster runner, its virtiofsd helpers and QEMU guests. Systemd killed those
children while stopping the App Server service.

The switch had quiesced terminal Codex clients and restored them after the App
Server restart, but it did not restore the development-cluster processes.

## Follow-up

Before future workspace profile switches coexist with active development
clusters, determine whether their runners must be moved out of the App Server
service cgroup or explicitly stopped and recovered by the transition workflow.
Do not recreate or reset another initiative's cluster solely because a profile
switch terminated it.

Related initiative: `work/2026-09-18-codex-0-155-update/`.
