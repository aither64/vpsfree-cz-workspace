Result: failed, exit status 1.

Operation: user unit `upload-profile-switch-20261004-1.service`.
Expected source workspace: `88c0b957a1e870e4ce36a1743f72b529ba4825e1`.
Expected candidate: `/nix/store/jq982nq0jxfhmr4jxyvkglnyy77n1kxf-dev-workspace-0.2.0`.

Completion evidence: `profile-switch.exit` contains `1`; `systemctl --user show` reports `ActiveState=failed`, `SubState=failed`, `Result=exit-code`, `ExecMainStatus=1`.

Phase: `refused; requires coordinator diagnosis`.
Log excerpt: `2026-10-04T23:02:07+02:00 workspace-portal: inspect archived member architect0: archive proof requires a retained thread, canonical directory and Codex home`.

Elapsed time: unavailable from the supplied status files.
