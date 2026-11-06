# T3: English archive drafts

Source checkpoint accepted by the lead. Main-context prose checks and requested
corrections are complete. Independent final review awaits completion and quick
checks of C/E/T2. Every T3 translation remains a draft pending human review of
meaning and voice. Implementer3 retains technical and review-fix ownership.

## Scope and exact revisions

- Repository: `git@github.com:vpsfreecz/blog.git`, feature branch
  `2026-11-06-multilingual-blog-migration`.
- Checkout: `worktrees/2026-11-06-multilingual-blog-migration/blog`.
- Parent: `e9c286b2f403603907265ac28f4bd38b3ae00227`.
- T3 commit: `e8aed2ef787217e8085d782e38a760cd51ddbd90`,
  **Translate 63 archived articles into English drafts**.
- Exactly 63 new `content/posts/<id>/index.en.html` files, 2,213 inserted lines.
  The authoritative ID inventory is implementer3's batch in
  [translation-batches.json](translation-batches.json): 21,528 Czech source words.
- Final inventory digest:
  `b522ed1cde36f23be33c456e9cb1d4f02bb3ab52d070651d86ec3b46eb79977b`.
  Compute SHA-256 over the concatenation, in assigned batch order, of relative
  English path, tab, file SHA-256, newline.

The complete T3 series is this one coherent commit; no superseded T3 approaches,
follow-up commits, database migrations or dependency/generated update streams.
Historical migration narratives inside articles are preserved content, not new
application migrations. Review the exact parent-to-commit diff; the lead owns the
complete multi-package branch packet and history conclusion.

## Sources and editorial decisions

The sanitized public Czech import manifest has SHA-256
`e3c56173acbc2dd018da1d7ce5cd8b73d52e5ef83847a0353b17b107e5a36ab4`.
Each English `translation_source_sha256` records the exact complete Czech-file
hash from that manifest. Original dates, lastmod, taxonomy slugs, article IDs,
translation keys and shared author/discussion metadata remain unchanged.

Read all assigned Czech bodies and the public author map before translation.
Applied repository authoring instructions, D6, the lead's voice brief,
vpsfree-user-facing-writing and English Humanizer guidance. The two reference
Discourse announcements were verified as aither/Jakub Skokan. Translations retain
each source author's byline, viewpoint, first person, jokes and historical claims;
they do not invent experiences or update old recommendations. Complete prose,
headings, lists, tables, captions and relevant alt text were translated. Literal
code, including Czech comments and arguments, stays in the original language.

Lead performed contextual prose checks across all 63, including full paired
source reading for the pilot and next ten. Requested wording corrections were
applied before committing. This is agent editorial checking, not human approval.

Recorded source/presentation exceptions:

- wp-592: interpreted the invitation's missing Czech negation as “don't miss it,”
  accepted by the lead; Czech source remains unchanged.
- wp-662: retained the original weekday/date mismatch. Lead approved the explicit
  clarification “4 June (4.6.)” for the symbolic date.
- wp-746: translated the source's “before 13” as “before 13:00,” as directed;
  the complete supplier statement and all other dates/times remain intact.
- Decimal commas and spaces before percent signs were localized to English
  presentation, preserving values. Original statistical inconsistencies were
  retained; the missing-value en dash in wp-702 is source table data.
- wp-821 retains its source HTML list nesting. Protected relative Czech links
  remain literal; render-time resolution belongs to the theme owner.

## Verification and limits

All 63 passed complete-source hash freshness, draft/status/no-human-review-fields,
date/lastmod/taxonomy/identity, HTML tag/end/comment/nonlocalized attribute order,
URL/media order, original more-anchor and normalized numeric-value checks.
Numeric comparison includes the two explicit equivalent date/time presentations
above. Routes had no collisions in the concurrent snapshot of 113 English
articles; that was not a claim of final 125-article completion.

Final **raw-byte** pre/code parity passed for all 63. Earlier text-mode checking
missed newline normalization during prose edits in wp-662 and wp-824. Commit was
stopped, owned index entries were unstaged, and the lead renewed the repair window.
Restored exact protected spans from authoritative Czech bytes: 11 CRLF in wp-662
and 21 CRLF in wp-824. Removed only unprotected EOF blank lines across all 63;
accepted prose stayed unchanged. The final verifier compared raw bytes.

Remaining `git diff --cached --check` diagnostics were all byte-identical protected
source code: 43 locations, wp-15=2, wp-174=4, wp-397=5, wp-662=11, wp-824=21.
Every diagnostic was mapped to a source-identical pre/code span; no unprotected
whitespace remained. No hook framework or active custom hook is declared. No hook
was bypassed. Commit used an ordinary temporary message file with `git commit -F`.
Working and staged inventories matched the final digest; post-commit checks
confirmed exactly 63 committed paths and an empty index, then index ownership
was yielded. No whole-checkout cleanliness claim: T2/C/E work was preserved.

No push, default-branch integration, production change, forum write or deployment
was performed by T3. No runtime build was launched for this source batch; the
lead coordinates combined source checks and independent review. All translations
have `draft=true`, `translation_status="draft"`, no human reviewer/date, and
explicit English root paths. Human review and publication approval remain later
requirements. Source changes invalidate affected translation hashes.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.
