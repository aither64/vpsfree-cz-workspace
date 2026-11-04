# Final source selector discovery

- Result: failed (both listing commands exited 1 during selector metadata evaluation).
- Session: `2026-11-03-opensuse-leap-image-build`; environment markers matched the bound workspace.
- Source: `/nix/store/m1n49nc1qdf1f3j298zcmjjb5ni43iag-source`, Git head `742eb30cb1a8b6766c85e915d26b0400e38244b1`, tree `19f423e70ff439867d4bb27e8ed07b9c95fdb703`.
- Configuration: `final-verification-742eb30cb.nix` (8 GiB sizing module importing `final-revision-742eb30cb.nix`); source module hashes are listed below.
- Expected first selector: `image-scripts/test@opensuse-{leap-15.6,leap-16.0,leap-16.1,tumbleweed}`. It produced no selected names, so the expected four cases were not confirmed.
- Second selector: `systemd/device-units#opensuse-*`. It produced no selected names, so existing selectors were not confirmed.
- Both failed with the same Nix evaluation conflict: `boot.qemu.memory` has definitions `4096` and `8192`, at metadata evaluation of `kernel/namespaces` resource sizes.
- Elapsed time: approximately 80 seconds including both sequential selector evaluations.
- Complete stdout/stderr and per-command exit statuses: `final-discovery.log` (`listing1=1`, `listing2=1`).
- Running effects: both selector processes completed. The runner realized `/nix/store/i17am2nvd2ih3slwj5nv6gyr38yi1n6s-test-runner-repository-source.drv`; no VM, test, or kernel build was started.
- No retries or source/config/input edits were made.
