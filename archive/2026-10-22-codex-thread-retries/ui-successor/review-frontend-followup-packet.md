# Composer and question keyboard: affected final review packet

Status: RELEASED for affected FINAL review. Intended frontend changes are complete,
committed and quickchecked. No policy/backend expansion is included.

User steering during the retry UI work:

- Ordinary Send can remain “Sending…” for five seconds with text trapped in the
  textarea; rapid follow-up messages are awkward.
- Question answers must submit with Enter and insert newline with Shift+Enter,
  matching the main prompt. The user explicitly corrected the shortcut.

Accepted scope: design.md supplement “Ordinary Send composer latency and question
keyboard follow-up”. Architect0 owns design. Implementer0 owns small A keyboard
binding/contracts/docs; implementer1 owns B composer/wizard/actual-page fixtures.
Lead applies visible-copy pass and accepts evidence.

## Review boundaries

Retain reviewer0 Sol/xhigh/read_only, all four affected lanes. Risk high: ordinary
delivery UX, browser-persisted intent, exact replay/draft ownership and public
cross-project helper. Prior all-lane presentation review is review.md; P1 direct
remedy in review-findings.md. No need to repeat unchanged native/ledger review.
Full final histories, migration and sole A update-stream conclusions remain
mandatory for complete branch readiness.

Expected A change: bindQuestionAnswerKeyboard(input,submit), optional inline/pinned
answers and required JSON editor use existing submit action. Plain Enter once;
Shift/other modifiers and IME/229 preserved; repeats cannot duplicate. Hidden,
disabled/readOnly/invalid states cannot bypass ordinary validation. No standalone
durable sender redesign or native change.

Expected B composer: durably save/read back captured UUID/text/attachments/target,
honest pending Sending row, detach selection before clearing captured draft,
immediate editing/uploading next draft. One ordinary HTTP request in flight,
Send/Queue dispatch held while it runs; no automatic buffered second send.
Settle without waiting for refresh/ack. Original receipt/retry/history must not
clear next text/selection even when intentionally identical. Recovery/reload uses
exact old identity. Local persistence/detach failure preserves draft and sends
zero requests. Captured target/generation prevents member response rerouting.
Queue/plan/Interrupt/settings retain owning semantics and backend gates.

B required wizard uses shared helper via its existing requestSubmit/Next/Submit
validation, saving/progressing answers without premature final submission.

## Evidence required at release

- Exact A/B bases, final heads/trees, clean/SSH proof and complete final inventories.
- One final A dependency stream including Go/Nix/vendor; retain deployed sources
  and compare old/new patch IDs/trees if consolidation refreshes history.
- Focused deterministic promise/barrier tests, local failures and uncertainty/
  equal-content/new-draft/member/reload/attachments cases; existing actual HTTP
  incident recovery tests and meaningful keyboard/required wizard contracts.
- Owning documentation/copy and quick log/tested-tree hashes.
- No native/ledger/browser-attempt format migration expected; verify actual source.

A owner package complete:55e0300b27b6927b1693b3792042762f31a385cc,
treeb89b91b73ad5a028edfe9e72f6ecf056bde086af, tested tree exact/clean/published.
Full packet ../question-keyboard-a/final.json and complete base/prior/deployed
histories/diffs/bundles there. Six total A commits retain earlier five and add
one coherent keyboard successor. Node14PASS/0fail/0skip, Go prompt0.019sPASS.
Go v0.0.0-20261023200504-55e0300b27b6, source NAR
sha256-IhCdZ7HpW3sora4/WnvWoCLotFZtMMldGCLItXoC90w=.
No A sender/native/ledger change. Lead copy pass approved, no labels changed.

## Final sources and complete history

A baseea64ef57fdd2ff5fd60715b62f2d1696bc0133e5; final55e0300b27b6927b1693b3792042762f31a385cc,
treeb89b91b73ad5a028edfe9e72f6ecf056bde086af, clean, exact SSH feature confirmed.
Full packet ../question-keyboard-a/final.json SHA256
cdee7120c6e880de36576d07c62769d96c169c5a656515de3ff8967e420a5e27.
Full six commits and deltas there; the prior five remain unchanged.

B basebf6d4b0c49600c15e17fe71248807ef43424e932;
final07e753357f743e4ad6c7a8f4d225ae473ee8292f,
tree9ff7d31d60bc2b189e418a677fc6a934aa137492, clean, tested tree exact.
Complete ten logical commits:

1.7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99 original core.
2.b3c7187c6e26e269994433716a0ee719d0a7edf7 original capability.
3.aafaf4195d695c4641ce4f9342d56a1786f237c3 original runtime.
4.4ff797e51397b9a5c59b1e12b592c9fc0c34c1fd sole final A55e selection.
5.24bf3c0be7288184a420f3112accfc54a94f9cd3 retention.
6.4b3683377a5defcb9d8bcd6410c7177715f38f9b prepared plan.
7.0778278498dd4cd31be49e107cb851ba95e5398a bounded HTTP runtime wait.
8.187672056b5faad8d821ea6f9b8761699e0cab24 retry presentation/diagnostics.
9.a570286d005d52839344757edbdc90fdb461c065 composer handoff.
10.07e753357f743e4ad6c7a8f4d225ae473ee8292f wizard keyboard.

Original first3exact; retention/plan/wait expected unchanged product patch IDs;
verify independently. Prior reviewed/preserved/deployed refs/bundles and old/new
range proofs retained in b-* and reviewed-39497062/. Final tree equals quickchecked
preconsolidation tree. New final A stream includes all Go/Nix/vendor metadata,
vendor sha256-jrp5UYCY0XK0Nw1jzOPv5IRaH4YlLle5M15l8opx4Qo=.
No new migrations/native/protocol/sidecar; verify final source. Source publication/
NAR/final owner packet follows in this directory; do not infer deployment.

B focused final log b-frontend-final-quick.log passes composer barriers, original
notices and actual shipped client1.348s; fixture compile0.045s. Focused race2.642s
in b-frontend-final-race.log. Changed JS syntax passed. Earlier incident2 plan/wait
checks5.965s unchanged product lineage; full prior review in review.md. Actual
required wizard/composer/retry browser tests have NOT executed on this final tree.
Known geometry failure remains unresolved empirically, now with diagnostic trace;
do not label all visual acceptance passed.

The wizard next button already had type=button in baseline: owner initially
misread a truncated hunk, then corrected report. No button-type behavior introduced.
Lead approved guide copy/dynamic diagnostic; no broad server optimization claimed.

## Capture status and limits

Capture1 initial zero messages was corrected by fixture time-zero scheduler drain.
Capture2 reached capacity screenshot but failed scrolled-up anchor invariant.
Owner added bounded geometry/event/response diagnostics, no product fix guessed.
Attempt1/2 logs/images remain under this directory. Expanded reviewed candidate
must run that same invariant and the new composer/wizard browser cases through
a fresh operation watcher; any failure requires diagnosis, not assertion weakening.

Screenshot data is controlled actual-template/CSP/assets fixture evidence,
never backend delivery proof. UI remains undeployed. Policy/backend expansion
is held for user visual acceptance. No integration, machine release or lifecycle
authorization; existing deployed held machine remains retained.
