# Compact comparison layout: General review

Review lane: General
Reviewer model/effort: gpt-5.6-sol, xhigh

Reviewed committed ranges:

- `dev-workspace`:
  `41c6d75e8f7cdea1e5cbced7d0106d072d56484d..e35cf0b0bfc343d5a4d476340980e06ac252396b`
- `vpsfree-dev-workspace`:
  `6c98b3676a46c9a9c2830198eae9042b064a71e7..2a3f442263ea614173c7eb540c55542a9373b71a`
- `workspace`:
  `c6daa04a9cbf6ce8611c7ae38dcfc7c4cc7a5636..6f10c36642ecb290ee0699ecff965779f37b9702`
- `codex-web`: unchanged at
  `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`

## Findings

No Blocking, Important, or Advisory findings.

## Assessment

The commit series matches the approved compact comparison behavior and is
cleanly reviewable. Runtime commit `2414ffa7d9efbfe47e6d517e57f59b24b34a88b8`
removes tree counts and copy controls while retaining diff-header counts and
copying, and adds decorative folder state icons. Runtime commit
`e35cf0b0bfc343d5a4d476340980e06ac252396b` moves commit or branch details into
the independently scrolling comparison pane, retains the compact toolbar, and
keeps implicit first-file selection out of the URL. The implementation in
`portal/internal/web/static/repository-review.js` preserves explicit file and
line navigation, invalid-file handling, browser-history restoration, parent
navigation, full-file return, and the eight-editor retention bound.

The matching CSS keeps the toolbar outside the scroll pane, removes the nested
full-message scrollbar, preserves independent tree and diff scrolling, and
keeps the mobile layout bounded. The browser fixture in
`test/repository_browser.cjs` exercises a 70-line commit message, initial commit
and branch entry, explicit navigation and history return, desktop and mobile
toolbar geometry, folder disclosure state, retained header copying/counts,
parent/root/merge navigation, full-file and line links, CSP, lazy assets, and
editor retention. The README describes the resulting supported behavior.

The two downstream commits are exact pin-only updates. Commit
`2a3f442263ea614173c7eb540c55542a9373b71a` selects runtime
`e35cf0b0bfc343d5a4d476340980e06ac252396b`; commit
`6f10c36642ecb290ee0699ecff965779f37b9702` selects that same runtime and
organization commit `2a3f442263ea614173c7eb540c55542a9373b71a` with matching lock
metadata. Commit subjects and bodies follow the local repository rules, and
`git show --check` reports no whitespace errors.

## Residual risks and test gaps

- Full package verification, exact installed-source verification, and live
  browser acceptance are deliberately deferred until review reconciliation.
  The component fixture supplies strong behavioral coverage but does not
  replace the prepared live check and screenshot inspection.
- No 5,000-file stress run, shallow-repository exercise, or live rollback is
  claimed. These are deployment-confidence gaps rather than evidence of a
  defect in this range.
- The previously accepted extreme-directory-depth recursion limit is unchanged
  by these commits and remains the applicable comparison-availability risk.
- The coordinator's subsequent test-only CI timing remediation is outside the
  frozen ranges above and is not covered by this report.

## Supplemental General review: final CI-test delta

Reviewed additional committed ranges:

- `dev-workspace`:
  `e35cf0b0bfc343d5a4d476340980e06ac252396b..dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd`
- `vpsfree-dev-workspace`:
  `2a3f442263ea614173c7eb540c55542a9373b71a..b37edd0f63fb7a984ba634c2d52d08e9344304b4`
- `workspace`:
  `6f10c36642ecb290ee0699ecff965779f37b9702..7985e127b55b48683457fdfe12a894e983d32890`

### Supplemental findings

No Blocking, Important, or Advisory findings.

Commit `dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd` changes only
`portal/internal/web/creation_test.go:128`. The test now holds model validation
blocked, starts the creation request independently, and requires the HTTP 303
response through a buffered channel before the release channel can close. Its
five-second timeout is a deadlock guard rather than a performance assertion.
The later `entered` receive also proves that the worker reached the blocked
validation, so an implementation that omits validation cannot produce a false
pass. The request helper used by the goroutine only constructs and serves the
request; the buffered result channel prevents a delayed sender from blocking
during failure cleanup. The reported twenty focused repetitions and five
race-enabled repetitions provide appropriate quick coverage for this test-only
change. Runtime behavior and the already reviewed UI source are unchanged.

The amended pin commit
`b37edd0f63fb7a984ba634c2d52d08e9344304b4` selects exact runtime head
`dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd` in both `flake.nix` and
`flake.lock`. Site commit `7985e127b55b48683457fdfe12a894e983d32890`
selects that runtime and exact organization head
`b37edd0f63fb7a984ba634c2d52d08e9344304b4`, with matching original and locked
revisions. Each final branch contains one reviewable downstream pin commit
rather than successive pin updates. `git show --check` reports no whitespace
errors in the supplemental commits.

The package, exact-head CI, installed-source, and live-browser checks listed
above remain the residual acceptance gaps; this test-only supplement does not
change them.
