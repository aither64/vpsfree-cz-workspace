# Multi-script test aggregate selector

## Symptom

Running `./test-runner.sh test 'kernel/vpsadminos'` exits successfully but
reports that zero scripts and zero tests were run.

## Cause

`kernel/vpsadminos` is a multi-script test. The runner requires a fragment
selector to choose scripts within it; the bare test path does not implicitly
select every script.

## Fix and verification

Use `./test-runner.sh ls 'kernel/vpsadminos#*'` to inspect the aggregate and
`./test-runner.sh test 'kernel/vpsadminos#*'` to run every script. The latter
selected 14 scripts and completed successfully for initiative
`work/2026-09-02-vpsadminos-chattr-test/`.
