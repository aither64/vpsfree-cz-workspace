# Review follow-up: progress ownership and retry fixes

Original report: final-review.md. Same standalone Sol/xhigh reviewer.
Review committed runtime960dd816..39b0ee29739b315049e18510ce334ae2a9f080dd and
workspace0fe886f5..24764c677d9a384fe96142b432ef166754939f35. Runtime original
d4e59794 is retained in Git history for comparing the correction but is no longer
on the final feature series. Its fixes are folded into the single owning commit.
Workspace retains its verification and catalog commits and one amended final pin.
No migrations or deployed/external state; no new interface in codex-web.

All three review findings are addressed for reassessment:

- Dedicated workspacecodex.SendProgressCheck preserves submission/recovery
  identity and cancels prior retry work, but creates no ordinary retry admission
  snapshot. Manual observer assignments still use SendWithOptions. Real
  workspacecodex native-wire tests feed capacity and cyber failures through the
  ordinary retry controller, proving one scheduled call and no retry, then prove
  a subsequent manual assignment retains normal managed admission.
- settleProgressCheck runs before unrelated root/member reads or activity proof;
  exact owned observer cancellation survives their failures. New inference and
  notices still require normal fresh activity/admission. Provider/lifecycle/
  generation gates remain. Regression exercises broken root verification and
  broken implementer evidence at the deadline.
- A retained removed/archived member record retires its pending ownership before
  a replacement can start. It does not transfer work or discard unresolved live
  identity. A completed-but-uncollected old check followed by remove/readd is
  covered. Existing manual/unrelated observer work is held, never steered.

Additional focused check ensures an unconfirmed, unsent pending submission does
not start after non-observer work becomes idle. The older docs sentence about no
automatic team assignments now explicitly exempts scheduled observer checks.

All focused TestProgress tests pass in progressobserver, web and workspacecodex;
Node syntax checks pass. remediation-checks.log has concise evidence. Both trees
are committed and clean. Final lock changed only dev-workspace; all siblings and
extension preserved. Current CI run40300144238; superseded run40298217307 cancel
requested, no extra workflow dispatch or local long test yet.

Rerun affected general, architecture and risk/compatibility lanes. Preserve the
previous scope/proportionality assessment unless a concrete changed boundary
requires revisiting it. Inspect the new dispatch contract itself and its retry
consumer. Record follow-up in final-review-followup.md, retain original findings,
and explicitly update final history/repeated-stream/no-migration conclusions.
Do not edit source or run long tests or spawn another reviewer.
