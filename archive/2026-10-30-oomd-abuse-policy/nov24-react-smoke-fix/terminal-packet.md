# React Reports selector correction — terminal handback

Clean public head `b09d8dfd2605cb0733bc62ee9225bc295a9acf24`, tree
`2b262533098fbd03a3423db58a9f65125438a292`. SSH publication and independent
readback passed; PR333 reports this exact head. Main remains
`4499f90fe11df0e4df6f23e5fa54829e2254ec1b`. Supported comparison saved.

The full base-to-head series remains two purposes: unchanged registry dependency
`b8908402c3d27d324b3752ee05d6dfd15f74c728`, then complete UI `b09d8dfd`.
Normal owning amend preserved the UI author/date/message. The only change from
preserved `6c6792a6` is one local Select class line, `min-h-11 min-w-40`.
All other blobs/modes are identical. No migrations, dependency or shared CSS
change. See `affected.diff`, `full-final.diff`, `full-series.txt`,
`committed-review-source.json` and accepted independent `review.md` (no findings).
Old reviewed/deployed refs remain; no successor deployment or default integration
is claimed.

Original Chromium CI had eight Reports cases fail height 36 instead of44.
Original WebKit had four English Reports cases fail Policy selector width
156.765625 instead of at least160; its totals were647 pass/4 fail/2 skip.
Trace DOM and assertion ordering identify the same Policy selector. Baseline4499
already contains the unchanged selector/shared Select/test contract. See
`causal-baseline-kb-assessment.json`, `webkit-causal-result.json` and retained
original logs/artifacts. No managed KB text/media is affected.

The existing four semantic tests, focused strict typing, ESLint, Tailwind,
format and diff checks passed in the recorded20.712s quick batch. After final
review, all eight affected EN/CS desktop role cases passed in52.445s
(53.904s wrapper); actual Select height44 and widths175.14/211.23, with existing
overflow/focus/error/write assertions unchanged. See `fixed-cases.json` and
`desktop-fixed-geometry-summary.json`.

Local WebKit remains **unverified**: its first page fixture timed out before
navigation and three cases did not run. A single bounded blank-page diagnostic
shows resident WPE WebKit aborting while creating an EGL display. No application
assertion was reached; no retry, install, restoration or test relaxation followed.
See `webkit-local-disposition.json` and original probe stderr. Exact successor
hosted WebKit CI remains root-owned verification.

The five documented package outputs/checks passed on exactb09 in90.429s.
Actual frontend/BFF metadata both report fullb09, dirty=false. The cleaned source
contains2893 exact included Git blobs/modes; source18-required and package389-asset
checks passed. The actual rebuilt frontend FOD contains registry SDK0.6.0,
348076B, SHA256 `f4ea2206e80798f001cd16942c99fab1c3c4bcaccac707ea3ca841b65efd1f3d`,
with the verified SHA512. BFF logic/cache remain unchanged; provenance reused
its exact resident derivation. The frontend FOD was absent at admission and
rebuilt against the unchanged locked output/hash. See concise receipts under
`final-packaging/`; prior6c package/CI evidence retains its original scope.

Finite exact-head CI inventory (all attempt1, in progress at the single read):
main369520612/run45471733377; PR broad369520614/run45471732905;
PR smoke369520616/run45471733441; push broad369520614/run45471716923.
No active superseded same-branch runs required cancellation. No watch/wait/rerun.
Root owns CI disposition and final PR verification prose.

All command and fresh Luna/low watcher effects are joined. The finite Vite
registrations remain exited/failed; port15173 is unbound. No service stop,
retirement, cleanup, default, registry, deployment or lifecycle action.
See `terminal-receipt.json` for exact handles. All source/index/Git/check/effects
windows and capacity **returned to root**; technical follow-up remains ours.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
