# Host switch result

- Result: passed (exit status 0)
- Config: `e179a58ee3f7ceb4cf0b253d368c8ad94967b2d5`
- Unit: `upload-host-switch-20261004-1.service` — `ActiveState=inactive`, `SubState=dead`, `Result=success`, `ExecMainStatus=0`
- Expected toplevel observed: `/nix/store/ihrndjkq7sh2i6ldl5kh4m6cvbb192di-nixos-system-aitherdev-26.05.20261003.825e202`
- Outer status: `host-switch.exit` contains `0`
- Outer command log: `host-switch.log`; confctl full log: `worktrees/2026-10-04-upload-display-limits/vpsfree-cz-configuration/.confctl/logs/2026-10-04--23-00-00-confctl-deploy.log`
- Evidence: confctl reports activation succeeded; health checks report `SystemState=running`, `firewall.service` active, and 2 checks passed, 0 failed.
- Elapsed observation time: about 1 minute 10 seconds, from first active status observation at 23:00:14 CEST to terminal proof at 23:01:24 CEST.
