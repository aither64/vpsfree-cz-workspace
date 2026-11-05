# Read-only rollout observation 0872

- Bound session identity verified with `dev-session current` and matching `DEV_SESSION_SLUG`/`DEV_SESSION_WORKSPACE` markers.
- Native watcher policy verified as `dw_af6ea530112c2a5e816254d08d217be90f4c5f713a51db96`, danger-full-access / never; watcher model policy Luna/low.
- Observation: operation began at 2026-11-03T23:37:08Z and remains `running` in `operation-status.json` at last read.
- Dry activation: exit 0, 21.38 seconds.
- System switch: exit 0, 39.52 seconds.
- Workspace profile switch: exit 0, 40.63 seconds; command finished with no remaining process group.
- Installed driver: completed with exit 1 after 1076.44 seconds (started 23:40:55Z, ended 23:58:52Z), no remaining process group.
- Terminal evidence: `installed-driver/command.log` reports an AssertionError at test script line 330. The assertion payload showed the fixture session `2026-11-02-service-archive` active, service status unknown/unavailable, team count 1, and two artifacts. No diagnosis or retry was performed.
- Phase status sources: `dry-activate/status.json`, `switch/status.json`, `profile/status.json`, and `installed-driver/status.json`; corresponding `command.log` and `exit-status.txt` files where present.
- Last observed operation status: `state=running`, `phase=installed-driver`; main reconciliation remains pending. No owned process groups remain according to terminal phase status.
