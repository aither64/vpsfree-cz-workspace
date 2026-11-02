# Native NixOS test reboot mode

The pinned test driver's generic `start_all()` starts QEMU machines with
`allow_reboot=False`, adding `-no-reboot`. Calling `machine.reboot()` can then
perform a normal guest shutdown/reset while QEMU exits; the next control-shell
connection fails with `RuntimeError: Shell disconnected` before persistence can
be inspected.

Start the machine that must reboot with `machine.start(allow_reboot=True)` before
`start_all()`. The documented start operation is a no-op for an already started
machine. Keep the normal reboot API and same disk, then verify queue/content/state
after reconnecting. Do not hide the disconnect or replace persistence assertions.

Evidence: [mx2 runtime verification](../../work/2026-11-01-mx2-nixos-migration/state.md),
batch4 log and native-reboot remediation. This concerns the isolated test runner;
it does not change production startup or mail policy.
