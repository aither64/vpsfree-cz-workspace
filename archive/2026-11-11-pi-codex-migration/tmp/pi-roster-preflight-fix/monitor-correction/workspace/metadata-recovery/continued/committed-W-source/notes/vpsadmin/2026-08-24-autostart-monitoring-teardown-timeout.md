# Auto-start monitoring CI teardown timeout

## Symptom

vpsAdmin CI run `32666845611` attempt 1 reported
`vps/autostart-monitoring` as the only unexpected failure after the test had
already logged its example as successful.

## Cause

The test behavior passed in 192.53 seconds. During cleanup, osvm timed out while
running `poweroff -f`; the command produced no output and the runner then
terminated QEMU. The failure was therefore VM teardown, not an assertion or
vpsAdmin behavior failure.

## Investigation and follow-up

Download the full test-log artifact and inspect the failing test's
`test-runner.log`; the GitHub step summary alone only identifies the test name.
For initiative `work/2026-08-23-vpsadmin-outage-summary`, every WebUI script in
the same run passed, including `webui#support-pages`. After establishing the
cause, run `./test-runner.sh test vps/autostart-monitoring` locally and rerun
the failed hosted attempt rather than accepting an unexplained green rerun.
