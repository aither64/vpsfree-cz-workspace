**Result: stopped**, exit status 1 after 598.3 seconds. The single authorized operation stopped before the manifest build because its dry-run found an unadmitted prerequisite:

`RuntimeError: Unadmitted source/compiler/engine prerequisite in manifest plan; STOP before manifest build`

The run printed `capture-pid=2283191`. Its output identified the stop, but did not include the specific prerequisite details. No retry or cancellation was performed. The run’s artifacts are under `application-output-work/application-build-resume/`, including `manifest-frontier.json` and `outcome.json`.