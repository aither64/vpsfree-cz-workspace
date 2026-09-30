# Mandatory review result: retained team archive recovery

## Review identity

- Repository: `dev-workspace`
- Base: `e58f8f61ce43058aba49361a0b3bd1ecd98af866`
- Head: `b36691d52790dffb5e104900343dca7f841e55e6`
- Reviewer: retained `reviewer0`
- Model and effort: `gpt-6-sol`, `xhigh`
- Access: read-only
- Lanes: General; Architecture and repetition; Scope and proportionality; Risk and compatibility
- Result: two Blocking findings; no other findings

## Blocking findings

1. `libexec/workspace-host:769` loads `dev-session` through a source-tree-relative path that does not exist in the Nix package layout. A packaged `recover-archive` therefore fails before recovery begins, and the source-tree tests do not exercise the installed layout.
2. `portal/internal/teamruntime/runtime.go:1535` skips exact proof for members whose roster state is already `archived`. After retained-only completion updates the roster, the promised final all-member proof can therefore succeed without checking any member.

Both findings must be corrected and independently re-reviewed before package builds, downstream pin changes, or live recovery.

## Other conclusions

- No other Blocking, Important, or Advisory finding was reported for this correction.
- The change introduces no migration or persisted-format change.
- This was an incremental pre-push review, not the final whole-branch readiness review.

## Remaining verification gaps

- Packaged mixed-version execution
- Real final all-member proof
- Full archive test suite and real-lock integration
- Authorized live recovery of both paused journals
