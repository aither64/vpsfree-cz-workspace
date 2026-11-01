# Legacy advisory membership layout correction

Real legacy006454 run advanced to11passed/1failed/6notrun. Its normal check()
found node_101_add visible/enabled/stable but the aside help Edit link intercepted
its pointer. Native13files retained at
`/tmp/2026-11-01-published-advisory-corrections-acceptance/notification-diagnosed/native-failure`.
Guest screenshot/trace did not survive teardown; no visual proof of that guest
state is claimed. Native call log and production source establish the owner.

Source:1150px.main,820px#content with15px#content-in padding,300px aside. Seven
auto-layout columns including four size14date/note inputs and lastActions column
can extend beyond the805px available area. Cell-level overflow does not contain
the table. No test viewport override; default desktop is1280x720, page meta1150.

Lead accepted a narrow existing-form fix: only security_advisory_node_form() gets
form_create's third argument security_advisory_nodes. The helper emits that name;
no conflicting selector or generic_form JS dependency exists. Existing main.css
adds only a form[name=security_advisory_nodes] max-width100%/overflow-x:auto rule.
No table column/input size/payload/guard/sidebar/JS/membership semantics change.
The existing real membership case now checks the named form's right edge against
content and retains ordinary check()/form submission. No forced click or deadline.

Three frozen paths:
- webui/forms/security_advisory.forms.php
- webui/public/template/css/main.css
- tests/playwright/webui/specs/security-advisories.spec.cjs

Quick PHP syntax, PHP-CS-Fixer dry-run declared php83 tool(zerooffenses), JS syntax
and exact-three-path/whitespace checks passed. Initial component PATH/vendor
formatter invocations were unavailable; selecting declared Nix php83Packages tool
passed without any application/dependency change. Component shell preparation ran
existing Composer metadata maintenance; it reported no lock/install change.

One bounded synthetic capture used the actual PHP node form, actual XTemplate
and actual main/scheme CSS, with synthetic API objects, existing packaged
Playwright/Chromium and no API/network operation. This is layout evidence, not
real backend acceptance. Initial fresh watcher failed before browser launch due
to missing default headless-shell; legacy config explicitly selects full Chromium.
Temporary script was corrected to that same executable, then parent fallback
ran once when native delegation was not callable. The corrected command passed,
exit0; browser was closed in finally and command exited, no process remains.

At1280x720, real CSS without only the new scoped rule: form client805px,
table970px, content/form right885px, table right1049.921875px, scroll0,
overflow visible. With the rule: form remains805px/right885, scrollWidth970,
overflow auto. Normal checkbox check succeeded and naturally scrolled the form
165px; table right became884.921875px. Input size14, expected_statepublished and
revision9 remained unchanged. The [single screenshot](legacy-node-layout.png)
shows the implemented synthetic layout after that normal interaction; title
identifies synthetic source/data. No new screenshot campaign/harness/dependency.

Patch `/tmp/2026-11-01-advisory-layout.patch`; measurements
`/tmp/2026-11-01-advisory-layout-result.json`; initial launch failure
`/tmp/2026-11-01-advisory-layout-check.log`; corrected output
`/tmp/2026-11-01-advisory-layout-corrected.log`. Temporary PHP/JS fixture scripts
remain/tmp only. No project Git/index/commit/rebase/push or long runner by
implementer1. Handoff to implementer0 freezes all3paths; its B amendment,
independent affected committed review, D pin/strict check and released real
legacy retry remain. KB has zero existing advisory bindings from prior scope;
no content/capture/publication or KB edit performed by this owner.
