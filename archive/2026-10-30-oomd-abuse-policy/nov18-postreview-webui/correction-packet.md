# WebUI list pagination correction

Current verification: the final reviewed successor0117035 passed the complete
existing PHP/API browser scenario; see [the final execution packet](final0117035/packet.md).
The93e42090 source checkpoint and its unexecuted-live-test statements below are
historical. Original9e/d304 receipts remain immutable; no provenance is relabelled.

Package93e42090, implementer4. Final source is
`9e020bd0f8271fa6b2592bc6eeddee0067d615b5`, tree
`e7d8cb9c6060c48259f5443f9f4fc750e31f35f7`, parent reviewed/failed-run source
`d30445cb885d0da8186bf9a1620e8578f3414ffe`. Exactly one path changed:
`tests/playwright/webui/specs/incident-escalation.spec.cjs`. Worktree clean,
index empty; normal commit and fresh utility are terminal. The source/index
window is returned to root. No publication or new VM/browser integration run.

## Cause and original evidence

The original test navigated to the member's unbounded first admin VPS list page.
Its HTTP200 response contains VPS rows1–25, limit25, blank From ID, and an actual
Next link with `from_id=25`. The newly created VPS is29; it appears in the
transaction log, outside that list page. Thus the row locator had no element
at spec63; the negative old-summary assertion was not established. The original
trace, screenshot, full error context and HTTP response were recovered with
read-only `debugfs dump` from the stopped retained services image. No mount,
journal replay, guest restart or disk write was performed. Raw trace/context
remain ignored and untracked because they include disposable authentication
state; do not publish them.

The actual PHP `vps_list_form` forwards limit25/from_id0 to the list operation.
The exact packaged HaveAPI0.32.2 ActiveRecord adapter applies `id > from_id`
before the limit. The unchanged row helper correctly locates visible rows.
This establishes pagination as the cause without an API authority or rendering
change. [Original PNG](original-failure.png), [trace](original-trace.zip),
[HTTP HTML](original-list-response.html), [full context](original-error-context.txt).

## Correction and finite checks

The existing list URL now passes `from_id=${vpsId - 1}` and explicitly requires
the target row to be visible before the unchanged negative summary assertion.
Every other original byte/assertion remains unchanged, including all policy
draft/Save, shared permission, member denial, scoped history and CS navigation
checks. No timeout, fixture, helper, PHP, API or topology change.

The offline control uses the original HTML, actual unchanged row helper and
the existing packaged Chromium/project launch options. It confirms visible
row25, exactly rows1–25, missing row29 and the real Next cursor25, with an offline
browser context and no network requests. Its first launch used Playwright's
default headless-shell lookup, unavailable in the existing Chromium-only output;
that exit1/log is retained. Reusing the existing project launch options corrected
only this local control; the control then exited0. No dependency was installed.
See [control output](offline-dom-control.log) and
[original launch limitation](offline-dom-control-launch-failed.log).

Node syntax, whitespace and exact-delta/assertion-preservation controls passed.
Normal pre-commit hooks (Nixfmt, MigrationSpecs, API/WebUI i18n) and commit-msg
hooks passed; only the72-column text-width advisory remained, within the80-column
message requirement. Fresh Luna/low CLI74905 and source14989 both exited0;
sourcePID133105 is absent and the utility reports all owned work terminal.
See [quick log](correction-quick.log), [hook log](correction-commit.log) and
[receipt](correction-receipt.json), SHA256
`1955ded9325b1810fa16e52ab2f025687badaf3bd506cd8249626aaf5815b289`.

## History, input impact and remaining verification

The [complete series](correction-full-series.txt) starts at the final review's
backend base `537b0b7c4ce1d8a930c5fd24b8f4317271ae4f02`. This is one additive
normal corrective test commit; no history rewrite. d304 remains a literal
ancestor with all old review/publication refs retained. The
[exact d304 delta](correction-final.diff) is only the two added/changed test lines.
No migrations, exporter, schema, API, SDK, site, React or configuration input
changed. Existing5aa1 export/SDK/KB provenance stays literal. The earlier alerts
PASS remains bound to d304 and its actual inputs; this packet makes no new
whole-suite or Nix-result reuse claim from tree equality.

The actual WebUI config consumes this test script, so its config/derivation input
will change on any later execution and must be rebound then. The original
failed d304 attempt and all actual6687-graph/source evidence remain immutable in
[failed-receipt.json](failed-receipt.json), SHA256
`caece8654caedeb26ff32d83b35d6480a9a5b44964d01701fd5395ac5a234bc3`.
Earlier admin settings assertions reached spec63; member/history/CS and old-summary
absence remain unproven. The offline control establishes cause/locator behavior,
not successful execution of the corrected live query or subsequent assertions.
Root owns affected independent review and any later full existing scenario,
publication or demo allocation. Hosted CI44236668585 remains a separate root/
owner1 read-only diagnosis; no controls were repeated for it. Demo/reset HOLD.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
