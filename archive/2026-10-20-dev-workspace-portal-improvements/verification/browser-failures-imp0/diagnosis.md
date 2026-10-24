# Read-only diagnosis: three failed browser fixtures

Bound session verified from tracking; both markers absent under the trusted
binding. Inspected exact clean B `d617ef3968280e9955da85e2d7464a47030e7087`
before imp2's separately owned work. No B edit/index/ref/test/build/browser/live
probe or CI wait. Failed receipts remain unchanged under
`../followup-browser-final/run/`; watcher `../followup-browser-final/watcher/result.md`.
B stage exit1/411.160387s; six first-stop failures. A paging and the three C attrs
passed; those stages do not need repetition for these fixture-only corrections.

The lead accepted the three fixture alignments after direct source/contract
inspection. `candidate.patch` is **PREPARED ONLY**, not applied or syntax-tested.
Its exact three paths and base/candidate byte hashes are in `manifest.json`.
Candidate copies are beneath `candidate/`, never in B. Imp2 remains sole B/Git
owner; no handoff or implementation permission is inferred.

## 1. Files draft setup — fixture order

Retained log: `locator.fill` timed out at
`portal_improvements_browser_test.cjs:122`; textarea resolved but was **not
visible**. Earlier script lines112–114 activate legacy `#artifacts`→Files and
wait for the Files panel and503 eligible rows. It then tries to fill the Codex
textarea while that panel is hidden. app.js2715–2724 activates only the target
panel; style.css218–219 hides every inactive `.tab-panel`. This is expected
normal navigation, not a lost composer or transport failure.

Smallest candidate: move the existing exact draft fill before hash activation.
No force-fill or direct DOM write. Preserve actual Files popup, copy, original
CRLF-byte source download,503 rows, registered label, expansion/refresh-failure
retention and later draft-value assertion. No product change or new contract.
The prior loopback certificate warnings do not explain this explicit browser
visibility failure.

## 2. Settings catalog — obsolete request interception

Retained log: `selectOption("model-2")` at
`team_settings_browser_test.cjs:142` timed out with **did not find some options**,
after the actual select resolved; not a hidden/disabled-control error.
The fixture at line27 intercepts only glob `**/api/models`. app.js2565 calls
`/api/models?session=example` for existing session settings, so that exact glob
misses the request. server.go1639 passes session/provider queries to the normal
model resolver. With the required absent provider catalog,
provider_models.go25 returns `browserContractCodex.ListModels`; server_test.go2664
contains only `model-1`. Thus the fixture's intended second model is never
supplied, matching the failure exactly.

Smallest candidate: a URL predicate accepting only pathname `/api/models` with
exact one expected query `session=example`, retain the same two-model catalog,
count intercepted catalog reads and assert the model-2 option/label exists before
selection. No catchall URL widening, origin/authority behavior or catalog product
change. This fixture's creation/fork catalogs are not its subject; unrelated bare
or provider queries continue to the existing fixture server.

## 3. Paging geometry — overlay-era page coordinates

Retained assertion at `paging_browser_live_test.cjs:112` expected transcript
page-top82.78125 but observed112.15625 when the loading status appeared; difference
29.375px. The fixture stores the earlier page-top at line97 and requires it to
stay fixed. Current session.html110 places history controls immediately before
the transcript in a flex column. style.css258–261 makes the controls **static**,
nonshrinking and visible only when needed. Their appearance consumes normal flow
space. The exact observed direction/step matches that behavior; no current DOM
trace of controls height was retained, so do not claim an independently measured
29.375px notice-height proof.

This page-Y invariant contradicts the accepted contract: design.md16 requires
normal-layout history notices, and docs/workspace-portal.md430 says notices and
manual retry controls occupy normal space above the transcript. It is not
product evidence warranting a CSS reversal.

Smallest candidate: replace that one overlay-only invariant with explicit static
position, positive notice/transcript geometry and no notice/transcript overlap.
For the SAME retained message node, compare its top **relative to the transcript
viewport** during held loading and through successful prepend, failure and retry.
Keep exact held-position comparison, all original `<8px` displacement tolerances,
node identity/connectedness, native wheel intent, one in-flight read, no
programmatic load, failure no-replay and retry/exhaustion assertions. No budget,
wait or tolerance increases. The candidate adds explicit same-node checks at
error/retry rather than allowing a replacement node to satisfy geometry.

All later first-stop paths remain unverified until the targeted actual browser
runs. A later failure may establish a real within-transcript anchor issue; that
must be reported with evidence before any product fix or extra assertion change.

## Six-failure dependencies and review boundary

- Imp0 candidate owns only Files draft order, settings catalog interception and
  paging coordinate alignment above.
- Imp3 owns separate read-only diagnosis of optional-question, delivery-recovery
  and usability fixture failures; no candidate here touches those files or
  duplicates that diagnosis. Their causes/fixes are not certified by this report.
- Imp2 owns the separate four Firefox fixture paths and B Git. The raw Firefox50
  failure is separate from the six Question failures. Wait for explicit serialized
  transfer before applying anything in B; combine accepted fixture fixes without
  overwriting another owner's work. Parent closes sole downstream pins/guards once
  the final B source is settled.
- No production API, schema, authorization, read lifecycle or visible prose change
  is proposed. These are bounded regression alignments within reviewed contracts;
  direct source/test inspection is the intended narrow acceptance route. If an
  actual product failure emerges, route it to lead/architect before broadening.

See `proposed-commands.md` for unexecuted syntax and decisive three-subtest argv.
No blanket full-suite/CI rerun is prescribed by this candidate.
