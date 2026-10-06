# Mandatory review result: retained team archive recovery

## Review identity

- Repository: `dev-workspace`
- Base: `e58f8f61ce43058aba49361a0b3bd1ecd98af866`
- Initial head: `b36691d52790dffb5e104900343dca7f841e55e6`
- Reconciled head: `b9465ab61dfc4e9820e312b062cb7b96ed3f09b0`
- Reviewer: retained `reviewer0`
- Model and effort: `gpt-6-sol`, `xhigh`
- Access: read-only
- Lanes: General; Architecture and repetition; Scope and proportionality; Risk and compatibility
- Final result: both Blocking findings resolved; no remaining or new findings

## Blocking findings

1. `libexec/workspace-host:769` loads `dev-session` through a source-tree-relative path that does not exist in the Nix package layout. A packaged `recover-archive` therefore fails before recovery begins, and the source-tree tests do not exercise the installed layout.
2. `portal/internal/teamruntime/runtime.go:1535` skips exact proof for members whose roster state is already `archived`. After retained-only completion updates the roster, the promised final all-member proof can therefore succeed without checking any member.

## Reconciliation

- `47716d9e846b10698476728386b65b689abf8476` makes the final team gate re-prove exact archive identity for roster members already marked archived, while preserving removed-member and no-roster behavior. Reviewer0 confirmed this finding is resolved.
- The first packaged-loader correction in `47716d9e` found the public installed path but still targeted Nix's Bash wrapper. Reviewer0 kept that Blocking finding open.
- `b9465ab61dfc4e9820e312b062cb7b96ed3f09b0` loads the hidden unwrapped Ruby source used by the Nix wrapper, preserves lazy source-tree loading, and fails with a stable host error if neither supported Ruby source exists. Its regression models both the public wrapper and hidden Ruby file.
- Reviewer0's final read-only rerun found no new findings and confirmed both original Blocking findings are resolved.

Lead reruns at the reconciled head passed the aggregate host recovery/lazy-loader selection with 11 runs and 180 assertions, Ruby syntax, Nix parsing, Go formatting, focused teamruntime/workspace-portal Go tests, and diff checks.

## Other conclusions

- No remaining Blocking, Important, or Advisory finding was reported for this correction or its reruns.
- The change introduces no migration or persisted-format change.
- This was an incremental pre-push review, not the final whole-branch readiness review.

## Remaining verification gaps

- Full packaged mixed-version execution
- Live real-socket final all-member proof
- Full archive test suite and real-lock integration
- Authorized live recovery of both paused journals
