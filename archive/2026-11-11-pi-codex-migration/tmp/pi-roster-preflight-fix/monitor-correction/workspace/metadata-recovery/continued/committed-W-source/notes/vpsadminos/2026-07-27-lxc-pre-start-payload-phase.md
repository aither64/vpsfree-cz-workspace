# LXC payload cgroups do not exist at pre-start

Related initiative: `work/2026-07-24-ct-start-hang/`

## Symptom

A container with cgroup-v2 memory limits failed in `CtPreStart` while writing
`runs/<generation>/user-owned/payload/memory.max`.

## Cause

LXC runs `lxc.hook.pre-start` before initializing its cgroup driver and creating
the configured `payload` and `payload/inner` cgroups. A durable lifecycle run
can therefore be active and preparing while its LXC-owned payload hierarchy
does not yet exist.

## Design rule

During pre-start, apply ordinary limits to the stable osctld-owned container
root. CPU bandwidth and cpuset have explicit generation-aware policy
transactions. Mirror ordinary parameters to the LXC payload only after the
container has published the running state.

Dynamic updates to a running container may update both the stable root and the
existing payload. Do not use lifecycle-run existence as a substitute for
payload existence.

Verification for this instance is recorded in the initiative state.
