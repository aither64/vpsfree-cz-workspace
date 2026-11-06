# Verification batch 3 — parent monitoring fallback

Source `9738dfbc66bd06b75670d8efd93c684a174acbee`, clean source and unchanged
lock SHA256 checked before execution. Documented fallback used after the fresh
standalone utility ended incomplete without running any command. Root retained
cancellable handle67515 and exact Nix PID/status; no other watcher polled logs.

Command1 `nix build --no-link -L .#checks.x86_64-linux.mx2` failed, exit1 after
102.34 seconds. Commands2-6 did not run.
Full evidence: `verification-3-vm.log`, `verification-3-status.json`.

Native type/lint/build preparation succeeded; all three VMs booted. Runtime
subtests completed before failure:

- Isolated DNS, effective policy and enabled SMTP firewall.
- Relay denial independent of greylisting/no queued DATA (both address families).
- Fresh Postgrey tuple, retry and policy-state service restart persistence.

DNSBL case then failed before SMTP: dedicated source192.168.1.11 could not bind,
OSError99 Cannot assign requested address. This is a fixture address-plumbing
failure; it does not establish DNSBL rejection or later delivery/queue behavior.
Implementer0 owns diagnosis and minimal correction, preserving intended DNSBL
assertions and all production/security/isolation policy. No blind retry.

Native cleanup log records all three QemuMachine processes terminated and cleanup
finished0.48s. Nix/parent handle exited1; status running=null. No owned VM/process,
cancellation or production effect. No new expected-output success claim.
