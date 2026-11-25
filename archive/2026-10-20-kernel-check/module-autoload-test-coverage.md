# Module autoload: existing coverage at merged 846bb

Read-only inventory at `846bb469505789ba0b2a405fa5905ba6d8253006`, under
[the investigation brief](design.md#module-autoload-compatibility-investigation-brief).
No tests, evaluation, builds, remote queries, Git or host changes were run.

Existing tests provide real autoload behavior coverage for both enable settings
with logging enabled, including direct activation. They do not explicitly
compose the new sysctl service's completion/restart with policy-changing
switches, silent modes or conflicting key inputs.

## Assertions and evidence

Source references are to the exact merged OS revision above.

| Contract | Existing assertions | Limit |
| --- | --- | --- |
| Boot, disabled/enabled with logging | `tests/suite/kernel/module-autoload.nix:4-27,247-256`: two VMs, `enable=false/true`, inherited default `log=true`; read nonempty, distinct executable helper paths. | No `log=false` VM. No explicit wait for `/service/sysctl/check` before the autoload assertions. |
| Direct activation | Same file `:259-267`: run `/run/current-system/activate` on both and assert helper paths unchanged. | This does not invoke the switch/test service phase or explicitly replay sysctl. |
| Wrapper function and logging | `:270-284`: invoke the selected wrapper with `bonding`; disabled fails without loading, enabled loads; assert matching deny/load syslog message. | Direct helper invocation, distinct from a kernel-triggered autoload request. |
| Actual trigger outcomes | `:183-229,305-311` with helper assertions `:86-111`: dummy link, netem qdisc, xt_recent, nft limit, AF_ALG AEAD. Each target module is absent before probing. Disabled command fails with no newly loaded modules; enabled command succeeds and its module appears. | Meaningful behavioral evidence, beyond path equality. Blocked cases do not separately assert a fresh per-trigger wrapper log/argument; error status alone would be weaker without the matched enabled controls and module checks. |
| Explicit load distinction | `:287-293`: explicit host `modprobe bonding` works in both VMs and unloads cleanly. | Does not test automatic loading. |
| Runtime admin override | `:315-323`: manually point disabled VM's `kernel.modprobe` at plain modprobe, repeat real dummy trigger successfully, clear the path, then verify trigger blocked. | No following activate, switch, service restart or completion check. |
| Generic service lifecycle | `tests/suite/system/sysctl.nix:115-221`: waits direct completion; boot repeat; changed switch/test; stale identity; unchanged-input override retention; extra target files and `/etc/sysctl.conf` precedence; null/removal; failures/no retry and explicit retries. | Assertions use `kernel.printk_ratelimit` and `vm.vfs_cache_pressure`, not `kernel.modprobe`, and leave module-autoload policy unchanged. |

Both tests are registered and tagged CI: `tests/all-tests.nix:260,316`.
Other nearby tests do not fill the interaction gap:
`system/boot/stage-2.nix:30-32,67-70` rejects console modprobe errors;
`system/switch-to-configuration.nix:230-305` checks explicit `kernel-modules`
load/unload/reload behavior, not the kernel's autoload helper policy.

No test/fixture references `logModuleLoading` by that spelling, and no test
sets `boot.kernel.moduleAutoload.log` or explicitly overrides/nulls
`boot.kernel.sysctl."kernel.modprobe"`. Option spelling/meaning is part of
implementer1's source lane; absence here is a coverage result.

## Executed results, not new execution

Saved exact-head CI `39767770407`, product job `119793311317`, native root:
`generic-sysctl-ci-39767770407-600s-failure-119793311317/artifacts/`
`os-test-logs-39767770407-1-native/`.

- `os-test-kernel__module-autoload-c6f165d1/test-result.txt` is
  `expected_success`. `test-runner.log:3-34` records all 16 examples succeeding,
  16:04:11–16:05:58 CEST; script finishes at 16:06:03 in 182.24 seconds.
  Actual helper/path reads, direct activation and requests are preserved in
  `autoload_disabled-shell.log` and `autoload_enabled-shell.log`.
  Disabled helper is `/nix/store/bcx5jqj8lrm9bvjgw3x3a5ih5fa2vw63-kernel-modprobe-wrapper`;
  enabled helper is `/nix/store/30nfxa5z6vxz3wzzs2wl0jvv0w7j6hyy-kernel-modprobe-wrapper`.
- `os-test-system__sysctl-8ae7035e/test-result.txt` is `expected_success`;
  its `test-runner.log` records all eight examples succeeding, 15:26:23–15:27:27,
  script time 82.02 seconds. The separate accepted focused native run also
  passed eight examples; exact binding is in
  [the existing verification packet](generic-sysctl-verification.md#verification-status).

Those receipts establish the listed assertions ran successfully on the merged
source. They do not establish absent cases. Console `kernel.modprobe = ...`
output is early boot application, not proof of the later service replay.

## Smallest useful extensions, proposed only

Reuse the existing module-autoload fixture, its absent-module guard and one
real dummy-link trigger; do not duplicate all five trigger families.

1. Explicitly await a fresh completed sysctl attempt at boot and after an
   explicit same-input service restart, then read `kernel.modprobe` and repeat
   the matched deny/allow trigger. Observe the fresh attempt before down/check;
   do not infer application from switch exit or initial supervisor down.
2. Add a compact switch/test sequence through the four enable/log combinations,
   including return from a permissive mode to disabled. Check path/empty value,
   completed replay where scheduled, real trigger outcome and logging behavior.
   This covers addition/removal of the generated key and a policy-changing
   switch without requiring all existing probes for every mode.
3. Add focused explicit-key cases after the source owner fixes their intended
   expectations: a strong override; a forced null; and a later managed file
   overriding the generated key. Include a subsequent otherwise unchanged
   `test` after manual drift. Source owner confirms activation always rewrites
   `kernel.modprobe`, even if unchanged service inputs skip replay, so the
   existing printk override-retention expectation must not be copied here.

The first two items close the direct disabled-autoload preservation concern.
The third documents the separate precedence/activation contract; it must not
promise that null restores a value or that explicit conflicting inputs preserve
the declared autoload policy. These are proposals, not authorization to edit or
run tests. No new regression or unconditional compatibility verdict follows
from test absence alone; architect combines this inventory with source ordering.
