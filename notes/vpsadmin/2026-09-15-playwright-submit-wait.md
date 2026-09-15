# Wait for form controls after navigation

Related initiative: `work/2026-09-09-ip-release-mechanism/`.

The IP release browser scenario failed locally and in CI with `No submit button
matched /^Preview addresses$/`, although the captured page contained the button.
The submitForm helper snapshots matching controls with Locator.all(), which does
not wait for the control to arrive after navigation. A later live DOM check
confirmed the expected named form and button.

For the new campaign creation submits, use a scoped
`form.getByRole('button', {name: ..., exact: true}).click()` so Playwright waits
for the control. Existing callers often establish visibility before submitForm;
do not assume the helper itself waits. The corrected live navigation check
passed; the complete isolated scenario rerun is recorded in initiative state.
