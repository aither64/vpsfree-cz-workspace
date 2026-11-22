# Parallel vpsAdmin capture cluster networking

Initiative: `work/2026-06-15-vpsadmin-events`

## Symptom

Starting the dedicated screenshot topology on the bridge network failed with:

```text
error: 172.16.106.53 responds; stop the existing dev frontend or use --force
```

## Cause

The capture repository and primary vpsAdmin development cluster use the same
default bridge service addresses. The primary cluster was intentionally kept
running for the final deployment, so a second bridge topology would conflict.

## Workaround

Reset the disposable capture slug and start that screenshot-only topology with
local networking. Keep the primary deployment on the bridge network. Do not use
`--force`, because it would hide the address collision rather than isolate the
clusters.

## Verification

Run `bin/devcluster status SLUG` in the capture repository and record that the
topology is `screenshots` and network is `local`. This exception applies only
while the bridge address is occupied by the primary cluster.
