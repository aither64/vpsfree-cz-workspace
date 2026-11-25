# Generic sysctl application: existing runit contract

Proposal evidence only, at clean OS head
`14cdf1caec606bb6bc88fcb32ac48f707f5dabb0`. No code, evaluation, build, CI,
Git/ref mutation or runtime operation was performed. This checks current source,
not historical pins. Architect0 owns the resulting design.

**A runit one-shot can schedule application after a changed configuration, but
its default wrapper does not supply reliable per-configuration success or switch
failure propagation.** A service is optional if the required behavior is simply
a synchronous generic apply during `switch`/`test`.

## Concrete service contract

Existing `runit.services.<name>` fields in
`os/modules/system/boot/runit/default.nix` are `run`, `oneShot`, `check`, `path`,
`runlevels`, `restartTriggers`, `onChange`, and `log.enable`/`logStandardError`.
Runlevels default to `[ "default" ]` (12–15); `oneShot` defaults false (54–61);
`onChange` defaults `"restart"` (87–106). No new service framework is necessary.

A trigger on `config.environment.etc."sysctl.d/60-nixos.conf".source` detects
changes to generated `boot.kernel.sysctl` settings. The service manifest exports
flattened trigger strings (`activation/top-level.nix:13–20`). The switch compares
resolved run paths and triggers; changed triggers force restart even for
`onChange = "ignore"` (`switch-to-configuration.rb:186–203,293–318`). This trigger
does not cover unrelated local files or every other input to `sysctl --system`.

`switch` calls `test`. Both use this order (`switch-to-configuration.rb:75–114`):
probe old/new services; stop removed/changed services; execute the new activation
program; switch runlevel; reload and start changed services. The new `/etc` is
therefore installed before the explicit changed-service start. New services
are started asynchronously by runsvdir after their links appear; the real
`test` path does not explicitly call `Services.start` (compare dry-run 60–61
with real 112–114). Service selection is restricted to the chosen runlevel
(353–365), and the protected-service list can skip a restart (206–218).

## Completion and failure pitfalls

- The wrapper inserts `service.run`, then prints success, creates
  `/run/service/<name>/done` and sends `sv once` (runit module 283–298).
  It has no automatic `set -e` or guard on the run body's last status. A plain
  failing sysctl command can therefore fall through to the success footer.
  The service body must explicitly exit on failure. Conversely, `exec sysctl`
  would bypass the success footer even on success.
- The default check only tests whether `done` exists (301–313). No default
  start/stop path clears the previous marker or ties it to current input.
  Clearing it only inside `run` also leaves a possible check-before-clear race.
  A small custom check that recognizes success for the desired configuration,
  with its marker written only after successful application, is needed if
  current-generation completion is promised. A generic old `done` is insufficient.
- Cached runit 2.3.1 `sv(8)` defines `start` as `up`, waiting normally seven
  seconds and consulting `./check`; `once` disables restart after exit.
  `runsv(8)` restarts a normally-up service after run/finish exit, delaying
  immediate failures by one second. Thus explicit failure before the success
  footer permits automatic, unbounded retries. A permanent unsupported setting
  could repeatedly reapply other settings and log errors. That retry policy
  must be deliberate; sysctl application is not an atomic transaction.
- `log.enable = true` captures output/stderr using the existing service log.
  Custom checks/status can expose failure, but `switch-to-configuration.rb`
  ignores the boolean result of both `activate` (117–121) and service commands
  (206–231). A timeout can be printed without a failing overall switch exit.
  This remains true even after fixing markers. Runtime success must not be
  inferred solely from the current switch command's exit status.

The local runit overlay changes only `runit.c`, `runit.h` and `runsvdir.c`
(`os/overlays/packages.nix:50–55` and its two patches), not these sv/runsv
contracts. No supervisor was launched to test this proposal.

## Preserve boot ordering and choose the smallest path

Keep the existing `config/runit.nix:19–26` application after kernel-module
loading and before loopback/network setup. A new default-runlevel service is
later and cannot replace that early boot step. If it also runs on every boot,
it duplicates the apply, potentially after other services have begun changing
runtime state. Covering rescue/single/custom runlevels is a separate scope
decision; the default service list alone does not cover them.

A generic activation snippet avoids service markers, supervisor timing and
retries, but also runs during boot: `stage-2-init.sh:65–81` calls activation
before starting runit and its stage 1. An ungated hook would reorder/duplicate
boot application before module loading. It needs a runtime-only distinction;
it also runs on every activation unless change detection is added, and its
failure still needs propagation through the switch caller.

If the requirement is simply synchronous apply on `switch`/`test`, preserving
stage 1 and adding a checked generic apply in the existing runtime switch path
after successful activation is the smallest state model. It naturally avoids
the boot ordering problem. Whether to replay on every switch or only changed
generated configuration must be specified. Prefer the service only if its
separate status/retry/changed-input behavior is required and the above pitfalls
are accepted or addressed. Neither approach resets a live value merely because
its declaration was removed. No solution is implemented by this report.

Existing source fixtures: `tests/suite/system/switch-to-configuration.nix:188`
tests trigger-only restart selection; `system/activation/switch_to_configuration_spec.rb`
tests trigger precedence. Neither demonstrates sysctl application, fresh
one-shot markers or propagated failure. A later implementation needs focused
verification of those selected contracts, not a kernel build or fault test.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/>
