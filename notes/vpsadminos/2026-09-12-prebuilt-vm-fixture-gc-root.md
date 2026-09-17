# Root prebuilt VM test fixtures before running them

A scratch TestEvaluator harness overrode TestConfig.build with a JSON fixture
built using `nix-build --no-out-link`. The fixture and helper program disappeared
during the run when Nix garbage collection reclaimed unrooted outputs. Twenty
NFS examples passed, then the next push_file failed before executing a guest
command; the JSON fixture and original Nix helper paths were absent afterward.

Prefer the standard test runner, whose configuration output link retains the
fixture. A custom prebuilt harness must create an indirect GC root with
`nix-store --add-root STATE/config.json --indirect --realise STORE_JSON` before
reading the configuration. Build the initial fixture with an output link too.
Merely loading JSON or booting QEMU does not retain all source programs needed
by later test examples.

Root cached prerequisites before a dry run when planning to reuse them. Another
attempt found the old kernel available and a dry run showed no kernel build;
GC removed required outputs before the actual build registered its dependencies,
causing an old kernel rebuild to be scheduled. Separate outputs such as `dev`
need their own retention when the kernel's runtime closure does not refer to
them. Stop an unexpected superseded-kernel rebuild instead of accepting the
preflight result as a guarantee that outputs remain available.

Related initiative: `work/2026-09-12-nfs-cancellation`, early external-ZFS run
at `/tmp/nfs95-external.aTwdvj`. Retain its twenty passing examples as partial
evidence; do not count the interrupted suite as a pass.
