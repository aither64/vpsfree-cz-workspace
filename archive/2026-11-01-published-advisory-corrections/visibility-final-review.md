# Advisory visibility: affected independent final review

## Findings

**No findings.** Blocking: none. Important: none. Advisory: none.

The committed server-only correction satisfies the inspected read-authority contract. No source change is requested by this review. This completes the affected independent review gate; it does not establish successful long acceptance or a corrected running preview.

## Identity, instructions and boundary

Reviewer: reviewer0, review-purpose/read_only, saved gpt-6.1-sol/xhigh, codex-lb; native thread 01a19801-1fc5-70e3-ba37-8c0952a89392. The live same-session roster matches that thread, purpose, access and saved settings. No model/effort override, fallback, substantive authorship or nested reviewer was used.

Binding was checked with dev-session current: 2026-11-01-published-advisory-corrections, workspace /home/aither/workspace/ai/vpsfree.cz. Both DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE are absent, consistent with the trusted thread binding.

Read the mandatory-change-review SKILL.md and all four references in full, plus applicable workspace/repository guidance and visibility-design.md, visibility-diagnosis.md, visibility-verification.md. General/history, architecture/repetition, scope/proportionality and risk/compatibility lanes apply. Overall risk remains HIGH because this changes privacy/read authority.

The latest user decision is authoritative: only published advisories are readable by anonymous/member/support; draft and retracted records, children and relations are admin-only. The server owns visibility completely; UIs display its responses. No additional UI hiding, cache/render guard, mock defense or restriction of an administrator's public route is part of this deliverable.

The submitted affected delta is proportional to that contract: two existing server query owners, owning documentation and focused additions to existing tests/fixtures. Prior broad final/refresh/readiness/layout reviews and review-reconciliation.md remain evidence for their exact reviewed sources; this report does not repeat unaffected client/modern implementation review.

## Exact sources and complete history

vpsAdmin, target master:

- Base: 097226b22edf8b59f80b5dfaa55265e9d0cac633
- Final head: a38c9f871f89312f16d18e158efbbbb340ec53e4
- Complete series: A 163677bd45b5ac0a179a0bfa144bcbd9ada9e231, then B a38c9f871f89312f16d18e158efbbbb340ec53e4
- Final tree: 101b160ada8bedb4a316618e7d36355e6a427b1c
- Complete final diff: 26 paths, +2180/-155
- Affected comparison: 49f5a29e5a7d85559d06d31496acb5c08895bcda..a38c9f871f89312f16d18e158efbbbb340ec53e4, eight paths, +223/-6

KB contracts, target master:

- Base: ce2c8cd9358c3636e5d39343e595df813a0b197f
- Final head: 4fd4f2b8ca737b6b6baaf97998fb9484be4c1e91
- Complete series: that single consolidated five-file pin commit, +8/-8
- Final tree: 2c13e344ac4cb5907bae4e450ee87d1cc5be0f8f

Inspected complete commit lists/messages, file inventories and final diffs, together with the affected source diff and preserved earlier-review boundaries. Both worktrees are clean and the supplied bases match their merge bases. Fresh SSH/default/feature-head proof is retained in the packet; I did not fetch or mutate remotes.

The A/B division remains coherent: server behavior with its specs/documentation, then legacy UI behavior with its fixtures/browser coverage. The new visibility correction is folded into the owning commits rather than retained as a fixup chain. No obsolete unmerged approach or transitional implementation remains in these submitted histories.

There is no repeated dependency-update stream in the two-commit API series. The KB vpsAdmin source update is one logical stream consolidated into one final commit; no redundant intermediate pin commit remains. Its four source declarations and locked/original revisions select exact a38c. Only the intended vpsAdmin lock metadata changes; node inputs, root follows, unrelated dependencies, page content, assets and capture provenance remain intact. Explicit vpsAdminOS 6bdf458fd9105379860234ff33d352e55844f08f is preserved. Selected narHash: sha256-GJYdsGVOnxuWjfhUhSdPkQMF3pMDxDrheDpTMharQmk=.

**No migrations in either complete range.** No schema conversion, product seed change, migration rewrite or intermediate migration lineage is introduced or retained.

Old reviewed API49f5/KB5276 references remain retained as historical source/runtime evidence. They are not claimed to be literal ancestors merged into these rewritten successors. I independently checked the submitted affected patch against the recorded candidate, final tree identity, legacy runtime equality and selected KB input graph. These comparisons delimit review reuse; tree equality alone is not a claim that new derivations or running systems have passed acceptance.

Modern source is restored to exact 1c8478bceb3943645ec06ccde895ee4b0985873f, clean, as recorded in modern-visibility.md. The 15-path f7c4eb282cd146d5b905c70db74f2aedb4ff4969 visibility candidate is withdrawn. Client 0b771120bb2a878c012512b685208124c2b4263b is unchanged. Neither is a new substantive deliverable in this affected review.

## Read-authority assessment

