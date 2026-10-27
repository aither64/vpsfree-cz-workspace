## Browser acceptance selector correction for Keep open

Status: confirmed static mismatch, narrow correction prepared for lead
disposition; no application/test-source edit or browser run by architect.
Owner2 reported this while preparing the existing acceptance selectors.

In accepted44a/alhm, `portal/internal/web/templates/session.html:104` exposes
Keep open as the intended native checkbox input with explicit `role="switch"`.
`portal/internal/web/presentation_browser_test.cjs:328,329,332` still locates it
as `getByRole("checkbox", {name: "Keep open", exact: true})`. An explicit switch
role overrides the implicit checkbox role for the semantic locator. The
`TestQuestionBrowser` wrapper includes this script, so this is an affected
acceptance-input mismatch, not an assertion that the browser test has actually
run or failed. It does not establish a production switch defect.

Smallest owning source correction: change those three locator roles to `switch`,
keeping exact accessible name, `.check()`, enabled/checked assertions, successful
hold-save behavior, failed POST503, requested hold=false, restored checked state
and visible failure diagnostics. `.check()` still targets the same native
checkbox input; no alternative selector, skipped block or template rollback is
needed. Do not silently patch a copied test, omit this script from its wrapper,
weaken the settings failure assertions or add a new parallel test framework.
The implementation owner is assigned by the lead; owner2's static packet labels
the current selector blocked while preserving the exact current-source recipe.

The focused change needs syntax verification and retained owning browser
acceptance on the corrected source, with the normal final-review/narrow-fix
disposition made by the lead after commit and quick checks. No standalone
new regression test is needed for this locator correction. This diagnosis adds
no reason to repeat unaffected client/native/Go/Ruby results. Preserve old44a
receipts; a repository test edit changes the runtime self-source NAR and may
change the selected package/goModules derivation, so it cannot inherit the
44a/alhm/xcl label. Bind the final corrected source and derivation explicitly,
apply the existing final-dependency proof requirements and assess unaffected
result reuse by actual inputs. Group final source preparation with any other
already-required acceptance corrections before publishing or rebuilding; do
not launch a stale acceptance packet to obtain a predictable locator timeout.
