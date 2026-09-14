# General review

Reviewed the committed series at the packet's exact bases and heads, including
all repository-local `AGENTS.md` files, commit messages, implementation diffs,
tests, and documentation. The five series are logically split and their commit
messages follow the applicable repository rules. `git diff --check` and the
base-to-head ancestry check pass for every reviewed range.

## Findings

### Blocking: other session windows never remove a cluster after reset completes

Commit `451d25ddbf9f33aa0e696a0cd4b2896eb24dd333` adds cluster observations to
the session-details response, but the browser only iterates over clusters that
are present in that response
(`dev-workspace/portal/internal/web/static/app.js:1535-1546`). It does not
remove an existing card when a provider disappears or rebuild the cluster
section. The actual reset path removes the entire provider state directory
(`vpsfree-dev-workspace/dev-clusters/lib/runtime.sh:566-575`), after which
`MayExist` is false and the details response contains no entry for that
provider (`dev-workspace/portal/internal/web/server.go:884-895`). Consequently,
another window that observed the cached running state plus “Cluster is
changing” receives an empty cluster list after reset and leaves the old card,
running state, readiness, credentials, and transition notice visible
indefinitely. This contradicts both the cross-window stop outcome and the
notice that status will update when the operation finishes.

The Go cache test ends with a synthetic `found: true, state: stopped` response;
it does not exercise the real reset result (`found: false`), and there is no
browser contract for the busy-to-absent transition. Reconcile removals in the
DOM (or return and replace the rendered cluster section) and cover a second
window through busy status to absent state.

### Important: creation reloads discard selected model and reasoning effort

The new draft record stores only `name`, `goal`, and `creation_date`
(`dev-workspace/portal/internal/web/static/app.js:1000-1017`), while the same
form also contains user-selectable `model` and `effort` controls
(`dev-workspace/portal/internal/web/templates/index.html:41-48`). After an HTTP
or network failure, reloading repopulates those controls from the model catalog
with their defaults, so resubmission can create a session with different
settings from the user's pre-acceptance form. The new browser acceptance checks
only prompt restoration (`dev-workspace/test/creation_browser.cjs:45-60`) and
does not expose this loss. Persist both selections and restore them after the
asynchronous model options are populated, with coverage for a failed request,
reload, and unchanged submission settings.

### Advisory: comparison capture reports ordinary lock contention as failure

`saveComparison` takes its per-pair lock with `LOCK_NB` and returns
`EWOULDBLOCK` directly (`dev-workspace/portal/internal/web/repository_comparisons.go:74-90`).
The new status observation, history rendering, comparison opening, and the
explicit CLI capture can all save the same head. A concurrent loser therefore
becomes a generic unavailable result in the repository-state/history APIs
(`portal/internal/web/repository_review_batch.go:83-95` and
`portal/internal/web/repository_review.go:392-395`) or makes the required
pre-integration CLI command fail. Status and history refreshes run on their own
timers, so this is an expected overlap rather than corrupt input. Wait for the
short critical section, retry/reload the winner's record, or treat contention
as a skipped supplementary observation. Add a concurrent writer test that
also proves an exact capture cannot be replaced by a fallback.

## Residual risks and test gaps

- The planned headless creation acceptance, packaged checks, and live
  cross-window validation remain pending until findings are reconciled.
- The focused runner test proves concurrent calls and a bounded stuck guest,
  but real OSVM poweroff, forced reaping, wrapper cleanup, and the portal's
  180-second deadline still require the planned integration exercise.
- The reported no-build flake evaluations for the organization and workspace
  passed; this review did not repeat them or run long integration tests.
