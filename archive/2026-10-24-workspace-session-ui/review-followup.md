# Independent focused affected-design review

Preserved by lead from read-only reviewer report. Reviewer0 retained
`gpt-6.1-sol`/`xhigh`, native thread
`01a16f9d-3224-70f3-b688-e9fe41ba53f1`, exact session/binding verified, env markers
absent. No override/fallback/nested review, source/Git/runtime action or long
checks. Exact base/head:
`b3a6eb2fc0b41cf0cb965bf4c39991815d9df734..07d41aac2663f6e7079618da6d81bc9474af95ad`.
Clean at assignment; local origin/master equals base. Original review applies to
unchanged patches; R1/R2 direct narrow repair disposition stays lead step9.
General, architecture/repetition, scope/proportionality and risk/compatibility
covered changed R3 design/interactions.

## R4 — Important — general and risk/compatibility

Unchanged retry of definitely-unsent input becomes permanently uncertain.
Composer `a269c622`, `app.js:5823` routes unchanged failed text through
`retryMessageReceipt` with same ID. `dispatcher.retry:337–340` resets waiting,
but first dispatch consumed freshness at `:286`. Second known pre-native refusal
cannot satisfy firstDispatch at `:304`, becomes unknown, disabling replacement/
discard and blocking later work.

Immutable-head shipped-fixture reproduction for Send/Queue: first known400 ->
failed; unchanged retry -> second same400 -> unknown/sameID=true/discard=false;
main-composer replacement makes no request (HTTP count2), head Original message.

Bounded correction: use existing fresh-ID replacement path for every proven
unsent retry, even identical text; preserve action/head/attachments. Test Send/
Queue repeated refusal, including failed persisted entry after reload. This is
a direct correction inside assessed design, eligible for lead step9 focused
inspection/checks; no blanket rerun/protocol expansion. Fix/dispose before long
verification. No new Blocking or Advisory findings.

## Other design conclusions

Apart from R4, R3 boundary is sound/proportional: finite exact status/text pairs
bound to pinned pre-native checks; no generic4xx/substring inference; tab-local
freshness not inferred from restored retry:false; unknown/native/postaccept
outcomes stay uncertain; acceptance proof wins. Main-composer replacement keeps
action/FIFO head, takes ready current IDs/newID, persists before detach and reuses
uploader/cross-record compensation. No shared/server/protocol expansion or
unneeded transaction framework. Real-handler tests establish all ten responses/
zero native calls, plus distinct generic native/postaccept errors; no claim of
native execution ordering.

## Whole-branch history and migrations

Independent full five-commit series/range-diff/final inventory assessed:
settings `439e33a5` and unread `4b3817f4` unchanged; composer `a269c622` folded
repairs/validation tests; quiet `45b12ebd` equivalent to `dedf61d8`; guide
`07d41aac` adds relevant recovery paragraph. No obsolete approaches, fixups or
transitional history. No repeated dependency/channel/input/generated streams.
No migrations or versions requiring merged/released/deployed/external-use proof.
Browser schema1 separate key, legacy attempts unchanged; server/native schemas,
public endpoints/pins unchanged. No deployed/released feature reported or
contrary evidence inspected; no deployment claim. Supplied pre-consolidation
and final tree both `e1444e278ad761b5ce9495a97a86341501c85579`. Fold R4 into
composer and record final head under narrow-fix/history gate.

## Evidence and limits

Exact range whitespace passes. Refreshed final diff SHA256
`d428e833357dc0106e3823a7f3bb1ce6436f7d7cd1b2adbbc594cef343b4e7c1`;
remediation SHA256
`e19aeb3a3e32ed11c9844f01f46459268cac9c355ec1d3400b5cf20fa7430df6`,
match reconstructed Git objects. Go source SHA256
`5071e7331bdbc56b5d8a86ce10e15eac25c5be06a0756d8a166c58efe843cbbc`
matches provided successful unit receipt (exit0, package2.966s), inspected not
rerun by reviewer. Reviewer ran short immutable-object Node R4 diagnostics only.

Chromium/package/native checks outstanding. Multi-steer/two-tab/arbitration not
proven; browser FIFO promises this tab dispatch only. Preserve forward recovery
and pending state; don't use older browser to manage new ordered state. No
integration/deployment approval from review.

Lead disposition: accepts R4, original implementer assigned direct fresh-ID
retry fix/regression; no new design/contract/blanket rereview warranted.
