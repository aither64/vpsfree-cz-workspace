# A resume response can precede immediate disconnection

`TestWatchedThreadIsResumedAfterReconnect` and
`TestStaleWatchedThreadDoesNotBreakHealthyThreadReconnect` deliberately close
the first App Server connection immediately after a successful `thread/resume`
response. The disconnection may be processed before `resumeWatched` regains
control. Ordinary local and race runs can miss this scheduling order; the
packaged GitHub Actions run exposed it.

After an accepted resume, retain the watch and successful `Subscribe` result
if the connection generation changed. Skip observer coverage on the stale
transport. Returning an error would remove the accepted watch and prevent the
existing reconnect workflow from restoring it.

The correction passed the two reconnect tests 100 times, and the wider
activity/observer/reconnect tests 10 times with `go test -race`; all Go packages
also passed. Failure evidence: GitHub Actions run 34691312489 in
`aither64/codex-web`.

Related initiative: `work/2026-09-12-portal-review-experience/`.
