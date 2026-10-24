# B expanded frontend handoff

Final B is `9f03387583185d213c14ca09af190bcc27a7f309`, tree
`d73fbad45383f236a926f81a6be10931b79f4830`, SSH-published and clean.
Base is `bf6d4b0c49600c15e17fe71248807ef43424e932`; remote master is unchanged.
The exact tested tree equals the final tree. Receipt: b-frontend-final.json.

The complete ten-commit series is b-frontend-series.txt. The first seven commits,
including the sole final A55e selection, are exact to reviewed07e. The last three
own presentation/geometry diagnostics, ordinary composer handoff and required
question keyboard adoption. F1 URL changes are folded into their owning UI and
keyboard commits; the private member fixture correction is in the composer commit.
No fixup commits remain. There are no migrations or new browser record formats.

A is published55e0300b27b6927b1693b3792042762f31a385cc. The Go module, checksums,
Nix source and regenerated vendor digest agree; exact values and source consumer
graph are in the receipt. No W/C edits. Original deployed7b8c and reviewed394/480/5e/
07e sources, bundles and receipts remain preserved. The deployed head is not a
literal ancestor after accepted history consolidation. No substantive product-tree
equivalence to the deployed package is claimed. Mechanical history refresh equals
its preconsolidation tested tree; retained safety patch IDs are unchanged.

## Changes and review boundaries

The real transcript viewport retains its stable message-list/footer children.
The original capture2 wheel, clock and anchor invariant remain unchanged.
A bounded200-event fixture timeline now records exact anchor/viewport/footer/
entries geometry, wheel/scroll/resize/DOM and request/release/response order.
Capture2's scrolled-up failure remains unproved; no product follow fix was guessed.

Ordinary Send verifies durable identity before a Sending row owns the captured
intent, detaches saved attachments before clearing text and permits next-draft
editing/uploads. Only one ordinary HTTP dispatch runs; Send/Queue wait for HTTP
settlement independently of refresh/ack. Original unknown identities remain exact.
Late receipts/ack cannot clear even equal-content new drafts. Known accepted text
can be sent explicitly again under a fresh ID, including page-local acceptance
whose metadata write failed. Queue/native/server admission remains unchanged.

Required wizard fields use A's actual published bindQuestionAnswerKeyboard with
the existing owning Next/Submit button and validation. The button was already
explicit type=button; no extra button-behavior change was made. Approved guide
copy is applied verbatim. Optional inline/pinned questions inherit the A binding.

F1 separates public cached A module23 from mandatory-export module24 and A CSS9
from notice CSS10. All B app consumers select58; session B style23 already
separates deployed22. The full asset inventory is b-f1-cache-inventory.json.
The focused cache source contract plus actual HTTP helper-export assertion pass.
This is source-contract evidence, not a browser cache-navigation pass.

The private QuestionBrowser fake accepts only its two explicit synthetic IDs and
returns matching transcript identity. The shared strict fake is unchanged.
Fault cases reset only disposable upload selection between cases; every durable
attempt and attachment tuple remains. These API fixtures never prove native
acceptance or backend retry delivery.

## Checks and evidence

b-f1-final-quick.log: changed JavaScript syntax, focused cache/archival/composer/
receipt/shipped-client normal1.421s, races2.752s, fixture compile0.048s PASS.
Browser, Firefox, native, long tests and builds were not run by this owner.
No live Send, provider, plan, ledger, lifecycle, deployment or integration action.

The final published Nix source is
`/nix/store/avimdzlgggbc2p5m9jwc2ghidgnxymvr-source`, NAR
`sha256-rV0aCWEaMwDAuQvbEjj/wmxpdPWHNSmBT6aiH5EsI7k=`.
All566 Git blobs and modes match. Full/delta/range/history/source evidence is
bound by b-frontend-final.json. b-f1-delta.diff is the exact eight-file07e remedy;
b-frontend-critical-production.diff is empty. F1 direct inspection is step9;
expanded retained review disposition still belongs to the lead.

One-shot final CI snapshot:40020133863 queued. Superseded07e40018792686 was active;
its one cancellation attempt returned HTTP403. Evidence is retained without
retry or credential workaround. Prior5e40014973711 completedSUCCESS. No CI wait.
Prior394 failure uncertainty and all failed screenshot attempts remain preserved.

## Fresh watcher packet after review disposition

Run once from the session tracking directory:

```sh
bash ui-successor/capture-attempt-3.sh
```

The script checks exact final B head and a clean source, retains the Nix shell,
Node24.19.0, Go1.26.6, Playwright1.59.1 and existing browser store paths. It enters
B then `portal` and runs exactly:

```sh
go test -mod=readonly ./internal/web \
  -run '^TestQuestionBrowser$/^(retry_activity_browser_test|composer_handoff_browser_test|required_question_keyboard_browser_test)[.]cjs$' \
  -count=1 -v -timeout=360s
```

PORTAL_BROWSER_TEST=1; screenshots go only to
ui-successor/capture-attempt-3/screenshots. Keep stdout.log/stderr.log/result.json
under that unique attempt directory. The lead launches one fresh Luna/low utility
under dev-session-monitor after review disposition. No manual browser execution.
Retry fixture time stays frozen; do not manually scroll away the failed invariant.
Composer fixture adds desktop/mobile Sending-next-draft images. All actual
HTTP/template/CSP/assets and meaningful geometry assertions remain enabled.

The cheap compilation command is separate from capture:

```sh
nix develop --no-update-lock-file --command bash -c \
  'cd portal; TMPDIR=/tmp go test -mod=readonly ./internal/web -run "^$" -count=1'
```

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
