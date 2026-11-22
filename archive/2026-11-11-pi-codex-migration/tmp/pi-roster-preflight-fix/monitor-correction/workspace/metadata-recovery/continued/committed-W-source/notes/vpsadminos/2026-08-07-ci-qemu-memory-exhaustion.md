# CI QEMUs can be killed when stable scheduling fills runner memory

Related initiative: `work/2026-08-07-vpsadminos-test-failures`

## Symptom

Several unrelated vpsAdminOS tests fail together with
`OsVm::MachineShellClosed`. Machine lifecycle logs show `qemu_exit` with an
empty `STATUS`, guest consoles stop without a panic or clean shutdown, and
cleanup may add `Process.kill: no implicit conversion from nil to integer`.

## Cause

An empty OSVM QEMU exit status means the child was terminated by a signal. In
run 31210461594, QEMUs disappeared in synchronized groups while the test-runner
had reserved its full 92 GiB pool on a 96 GiB, swapless runner.

The scheduler's stable capacity uses total assigned memory minus the default
4 GiB reserve. It does not subtract existing memory use or account separately
for Nix evaluation/build and QEMU/virtiofsd overhead. QEMU RAM is backed by
`/dev/shm`. Historical metrics showed about 5.8 GiB shared memory before the
VMs, 85.8 GiB immediately before the first kills, and a 93.8 GiB peak with only
1.2 GiB available.

## Diagnosis

1. Download the full test artifact and compare all `*-log.log` machine
   lifecycle timestamps, not just the reported failures.
2. An empty `STATUS` under `ACTION: qemu_exit` indicates a signaled process;
   normal guest shutdown records status 0.
3. Check the test-runner's initial `Resource limits` and `Reserved resources`
   lines.
4. Correlate QEMU exits with `node_memory_Shmem_bytes`,
   `node_memory_MemAvailable_bytes`, total memory, and swap metrics.
5. Compare identical-head runs on other runners before attributing unrelated
   test failures to the source commit.

## Mitigation

Configure enough memory reserve or a lower scheduling cap for the runner's
real non-VM peak. Improve OSVM diagnostics to record `Process::Status#termsig`
and tolerate cleanup after the reaper has cleared `qemu_pid`.