At api/models/security_advisory.rb:28, visible_to retains all records for administrators and selects only published state for everyone else. This is the existing shared policy owner; no parallel policy framework is added.

Checked actual consumers:

- SecurityAdvisory Index and Show start with visible_to; all other filters intersect that relation. Counts use the same query. Its cursor lookup is independently scoped, so a hidden cursor returns an empty scope. The recent_since predicate cannot override the initial visibility scope.
- Nested node-status Index joins/scopes the parent; no separate node-status Show exposes a second unscoped read path.
- CVE and update Index/Show owners scope through the parent.
- Affected-user/VPS projection lists retain both parent visibility and their existing ownership/field restrictions.
- OutageSecurityAdvisory Index/Show retain both outage visibility and advisory visibility.

At plugins/outage_reports/api/resources/outage.rb:174, the reverse advisory filter now intersects the same parent scope through a link subquery. The outer query still begins with Outage.visible_to(current_user). This prevents a hidden advisory from selecting related outage rows and preserves administrator access. Selecting outage IDs through the subquery avoids duplicate outer rows and the old grouped-count Hash failure; total_count remains scalar for this filter. Other outage filters are unchanged.

The explicit reverse-filter scope is necessary with installed HaveAPI 0.32.1: resource-input authorize_record! checks Show authorization but does not execute its scoped prepare. Conversely, the installed ActiveRecord output resourcify path checks authorization and show_prepared?, which validates/prepares the target Show. Thus resource-input authorization was not mistaken for row visibility, and output includes use the scoped Show owner. Inspected the actual known resource/filter/include paths rather than proposing a broader framework audit.

No mutation, mail, revision, lock or projection-storage behavior changes in this delta. Direct retraction remains silent and preserves administrator history. Retained rows are hidden through read scopes rather than deleted. The entire PHP/CSS/locale runtime tree equals the prior reviewed49f5 source; B's webui patch is byte-equal to the preceding B patch. Legacy differences are tests/fixtures only. No frontend enforcement remains in the submitted correction.

The owning docs/security-advisories.md now states published-only public/member reads, admin-only draft/retracted relations and silent retention on retraction, consistent with the code.

## Evidence assessed and its limits

I inspected the actual added specs, browser regression/fixture diff and native focused results without executing tests.

The API coverage exercises anonymous/member/support/admin across published/draft/retracted originals, direct reads, actual wrapped state filters, counts, hidden cursors, populated CVE/update children and includes, nested node rows, owned projections and outage links/reverse filters. Positive published/admin cases and retained history/projection rows are checked alongside denials. Resource regressions use real retraction; the legacy fixture also publishes then silently retracts its report.

Initial exact-line full-mode run: six examples, four passed and two failed. One failure was a positional/keyword translation-Hash fixture error, corrected with explicit braces. The other exposed the grouped reverse-outage count500, corrected by the scoped subquery. The final affected full-mode recheck has two examples, zero failures/pending/outside-example errors; native duration537.967s. The core batch has five examples, zero failures/pending/outside-example errors; native duration602.778s. The four unchanged full-mode successes are retained separately, not represented as a fresh six-case pass. Earlier zero-example selector runs are incomplete tooling evidence and contribute no passing coverage.

Touched Ruby lint, Nixfmt/whitespace, pinned Node syntax and normal hooks passed according to the supplied receipts. The lock/source/input comparison was independently inspected. Hosted queued/in-progress results in the packet are pending evidence, not completed success. These focused checks do not replace full affected suites or real UI/server acceptance.

## Compatibility, recovery and remaining acceptance

This intentionally removes non-admin access to formerly public retracted reports, including old direct links, feeds/lists and related records. Public published and authorized administrator access remain supported; existing token scopes/ownership restrictions still apply.

No schema, stored format, daemon protocol, generated client or companion UI upgrade is required. Existing UIs consume the corrected server responses. Mixed old/new API instances cannot enforce the privacy contract consistently. Rollback is data-compatible but **privacy-reexposing**: restoring the old API makes retracted content public again. Recovery must preserve the visibility correction. Already delivered browser content or mail cannot be recalled; this accepted limit does not authorize UI cache redesign.

Residual checks remain:

- Full affected multi-file API coverage in full-plugin and core modes.
- Relevant native legacy browser scenario against the final source.
- Full strict KB contract check at exact4fd4 and its selected source/input graph.
- Authorized own-preview update followed by source/runtime proof and ordinary verified-TLS anonymous/member/support/admin checks for originals, related records and both unchanged UIs, including admin history and normal OAuth/published rendering.

The running preview still uses old API49f5, so it is not yet corrected. No new long acceptance or preview activation is established by this report. No source/session file was written and no test, build, fetch, deployment, integration, production or lifecycle action was performed by this reviewer.

Lead may proceed with the planned affected verification; any later substantive successor must be assessed under the mandatory review's affected-lane/narrow-fix rules. Integration and production remain separate authorization boundaries.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
