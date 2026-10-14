# Adapter publication failure

The two ordinary feature-only SSH push attempts of E
d2079f605ae87871037ae73c5e5daf20a3e0d03d were rejected by GitHub with
Internal Server Error. Complete logs/status are kb-runtime-e-publish1 and
kb-runtime-e-publish2. Between attempts, ls-remote reported default0ff827df
and no feature ref. The local source stayed clean at the exact checked head.
No source or credentials were changed, and no default branch was pushed.
The response establishes a server rejection; its internal cause is unknown.
A future attempt must recheck the remote feature and default before pushing the
same committed SHA. Publication does not replace the independent source review.

The corrected final E headf6d2c080469b224ac77765aecd76a6d531358363 also received
Internal Server Error on its separately selected feature publication. The
exact-head publication guard proved default0ff and an absent feature before
push, then stopped at rejection. A fresh read-only after-failure query again
proves default0ff/feature absent; source/index remain clean. Receipts are
kb-runtime-e-review-publish1.*. No blind retry or alternate ref is selected.
Filtered repository metadata/ruleset observations are pending; server root cause
is unknown. Independent committed-source review and local package checks can
proceed without relabeling this as published readiness.

The user explicitly authorized another retry on 2026-10-07. The fresh
`kb-runtime-e-review-publish2.sh` rechecked clean exact f6, unchanged default0ff
and an absent feature, then successfully pushed the feature. The remote head
matches f6 and the local tree remains clean; all publication receipts exit0.
Earlier errors remain preserved without an established internal cause. No PR or
default integration was performed. Publication is no longer a blocker.
