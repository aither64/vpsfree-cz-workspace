# C fresh rooted browser failures: two mobile expand clicks

Current source unchanged and clean at f10d3d48c4f21cc39187c3667ffffd9952404c11;
base5a2d2bdc3ad7a827038f877d75959916528db844, two-commit authored series retained.
Fresh actual rooted-runtime62case batch exit1,393.23s, retries0:
31/31desktop and29/31mobile passed. This result is independent of historical
31desktop passes on the earlier collected rootfs. No synthetic result merging.

Failures: e2e/specs/app/action_state_detail_page.spec.ts:60, user and admin cases.
Both reach line129 clicking action_state.detail.tx.toggle.7001. Target exists,
is visible/enabled/stable and related transaction data are present. Click logs
repeatedly report page space-y-6/CardBody/progress-bar elements intercepting
pointer events after scrolling; native90s timeout then fails the case. Both
screenshots show the view shifted horizontally, with the card edge/expand
chevron at the far left and broad blank area. This indicates a responsive
hit-testing/overflow problem; exact cause and base reproducibility remain
unproven. There is no receipt/auth/transport assertion failure in these cases.

Spec and owning ActionStateTransactionsTable.tsx, ActionStateDetailPage.tsx,
and components/ui/Table.tsx are unchanged from base (empty scoped Git diff).
The inherited table uses overflow-x-auto, minWidthlg and last-column expand
button. Source identity alone does not prove the failure is preexisting; no
base browser rerun or fix has been performed. Do not force-click, hide the
case, add retries/timeouts or modify UI without an assigned boundary.

Artifacts retained for BOTH roles under browser-full-rooted-artifacts/:
app-action_state_detail_pa-219c4-xpandable-payloads-for-user-mobile-chrome/
and app-action_state_detail_pa-0f42b-pandable-payloads-for-admin-mobile-chrome/.
Each contains error-context.md, test-failed-1.png, video.webm and trace.zip.
SHA256/size inventory: browser-full-rooted-failure-artifact-inventory.json.
Full reporter JSON browser-full-rooted-results.json, full command/log/exit/time
browser-full-rooted.*, before/afterclosureJSON and reconciliation JSON adjacent.
Fixtures contain synthetic sessions/data; no live OAuth/member/API mutation.

All185runtime closure paths/NAR sizes/references match before/after the full
run; registered fhs-gc-root remains present. Same wrapper/locked inputs/
Playwright1.61/Chromium1228/ffmpeg1011 and unchanged cached binary hashes.
The historical8byte rootfs NAR delta is retained separately, with plausible
builder/cache explanation explicitly unproven. Current full run directly
tests the restored actual closure; runtime collection is not the cause of
these two remaining click failures.

All owned operations reconciled, native handles consumed, Vite/browser exited,
52847no listener/free. Normal frontend/BFF/provenance/source/package outputs
and clean/flake sources restored exactly and protected by registered roots;
retain for later cluster preparation. No cluster use, deployment, source/Git,
push/PR, host policy/GC, lifecycle or root cleanup action. A owns solewatcher;
C used authorized parent fallback and has released execution capacity.

Browser acceptance remains open pending lead disposition/assigned fix for
the two mobile cases. Unit1899/script228/BFF57/normalbuild/Nix checks passed.
No retest or repair launched.

Baseline facts prepared without a checkout/run: mobile-baseline-source-facts.json
contains exact BASE/current source and lock comparison; mobile-expand-trace-facts.json
contains both retained trace context/viewports, scroll attributes and click
coordinates. Architect baseline brief is pending; no preexisting disposition yet.
