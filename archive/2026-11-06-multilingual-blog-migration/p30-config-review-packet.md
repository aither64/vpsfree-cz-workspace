# P30 committed CONFIG final review

User requests embedding/site settings declared in existing Discourse Nix config.
Completed independent CONFIG source deliverable: one file18+/0. BLOG metadata/counts
are separate pending source and are NOT being submitted as final in this review.

Session2026-11-06-multilingual-blog-migration; plan.md/state.md/design.md:4681.
CONFIG worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/vpsfree-cz-configuration.
Incremental9b0cf03eb51cac24efb1b763b4349fae7c8d704d..41ca287dc84d57e9ab3ee8ed970c84c389704aab,
tree6f810a49997278bc28c0b9363a25d846fbb696c8; clean/index empty, source frozen.
Full5941cdb3dda259e91c6a988a7dbf08c84700b326..41ca287d eight commits,23paths6407+/25-.
Exact full series, full diff and incremental in p30-config-source-proof.json links.
Lead matched proof SHAde10113d73ab0a8d3732ffa29a84f3edfeda431696fd2061dd670fcaadb3d9d4
and all13 linked sizes/hashes. Prior seven commits exact unchanged from P28 review.

Eleven ordinary services.discourse.siteSettings values in existing pinned upstream
categories: article selector, ordinary iframe origin/CSP policy, truncated/nonmarkdown
native import, imported topics unlisted until reply, no full app/canonical override,
blank extraction blacklist and embed_by_username reference existing configured admin.
No custom module/provisioner/DB reset/API or schema, pin, secret or workflow change.
Host/path/category/tags/blank-host-author rows remain operator UI work. User says
listed settings not touched; source is defaults and existing DB/UI values still win.
Do not infer live effective values/account existence from config. Both-blog shared
English forum source is being prepared in BLOG after later user steering; these
settings are language-neutral. BLOG embed stays disabled until later settled pilot.

One coherent settings commit includes fallback/extraction/visibility/framing policy
that together implements the requested native comment integration. No separable
input/generated update in the increment. Entire range contains one vpsfreeWeb update
stream307635a9->7fec3e3c at9b0, unchanged; no repeated update streams or new migrations.
Prior source/history reviews remain reusable only for unchanged bytes. Full-history
conclusions still required: DNS, publisher-free routing, authenticated delivery,
coexistence, static selection, retention, web pin and these forum defaults remain
supported boundaries. Actual deployed1649/cqjh and76d7/w3 retain ORIGINAL old SHAs,
not replayed P28 identities; old95b/native recovery refs/roots remain. The original
P28 history proof is linked; no new native/NAR/equivalence or literal-merged claim.
Existing schema2 publication/schema1 content-recovery compatibility is unchanged.

Quick checks: real pinned NixOS module scoped option evaluation + pinned Discourse
YAML exact11category/key/type checks, baseline sibling/admin/secret-path equality,
inherited force_https preserved, no secret read/output: PASS17.73s. This intentionally
omits unrelated site imports and does NOT replace full native generation. Nixfmt/
ordinary precommit+commit-msg PASS7.63s; width>72 advisory, all<=80. Initial wrapper
/usr/bin/time absent exit127 before checks preserved, corrected Bash time operation
passed once; no product failure/rerun. Evidence source scripts/results/logs linked.

Docs: reusable setup/precedence/host ownership belongs in BLOG docs/discussions.md,
whose current3c48 metadata commit has lead prose pass and will receive English-source
and counts updates. No CONFIG rollout/test receipts added; source settings self-contained
and upstream module documents defaults/override behavior. Operational record in session.

Overall risk HIGH conservatively: external public iframe/import policy, topic attribution
and persistent UI override/rollback behavior. Reviewer0 saved Sol/xhigh/read_only,
thread01a1b293-016d-7f41-95f0-b2c1da14ee3e verified current ready/review. Allfour lanes:
GENERAL, ARCHITECTURE, SCOPE, RISK. Read mandatory-change-review SKILL plus allfour
reference files/current CONFIG guidance; direct immutable review, no nested agents,
checks/eval/build/network/SSH/writes/runtime. Inspect exact pinned provider and current
consumer/source contract, do not rubber-stamp packet claims. Whole range/history,
repeated streams and migration conclusion required. Prompt findings for owner3 fixes.

No Discourse-only native build yet; accepted committed review is its release prerequisite.
No copy/dry/deploy/claim/default integration/cleanup authorized. User owns web.int later.
