# 2026-08-09-test-vm-kernel-oops

## Goal

Prevent recurring Linux 6.18 module-loader Oopses from being misreported as
unrelated vpsAdmin integration failures. Serialize udev-triggered module
loading in generated NixOS test VMs and make the shared test framework fail
quickly and explicitly when either a NixOS or vpsAdminOS guest reports a fatal
kernel failure. Complete dual-vendor livepatch validation with a dedicated AMD
runner that cannot receive generic self-hosted jobs.

## Affected repositories

- `vpsadminos`: NixOS test-VM kernel parameters, shared osvm console
  detection, test-runner propagation, intentional crashdump allowances,
  lifecycle checksum correction, and runner routing.
- `vpsadmin`: update the locked vpsAdminOS test-framework revision after the
  framework change is merged.
- `vpsadminos-org-configuration`: add the dedicated AMD GitHub runner.
- `vpsfree-cz-configuration`: add its internal DNS record.

## Approach

1. Keep the existing `rd.udev.children_max=1` test-VM parameter and add
   `udev.children_max=1`. Document in the code that Linux 6.18 can race while
   udev workers load modules, that the two parameters cover initrd and normal
   udev processing respectively, and that this is test-only.
2. Parse captured QEMU console output in `OsVm::Machine`, shared by NixOS and
   vpsAdminOS machines. Treat kernel Oopses, kernel BUG/page faults, general
   protection faults, and kernel panics as fatal. Do not treat WARN, KASAN, or
   UBSAN output as automatically fatal.
3. Preserve the first unexpected failure and propagate a dedicated
   `OsVm::KernelFailure` through machine/shell waits and test-runner polling
   boundaries within approximately one second. Drain console output briefly,
   then skip graceful shutdown and kill a failed guest.
4. Provide a scoped `Machine#allow_kernel_failure(pattern) { ... }` API. Use
   it only around the intentional sysrq panic in crashdump tests, constrained
   to the expected panic message.
5. Update vpsAdmin with `tools/update_vpsadminos_flake.sh` after publishing the
   reviewed vpsAdminOS feature revision.
6. Remove the checksum of the current livepatch candidate, whose bytes follow
   the current locked kernel and toolchain inputs. Retain checksums for
   historical predecessors evaluated from immutable vpsAdminOS revisions.
7. Route the lifecycle matrix through the existing `vpsAdminOS runners` group
   with `intel-kvm` and `amd-livepatch` labels. Keep runners 1-3 unchanged.
8. Add `gh-runner4.int.vpsadminos.org` at `172.16.4.31`, configured without
   GitHub's default runner labels and with only `amd-livepatch`, plus its
   internal DNS record. VPS ID 30102 is operational inventory and is not
   represented in the vpsadminos.org configuration module.

## Compatibility and deployment

- No NixOS kernel patch, kernel-package change, database change, API change,
  persistent format change, or production deployment is involved.
- `udev.children_max=1` serializes all normal udev processing in generated
  NixOS test VMs. Boot and hotplug handling may be slightly slower and udev
  concurrency is intentionally reduced to avoid the observed Linux 6.18 race.
- New test-framework consumers fail on genuine guest kernel failures instead
  of timing out later. Existing intentional crash tests use a scoped allowance.
- Livepatch modules are loaded into a QEMU guest. Ordinary livepatch faults are
  expected to affect only that guest, but host KVM/SVM bugs remain a residual
  risk because the production runner exposes `/dev/kvm`.
- Runner4 has no `self-hosted`, OS, or architecture default labels, so generic
  jobs continue to use runners 1-3. Pull-request use of the explicit
  `amd-livepatch` label remains allowed by user decision.
- The runner and DNS changes are additive. Rollback removes or disables
  runner4 and its DNS record; unmatched AMD jobs then remain queued.
- Mixed versions are safe: consumers pinned to the old test framework retain
  old behavior, while updated consumers receive detection and serialization.
- Rollback consists only of reverting the framework/input commits. No state
  conversion or coordinated machine update is required.

## Testing plan

- Focused and full osvm/test-runner RSpec suites for fragmented console input,
  fatal signature matching, ignored warnings, first-failure retention, scoped
  allowances, polling propagation, and failed-guest teardown.
- Evaluate generated NixOS configuration and confirm both udev parameters.
- Run repository Overcommit hooks before every commit.
- Run the mandatory standalone change review after quick verification and
  commits, before long VM integration tests.
- Target vpsAdminOS crashdump and module-autoload integration tests.
- Update the vpsAdmin lock and run `services-up`, covering a NixOS services VM
  and a vpsAdminOS node with the updated shared framework.
- Push both feature branches, inspect GitHub Actions and artifacts, and cancel
  only superseded runs whose SHA no longer matches the branch head.
- Validate workflow syntax, the internal DNS zone, and the evaluated runner4
  configuration. Before activation, verify the VPS exposes an AMD CPU with
  `svm`, `npt`, `nrip_save`, and a usable `/dev/kvm`.
- Run both Intel and AMD lifecycle jobs. Confirm generic jobs remain on runners
  1-3, AMD runs only on runner4, QEMU is cleaned up, and the host node reports
  no KVM/SVM fault after the first run.
