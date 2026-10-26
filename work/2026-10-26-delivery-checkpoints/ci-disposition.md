# CI disposition

Runtime run [40353591313](https://github.com/aither64/dev-workspace/actions/runs/40353591313)
tested exact head `f8b94441a6b5066973a72284955b793b301c60ac`. Fast package/check
and creation jobs passed; host was skipped. Archive failed before testing archive
behavior, when its fixture added a worktree immediately after starting a session:
`another dev-session command is changing 2026-10-25-lead-archive-repair`.

Downloaded the failed log to ci-failed.log. The failure occurred at 15:57:18 UTC;
the portal started at 15:57:08 and restarted at 15:57:11. Progress observation's
first automatic iteration is after a one-minute ticker, so no scheduled progress
check could have run. This fixture has no configured team catalog or observer,
and it makes no manual progress API request. The changed evidence/settlement
paths cannot run here. Fixture, lifecycle command and lock acquisition code are
unchanged by this branch.

The immediate cause is the existing session command lock being held during
fixture setup. The log reports terminal reconciliation after an App Server
disconnect; the exact holder is not established. Do not turn this into an archive
or provider-recovery rewrite in this delivery feature. No blind CI rerun requested;
retain this unrelated CI limitation in readiness and release notes. Local composed
package verification separately covers the site policy and runtime composition.
