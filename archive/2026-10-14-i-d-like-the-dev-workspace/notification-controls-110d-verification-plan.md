# Exact110d verification plan — prepared only

Source110d1f71a6fd8671cc9316f509d61ed56cf740b3, tree2faf1a5400edf16a06708d2095f17561613c9114.
Run only after final affected fixture review is accepted and source gate bound.
Fresh Luna/low utility owns one related batch:
1. bash run-notification-controls-110d-browser.sh (both engines; stop on failure).
2. Only on browser PASS, bash run-notification-controls-110d-flake.sh.
3. Observe exact-head CI after SSH publication, collecting status/failure evidence
   without retry. Prior6c CI is historical successful fast/host-skipped evidence.

No source edits/retries/provider/native/host or deployment by watcher. Existing
fixture privacy and finite deadlines remain. Preserve full new logs and statuses;
no inherited preload or diagnostic environment. Kernel compilation unexpectedly
starting requires stopping only the owned local check and reporting evidence.
No generic timeout for quiet fullflake. Main owns diagnosis, consumer pins,
composition review and later preparation/activation. Browser options/click plumbing
does not certify physical OS sound suppression or Firefox/macOS focus.

Original6c and diagnostic failures remain sealed and version-bounded; passing
corrected fixture will not retroactively explain the original unlocated run.
