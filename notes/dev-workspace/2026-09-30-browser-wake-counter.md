# Capture browser request counters before the triggering event

The portal lifecycle fixture sampled its activity-request counter after an
awaited `page.evaluate` dispatched `visibilitychange`. Playwright could process
the intercepted wake request before evaluation returned. The later poll then
expected another request, even though the wake request had already happened.

At generic revision `50af66d`, the full browser suite failed with expected
`> 3`, received `3`. The route handler and
`resumePageReads -> resumeTiming -> refreshActivity(true)` establish the race.
Commit `50586880` moves the counter sample before event dispatch, preserving
the HTTP 503 injection and all existing assertions. Increasing the timeout
would not correct the baseline.

Declared-environment Node syntax passed. A fresh Luna/low watcher ran the
corrected lifecycle fixture three times, the complete six-case browser suite,
and generic flake checks at `50586880`; all passed. Go reports 41.582s for the
three focused runs and 81.702s for the full suite. The flake check took about
6m40s. Logs:
`/tmp/portal-review-browser-505-focused.log`,
`/tmp/portal-review-browser-505-full.log`, and
`/tmp/portal-review-generic-505-check.log` (each has a `.status` file).

The independent review accepted a test-isolation Advisory: a late response
from an earlier focus request could also increment this shared counter. If
the fixture becomes intermittent again, settle or label that request before
sampling the wake baseline. No production behavior changed.

Evidence is in
[the session state](../../work/2026-09-30-portal-review-improvements/state.md)
and `/tmp/portal-review-final-5.log`.
