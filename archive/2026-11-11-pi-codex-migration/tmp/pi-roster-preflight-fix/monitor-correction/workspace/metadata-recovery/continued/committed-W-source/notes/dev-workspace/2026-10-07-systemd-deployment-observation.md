# Deployment completion survives a disconnected launch client

A named transient user service with systemd-run and Type=oneshot ran aitherdev host
activation followed by the workspace profile switch. The launch client reported
"D-Bus connection terminated while waiting for jobs" and returned nonzero during
activation. The independent named unit continued and completed all stages.

Atomic per-stage/overall status files contained 0. The matching systemd invocation
journal recorded JOB_RESULT=done, and installed package/service/live checks passed.
A client transport failure alone did not justify a deployment retry. See
work/2026-10-07-lead-review-defaults/rollout.md and its observation metadata.

systemd-run --help documents --no-block as not waiting for the operation to finish.
Future launchers can use it with independent status and journal proof. This option
was not used for this successful operation. Preserve owned invocation identity
and logs; never equate a missing status with completion.
