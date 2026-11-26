# I4 current review correction

Current head: **73bb7a4f40a3120f80b87def611e3dd15cbb6d6d**; clean worktree.
The retained original reviewed/accepted head is
`9e6ed96a49de2f6b65bb3e730047c428b77185f4`. Its complete packet is preserved in
[reviewed-9e6ed96a-evidence.md](i4-logs/reviewed-9e6ed96a-evidence.md).

Reviewer0's lead-relayed interim finding was reproduced against the original
component code plus new regression fixtures: a TypeError, HTTP-503 HaveApiError,
or malformed-output ApiOutputError from the active-chain READ displayed unknown
submission and disabled retry before any POST or durable acquisition occurred.
All three new cases failed in the [reproduction](i4-logs/review-preflight-reproduction.log).

The focused correction uses the existing React Query mutation context. It exists
only after onMutate's preflight and durable acquire succeed; the installed
query-core resets context at each attempt. Submission uncertainty now requires
that context, and error-receipt tracking has the same condition. Read/acquire
failures remain ordinary recoverable errors. No new error type, local state,
controller, SDK/API behavior or user-visible copy is added.

New regressions prove no generated submit, lock acquisition/settlement, task
tracking or fabricated uncertainty panel for failed READs, and a deliberate retry
can submit once and complete acceptance. Existing ambiguous-POST and missing
receipt tests still require the uncertainty guard.

- Fix range: `9e6ed96a49de2f6b65bb3e730047c428b77185f4..73bb7a4f40a3120f80b87def611e3dd15cbb6d6d`.
- Commit: `73bb7a4f storage: keep backup preflight read failures retryable`.
- Fix scope: **2 files, +38/-4**, component and current component tests only.
- Complete branch range: `e311b1c0af0f50fa4c6f6ce83c514c1a866eb042..73bb7a4f40a3120f80b87def611e3dd15cbb6d6d`.
- Complete series: original `9e6ed96a` plus focused `73bb7a4f`; **19 files, +849/-10**.
- [Fix diff](i4-logs/review-preflight.diff), [complete diff](i4-logs/review-current.diff),
  [series](i4-logs/review-current-series.txt), [exact receipt](i4-logs/review-preflight-receipt.json).
- Final consolidation remains under lead coordination; original review continues
  on committed fixed heads. No published or merged history was rewritten.

| Affected check | Result | Evidence |
| --- | --- | --- |
| Component suite | **16 passed**, including the three read failures and existing unknown dispatched-request safety | [unit](i4-logs/review-preflight-unit.log) |
| Application `npm run typecheck` | **Passed** | [types](i4-logs/review-preflight-types.log) |
| `audit:mutations:check` | **Passed**, zero warnings | [audit](i4-logs/review-preflight-mutations.log) |
| `audit:ui-strings:check` | **Passed** | [audit](i4-logs/review-preflight-strings.log) |
| Declared Prettier and `git diff --check` | **Passed** | Scoped source/test formatting; no whitespace errors |

The initial type check caught a missing httpStatus in the new test's synthetic
ActionResult; that fixture was corrected before the final 16-case and type pass.
No unchanged full batch was repeated. The same final SDK/canonical dependency
input from the accepted packet remains installed; no manifest/lock/provenance
change occurred. Nix-context contributor identity and required hooks were honored;
no hook was bypassed. No repository docs changed because the existing documented
submission-uncertainty contract is unchanged; session evidence records this fix.

No migrations, backend changes, long/browser checks, push, PR, CI, release,
integration, deployment, service/machine ownership or lifecycle effects occurred.
No command remains running. Independent review, post-review long/browser/KB work
and published-SDK prerequisite remain under the retained I4 package. No next
package was accepted.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-backup-disable-design/
