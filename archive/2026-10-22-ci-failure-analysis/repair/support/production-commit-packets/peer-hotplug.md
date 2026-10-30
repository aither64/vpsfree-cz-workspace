## Livepatch CPU hotplug diagnostics

Qualification checks kernel health after each hotplug and workload-progress
check, using the example's original dmesg baseline. A warning before the
transition fails that phase even when CPU online/offline and progress checks
succeed. The ordinary workload, aging, ABI, quarantine and recovery requirements
still apply.

The [livepatch test sources](https://github.com/vpsfreecz/vpsadminos/tree/staging/tests/suite/kernel/livepatch-6.12.95)
include the standalone experimental `hotplug-recorder.nix` and its C/BPF sources.
The caller must authenticate its required `vmlinuxHeader` against the original
boot binary. The recorder requires GNU build ID
`7801779436291880089e3407e50e5813f80d76f1`, CPU127 and the locked predicate at
`sched_cpu_dying+0xa4`. Its command-line entry point is `hotplug-recorder --help`.

Runtime attachment, verifier admission and complete recording remain unproven.
Ordinary qualification does not invoke the recorder or orchestrate its first
hotplug capture. A successful source build or help command does not establish
runtime admission or a kernel-fault cause.

