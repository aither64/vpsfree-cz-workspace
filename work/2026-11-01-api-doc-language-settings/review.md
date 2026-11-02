# Independent final review

Reviewer: retained `reviewer0`, GPT-6.1 Sol/xhigh, read-only. Reviewed the complete
HaveAPI range `391b0190241cf195a69b06f7297d3e4eebec5a83..fd61d71ea06a971453c3491370dbc8133b410926`.
All four mandatory-review lanes applied; High risk for auth/search/locale
coverage. Identity/settings verified, no fallback or nested reviewers. Report
received through same-session lead reporting; lead saved this record.

## Findings

1. **Important (general/risk):** Python workflow push/pull_request filters still
   name deleted `doc/protocol.md` and `doc/typed-input-validation.md`. Later
   changes confined to moved English normative articles would stop triggering
   existing Python checks. Update both sections to their `doc/en/` locations.
2. **Advisory (general/architecture):** language submit/change handlers are bound
   inside `updateControls`, accumulating after unrelated preference changes.
   Move to one-time setup and check one navigation after a preference update,
   preserving path/query/fragment and native fallback.

No Blocking or other Important findings. Both findings accepted for remediation.
Reviewer explicitly permits focused direct-fix verification and fresh lead
range/history inspection under mandatory-change-review step 9; no full review
rerun needed if fixes stay within these recommendations.

## History and provenance conclusions

Complete series: runtime/UI/catalog `aa07bfa91179ffda64d5a101a83ed73b3b77e69b`,
article/source-layout/packaging `fd61d71ea06a971453c3491370dbc8133b410926`.
Base is actual merge base; final HEAD and clean worktree/index verified.
Split is coherent and separately reviewable; helpers/templates/catalog belong
together and substantial article prose belongs with source-layout consumers.
No obsolete approach, transitional implementation, abandoned shim or standalone
fixup retained; forthcoming narrow fixes should be folded into owning commits.

**No migrations.** No DB/schema migration, protocol conversion or application
format transition. Source/article relocation ships as a matching package; only
new persisted user state is a nonsecret mount-scoped cookie ignored by old code.
No published/deployed/integrated intermediate migration requires preservation.
**No repeated dependency/channel/input streams.** Generated server catalogs are
one final canonical translation update, no redundant generated history.

## Scope, architecture and compatibility

84-file +4440/-811 diff proportionate to accepted UI localization, five translated
articles and explicitly authorized source reorganization. Growth primarily
translations/catalog data. Existing I18n, server templates and private search
remain the owning mechanisms; no unnecessary subsystem or broadened API rollout.

Authentication resolves before reference/index rendering override; ensure restores
locale. OPTIONS/actions retain API locale handling. Authorized search projection,
locale-keyed indexes, pinned URLs, read-only preference behavior and private cache
checks preserved. No concrete authorization, credential disclosure, traversal or
locale isolation regression found.

Exact English/Česky above Theme and separate programming preferences confirmed.
Weighted/region negotiation reuses existing parser; native form/JS URL fallback
fits intended navigation. Presentation text escaped; JSON uses safe existing
helper. Runtime generated executable code unchanged; schema changes only Envelope
heading. Application/custom renderer text retains documented translation boundary.

Article lookup validates IDs, selects locale/English fallback, preserves public
routes/aliases, mounted links and stable English anchors. Copying/nested gem
inclusion/required-doc/extracted-gem tests cover package boundary. Guides explain
supported behavior and complete-package rollback. No downstream pin/database/node
coordination needed. Python workflow omission is the remaining source consumer gap.

## Evidence and limits

Reviewer independently inspected committed source, tests, catalog consumers,
article prose/links, packaging/release assertions and both messages; diff whitespace
passed. Quick evidence in packet assessed, not rerun. No long checks, source edits,
deploy or merge by reviewer. Broader server/browser checks and live preview remain
pending at this checkpoint. Full browser event integration is needed because
pure URL/message helper tests missed repeated listener binding. Optional generated
adapter prose may remain English under existing-author translation boundary.

Disposition: final review complete with the two findings above, both accepted for
bounded repair before broader verification. This report grants no integration or
deployment approval. Exact final repaired ranges/evidence belong in state.md.
