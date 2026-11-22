# Measure elapsed time inside long-check observation

During the container-image pipeline smoke, a verification utility announced
15- and 30-minute milestones within roughly six minutes of the registered
driver launch. The authoritative UTC launch/exit timestamps contradicted those
labels. The test itself had no exit receipt at the first report; the utility's
claimed elapsed time was not evidence of failure or permission to cancel it.

Use actual UTC and time.monotonic in one observation process when a deadline or
reassessment matters. Do not infer elapsed time from the number of tool waits.
Keep the driver's atomic numeric exit receipt separate from the monitor's prose.
A driver receipt of 1 means a failed completed test even if the utility calls it
incomplete. An observer startup error is a separate result and cannot classify
the test. Redirect logs and capture status in the original observer invocation;
retain its tool handle rather than launching it again to add log capture.

The follow-up observation read the existing receipt without relaunching anything
and recorded UTC/monotonic values. In that run, source/assignment receipts also
showed the guests had progressed beyond an earlier BIOS-only snapshot. Preserve
timestamps and phase-specific evidence instead of treating an old snapshot as
the terminal cause.

Evidence: work/2026-11-04-container-image-build-pipeline/state.md and
artifacts/p3-boot-continuation.log. No session or service lifecycle action was
needed to repair observation.
