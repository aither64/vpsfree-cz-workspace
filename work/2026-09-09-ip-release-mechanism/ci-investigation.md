# CI failure investigation, 2026-09-10

## API Specs follow-up, 2026-09-15

[API Specs 34491288836](https://github.com/vpsfreecz/vpsadmin/actions/runs/34491288836)
on `7483c4d2535b994a10ea3a82856052bd78c4913c` failed only the core-engine job
`102918382409`: 912 examples, one failure, 50 pending, seed 24922. All other
jobs passed. The separate full integration workflow `34491288911` passed.

The failed job log identifies a false positive in the initial-notice test:
`not_to include(first.addr, third.addr)` rejects `192.0.2.20` even when the
correctly rendered eligible address is `192.0.2.200/32`. The shared fixture
helper derives addresses from `IpAddress.maximum(:id)`, and rolled-back rows
still advance the database auto-increment counter, making the collision depend
on preceding examples.

Using explicit `.20` and `.200` fixtures reproduced the initial-notice failure.
The reminder example has the same assertion problem; explicit `.20` and `.204`
fixtures reproduced it too. With the old assertions, the focused run produced
two examples and two failures. Both tests now compare the rendered CIDR strings,
including `/32`, and retain the overlapping addresses as deterministic fixtures.
No production eligibility or locking code was changed to fix this failure.

The complete core-engine suite passed with the original CI seed 24922:
912 examples, zero failures, 50 existing pending examples (4 minutes 51.6
seconds). Command: `VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec
rspec spec/models --seed 24922`. Final validation and pushed heads are recorded
in `state.md`.

The fix was pushed in `36a6869fe`, followed by the neutral closing commit
`395bf80b7`. The previously failed core-engine job passed in the new
[API Specs run 34943116908](https://github.com/vpsfreecz/vpsadmin/actions/runs/34943116908).
The rest of that matrix and the new integration workflow are still running at
handoff; template, RuboCop and i18n checks have passed.

The latest failed feature-branch CI run is
[34412825378](https://github.com/vpsfreecz/vpsadmin/actions/runs/34412825378)
at vpsAdmin `1e2d2d7c9bec10d7eb06feaa2c172d10d9fb7a15`. It ran 135 scripts
across 118 tests: 116 tests succeeded and two failed. Both the completed workflow
log and uploaded per-machine logs were inspected; this was not a blind rerun.

## VPS browser fixture

`webui#vps-user-core` failed while adding directly owned IPv4 `203.0.113.137`.
The browser expected “Addition of IP address planned” and received “IP address
is from the wrong location”. The seed constructed the owned IP without
`charged_environment`, so the new accounting-provenance guard correctly rejected
assignment. Other owned IP fixtures supplied that field.

The missing `charged_environment: env` was fixed in `tests/suite/webui.nix` in
`473b5c62aae74734a1b57d7780b75c906400a8d4`. The complete four-test VPS browser
scenario passed locally afterwards (1944.17-second example, 2303.26-second
script). Its later steps, including reinstall, also completed. This fix was
reviewed in v5 and is present in the current branch.

## Network shaper VM shutdown

`network/network-interface-shaper-and-rename` completed every assertion at
03:26:15 CEST. Its example passed in 132.58 seconds and the script in 252.71
seconds. The node's last successful query showed interface `wan0` with
`max_tx=2048` and `max_rx=4096`, as expected.

The failure happened in the test runner's subsequent VM shutdown:
`OsVm::Machine#stop` called `poweroff -f`; the command channel returned neither
output nor EOF before its timeout. `OsVm::Shell#read_output` raised
`UnrecoverableTimeoutError` with an empty buffer. The runner then terminated
QEMU at 03:41:21; QEMU exited at 03:41:24. The guest console contains no kernel
panic or shutdown backtrace. The retained logs establish the shutdown/channel
failure, but do not establish why the guest stopped responding to that command.
There is no failed shaper assertion or evidence of an IP release defect here.

[CI 34474145934](https://github.com/vpsfreecz/vpsadmin/actions/runs/34474145934)
at `feccc00735c1d6323732ca39ef2aced8691d0432` subsequently passed all 12 selected
network/DNS tests. The same shaper scenario, including normal VM shutdown,
passed in 320.98 seconds. The earlier failure evidence remains recorded;
a successful later run is not being presented as proof of the unknown guest
hang's underlying cause. No speculative runner change is included in this
email-copy follow-up.

## Current validation

The feature branch was green at `feccc0073` before this follow-up's literal email
sentence deletion. The new edit changes only email prose and the existing
render assertion; it does not alter release, assignment or VM shutdown behavior.
Focused campaign checks passed 38 examples and localized-render checks passed
24 combinations for this edit; the overlay flake check and touched RuboCop
also passed. Review packet v6 records the exact committed copy-only delta.

The copy changes are pushed as vpsAdmin `37e08d8be` and overlay `ff5cc7c4`,
with v6 review complete and no findings. New hosted checks are running on those
heads, including vpsAdmin CI 34484865348. These are distinct from the successful
network/DNS follow-up 34474145934 discussed above.

## WebUI redesign follow-up

API Specs run 34977231855 failed full coverage job 104407949077 because the
three new campaign endpoints were absent from covered_endpoints.yml. Its raw
log names Exempt, Address.Index and Notice.Index. Registered the existing request
coverage; the plugin-enabled inventory test passed locally and both hosted
coverage jobs passed on subsequent heads.

CI run 34978785877 failed only webui#networking-dns. Downloaded artifact
10402055358 confirms No submit button matched Preview addresses in submitForm.
The helper snapshots controls without waiting after navigation. Scoped waiting
button locators replaced the new creation submits. The other eleven selected
integration scripts passed. The corrected local scenario passed on a75bb80d5
with all five Playwright tests, including the full campaign flow.

Separate live validation exposed the PHP client's required-null rejection on
exemption removal. The new bulk action now uses an explicit removal flag. Its
regression, three fresh review reruns and live bulk removal all passed. Current
head a75bb80d5 has green quick workflows; final hosted API/integration completion
is recorded in state.md. Superseded active workflows were cancelled only after
their replacement heads were pushed.
