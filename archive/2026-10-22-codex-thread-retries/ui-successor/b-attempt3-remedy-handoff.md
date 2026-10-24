# Capture3 remedies and capture4 handoff

Final B: e1e165e89b7741a95a5b66dfbd15f8a3c3987285. Exact tested tree:
c9874dd068d2de9431b12114e0fb91b95f1ad186. Clean, SSH-published and remote verified.
Receipt: b-attempt3-remedy-final.json. Full ten-commit series, delta, range-diff,
preconsolidation tree equality, final bundle, Nix source and566blob/mode proof are
bound there. First seven commits and sole A55e pin are exact to9f. The last three
own the UI, composer and keyboard test corrections. No fixups or migrations.

Only three browser fixtures differ from9f. Every product, configuration, guide
and dependency-selection blob is identical; b-attempt3-remedy-product.diff is
empty. Original9f ref/bundle/sourcepacket and capture3 artifacts are preserved.
No browser, native, build, live input, deployment or lifecycle command was run
by this owner. Capture3 remains FAILED in all three cases, with partial assertions
and screenshots retained; no missing or failed case is accepted as passing.

## Separate diagnoses

1. Retry trace sequence26 captures top67 at scrollTop1383 before native wheel
   sequence30. The wheel then moves scrollTop1263 and anchor top187. The exact
   120px shift equals input; footer131.59375/scrollHeight2086/clientHeight703 are
   constant and there is no transcript read/render. The test now witnesses upward
   wheel and scroll delivery plus >48px tail departure before capturing its
   anchor. Its real wheel, fixed JS-clock advance, same node and <2px invariant
   remain. No product observer/follow change.
2. Composer fails at observed-before-reply, after earlier unknown/reload/original
   retry checks. Focus invokes recover(false), which can suppress a healthy fresh
   transcript read. The controlled entries changed without a stream hint. The
   fixture now emits the existing EventSource.onmessage, witnesses a new response
   with exact UUID/digest and durable observed proof while the reply stays held,
   then retains lost-response/new-draft/original-ID/ack checks. Request/fulfill/
   hint/hold diagnostics are bounded. Owner0 independently corroborated the source
   boundary; no sender/sync product fix.
3. Required wizard reached its second mouse case after the preceding Enter and
   validation checks. Exact radio name First omitted its description First
   approach. The selector now uses exact owned name/value and asserts checked;
   exactly-once progression/respond remain. Bounded phase/radio-label diagnostics
   help any later failure. Lead accepted this fix; architect corroboration stays
   in its read-only lane. No A helper defect or pin change is asserted.

Syntax of all three changed CJS files passed; Go fixture compile passed0.048s
(attempt3-fixture-quick.log). Production normal/race evidence is retained at9f
with exact old-tree provenance; it is not relabeled as a new browser result.

## One self-recording next command, after lead step9

From the session tracking directory, the fresh Luna/low watcher runs once:

```sh
bash ui-successor/capture-attempt-4.sh
```

The command itself creates the previously absent capture-attempt-4 directory,
opens stdout.log/stderr.log before launching capture.sh and writes result.json
with actual subprocess returncode, UTC times, monotonic elapsed and source
identity. An existing output directory refuses rather than overwriting evidence.
The utility does not copy or reconstruct these receipts. capture-command.py
passed a41ms smoke command with exact exit7 and separate stdout/stderr; that
smoke is not a browser test.

capture.sh checks exact final e1 and clean source, uses the existing resolved
Node24.19.0/Go1.26.6/Playwright1.59.1/browser store paths, enters B/portal through
its Nix shell and runs exactly:

```sh
go test -mod=readonly ./internal/web \
  -run '^TestQuestionBrowser$/^(retry_activity_browser_test|composer_handoff_browser_test|required_question_keyboard_browser_test)[.]cjs$' \
  -count=1 -v -timeout=360s
```

Screenshots and bounded failure diagnostics go inside capture-attempt-4/screenshots.
All actual template/CSP/assets, original delivery/geometry assertions and fixed
capture time remain. The lead owns direct remediation inspection/review
disposition and the fresh watcher launch. No browser rerun is authorized here.

## Separate CI reconciliation

One-shot current e1 run40022639730 was in progress; no wait. Superseded9f
run40020133863 completed failure: fast/archive passed, creation failed, host
skipped. Its actual explicit-fork receipt stopped with another dev-session
command changing the source slug, at creation_acceptance_browser.cjs242.
Full failed-step logs and job metadata are retained at ci-9f-failure*. Source
cause is not established and no correction/rerun was taken. Superseded07e
run40018792686 completed success. Prior403 cancellation evidence is retained.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
