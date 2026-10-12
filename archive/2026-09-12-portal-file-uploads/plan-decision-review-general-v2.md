# General review rerun: turn-bound plan request identity

Reviewed only the correction and consolidated pins described in the final
section of `plan-decision-review-packet.md`:

- dev-workspace correction
  `9ed5ff56171b0b1a127aa1bbe26b10580bef7d36..2bfb0ee6aa4d56cbcbe079ef49c79d772a2e8fcf`
- final vpsfree-dev-workspace pin `909fde20f06384a54cd36297688182456f1dc7b1`
- final workspace pin `f9d156a2f2447ba033b4dd3ceb967203cfe972e3`
- final vpsfree-cz-configuration pin
  `4362c8c1a866b125a398fa40737fbd9082913223`

Provider `c0fbae9d4828bb05fdf5f17f9b85a66eaf98c612` is unchanged. This
bounded rerun used gpt-5.6-sol with xhigh reasoning effort and did not rereview
the previously accepted upload, plan-freshness or composer-presentation work.

## Findings

No Blocking, Important or Advisory findings.

Runtime commit `2bfb0ee6aa4d56cbcbe079ef49c79d772a2e8fcf`
binds a new same-thread implementation attempt to both the plan turn and exact
content digest. The browser uses `plan:<turnId>:<digest>` consistently when it
looks for a pending receipt, selects a durable attempt and sends the version 2
request. An accepted attempt from an earlier turn with identical plan text can
therefore remain visible as its own delivery receipt without qualifying the new
decision as pending or donating its client ID to that decision.

The server selects the versioned context before calling the provider's
non-submitting reconciliation API. Version 2 can recover its own accepted or
submitting receipt after the conversation advances. An unversioned old-page
request gets only legacy `plan:<digest>` reconciliation; if that finds no
submitted receipt, the handler returns a reload conflict before reading the
plan, changing collaboration mode or calling `Send`. Unknown nonzero versions
on same-thread requests are rejected before acquiring the mutation lock. The
existing provider ledger stores an opaque context string, so the stronger
identity needs no schema or state migration.

The compatibility boundary is safe in both directions. A new server can finish
an old submitted receipt while refusing an ambiguous legacy prepared request.
An old server cannot mistake a recorded version 2 attempt for a legacy attempt
because its action context differs, so rollback may require a fresh browser
attempt but cannot silently reuse or resubmit the version 2 identity.

## Commit series and pin consistency

The correction is one focused commit containing the two sides of the same
browser/server request contract and their regressions. Splitting either side
would create a temporarily mismatched identity, so the stated indivisibility
rationale is convincing. Its message describes the final behavior, legacy-page
boundary, unchanged ledger and rollback consequence.

Each downstream feature range still contains one pin-only commit. The final
graph selects codex-web `c0fbae9`, runtime `2bfb0ee`, organization package
`909fde2` and workspace package `f9d156a`; the configuration lock selects the
same provider and runtime. The generated configuration changelog includes the
turn-bound correction. No unrelated committed delta appears in the rewritten
pin commits.

`git diff --check` passed for the correction and all three downstream ranges.
Reviewer `GOWORK=off GOFLAGS=-mod=mod go mod tidy -diff` produced no module-file
change. The packet records a green full runtime Go suite at the final head,
including the browser contract, plus a passing JavaScript syntax check; those
checks were not repeated.

## Residual validation gaps

- Runtime tests use a controlled Codex controller while provider tests establish
  the generic context/state checks separately. The later live acceptance should
  exercise a version 2 response-loss recovery and a legacy submitted receipt
  against the real durable ledger.
- The browser contract directly covers equal text across different plan turns,
  but the real-browser fixture should still verify the emitted version field,
  fresh client ID selection and visible receipt/decision behavior through an
  actual second identical plan.
- Unsupported explicit plan-context versions are rejected by a simple branch,
  but this new input-validation branch has no focused regression.
- Exact-head package/configuration builds, cached forward/rollback behavior and
  deployment remain later phases; this rerun inspected pin consistency without
  executing those long checks.
