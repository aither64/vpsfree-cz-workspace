# Architecture and repetition review

No Blocking or Important findings.

## Advisory A1: Keep the editor's reveal completion inside its interface

`dev-workspace`, commit `28a49ea405d60d7a4620d2727ce2867f77baa385`,
`portal/internal/web/static/repository-review.js:332`.

The new sticky-header adjustment waits two animation frames after `revealLine`
and queries `.review-linked-line` inside the editor's DOM. Both the highlighted
class and the second scroll measurement are owned by
`portal/review-ui/editor.js:204`, whose current `revealLine` interface returns
only a boolean. This makes the host depend on undocumented editor timing and
markup. A future change to highlighting or measurement scheduling can leave a
linked line obscured while `revealLine` still reports success; the missing DOM
match silently skips the adjustment.

When this boundary next changes, let the editor provide a completed reveal with
an explicit inset or a documented position result. Keep the enclosing pane and
sticky-header geometry owned by the review component. The new browser checks
exercise the present implementation, so this is a maintenance concern rather
than a reason to block the presentation follow-up.

## Scope and ownership checked

- Reviewed the three runtime commits from `b837f0d974a98857daef7e4cc09d8f3039a059a0`
  through `774db1205a0cd653b687cec34e788eabd6a9f1c1`, their messages, changed
  implementation and tests, adjacent editor and routing code, and local rules.
- The optional comparison callback has two discovered mount consumers: the
  shell in `app.js` and `test/repository_browser.cjs`. The shell owns sidebar
  layout, while the renderer reports comparison transitions, including loading,
  unavailable repositories, closure and destruction. Both desktop comparison
  mode and the existing mobile mode use one CSS presentation.
- Inspected both consumers of the shared Codex limits template: session and
  index. The index retains its separate mobile width and popover placement.
- The archival presentation adapter consumes the existing CLI payload.
  `WorkspaceAutoArchive::Policy` still owns tier selection, delays and
  eligibility; no duplicate archival decision engine or persisted-state writer
  was introduced. Matching selected legacy diagnostic strings is proportionate
  to the explicit no-API-change boundary; unmatched diagnostics remain visible
  in Technical details. Read generations keep old reads from replacing a hold
  response, and failed refreshes retain the last successful values.
- Checked the organization delta `f6050a4d661be7c923518e0b962a4372ebad7f50` to
  `109e9ded49d9b336a25f44ebfdbe19e5ed598b90` and workspace pin delta
  `1c3f3e156cad0f84090ec1934acbb867eb723345` to
  `a24742ab2e999cabafe81926a4271af436546b19`. Their `lib.mkPackage` consumption
  remains unchanged and pins the reviewed runtime through the organization
  extension. The Codex provider remains at `882c88ccfbebfb646fb2cafbe9bc6790141b2d13`.
  The intervening shared-master tracking commit is outside this implementation
  review.

## Residual verification

The packet records passing focused Go, JavaScript syntax and whitespace checks.
I inspected the new browser tests but did not run browser or integration suites,
as requested. Actual sticky-header geometry, mobile linked-line visibility and
popover/focus transitions remain for post-review acceptance. The new real-page
fixture exercises the session sidebar; include the shared index template in the
responsive smoke check because its mobile selectors also changed.

Risk: Medium. Lane: Architecture and repetition. Reviewer: gpt-6-astra, xhigh.
