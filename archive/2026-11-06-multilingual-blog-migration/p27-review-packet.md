P27 review packet — committed source milestone

BLOG branch 2026-11-06-multilingual-blog-migration at /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog.
Package 8b30ba027d3cedcc0b9bc10746a2dbc199b18aba..e9d241f4243a4098e669da0d9f7caf2d85976a9f; tree f5d604099c704fba343e6c88529129bd2643a984; clean worktree and empty index.
Complete history 0354dac281978867ea8c1553b092ce19bccb5ccd..e9d241f4243a4098e669da0d9f7caf2d85976a9f: 31 coherent commits (p27-full-history.txt).
Final package diff: p27-source.diff; inventory/checks: p27-source-result.json.
Brief: design.md:4305; accepted extra byline partial recorded by lead.

Requested outcome: draft/unlisted/published visibility via explicit draft plus
optional boolean params.unlisted. Reviewed unlisted copies use main/direct URLs,
not discovery. Announcement date can change before publication; published cannot
demote or reset its date. Stable IDs/URLs/bundles/GUIDs/review provenance retained.
One state partial and finite filters, no build-list accessor/state framework.

Quick evidence:21 authoring tests PASS215.074s, including real staged hook and all
P26 main/feature/rerun/unknown regressions plus new state/date cases. Tiny pinned
Hugo production/promotion/future-preview fixture PASS1.256s. New Pagefind variant
is committed for later full bin/check, not run at this stage. Normal retained
hook PASS125 bundles during declared-env commit-F. Syntax/diff checks PASS.
All250 imported language files and shared-data/import-manifest/pins/workflow/client
source remain byte-identical (p27-protected-source.json). MAIN six-file writing
pass and approved banner strings match p27-main-prose.json.

Retained failure evidence: initial tiny assertion reused a boolean-attribute
helper incorrectly; scoped assertions now test membership. Content-dir override
was not faithful for the source-scanning adapter. One unsupported ContentDir
probe was reverted completely; isolated --source root exercises literal
content/posts, with no product configuration extension. Empty term structural
canonicals are permitted, navigation/sitemap must exclude them. Count assertion
now reads actual HTML. Logs r1/r2/r3/r4/r5 retained;21 passes were not rerun.

No migrations, schema/client/package/uploader/protocol/pin/workflow changes.
No repeated dependency/generated streams added. P27 is one coherent feature
commit, extending the accepted P26 ancestor without fixup/obsolete commits.
Prior complete30-commit review retained; consumed a66 upload and ordinary
main-only restoration remain ancestors and their immutable artifacts/receipts
are separate. No history rewriting/consolidation of consumed identities.

Compatibility: older templates ignore unlisted. Build review content only with
compatible templates/checks; rollback code must preserve that support or remove
the review source through reviewed edits. Static complete-payload rollback is
unchanged. Visibility is not access control; explicit links may disclose URLs.
No production source currently uses unlisted; existing corpus defaults published.

Lead owns final independent review invocation and lane/risk selection (state,
publication/rollback compatibility suggests all4 lanes). No independent review,
full bin/check/check-release/native build, push/CI, integration, deployment,
settings, service or lifecycle action is claimed by this source packet. Keep
actual selected a66 artifact distinct. Next: review, fixes if any, then released
related full-check/native batch. Session remains open.

P27 narrow review correction successor

Immutable initial review source remains e9d241f4243a4098e669da0d9f7caf2d85976a9f. Owning unpublished commit was
ordinary-hook amended to a24ed26f04ccdbf09684ad8e855c64b37d03aae4, tree 0eaf28311e866c2591dc7d71b140edc4202c0724, parent8b30. Exact old-to-new delta
is p27-review-fixes.diff: bin/check only43+/11-. Every other blob, including all
six MAIN prose hashes, is identical. This is a changed successor, not an
equivalence claim. G1/G2/G3 focused actual Hugo checks PASS4.351s/1.397s, syntax
and whitespace PASS. Declared-env normal pre-commit hook PASS125 bundles during
commit--amend-F. Clean head/index, full31-commit history and no migrations.
Evidence p27-amended-source-result.json, p27-amended-full-history.txt,
p27-review-fixes-quick.log, p27-review-fixes-commit.log. Prior21 green retained
without repeat. Fullcheck/Pagefind/native/push remains held for final acceptance.
