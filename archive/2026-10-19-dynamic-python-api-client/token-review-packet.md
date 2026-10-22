# Token bridge follow-up review

Read-only affected review after checked committed correction/consolidation.
Retain reviewer0 saved Sol/xhigh settings. Reuse original full four-lane review
and GET-boundary/history follow-up; only new bridge diagnostics and token-test
assertions need inspection. No live tests, dependency setup or source writes.

Change: `7cb07fa77dd048fa46241a766dfacbbea946f04f` to the final tree
`18ef1468e4c3f1c2bb3a1694d93c01ea1c87b3b7`; four paths, +81/-9.
Final consolidated HEAD `9cdb038b2e8400a4e99885ae88d8278a352f34b7`;
seven series:9530f37,ef5af18,4787ad2,69699d9,40526b2,f575a84,9cdb038. Base remains
`c58704a08451a231fdf6c6123437133422af46dc`.

Intended outcome: actual revoked/pre-expired tokens must fail a fresh protected
`user.current` request (401/403 + status=false). Public OPTIONS can succeed for
invalid credentials; the prior set_auth expectation was invalid. The original
local batch's root assertion line was suppressed, so source proof justifies the
correction but a targeted rerun must still confirm. All runtime bytes unchanged.

New harness diagnostics: private --tb=short child output is removed with private
manifest; persistent evidence contains only bounded known file/line locations,
allowlisted error types and fixed test identity in explicit evidence directory,
mode0600. No raw message, source line, local variable/function or fixture value
is copied. CONTRIBUTING documents required variable and outputs. Assess secret
handling, useful failure evidence, actual HTTP proof and proportionality. Risk
HIGH due to authentication test artifacts; apply general, architecture and risk
lanes, bounded scope check only for the new sanitizer. All reference paths in
mandatory-change-review skill apply. Avoid Nix shells that install dependencies.

Owner checks: Python Ruff and five-scenario collection; Ruby syntax/RuboCop;
secret-injection proof (forged frames/types, source/function/locals ignored,
permissions and 80-line bound), whitespace and normal hooks. Lead inspected
four-file diff, new CONTRIBUTING prose and server-source rationale. No live
retry before this review. Prior checks:261 units/mypy18/Ruff38/Rack46; generic
59 and package/release pass; CI five workflows pass at original published head.
Actual vpsAdmin ten scenarios: eight pass, two token modes need this rerun.

History: correction a650bba folded into owning bridge40526b2, exact
pre/post tree equality verified. Other six streams patch-equivalent; no new
pins/dependencies/versions/generated updates or runtime compatibility changes.
No migrations/schema/server persisted format; feature never merged, released,
deployed or externally consumed. Retain refs. Final branch remains unmerged;
no integration/publication/session lifecycle operation authorized.

Related evidence: verification/token-remediation.md, verification-summary.md,
review.md, review-followup.md, verification-plan.md. Test-only changed files are
in HaveAPI feature worktree; vpsAdmin reference fb2f512 remains read-only and
actual released gem0.29.12. End report with findings, remaining gaps and explicit
scope/history/no-migrations conclusion for this bounded delta.
