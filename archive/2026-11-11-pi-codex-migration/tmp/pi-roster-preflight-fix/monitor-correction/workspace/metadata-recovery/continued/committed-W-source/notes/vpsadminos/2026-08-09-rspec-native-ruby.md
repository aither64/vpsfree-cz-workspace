# vpsAdminOS osvm and test-runner RSpec native extension

## Symptom

Running osvm and test-runner specs together can load the wrong `spec_helper`.
Building `libosctl/native.so` in the generic `.#osvm` shell then fails at load
time with an undefined `rb_thread_start_timer_thread` symbol. Rebuilding that
shared file while another suite is running can also make the other Ruby process
exit with status 139 after otherwise passing examples.

## Cause

The two suites have separate helpers and Gemfiles. `libosctl` deliberately uses
timer-thread symbols exported by the patched vpsAdminOS Ruby, so its native
extension must be built with that Ruby. The extension path is shared by both
suites within a worktree.

## Workflow

Build `libosctl/ext/libosctl` once inside `nix develop .#vpsadminos`, copy
`native.so` to `libosctl/lib/libosctl/native.so`, and then run osvm and
test-runner specs sequentially with their respective Gemfiles. Do not rebuild
the shared extension concurrently with either suite.

This was verified in `work/2026-08-09-test-vm-kernel-oops`: the focused osvm
suite passed 47 examples and the focused test-runner suite passed 18 examples.
