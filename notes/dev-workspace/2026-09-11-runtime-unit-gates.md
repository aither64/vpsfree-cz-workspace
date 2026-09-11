# Runtime systemd masks do not override persistent unit definitions

During the `2026-09-09-workspace-components` aitherdev cutover, a runtime mask
under `/run/systemd/system` did not reliably gate certificate renewal when the
same unit had a persistent definition under `/etc/systemd/system`; persistent
unit lookup precedence won.

For a temporary cutover gate, install a drop-in under
`/run/systemd/system/<unit>.d/` with `ConditionPathExists=` tied to an absent
admission flag, reload systemd, and stop the timer and service. On acceptance,
remove only those exact drop-ins, reload, start the timer, and verify it is
active. The same condition-drop-in pattern worked for the user router, but its
socket needed a short readiness wait after `systemctl start`.

Related initiative: `work/2026-09-09-workspace-components/`.
