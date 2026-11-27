# Independent review

Reviewer: `/root/final_review`, standalone gpt-6.1-sol / xhigh, read-only.
Installed catalog selection and fallback reason are in the review packet.
All four lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. No nested agents.

## First committed review

Range `99207a8dcd92f5907c52dbc99af52b30aa7ecac1..84cc09332fc09e3178405df34539cbd4c1d20a46`.

- Important (general/risk): intentional pause, graceful draining and full queues
  stop advancing the poll timestamp. Enabling watchdog supervision could restart
  a healthy paused daemon after 900 seconds and resume queued work. Fix required
  before integration tests; liveness must originate in the transaction thread.
- Advisory (documentation): explain the existing watchdog_debug diagnostic
  interface so operators can obtain a backtrace before manual recovery.

Lead accepts both findings. The design addendum records the main-thread progress
clock and preservation of real-poll timestamps. Specs and packaged pause/resume
coverage will verify the correction; affected-lane follow-up uses this reviewer.
The runbook now documents the existing newline-delimited JSON debug request,
greeting/response framing, root access and bounded client waits.

Reviewer concluded: coherent two-commit purposes; no obsolete unmerged history,
no repeated dependency/channel/input/generated update streams, no migrations.
Policy belongs in AppConfig and supervision in the common NixOS module. Scope
matches all-role mail/DNS request; test acceleration remains guest-only.
Restart=always, KillMode=mixed and the 90-second deadline fit the existing
wrapper. Generated unit and package must be deployed together. No coordinated
node update or data migration is required. Documentation placement and preserved
transaction-failure reference are appropriate, with the diagnostic omission
above. Runtime integration remains unexecuted pending remediation/review.

## Corrected final review

Same reviewer/settings; final head `258a62e4ac7234639aecebf6cdce726ef9c5fcd7`.
Reviewed the old-head correction and full final range against the original base.
No new findings; both prior findings resolved. Progress belongs to the main
transaction loop, remote handlers expose it without manufacturing liveness,
and the wrapper's fallback preserves older response compatibility. Paused,
draining and saturated loops remain healthy; blocked DB/worker-completion
paths still expire. No competing watchdog or speculative abstraction.

Final history conclusion: coherent two-commit series; rejected polling-only
iteration folded into its owning second commit; no obsolete branch history,
no repeated update streams, no migrations or persisted-format changes.
Documentation placement and preservation remain sound; diagnostics and
in-memory pause semantics now explicit. Reviewed evidence: 37 focused examples,
six final CLI examples, nine Ruby files lint-clean, clean worktree/range diff.
Gate clear for long integration. Runit consumers also receive the intentional-
skip correction, so the selected standard-node regression remains required.

## Narrow runtime-test correction

Head `f3a74127a30fffc9d14a26100636ce2cfed91110` folds the runner-DSL correction
into the same second commit. The exact delta from the final reviewed head is
one line: replace unsupported `let(:machine)` with a local machine binding.
No production change, new design or contract expansion. Lead inspected the
whole delta and final two-commit series, Nix parse/whitespace passed, all hooks
passed. Apply the mandatory-review narrow-fix rule without repeating review;
runtime rerun remains required. No migrations/obsolete history/update streams.

## Runtime-discovered CLI correction

Retained reviewer `/root/final_review`, gpt-6.1-sol/xhigh, reviewed affected
General and Risk/compatibility lanes at final head
`a8ef7163832f3c246bb3927f00d68dd5a001818b`. No findings. The one-line parser
binding restores default stop, force flags and help without changing parameters,
authorization or daemon shutdown behavior. CLI dispatch checks intercept remote
execution and exercise the actual parser. Prior runtime failure is before RPC.
The test DSL correction preserves all assertions.

The reviewer checked the complete original-base-to-final-head three-commit
series: minimal policy, supervision/progress/tests/docs, independently revertible
pre-existing stop parser fix. No obsolete branch history, redundant/repeated
updates, dependency streams or migrations. Unaffected architecture and scope
conclusions remain valid. Documentation remains consistent and correctly placed;
recovery guidance and navigation are preserved. Range whitespace and clean tree
were independently checked. Final-head packaged/runtime checks remain required.
