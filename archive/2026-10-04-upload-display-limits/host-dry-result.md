Result: failed (exit 90)

- Unit: `upload-host-dry-20261004-1.service`
- Tested config head: `e179a58ee3f7ceb4cf0b253d368c8ad94967b2d5`
- Elapsed: under one second (systemd start and exit timestamps both 2026-10-04 22:53:24 CEST)
- Status file: `host-dry-activate.exit` contains `90`.
- systemd: `ActiveState=failed`, `SubState=failed`, `Result=exit-code`, `ExecMainStatus=90`.
- Log: `host-dry-activate.sh: line 10: git: command not found`
- Full log: `host-dry-activate.log`
