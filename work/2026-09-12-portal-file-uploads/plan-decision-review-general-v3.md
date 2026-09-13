# General review: final plan recovery correction

Reviewed only the bounded correction and final pins described in
`plan-decision-review-packet-v3.md`:

- codex-web
  `c0fbae9d4828bb05fdf5f17f9b85a66eaf98c612..ee9ab42791a84b79315d952501264a6cbafc8695`
- dev-workspace correction relative to the previously reviewed tree
  `2bfb0ee6aa4d56cbcbe079ef49c79d772a2e8fcf..7f0d1abd0c382088cc05e7f82d2e65af5b5dd4c8`
- final vpsfree-dev-workspace pin `a4b837f1c976c7611493e2f4f87ad49a008a4853`
- final workspace pin `ab7a866482b3dcd0d1cc2d675a58e8ce00d2527b`
- final vpsfree-cz-configuration pin
  `c7d639ec9d63e5d1f69d3508cf06b49d72b76a36`

The runtime range crosses rewritten equivalents of the preceding reviewed
commits; this review inspected their net difference, the consolidated provider
pin and the new recovery commit. It used gpt-5.6-sol with xhigh reasoning
effort. Previously reviewed upload, plan-selection and composer behavior was
not reopened.

## Findings

### Important: v2 recovery can retire a current or unproven same-turn request

In dev-workspace commit `7f0d1abd0c382088cc05e7f82d2e65af5b5dd4c8`,
`portal/internal/web/server.go:1588-1590` trims `PlanTurnID` when it builds the
exact provider action context, but the retention check at line 1610 compares
the current plan with the untrimmed `body.PlanTurnID`. A recovery request whose
turn ID contains surrounding whitespace therefore matches the real prepared
ledger entry, fails the raw current-plan equality, and reaches
`DiscardPreparedSend`. It retires the current request despite the contract that
current v2 proposals remain retryable.

The same conditional also falls through when `LatestTurnID` equals the source
turn but `completedPlan` cannot prove a nonempty completed plan entry. That is
an unproven same-turn state, yet line 1610 permits retirement because `current`
is false. The packet explicitly requires unproven v2 proposals to be retained.

This can remove the only server-side prepared identity after collaboration mode
has already changed to default. The browser still holds the current local retry,
does not classify it as obsolete, and cannot create a fresh default-mode
submission, leaving the decision retry stuck while also weakening the lifecycle
guard that the retirement API is meant to repair.

Normalize the source turn ID once and require affirmative proof that its plan
identity has been superseded before retirement. At minimum, retain when
`LatestTurnID` is empty or equals the normalized source turn and the current
plan cannot be proven different. Add focused cases for a whitespace-wrapped
current turn and for `LatestTurnID == sourceTurnID` with no qualifying plan
entry to `TestPlanRecoveryRetiresOnlyObsoletePreparedRequests`.

No other Blocking, Important or Advisory findings.

## Reviewed behavior and commit series

Provider `DiscardPreparedSend` takes the existing per-thread and durable ledger
locks, matches the exact message digest and opaque action context, removes only
prepared state, treats absence idempotently, and refuses submitting or accepted
state. Its write-error path restores the in-memory record. The focused provider
test covers exact matching, absence, prepared retirement, lifecycle unblocking,
and preservation plus reconciliation of submitted states.

The runtime separates old-page `action=same` from `action=recover` before any
reconciliation. Recovery cannot send or change collaboration mode. Submitted
legacy and v2 attempts retain the existing reconciliation path; browser state
is removed only after an identity-matched retirement response. The browser
recognizes only the exact legacy and turn-bound context forms and does not
automatically recover a v2 attempt whose source turn is still latest. These
paths are coherent apart from the server retention check above.

Prepared retirement is a focused provider commit. The runtime keeps its
provider pin in the owning pin commit and groups the new server/browser recovery
action in one commit with a convincing shared-contract rationale. The final
downstream ranges each remain one mechanical pin commit. Their lock graph
consistently selects provider `ee9ab42`, runtime `7f0d1ab`, organization package
`a4b837f` and workspace package `ab7a866`; configuration selects the same
provider and runtime. No unrelated committed pin delta was found.

`git diff --check` passed for the runtime correction and all downstream pin
ranges. The packet records green provider and runtime suites, focused recovery
tests, browser contract and JavaScript syntax checks at these heads.

## Residual validation gaps

- The provider write-failure restoration branch is clear on inspection but the
  new retirement test does not inject a ledger replacement failure.
- The Node contract covers recovery request classification, while the prepared
  Firefox fixture remains responsible for proving automatic recovery, local
  record cleanup, held receipt visibility and a later identical plan in a real
  page.
- Package builds, cached forward/rollback behavior, live Codex recovery and
  deployment remain later phases and were not executed in this review lane.
