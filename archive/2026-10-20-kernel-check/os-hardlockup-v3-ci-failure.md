# Panic-policy v3 CI preparation failure

Existing run [39745935323](https://github.com/vpsfreecz/vpsadminos/actions/runs/39745935323)
at exact `8528262315b0794a8f50917cf33c53a07fd14030` reported a failed native
product test-suite job while lifecycle jobs remained pending. Its retained
Luna/low watcher completed accounting after replacement-head publication;
no duplicate observer or retry was launched for this old run.

Final status: completed/cancelled at exact old head after authorized stale-run
cancellation. All eleven jobs are terminal: four success (OS/cache and three
livepatch), one failure (native test suite), six cancelled (livepatch).
[Final metadata](os-hardlockup-v3-ci-39745935323-final-metadata.json),
[test-suite log](os-hardlockup-v3-ci-39745935323-test-suite.log) and the final
artifact directory `os-hardlockup-v3-ci-39745935323-final-artifacts/` (125 files)
are retained. Watch handle99939 ended, CLI exit130 following terminal-state
SIGINT, no watch process remains. The new generic-feature CI has its own single
fresh watcher; these old results do not validate it.

The first preserved cause is a kernel-source fetch failure in preparation:
GitHub returned HTTP 429 for Linux archive `1dfea587406b7dd79973831d1677fb2418e5e9aa`.
The fetcher's own retries at one/two/four seconds also failed. The failed fetch
caused `linux-config-6.12.113`, `55-nixos-aslr-entropy.conf`, `/etc`, an OS closure,
`os-test-zfs-boot-modes.json` and the aggregate prebuild to fail. The native
`test.log` contains the selected test list; there are no executed VM assertions
in this attempt. This is a preparation failure, distinct from the older
[retained-dataset assertion failures](os-hardlockup-ci-failure-analysis.md).
No runtime panic-policy failure or generic-service validation follows from it.

First evidence: [full native preparation log](os-hardlockup-v3-ci-39745935323-test-suite-artifacts/os-test-logs-39745935323-1-native/prebuild-20261022-2473075-piak9v/build.log),
[native test log](os-hardlockup-v3-ci-39745935323-test-suite-artifacts/os-test-logs-39745935323-1-native/test.log).
Original watcher-downloaded artifacts are retained. No retry or workaround was
performed. The lead accepted this bounded classification; later focused test
sequencing must avoid an unexpected local kernel build and may wait for its
new exact-head CI/cache prerequisite. No VM test is authorized before review.
