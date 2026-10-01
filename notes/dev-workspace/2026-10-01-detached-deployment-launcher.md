# Detached deployment launchers from command tools

A deployment shell started with `nohup ... &` from a command tool can disappear
when the parent command returns, before its script writes a log or status file.
The failed attempt in
`work/2026-09-30-portal-review-improvements` left the selected profile and portal
PID unchanged. This indicates that the command runner cleaned up the detached
child; the exact mechanism was not independently proven.

For an authorized operation that must outlive the launching command, use a
named transient user service with `systemd-run --user`. Have its script write an
atomic status file and keep its complete log separately. Assign a fresh
verification watcher to observe that existing unit and status file. The same
profile switch then completed with exit status 0, and `systemctl --user show`
reported `Result=success` and `ExecMainStatus=0`.

Do not treat a missing status file as a failed or successful deployment. Check
the authoritative selected profile, service state and process list before
deciding whether a retry is safe.
