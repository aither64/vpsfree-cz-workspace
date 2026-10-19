Both Important findings addressed in runtime HEAD (git rev-parse ../dev-workspace).
Sidecar callback invokes lifecycle_completed after validated retirement proof and
before unlink. Real CLI/store regression 1/30 passed including failed replay.
Requested reservations stay requested during archive fence, already-held become
blocked_recovery, completion releases. Waiting-owner and related focused tests
4/25 passed. Both amended into reservation commit; consumer pins await review
completion to avoid churn. Please conclude remaining review and rollout assessment;
lead will inspect narrow fixes and bind final generated pins to exact runtime.

CLI revive finding also fixed in runtime 9deefdf. revive_confirmation now enters
its own lifecycle access context so preflight waits/revalidates, and run_revive
runs that read preflight under with_lifecycle_transition. The package/session
locks release before prompting; Runner#revive retains its ordinary mutation
admission afterward. No locks across prompt. CLI contention test passes 4/32
including original archived-lifecycle and pending-confirmation tests. Diff is
review-cli-remediation.diff. Workspace docs/coordination.md archive exception
is fixed and consolidated into policy docs commit. Final pins regenerating now.

History cleaned: runtime now 10eccec lifecycle + 6ab3b48 reservation release.
CLI confirmation fix and its test are in lifecycle commit. Final tree differs
from 9deefdf only by removing the whitespace at line2308; full-range diff check
passes. Generated consumer pins now being regenerated to final 6ab3b48 source.
No additional substantive change. Lead independently verified commit split and
both complete final ranges. Rollout finish accepted per reviewer source check.

Final inventory updated at runtime6ab3b48 / workspace4b22d04f / config9e90ff6e.
All worktrees clean and published. Ready for report.
