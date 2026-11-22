# Test asynchronous creation by ordering

Organization CI 34713657833 failed the creation-navigation test after 0.88s even
though the handler returned the expected 303 while ListModels was held on a
fixture channel. The assertion imposed 500 ms on response handling, so runner
scheduling or filesystem overhead could fail a correct asynchronous response.
The logs did not isolate which overhead dominated. The same UI head passed
runtime CI 34713615190.

Keep validation blocked and require the response via a buffered channel; use a
generous timeout only to detect a deadlock. This proves response ordering without
benchmarking CI hardware. Twenty focused runs and five race runs passed after the
change. Runtime behavior was unchanged. The final pinned organization flake check
and development-cluster check both passed on the corrected final head.

For details and final CI result, see
work/2026-09-12-portal-review-experience/compact-ci-investigation.md and
compact-ci-results.json.
