# vpsAdminOS test-runner socket multicast port collisions

## Symptom

When multiple independent vpsAdminOS test-runner processes run on the same host,
VMs that use the default socket network can accidentally join the same multicast
network. This can make separate suites see each other's traffic or fail in
surprising ways.

## Cause

The default socket network uses multicast address `230.0.0.1:10000`. The
test-runner port reservation logic is process-local, so separate runner
processes do not coordinate the default port.

## Workaround

For suites likely to run concurrently with other local VM tests, define an
explicit socket network multicast port and use it for every machine in that
suite. In `vpsf-status` integration tests, the suite uses port `22131` for the
services, node, and status VMs.

## Verification

During `2026-06-01-vpsf-status-integration-tests`, `ps` output showed the
status-page VMs using `mcast=230.0.0.1:22131` while an unrelated
`vpsfree-irc-bot` suite used `mcast=230.0.0.1:10000`.
