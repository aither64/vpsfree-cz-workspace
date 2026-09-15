# Pause NixOS services across package activation with a start condition

A NixOS unit under `/etc/systemd/system` outranks a runtime mask under
`/run/systemd/system`. `systemctl mask --runtime` can succeed while the unit
remains startable. The kernel-history rollout review reproduced this with an
isolated systemctl root fixture and verified the exact built API1 unit layout.

For a short maintenance window, use a uniquely named runtime unit drop-in with
`[Unit] ConditionPathExists=!/run/TASK-paused` and create that marker. Reload the
manager and stop the service. Before probing start, verify marker existence,
exact drop-in content, loaded DropInPaths, and the effective Conditions tuple.
Then require inactive and ConditionResult=no after a start request. A skipped
start can return success. Repeat the checks after each package activation.

A harmless local user-unit test proved the condition remains effective after
base-unit replacement and daemon-reload. Inspection of the pinned NixOS
activation code confirms it replaces `/etc` and uses normal manager jobs while
preserving this `/run` drop-in. The guard lasts only until host reboot. Remove
only the task drop-in and marker, reload, and start once packages/schema are
ready. This was tested with fixtures, not by pausing a production service.

Systemd 260.2 prints Conditions as `[unprintable]` through `systemctl show`.
`busctl --json=short get-property org.freedesktop.systemd1 UNIT_OBJECT_PATH
org.freedesktop.systemd1.Unit Conditions` returns the effective condition tuples.
Check the name, trigger=false, negate=true and exact path; use ConditionResult
for the observed start result instead of the tuple's evaluation integer.

Related initiative: `work/2026-09-14-kernel-history-fix/rollout.md` and
`recovery-pin-review-general.md`.
