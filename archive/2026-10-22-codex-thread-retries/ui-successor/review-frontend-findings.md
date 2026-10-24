# Frontend follow-up review findings

Reviewer0, retained Sol/xhigh/read_only, all four lanes, exact A55e/B07e.
Complete report saved review-frontend-followup.md. Exactly one Important F1;
no Blocking/Advisory. A keyboard no findings; no other substantive finding.

## F1: cached old module lacks mandatory question helper

Important, risk/general. B07e app.js1211,5012 imports
/codex/assets/conversation.js?v=23, unchanged from deployed7b8c, then calls
bindQuestionAnswerKeyboard unconditionally. A handler.go268 serves asset with
public,max-age=300. Cached deployedac62/priorf862 module has no export, so new
B page can TypeError while rendering required questions. Fresh contexts miss it.

Requested remedy: version top-level module URL for mandatory export; inventory
changed cached styles/modules in same final frontend selection; focused cache
identity/navigation contract. Keep actual helper, no silent optional fallback.

Lead disposition: fix required, assigned B owner with narrow existing asset-version
mechanism, no new cache framework/API. Preserve07e source/ref/bundle; fold fixes
into owning UI/keyboard commits, focused checks/full history evidence. Reviewer
completes frozen source review; lead direct-check step9 if no new boundary.

Final remedy B9f03387583185d213c14ca09af190bcc27a7f309,
treed73fbad45383f236a926f81a6be10931b79f4830. Lead inspected entire07e→9f eight-file
delta, whitespace, clean status and fresh SSH feature head. Top-level A module24,
session A CSS10 and all three B app entrypoints58; session B CSS23 already differs
from deployed22. Focused source contract binds fresh identities/consistent app
consumers and shipped HTTP helper presence. Cache inventory b-f1-cache-inventory.json
records unchanged child/page URLs; no missing-export fallback.
First seven commits/sole A55e pin unchanged; last three owning commits amended,
reviewed07e source/bundle/receipts preserved. No new API/design/cache framework.

Quick b-f1-final-quick.log: normal1.421s, race2.752s, fixture compile0.048s,
syntax PASS. Tested candidate tree equals final. Requested narrow remedy accepted
under step9, no redundant review turn. No unresolved source findings prevent
focused browser execution; empirical geometry/keyboard/composer gates remain.

## Private member-upload fixture correction

Owner found shared browserContractCodex.VerifyThread permits only thread-1 while
new member-upload case uses member-thread. Lead accepted private QuestionBrowser
fake scoped to those exact two synthetic IDs and matching transcript, preserving
shared strict fake. Disposable upload-selection reset avoids unrelated active-file
deletion. Test-only delta, not a production delivery exception. Commit/check
evidence checked in exact07e→9f delta: private questionBrowserCodex adds explicit
member-thread to shared root strict verification; ReadThread returns matching
identity. Shared strictfake unchanged. Only disposable selection reset changes
fault-case cleanup. No product proof/validation weakened. No browser rerun yet.
